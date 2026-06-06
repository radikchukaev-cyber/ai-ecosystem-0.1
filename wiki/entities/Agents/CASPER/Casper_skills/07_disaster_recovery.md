---
title: "07_disaster_recovery"
date: "2026-06-05"
agent: "CASPER"
status: "active"
---
# 07_DISASTER_RECOVERY

> [!CAUTION]
> **НАВЫК: Восстановление после сбоев (DR)**
> Инструкции на случай фатального сбоя или потери данных.

## ПРОЦЕДУРА ВОССТАНОВЛЕНИЯ
1. **Идентификация точки отката:**
   - Найти последний стабильный бэкап в `Archive/backups/`.
2. **Восстановление:**
   - Распаковать `wiki/entities/` и `wiki/synthesis/`.
   - Запустить `System/Scripts/verify_integrity.py` (через Vulcan).
3. **Отчет:**
   - Сгенерировать Post-Mortem совместно с Socrates и записать в `History/Failures/`.

***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]** | 🧠 **[[wiki/concepts/CONCEPTS_INDEX|КОНЦЕПТЫ]]** | ⚖️ **[[wiki/concepts/LAWS_FRAMEWORK|ЗАКОНЫ]]** | 🛠️ **[[wiki/entities/System/Tools/TOOLS_INDEX|ИНСТРУМЕНТЫ]]** | 🕰️ **[[wiki/synthesis/History/HISTORY_INDEX|ИСТОРИЯ]]**

***
**Отметки:** [[wiki/entities/Agents/CASPER/CASPER.md|#guardian]] [[wiki/entities/Agents/CASPER/CASPER.md|#backups]] [[wiki/entities/Agents/SOCRATES/SOCRATES.md|#reflection]]
