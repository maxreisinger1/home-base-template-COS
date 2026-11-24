---
name: "onboard-home-base"
description: "Use when someone says 'onboard me', 'set up Home Base' or opens this template for the first time. Walks them through setup step by step and shows what it learned at each step."
---

# Onboard Home Base

Goal: in about 30 minutes they have a live dashboard that already knows their world. Make it feel like the system is plugging into their life and learning fast: after every step, show real things you found (names, counts, deals, dates), not "done". Short, warm, one step at a time. Never send, reply, post or change anything during onboarding.

Keep a visible checklist the whole way through and tick it as you go.

## Step 1. Five questions (one at a time, voice dumps welcome)
1. Name, role, company, city and time zone.
2. The one number you're chasing (north star) and your three 90-day goals.
3. Co-founders and the team: who owns what.
4. VIPs (people whose messages always come first) and meeting hours you want protected.
5. What should I push you on? Where do you dodge?
Fill every `{{PLACEHOLDER}}` in the repo from the answers. Read them back in 5 lines and get a yes.

## Step 2. Connect accounts
Check each connector and offer the missing ones: Gmail, Google Calendar, Google Drive, Slack, Notion. After each one connects, prove it with a receipt:
- Gmail: "I can see N threads from the last 30 days. Top senders: A, B, C."
- Calendar: "You have N meetings this week, N hours. Busiest day is X."
- Slack: "N DMs and mentions waiting. Most active channels: ..."
- Notion: "Found N meeting notes from the last 2 weeks."

## Step 3. Train your voice
Ask with a choice card:
- "Last 500 sent emails": quicker, good for most people.
- "Last 1,000 sent emails" (recommended if you write a lot or to very different audiences): slower, sharper, picks up how you sound with clients vs team vs friends.
Then:
1. Page through Gmail sent mail (`in:sent`, newest first) until the chosen count. Skip forwards with no added text, calendar replies and auto-replies. Read only what they wrote, not the quoted chain.
2. Tag each by audience: client, team, investor or partner, vendor, candidate, personal.
3. Extract: openers, closers and sign-off, typical length, exclamation and emoji use, favorite phrases, words they never use, how they say no, how they ask for things, how tone shifts by audience.
4. Write the profile into the `owner-email-voice` skill (under 60 lines, real quoted examples, no confidential content) and propose it as a skill update.
5. Show the receipt: "Read N emails to N people. You open with X about N% of the time, average N words, and you never say Y." Then write one sample reply to a real recent email and ask "does this sound like you?" Fix from their edits.
Progress updates every ~250 emails so it never looks stuck.

## Step 4. Build the first picture
Read the last 30 days of Gmail, Calendar, Slack and Notion and seed the dashboard database:
- `cos/people`: the 25 people they talk to most, role, last touch.
- `tasks`: open asks waiting on them (kind reply) and things they said they'd do (kind task).
- `waiting`: things they are waiting on from others.
- `goals`: the three 90-day goals.
- `cos/state.settings.vip`, `cos/facts` with their rules from Step 1.
Receipt: "Found N people, N replies you owe, N things you're waiting on, N live deals. The oldest unanswered one is from X, N days ago."

## Step 5. Texts (optional, Mac only)
Ask: "Want me to read your iMessages too, read only, with names from your Mac Contacts?" If yes, follow `texts/README.md` and the `read-my-texts` skill: link the Mac, Full Disk Access, approve the two folders, export Contacts as a vCard, build `contacts.json`. Receipt: "Matched N numbers to names. N texts are waiting on you." Say plainly: personal texts stay private and never become tasks.

## Step 6. Go live
1. Publish `dashboard/home-base.html` with capabilities db, user, sample and mcp (Gmail, Google Calendar, Google Drive, Slack, Notion, Claude Code Remote).
2. Paste `docs/project-instructions.md` (filled in) into the project's instructions and write `docs/standing-rules.md` into `cos/facts`.
3. Create the routines in `routines/` at their times (01 to 08 first) and wire in the job runner id.
4. Publish `dashboard/inbox-quest.html` with the voice profile pasted in, and offer the two scripts in `extras/`.
5. Save the skills in `skills/`.
6. Show the dashboard with their real first day on it and one honest observation: where their calendar and their stated goal disagree.

## Close
Three lines: what's now running and when the first morning one-pager lands, what they should say when something is missed ("that was a miss"), and one thing to try today.

## Rules
- One step at a time. If they stall, save progress in `cos/state.onboarding {step, done[]}` and pick up there next time.
- Every claim comes from something you actually read. No invented counts.
- NDA or confidential deals: ask once whether any exist and keep them out of anything shareable.
