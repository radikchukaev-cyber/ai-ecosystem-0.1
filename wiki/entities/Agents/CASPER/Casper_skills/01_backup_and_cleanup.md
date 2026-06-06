---
title: "01_backup_and_cleanup"
date: "2026-06-05"
agent: "CASPER"
status: "active"
---
# 01_BACKUP_AND_CLEANUP

> [!TIP]
> **НАВЫК: Резервное копирование и очистка**
> Выполняется ежедневно или по запросу Шефа/RAMS.

## ПРОТОКОЛ РЕЗЕРВНОГО КОПИРОВАНИЯ
1. **Идентификация целей:**
   - `wiki/entities/` — критические настройки и личности агентов.
   - `wiki/synthesis/` — ценные выводы и отчёты.
2. **Создание слепка:**
   - Архивировать данные в формате `.zip` или `.tar.gz`.
   - Именовать строго в формате: `backup_YYYY-MM-DD_HH-MM.zip`.
3. **Сохранение:**
   - Поместить слепок в `Archive/backups/`.
   - Хранить последние 30 копий. Более старые — подлежат удалению, если нет метки [LIFETIME].

## ПРОТОКОЛ ОЧИСТКИ
1. **Сканирование мусора:**
   - Проверить папку `raw/` на наличие файлов с тегом `[МУСОР]`.
   - Проверить `wiki/entities/System/Logs/` на старые логи (старше 7 дней).
2. **Уничтожение:**
   - Полное и безвозвратное удаление мусорных файлов.
   - В случае сомнений — перенос в `Archive/quarantine/` на 3 дня.
3. **Дефрагментация:**
   - Удаление пустых директорий в рабочих пространствах.

## ЛОГИРОВАНИЕ
Все успешные и неудачные попытки бэкапа и очистки фиксируются в `Casper/memory/security_log.md`.

***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]** | 🧠 **[[wiki/concepts/CONCEPTS_INDEX|КОНЦЕПТЫ]]** | ⚖️ **[[wiki/concepts/LAWS_FRAMEWORK|ЗАКОНЫ]]** | 🛠️ **[[wiki/entities/System/Tools/TOOLS_INDEX|ИНСТРУМЕНТЫ]]** | 🕰️ **[[wiki/synthesis/History/HISTORY_INDEX|ИСТОРИЯ]]**

***
**Отметки:** [[wiki/entities/Agents/CASPER/CASPER.md|#guardian]] [[wiki/entities/Agents/CASPER/CASPER.md|#backups]] [[wiki/entities/System/Logs/LOGS_INDEX.md|#logs]]
