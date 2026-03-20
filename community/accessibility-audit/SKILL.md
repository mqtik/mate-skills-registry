---
name: accessibility-audit
description: "Audit web pages for WCAG accessibility compliance"
argument-hint: "paste the HTML you want audited for accessibility"
categories: audit, web, accessibility
version: 1.0.0
---

Audit the provided HTML or component code for WCAG 2.1 accessibility compliance. Check for missing or inadequate alt text on images. Check that all interactive elements (buttons, links, inputs) have accessible names via aria-label, aria-labelledby, or visible text. Check heading hierarchy for logical document structure. Check color contrast ratios — flag combinations that fail the 4.5:1 ratio for normal text and 3:1 for large text. Check form inputs for associated labels. Check keyboard navigability: focus order, skip links, and focus trap in modals. Check ARIA usage for correctness — flag roles and attributes that are misused or redundant. For each issue, cite the specific WCAG success criterion (e.g., 1.1.1, 2.4.3) and its level (A, AA, AAA). Provide a concrete fix for each finding.
