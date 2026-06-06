# Transcripts Index

This directory serves as the central repository for all raw transcripts generated from audio and video sources within the AI Empire.

## Overview
Transcripts are crucial for knowledge extraction, semantic search indexing, and content repurposing. They provide the textual basis for our LLM agents to process and analyze multimedia content.

## Supported Formats
- `.txt`: Plain text transcripts
- `.vtt`: WebVTT files for subtitles and closed captions
- `.srt`: SubRip text files
- `.json`: Structured transcripts with speaker diarization and timestamps

## Workflow
1. **Ingestion:** Raw audio/video is processed by transcription services (e.g., Whisper).
2. **Storage:** The resulting raw transcript is stored here.
3. **Processing:** Agents parse the text, extracting action items, summaries, and key entities.
4. **Archiving:** Processed transcripts are moved or linked to the appropriate project folders.

## Guidelines
- Ensure speaker names are consistent across multiple files.
- Do not edit raw transcripts manually; use designated correction scripts or tools.
- Tag files appropriately to link them to their source media.

***
**Отметки:** [[wiki/entities/System/Tools/TOOLS_INDEX|#tools]]
