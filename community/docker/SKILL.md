---
name: docker
description: "Write and optimize Dockerfiles, docker-compose configs"
argument-hint: "describe your app stack and what you need containerized"
categories: development, devops, infrastructure
version: 1.0.0
---

Help the user write and optimize Docker configurations. When writing Dockerfiles, use minimal base images, multi-stage builds to reduce final image size, and proper layer ordering to maximize cache efficiency. Always run as a non-root user, copy only necessary files, and set WORKDIR explicitly. When writing docker-compose files, define named volumes, health checks, restart policies, and environment variable references using .env files. For production configs, separate concerns into multiple compose files with override patterns. Flag common mistakes: ADD instead of COPY, installing dev dependencies in production, missing .dockerignore, and exposed debug ports. Ask for the language/framework and target environment before generating.
