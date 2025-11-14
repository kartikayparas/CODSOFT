import json
import argparse
from datetime import datetime
from pathlib import Path
import uuid

DB = Path("todo.json")

def load():
    if not DB.exists():
        return []
    return json.loads(DB.read_text())

def save(data):
    DB.write_text(json.dumps(data, indent=2))

def add(title, due):
    tasks = load()
    task = {
        "id": str(uuid.uuid4()),
        "title": title,
        "created": datetime.now().isoformat(),
        "due": due,
        "done": False
    }
    tasks.append(task)
    save(tasks)
    print("Added:", title)

def list_tasks(show_all=False):
    tasks = load()
    if not tasks:
        print("No tasks.")
        return
    for t in tasks:
        if not show_all and t["done"]:
            continue
        status = "✓" if t["done"] else " "
        print(f'[{status}] {t["id"][:8]} - {t["title"]} (due: {t["due"]})')

def complete(task_id):
    tasks = load()
    for t in tasks:
        if t["id"].startswith(task_id):
            t["done"] = True
            save(tasks)
            print("Marked done:", t["title"])
            return
    print("Task not found.")

def delete(task_id):
    tasks = load()
    new = [t for t in tasks if not t["id"].startswith(task_id)]
    if len(new) == len(tasks):
        print("Task not found.")
    else:
        save(new)
        print("Deleted.")

def update(task_id, title=None, due=None):
    tasks = load()
    for t in tasks:
        if t["id"].startswith(task_id):
            if title: t["title"] = title
            if due: t["due"] = due
            save(tasks)
            print("Updated:", t["title"])
            return
    print("Task not found.")

def main():
    p = argparse.ArgumentParser(description="To-Do List")
    sub = p.add_subparsers(dest="cmd")
    a = sub.add_parser("add"); a.add_argument("title"); a.add_argument("--due", default="")
    sub.add_parser("list").add_argument("--all", action="store_true")
    c = sub.add_parser("complete"); c.add_argument("id")
    d = sub.add_parser("delete"); d.add_argument("id")
    u = sub.add_parser("update"); u.add_argument("id"); u.add_argument("--title"); u.add_argument("--due")
    args = p.parse_args()
    if args.cmd == "add": add(args.title, args.due)
    elif args.cmd == "list": list_tasks(args.all)
    elif args.cmd == "complete": complete(args.id)
    elif args.cmd == "delete": delete(args.id)
    elif args.cmd == "update": update(args.id, args.title, args.due)
    else: p.print_help()

if __name__ == "__main__":
    main()
