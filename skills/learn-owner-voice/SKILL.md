---
name: "learn-owner-voice"
description: "Use every time a draft is written for {{OWNER_NAME}} (email card, Gmail draft, Slack or text draft) and every time {{OWNER_NAME}} sends one, to compare our draft with what {{OWNER_NAME}} sent and teach the voice profile."
---

# Learn the owner's voice

Goal: every edit {{OWNER_NAME}} makes to a draft makes the next draft better, without them asking and without burning credits. Read only. This skill never sends, edits or deletes mail.

## The files (all in {{VOICE_FOLDER}}/)
- voice-profile.md: the living profile. Every draft reads it first. 60 lines max.
- lessons.md: raw log, one line per compared draft.
- pending/: one small file per draft that is waiting to be compared.
- archive/: lessons older than 30 days.

## Step 1. When you write a draft for {{OWNER_NAME}} (any session, any model)
1. Read voice-profile.md, then the owner-email-voice skill. The profile wins where they differ.
2. Right after showing the draft, save it as pending/YYYY-MM-DD-recipient-topic.md with: to, subject, channel (card, gmail draft, slack, text), where it was shown, and the exact body. This is the step that makes learning possible. A draft that is not saved cannot be compared.
Drafts on the Home Base Drafts shelf are already stored in the dashboard database (drafts collection), so those need no file.

## Step 2. When {{OWNER_NAME}} sends (free, do it on the spot)
If {{OWNER_NAME}} presses Send on the card or says it is sent while you are still in the conversation, you already have both versions. Compare them right there, add one line to lessons.md, delete the pending file. No extra run needed.

## Step 3. Daily catch-up for edits made in Gmail (Haiku, silent)
A scheduled task on Haiku, once each weekday evening, posts nothing in chat:
1. For each file in pending/ and each ready email draft on the Drafts shelf from the last 7 days, search Gmail sent mail (to the same person, after the draft date) and open the match.
2. No match after 7 days: log "not sent" and delete the pending file. Do not guess why.
3. Match found: compare line by line and write one line in lessons.md with the date, who, the type of email, the verdict (as-is, light edit, heavy edit), exactly what {{OWNER_NAME}} cut, added and changed (quote their words), and a one-line lesson.
4. Look at: opener, closing and sign-off, length (word count ours vs their), exclamation marks and energy, words {{OWNER_NAME}} swapped, anything {{OWNER_NAME}} added that we could not have known (new facts or asks are context, not voice, so tag them "context"), and anything {{OWNER_NAME}} removed.
5. A draft sent as-is is a lesson too: log it as "as-is" so we know what is working.
Haiku only extracts and quotes. It never rewrites the profile.

## Step 4. Weekly tidy (Sonnet, once a week, silent unless something changed)
1. Read the week's lessons and the profile.
2. Promote a pattern to Confirmed only if it showed up 2 or more times, or {{OWNER_NAME}} said it outright. One-offs go to Watching. Three weeks in Watching with no repeat: drop it.
3. When a new lesson contradicts an old rule, the newer one wins. Note the date.
4. Keep the profile under 60 lines: merge near-duplicates, cut anything the owner-email-voice skill already says, move old lessons to archive/.
5. If the profile changed, tell {{OWNER_NAME}} in 3 lines at most: what I learned this week, with one example in their words.
6. Once a month, if Confirmed has 5 or more rules the skill lacks, propose an updated owner-email-voice card so the skill itself catches up.

## Rules
- Never learn from their typos or dictation slips. Clean them.
- Voice is how {{OWNER_NAME}} says it. Facts {{OWNER_NAME}} added are context. Do not turn "{{OWNER_NAME}} added a question about contracts" into a rule to always ask about contracts.
- Recipient type matters. Log who it was to (client, team, candidate, lawyer, friend) so a lesson from a friend email does not leak into client emails.
- NDA deals: log the lesson, never the content.
- If the files cannot be read or written, say so in one line and carry on with the skill as written.

## Why it is cheap
The compare is a few short emails a day on the cheapest model. The profile is one short file, so reading it adds almost nothing to each draft. The expensive models never do this work.