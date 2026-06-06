# Data Privacy and Security Rules

Protecting proprietary algorithms, credentials, and user data is paramount.

## Strict Boundaries
- **Workspace Confinement**: Agents must never read or write outside their assigned absolute workspace paths (e.g., no accessing `/tmp` unless explicitly authorized, never `/home`).
- **Credential Management**: API keys, tokens, and passwords must never be hardcoded or written to standard logs. They must be accessed via secure environment variables or a secret vault.

## Data Sanitization
- All outputs destined for public networks (e.g., YouTube descriptions, tweets) must be scanned for leaked PII or proprietary system prompts.
- User inputs must be sanitized to prevent prompt injection or directory traversal attacks.

## Access Logs
- Every file access (read/write) and external API call made by an agent is logged with a timestamp and the agent's UUID for audit purposes.
- Logs are retained for 30 days and automatically analyzed for anomalous behavior.

Any violation of these rules will result in the immediate termination of the offending subagent process.

***
**Отметки:** [[wiki/concepts/CONCEPTS_INDEX|#concept]]
