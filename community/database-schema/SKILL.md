---
name: database-schema
description: "Document database schemas with diagrams and descriptions"
argument-hint: "paste your schema SQL, ORM models, or describe the data model"
categories: documentation, database, development
version: 1.0.0
---

Help the user document their database schema. When given SQL CREATE TABLE statements or ORM model definitions, generate a structured document describing each table: its purpose, all columns with types, constraints, and descriptions, primary keys, foreign keys, and indexes. Generate a Mermaid erDiagram block showing the entity relationships with cardinality labels. For each relationship, explain the business logic it represents. Document any important constraints, triggers, or conventions (e.g., soft-delete patterns, audit timestamps). Group tables logically by domain or module. When schema purpose is unclear, infer from column names and ask for confirmation. Output the documentation in Markdown format, ready to include in a project wiki or README.
