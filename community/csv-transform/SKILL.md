---
name: csv-transform
description: "Parse, transform, filter, and convert CSV data"
argument-hint: "paste your CSV data or describe the transformation you need"
categories: data, text-processing, files
version: 1.0.0
---

Help the user work with CSV data. When parsing CSV, identify the delimiter (comma, semicolon, tab), detect headers, and summarize the column names and row count. When transforming, rename columns, reorder, add computed columns, or filter rows based on conditions. When cleaning data, identify empty cells, inconsistent formats in date or numeric columns, and duplicate rows. When converting, output to JSON, Markdown table, or SQL INSERT statements as needed. When the user needs to process CSV in code, generate a Python (pandas or csv module) or JavaScript snippet. Handle quoted fields and escaped delimiters correctly. For large files, suggest streaming approaches. Ask about encoding (UTF-8, Latin-1) if special characters are present.
