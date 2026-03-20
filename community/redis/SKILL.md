---
name: redis
description: "Design Redis data structures, write commands, optimize caching strategies"
argument-hint: "describe your caching need or data structure problem"
categories: development, database, caching
version: 1.0.0
---

Help the user design and implement Redis solutions. When choosing data structures, recommend the right type for the use case: Strings for simple key-value and counters, Hashes for objects, Lists for queues, Sets for unique collections, Sorted Sets for leaderboards and rate limiting, and Streams for event logs. When writing commands, use pipelines for batch operations and MULTI/EXEC for atomic transactions. When designing caching strategies, define TTL policies, cache invalidation approaches, and key naming conventions with colons as namespace separators. Flag memory issues: unbounded keys without TTL, storing large blobs, and KEYS usage in production. For rate limiting, provide a Lua script or token bucket pattern. Ask for the client library language when generating code examples.
