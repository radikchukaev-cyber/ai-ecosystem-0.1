# Subagent Delegation Rules

To maintain order and efficiency, Caller Agents must follow strict rules when delegating tasks to Subagents.

## Delegation Criteria
1. **Scope Definition**: Tasks must be narrow, well-defined, and have clear success criteria.
2. **Resource Limits**: Subagents must be launched with strict token limits, timeout durations, and memory boundaries.
3. **Context Minimization**: Only pass the absolute minimum context required for the subagent to perform its task. Do not send entire codebases if only a single file needs review.

## Lifecycle Management
- **Monitoring**: The Caller Agent must actively monitor the status of its Subagents.
- **Handling Failures**: If a Subagent fails or times out, the Caller Agent must either retry with a clearer prompt/adjusted parameters or escalate to the human supervisor.
- **Termination**: Once a Subagent returns its result via `send_message`, the Caller Agent must ensure the Subagent process is gracefully terminated to free up resources.

Proper delegation prevents runaway costs and ensures the swarms operate cohesively.

***
**Отметки:** [[wiki/concepts/CONCEPTS_INDEX|#concept]]
