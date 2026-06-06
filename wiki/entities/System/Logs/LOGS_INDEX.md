# System Logs - Master Index

## 1. Logging Philosophy
Logs are the lifeblood of the AI Empire's self-improvement mechanisms. We do not just log errors; we log intent, execution, and outcomes to train future iterations of the agents.

## 2. Log Categories
- **Action Logs:** Records of every tool call made by an agent, including inputs and outputs.
- **Cognitive Logs:** Snapshots of the agent's internal reasoning process ("scratchpad" or "thought" blocks).
- **Error Logs:** Stack traces, API timeouts, and unexpected system states.
- **Financial Logs:** Transactional data, API cost tracking, and revenue events.

## 3. Retention & Storage Policy
- **Hot Storage (0-7 Days):** Searchable, indexed in Elasticsearch for immediate debugging.
- **Warm Storage (7-30 Days):** Compressed, available for mid-term trend analysis and performance reviews.
- **Cold Storage (30+ Days):** Aggregated and archived in S3-compatible object storage. Used only for bulk training of foundation models.

## 4. Alert Thresholds
- **Critical:** System unbootable, core APIs down, or unauthorized access attempts. Triggers immediate pager notifications.
- **Warning:** Elevated error rates, nearing API quotas, or abnormal latency. Logs are flagged for review by the Maintenance Agent.
- **Info:** Routine operations proceeding normally.

***
**Отметки:** [[wiki/entities/System/SYSTEM_INDEX|#system-logs]]
