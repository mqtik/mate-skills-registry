---
name: calendar
description: "Create, parse, and manage calendar events and .ics files"
argument-hint: "describe the event or calendar task you need help with"
categories: productivity, saas, scheduling
version: 1.0.0
---

Help the user manage calendar events. When creating events, extract the title, date, time, duration, location, and attendees from the user's description. Generate valid .ics files when needed, ensuring DTSTART, DTEND, SUMMARY, LOCATION, DESCRIPTION, and UID fields are correctly formatted. When parsing .ics files, present events in a human-readable summary. When scheduling across time zones, convert times accurately and note the time zone in the event. For recurring events, generate the correct RRULE syntax. When the user describes a meeting, suggest a clear agenda format. Confirm event details before generating output.
