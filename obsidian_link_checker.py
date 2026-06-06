import os
import re

user_text = """
## 📥 ШЛЮЗЫ И СЫРЬЕ
Сюда попадает вся необработанная информация из внешнего мира.
* [[wiki/raw/assets/|Assets]] (Картинки, видео, PDF)
* [[wiki/raw/sources/|Sources]] (Внешние мануалы)
* [[wiki/raw/transcripts/|Transcripts]] (Расшифровки)
* [[wiki/raw/web-clipped/|Web-clipped]] (Дампы сайтов)  * [[wiki/sources/|Обработанные выжимки фактов]] * [[wiki/synthesis/Canvases/|Визуальные схемы]]
* [[wiki/synthesis/Archive/|Архив]]  * [[wiki/entities/System/Configs/Root_Configs/|Конфигурации Системы]]
* [[wiki/entities/System/Audit/|Логи Аудита]]
* [[wiki/entities/Companies/|Компании]] Ы: [[wiki/entities/System/Configs/Root_Configs/]] [[wiki/entities/System/Configs/OBSIDIAN_PLUGINS/]] [[wiki/entities/Agents/RAMS/]]: [[wiki/entities/Agents/VULCAN/]]: [[wiki/entities/Agents/ARGUS/]]  [[wiki/entities/Agents/MNEMOSYNE/]]  [[wiki/entities/Agents/SOCRATES/]] : [[wiki/entities/Agents/CASPER/]]  
YouTube Team: [[wiki/entities/Agents/YouTube_Researcher/]] ← для видео-проектов
             [[wiki/entities/Agents/Writer/]]
             [[wiki/entities/Agents/Thumbnail_Agent/]]
             [[wiki/entities/Agents/Packaging_Agent/]]
             [[wiki/entities/Agents/Analytics_Agent/]]

Business Trio: [[wiki/entities/Agents/Market_Researcher/]] ← для бизнеса
              [[wiki/entities/Agents/Offer_Strategist/]]
              [[wiki/entities/Agents/Execution_Agent/]]

Health: [[wiki/entities/Agents/Health_Assistant/]] ← для здоровья Шефа

ЭТАЖ 3: ЗНАНИЯ (wiki/concepts/ + wiki/sources/)
┌─ 📚 КОНЦЕПТЫ (Законы архитектуры): [[wiki/concepts/]] : [[wiki/synthesis/History/]]  : : [[wiki/synthesis/Legacy_2_Wiki/]] [[wiki/synthesis/Canvases/]]  [[wiki/synthesis/Archive/]]: [[wiki/entities/System/Configs/]] ─ [[Root_Configs/]]    └─ [[.env]]   🛠️ СКИЛЛЫ (ИНСТРУМЕНТЫ): [[wiki/entities/System/Tools/Skills/]] #tools
│  ├─ [[obsidian-cli/]] — работа с Obsidian из скриптов ← ЗДЕСЬ
│  ├─ [[github-sync/]] — синхронизация с GitHub ← ЗДЕСЬ
│  ├─ [[json-parser-safe/]] — безопасный парсинг JSON ← ЗДЕСЬ
│  ├─ [[vector-search/]] — семантический поиск ← ЗДЕСЬ
│  ├─ [[youtube-api-wrapper/]] — обертка YouTube API ← ЗДЕСЬ
│  └─ [[references/]] — до [[wiki/entities/System/Tests/]]: [[raw/]] #incoming
│  ├─ [[raw/assets/]] — картинки, видео, PDF
│  │  ├─ youtube_thumbnails/
│  │  ├─ screenshots/
│  │  └─ documents/
│  │
│  ├─ [[raw/sources/]] — внешние мануалы, статьи
│  │  ├─ claude_documentation.pdf
│  │  ├─ youtube_api_reference.md
│  │  └─ github_guides/
│  │
│  ├─ [[raw/transcripts/]] — голосовые записи Шефа, расшифровки
│  │  ├─ 2024-01-15_meeting_transcript.md
│  │  └─ voice_notes/
│  │
│  └─ [[raw/web-clipped/]] — дампы с веб-сайтов─ [[wiki/synthesis/History/]] #memory #success
│  ├─ [[wiki/concepts/]] ─ [[wiki/entities/System/Scripts/]] #code #python
│  ├─ [[wiki/concepts/Code_Patterns.md]] #code #templates
│  ├─ [[wiki/entities/Agents/VULCAN/]] # ├─ [[wiki/entities/System/Tools/Scripts/]] #tools #code
│  ├─ [[wiki/entities/System/Tools/Skills/]]  #ВИДЕО (YouTube проект)
│  ├─ [[wiki/concepts/YouTube_Workflow.md]] #youtube #workflow
│  ├─ [[wiki/entities/Agents/YouTube_Researcher/]] #youtube
│  ├─ [[wiki/synthesis/History/YouTube_*]] #youtube #examples
│  └─ Полный цикл: идея → скрипт → видео → аналитика
│
├─ #БИЗНЕС (Business Trio)
│  ├─ [[wiki/concepts/Business_Trio_Process.md]] #business #strategy
│  ├─ [[wiki/entities/Agents/Market_Researcher/]] #business
│  └─ [[wiki/entities/Companies/]] #business #projects
│
├─ #ОШИБКА (Что-то упало?)
│  ├─ [[wiki/synthesis/Failures/]] #error #learning
│  ├─ [[wiki/entities/Agents/SOCRATES/]] #error #analysis
│  └─ Поиск похожей ошибки → смотри как исправляли
│     ├─ medium_articles/  ├─ [[wiki/synthesis/History/]] 
"""

links = re.findall(r'\[\[(.*?)\]\]', user_text)
vault_dir = r"D:\.antigravity\AI-ИМПЕРИИ3"
missing_for_obsidian = []

for raw_link in links:
    link = raw_link.split('|')[0].strip()
    if not link:
        continue
    
    if link.endswith('/'):
        # For a folder link [[folder/]], Obsidian Folder Notes plugin expects folder/folder.md
        # Or standard obsidian might expect folder.md
        folder_path = os.path.join(vault_dir, link.replace('/', os.sep))
        folder_name = os.path.basename(link.strip('/'))
        note_inside = os.path.join(folder_path, folder_name + ".md")
        note_outside = os.path.join(vault_dir, link.strip('/').replace('/', os.sep) + ".md")
        
        if not os.path.exists(note_inside) and not os.path.exists(note_outside):
            missing_for_obsidian.append(link)
    else:
        # Standard file
        if not link.endswith('.md') and '.' not in link:
            file_path = os.path.join(vault_dir, link.replace('/', os.sep) + ".md")
        else:
            file_path = os.path.join(vault_dir, link.replace('/', os.sep))
            
        if not os.path.exists(file_path):
            # Try to search it
            filename = os.path.basename(file_path)
            found = False
            for root, dirs, files in os.walk(vault_dir):
                if filename in files:
                    found = True
                    break
            if not found:
                missing_for_obsidian.append(link)

missing_for_obsidian = sorted(list(set(missing_for_obsidian)))
print("TOTAL BROKEN LINKS IN OBSIDIAN'S EYES:", len(missing_for_obsidian))
for m in missing_for_obsidian:
    print("- " + m)
