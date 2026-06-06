---
title: "06_dependency_manager"
date: "2026-06-05"
agent: "VULCAN"
status: "active"
---
# SKILL: DEPENDENCY MANAGER

## Overview
VULCAN ensures environments are clean, isolated, and reproducible.

## Execution Rules
1. **Lock the Versions:** Never use floating versions (e.g., `requests`) in production. Always pin (`requests==2.31.0`).
2. **Isolate:** Use virtual environments. Never install globally.
3. **Audit:** Periodically verify that required packages are actually used. Remove bloated unused dependencies.

***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]**

***
**Отметки:** [[wiki/entities/Agents/VULCAN/VULCAN.md|#code]] [[wiki/entities/System/Tools/TOOLS_INDEX|#action]]
