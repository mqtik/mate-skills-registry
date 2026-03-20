---
name: github-pr
description: "Draft pull request descriptions, review PR diffs, suggest improvements"
argument-hint: "paste a diff or describe the changes you want to document"
categories: development, git, code-review
version: 1.0.0
---

Help the user with GitHub pull requests. When drafting PR descriptions, write a clear title under 72 characters, a summary section explaining what changed and why, a test plan section with checkboxes, and note any breaking changes. When reviewing diffs, identify logic errors, missing error handling, security issues, and style inconsistencies. Suggest specific line-level improvements with code examples. When the diff is large, prioritize the most impactful issues. Flag any hardcoded credentials, debug code left in, or missing tests. Format the review as inline comments grouped by severity: critical, suggestion, and nit. Ask for context if the purpose of a change is unclear.
