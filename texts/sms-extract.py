import sqlite3, sys, json, re, os
# number -> name map built from your Contacts vCard export (stays on the Mac)
CONTACTS = {}
for cp in [os.path.expanduser("~/mnt/Documents/Home Base/contacts.json"), "contacts.json"]:
    try: CONTACTS = json.load(open(cp)); break
    except Exception: pass
def who(h):
    if not h: return None
    if "@" in h: d = h.strip().lower()  # email handle
    else:
        d = re.sub(r"\D","",h)
        if len(d)==11 and d[0]=="1": d=d[1:]
    c = CONTACTS.get(d)
    return c["name"] if c else None
since_hours = float(sys.argv[1]) if len(sys.argv)>1 else 24
min_rowid = int(sys.argv[2]) if len(sys.argv)>2 else 0
c=sqlite3.connect("file:chat.db?mode=ro",uri=True)
def body(text, ab):
    if text: return text
    if not ab: return ""
    try:
        i = ab.find(b"NSString")
        if i<0: return ""
        j = ab.find(b"+", i)  # length prefix marker
        p = j+1; n = ab[p]
        if n == 0x81: n = int.from_bytes(ab[p+1:p+3],"little"); p+=3
        elif n == 0x82: n = int.from_bytes(ab[p+1:p+5],"little"); p+=5
        else: p+=1
        return ab[p:p+n].decode("utf-8","replace")
    except Exception: return ""
q="""select m.ROWID, datetime(m.date/1000000000+978307200,'unixepoch') ts, m.is_from_me, h.id handle,
 ch.display_name, ch.chat_identifier, m.text, m.attributedBody, m.cache_has_attachments
 from message m left join handle h on h.ROWID=m.handle_id
 left join chat_message_join cmj on cmj.message_id=m.ROWID left join chat ch on ch.ROWID=cmj.chat_id
 where m.date/1000000000+978307200 > strftime('%s','now')-? and m.ROWID > ? and m.associated_message_type=0
 order by m.ROWID"""
out=[]
for r in c.execute(q,(int(since_hours*3600),min_rowid)):
    t=body(r[6],r[7]).replace("￼","").strip()
    if not t and not r[8]: continue
    out.append({"id":r[0],"ts":r[1],"me":r[2],"from":r[3],"name":who(r[3]),"group":r[4] or None,"chat":r[5],"text":t[:500] or "[attachment]"})
print(json.dumps(out,ensure_ascii=False))
