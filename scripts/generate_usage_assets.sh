#!/bin/sh
#
# Generate release asset files for Self-Hosted AI Stack usage counters.

set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
MANIFEST="$ROOT_DIR/manifests/usage-v1.txt"
DIST_DIR="$ROOT_DIR/dist"
CONTENT="Usage counter for Self-Hosted AI Stack. See https://github.com/hwdsl2/self-hosted-ai-stack. Do not download manually."

mkdir -p "$DIST_DIR"

seen_file=$(mktemp)
trap 'rm -f "$seen_file"' EXIT HUP INT TERM

while IFS= read -r asset || [ -n "$asset" ]; do
  [ -n "$asset" ] || continue
  case "$asset" in
    usage-v1-*) ;;
    *) echo "Invalid asset name: $asset" >&2; exit 1 ;;
  esac
  if grep -Fxq "$asset" "$seen_file"; then
    echo "Duplicate asset name: $asset" >&2
    exit 1
  fi
  printf '%s\n' "$asset" >> "$seen_file"
  printf '%s\n' "$CONTENT" > "$DIST_DIR/$asset"
done < "$MANIFEST"

echo "Generated $(wc -l < "$seen_file" | tr -d ' ') usage counter assets in $DIST_DIR."
