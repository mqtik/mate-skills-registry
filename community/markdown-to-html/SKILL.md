---
name: markdown-to-html
description: "Convert Markdown to styled HTML with custom themes"
argument-hint: "paste your Markdown content or describe the styling you want"
categories: data, text-processing, frontend
version: 1.0.0
---

Help the user convert Markdown to HTML. When converting, produce valid semantic HTML with appropriate tags: h1-h6 for headings, p for paragraphs, ul/ol/li for lists, blockquote, pre/code for code blocks, and table/thead/tbody for tables. When the user requests styling, generate an embedded CSS style block with clean typography — readable font stack, appropriate line height, and a max-width container. Support theme requests: light, dark, or GitHub-style. For code blocks, add a language class for syntax highlighting library compatibility (highlight.js, Prism). When converting entire documents, include a proper HTML5 boilerplate with meta charset and viewport. Ask if the user needs self-contained HTML (embedded CSS) or a separate stylesheet.
