---
name: code-review
description: "Review code for bugs, security issues, and best practices"
argument-hint: "paste the code you want reviewed"
categories: development, code-quality, security
version: 1.0.0
---

Review the provided code thoroughly. Check for correctness issues: logic errors, off-by-one errors, null/undefined handling, and incorrect assumptions. Check for security issues: injection vulnerabilities, improper authentication checks, sensitive data in logs, and insecure dependencies. Check for performance issues: unnecessary loops, missing indexes, N+1 queries, and synchronous blocking calls. Check for maintainability: overly complex functions, missing error handling, unclear variable names, and duplicated logic. Structure the review with severity labels: Critical (must fix), Warning (should fix), and Suggestion (consider improving). Provide specific, actionable feedback with corrected code snippets where helpful. Ask for the language and framework if not obvious from the code.
