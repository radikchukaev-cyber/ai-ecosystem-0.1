# Навык: Развертывание Архитектуры "Вечный Разум" (Git-Driven Cloud AI)

> [!IMPORTANT] Уровень допуска: VULCAN / RAMS
> Этот навык позволяет агенту с нуля воссоздать автономный Telegram-шлюз на сервере Fly.io, который будет работать независимо от локального терминала, связываясь с Экосистемой исключительно через Git-коммиты в репозиторий GitHub.

## 1. Суть Архитектуры
- **Ввод:** Пользователь пишет в Telegram.
- **Облако:** Сервер Fly.io (FastAPI + webhook) получает сообщение, клонирует/пуллит репозиторий GitHub, генерирует ответ через Gemini API, создает файлы локально на сервере и делает `git commit` + `git push` обратно в GitHub.
- **Локал:** Локальный компьютер через фоновый демон (Мнемозина) каждые 30 минут (или вручную) делает `git pull` и скачивает файлы на жесткий диск.

## 2. Предварительные Требования (Запрос у Шефа)
Прежде чем начать, Агент обязан запросить у Шефа следующие данные:
1. **Telegram Bot Token** (через @BotFather).
2. **GitHub PAT (Personal Access Token)** (с правами Read/Write Contents на целевой репозиторий).
3. **Gemini API Key** (из Google AI Studio, желательно поддерживающий `gemini-3.1-flash-lite` или актуальную модель).
4. **URL репозитория** (формат: `radikchukaev-cyber/ai-ecosystem-0.1`).
5. **URL Telegram-Webhook** (будет получен после `fly launch`).

## 3. Пошаговый Алгоритм Исполнения (Команды для Агента)

### Шаг 3.1: Создание Локального Демона Синхронизации
Агент должен создать скрипт `memory_autosave.py` и `START_MEMORY_DAEMON.bat`, которые будут работать в цикле.
В `memory_autosave.py` **обязательно** должна быть логика `git pull origin main --rebase` перед `git push`:
```python
# Фрагмент кода для memory_autosave.py
def process_memory():
    # 1. Загрузить изменения из облака
    run_cmd("git pull origin main --rebase")
    # 2. Сохранить локальные изменения
    run_cmd("git add .")
    run_cmd('git commit -m "Автосохранение памяти"')
    run_cmd("git push origin main")
```

### Шаг 3.2: Подготовка Кодовой Базы Облака (gateway.py)
Агент должен создать папку для шлюза (например, `OpenClaw_Gateway`) и поместить туда 3 файла:

**1. `requirements.txt`**
```text
fastapi
uvicorn
httpx
python-dotenv
google-generativeai
```

**2. `Dockerfile`**
> [!CAUTION] Установка Git
> Для работы Облака критически важно установить `git` внутрь Docker-контейнера!
```dockerfile
FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "gateway:app", "--host", "0.0.0.0", "--port", "8080"]
```

**3. `gateway.py` (Основная логика)**
Агент должен сгенерировать сервер FastAPI с двумя эндпоинтами.
- `sync_repo()`: клонирует через `https://<PAT>@github.com/...`
- `process_message()`: читает `MEMORY.md`, вызывает `gemini-3.1-flash-lite`, парсит теги `[CREATE_FILE]` и делает `git commit` + `git push`.
*(Полный код gateway.py доступен в текущем репозитории, используйте его как шаблон).*

### Шаг 3.3: Инициализация сервера на Fly.io
Агент использует инструмент `run_command` для выполнения команд в терминале Шефа.
*(Если в PATH нет команды fly, Агент должен найти `C:\Users\<user>\.fly\bin\flyctl.exe`).*

1. Запустить инициализацию:
   ```bash
   flyctl launch --no-deploy
   ```
2. Установить секреты:
   ```bash
   flyctl secrets set TELEGRAM_BOT_TOKEN="<token>" GITHUB_PAT="<pat>" GEMINI_API_KEY="<key>"
   ```
3. Задеплоить сервер в фоновом режиме:
   ```bash
   flyctl deploy
   ```

### Шаг 3.4: Привязка Webhook
После успешного деплоя, Агент должен привязать Telegram к новому облачному серверу через HTTP-запрос (выполняется через curl или Python):
```python
import httpx
url = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://<fly-app-name>.fly.dev/webhook"
httpx.get(url)
```

## 4. Верификация
После деплоя Агент просит Шефа отправить тестовое сообщение боту:
*"Создай тестовый файл в папке N"*
Затем Агент вручную вызывает `git pull` локально и проверяет наличие файла.

---
**Ключ Активации Навыка:** Если Шеф произносит: *"Разверни облачного агента"* или *"Создай такую же систему на другом сервере"* — Агент немедленно загружает этот файл в контекст и исполняет шаги 2-4.
