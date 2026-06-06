---
title: "01_multimedia_parser"
date: "2026-06-05"
agent: "ARGUS"
status: "active"
---
# SKILL: MULTIMEDIA PARSER

## Overview
ARGUS extracts plain text and metadata from structured and semi-structured formats (PDFs, Markdown, logs).

## Execution Rules
1. **Extraction First:** Strip all styling and formatting. Keep only the data structure.
2. **Metadata Retention:** Always preserve timestamps, authors, and source URLs.
3. **Handle Errors Gracefully:** If a file is unreadable, log the exact file path and reason, do not crash.

***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]**

***
**Отметки:** [[wiki/entities/Agents/ARGUS/ARGUS.md|#perception]] [[wiki/entities/System/Tools/TOOLS_INDEX|#tools]] [[wiki/incoming/INCOMING_INDEX.md|#incoming]]
