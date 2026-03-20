---
name: contacts
description: "Parse, merge, deduplicate, and export contact lists (vCard/CSV)"
argument-hint: "describe what you need to do with your contacts"
categories: productivity, data, files
version: 1.0.0
---

Help the user manage contact data. When parsing vCard (.vcf) files, extract name, email, phone, address, and organization fields and present them in a readable table. When parsing CSV contact exports, identify and map columns to standard fields. When deduplicating, identify exact duplicates and near-duplicates (same name, different email formats), and ask the user to confirm merges. When merging contacts, combine non-conflicting fields and flag conflicts for user resolution. When exporting, generate valid vCard 3.0 or 4.0 format, or produce a clean CSV with standard column headers. Handle international phone number formats and Unicode names correctly.
