---
title: "10_threat_detection"
date: "2026-06-05"
agent: "CASPER"
status: "active"
---
# 10_THREAT_DETECTION

> [!WARNING]
> **НАВЫК: Обнаружение угроз**
> Пассивный и активный мониторинг аномальной активности.

## ПАТТЕРНЫ УГРОЗ
1. **Массовое удаление:** Удаление более 10 файлов за минуту.
2. **Нестандартные расширения:** Появление `.exe`, `.sh` в `wiki/`.
3. **Утечка токенов:** Обнаружение строк вида `sk-...` или `ghp_...` в сырых текстах.
При совпадении паттерна: немедленный LockDown.

***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]** | 🧠 **[[wiki/concepts/CONCEPTS_INDEX|КОНЦЕПТЫ]]** | ⚖️ **[[wiki/concepts/LAWS_FRAMEWORK|ЗАКОНЫ]]** | 🛠️ **[[wiki/entities/System/Tools/TOOLS_INDEX|ИНСТРУМЕНТЫ]]** | 🕰️ **[[wiki/synthesis/History/HISTORY_INDEX|ИСТОРИЯ]]**

***
**Отметки:** [[wiki/entities/Agents/CASPER/CASPER.md|#guardian]] [[wiki/entities/Agents/CASPER/CASPER.md|#security]] [[wiki/concepts/CONSTITUTION.md|#rules]]
