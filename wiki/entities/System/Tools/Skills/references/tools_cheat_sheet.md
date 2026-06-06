# Tools Cheat Sheet

Welcome to the ultimate cheat sheet for the tools and skills available within the AI Empire ecosystem. This reference guide provides quick syntax examples, usage tips, and integration patterns for developers and agents.

## Core Utilities

### `github-sync`
- **Purpose:** Synchronize local repositories with remote branches.
- **Usage:** Run `python sync_script.py` in the workspace directory.
- **Env Vars:** `WORKSPACE_DIR`

### `obsidian-cli`
- **Purpose:** Read and write Obsidian markdown files programmatically.
- **Usage:** Instantiate `ObsidianVault(path)` and call `create_note(title, content)`.
- **Key Feature:** Extracts wikilinks automatically.

### `json-parser-safe`
- **Purpose:** Parse malformed JSON from LLM outputs.
- **Usage:** `SafeJsonParser.parse(inputString)`
- **Capabilities:** Fixes trailing commas, missing quotes, and extracts from markdown blocks.

## Advanced Integrations

### `vector-search`
- **Platform:** Pinecone
- **Capabilities:** Upsert embeddings, semantic search, RAG context retrieval.
- **Tip:** Always batch your upserts for better performance.

### `youtube-api-wrapper`
- **Purpose:** Fetch metadata, captions, and analytics from YouTube.
- **Setup:** Requires `client_secret.json` for OAuth 2.0 flow.

Keep this cheat sheet handy when designing new workflows or expanding agent capabilities!

***
**Отметки:** [[wiki/entities/System/Tools/TOOLS_INDEX|#tools]]
