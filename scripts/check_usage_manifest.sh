#!/bin/sh
#
# Validate the usage counter manifest.

set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
MANIFEST="$ROOT_DIR/manifests/usage-v1.txt"

EXPECTED_COUNT=126

# Accepted usage asset names follow one of two forms:
#   usage-v1-<action>-<variant>-<accel>-<arch>
#   usage-v1-feature-proxy-caddy-<variant>-<accel>-<arch>
# where:
#   action  ∈ deploy upgrade
#   variant ∈ full chat-ui chat-only rag-pipeline rag-pipeline-full \
#             ai-tools code-assistant voice-pipeline voice-chat   (for deploy/upgrade)
#             full chat-ui voice-chat                                (for feature-proxy-caddy)
#   accel   ∈ cpu cuda
#   arch    ∈ amd64 arm64 other
ASSET_RE='^usage-v1-((deploy|upgrade)-(full|chat-ui|chat-only|rag-pipeline|rag-pipeline-full|ai-tools|code-assistant|voice-pipeline|voice-chat)|feature-proxy-caddy-(full|chat-ui|voice-chat))-(cpu|cuda)-(amd64|arm64|other)$'

tmp_manifest=$(mktemp)
tmp_dupes=$(mktemp)
trap 'rm -f "$tmp_manifest" "$tmp_dupes"' EXIT HUP INT TERM

grep -v '^[[:space:]]*$' "$MANIFEST" > "$tmp_manifest"

sort "$tmp_manifest" | uniq -d > "$tmp_dupes"
if [ -s "$tmp_dupes" ]; then
  echo "Duplicate manifest assets:" >&2
  cat "$tmp_dupes" >&2
  exit 1
fi

bad=$(grep -Ev "$ASSET_RE" "$tmp_manifest" || true)
if [ -n "$bad" ]; then
  echo "Malformed manifest asset names:" >&2
  printf '%s\n' "$bad" >&2
  exit 1
fi

count=$(wc -l < "$tmp_manifest" | tr -d ' ')
if [ "$count" != "$EXPECTED_COUNT" ]; then
  echo "Expected $EXPECTED_COUNT usage assets, found $count." >&2
  exit 1
fi

echo "Usage manifest OK ($count assets)."