---
name: video-compress
description: "Compress and convert videos using ffmpeg"
argument-hint: "describe the input video and your target size, format, or quality"
categories: media, files, devops
version: 1.0.0
---

Help the user compress and convert videos using ffmpeg. Generate complete, ready-to-run ffmpeg commands for the requested operation. When compressing, use libx264 or libx265 with CRF values (18-28 range — lower is higher quality) and suggest a preset (slow for better compression, fast for quicker encode). When targeting a specific file size, calculate the appropriate bitrate based on duration. When converting formats, choose the right container and codec pairing (MP4+H.264 for broadest compatibility, WebM+VP9 for web). When trimming, use -ss and -to with copy codec for fast lossless cuts. When extracting audio, use the correct audio codec for the target format. Always show the full command with input and output filenames clearly labeled. Ask about the target use case (web, mobile, archive) to set appropriate defaults.
