---
name: translate
description: "Translate text between languages preserving formatting"
argument-hint: "paste the text to translate and specify the target language"
categories: data, text-processing, productivity
version: 1.0.0
---

Translate the provided text accurately into the requested target language. Preserve all original formatting including Markdown syntax, HTML tags, code blocks, bullet points, and line breaks — translate only the human-readable text content. Match the tone and register of the source: formal documents stay formal, casual messages stay casual. When translating technical content, use domain-appropriate terminology in the target language. When a phrase has no direct translation, provide the closest equivalent and note the nuance in parentheses. For UI strings, keep translations concise to fit UI constraints. If the source language is ambiguous, identify the detected language before translating. Ask the user to specify formal or informal register for languages that distinguish them (e.g., French tu/vous, Spanish tú/usted).
