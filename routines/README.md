# Scheduled routines

Each file here is the prompt for one scheduled task (a Claude Code remote trigger or a Claude project routine). Every run starts with no memory, so each prompt begins with `00-preamble.md` pasted on top. All state lives in your Home Base dashboard's database.

| File | Schedule (edit to taste) | What it does |
|---|---|---|
| 01-morning-one-pager.md | Weekdays 6:42am | Builds today's one-pager and the one thing |
| 02-quick-check.md | Weekdays :07 and :37, 8am to 6pm | Runs queued jobs, checks who replied, auto-completes tasks from sent mail |
| 03-full-sweep.md | Weekdays :22, 8am to 6pm | Inbox, Slack, Calendar, Notion sweep into tasks, replies and one card |
| 04-end-of-day.md | Weekdays 5:40pm | Nudges the end of day dump and preps the reflection |
| 05-friday-review.md | Fridays 3:46pm | Gathers the week for the Friday review |
| 06-job-runner.md | No schedule (fired by the page) | Does heavy jobs the dashboard queues |
| 07-overnight-catch-up.md | Weekdays 7:15am | Slack, email and texts since 6pm yesterday, sorted by deadline |
| 08-plan-your-day.md | Weekdays 7:41am | The one thing, top 3, who else could own each, email and Slack roll call |
| 09-news.md | Daily 6:23am | Fills the News tab (max 72 hours old) |
| 10-text-sync.md | Weekdays hourly :52 (Mac only) | Business texts into tasks and replies |
| 11-owe-a-reply-texts.md | Daily 6:43pm (Mac only) | Texts you owe a reply, with drafts |
| 12-voice-compare.md | Weekdays 6:13pm, silent | Compares drafts with what you actually sent |
| 13-voice-tidy.md | Fridays 4:17pm | Updates your voice profile from the week's lessons |
| 14-weekly-kickoff-pages.md | Mondays 5:33am | Creates the week's Notion kickoff pages |

Start with 01 to 08. Add the rest once the basics feel right.

Tips that cost us time to learn:
- Keep each prompt under about 9,000 characters. Longer ones get cut off mid-run.
- Routine prompts often can't be edited after creation. Put rules that change in the `cos/facts` document in the database, which every run reads, instead of in the prompt.
- Every run posts a line in chat. Fewer, merged routines means less clutter.
