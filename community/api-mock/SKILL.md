---
name: api-mock
description: "Generate mock API servers and sample data from OpenAPI specs"
argument-hint: "paste your OpenAPI spec or describe the API endpoints you need"
categories: development, testing, api
version: 1.0.0
---

Help the user create mock API servers and realistic sample data. When given an OpenAPI spec, generate a working mock server config for tools like json-server, msw, or Prism — ask which the user prefers. Generate realistic sample data that matches the schema types and constraints: use plausible names, valid emails, realistic dates, and appropriate numeric ranges rather than generic placeholder values. When creating endpoints from a description, define request/response shapes, status codes, and error responses. Include at least one error scenario per endpoint. For collections, generate 5-20 sample records by default. Ask the user if they need specific edge cases covered in the mock data.
