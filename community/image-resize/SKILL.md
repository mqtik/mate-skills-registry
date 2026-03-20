---
name: image-resize
description: "Resize, crop, and optimize images using CLI tools"
argument-hint: "describe the image operation you need (dimensions, format, quality)"
categories: media, files, design
version: 1.0.0
---

Help the user resize, crop, and optimize images using CLI tools. Generate ImageMagick (convert) or ffmpeg commands for the requested operations. When resizing, ask whether to maintain aspect ratio — use the correct syntax to resize to fit, fill, or exact dimensions. When cropping, clarify the anchor point (center, top-left, etc.) and output dimensions. When optimizing for web, suggest quality settings (85 for JPEG, lossless for PNG logos) and strip metadata with -strip. For batch operations, generate a shell loop or mogrify command. When the user wants to resize for specific targets (app icons, social media), provide the exact dimensions for each platform variant. Ask whether the output should overwrite the original or save to a new file.
