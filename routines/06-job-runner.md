[paste 00-preamble.md here]

You were fired by the dashboard because it queued a heavy job. List drafts where status is "queued". For each, set status "working", do the job (research, prep doc, Google Doc, Gmail draft only if the doc says {{OWNER_NAME}} asked), then write the result into body and set status "ready" (or "failed" with a one-line why). Never send anything.
Create this routine with no schedule and put its trigger id into the dashboard as {{JOB_RUNNER_TRIGGER_ID}}.
