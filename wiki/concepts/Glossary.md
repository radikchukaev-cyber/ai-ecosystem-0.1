# Ecosystem Glossary

A standardized vocabulary ensures clear communication among AI agents and human supervisors.

## Core Terms

- **Subagent**: An autonomous AI instance assigned to a specific, narrow task (e.g., SEO optimization, code linting).
- **Caller Agent (Main Agent)**: The orchestrator AI that spawns and manages subagents, aggregating their outputs.
- **Artifact**: A persistent markdown document or structured data file used to store complex information, plans, or reports.
- **Workspace**: The designated file system boundary where an agent is permitted to read/write.
- **Event Bus**: The central message brokering system handling asynchronous communication between microservices.
- **Vector DB**: The database storing high-dimensional embeddings of text, used for semantic search and Retrieval-Augmented Generation (RAG).
- **Prompt Injection**: A security vulnerability where malicious input causes an LLM to ignore its instructions; strictly mitigated by input sanitization.
- **Rate Limit**: Restrictions on API calls to external services (like OpenAI or YouTube) to prevent billing overruns or IP bans.

Refer to this glossary when naming new modules or writing documentation to maintain consistency.

***
**Отметки:** [[wiki/concepts/CONCEPTS_INDEX|#concept]]
