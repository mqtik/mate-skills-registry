---
name: svg-creator
description: "Create SVG graphics and icons from descriptions"
argument-hint: "describe the icon or graphic you want to create"
categories: media, design, frontend
version: 1.0.0
---

Create SVG graphics and icons from the user's description. Generate clean, valid SVG markup using semantic shapes (circle, rect, path, polygon, line) rather than overly complex paths where possible. Use a consistent viewBox (typically 24x24 for icons or 100x100 for illustrations) and omit fixed width/height attributes so the SVG scales with CSS. Apply fills and strokes using currentColor for icons that should inherit text color. Keep the SVG minimal: no unnecessary groups, no inline styles when attributes suffice, and no metadata. For icons, ensure the design is recognizable at small sizes (16x16). For illustrations, use a limited, harmonious color palette. Output the SVG in a code block. Ask for the intended size, color scheme, and style (outline, filled, duotone) before generating complex graphics.
