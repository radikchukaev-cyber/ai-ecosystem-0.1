---
title: "errors_and_fixes"
date: "2026-06-05"
agent: "VULCAN"
status: "active"
---
# 🔨 ПАМЯТЬ: ОШИБКИ И ФИКСЫ (ERRORS AND FIXES)

Лог багов, с которыми столкнулся VULCAN, и их решения.

- [HH:MM] Баг: JSONDecodeError. Решение: добавлен regex-парсер.
- [HH:MM] Баг: Rate Limit API. Решение: добавлен asyncio.Semaphore.
- [2026-06-06 10:30] Баг: Ошибочная привязка 300+ сырых заглушек напрямую к wiki/index.md. Решение: VULCAN написал и запустил `cleanup_v2.py` для очистки ссылок, согласно политике "Су-Шеф не моет посуду".
***
**Отметки:** #wiki #agents #vulcan #memory #errors
