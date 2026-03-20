---
name: changelog
description: "Generate and maintain CHANGELOG.md following Keep a Changelog format"
argument-hint: "describe the changes to add or paste content to update"
categories: documentation, development, git
version: 1.0.0
---

Help the user create and maintain a CHANGELOG.md following the Keep a Changelog format (keepachangelog.com). Structure the file with an Unreleased section at the top, followed by version sections in reverse chronological order. Each version section must include the version number, release date in ISO 8601 format (YYYY-MM-DD), and changes grouped under: Added, Changed, Deprecated, Removed, Fixed, and Security. Only include sections that have entries. When adding new entries, place them under Unreleased. When cutting a release, move Unreleased entries to a new version section. Write entries from the user's perspective — what changed, not how. Keep entries concise, one line per change. Ask for the version number and release date when preparing a new release section.
