---
title: "10_content_classifier"
date: "2026-06-05"
agent: "ARGUS"
status: "active"
---
# SKILL: CONTENT CLASSIFIER

## Overview
ARGUS categorizes processed data into the correct semantic buckets within the knowledge base.

## Execution Rules
1. **Determine the Domain:** Is this engineering, philosophy, history, or a system log?
2. **Apply Specific Tags:** Never use generic tags like `#data` or `#info`. Use specific tags like `#framework/react`, `#concept/architecture`, `#log/error`.
3. **Route to Folder:** Based on classification, define whether the file belongs in `concepts/`, `sources/`, or `entities/`.

***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]**

***
**Отметки:** [[wiki/entities/Agents/ARGUS/ARGUS.md|#perception]] [[wiki/entities/System/Tools/TOOLS_INDEX|#tools]] [[wiki/concepts/CONSTITUTION.md|#rules]]
