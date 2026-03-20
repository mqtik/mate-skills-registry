---
name: dependency-audit
description: "Audit project dependencies for outdated packages and vulnerabilities"
argument-hint: "paste your package.json, requirements.txt, Gemfile, or pubspec.yaml"
categories: audit, security, development
version: 1.0.0
---

Audit the provided dependency file for outdated packages and known vulnerabilities. Identify the package manager from the file format (npm/yarn, pip, bundler, pub, cargo, go.mod). For each dependency, flag packages with known CVEs, packages that are significantly behind the latest version, and packages that have been deprecated or abandoned. Group findings by severity: Critical (active CVE), High (major version behind with security fixes), Medium (outdated but no known CVE), and Low (minor version behind). For each critical or high finding, provide the safe version to upgrade to and note any breaking changes in the upgrade path. Suggest running the appropriate audit command (npm audit, pip-audit, bundle audit) for a complete programmatic scan. Ask if the user wants upgrade commands generated for the flagged packages.
