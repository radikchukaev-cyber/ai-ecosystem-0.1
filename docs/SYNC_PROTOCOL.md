# Протокол синхронизации Telegram-GitHub
Данный протокол обеспечивает сохранение диалогов Шефа и Агента в репозиторий даже при закрытом терминале. 
1. Telegram-сервер принимает сообщение.
2. Агент записывает сообщение в /tmp/ai-ecosystem/history/telegram_buffer.md.
3. Демон Мнемозины (memory_autosave.py) при запуске выполняет:
   - git pull (синхронизация с облаком)
   - git add history/telegram_buffer.md
   - git commit -m "AUTOSAVE: Telegram interaction sync"
   - git push