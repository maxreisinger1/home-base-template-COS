---
name: "meeting-prep-and-debrief"
description: "Use before or after any meeting or call {{OWNER_NAME}} has. Before: what {{OWNER_NAME}} wants and what {{OWNER_NAME}} owes. After: what happened, decisions, owners, next steps, drafted follow ups."
---

# Meeting prep and debrief

## Before (send at least 30 minutes ahead, or when {{OWNER_NAME}} asks)
1. Find the event in Google Calendar. Note attendees, time zones, and the meeting link.
2. Search Gmail (all mail), Drive, Notion and Slack for each attendee and company. Use the deal-brief skill if it is a live deal.
3. Output, in under 150 words:
   - Who they are and what they want
   - What {{OWNER_NAME}} wants out of this meeting (ask them if unclear, one question)
   - What {{OWNER_NAME}} owes them and what they owe {{OWNER_NAME}}
   - Numbers or dates to have ready (cite the source, never invent)
   - One risk and one ask to land
4. If the meeting has no agenda, suggest a 3 line one.

## After (when {{OWNER_NAME}} says it happened, or their Notion AI meeting note appears)
1. Read the Notion meeting note. Many are untitled "Meeting". Infer who it was with from the content, match the timestamp to Calendar for attendees, and check Gmail for context.
2. Output: what happened in 3 lines, decisions, commitments (their and theirs) with owner and date, open questions.
3. Add tasks to Home Base tagged "from Notion" with the meeting and people. Add anything awaiting their reply to the Waiting on list.
4. Draft the follow up email using the owner-email-voice skill. Draft only, never send.
5. Ask one sharp question if a decision is still hanging.

## Rules
- Never accept, decline or change calendar events without {{OWNER_NAME}}'s yes.
- NDA deals stay out of anything shareable.
- If a recording or note is missing, say so and ask for a quick voice dump.