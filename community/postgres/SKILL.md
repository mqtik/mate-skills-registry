---
name: postgres
description: "Write optimized PostgreSQL queries, migrations, and schema designs"
argument-hint: "describe the query, schema, or migration you need"
categories: development, database, sql
version: 1.0.0
---

Help the user work with PostgreSQL. When writing queries, use CTEs for readability, choose appropriate JOIN types, and add EXPLAIN ANALYZE guidance when performance matters. When designing schemas, choose correct column types, define constraints (NOT NULL, UNIQUE, CHECK, FOREIGN KEY), and suggest indexes based on query patterns. When writing migrations, make them reversible with both up and down steps, and never drop columns without a deprecation period in production. Flag N+1 query patterns, missing indexes on foreign keys, and overly broad SELECT *. For full-text search, use tsvector and tsquery. Ask for the PostgreSQL version and ORM (if any) when generating migration files.
