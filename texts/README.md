# iMessage + Mac Contacts (optional, Mac only)

Lets Home Base read your texts, read only, and put real names on phone numbers by cross-referencing your Mac Contacts. Business asks become Replies with a drafted text. Personal texts never leave your Mac.

| File | What it does |
|---|---|
| `sms-extract.py` | Pulls recent messages from `chat.db` as JSON (text, sender, name, group) |
| `owe-reply.py` | Lists chats where someone else spoke last and you haven't replied or reacted |
| `build-contacts.py` | Turns a Contacts export into `contacts.json`, the number-to-name map |

## One-time setup
1. Install the Claude desktop app on your Mac and link your computer to your Home Base project.
2. Give the Claude app Full Disk Access (System Settings > Privacy & Security > Full Disk Access). Without it `chat.db` reads as empty.
3. Approve two folders when Claude asks: `~/Library/Messages` and `~/Documents`.
4. Copy this `texts/` folder to `~/Documents/Home Base/texts-kit/` on the Mac.
5. Contacts: in Contacts.app select all, then File > Export > Export vCard, save to `~/Documents`. Claude runs `python3 build-contacts.py <file>.vcf > "~/Documents/Home Base/contacts.json"`. (The live AddressBook folder is usually blocked as protected; the vCard export is the reliable route.) Re-export every month or two.
6. Set `OWNER_FIRST_NAME` when running `owe-reply.py` so texts that mention you count.

## How a run works
Always on a temporary copy, read only:
```bash
mkdir -p $HOME/cdb && cp $HOME/mnt/Messages/chat.db* $HOME/cdb/ && cd $HOME/cdb
cp "$HOME/mnt/Documents/Home Base/contacts.json" "$HOME/mnt/Documents/Home Base"/texts-kit/*.py .
python3 sms-extract.py 24 0          # last 24 hours, from message id 0
OWNER_FIRST_NAME=sam python3 owe-reply.py 14   # chats you owe in the last 14 days
cd $HOME && rm -rf $HOME/cdb
```
Copy all three `chat.db*` files; recent messages sit in the `-wal` file. Store the highest `id` processed and pass it next time.

## Name matching
Numbers normalize to 10 digits (drop a leading +1) or a lowercased email, then look up in `contacts.json`. Unknown number: Claude checks Gmail signatures, Slack profiles and the chat itself and gives a best guess with confidence, never a bare number.

## Suggested routines
- Hourly text sync (weekdays): `sms-extract.py` from the last id, business asks into tasks with source "text".
- Daily owe-a-reply sweep (evening): `owe-reply.py 14`. Business owes become Replies with a drafted text. Personal owes go only to the private doc `data/users/me/owe-replies`.
Both need the Mac on and awake.

## Privacy rules
- Read only. Never send, reply, react, delete or write to `chat.db`. You send texts yourself.
- Delete the temporary copy every run. Never upload `chat.db` or `contacts.json` to the cloud, a doc, an artifact, Slack or email.
- Personal stays private: family, friends, dating, health, money, spam and 2FA codes are never quoted, summarized or turned into tasks.
- Tune the `JUNK` regex and `BOTS` list in `owe-reply.py` for your own spam.
