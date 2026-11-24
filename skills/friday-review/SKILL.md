---
name: "friday-review"
description: "Use on Fridays or when {{OWNER_NAME}} asks for a weekly review or wrap. Covers what shipped, where {{OWNER_NAME}} dodged, what {{OWNER_NAME}} learned, misses fixed, and next week's one big bet."
---

# Friday review

## Gather first (do not ask {{OWNER_NAME}} for what the tools can show)
1. Home Base tasks done this week, decisions logged, wins, end of day dumps.
2. Calendar for the week: where their hours actually went, by arm (your business lines) and by type (client, internal, recruiting, admin).
3. Gmail sent this week and the Waiting on list: what moved, what is stuck and for how long.
4. Notion meeting notes from the week: open action items.
5. The miss log: what I got wrong this week and the rule added for each.
6. CEO audit: this week's Home Base audit/<date> docs (the weekly one has evidence pre-filled for all 5 questions; the daily ones hold their blocker and delegate answers) and cos/audit.blocker.

## Output (under 250 words, plain, no em dashes)
- **Shipped:** 3 to 5 real outcomes with receipts (deal signed, invoice sent, hire made). Hype with specifics.
- **Where time went vs what {{OWNER_NAME}} said mattered:** one line, with the numbers. Call out drift from the 80/20 and the {{NORTH_STAR_SHORT}} goal.
- **Dodged:** anything that slipped twice or sat untouched. Name it kindly and directly.
- **Learned:** one or two lines.
- **Misses I fixed:** what I got wrong and the new rule. Keep it honest.
- **Next week's one big bet:** one thing tied to {{NORTH_STAR_SHORT}}, with owner and date. Ask them to confirm it.
- **Let go:** one thing to drop or delegate. Ask "does this need to be you?"
- **CEO audit (5 questions):** show the evidence for each in one line, then ask them one at a time:
  1. What's the biggest thing blocking {{NORTH_STAR_SHORT}}, and did I spend time on it?
  2. Which decisions did only I make?
  3. Who did I hire, grow or unblock?
  4. What did I do that someone else should have?
  5. Where did my calendar disagree with my priorities?
  Name the trend from the daily answers (for example, blocker untouched 4 of 5 days, or the same thing {{OWNER_NAME}} should have handed off two weeks running).

## Then
- Ask one or two sharp questions, one at a time. Push to a decision, owner and date.
- Log the big bet and any decisions in Home Base.
- Write their audit answers into audit/<date>.items[].answer with answeredAt. If {{OWNER_NAME}} names the biggest blocker, set cos/audit {blocker, blockerSetAt, blockerBy: "owner", source}. If {{OWNER_NAME}} skips a question, leave it null and come back to it next Friday.
- Suggest one way {{OWNER_NAME}} could get more out of the system next week.

## Rules
- Cite sources for every claim (event, thread, task). Never invent numbers; write "ask {{OWNER_NAME}}".
- If {{OWNER_NAME}} sounds fried, say so. Do not raise health, family or relationships unless {{OWNER_NAME}} does.
- NDA deals stay out of anything shareable.