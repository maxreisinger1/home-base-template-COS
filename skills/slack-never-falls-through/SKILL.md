---
name: "slack-never-falls-through"
description: "Use on every Home Base sweep, morning brief or 'what did I miss' for {{OWNER_NAME}}, so Slack @mentions, DMs and asks with deadlines get caught and resurfaced until handled."
---

# Slack never falls through

## Every sweep
1. Search Slack since the last sweep (overnight: since 6pm yesterday) for:
   - messages that @mention {{OWNER_NAME}}, in any channel or thread
   - all DMs and group DMs to {{OWNER_NAME}}
   - thread replies on threads {{OWNER_NAME}} started or posted in
2. Flag as time-sensitive when it has a deadline or time word (by noon, tmrw, today, EOD, ASAP, before the call, a date), asks them to approve, check, review, sign or decide, or comes from a client channel (client shared channels).
3. Check whether {{OWNER_NAME}} already handled it: a reply from {{OWNER_NAME}} after the message, a reaction from {{OWNER_NAME}}, or the ask done elsewhere. If handled, drop it.
4. Add each unhandled ask to Home Base as a task with the deadline, the person, a one-line summary and the Slack link. Put deadline-today items at the top of Next up.
5. Keep re-surfacing every sweep until handled. Escalate when under 2 hours to the deadline: post one line in the project chat.

## Rules
- Drafts only. Never post in Slack without {{OWNER_NAME}}'s yes on the exact wording.
- Group email and Slack asks into one list in the morning brief, sorted by deadline.
- Personal or social chatter is not a task.