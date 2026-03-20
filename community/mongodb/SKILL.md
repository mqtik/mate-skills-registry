---
name: mongodb
description: "Write MongoDB queries, aggregation pipelines, and schema designs"
argument-hint: "describe the query, schema, or aggregation you need"
categories: development, database, nosql
version: 1.0.0
---

Help the user work with MongoDB. When writing queries, use projection to return only needed fields, add appropriate index hints, and avoid full collection scans. When designing schemas, choose between embedding and referencing based on access patterns and document size limits. When building aggregation pipelines, order stages to reduce documents early ($match and $limit before $lookup), and explain each stage's purpose through clear variable names. When creating indexes, recommend compound indexes based on the query filter and sort fields, and flag missing indexes on high-cardinality query fields. Warn against storing large arrays that grow without bound. Ask for the MongoDB version and driver language when generating code.
