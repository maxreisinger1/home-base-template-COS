---
name: "orchestrate-big-task"
description: "Use for big multi-step builds or specs (dashboard work, research projects, code) to split the work into tasks and give each the cheapest model that can do it well."
---

# Orchestrate a big task

You are the lead. You own coordination, integration, review and final checks.

## 1. Break it down
Split the spec into small, independent tasks. For each: what it does, what it depends on, how we know it's done.

## 2. Pick a model per task (default Opus, not Fable)
- Haiku 5.5: simple, repetitive, well-defined (renames, sorting, labeling, copy tweaks).
- Sonnet 5.5: standard building, small features, refactors, tests, moderate debugging, small dashboard tweaks.
- Opus 5.5: the default for anything that needs reading a lot and connecting dots.
- Fable 5.2: only architecture calls, nasty debugging, ambiguous requirements, legal, or high-stakes work where being wrong is expensive. Fable may be capped on your plan, so never spend it on work Sonnet can nail.
Use the Agent tool's model override (haiku, sonnet, opus, fable) for subagents.

## 3. Show the plan only when it's big
If the job has 5+ tasks or will use Fable, show {{OWNER_NAME}} a short table first: task, model, one-line why. Otherwise just start.

## 4. Run it
Run independent tasks in parallel, respect dependencies, avoid two agents editing the same file. Escalate to a stronger model only after a failed attempt or when risk turns out higher than expected.

## 5. Finish
Review and integrate everything yourself, verify it works, then give {{OWNER_NAME}} the outcome in a few plain lines.