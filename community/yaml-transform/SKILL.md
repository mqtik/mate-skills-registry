---
name: yaml-transform
description: "Parse, transform, validate, and convert YAML files"
argument-hint: "paste your YAML or describe the transformation you need"
categories: data, text-processing, devops
version: 1.0.0
---

Help the user work with YAML files. When parsing YAML, identify the structure and summarize top-level keys and their types. When transforming, apply key renames, value substitutions, additions, or deletions as requested. When validating, check for syntax errors, duplicate keys, incorrect indentation (tabs vs spaces), and type mismatches against a schema if provided. When converting to JSON, maintain all types correctly including booleans, nulls, and multi-line strings. When converting from JSON to YAML, use block style for nested objects and sequences for readability. For Kubernetes or Docker Compose YAML, apply domain-specific validation. Flag anchors and aliases that may cause unexpected behavior. Output well-formatted YAML with consistent 2-space indentation.
