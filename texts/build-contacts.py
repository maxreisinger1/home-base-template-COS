# Build contacts.json (handle -> {"name": ...}) for sms-extract.py and owe-reply.py.
# Keys: US/CA phones as 10 digits (leading 1 dropped), other phones as all digits, emails lowercased.
# Usage:
#   python3 build-contacts.py contacts.vcf  > contacts.json   (vCard export from Contacts.app, the route that works today)
#   python3 build-contacts.py AddressBook/  > contacts.json   (folder; reads every Sources/*/AddressBook-v22.abcddb read-only)
# Output stays on the Mac. Never upload it or paste it anywhere.
import sys, os, re, json, glob, sqlite3

def key(h):
    h = (h or "").strip()
    if "@" in h: return h.lower()
    d = re.sub(r"\D", "", h)
    if len(d) == 11 and d[0] == "1": d = d[1:]
    return d if len(d) >= 7 else None

out = {}
def add(handle, name):
    k = key(handle)
    if k and name and k not in out: out[k] = {"name": name.strip()}

src = sys.argv[1]
if src.lower().endswith(".vcf"):
    raw = open(src, encoding="utf-8", errors="replace").read()
    raw = re.sub(r"\r?\n[ \t]", "", raw)  # unfold folded lines
    for card in raw.split("BEGIN:VCARD")[1:]:
        fn = re.search(r"^FN[^:]*:(.*)$", card, re.M)
        n = re.search(r"^N(?:;[^:]*)?:(.*)$", card, re.M)
        org = re.search(r"^ORG[^:]*:(.*)$", card, re.M)
        name = (fn and fn.group(1)) or (n and " ".join(p for p in n.group(1).split(";")[1::-1][:2] if p)) or (org and org.group(1).split(";")[0])
        name = (name or "").replace("\\,", ",").strip()
        for m in re.finditer(r"^(?:item\d+\.)?(?:TEL|EMAIL)[^:]*:(.*)$", card, re.M):
            add(m.group(1), name)
else:
    for db in glob.glob(os.path.join(src, "**", "AddressBook-v22.abcddb"), recursive=True):
        c = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
        names = {pk: " ".join(x for x in (f, l) if x) or (o or "")
                 for pk, f, l, o in c.execute("select Z_PK, ZFIRSTNAME, ZLASTNAME, ZORGANIZATION from ZABCDRECORD")}
        for owner, num in c.execute("select ZOWNER, ZFULLNUMBER from ZABCDPHONENUMBER"):
            add(num, names.get(owner))
        for owner, em in c.execute("select ZOWNER, ZADDRESS from ZABCDEMAILADDRESS"):
            add(em, names.get(owner))
print(json.dumps(out, ensure_ascii=False))
