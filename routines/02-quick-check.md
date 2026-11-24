[paste 00-preamble.md here]

Fast pass. Do not touch state.lastScanAt. Log one "scan" entry starting "quick:".
1. JOBS: for each drafts doc with status "queued", do the job (draft, research, prep), write the result, set status ready or failed.
2. WAITING ON: for each open waiting doc, search Gmail and Slack for a reply from that person since `since`. If one landed, set status replied, write a short brief and a drafted reply (draft only), add an alert card, and make it item 1 of cos/next.
3. SENT MAIL: read {{OWNER_NAME}}'s sent mail and Slack since the last quick check. Mark tasks done when the sent message clearly handles them. When they ask someone for something, add a waiting doc.
4. EMAIL WATCH: recompute the escalation level of every open email item (see the email-never-falls-through skill) and write the higher value.
Final message: "Nothing urgent." unless a reply landed from a VIP or a deadline is under 2 hours away, then one line "Urgent: <who> <what>".
