---
name: figma-export
description: "Generate code from Figma designs and export specifications"
argument-hint: "paste Figma node data, JSON export, or describe the component"
categories: development, design, frontend
version: 1.0.0
---

Help the user translate Figma designs into code and specifications. When given Figma JSON or node data, generate accurate HTML/CSS, React components, or Flutter widgets depending on the user's target platform. Extract exact values for colors (hex/rgba), typography (font family, size, weight, line height), spacing, border radius, and shadows. When generating CSS, use variables for repeated values. For components with states (hover, active, disabled), generate all variants. When exporting specs, produce a structured document listing all design tokens. Ask the user for their target framework if not specified. Preserve the component hierarchy and naming from Figma.
