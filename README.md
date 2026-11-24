# Chief of Staff Home Base

An AI chief of staff and CEO coach that lives in one dashboard. It reads your Gmail, Calendar, Slack, Notion and Drive, turns what matters into tasks, replies and a short daily plan, and coaches you toward one goal. It drafts, it never sends.

This repo is a clean template. It holds no one's data. Your copy fills in from your own accounts the first time the routines run.

## What's in here

| Path | What it is |
|---|---|
| `dashboard/home-base.html` | The dashboard (a single-page Claude artifact) |
| `dashboard/inbox-quest.html` | Inbox Quest: a game that clears your inbox, with drafted replies in your voice |
| `routines/` | 14 prompts for the scheduled tasks that keep it fresh |
| `skills/` | 27 skills: sweeps, drafts, voice learning, deals, meetings, reviews, coaching, model routing |
| `texts/` | Optional: read iMessages on your Mac and match numbers to your Contacts |
| `docs/project-instructions.md` | The coach's standing brief, to paste into your Claude project |
| `docs/standing-rules.md` | 17 rules every routine follows, each one earned from a real miss |
| `docs/database.md` | The shape of the dashboard's database |
| `extras/` | Google Apps Scripts: save email attachments to Drive, unsubscribe sweep (pairs with Inbox Quest) |

## Quick start
Open this repo in a Claude project and say **"onboard me"**. The `onboard-home-base` skill walks you through everything below, one step at a time, and shows you what it learned as it goes:
1. Five questions about you, your goal and your team.
2. Connects Gmail, Calendar, Drive, Slack and Notion, and shows what it can see in each.
3. Trains your voice on your last 500 or 1,000 sent emails (you pick), then writes a sample reply so you can check it sounds like you.
4. Reads your last 30 days and fills the dashboard: who matters, what you owe, what you're waiting on.
5. Optional on a Mac: reads your iMessages, read only, with names from your Contacts.
6. Publishes your dashboard and Inbox Quest, loads the standing rules and turns on the daily routines.

## Manual setup (if you'd rather do it by hand)

### 1. Fill in the placeholders
Search the whole repo for `{{` and replace each one. The main ones:

| Placeholder | Example |
|---|---|
| `{{OWNER_NAME}}` / `{{OWNER_FULL_NAME}}` | Sam / Sam Rivera |
| `{{OWNER_ROLE}}` | co-founder and President |
| `{{COMPANY}}` | Acme Studio |
| `{{COFOUNDERS}}` | names of the other founders |
| `{{TEAM_ROLES}}` | Jordan sales, Lee ops, Pat finance |
| `{{NORTH_STAR}}` / `{{NORTH_STAR_SHORT}}` | $1M a month in revenue at 25% EBITDA / $1M a month |
| `{{GOALS_90_DAY}}` | your three 90-day goals |
| `{{STANDING_DECISIONS}}` | decisions you want to be held to |
| `{{GROWTH_AREAS}}` | what you want it to push you on |
| `{{EMAIL_STYLE}}` | how your emails sound |
| `{{MEETING_HOURS}}` | 9am to 6pm ET |
| `{{CITY}}`, `{{TIMEZONE_NAME}}`, `{{TIMEZONE}}` | NYC, Eastern, America/New_York |
| `{{OWNER_EMAIL}}`, `{{OWNER_EMAIL_LOCAL}}` | sam@yourcompany.com, sam |
| `{{SLACK_USER_ID}}` | your Slack member id (Profile, then Copy member ID) |
| `{{HOME_BASE_URL}}` | your dashboard's artifact link (step 3) |
| `{{JOB_RUNNER_TRIGGER_ID}}` | the trigger id from step 4 |
| `{{VOICE_FOLDER}}` | a folder Claude can write to for voice learning |
| `{{VOICE_PROFILE}}` | your voice profile, pasted into Inbox Quest after onboarding |
| `{{VIPS}}`, `{{KEY_CLIENTS}}`, `{{NDA_DEALS}}`, `{{NEWS_TOPICS}}` | people who come first, client names, deals to keep private, news to follow |

Also replace `yourcompany.com` with your email domain. The dashboard runs on Eastern time by default; change `America/New_York` and the "ET" labels if you're elsewhere.

### 2. Connect your accounts
In Claude, connect: Gmail, Google Calendar, Google Drive, Slack and Notion. The dashboard and routines only read, except Gmail drafts (made only when you tap to draft) and Drive files for docs it makes for you.

### 3. Publish the dashboard
Ask Claude: "Publish dashboard/home-base.html as an artifact with these capabilities: db, user, sample, and mcp for Gmail, Google Calendar, Google Drive, Slack, Notion and Claude Code Remote." Copy the artifact link into `{{HOME_BASE_URL}}`. The database starts empty, which is right.

### 4. Create the scheduled routines
For each file in `routines/` (see `routines/README.md` for times), paste `00-preamble.md` on top and ask Claude to create it as a scheduled task. Create `06-job-runner.md` with no schedule and put its trigger id in the dashboard as `{{JOB_RUNNER_TRIGGER_ID}}`, then republish.

### 5. Add the skills
Ask Claude to save each folder in `skills/` as a skill. Then ask it to train your voice on your last 500 or 1,000 sent emails (see `onboard-home-base`, step 3).

### 6. Texts (optional, Mac only)
Follow `texts/README.md` to read iMessages and match numbers to your Mac Contacts.

### 7. First week
Tell it your goals and your VIPs in the dashboard's box. Expect the first few days to be noisy. Every time it misses something, say so; the `fix-it-forward` skill turns each miss into a rule.

## Guardrails built in
- Never sends, replies, posts, accepts or declines invites, or changes your calendar without your yes.
- Cites a source for every claim and writes "ask <you>" instead of inventing a number.
- Keeps NDA deals out of anything shareable.

## Keep your data out of this repo
Your tasks, messages and notes live in your own dashboard's database, never in these files. Don't commit exports, backups or your voice files (`.gitignore` blocks the usual ones). If you improve the template, change the files here and keep the placeholders.
