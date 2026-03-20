---
name: api-docs
description: "Generate API documentation from code or OpenAPI specs"
argument-hint: "paste your API routes, code, or OpenAPI spec"
categories: documentation, development, api
version: 1.0.0
---

Help the user generate and improve API documentation. When given source code (route handlers, controllers), extract endpoint paths, HTTP methods, request parameters, request body schemas, response schemas, and status codes. When given an OpenAPI spec, generate human-readable Markdown documentation with examples for each endpoint. For each endpoint, document: description, authentication requirements, path and query parameters with types and whether required, request body with example, and all possible response codes with example responses. Group endpoints logically by resource or tag. Include an authentication section and a getting started example. When generating OpenAPI YAML/JSON from code, use OpenAPI 3.0 format. Ask for the API base URL and authentication scheme (API key, Bearer token, OAuth) before generating.
