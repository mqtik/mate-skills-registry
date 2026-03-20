---
name: performance-audit
description: "Audit web application performance and suggest optimizations"
argument-hint: "paste your code, config, or describe the performance issue"
categories: audit, web, development
version: 1.0.0
---

Audit the provided code or configuration for web performance issues. Check for render-blocking resources: synchronous scripts in the head, undeferred CSS. Check for unoptimized assets: uncompressed images, missing WebP alternatives, fonts loaded without font-display: swap. Check for JavaScript performance: large bundle sizes, no code splitting, missing lazy loading for off-screen content. Check for caching: missing cache-control headers, no service worker for static assets. Check for network efficiency: unminified assets, no HTTP/2 or CDN usage. Check for React/Vue/Angular specific issues: unnecessary re-renders, missing memoization, large dependency imports. For each issue, estimate the impact (High/Medium/Low) and provide a specific fix. Ask for the framework and build tool to give targeted recommendations.
