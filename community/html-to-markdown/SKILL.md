---
name: html-to-markdown
description: "Convert HTML pages to clean Markdown"
argument-hint: "paste the HTML you want to convert to Markdown"
categories: data, text-processing, files
version: 1.0.0
---

Help the user convert HTML to clean Markdown. When converting, strip navigation bars, footers, sidebars, cookie banners, and advertisements — focus on the main content. Convert headings, paragraphs, lists, links, images, tables, and code blocks to their Markdown equivalents. For tables, use standard GFM (GitHub Flavored Markdown) table syntax. For links, preserve href and alt text. Remove inline styles, class attributes, and empty tags. When the HTML contains nested elements that don't translate cleanly to Markdown, use the simplest readable approximation. Preserve code blocks with language hints from class attributes when present. If the input is a full page, ask the user if they want the full content or just the main article body.
