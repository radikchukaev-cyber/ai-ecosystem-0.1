# System Scripts - Master Index

## 1. Overview
This directory serves as the central repository for all automation, deployment, and utility scripts used across the AI Empire ecosystem. These scripts act as the muscle, executing commands initiated by the cognitive agents.

## 2. Core Categories
- **`/deploy`**: Scripts for provisioning servers, updating Docker containers, and managing CI/CD pipelines.
- **`/maintenance`**: Automated database backups, log rotation, and garbage collection routines.
- **`/monitoring`**: Health check scripts that ping API endpoints and verify agent uptime.
- **`/data_pipeline`**: ETL (Extract, Transform, Load) scripts for moving data between scrapers, databases, and LLM context windows.

## 3. Execution Policies
- All scripts must be idempotent (can be run multiple times without causing unintended side effects).
- Execution must be logged centrally via the unified logging interface.
- Destructive scripts (e.g., database drops, large-scale deletion) require a cryptographic key sign-off from a Tier 1 Agent.

## 4. Adding New Scripts
- Create a new file with the standard `.py` or `.sh` extension.
- Include a docstring detailing inputs, outputs, and side effects.
- Register the script in the `available_scripts.json` manifest to make it discoverable by agents.

***
**Отметки:** [[wiki/entities/System/SYSTEM_INDEX|#system-scripts]]
