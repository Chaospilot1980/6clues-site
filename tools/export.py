"""Builds app/mysteries.php from every tools/mysteries/round*.py file.

Each round file defines MYSTERIES = [ {...}, ... ].  Run:  python3 tools/export.py
The script validates every mystery and refuses to write the file if anything is wrong.
"""
import glob, importlib.util, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib import poster  # noqa: E402

REQUIRED = ["slug", "level", "crime", "who", "caseno", "title_html", "title_plain", "teaser", "intro", "clues", "solution"]


def load_all():
    out = []
    for f in sorted(glob.glob(os.path.join(HERE, "mysteries", "round*.py")),
                    key=lambda p: int(re.search(r"round(\d+)", p).group(1))):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for m in mod.MYSTERIES:
            m["_file"] = os.path.basename(f)
            out.append(m)
    return out


def validate(ms):
    errors, slugs = [], set()
    for m in ms:
        where = f"{m.get('_file')}:{m.get('slug')}"
        for k in REQUIRED:
            if k not in m:
                errors.append(f"{where}: missing {k}")
        if errors:
            continue
        if m["slug"] in slugs:
            errors.append(f"{where}: duplicate slug")
        slugs.add(m["slug"])
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", m["slug"]):
            errors.append(f"{where}: bad slug")
        if m["level"] not in (1, 2, 3):
            errors.append(f"{where}: level must be 1, 2 or 3")
        if len(m["clues"]) != 6:
            errors.append(f"{where}: needs exactly 6 clues")
        names = [c.get("name") for c in m["clues"]]
        if len(set(names)) != len(names):
            errors.append(f"{where}: duplicate suspect names")
        for i, c in enumerate(m["clues"]):
            for k in ["name", "role", "quote", "label", "evidence"]:
                if not c.get(k):
                    errors.append(f"{where}: clue {i+1} missing {k}")
            if len(c.get("quote", "")) > 300:
                errors.append(f"{where}: clue {i+1} quote is {len(c['quote'])} chars (max 300, or it overflows the poster)")
        s = m["solution"]
        if s.get("killer") not in names:
            errors.append(f"{where}: solution killer '{s.get('killer')}' is not one of the six suspects")
        for k in ["motive", "proof", "cleared"]:
            if not s.get(k):
                errors.append(f"{where}: solution missing {k}")
        if len(m["teaser"]) > 160:
            errors.append(f"{where}: teaser over 160 chars")
    return errors


LAUNCH = "2026-11-15"   # Daily case #1
LIBRARY_SIZE = 30       # the first 30 cases form the free library; every case after that is released as a daily case


def schedule(ms):
    """Library cases (the first LIBRARY_SIZE) are public at once and have no daily date. Every later case gets
    one daily date and stays hidden until then. Stored in tools/schedule.json so dates never move once given.
    Daily cases: level 3 at weekends, levels 1 and 2 alternate on weekdays."""
    import datetime
    path = os.path.join(HERE, "schedule.json")
    sched = json.load(open(path)) if os.path.exists(path) else {}
    used = {v["daily"] for v in sched.values() if v.get("daily")}
    library = sum(1 for v in sched.values() if not v.get("daily"))
    pool = [m for m in ms if m["slug"] not in sched]
    today = datetime.date.today().isoformat()
    while pool and library < LIBRARY_SIZE:
        m = pool.pop(0)
        sched[m["slug"]] = {"daily": None, "public": m.get("added") or today}
        library += 1
    day = max(datetime.date.fromisoformat(LAUNCH), datetime.date.today() + datetime.timedelta(days=1))
    last_l12 = 2
    while pool:
        d = day.isoformat()
        day += datetime.timedelta(days=1)
        if d in used:
            continue
        weekend = datetime.date.fromisoformat(d).weekday() >= 5
        want = [3, 2, 1] if weekend else ([1, 2, 3] if last_l12 == 2 else [2, 1, 3])
        pick = next((m for lv in want for m in pool if m["level"] == lv), None)
        pool.remove(pick)
        if pick["level"] in (1, 2):
            last_l12 = pick["level"]
        sched[pick["slug"]] = {"daily": d, "public": d}
    with open(path, "w") as f:
        json.dump(dict(sorted(sched.items(), key=lambda kv: (kv[1]["daily"] or "", kv[1]["public"]))), f, indent=1)
    return sched


def strip(html):
    return re.sub(r"<[^>]+>", "", html).replace("&amp;", "&")


def export(ms, target):
    sched = schedule(ms)
    out = []
    for m in ms:
        posters = []
        for i, c in enumerate(m["clues"]):
            html = poster(m, i + 1, c, qr=True)
            body = html.split("<x-dc>", 1)[1].split("</x-dc>", 1)[0]
            body = re.sub(r"<helmet>.*?</helmet>", "", body, flags=re.S).strip()
            posters.append(body)
        out.append({
            "slug": m["slug"], "level": m["level"], "crime": m["crime"].title(), "who": m["who"],
            "title": m["title_plain"], "teaser": m["teaser"], "intro": m["intro"], "intro_text": strip(m["intro"]),
            "added": m.get("added", ""),
            "daily": sched[m["slug"]]["daily"], "public": sched[m["slug"]]["public"],
            "suspects": [{"name": c["name"], "role": c["role"]} for c in m["clues"]],
            "clues": [{"name": c["name"], "role": c["role"], "quote": c["quote"], "label": c["label"],
                       "evidence": c["evidence"], "poster": posters[i]} for i, c in enumerate(m["clues"])],
            "solution": m["solution"],
        })
    js = json.dumps(out, ensure_ascii=False)
    assert "JSON_END" not in js
    with open(target, "w") as f:
        f.write("<?php\n// Generated by tools/export.py – do not edit by hand.\nreturn json_decode(<<<'JSON_END'\n" + js + "\nJSON_END, true);\n")


if __name__ == "__main__":
    ms = load_all()
    errs = validate(ms)
    if errs:
        print("NOT EXPORTED – fix these first:")
        print("\n".join(errs))
        sys.exit(1)
    export(ms, os.path.join(HERE, "..", "app", "mysteries.php"))
    import datetime
    with open(os.path.join(HERE, "..", "VERSION"), "w") as f:
        f.write(datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d%H%M%S") + f"-{len(ms)}\n")
    by = {}
    for m in ms:
        by[m["level"]] = by.get(m["level"], 0) + 1
    print(f"Exported {len(ms)} mysteries: " + ", ".join(f"level {k}: {v}" for k, v in sorted(by.items())))
    sched = json.load(open(os.path.join(HERE, "schedule.json")))
    import datetime as _d
    today = _d.date.today().isoformat()
    lib = sum(1 for v in sched.values() if not v.get("daily"))
    dailies = [v["daily"] for v in sched.values() if v.get("daily")]
    ahead = sum(1 for d in dailies if d > today)
    print(f"Library: {lib} cases (target {LIBRARY_SIZE})")
    try:
        import m_images; m_images.main()
    except Exception as ex:
        print("Portrait list not updated:", ex)
    print(f"Daily cases scheduled until {max(dailies) if dailies else '-'} ({ahead} days ahead of today)")
