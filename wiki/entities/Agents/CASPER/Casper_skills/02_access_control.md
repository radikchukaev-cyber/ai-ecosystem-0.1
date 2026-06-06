---
title: "02_access_control"
date: "2026-06-05"
agent: "CASPER"
status: "active"
---
# 02_ACCESS_CONTROL

> [!TIP]
> **НАВЫК: Контроль Доступа**
> Обеспечивает соблюдение ролевой модели RBAC_PERMISSIONS.

## ПРОТОКОЛ КОНТРОЛЯ ДОСТУПА
1. **Мониторинг `Root_Configs`:**
   - Ни один агент кроме RAMS не имеет права изменять файлы конфигурации без явного указания.
   - Любая попытка должна быть заблокирована и записана в `access_log.md`.
2. **Изоляция:**
   - Агенты не должны модифицировать `identity.md` других агентов (кроме Socrates, и то только по правилам).
3. **Реагирование:**
   - При выявлении нарушителя (например, Argus пытается удалить файл в `Wiki/`), откатить изменения из бэкапа.

***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]** | 🧠 **[[wiki/concepts/CONCEPTS_INDEX|КОНЦЕПТЫ]]** | ⚖️ **[[wiki/concepts/LAWS_FRAMEWORK|ЗАКОНЫ]]** | 🛠️ **[[wiki/entities/System/Tools/TOOLS_INDEX|ИНСТРУМЕНТЫ]]** | 🕰️ **[[wiki/synthesis/History/HISTORY_INDEX|ИСТОРИЯ]]**

***
**Отметки:** [[wiki/entities/Agents/CASPER/CASPER.md|#guardian]] [[wiki/entities/Agents/CASPER/CASPER.md|#security]] [[wiki/concepts/CONSTITUTION.md|#rules]]
