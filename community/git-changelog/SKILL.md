---
name: git-changelog
description: "Generate changelogs from git commit history"
argument-hint: "paste your git log output or specify the version range"
categories: development, git, documentation
version: 1.0.0
---

Help the user generate changelogs from git commit history. When given raw git log output, parse commit messages and categorize them into Added, Changed, Fixed, Removed, Security, and Deprecated sections following the Keep a Changelog format. Group commits by version tag or date range. Rewrite cryptic commit messages into clear, user-facing language — focus on what changed for users, not implementation details. Ignore merge commits, version bumps, and lint/formatting-only changes unless they affect behavior. When multiple commits address the same feature, consolidate them into a single entry. Ask for the version number and release date if not provided. Output valid Markdown ready to prepend to CHANGELOG.md.
