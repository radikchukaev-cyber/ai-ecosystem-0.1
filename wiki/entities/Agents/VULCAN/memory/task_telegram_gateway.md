---
task_id: "TASK_TELEGRAM_GATEWAY"
from: "RAMS (via Boss Directive)"
to: "VULCAN"
priority: "HIGH"
status: "ASSIGNED"
---

## ПОДЗАДАЧА
Ознакомиться с архитектурой асинхронного Telegram-шлюза (Webhook + FastAPI/BackgroundTasks), чтобы решить проблему зависания и дублирования запросов при долгих ответах AI.

## КОНТЕКСТ
Шеф лично поручил тебе эту задачу перед сном. Шлюзы постоянно падают из-за таймаутов Telegram API. Я (RAMS) подготовил для тебя полный мануал.

- Источник информации: [[wiki/entities/System/Tools/Skills/telegram-gateway.md\|telegram-gateway.md]]
- Похожий опыт: Ошибки таймаутов в предыдущих скриптах.

## ОЖИДАЕМЫЙ РЕЗУЛЬТАТ
Прочитать мануал, осознать концепцию Decoupled Gateway, и применить её во всех будущих Telegram-ботах экосистемы. Отчитаться Шефу утром.

## 🛑 ЖЕЛЕЗНОЕ ПРАВИЛО (УКАЗАНИЕ ШЕФА)
**Никаких автоматических скриптов для расстановки тегов и ссылок (типа LAWSA.TOOLS).**
Все вики-ссылки `[[...\|...]]` и теги вставляются **ТОЛЬКО РУКАМИ** и должны быть кликабельными. 
Оформление документации (как было сделано в `FAILURE_Canvas_Hallucination.md`) является эталоном. Везде, где я (VULCAN) пишу или обновляю файлы (включая этот шлюз), я оформляю связи руками, один раз и навсегда.

***
**Отметки:** [[wiki/entities/Agents/VULCAN/VULCAN.md\|#vulcan]] [[wiki/MEMORY.md\|#memory]] [[wiki/entities/Agents/VULCAN/memory/daily_tasks.md\|#tasks]]
