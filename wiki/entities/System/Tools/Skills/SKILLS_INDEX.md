# AI Skills & Tools - Master Index

## 1. Skill Architecture
The AI ecosystem relies on a modular skill system. Agents are essentially empty cognitive shells until equipped with specific "Skills" (Tools) that allow them to interact with their environment.

## 2. Core Skill Modules
- **FileOps:** Reading, writing, modifying, and traversing the local filesystem.
- **WebInteract:** Scraping web pages, interacting with forms, and bypassing basic anti-bot measures.
- **CodeExecution:** Sandboxed execution of Python, Node.js, and shell scripts.
- **API_Gateway:** Standardized methods for communicating with external services (Twitter, YouTube, Stripe).

## 3. Custom Tool Integration
To add a new skill to an agent:
1. Define the tool schema in OpenAPI format.
2. Implement the backend logic in the `/Tools` directory.
3. Bind the tool to the specific agent's execution context.
4. Provide prompt-level instructions on when and how the agent should utilize the tool.

## 4. Versioning & Deprecation
- Skills are versioned (v1, v2, etc.). Breaking changes must introduce a new version rather than modifying the existing one to preserve backward compatibility for legacy agents.
- Deprecated skills will log a warning when invoked and will be removed entirely after 90 days.

## 5. Recent Additions
- **OpenClaw_Gateway:** Telegram integration gateway for asynchronous communication.

***
**Отметки:** [[wiki/entities/System/SYSTEM_INDEX|#system-skills]]
