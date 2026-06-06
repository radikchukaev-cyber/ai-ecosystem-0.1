@echo off
title MNEMOSYNE DAEMON (AI MEMORY AUTO-LOG & GITHUB SYNC)
color 0b
echo ========================================================
echo [MNEMOSYNE DAEMON] Starting Memory Autosave
echo ========================================================
echo The daemon will check for changes every 30 minutes, 
echo update MEMORY.md and sync with GitHub.
echo Do not close this window if you want the tracker to run.
echo ========================================================
python wiki\entities\System\Scripts\memory_autosave.py
pause
