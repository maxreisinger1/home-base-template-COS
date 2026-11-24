---
name: "read-my-texts"
description: "Use when a task needs {{OWNER_NAME}}'s iMessages (recent texts, who texted, texts owed a reply), to read chat.db on their Mac read only and put Contacts names on numbers."
---

# Read my texts (read only)

Scripts and guide: `~/Documents/Home Base/texts-kit/` on the Mac (README.md has the full setup).

## Setup check
1. The Mac must be linked and on. Approve `~/Library/Messages` and `~/Documents` if not connected.
2. Names come from `~/Documents/Home Base/contacts.json`. Missing or older than ~2 months: ask for a fresh Contacts vCard export to Documents, then run `build-contacts.py <file>.vcf > contacts.json`.

## Each run (on the Mac)
```bash
K="$HOME/mnt/Documents/Home Base"
mkdir -p $HOME/cdb && cp $HOME/mnt/Messages/chat.db* $HOME/cdb/ && cp "$K/contacts.json" "$K"/texts-kit/*.py $HOME/cdb/ && cd $HOME/cdb
python3 sms-extract.py <hours> <lastRowId>
OWNER_FIRST_NAME={{OWNER_NAME}} python3 owe-reply.py <days>
cd $HOME && rm -rf $HOME/cdb
```
- `cp contacts.json` fails with "Resource deadlock": the file is iCloud-evicted; stage it once to download, then retry.
- Timestamps are UTC; show local time.

## Rules
- Read only. Never send, reply, react, delete or write to chat.db. Drafts only.
- Delete the copy every run. Never upload chat.db or contacts.json anywhere.
- Only business asks become tasks. Personal content is never quoted, stored in shared places or mentioned.
- No bare phone numbers: check Gmail signatures, Slack profiles and chat context for a best guess.
- If {{OWNER_NAME}} marked an owe done without replying, treat it as dismissed.
