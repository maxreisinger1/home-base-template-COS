---
name: "do-it-for-me"
description: "Use whenever a fix or setup step seems to need {{OWNER_NAME}}'s hands (settings, filters, accounts, files). Find a way to do it yourself first."
---

# Do it for me

## Before you write "you can do X" or list steps for them

Work down this list until one works:

1. **Connector tools** (Gmail, Calendar, Drive, Docs, Sheets, Notion, Slack). Check ToolSearch for an action that does it directly.
2. **Claude in Chrome** (their real Chrome, already signed in). Good for settings pages with no API: Gmail filters (use the right Google account), app settings, admin consoles. Run tabs_context_mcp first, work in a new tab and close it when done. Never enter passwords, payment details or accept terms.
3. **Apps Script** in {{OWNER_EMAIL}} for anything that has to run on its own (archiving, saving attachments). 
4. **Remote Control or folder access** on their Mac for local files and command-line tools.
5. **Scheduled tasks** for recurring work. They can read, but the safety check blocks them from writing to outside systems (Gmail archive, etc.), so build anything that changes data with 2 or 3 instead.

If none works, tell them in one line what you tried and the one smallest thing you need from them.

## Verify, don't assume

A test that had nothing to act on proves nothing. Check the real result (the filter exists in settings, the inbox is clear) before you call it done.

## Effort and model

If the problem needs more digging than you can do well at your current effort level, tell {{OWNER_NAME}} to switch to high effort, or to Opus, and say why in one line.

## Still guarded

Sending email, accepting or declining invites, purchases, deletes and anything sent outside the company still need their clear yes. "Do it for them" covers setup and fixes, not those.