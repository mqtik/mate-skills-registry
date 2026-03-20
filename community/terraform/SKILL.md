---
name: terraform
description: "Write Terraform modules, providers, and state management configs"
argument-hint: "describe the infrastructure you need to provision"
categories: development, devops, infrastructure
version: 1.0.0
---

Help the user write and organize Terraform configurations. When creating resources, use descriptive names, add required tags, and group related resources into modules. When writing modules, define clear variable types with descriptions and defaults, and expose outputs for values consumers need. For state management, recommend remote backends (S3+DynamoDB for AWS, GCS for GCP) with state locking enabled. When writing provider configurations, use version constraints and separate provider credentials from resource definitions. Flag common issues: hardcoded secrets in .tf files, missing lifecycle rules on stateful resources, and lack of depends_on for implicit dependencies. Always suggest running terraform plan before apply. Ask for the cloud provider and Terraform version before generating.
