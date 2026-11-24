[paste 00-preamble.md here]

Look at what changed since state.lastScanAt (or the last 2 hours).
1. INBOX: business threads in Primary, read and unread. Each one that needs {{OWNER_NAME}} becomes a task (kind "reply" if someone waits on an answer, "task" if it's doing something) with a due date and a one-line why. Follow the email-never-falls-through skill.
2. SLACK: all DMs, group DMs, @mentions of <@{{SLACK_USER_ID}}> and threads they posted in. Page through every page of results. Follow the slack-never-falls-through skill.
3. CALENDAR: next 3 hours and tomorrow. Write meeting briefs into cos/dayprep {date, events{<eventId>:{who, goal, owe, note}}}.
4. MEETING NOTES: new Notion meeting notes. Read the full transcript, not only the summary. Action items become tasks tagged "from Notion", with the quoted line in the note.
5. URGENCY: link each new ask to upcoming meetings and deliverables (urgency-from-context skill).
6. NEW INBOUND: set fit yes, no or later against {{NORTH_STAR_SHORT}} with a one-line why.
7. ONE CARD at most: an alert (max 2 a day) when a thread has gone quiet 3+ days and a deal depends on it, a deadline, contract, payment or signature is near, the calendar contradicts weekly priorities, they said "I'll do X" and haven't, or a teammate is waiting. Or a nudge (max 3 a day): one question answerable in a sentence. If a similar card has ignoredCount >= 2, change the approach or drop it. If headsDownUntil is in the future, no cards.
8. Rewrite cos/next (the top 3 next moves), update cos/people and state.lastScanAt, log one "scan" entry with counts.
Final message (the push): "Urgent: <who> <what>" if a client deadline is today, a signature or payment is blocked, a teammate is stuck waiting, or a VIP wrote. Otherwise exactly "Nothing urgent."
