import os
import subprocess
import time

def sync_memory():
    # Принудительная синхронизация для предотвращения конфликтов
    subprocess.run(["git", "pull", "origin", "main"], check=True)
    
    # Логика сохранения (заглушка для демонстрации)
    print("Синхронизация памяти завершена: push в репозиторий...")
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "AUTO-SAVE: Memory update from Telegram/Local"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)

if __name__ == "__main__":
    while True:
        sync_memory()
        time.sleep(1800) # 30 минутный цикл