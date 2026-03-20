---
name: security-audit
description: "Audit code and configs for security vulnerabilities"
argument-hint: "paste the code or configuration you want audited"
categories: audit, security, development
version: 1.0.0
---

Audit the provided code or configuration for security vulnerabilities. Check for injection vulnerabilities: SQL injection, command injection, LDAP injection, and XSS. Check authentication and authorization: hardcoded credentials, missing authentication checks, insecure session handling, and JWT misuse. Check sensitive data handling: secrets in source code, unencrypted storage of passwords, PII logged in plain text, and sensitive data in URLs. Check dependency issues: known-vulnerable library versions and use of deprecated cryptographic algorithms (MD5, SHA1, DES). Check configuration issues: debug mode enabled in production, permissive CORS, missing security headers, and exposed stack traces. Map each finding to a CWE identifier and CVSS severity. Provide a specific remediation for each issue. Never reproduce or suggest storing actual credentials.
