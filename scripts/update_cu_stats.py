#!/usr/bin/env python3
"""Update public component usage count snapshots from GitHub release assets."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OWNER = "hwdsl2"
DEFAULT_REPO = "ai-stack-extras"
DEFAULT_TAG = "v1.0.0"
CUDA_CAPABLE_COMPONENTS = {"docling", "kokoro", "ollama", "whisper", "whisperlive"}


def read_manifest(path: Path) -> list[str]:
    names = [line.strip() for line in path.read_text().splitlines() if line.strip()]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        raise SystemExit(f"Duplicate manifest assets: {', '.join(duplicates)}")
    for name in names:
        if not name.startswith("cu-v1-"):
            raise SystemExit(f"Invalid manifest asset name: {name}")
    return names


def github_json(url: str, token: str | None) -> object:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "ai-stack-extras-component-usage-stats",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def release_by_tag(owner: str, repo: str, tag: str, token: str | None) -> dict:
    encoded_tag = urllib.parse.quote(tag, safe="")
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/tags/{encoded_tag}"
    data = github_json(url, token)
    if not isinstance(data, dict) or "id" not in data:
        raise SystemExit("Unexpected release response from GitHub.")
    return data


def release_assets(owner: str, repo: str, release_id: int, token: str | None) -> list[dict]:
    assets: list[dict] = []
    page = 1
    while True:
        url = (
            f"https://api.github.com/repos/{owner}/{repo}/releases/"
            f"{release_id}/assets?per_page=100&page={page}"
        )
        data = github_json(url, token)
        if not isinstance(data, list):
            raise SystemExit("Unexpected assets response from GitHub.")
        assets.extend(data)
        if len(data) < 100:
            return assets
        page += 1


def split_cu_name(name: str) -> dict[str, str]:
    parts = name.split("-")
    if len(parts) != 6 or parts[:2] != ["cu", "v1"]:
        return {"kind": "unknown"}
    return {
        "kind": "component",
        "component": parts[2],
        "action": parts[3],
        "image_variant": parts[4],
        "arch": parts[5],
    }


def aggregate(counts: dict[str, int]) -> dict:
    totals = {
        "all": sum(counts.values()),
        "deploy": 0,
        "upgrade": 0,
    }
    by_component: dict[str, int] = {}
    by_image_variant: dict[str, int] = {}
    by_image_variant_cuda_capable: dict[str, int] = {}
    by_arch: dict[str, int] = {}

    for name, value in counts.items():
        parsed = split_cu_name(name)
        if parsed["kind"] != "component":
            continue
        totals[parsed["action"]] += value
        for key, target in (
            ("component", by_component),
            ("image_variant", by_image_variant),
            ("arch", by_arch),
        ):
            label = parsed[key]
            target[label] = target.get(label, 0) + value
        if parsed["component"] in CUDA_CAPABLE_COMPONENTS:
            label = parsed["image_variant"]
            by_image_variant_cuda_capable[label] = by_image_variant_cuda_capable.get(label, 0) + value

    return {
        "totals": totals,
        "by_component": dict(sorted(by_component.items())),
        "by_image_variant": dict(sorted(by_image_variant.items())),
        "by_image_variant_cuda_capable": dict(sorted(by_image_variant_cuda_capable.items())),
        "by_arch": dict(sorted(by_arch.items())),
    }


def render_markdown(generated_at: str, counts: dict[str, int], summary: dict) -> str:
    lines = [
        "# Component Usage Counts",
        "",
        f"Last updated: `{generated_at}`",
        "",
        "Counts are approximate GitHub release asset download counts, not unique users or active installs.",
        "The `cpu`/`cuda` dimension is the Docker image variant, not measured runtime hardware use.",
        "The CUDA-capable image variant table excludes CPU-only components: embeddings, litellm, and mcp.",
        "",
        "## Totals",
        "",
        "| Metric | Count |",
        "|---|---:|",
    ]
    for key, value in summary["totals"].items():
        lines.append(f"| {key} | {value} |")
    for title, data_key in (
        ("By Component", "by_component"),
        ("By Image Variant", "by_image_variant"),
        ("By Image Variant (CUDA-Capable Components Only)", "by_image_variant_cuda_capable"),
        ("By Architecture", "by_arch"),
    ):
        lines.extend(["", f"## {title}", "", "| Name | Count |", "|---|---:|"])
        for key, value in summary[data_key].items():
            lines.append(f"| {key} | {value} |")
    lines.extend(["", "## Raw Counters", "", "| Asset | Count |", "|---|---:|"])
    for name in counts:
        lines.append(f"| `{name}` | {counts[name]} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--owner", default=os.environ.get("AI_STACK_EXTRAS_OWNER", DEFAULT_OWNER))
    parser.add_argument("--repo", default=os.environ.get("AI_STACK_EXTRAS_REPO", DEFAULT_REPO))
    parser.add_argument("--tag", default=os.environ.get("AI_STACK_EXTRAS_TAG", DEFAULT_TAG))
    parser.add_argument("--manifest", type=Path, default=ROOT / "manifests" / "cu-v1.txt")
    parser.add_argument("--stats-dir", type=Path, default=ROOT / "stats")
    parser.add_argument("--token", default=os.environ.get("GITHUB_TOKEN"))
    args = parser.parse_args()

    manifest = read_manifest(args.manifest)
    release = release_by_tag(args.owner, args.repo, args.tag, args.token)
    assets = release_assets(args.owner, args.repo, int(release["id"]), args.token)
    by_name = {asset["name"]: asset for asset in assets if isinstance(asset, dict) and "name" in asset}

    missing = [name for name in manifest if name not in by_name]
    if missing:
        raise SystemExit("Missing release assets: " + ", ".join(missing))

    extras = sorted(name for name in by_name if name.startswith("cu-v1-") and name not in manifest)
    if extras:
        print("Warning: unexpected component usage assets: " + ", ".join(extras), file=sys.stderr)

    counts = {name: int(by_name[name].get("download_count", 0)) for name in manifest}
    generated_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    summary = aggregate(counts)

    args.stats_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.stats_dir / "cu-v1.json"
    md_path = args.stats_dir / "cu-v1.md"

    payload = {
        "generated_at": generated_at,
        "owner": args.owner,
        "repo": args.repo,
        "tag": args.tag,
        "release_id": release["id"],
        "counts": counts,
        **summary,
    }

    old_json = json.loads(json_path.read_text()) if json_path.exists() and json_path.read_text().strip() else None
    old_counts = old_json.get("counts") if isinstance(old_json, dict) else None
    changed_counts = old_counts != counts
    changed_summary = not isinstance(old_json, dict) or any(old_json.get(key) != value for key, value in summary.items())

    if changed_counts or changed_summary:
        json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        md_path.write_text(render_markdown(generated_at, counts, summary))
        print("Component usage stats updated.")
    else:
        print("Component usage counts unchanged; no files updated.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except urllib.error.HTTPError as exc:
        print(f"GitHub API error: {exc.code} {exc.reason}", file=sys.stderr)
        raise
