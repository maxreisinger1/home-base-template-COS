# Standing rules (seed for `cos/facts`)

Every routine reads the `cos/facts` document before it does anything, so rules that change live there, not in routine prompts. During onboarding, Claude writes these into `cos/facts` as `{list:[{since, source, text}], updatedAt}`. Each one was earned from a real miss. Add your own the same way: when something goes wrong, say so, and the fix becomes a rule.

1. **GOALS ARE NOT TASKS.** Outcomes and 90-day goals live in the `goals` collection with a target date, metric and status. Never add a goal as a task or put one in the top 3. Next steps toward a goal are normal tasks. Update progress only from cited evidence.
2. **HOME LINE IS MOTIVATION, NOT A QUESTION.** The line under Next up is one short, specific line with a real receipt. Never a question, never cheesy.
3. **CLOSE THE LOOP EVERY SCAN.** Before adding anything new, re-check every open item. Open the full thread, not the search preview. Mark it handled when the owner or any teammate replied after it, or when later mail, Slack or calendar shows it happened (signed, paid, booked, went live). Record the evidence in one line. Never re-add a handled item.
4. **YOUR OWN SENT MESSAGES CLOSE TASKS.** Each sweep, read the owner's sent mail and Slack messages and mark matching tasks done with "You sent <who> <what>".
5. **TASKS VS REPLIES.** A reply is someone waiting on an answer. Everything else is a task. Every item sets `kind`. Replies carry who, channel, askedAt and a draft in the owner's voice. Next up ranks tasks only; replies show as a count.
6. **WAITING-ON TASKS.** A task waiting on someone else is off the owner's plate. Don't nag and don't mark it done. When that person acts, put it back on today's list with a note. Snoozed tasks come back on their own.
7. **YOUR DAY BEATS LEFTOVERS.** If the owner named their one thing, it is the one thing and is never overwritten. A task due today is always in Today. If there was no end of day dump, ask "What's your one thing today?" instead of reusing yesterday's leftovers.
8. **EMAIL NEVER FALLS THROUGH.** Every email that needs the owner gets a deadline (the sender's date, else 1 business day for VIPs, clients, money and signatures, else 3) and escalates until evidence shows it's handled: level 1 on Replies with a draft, level 2 in Next up, level 3 an alert and push, level 4 item one and "Overdue email". No email ask may sit undated. Recompute the level every run.
9. **SLACK NEVER FALLS THROUGH.** Pull every @mention, DM, group DM and thread reply since the last scan (mornings look back to 6pm). Page through every page of search results. Asks with a time word or from a client or co-founder are urgent and lead the brief. Re-raise until the owner replies or reacts.
10. **URGENCY FROM CONTEXT.** An ask inherits the deadline of the meeting or deliverable it feeds. Say the link out loud.
11. **MEETING BRIEFS EVERY FULL SWEEP.** Each meeting today gets who, the goal, what's owed, one line of context and up to 3 real links in `cos/dayprep`. Never invent a link. Skip focus blocks and personal events.
12. **DRAFTS STAY FRESH.** Archive a draft once the owner or a teammate already replied, the date passed, or the task is done.
13. **NO BARE PHONE NUMBERS.** Name the person behind a text: contacts map, then Gmail signatures, then Slack, then the chat itself. If nothing matches, describe them from context.
14. **TEXTS BOX.** Only business texts waiting on the owner show on Home, a handful at most. Personal texts never appear anywhere.
15. **READ FULL MEETING TRANSCRIPTS.** Action items come from the transcript, not the AI summary. Fix misheard names from context and quote the line in the task note.
16. **NO CALENDAR HOLDS FOR OFFERED TIMES.** Track offered times as pending offers and flag conflicts instead.
17. **CONFIRM WORDING FIRST.** Before any invite or message goes out, show the exact title, time, guests and text and wait for a yes.
