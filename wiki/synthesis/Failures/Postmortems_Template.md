# Incident Postmortem Template

## Incident Overview
- **Incident Name**: [e.g., Database Outage, Campaign Failure]
- **Date of Incident**: [YYYY-MM-DD]
- **Authors**: [Agents or Humans involved in the analysis]
- **Status**: [Draft / In Review / Finalized]

## Executive Summary
A brief, 2-3 paragraph summary of what happened, why it happened, the impact it had, and the core resolution.

## Timeline
A detailed chronological breakdown of the incident.
- `[00:00]` - First symptom detected.
- `[00:15]` - Alert triggered by Sentinel.
- `[00:30]` - Initial mitigation attempted.
- `[01:00]` - Issue resolved.

## Root Cause Analysis
Use the "5 Whys" methodology to drill down to the fundamental system or process failure.
1. Why did X happen? Because Y.
2. Why did Y happen? Because Z...

## Impact Assessment
- **Financial**: Estimated revenue lost or excess costs incurred.
- **System**: Downtime, data loss, or resource drain.
- **User/Client**: Number of affected users, impact on trust.

## Corrective Actions
Actionable steps to prevent recurrence.
- [ ] Implement additional rate limiting on API endpoints. (Assigned to: Sentinel)
- [ ] Revise the offer copy to comply with new platform policies. (Assigned to: Offer Specialist)

***
**Отметки:** [[wiki/entities/AGENTS_INDEX|#agent]]
