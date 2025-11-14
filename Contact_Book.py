import json
from pathlib import Path
import argparse
import uuid

DB = Path("contacts.json")

def load():
    if not DB.exists(): return []
    return json.loads(DB.read_text())

def save(data):
    DB.write_text(json.dumps(data, indent=2))

def add(name, phone, email="", address=""):
    contacts = load()
    contact = {"id": str(uuid.uuid4()), "name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    save(contacts)
    print("Added:", name)

def list_contacts():
    for c in load():
        print(f'{c["id"][:8]} - {c["name"]} | {c["phone"]} | {c.get("email","")}')

def find(query):
    q = query.lower()
    for c in load():
        if q in c["name"].lower() or q in c["phone"]:
            print(c["id"][:8], "-", c["name"], c["phone"], c.get("email",""))

def update(cid, name=None, phone=None, email=None, address=None):
    contacts = load()
    for c in contacts:
        if c["id"].startswith(cid):
            if name: c["name"] = name
            if phone: c["phone"] = phone
            if email is not None: c["email"] = email
            if address is not None: c["address"] = address
            save(contacts)
            print("Updated:", c["name"])
            return
    print("Not found.")

def delete(cid):
    contacts = load()
    new = [c for c in contacts if not c["id"].startswith(cid)]
    if len(new) == len(contacts):
        print("Not found.")
    else:
        save(new)
        print("Deleted.")

def main():
    p = argparse.ArgumentParser(description="Contact Book")
    sub = p.add_subparsers(dest="cmd")
    a = sub.add_parser("add"); a.add_argument("name"); a.add_argument("phone"); a.add_argument("--email", default=""); a.add_argument("--address", default="")
    sub.add_parser("list")
    f = sub.add_parser("find"); f.add_argument("query")
    u = sub.add_parser("update"); u.add_argument("id"); u.add_argument("--name"); u.add_argument("--phone"); u.add_argument("--email"); u.add_argument("--address")
    d = sub.add_parser("delete"); d.add_argument("id")
    args = p.parse_args()
    if args.cmd == "add": add(args.name, args.phone, args.email, args.address)
    elif args.cmd == "list": list_contacts()
    elif args.cmd == "find": find(args.query)
    elif args.cmd == "update": update(args.id, args.name, args.phone, args.email, args.address)
    elif args.cmd == "delete": delete(args.id)
    else: p.print_help()

if __name__ == "__main__":
    main()
