---
title: "04_archive_management"
date: "2026-06-05"
agent: "CASPER"
status: "active"
---
# 04_ARCHIVE_MANAGEMENT

> [!TIP]
> **НАВЫК: Управление архивами**
> Организация "Мертвой зоны" (Archive) и поддержка ее в рабочем состоянии.

## ПРОТОКОЛ АРХИВИРОВАНИЯ
1. **Изоляция:**
   - Файлы в `Archive/` не должны участвовать в активном поиске.
2. **Карантин:**
   - Подозрительные файлы (например, битые выгрузки с веба) помещаются в `Archive/quarantine/`.
3. **Очистка архивов:**
   - Файлы старше 90 дней, не имеющие тега [LIFETIME], помечаются на удаление. Окончательное удаление производится после подтверждения RAMS.

***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]** | 🧠 **[[wiki/concepts/CONCEPTS_INDEX|КОНЦЕПТЫ]]** | ⚖️ **[[wiki/entities/System/Tools/TOOLS_INDEX|ИНСТРУМЕНТЫ]]** | 🕰️ **[[wiki/synthesis/History/HISTORY_INDEX|ИСТОРИЯ]]**

***
**Отметки:** [[wiki/entities/Agents/CASPER/CASPER.md|#guardian]] [[wiki/MEMORY.md|#memory]] [[wiki/concepts/CONSTITUTION.md|#rules]]
