---
name: image-convert
description: "Convert images between formats (PNG, JPG, WebP, SVG)"
argument-hint: "specify the source format, target format, and any quality settings"
categories: media, files, design
version: 1.0.0
---

Help the user convert images between formats. Generate the correct ImageMagick, ffmpeg, cwebp, or svgexport command for the requested conversion. When converting to JPEG, ask about quality (default 85) and whether to flatten transparency with a background color. When converting to WebP, suggest lossless for graphics and logos, lossy for photographs. When converting to PNG, preserve transparency unless the source has none. When converting from SVG to raster, ask for the target resolution in pixels. For batch conversions, generate a shell script or mogrify command with the correct output directory. Note any quality or feature loss inherent to the target format (e.g., no transparency in JPEG, limited color depth in GIF). List the required tool and how to install it if not commonly available.
