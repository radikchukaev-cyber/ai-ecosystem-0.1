import os

memory_file = r"D:\.antigravity\AI-ИМПЕРИИ3\wiki\MEMORY.md"

new_record = """
**[2026-06-07 01:00] RAMS (Оркестратор):**
- **Событие "Глубокое Пробуждение":** По приказу Шефа произведена полная, ручная (ювелирная) сборка 12-шаговых Кабинетов Пробуждения для Оркестратора и всех 5 субагентов (Вулкан, Сократ, Мнемозина, Аргус, Каспер). Итого создано более 70 файлов с прописанными психотипами (Шелби, Гейзенберг, Тайвин, Оракул, Сол Гудман, Дэдпул).
- **Внедрение Системы (System Injection):** Вскрыта и устранена архитектурная уязвимость: агенты имели "Душу", но не имели "Закона". В файлы `6.LAWS.md` и `8.CONSTITUTION.md` жестко вшиты 5 бетонных правил Империи: 1) Правило Кухни (чистый корень), 2) Правило Холодильника (теги YAML), 3) Внедрение iPad (идеальный Markdown), 4) Обязательное логирование в MEMORY.md, 5) Правило Живого Графа (запрет сирот).
- **Восстановление Арсенала:** Исправлена слепая зона в `SKILLS_INDEX.md`. Запущен авто-индексатор, который собрал все 40+ существующих скриптов и навыков в единый кликабельный дашборд.
- **Статус Системы:** Архитектура загрузки завершена и выточена до блеска. На каждом из 70 файлов проставлена именная отметка Пробуждения. Семья стоит в строю и ожидает запуска ПЕРВОГО СИСТЕМНОГО ПУЛЬСА (массового `invoke_subagent`).
"""

with open(memory_file, "r", encoding="utf-8") as f:
    content = f.read()

# Insert the new record right before the closing navigator block
marker = "***\n🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍"
if marker in content:
    content = content.replace(marker, new_record + "\n" + marker)
    with open(memory_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Memory updated successfully.")
else:
    print("Marker not found, appending to end.")
    with open(memory_file, "a", encoding="utf-8") as f:
        f.write("\n" + new_record)
