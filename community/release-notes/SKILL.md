---
name: release-notes
description: "Draft release notes from commits and PRs"
argument-hint: "paste commits, PR titles, or describe what changed in this release"
categories: documentation, development, git
version: 1.0.0
---

Help the user draft release notes for a software release. Transform raw commit messages and PR titles into polished, user-facing release notes. Open with a brief summary sentence describing the theme of the release. Group changes into clear sections: New Features, Improvements, Bug Fixes, and Breaking Changes. Write each item from the user's perspective, focusing on the benefit rather than the implementation. Highlight breaking changes prominently at the top with clear migration instructions. Include upgrade instructions if dependencies or configuration changed. Omit internal refactors, dependency bumps, and test changes unless they affect users. Ask for the version number, release date, and whether this is a major, minor, or patch release to set the appropriate tone and emphasis.
