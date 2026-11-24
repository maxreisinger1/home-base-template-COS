---
name: "personal-inbox-sweep"
description: "Use when {{OWNER_NAME}} asks to check, clear or scan their personal inbox, or on any personal morning brief, to pull out money, deadlines, returns and real people from their personal Gmail."
---

# Personal inbox sweep

Optional: only if a personal Gmail is connected as a second account. Keep work and personal items apart.

## What to look for (in this order)
1. **Money with a date**: bills, statements, autopay notices, failed payments, collections, price increases, renewals, free trials ending. Always give the amount and due date.
2. **Return and refund windows**: orders with a return deadline, refunds promised but not yet seen, price drops on recent purchases within a price-adjust window.
3. **Real people**: friends, family, landlord, doctors, anyone waiting on a reply. These matter more than any brand email.
4. **Logistics**: deliveries arriving today/tomorrow, appointments, travel changes.
5. **Everything else** is noise: count it, don't list it.

## How to sweep
- Default window: since the last sweep (check the sweep log in memory file personal-inbox-log.md), or 3 days if none.
- Skip anything already in the RESOLVED list in that log, so nothing nags twice.
- New errands or deadlines go into Home Base tasks with a due date. Check for an existing one first.
- Draft replies to real people only when useful, in a casual personal voice, as a draft card. Never send, archive in bulk, unsubscribe or delete without {{OWNER_NAME}}'s yes on that item.
- Offer one batch action at the end if it would help (e.g. "unsubscribe from these 6 senders you never open?"), and wait for a yes.

## Output
Under 120 words. Lead with the one thing that costs money or a deadline if ignored. Then: Money (amount, date), People waiting, Returns/refunds, Arriving. End with the noise count. No guilt language: give each item a first step, not a lecture.

## After
Append to personal-inbox-log.md: sweep time, items surfaced, and move anything {{OWNER_NAME}} handled or dismissed to RESOLVED.