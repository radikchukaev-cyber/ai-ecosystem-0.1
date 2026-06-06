#!/usr/bin/env python3
# purge_stubs.py — VULCAN Sanitation Protocol
# Удаляет файлы-заглушки из экосистемы AI-ИМПЕРИИ3

import os
import sys
from pathlib import Path

ROOT = Path(r"D:\.antigravity\AI-ИМПЕРИИ3")

# Маркеры заглушек
STUB_MARKERS = [
    "Файл памяти агента. Ждет заполнения рабочими данными.",
    "Скилл агента. Ожидает детальной настройки инструкций.",
    "Системный документ инфраструктуры CARPATH.",
    "ВРЕМЕННО ЗАМОРОЖЕНО.",
]

# Папки-исключения (относительные пути от ROOT)
EXCLUDED_DIRS = [
    "wiki/templates",
    "wiki\\templates",
    "RAMS.Awakening",
    "VULCAN",
    "AI-ИМПЕРИИ",
    ".obsidian",
]

def is_excluded(filepath: Path) -> bool:
    """Проверяет, находится ли файл в исключённой директории."""
    try:
        rel = filepath.relative_to(ROOT)
    except ValueError:
        return False
    parts = rel.parts
    for excluded in EXCLUDED_DIRS:
        excl_parts = Path(excluded).parts
        # Проверяем, начинается ли путь с исключённой папки
        if parts[:len(excl_parts)] == excl_parts:
            return True
        # Дополнительная проверка: если любая часть пути совпадает с именем исключённой папки (однокомпонентные)
        if len(excl_parts) == 1 and excl_parts[0] in parts:
            return True
    return False

def is_stub(filepath: Path) -> bool:
    """Проверяет, содержит ли файл маркер заглушки."""
    try:
        content = filepath.read_text(encoding="utf-8", errors="ignore")
        for marker in STUB_MARKERS:
            if marker in content:
                return True
    except Exception as e:
        print(f"  [WARN] Не удалось прочитать {filepath}: {e}")
    return False

def main():
    deleted_files = []
    deleted_dirs = set()
    skipped_excluded = 0
    errors = []

    print("=" * 60)
    print("  VULCAN PURGE PROTOCOL — Санация заглушек")
    print(f"  Корень: {ROOT}")
    print("=" * 60)

    all_md = list(ROOT.rglob("*.md"))
    print(f"\n  Найдено .md файлов: {len(all_md)}")
    print("-" * 60)

    for filepath in sorted(all_md):
        if is_excluded(filepath):
            skipped_excluded += 1
            continue

        if is_stub(filepath):
            try:
                filepath.unlink()
                rel = filepath.relative_to(ROOT)
                deleted_files.append(str(rel))
                deleted_dirs.add(str(rel.parent))
                print(f"  [УНИЧТОЖЕН] {rel}")
            except Exception as e:
                errors.append(f"{filepath}: {e}")
                print(f"  [ОШИБКА] {filepath}: {e}")

    print("\n" + "=" * 60)
    print(f"  ИТОГ:")
    print(f"  • Уничтожено файлов: {len(deleted_files)}")
    print(f"  • Пропущено (защищённые зоны): {skipped_excluded}")
    print(f"  • Ошибок: {len(errors)}")
    print(f"  • Затронутые директории ({len(deleted_dirs)}):")
    for d in sorted(deleted_dirs):
        print(f"      — {d}")
    if errors:
        print(f"\n  ОШИБКИ:")
        for e in errors:
            print(f"      {e}")
    print("=" * 60)

    # Сохраняем отчёт
    report_path = ROOT / "purge_report.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("VULCAN PURGE REPORT\n")
        f.write("=" * 60 + "\n")
        f.write(f"Уничтожено файлов: {len(deleted_files)}\n")
        f.write(f"Пропущено (защита): {skipped_excluded}\n")
        f.write(f"Ошибок: {len(errors)}\n\n")
        f.write("ЗАТРОНУТЫЕ ДИРЕКТОРИИ:\n")
        for d in sorted(deleted_dirs):
            f.write(f"  — {d}\n")
        f.write("\nСПИСОК УНИЧТОЖЕННЫХ ФАЙЛОВ:\n")
        for fp in deleted_files:
            f.write(f"  {fp}\n")
        if errors:
            f.write("\nОШИБКИ:\n")
            for e in errors:
                f.write(f"  {e}\n")

    print(f"\n  Отчёт сохранён: {report_path}")
    return len(deleted_files), deleted_dirs

if __name__ == "__main__":
    main()
