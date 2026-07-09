#!/bin/sh
#
# Validate the component usage counter manifest.

set -eu

SCRIPT_DIR=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
ROOT_DIR=$(CDPATH='' cd -- "$SCRIPT_DIR/.." && pwd)
MANIFEST="$ROOT_DIR/manifests/cu-v1.txt"

EXPECTED_COUNT=78

# Accepted component usage asset names follow:
#   cu-v1-<component>-<action>-<image_variant>-<arch>
# where:
#   component in whisper kokoro docling mcp embeddings litellm ollama whisperlive
#   action    in deploy upgrade
#   image_variant in cpu cuda
#   arch      in amd64 arm64 other
ASSET_RE='^cu-v1-(whisper|kokoro|docling|mcp|embeddings|litellm|ollama|whisperlive)-(deploy|upgrade)-(cpu|cuda)-(amd64|arm64|other)$'

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
  echo "Expected $EXPECTED_COUNT component usage assets, found $count." >&2
  exit 1
fi

echo "Component usage manifest OK ($count assets)."
