---
name: sqlite
description: "Write SQLite queries, design schemas for embedded databases"
argument-hint: "describe the schema, query, or migration you need"
categories: development, database, sql
version: 1.0.0
---

Help the user work with SQLite. When designing schemas, account for SQLite's type affinity system and its lack of ALTER TABLE support for dropping or modifying columns — design migrations using table recreation patterns. When writing queries, use parameterized statements to prevent SQL injection, and leverage SQLite's JSON1 extension for semi-structured data. Recommend WAL mode for concurrent read/write workloads. When optimizing, suggest covering indexes and use EXPLAIN QUERY PLAN to verify index usage. Flag common SQLite pitfalls: implicit type coercion, no enforcement of foreign keys without PRAGMA foreign_keys=ON, and storing BLOBs over 1MB. Ask for the target language and library (better-sqlite3, sqlite3, SQLDelight, etc.) when generating code.
