# Owe-a-reply finder for your iMessages. Run on your Mac in $HOME/cdb next to a copy of chat.db and contacts.json.
# Usage: python3 owe.py [days=14]  -> JSON list of chats where the last real message is from someone else and you haven't replied or reacted.
import sqlite3,re,json,sys,os
OWNER=os.environ.get("OWNER_FIRST_NAME","owner").lower()  # your first name, so texts that mention you count
try: C=json.load(open("contacts.json"))
except Exception: C={}
def norm(h):
    if h and "@" in h: return h.strip().lower()  # email handle
    d=re.sub(r"\D","",h or "")
    if len(d)==11 and d[0]=="1": d=d[1:]
    return d
def who(h):
    x=C.get(norm(h)); return x["name"] if x else None
def body(text, ab):
    if text: return text
    if not ab: return ""
    try:
        i=ab.find(b"NSString")
        if i<0: return ""
        j=ab.find(b"+",i);p=j+1;n=ab[p]
        if n==0x81: n=int.from_bytes(ab[p+1:p+3],"little");p+=3
        elif n==0x82: n=int.from_bytes(ab[p+1:p+5],"little");p+=5
        else: p+=1
        return ab[p:p+n].decode("utf-8","replace")
    except Exception: return ""
JUNK=re.compile(r"verification code|your code|\bcode[: ]\d|reply stop|text stop|stop to|unsubscribe|direct lender|funding|fund you|working capital|line of credit|\bLOC\b|HELOC|debt collector|payback|underwriting|receipt|open enrollment|premiums|election|vote|polls|registration of|vehicle transport|loyalty|partiful|luma\.link",re.I)
BOTS=set()  # names of bots or assistants that text you, e.g. {"Reminder Bot"}
days=float(sys.argv[1]) if len(sys.argv)>1 else 14
c=sqlite3.connect("file:chat.db?mode=ro",uri=True)
chats=c.execute("""select ch.ROWID, ch.chat_identifier, ch.display_name from chat ch where exists(select 1 from chat_message_join j join message m on m.ROWID=j.message_id where j.chat_id=ch.ROWID and m.date/1000000000+978307200 > strftime('%s','now')-?)""",(int(days*86400),)).fetchall()
out=[]
for cid,ident,dn in chats:
    if "rbm.goog" in ident or ident.startswith("urn:"): continue
    msgs=c.execute("""select m.ROWID, datetime(m.date/1000000000+978307200,'unixepoch'), m.is_from_me, h.id, m.text, m.attributedBody, m.associated_message_type from chat_message_join j join message m on m.ROWID=j.message_id left join handle h on h.ROWID=m.handle_id where j.chat_id=? order by m.date desc limit 40""",(cid,)).fetchall()
    theirs=[]; acked=False
    for r in msgs:
        if r[6]!=0:
            if r[2]==1: acked=True; break
            continue
        if r[2]==1: break
        theirs.append(r)
    if not theirs or acked: continue
    members=[h for (h,) in c.execute("select h.id from chat_handle_join j join handle h on h.ROWID=j.handle_id where j.chat_id=?",(cid,))]
    texts=[body(r[4],r[5]).replace("￼","").strip()[:280] or "[attachment]" for r in reversed(theirs[:4])]
    last=theirs[0]; frm=who(last[3])
    if frm in BOTS: continue
    if len(norm(last[3] or ident))<10 and "@" not in (last[3] or ""): continue  # shortcodes
    if any(JUNK.search(t) for t in texts) and not frm: continue
    group=len(members)>1
    you_spoke=c.execute("select count(*) from chat_message_join j join message m on m.ROWID=j.message_id where j.chat_id=? and m.is_from_me=1",(cid,)).fetchone()[0]
    if not frm and not you_spoke and not re.search(r"\b("+OWNER+"|intro|met|meeting|great meeting|it.s [A-Z])",
        " ".join(texts)): continue  # unknown cold number, no thread history
    out.append({"chat":ident,"rowid":last[0],"lastIn":last[1],"from":frm or last[3],"known":bool(frm),
      "group":(dn or ", ".join((who(h) or h) for h in members[:5])) if group else None,
      "youEverReplied":bool(you_spoke),"n":len(theirs),"texts":texts})
out.sort(key=lambda x:x["lastIn"],reverse=True)
print(json.dumps(out,ensure_ascii=False))
