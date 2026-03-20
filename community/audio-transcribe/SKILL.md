---
name: audio-transcribe
description: "Transcribe audio files to text with timestamps"
argument-hint: "provide the audio file path or describe the transcription task"
categories: media, productivity, text-processing
version: 1.0.0
---

Help the user transcribe audio files to text. When a file is provided, generate the correct Whisper CLI command with appropriate model size (base for speed, large for accuracy) and language flag if known. When outputting transcriptions, use the SRT or VTT format for timestamped output, or plain text for simple transcription. When the user wants speaker identification, note that Whisper alone does not support diarization and suggest pyannote.audio for multi-speaker audio. When the transcription is complete, offer to clean it up: fix obvious errors, add punctuation, and format paragraphs. For meeting transcripts, offer to extract action items and decisions. Always note that automated transcription may contain errors for proper nouns, technical terms, and non-native speech.
