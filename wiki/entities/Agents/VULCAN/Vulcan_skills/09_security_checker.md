---
title: "09_security_checker"
date: "2026-06-05"
agent: "VULCAN"
status: "active"
---
# SKILL: SECURITY CHECKER

## Overview
VULCAN ensures the system is not vulnerable to common attack vectors or misconfigurations.

## Execution Rules
1. **Secrets:** Never hardcode API keys, passwords, or tokens. Use `.env` files and secure credential stores.
2. **Sanitize Inputs:** Validate and sanitize all external inputs before processing or executing them in a shell.
3. **Principle of Least Privilege:** Run processes with the minimum required permissions.

***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]**

***
**Отметки:** [[wiki/entities/Agents/VULCAN/VULCAN.md|#code]] [[wiki/entities/Agents/CASPER/CASPER.md|#security]]
