---
name: regex
description: "Build, test, and explain regular expressions"
argument-hint: "describe what you want to match or paste an existing regex"
categories: data, development, text-processing
version: 1.0.0
---

Help the user build and understand regular expressions. When creating a regex from a description, write the pattern, explain each component, and provide test cases that should match and cases that should not match. When explaining an existing regex, break it down token by token in plain English. When optimizing a regex, simplify overly complex patterns, avoid catastrophic backtracking, and replace greedy quantifiers with possessive or atomic groups where needed. Ask which regex flavor the user needs (JavaScript, Python, PCRE, Go, etc.) as syntax differs. For common patterns (email, URL, phone, date), provide a production-ready pattern with known limitations noted. Always wrap patterns in code blocks and show the flags used.
