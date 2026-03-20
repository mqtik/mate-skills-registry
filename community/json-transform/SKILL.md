---
name: json-transform
description: "Transform, filter, merge, and validate JSON data"
argument-hint: "paste your JSON and describe what transformation you need"
categories: data, text-processing, development
version: 1.0.0
---

Help the user work with JSON data. When transforming JSON, apply the requested reshaping — rename keys, flatten nested objects, pick or omit fields, or convert arrays to maps. When filtering, extract items matching the user's criteria and explain the filter logic. When merging multiple JSON objects or arrays, define the merge strategy (deep merge, array concatenation, deduplication) and ask if unclear. When validating JSON, check syntax first, then validate against a schema if provided. Generate jq commands for operations the user wants to repeat in scripts. When the JSON is large, summarize the structure first before transforming. Output transformed JSON in properly formatted, indented form. Warn if the transformation loses data.
