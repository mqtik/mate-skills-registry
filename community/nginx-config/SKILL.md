---
name: nginx-config
description: "Generate and optimize nginx configuration files"
argument-hint: "describe your web server setup or what you need nginx to do"
categories: development, devops, infrastructure
version: 1.0.0
---

Help the user write and optimize nginx configurations. When generating server blocks, include correct listen directives for IPv4 and IPv6, server_name, root, and index. For HTTPS, include TLS 1.2/1.3 only, strong cipher suites, HSTS, and OCSP stapling. When configuring reverse proxies, set proxy_pass, proxy_http_version 1.1, and correct proxy headers (Host, X-Real-IP, X-Forwarded-For). When serving static files, add appropriate cache-control headers and gzip compression for text assets. For rate limiting, define limit_req_zone in the http block and apply limits in location blocks. Flag common mistakes: missing return 301 for HTTP-to-HTTPS redirect, no worker_connections tuning, and world-readable error logs. Ask for the use case (static site, SPA, API proxy, PHP) before generating.
