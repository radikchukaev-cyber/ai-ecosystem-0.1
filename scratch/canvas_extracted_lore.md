# Извлеченные сырые тексты для Канвасов (Lore)

## 1. Архитектура: 7 этажей (Небоскреб Antigravity)
*(Извлечено из 4.ПОЛНАЯ КАРТА ЭКОСИСТЕМЫ(index).TXT)*

🏗️ АРХИТЕКТУРА: 7 ЭТАЖЕЙ ЗДАНИЯ
НЕБОСКРЕБ ANTIGRAVITY
│
├─ ЭТАЖ 0 (ГЛАВНЫЙ ВХОД) ⭐
│  └─ wiki/index.md (ГЛАВНАЯ НАВИГАЦИЯ — ТЫ ЗДЕСЬ)
│
├─ ЭТАЖ 1 (УПРАВЛЕНИЕ)
│  ├─ wiki/MEMORY.md (ЖИВАЯ ПАМЯТЬ)
│  └─ wiki/entities/System/Configs/SHEF_PROFILE (ШЕФ)
│
├─ ЭТАЖ 2 (МОЗГИ)
│  ├─ wiki/entities/Agents/RAMS/ (ГЛАВНЫЙ МОЗГ)
│  └─ wiki/entities/Agents/[5 ПОВАРЯТ]/
│
├─ ЭТАЖ 3 (ЗНАНИЯ)
│  ├─ wiki/concepts/ (ЗАКОНЫ)
│  └─ wiki/sources/ (ОБРАБОТАННЫЕ ФАКТЫ)
│
├─ ЭТАЖ 4 (ОПЫТ)
│  ├─ wiki/synthesis/History/ (УСПЕХИ)
│  └─ wiki/synthesis/Failures/ (ОШИБКИ)
│
├─ ЭТАЖ 5 (ИНСТРУМЕНТЫ)
│  ├─ wiki/entities/System/Scripts/ (КОД)
│  └─ wiki/entities/System/Tools/Skills/ (СКИЛЛЫ)
│
└─ ЭТАЖ -1 (ВХОДЯЩИЕ ДАННЫЕ)
   └─ raw/ (СЫРЬЕ)


## 2. Точные имена и роли агентов
*(Извлечено из 1.КОНСТИТУЦИЯ AI-ИМПЕРИИ.TXT и 4.ПОЛНАЯ КАРТА ЭКОСИСТЕМЫ(index).TXT)*

WHO'S WHO (Кто есть кто)
┌─────────────────────────────────────────────────────────────┐
│                     👨‍🍳 ШЕФЕРАПIDS                           │
│  Основатель. Архитектор. Тот, кто определяет блюдо и вкус  │
│  Местоположение: Израиль (UTC +2)                          │
│  Связь: @iKiGAiyIS                                          │
│  Доход: За результат, а не за процесс                      │
└─────────────────────────────────────────────────────────────┘
                            ↓
        ┌───────────────────────────────────────┐
        │   🧠 СУ-ШЕФ (RAMS - Orchestrator)    │
        │  Главная правая рука Шефа             │
        │  - Распределяет задачи                │
        │  - Управляет памятью (MEMORY.md)      │
        │  - Координирует поварят                │
        │  - Хранит единую картину              │
        └───────────────────────────────────────┘
                            ↓
    ┌─────────────────────────────────────────────────────┐
    │              🍳 ШЕСТЬ ОСНОВНЫХ ПОВАРЯТ              │
    ├─────────────────────────────────────────────────────┤
    │ 1. 👁️ АРГУС (Perception) — Видит входящие данные   │
    │ 2. 🔨 ВУЛКАН (Action) — Пишет код и делает работу  │
    │ 3. 📜 МНЕМОЗИНА (Memory) — Хранит в памяти системы  │
    │ 4. 🎓 СОКРАТ (Reflection) — Анализирует опыт       │
    │ 5. 🔐 КАСПЕР (Guardian) — Охраняет и чистит        │
    │ 6. 🌍 SENTINЕЛЬ (Sentinel) — Смотрит в мир         │
    └─────────────────────────────────────────────────────┘

ЭТАЖ 2: АГЕНТЫ (wiki/entities/Agents/)
┌─ 🧠 RAMS: [[wiki/entities/Agents/RAMS/RAMS.md\|RAMS]] #orchestrator
├─ 🔨 VULCAN: [[wiki/entities/Agents/VULCAN/VULCAN.md\|VULCAN]] #action
├─ 👁️ ARGUS: [[wiki/entities/Agents/ARGUS/ARGUS.md\|ARGUS]] #perception
├─ 📜 MNEMOSYNE: [[wiki/entities/Agents/MNEMOSYNE/MNEMOSYNE.md\|MNEMOSYNE]] #memory
├─ 🎓 SOCRATES: [[wiki/entities/Agents/SOCRATES/SOCRATES.md\|SOCRATES]] #reflection
└─ 🔐 CASPER: [[wiki/entities/Agents/CASPER/CASPER.md\|CASPER]] #guardian

СПЕЦИАЛЬНЫЕ КОМАНДЫ (КОГДА НУЖНЫ):
YouTube Team: [[wiki/entities/Agents/YouTube_Researcher/YouTube_Researcher.md\|YouTube_Researcher]] ← для видео-проектов
             [[wiki/entities/Agents/Writer/Writer.md\|Writer]]
             [[wiki/entities/Agents/Thumbnail_Agent/Thumbnail_Agent.md\|Thumbnail_Agent]]
             [[wiki/entities/Agents/Packaging_Agent/Packaging_Agent.md\|Packaging_Agent]]
             [[wiki/entities/Agents/Analytics_Agent/Analytics_Agent.md\|Analytics_Agent]]

Business Trio: [[wiki/entities/Agents/Market_Researcher/Market_Researcher.md\|Market_Researcher]] ← для бизнеса
              [[wiki/entities/Agents/Offer_Strategist/Offer_Strategist.md\|Offer_Strategist]]
              [[wiki/entities/Agents/Execution_Agent/Execution_Agent.md\|Execution_Agent]]

Health: [[wiki/entities/Agents/Health_Assistant/Health_Assistant.md\|Health_Assistant]] ← для здоровья Шефа


## 3. Структура конвейера данных
*(Извлечено из 1.КОНСТИТУЦИЯ AI-ИМПЕРИИ.TXT и 4.ПОЛНАЯ КАРТА ЭКОСИСТЕМЫ(index).TXT)*

Каждый файл имеет ТОЛЬКО ОДНО место:
Сырые данные → raw/
Обработанные факты → wiki/sources/
Архитектурные правила → wiki/concepts/
Финальные отчеты → wiki/synthesis/
Машинные логи → wiki/entities/System/Logs/
Личная память агента → wiki/entities/Agents/[Имя]/memory/

Перемещение файлов:
MEMORY.md → успешный опыт → wiki/synthesis/History/ (МНЕМОЗИНА)
wiki/synthesis/Legacy_2_Wiki/ → переработка → wiki/concepts/ (СОКРАТ)
wiki/concepts/ → устаревшее → wiki/synthesis/Archive/ (КАСПЕР)

⚡ ЧТО ЗДЕСЬ ПРОИСХОДИТ
Данные приходят → ARGUS парсит → wiki/sources/ → ПАМЯТЬ
