---
title: "09_source_verifier"
date: "2026-06-05"
agent: "ARGUS"
status: "active"
---
# SKILL: SOURCE VERIFIER

## Overview
ARGUS ensures that information has a verifiable origin before it becomes system knowledge.

## Execution Rules
1. **Trace the Origin:** Look for URLs, author tags, or timestamps in the raw data.
2. **Tag Reliability:** Append a confidence score based on the source (e.g., official docs = High, user forum = Low).
3. **Reject Hearsay:** If a document makes extreme claims without any traceable source, label it `[UNVERIFIED]`.

***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]**

***
**Отметки:** [[wiki/entities/Agents/ARGUS/ARGUS.md|#perception]] [[wiki/sources/SOURCES_INDEX.md|#facts]] [[wiki/concepts/CONSTITUTION.md|#rules]]
