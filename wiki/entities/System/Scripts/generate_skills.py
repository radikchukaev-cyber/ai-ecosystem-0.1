import os

skills_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\wiki\entities\System\Tools\Skills"
os.makedirs(skills_dir, exist_ok=True)

skills_data = {
    "RAMS": {
        "desc": "Оркестратор. Управление всей Семьей и ресурсами.",
        "skills": [
            {"file": "orchestration.md", "title": "🎼 СКИЛЛ: Оркестрация (Распределение задач)", "target": "Субагентам Империи"},
            {"file": "decision_making.md", "title": "⚖️ СКИЛЛ: Принятие решений (Decision Making)", "target": "Вся Империя (разрешение конфликтов)"},
            {"file": "resource_management.md", "title": "💰 СКИЛЛ: Управление ресурсами (Resource Management)", "target": "Бюджет токенов и времени"}
        ]
    },
    "VULCAN": {
        "desc": "Инженер (Гейзенберг). Создание и починка кода, скриптов, парсеров.",
        "skills": [
            {"file": "coding.md", "title": "💻 СКИЛЛ: Кодирование (Coding Standards)", "target": "Терминал / Python / PowerShell"},
            {"file": "testing.md", "title": "🧪 СКИЛЛ: Тестирование (Testing & QA)", "target": "Файлы с кодом"},
            {"file": "debugging.md", "title": "🐛 СКИЛЛ: Отладка (Debugging)", "target": "Логи ошибок"},
            {"file": "deployment.md", "title": "🚀 СКИЛЛ: Развертывание (Deployment)", "target": "Sandbox / Production"},
            {"file": "optimization.md", "title": "⚡ СКИЛЛ: Оптимизация (Performance)", "target": "Медленные скрипты"}
        ]
    },
    "SOCRATES": {
        "desc": "Аналитик (Тайвин Ланнистер). Анализ сырых данных от Аргуса и логов от RAMS.",
        "skills": [
            {"file": "root_cause_analysis.md", "title": "🔍 СКИЛЛ: Анализ первопричин (Root Cause Analysis)", "target": "Ошибки и падения системы"},
            {"file": "pattern_detection.md", "title": "📊 СКИЛЛ: Поиск паттернов (Pattern Detection)", "target": "Большие массивы данных"},
            {"file": "learning_synthesis.md", "title": "🧠 СКИЛЛ: Синтез знаний (Learning Synthesis)", "target": "Концепты и wiki"},
            {"file": "instruction_update.md", "title": "📜 СКИЛЛ: Обновление инструкций", "target": "Промпты агентов"},
            {"file": "hypothesis_testing.md", "title": "⚖️ СКИЛЛ: Проверка гипотез", "target": "Бизнес-идеи Шефа"}
        ]
    },
    "MNEMOSYNE": {
        "desc": "Хранительница (Оракул). Граф Obsidian, Индексы, История.",
        "skills": [
            {"file": "organization.md", "title": "📁 СКИЛЛ: Организация (Organization)", "target": "Файловая структура"},
            {"file": "deduplication.md", "title": "🔄 СКИЛЛ: Дедупликация (Deduplication)", "target": "Похожие заметки"},
            {"file": "linking.md", "title": "🔗 СКИЛЛ: Связывание (Linking)", "target": "Осиротевшие файлы"},
            {"file": "archivization.md", "title": "📦 СКИЛЛ: Архивация (Archivization)", "target": "Завершенные проекты"},
            {"file": "index_management.md", "title": "📑 СКИЛЛ: Управление индексами", "target": "MOC (Map of Content)"}
        ]
    },
    "ARGUS": {
        "desc": "Ищейка (Сол Гудман). Внешний интернет, дампы, грязный HTML.",
        "skills": [
            {"file": "compression.md", "title": "🗜️ СКИЛЛ: Сжатие (Compression)", "target": "Огромные статьи"},
            {"file": "parsing.md", "title": "🕷️ СКИЛЛ: Парсинг (Parsing)", "target": "Внешние сайты и API"},
            {"file": "validation.md", "title": "✅ СКИЛЛ: Валидация (Validation)", "target": "Собранные факты"},
            {"file": "summarization.md", "title": "📝 СКИЛЛ: Саммаризация (Summarization)", "target": "Длинные тексты"},
            {"file": "contradiction_detection.md", "title": "⚠️ СКИЛЛ: Поиск противоречий", "target": "Два разных источника данных"}
        ]
    },
    "CASPER": {
        "desc": "Чистильщик (Дэдпул). Мусор, пустые файлы, угрозы безопасности.",
        "skills": [
            {"file": "backup_and_cleanup.md", "title": "🗑️ СКИЛЛ: Бэкап и чистка", "target": "Корзина / Старые файлы"},
            {"file": "access_control.md", "title": "🔐 СКИЛЛ: Контроль доступа", "target": "Системные файлы Империи"},
            {"file": "integrity_validation.md", "title": "🛡️ СКИЛЛ: Проверка целостности", "target": "YAML-заголовки"},
            {"file": "archive_management.md", "title": "📂 СКИЛЛ: Управление карантином", "target": "Удаленные файлы"},
            {"file": "security_protocols.md", "title": "🚨 СКИЛЛ: Протоколы безопасности", "target": "Защита от RCE / Внешних угроз"}
        ]
    }
}

# Generate Index Content
index_content = "# ГЛАВНЫЙ АРСЕНАЛ (SKILLS INDEX)\n\n"
index_content += "Здесь хранятся все 28 ядерных Скиллов Империи, распределенных по агентам.\n\n"

for agent, data in skills_data.items():
    index_content += f"## {agent}\n"
    index_content += f"**Вектор применения:** {data['desc']}\n\n"
    index_content += "| Скилл | Владелец (Чей) | Кому / Для чего (Вектор) |\n"
    index_content += "|---|---|---|\n"
    
    agent_dir = os.path.join(skills_dir, agent)
    os.makedirs(agent_dir, exist_ok=True)
    
    for skill in data["skills"]:
        # Write individual skill file
        skill_content = f"""---
title: "{skill['title']}"
agent: "{agent}"
target: "{skill['target']}"
tags: ["#skill", "#{agent.lower()}"]
---

# {skill['title']}

**Чей скилл:** {agent}
**Кому / Для чего применяется:** {skill['target']}

## Описание
Данный скилл является официальным протоколом для агента {agent} при работе с объектами типа: {skill['target']}.

## Как использовать
[Заглушка из лора. Здесь будет детальная пошаговая инструкция]

**Отметки:** [[wiki/entities/System/Tools/Skills/SKILLS_INDEX.md|#skills_index]]
"""
        skill_path = os.path.join(agent_dir, skill["file"])
        with open(skill_path, "w", encoding="utf-8") as f:
            f.write(skill_content)
            
        # Add to index
        index_content += f"| [[wiki/entities/System/Tools/Skills/{agent}/{skill['file']}\\|{skill['title']}]] | **{agent}** | {skill['target']} |\n"
    
    index_content += "\n"

# Write the index file
index_path = os.path.join(skills_dir, "SKILLS_INDEX.md")
with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_content)

print("Skills integration completed successfully.")
