#!/usr/bin/env python3
"""Validate Founder's Errata entries.

Enforces the rules in the build specification:
  1. Every entry in entries/ has the three required headings, each with non-empty content.
  2. Filenames match YYYY-MM-DD-NNNN-kebab-slug.md.
  3. No historical entry has been modified on this branch relative to main, except
     for changes isolated to the superseded_by frontmatter field.
  4. No entry has been deleted relative to main.

Zero external dependencies. Python 3 standard library only.
Run from the repository root:  python3 scripts/validate.py
Exit status: 0 on success, 1 on any validation failure.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ENTRIES_DIR = Path("entries")
FILENAME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$")
REQUIRED_HEADINGS = ("## Prior Position", "## Current Position", "## Causal Update")

errors: list[str] = []


def parse_frontmatter(text: str) -> tuple[dict[str, str] | None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    block = text[4:end]
    body = text[end + len("\n---\n"):]
    fm: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip()
    return fm, body


def section_content(body: str, heading: str) -> str | None:
    lines = body.splitlines()
    target = heading.strip()
    start = -1
    for i, line in enumerate(lines):
        if line.strip() == target:
            start = i
            break
    if start < 0:
        return None
    collected: list[str] = []
    for line in lines[start + 1:]:
        if line.startswith("## ") or line.startswith("# "):
            break
        collected.append(line)
    return "\n".join(collected).strip()


def validate_file(path: Path) -> None:
    name = path.name
    if not FILENAME_RE.match(name):
        errors.append(f"{name}: filename does not match YYYY-MM-DD-NNNN-kebab-slug.md")

    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    if fm is None:
        errors.append(f"{name}: missing or malformed YAML frontmatter")
        return

    for key in ("id", "date"):
        if not fm.get(key):
            errors.append(f"{name}: frontmatter field '{key}' is empty")

    for heading in REQUIRED_HEADINGS:
        content = section_content(body, heading)
        if content is None:
            errors.append(f"{name}: missing heading '{heading}'")
        elif not content:
            errors.append(f"{name}: section '{heading}' is empty")
        elif content.startswith("[") and content.endswith("]"):
            errors.append(f"{name}: section '{heading}' still contains the template placeholder")


def git(*args: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", *args], capture_output=True, text=True, check=True
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return result.stdout


def check_append_only() -> None:
    """Detect modifications or deletions of historical entries vs main branch."""
    if git("rev-parse", "--is-inside-work-tree") is None:
        return  # not a git repo yet; nothing to compare against

    if git("rev-parse", "--verify", "main") is None:
        return  # no main branch yet (pre-initial-commit); skip

    base = git("merge-base", "HEAD", "main")
    if not base:
        return
    base = base.strip()

    diff = git("diff", "--name-status", base, "HEAD", "--", "entries/")
    if diff is None:
        return

    for line in diff.splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        status, fname = parts[0], parts[1]

        if status == "D":
            errors.append(f"{fname}: entry deleted (entries are append-only)")
            continue

        if status.startswith("R"):
            errors.append(f"{fname}: entry renamed (entries are append-only)")
            continue

        if status == "M":
            file_diff = git("diff", base, "HEAD", "--", fname)
            if file_diff is None:
                errors.append(f"{fname}: entry modified (could not inspect diff)")
                continue
            offending = False
            for dl in file_diff.splitlines():
                if dl.startswith("+++") or dl.startswith("---") or dl.startswith("@@"):
                    continue
                if not (dl.startswith("+") or dl.startswith("-")):
                    continue
                changed = dl[1:].strip()
                if not changed:
                    continue
                if not changed.startswith("superseded_by:"):
                    offending = True
                    break
            if offending:
                errors.append(
                    f"{fname}: historical entry modified outside of the superseded_by frontmatter field"
                )


def main() -> int:
    if not ENTRIES_DIR.exists():
        print("error: entries/ directory not found (run from repo root)", file=sys.stderr)
        return 1

    entry_files = sorted(p for p in ENTRIES_DIR.iterdir() if p.is_file() and p.suffix == ".md")
    for path in entry_files:
        validate_file(path)

    check_append_only()

    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        return 1

    print(f"ok: {len(entry_files)} entr{'y' if len(entry_files) == 1 else 'ies'} validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
