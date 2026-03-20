---
name: erd-generator
description: "Generate Entity-Relationship Diagrams from database schemas"
argument-hint: "paste your schema SQL, ORM models, or describe your entities"
categories: documentation, database, design
version: 1.0.0
---

Generate Entity-Relationship Diagrams from the provided schema. When given SQL or ORM models, produce a Mermaid erDiagram with all entities, their attributes with data types, and relationships with correct cardinality notation (||--||, ||--o{, }o--o{). Label each relationship line with the relationship name. When given a description of the domain, infer the entities, attributes, and relationships, then confirm with the user before generating. Keep diagrams readable: omit internal audit columns (created_at, updated_at) unless the user wants them shown. For large schemas, offer to generate a high-level diagram showing only entities and relationships, plus detailed diagrams per domain. Also output the Mermaid code in a code block so the user can embed it in documentation.
