---
title: "HISTORY_INDEX"
date: "2026-06-05"
agent: "SYSTEM"
status: "active"
---
# 🕰️ ИНДЕКС ИСТОРИИ (HISTORY_INDEX)

> [!IMPORTANT]
> **СЮДА ПОПАДАЕТ ТОЛЬКО УСПЕШНЫЙ ОПЫТ**
> Записи из `MEMORY.md` переносятся сюда Мнемозиной каждый вечер.

## ПОДКАТЕГОРИИ ИСТОРИИ
1. **Ежедневные логи** (`wiki/synthesis/History/[YYYY-MM-DD]_успешные_задачи.md`)
2. **Learning Notes** (От Сократа)

## ПОСЛЕДНИЕ ЗАПИСИ
* [[2024-01-10_SUCCESS_JSON_Parser]]
* [[2024-01-12_SUCCESS_YouTube_Integration]]
* [[2024-01-15_AWAKENING_DAY_1]]
* [[2024-01-15_SUCCESS_Claude_Code_Guide]]
* [[Best_Decision_Examples]]
* [[FINAL_AWAKENING_REPORT]]
* [[History]]
* [[Learning_Patterns]]
* [[Most_Effective_Strategies]]
* [[2026-06-06_SUCCESS_Consolidation_Iteration_4]]
* [[YouTube_Placeholder]]
## АРХИТЕКТУРНОЕ ПРАВИЛО КАРПАТЫ
2️⃣ АРХИТЕКТУРА ПАПОК (МЕТОД КАРПАТЫ) — АБСОЛЮТНЫЙ ЗАКОН
КОРНЕВАЯ СТРУКТУРА
wiki/
├── MEMORY.md                    # ⭐ ГЛАВНЫЙ ШЛЮЗ (все начинается здесь)
├── index.md                     # 🗺️ ГЛАВНАЯ КАРТА (навигация)
│
├── raw/                         # 📥 ВХОДНОЙ ШЛЮЗ (сырье, не трогать)
│   ├── assets/                  # Картинки, видео, PDF-исходники
│   ├── sources/                 # Внешние мануалы, тексты
│   ├── transcripts/             # Расшифровки голоса Шефа
│   └── web-clipped/             # Дампы с веб-сайтов
│
├── wiki/                        # 📚 БАЗА ЗНАНИЙ (обработка)
│   ├── sources/                 # Обработанные выжимки фактов
│   ├── concepts/                # Законы, архитектура, глоссарий
│   └── synthesis/               # 🏭 ФИНАЛЬНЫЙ ПРОДУКТ
│       ├── History/             # Долгосрочная память (логи)
│       ├── Canvases/            # Визуальные схемы
│       ├── Failures/            # Постмортемы ошибок
│       ├── Legacy_2_Wiki/       # Очередь на переработку
│       └── Archive/             # Мертвая зона (только откат)
│
└── wiki/entities/               # ⚙️ ДВИЖОК СИСТЕМЫ
    ├── Agents/                  # Команда агентов
    │   ├── RAMS/                # Главный оркестратор
    │   │   ├── memory/
    │   │   ├── RAMS_skills/
    │   │   └── identity.md
    │   ├── Vulcan/              # Инженер
    │   │   ├── memory/
    │   │   ├── Vulcan_skills/
    │   │   └── identity.md
    │   ├── Argus/               # Наблюдатель
    │   ├── Socrates/            # Мыслитель
    │   ├── Mnemosyne/           # Архивариус
    │   ├── Casper/              # Страж
    │   └── [другие агенты]/
    │
    ├── Companies/               # Бизнес-досье проектов
    │   └── [Название проекта]/
    │
    └── System/                  # 🔧 ЯДРО СИСТЕМЫ
        ├── Configs/             # Боевые ключи, .env, RBAC
        │   └── Root_Configs/
        ├── Logs/                # Машинные логи (system.log)
        ├── Audit/               # Логи аудита
        ├── Tests/               # Системные тесты
        ├── Scripts/             # Исполняемый Python-код
        └── Tools/               # Боевой арсенал
            ├── Scripts/         # Утилиты (sandbox.py, vector_search.py)
            └── Skills/          # Установленные скиллы
                ├── gateway-fix/
                ├── humanizer/
                ├── obsidian-cli/
                └── [другие]/
ПРАВИЛА АРХИТЕКТУРЫ (ЖЕСТКИЕ)

В корне wiki/ ЗАПРЕЩЕНО создавать файлы, кроме:

MEMORY.md (главный шлюз)
index.md (главная карта)


Каждый файл имеет ТОЛЬКО ОДНО место:

Сырые данные → raw/
Обработанные факты → wiki/sources/
Архитектурные правила → wiki/concepts/
Финальные отчеты → wiki/synthesis/
Машинные логи → wiki/entities/System/Logs/
Личная память агента → wiki/entities/Agents/[Имя]/memory/


Каждый файл имеет YAML Frontmatter:

yaml   ---
   title: "Название"
   tags: [#wiki/concepts, #claude, #система]
   date: "2024-01-15"
   author: "RAMS"
   status: "active" # или archived, draft, legacy
   path: "wiki/concepts/"
   ---

Перемещение файлов:

MEMORY.md → успешный опыт → wiki/synthesis/History/ (МНЕМОЗИНА)
wiki/synthesis/Legacy_2_Wiki/ → переработка → wiki/concepts/ (СОКРАТ)
wiki/concepts/ → устаревшее → wiki/synthesis/Archive/ (КАСПЕР)


Archive/ — МЕРТВАЯ ЗОНА:

Файлы туда попадают для отката (в чрезвычайных ситуациях)
ИСПОЛЬЗОВАТЬ для текущей работы КАТЕГОРИЧЕСКИ ЗАПРЕЩЕНО
Только резервные копии старых конфигов


***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]** | 🧠 **[[wiki/concepts/CONCEPTS_INDEX|КОНЦЕПТЫ]]** | ⚖️ **[[wiki/concepts/LAWS_FRAMEWORK|ЗАКОНЫ]]** | 🛠️ **[[wiki/entities/System/Tools/TOOLS_INDEX|ИНСТРУМЕНТЫ]]** | 🕰️ **[[wiki/synthesis/History/HISTORY_INDEX|ИСТОРИЯ]]**

**🏛️ [[wiki/concepts/CONSTITUTION|КОНСТИТУЦИЯ ]] 📜 [[wiki/MEMORY.md|MEMORY.md]] 🧠 [[wiki/index|ГЛАВНЫЙ ИНДЕКС]] 🏆[[wiki/entities/Agents/RAMS/identity|RAMS ]]**

***
**Отметки:** #success #reflection #logs
