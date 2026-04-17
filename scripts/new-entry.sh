#!/usr/bin/env bash
# Create a new errata entry with correct filename + pre-filled frontmatter.
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
entries_dir="$repo_root/entries"
template="$repo_root/templates/entry-template.md"

if [[ ! -f "$template" ]]; then
  echo "error: template not found at $template" >&2
  exit 1
fi

read -rp "Slug (3-6 words, kebab-case, lowercase alphanumeric): " slug
if [[ -z "${slug// /}" ]]; then
  echo "error: slug is required" >&2
  exit 1
fi
if [[ ! "$slug" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "error: slug must be lowercase kebab-case (e.g. supabase-stack-assumption)" >&2
  exit 1
fi

date_str="$(date +%Y-%m-%d)"

# Next sequence number for today.
count=0
for f in "$entries_dir"/"${date_str}"-*.md; do
  [[ -e "$f" ]] && count=$((count + 1))
done
seq="$(printf "%04d" "$((count + 1))")"

filename="${date_str}-${seq}-${slug}.md"
target="$entries_dir/$filename"

if [[ -e "$target" ]]; then
  echo "error: $target already exists" >&2
  exit 1
fi

cp "$template" "$target"

# Pre-fill id and date. Portable sed across macOS/BSD and GNU.
if sed --version >/dev/null 2>&1; then
  sed -i -e "s/^id: NNNN\$/id: ${seq}/" -e "s/^date: YYYY-MM-DD\$/date: ${date_str}/" "$target"
else
  sed -i '' -e "s/^id: NNNN\$/id: ${seq}/" -e "s/^date: YYYY-MM-DD\$/date: ${date_str}/" "$target"
fi

echo "created: entries/$filename"
"${EDITOR:-vi}" "$target"
