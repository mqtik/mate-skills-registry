#!/usr/bin/env python3
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def shallow_clone(repo: str, dest: str) -> bool:
    result = subprocess.run(
        ["git", "clone", "--depth", "1", f"https://github.com/{repo}.git", dest],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def parse_frontmatter(content: str) -> dict | None:
    parts = content.split("---")
    if len(parts) < 3:
        return None
    fm = parts[1].strip()
    fields = {}
    for line in fm.split("\n"):
        line = line.strip()
        match = re.match(r'^([\w-]+):\s*(.+)$', line)
        if match:
            key, val = match.group(1), match.group(2).strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            elif val.startswith("'") and val.endswith("'"):
                val = val[1:-1]
            fields[key] = val
    return fields if fields.get("name") else None


def scrape_skills_repo(clone_dir: str) -> list[dict]:
    skills_dir = Path(clone_dir) / "skills"
    if not skills_dir.is_dir():
        return []
    entries = []
    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        if not fm:
            continue
        entries.append({
            "name": fm["name"],
            "description": fm.get("description", ""),
            "version": fm.get("version"),
            "categories": [c.strip() for c in fm.get("categories", "").split(",") if c.strip()]
                          or _infer_categories(fm.get("description", "")),
            "downloadUrl": f"https://raw.githubusercontent.com/anthropics/skills/main/skills/{skill_dir.name}/",
            "source": "anthropics/skills",
            "author": fm.get("author", "Anthropic"),
        })
    return entries


def scrape_plugins_repo(clone_dir: str) -> list[dict]:
    entries = []
    for top_dir in ["plugins", "external_plugins"]:
        base = Path(clone_dir) / top_dir
        if not base.is_dir():
            continue
        for plugin_dir in sorted(base.iterdir()):
            if not plugin_dir.is_dir():
                continue

            author = "Anthropic"
            plugin_json = plugin_dir / "plugin.json"
            if plugin_json.exists():
                try:
                    pj = json.loads(plugin_json.read_text(encoding="utf-8"))
                    author = pj.get("author", author)
                except (json.JSONDecodeError, KeyError):
                    pass

            skills_dir = plugin_dir / "skills"
            if not skills_dir.is_dir():
                continue
            for skill_dir in sorted(skills_dir.iterdir()):
                if not skill_dir.is_dir():
                    continue
                skill_md = skill_dir / "SKILL.md"
                if not skill_md.exists():
                    continue
                fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
                if not fm:
                    continue
                entries.append({
                    "name": fm["name"],
                    "description": fm.get("description", ""),
                    "version": fm.get("version"),
                    "categories": [c.strip() for c in fm.get("categories", "").split(",") if c.strip()]
                                  or _infer_categories(fm.get("description", "")),
                    "downloadUrl": f"https://raw.githubusercontent.com/anthropics/claude-plugins-official/main/{top_dir}/{plugin_dir.name}/skills/{skill_dir.name}/",
                    "source": "anthropics/claude-plugins-official",
                    "author": author,
                })
    return entries


def _infer_categories(desc: str) -> list[str]:
    desc_lower = desc.lower()
    cats = []
    if any(w in desc_lower for w in ["code", "develop", "build", "api", "sdk", "frontend", "web"]):
        cats.append("development")
    if any(w in desc_lower for w in ["design", "art", "visual", "style", "theme"]):
        cats.append("design")
    if any(w in desc_lower for w in ["document", "pdf", "docx", "pptx", "xlsx", "spreadsheet"]):
        cats.append("documents")
    if any(w in desc_lower for w in ["write", "comms", "report"]):
        cats.append("writing")
    if any(w in desc_lower for w in ["test", "playwright", "eval"]):
        cats.append("testing")
    if any(w in desc_lower for w in ["workflow", "automat", "productivity"]):
        cats.append("productivity")
    if any(w in desc_lower for w in ["slack", "discord", "telegram", "message"]):
        cats.append("messaging")
    return cats or ["general"]


def deduplicate(primary: list[dict], secondary: list[dict]) -> list[dict]:
    seen = set()
    result = []
    for entry in primary:
        if entry["name"] not in seen:
            seen.add(entry["name"])
            result.append(entry)
    for entry in secondary:
        if entry["name"] not in seen:
            seen.add(entry["name"])
            result.append(entry)
    return result


def main():
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    output_file = repo_root / "index.json"

    with tempfile.TemporaryDirectory() as tmpdir:
        skills_entries = []
        plugins_entries = []

        skills_clone = os.path.join(tmpdir, "skills")
        if shallow_clone("anthropics/skills", skills_clone):
            skills_entries = scrape_skills_repo(skills_clone)
            print(f"Found {len(skills_entries)} skills from anthropics/skills")
        else:
            print("Warning: Could not clone anthropics/skills", file=sys.stderr)

        plugins_clone = os.path.join(tmpdir, "plugins")
        if shallow_clone("anthropics/claude-plugins-official", plugins_clone):
            plugins_entries = scrape_plugins_repo(plugins_clone)
            print(f"Found {len(plugins_entries)} skills from anthropics/claude-plugins-official")
        else:
            print("Warning: Could not clone anthropics/claude-plugins-official", file=sys.stderr)

    all_skills = deduplicate(skills_entries, plugins_entries)
    print(f"Total unique skills: {len(all_skills)}")

    new_content = json.dumps({"skills": all_skills}, indent=2, ensure_ascii=False)

    if output_file.exists():
        existing = output_file.read_text(encoding="utf-8")
        if existing.strip() == new_content.strip():
            print("No changes detected, skipping write")
            return

    output_file.write_text(new_content + "\n", encoding="utf-8")
    print(f"Wrote {output_file}")


if __name__ == "__main__":
    main()
