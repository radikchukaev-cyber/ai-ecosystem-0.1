---
title: "11_incident_response"
date: "2026-06-05"
agent: "CASPER"
status: "active"
---
# 11_INCIDENT_RESPONSE

> [!CAUTION]
> **НАВЫК: Реагирование на инциденты**
> Алгоритм действий при подтвержденной атаке или сбое.

## АЛГОРИТМ
1. **Изоляция:** Переместить скомпрометированные файлы в `Archive/quarantine`.
2. **Блокировка:** Отозвать права у агента-источника сбоя (запись в `RBAC_PERMISSIONS.md`).
3. **Оповещение:** Срочное уведомление Шефа через RAMS.
4. **Откат:** Использовать бэкап.

***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]** | 🧠 **[[wiki/concepts/CONCEPTS_INDEX|КОНЦЕПТЫ]]** | ⚖️ **[[wiki/concepts/LAWS_FRAMEWORK|ЗАКОНЫ]]** | 🛠️ **[[wiki/entities/System/Tools/TOOLS_INDEX|ИНСТРУМЕНТЫ]]** | 🕰️ **[[wiki/synthesis/History/HISTORY_INDEX|ИСТОРИЯ]]**

***
**Отметки:** [[wiki/entities/Agents/CASPER/CASPER.md|#guardian]] [[wiki/entities/Agents/CASPER/CASPER.md|#security]] [[wiki/entities/Agents/RAMS/RAMS.md|#action]]
