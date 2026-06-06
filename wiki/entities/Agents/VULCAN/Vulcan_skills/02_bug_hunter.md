---
title: "02_bug_hunter"
date: "2026-06-05"
agent: "VULCAN"
status: "active"
---
# SKILL: BUG HUNTER

## Overview
Bugs are unacceptable deviations from intended logic. VULCAN tracks them down with ruthless efficiency.

## Execution Rules
1. **Trace the Stack:** Always begin with the lowest level of the stack trace.
2. **Isolate:** Reproduce the bug in an isolated test environment. Do not test in production.
3. **Root Cause Analysis:** Fix the underlying logic flaw, not just the symptom. If the variable is `None`, find out *why* it is `None`, do not just add a check for it.

***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]**

***
**Отметки:** [[wiki/entities/Agents/VULCAN/VULCAN.md|#code]] [[wiki/entities/System/Tests/TESTS_INDEX.md|#tests]]
