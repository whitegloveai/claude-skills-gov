#!/usr/bin/env python3
"""Build catalog.json by scanning plugins/.

Single source of truth for the GovHub UI and any third-party indexer.
Re-runnable: drop new skills into plugins/<plugin>/skills/<skill>/SKILL.md
and re-run this script to regenerate catalog.json.

Usage:
    python3 scripts/build-catalog.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PLUGINS_DIR = REPO_ROOT / "plugins"
CATALOG_PATH = REPO_ROOT / "catalog.json"

MARKETPLACE = "whitegloveai-gov"
REPO_URL = "https://github.com/whitegloveai/claude-skills-gov"
INSTALL_MARKETPLACE = "/plugin marketplace add whitegloveai/claude-skills-gov"
VERSION = "1.0.0"

# Plugin order (matches kickoff priority) + display name + icon keyword.
# The frontend maps icon keywords to actual icons; this list is authoritative.
PLUGIN_META: list[tuple[str, str, str]] = [
    ("council-ops",          "Council Operations",      "council"),
    ("clerk",                "Clerk",                   "clerk"),
    ("finance",              "Finance",                 "finance"),
    ("communications",       "Communications",          "communications"),
    ("hr",                   "Human Resources",         "hr"),
    ("planning",             "Planning & Development",  "planning"),
    ("it",                   "Information Technology",  "it"),
    ("legal",                "Legal",                   "legal"),
    ("public-safety",        "Public Safety",           "public-safety"),
    ("public-works",         "Public Works",            "public-works"),
    ("economic-development", "Economic Development",    "economic-development"),
    ("parks-recreation",     "Parks & Recreation",      "parks"),
    ("library",              "Library",                 "library"),
]


def title_case(kebab: str) -> str:
    """Convert kebab-case to Title Case, with small-word lowercasing."""
    small = {"and", "or", "of", "the", "for", "to", "a", "an", "in", "on"}
    parts = kebab.split("-")
    result = []
    for i, word in enumerate(parts):
        if i > 0 and word.lower() in small:
            result.append(word.lower())
        else:
            result.append(word.capitalize())
    return " ".join(result)


def extract_plugin_description(readme_path: Path) -> str:
    """First non-empty paragraph after the first H1 in a plugin README."""
    if not readme_path.exists():
        return ""
    after_h1 = False
    paragraphs: list[str] = []
    current: list[str] = []
    for raw in readme_path.read_text().splitlines():
        line = raw.rstrip()
        if not after_h1:
            if line.startswith("# "):
                after_h1 = True
            continue
        if line.startswith("## "):
            break
        if not line.strip():
            if current:
                paragraphs.append(" ".join(current))
                current = []
        else:
            current.append(line.strip())
    if current:
        paragraphs.append(" ".join(current))
    return paragraphs[0] if paragraphs else ""


def parse_frontmatter_description(skill_md: Path) -> str:
    """Read the `description` field from SKILL.md YAML frontmatter."""
    text = skill_md.read_text()
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not fm_match:
        return ""
    fm = fm_match.group(1)
    # Match `description:` value, possibly continuing on indented continuation lines
    desc_match = re.search(
        r"^description:\s*(.+?)(?=^\w[\w-]*:|\Z)",
        fm,
        re.MULTILINE | re.DOTALL,
    )
    if not desc_match:
        return ""
    raw = desc_match.group(1).strip()
    # Collapse internal whitespace
    return re.sub(r"\s+", " ", raw)


def extract_when_to_use_bullets(skill_md: Path, max_bullets: int = 3) -> list[str]:
    """Pull the first N bullets from the ## When to Use section."""
    text = skill_md.read_text()
    section = re.search(
        r"^## When to Use\s*\n(.*?)^## ",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not section:
        return []
    bullets = re.findall(r"^- (.+?)$", section.group(1), re.MULTILINE)
    # Strip wrapping quotes that some skills use for spoken triggers
    cleaned = []
    for b in bullets[:max_bullets]:
        b = b.strip().strip('"').strip()
        # Keep them short; some skills have multi-line bullets
        if len(b) > 200:
            b = b[:197].rstrip() + "..."
        cleaned.append(b)
    return cleaned


def find_example_path(skill_dir: Path) -> str | None:
    """Return the first example file path relative to repo root."""
    examples_dir = skill_dir / "examples"
    if not examples_dir.exists():
        return None
    files = sorted(p for p in examples_dir.glob("*.md") if p.is_file())
    if not files:
        return None
    return str(files[0].relative_to(REPO_ROOT))


def build() -> dict:
    plugins_data = []
    total_skills = 0
    errors: list[str] = []

    for plugin_name, display_name, icon in PLUGIN_META:
        plugin_dir = PLUGINS_DIR / plugin_name
        if not plugin_dir.is_dir():
            errors.append(f"missing plugin dir: {plugin_dir}")
            continue

        plugin_desc = extract_plugin_description(plugin_dir / "README.md")
        skill_entries = []

        skills_dir = plugin_dir / "skills"
        if skills_dir.is_dir():
            for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
                skill_md = skill_dir / "SKILL.md"
                if not skill_md.exists():
                    errors.append(f"missing SKILL.md: {skill_md}")
                    continue
                skill_name = skill_dir.name
                skill_entries.append({
                    "name": skill_name,
                    "display_name": title_case(skill_name),
                    "description": parse_frontmatter_description(skill_md),
                    "when_to_use_summary": extract_when_to_use_bullets(skill_md),
                    "slash_command": f"/{skill_name}",
                    "skill_md_path": str(skill_md.relative_to(REPO_ROOT)),
                    "example_path": find_example_path(skill_dir),
                })

        plugins_data.append({
            "name": plugin_name,
            "display_name": display_name,
            "description": plugin_desc,
            "install_command": f"/plugin install {plugin_name}@{MARKETPLACE}",
            "skill_count": len(skill_entries),
            "icon": icon,
            "skills": skill_entries,
        })
        total_skills += len(skill_entries)

    if errors:
        print("Warnings:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)

    return {
        "marketplace": MARKETPLACE,
        "version": VERSION,
        "install_marketplace": INSTALL_MARKETPLACE,
        "repo_url": REPO_URL,
        "plugin_count": len(plugins_data),
        "skill_count": total_skills,
        "plugins": plugins_data,
    }


def main() -> int:
    catalog = build()
    CATALOG_PATH.write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {CATALOG_PATH.relative_to(REPO_ROOT)}")
    print(f"  {catalog['plugin_count']} plugins")
    print(f"  {catalog['skill_count']} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
