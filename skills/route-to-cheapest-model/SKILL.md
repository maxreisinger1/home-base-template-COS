---
name: "route-to-cheapest-model"
description: "Use before starting any task with more than one step (sweeps, research, drafting, builds, reviews) to split it into parts and give each part the cheapest model that does it well."
---

# Route each part to the cheapest model that does it well

Usage costs real money. The job is to get the same quality for less, not to use the biggest model. When a cheaper model is good enough, use it and say so. This skill replaces the model tables in orchestrate-big-task and model-effort-check where they differ.

## Step 1. Split the task into parts
Most tasks are three kinds of work glued together:
- Gather: find, read, list, search, compare, extract, count.
- Make: draft, summarize for a person, build, research a normal question.
- Judge: decide, advise, negotiate, sign off, anything where being wrong costs money or trust.

## Step 2. Give each part a model
| Part | Model | Examples |
| --- | --- | --- |
| Gather | Haiku 5.5 | inbox and Slack sweeps, "did they reply", calendar lookups, pulling sent mail, diffing a draft against what was sent, extracting action items from a transcript, price watches, reminders, filing tasks, format and copy tweaks |
| Make | Sonnet 5.5 | email and Slack drafts in {{OWNER_NAME}}'s voice, meeting prep and debriefs, daily briefs, normal research, deal briefs from documents already gathered, small dashboard changes |
| Judge | Opus 5.5 | contract and redline review, pricing and comp, strategy calls, hiring decisions, coaching pushback, big dashboard builds, anything that needs many sources connected |
| Rare | Fable 5.2 | only when Opus got it wrong or the stakes are very high: a contract before signature, a hard legal or money question, system design that everything else depends on. Fable may be capped on your plan. |

Rough cost: Haiku is the cheap tier, Sonnet costs a few times Haiku, Opus costs more than Sonnet, Fable more again. Exact prices change, so check the model guide before quoting numbers. The bigger lever is usually how much gets read, not which model reads it.

## Step 3. Use the right lever
- New thread: the coordinator picks the model when it starts the thread. Say which one and why in one line.
- Inside a task: hand the Gather part to a helper on Haiku (Agent tool, model haiku) and keep only its short findings. Worth it when the reading is big (20 or more emails, a long transcript, many files). For a handful of lookups, just do them, because a helper has its own overhead.
- Scheduled tasks: each one has its own model setting. Changing it needs {{OWNER_NAME}}'s yes.
- Effort: low for Gather, medium for Make, high only for Judge.
- If the whole task is one kind of work and the current model is too big for it, say so once: "Sonnet is enough for this."

## Step 4. Cut the reading, whatever the model
- Do not reload what is already known. Read the one doc or thread needed, not the whole database or mailbox.
- Long threads cost more every turn, because the whole history is reread. New topic, new thread.
- Batch: one run that does five things beats five runs.
- Skip a run when nothing changed.

## Step 5. Move up only for a reason
Move a part up one tier when the cheaper model failed once, when the output goes to a client or counterparty without {{OWNER_NAME}} reading it closely, or when a mistake would cost real money. Say in one line that you moved up and why. Never move up just because the task feels important.

## Never go cheap on
Contracts, signatures, comp and offers, bank and payment details, anything sent in {{OWNER_NAME}}'s name to a client, and the checks that stop things falling through (deadlines in email and Slack). For those last ones, Sonnet is the floor.

## Show the plan only when it matters
For a task with 5 or more parts, or any use of Fable, show {{OWNER_NAME}} three lines: part, model, why. Otherwise just do it and mention the routing in one line at the end.

## Honest limits
- I cannot switch my own model in the middle of a task. I can only hand parts to helpers, or tell {{OWNER_NAME}} a different thread model fits.
- These picks are rules of thumb. If a cheap model misses something, log it with fix-it-forward and move that kind of work up a tier.