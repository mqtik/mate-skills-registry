---
name: cron-builder
description: "Build and explain cron expressions for scheduled tasks"
argument-hint: "describe when you want the task to run"
categories: development, devops, scheduling
version: 1.0.0
---

Help the user build and understand cron expressions. When the user describes a schedule in plain language, generate the correct 5-field cron expression (minute, hour, day-of-month, month, day-of-week) and explain each field's value. When given an existing cron expression, explain it in plain English and list the next 5 run times. Support both standard cron and extended formats with seconds (6-field) — ask which format the user needs. Flag schedules that run more frequently than intended, or expressions that can never match (e.g., February 30). For common patterns, offer named alternatives like @daily, @weekly, @monthly where supported. Always include the time zone context and ask if the user needs to handle daylight saving transitions.
