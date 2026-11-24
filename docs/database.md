# Home Base database

The dashboard keeps everything in its artifact database. Scheduled routines read it first and write to it last. You don't create these by hand: the page and the routines create them on first use.

## Documents (collection `cos`)
- `cos/state` {today{date,oneThing,top3[{id,text,done}]}, tomorrow{top3[]}, weekly{weekOf,big[{id,text,why}],tasks[]}, settings{vip[],quietHours,nudgeCap,alertCap}, headsDownUntil, pulse{revenue{value,label,source,asOf}, arms[{name,status,evidence,source}], blindSpot{text,evidence,source}}, lastScanAt}
- `cos/facts` standing rules every routine reads. Put rules here instead of editing routine prompts.
- `cos/onepager` the morning one-pager.
- `cos/next` the 3 next moves shown in the speech bubble on Home.
- `cos/brief` theme + 2 to 3 lines at the top of Today.
- `cos/dayprep` {date, events{<calendar eventId>:{who, goal, owe, note, prep[{label,url}]}}} meeting cards.
- `cos/people` {asOf, list[{name,role,lastTouch,daysSince,note}]} relationship pulse.
- `cos/talk`, `cos/leverage`, `cos/audit` {blocker, blockerSetAt, blockerBy, source}.
- `news/latest` optional daily news feed.

## Collections
- `tasks` {text, short, kind task|reply, due YYYY-MM-DD, horizon today|week|year|putoff|undecided, done, doneAt, owner, priority 1|2|3, note, source, who, channel, draft, emailWatch{threadId,deadline,level,...}}
- `messages` {source gmail|slack|text, from, email, subject, summary, why, urgent, rank, fit yes|no|later, ts, handled, drafts[], url}
- `waiting` {who, org, email, what[], since, threadId, status open|replied|closed, brief, draftId}
- `drafts` {title, kind, body, to, subject, status queued|working|ready|failed}
- `goals` {text, horizon "90-day", target, metric{unit,goal,current}, progress, status on_track|at_risk|behind|hit}
- `ideas` {title, note, source, status open|task|dropped}
- `cards` {kind nudge|alert, text, evidence, ts, status open|answered|ignored, ignoredCount}
- `log` {type win|decision|avoid|pattern|note|eod|friday|checkin|scan, text, ts, source}
- `audit/<date>` daily and weekly CEO audit questions.
- `candidates` optional hiring board (hidden from the nav by default).
