---
name: "model-effort-check"
description: "Use at the start of any new task from {{OWNER_NAME}}, especially builds, code, contracts, money, strategy or research. Pauses with a one line recommendation if a different model or effort level fits better."
---

# Model and effort check

Goal: before starting a task, tell {{OWNER_NAME}} in one line if a different model or effort level would do it better, then let them choose.

## Honest limits
- This only works when the skill loads at the start of a task. It cannot watch every message passively or block anything.
- I cannot switch my own model or effort mid-task on my own. A session only changes when {{OWNER_NAME}} asks for it in their own words, or uses the model picker.
- The picks below are rules of thumb, not measured on this setup. Review them monthly.
- If I am unsure which model I am running on, say so rather than guess.

## When to run the check
Run it on the first message of a new task, and again if the task changes size or type. Skip it for quick questions, acknowledgements, and filing a task.

## Current lineup
Haiku 5.5 (fastest, cheapest), Sonnet 5.5 (default for everyday work), Opus 5.5 (strongest reasoning), plus the Fable 5.1 tier where available. If {{OWNER_NAME}} names an older model, such as Opus 4, say which current model is the closest fit.

## Recommendation guide
| Task | Suggest |
| --- | --- |
| Quick lookups, filing tasks, calendar checks, simple scans | Sonnet, low effort (Haiku if only speed matters) |
| Email drafts, meeting prep, daily brief, inbox triage | Sonnet, medium |
| Deal briefs, contract or redline review, pricing, anything legal or money | Opus, high |
| Strategy calls, hiring, equity, major decisions | Opus, high |
| Building or changing code, dashboards, scripts, automations | Opus, high |
| Long research reports, multi-source analysis | Opus, high (max only if a mistake is costly) |
| Skill writing, system design | Opus, high |

{{OWNER_NAME}} effort costs more time and usage. Only recommend it when a mistake is expensive.

## How to pause
1. Name the task type in 3 words.
2. If the current setup is fine, say nothing and start.
3. If a change would clearly help, say one line: "This is a build task. I would use Opus on high. Want to switch, or keep going on Sonnet?" Then wait for their answer.
4. If {{OWNER_NAME}} says keep going, do not ask again for the same task.
5. If the task is small but {{OWNER_NAME}} is on a heavy setting, say so once: "Sonnet medium is enough here and faster."

## Also check
- Is this the right thread? Use the use-chief-of-staff-well skill. A new topic goes to the main chat. A follow up goes to the thread that has the context.
- If the work is large, restate the ask, success criteria and what I will skip, and get a yes first.