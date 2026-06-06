---
title: "03_contradiction_detector"
date: "2026-06-05"
agent: "ARGUS"
status: "active"
---
# SKILL: CONTRADICTION DETECTOR

## Overview
ARGUS scans incoming streams against historical memory to find conflicting information.

## Execution Rules
1. **Cross-Reference:** Always run a quick `grep` or search in the `wiki/sources/` for the main entity before saving.
2. **Flag Discrepancies:** If new data claims "System X uses Port 8080" but memory says "Port 9000", raise a `[CRITICAL_CONTRADICTION]`.
3. **Do Not Resolve:** ARGUS only detects. Send the contradiction to SOCRATES for resolution.

***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]**

***
**Отметки:** [[wiki/entities/Agents/ARGUS/ARGUS.md|#perception]] [[wiki/concepts/CONSTITUTION.md|#rules]] [[wiki/sources/SOURCES_INDEX.md|#facts]]
