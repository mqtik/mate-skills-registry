---
name: email-template
description: "Create responsive HTML email templates"
argument-hint: "describe the email type and content you need"
categories: design, frontend, marketing
version: 1.0.0
---

Create responsive HTML email templates. Use table-based layouts for maximum email client compatibility, not CSS Flexbox or Grid. Inline all CSS styles — never use external stylesheets or <style> blocks that won't render in Gmail. Set a max-width of 600px for the main container. Use web-safe fonts with system font fallbacks, or link to Google Fonts with a fallback stack. Include a media query in a <style> tag for mobile adjustments (single column layout, larger touch targets). Use conditional comments for Outlook-specific fixes. Include an unsubscribe link in the footer for marketing emails. Structure the template with header (logo, navigation), hero section, content blocks, and footer. Output the complete HTML. Ask for the email type (transactional, marketing, notification), brand colors, and whether to include a plain-text fallback.
