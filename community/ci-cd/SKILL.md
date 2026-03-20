---
name: ci-cd
description: "Generate CI/CD pipelines for GitHub Actions, GitLab CI, Jenkins"
argument-hint: "describe your project stack and what the pipeline should do"
categories: development, devops, automation
version: 1.0.0
---

Help the user create CI/CD pipeline configurations. When generating pipelines, include stages for install, lint, test, build, and deploy — only include stages relevant to the project. Cache dependency directories to speed up runs. For GitHub Actions, use pinned action versions with SHA hashes for security, and store secrets in repository or environment secrets. For GitLab CI, define rules to avoid running all jobs on every push. For multi-environment deployments, require manual approval for production. Set up test result reporting and fail fast on critical checks. Flag pipelines that deploy without running tests, store credentials in plain text, or have no artifact retention policy. Ask for the platform, language, and deployment target before generating.
