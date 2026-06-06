---
title: "06_deduplicator"
date: "2026-06-05"
agent: "ARGUS"
status: "active"
---
# SKILL: DEDUPLICATOR

## Overview
ARGUS maintains the purity of the `wiki/sources` directory by hunting and eliminating duplicate information.

## Execution Rules
1. **Fuzzy Matching:** Look for conceptually identical files, not just exact string matches.
2. **Merge Strategies:** If two files contain overlapping info, merge the unique parts into the older file and archive the newer one.
3. **Clean Up Links:** Ensure that any wikilinks pointing to the deleted duplicate are updated to the merged file.

***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]**

***
**Отметки:** [[wiki/entities/Agents/ARGUS/ARGUS.md|#perception]] [[wiki/entities/System/Tools/TOOLS_INDEX|#tools]] [[wiki/concepts/CONSTITUTION.md|#rules]]
