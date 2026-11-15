import re
import json, os, datetime

INK = "#1E1B18"; RED = "#A4161A"; PAPER = "#F3EEE4"; CARD = "#FFFDF8"; MUTED = "#5C554D"
W, H = 794, 1123
TW = "font-family: 'Special Elite', 'Courier New', monospace"
MONO = "font-family: 'Courier Prime', 'Courier New', monospace"
SANS = "font-family: Inter, system-ui, sans-serif"

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Special+Elite&amp;family=Courier+Prime:wght@400;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0}}
a{{color:#A4161A}}a:hover{{color:#7A0F12}}
</style>
</helmet>
"""
TAIL = """
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
"""

QR = f'<div style="display: flex; flex-direction: column; align-items: center; gap: 4px; background: #FFFFFF; border: 1.5px solid {INK}; padding: 6px"><div class="qr" data-url="{{{{ANSWER_URL}}}}" style="width: 96px; height: 96px"></div><div style="{SANS}; font-size: 10px; font-weight: 700; letter-spacing: 0.1em; color: {INK}">SCAN TO ANSWER</div></div>'
SILHOUETTE = """<svg width="120" height="130" viewBox="0 0 120 130" aria-hidden="true"><circle cx="60" cy="44" r="30" fill="#B9B0A2"></circle><path d="M8 130 C8 92 30 80 60 80 C90 80 112 92 112 130 Z" fill="#B9B0A2"></path></svg>"""

TH = f'style="{SANS}; font-size: 12px; font-weight: 700; text-align: left; padding: 7px 8px; background: {INK}; color: {PAPER}"'

# ---------- evidence helpers ----------
def ev_title(t):
    return f'<div style="{TW}; font-size: 19px; color: {INK}; margin-bottom: 6px">{t}</div>'

def ev_rows(title, rows, note=None):
    out = ev_title(title)
    for k, v in rows:
        out += (f'<div style="display: flex; gap: 12px; padding: 5px 0; border-bottom: 1px solid #D8D0C2">'
                f'<div style="width: 150px; flex-shrink: 0; {SANS}; font-size: 13px; font-weight: 600; color: {MUTED}">{k}</div>'
                f'<div style="{SANS}; font-size: 14px; color: {INK}; line-height: 1.4">{v}</div></div>')
    if note:
        out += f'<div style="{TW}; font-size: 16px; color: {RED}; margin-top: 8px; transform: rotate(-1deg)">{note}</div>'
    return f'<div style="display: flex; flex-direction: column; gap: 2px">{out}</div>'

def ev_table(title, headers, rows, highlight=None, note=None, mono_cols=(0, 1)):
    trs = ""
    for r in rows:
        hl = highlight and highlight(r)
        cells = ""
        for i, c in enumerate(r):
            fam = MONO if i in mono_cols else SANS
            col = RED if hl else INK
            fw = "700" if hl else "400"
            cells += f'<td style="{fam}; font-size: 14px; font-weight: {fw}; padding: 6px 8px; border-bottom: 1px solid #C9C0B1; color: {col}">{c}</td>'
        trs += f"<tr>{cells}</tr>"
    head = "".join(f"<th {TH}>{h}</th>" for h in headers)
    n = f'<div style="{SANS}; font-size: 13px; color: {MUTED}; line-height: 1.45">{note}</div>' if note else ""
    return (f'<div style="display: flex; flex-direction: column; gap: 10px">{ev_title(title)}'
            f'<table style="border-collapse: collapse; width: 100%"><tr>{head}</tr>{trs}</table>{n}</div>')

def ev_programme(heading, sub, items, sticky):
    prog = "".join(f'<div style="display: flex; gap: 18px; padding: 7px 0; border-bottom: 1px dotted #B9B0A2"><div style="{MONO}; font-size: 16px; font-weight: 700; width: 64px; color: {INK}">{t}</div><div style="{SANS}; font-size: 15px; color: {INK}">{d}</div></div>' for t, d in items)
    return f"""<div style="display: flex; gap: 22px; height: 100%">
<div style="flex: 1; display: flex; flex-direction: column">
<div style="{TW}; font-size: 22px; color: {INK}; text-align: center; margin-bottom: 4px">{heading}</div>
<div style="{SANS}; font-size: 12px; letter-spacing: 0.16em; color: {MUTED}; text-align: center; margin-bottom: 10px">{sub}</div>
{prog}
</div>
<div style="width: 190px; flex-shrink: 0; align-self: center; background: #F6E27A; padding: 16px; transform: rotate(3deg); {TW}; font-size: 16px; line-height: 1.4; color: {INK}">{sticky}</div>
</div>"""

def ev_phone(title, caption, msgs):
    b = ""
    for to, time, text in msgs:
        b += (f'<div style="display: flex; flex-direction: column; gap: 4px; align-items: flex-end">'
              f'<div style="{SANS}; font-size: 12px; color: {MUTED}">To: <b style="color: {INK}">{to}</b> · {time}</div>'
              f'<div style="max-width: 82%; background: #2F6FD6; color: #FFFFFF; border-radius: 14px 14px 4px 14px; padding: 9px 13px; {SANS}; font-size: 14px; line-height: 1.4">{text}</div></div>')
    return f"""<div style="display: flex; gap: 22px; height: 100%">
<div style="width: 150px; flex-shrink: 0; display: flex; flex-direction: column; gap: 10px">
<div style="{TW}; font-size: 19px; color: {INK}; line-height: 1.3">{title}</div>
<div style="{SANS}; font-size: 13px; color: {MUTED}; line-height: 1.5">{caption}</div>
</div>
<div style="flex: 1; background: #ECE8E1; border: 6px solid {INK}; border-radius: 22px; padding: 14px; display: flex; flex-direction: column; gap: 10px; overflow: hidden">{b}</div>
</div>"""

def ev_note(title, lines, sign, side=None):
    body = "".join(f'<div style="{TW}; font-size: 16px; line-height: 1.5; color: {INK}">{l}</div>' for l in lines)
    s = ""
    if side:
        s = f'<div style="width: 170px; flex-shrink: 0; align-self: center; {SANS}; font-size: 13px; color: {MUTED}; line-height: 1.5">{side}</div>'
    return f"""<div style="display: flex; gap: 22px; height: 100%; align-items: center">
<div style="flex: 1; background: #FFFFFF; border: 1px solid #C9C0B1; padding: 18px 22px; transform: rotate(-1deg); display: flex; flex-direction: column; gap: 6px; background-image: repeating-linear-gradient(transparent, transparent 23px, #E3DCCF 24px)">
<div style="{SANS}; font-size: 12px; font-weight: 700; letter-spacing: 0.14em; color: {MUTED}">{title}</div>
{body}
<div style="{TW}; font-size: 16px; color: {RED}; text-align: right">{sign}</div>
</div>{s}
</div>"""

def ev_receipt(lines):
    body = ""
    for kind, text in lines:
        if kind == "h": body += f'<div style="text-align: center; font-weight: 700; font-size: 18px">{text}</div>'
        elif kind == "s": body += f'<div style="text-align: center; font-size: 12px; margin-bottom: 8px">{text}</div>'
        elif kind == "hr": body += f'<div style="border-top: 1px dashed {INK}; margin-top: 6px; padding-top: 6px">{text}</div>'
        elif kind == "b": body += f'<div style="font-weight: 700">{text}</div>'
        else: body += f'<div>{text}</div>'
    return f"""<div style="display: flex; justify-content: center; height: 100%">
<div style="width: 340px; background: #FFFFFF; border: 1px solid #C9C0B1; padding: 16px 20px; {MONO}; font-size: 14px; color: {INK}; line-height: 1.55; transform: rotate(-1.5deg)">{body}</div>
</div>"""

def ev_photos(title, photos):
    cards = ""
    for name, time, cap in photos:
        cards += f"""<div style="flex: 1; min-width: 0; background: #FFFFFF; border: 1px solid #C9C0B1; padding: 8px 8px 10px; display: flex; flex-direction: column; gap: 6px">
<div style="height: 120px; background: #CFC6B6; display: flex; align-items: center; justify-content: center; {MONO}; font-size: 12px; color: {INK}">{name}</div>
<div style="{MONO}; font-size: 14px; font-weight: 700; color: {RED}">{time}</div>
<div style="{SANS}; font-size: 13px; line-height: 1.4; color: {INK}">{cap}</div>
</div>"""
    return f'<div style="display: flex; flex-direction: column; gap: 10px">{ev_title(title)}<div style="display: flex; gap: 12px">{cards}</div></div>'

# ---------- layout ----------
def header(m, n, qr=False):
    return f"""<div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 24px">
<div style="display: flex; flex-direction: column; gap: 6px">
<div style="{SANS}; font-size: 13px; font-weight: 700; letter-spacing: 0.18em; color: {RED}">{m['caseno']} · LEVEL {m.get('level', 1)} · {m.get('crime', 'MURDER')}</div>
<h1 style="margin: 0; {TW}; font-size: 46px; line-height: 1.02; color: {INK}; font-weight: 400">{m['title_html']}</h1>
</div>
<div style="display: flex; gap: 18px; align-items: flex-start">
<div style="transform: rotate(4deg); border: 4px solid {RED}; color: {RED}; padding: 10px 16px; text-align: center; {TW}; margin-top: 8px; background: {CARD}">
<div style="font-size: 15px; letter-spacing: 0.08em">CLUE</div>
<div style="font-size: 44px; line-height: 1">{n}</div>
<div style="font-size: 15px; letter-spacing: 0.08em">OF 6</div>
</div>{QR if qr else ""}
</div>
</div>"""

def slugify(x):
    import unicodedata
    x = unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", x.lower()).strip("-")

def suspect(name, role, quote, face=None):
    return f"""<div style="display: flex; gap: 24px; align-items: stretch; height: 290px">
<div style="width: 210px; flex-shrink: 0; transform: rotate(-2deg); background: {CARD}; border: 1.5px solid {INK}; padding: 12px 12px 10px; display: flex; flex-direction: column; gap: 8px; position: relative; box-sizing: border-box">
<div style="position: absolute; top: -9px; left: 97px; width: 18px; height: 18px; border-radius: 50%; background: {RED}"></div>
<div style="height: 190px; background: #DDD5C7; display: flex; align-items: flex-end; justify-content: center; overflow: hidden">{"{{FACE:" + face + "}}" if face else SILHOUETTE}</div>
<div style="{SANS}; font-size: 17px; font-weight: 700; color: {INK}; line-height: 1.2">{name}</div>
<div style="{SANS}; font-size: 13px; color: {MUTED}; margin-top: -6px">{role}</div>
</div>
<div style="flex: 1; min-width: 0; background: {CARD}; border: 3px solid {INK}; border-radius: 6px; padding: 20px 22px; display: flex; flex-direction: column; justify-content: center; gap: 12px; box-sizing: border-box">
<div style="{TW}; font-size: 18px; line-height: 1.45; color: {INK}">”{quote}”</div>
<div style="{SANS}; font-size: 12px; font-weight: 600; letter-spacing: 0.12em; color: {MUTED}">WITNESS STATEMENT · {name.upper()}</div>
</div>
</div>"""

def footer(n, qr=False):
    dots = ""
    for i in range(1, 7):
        on = i == n
        dots += (f'<div style="width: 30px; height: 30px; border-radius: 50%; border: 2px solid {RED if on else INK}; '
                 f'background: {RED if on else "transparent"}; color: {"#FFFFFF" if on else INK}; display: flex; '
                 f'align-items: center; justify-content: center; {SANS}; font-size: 13px; font-weight: 700">{i}</div>')
    return f"""<div style="display: flex; justify-content: space-between; align-items: center; gap: 24px; border-top: 2px solid {INK}; padding-top: 14px">
<div style="display: flex; flex-direction: column; gap: 8px">
<div style="display: flex; gap: 8px">{dots}</div>
<div style="{SANS}; font-size: 13px; color: {INK}">{"Find all 6 clues, then scan the code to name the culprit." if qr else "Find the other clues and write your answer on the answer card."}</div>
</div>
<div style="display: flex; flex-direction: column; gap: 4px; width: 250px">
<div style="{SANS}; font-size: 12px; font-weight: 700; letter-spacing: 0.12em; color: {MUTED}">NEXT CLUE IS HIDDEN …</div>
<div style="border-bottom: 1.5px dashed {INK}; height: 30px"></div>
</div>
</div>"""

def poster(m, n, c, qr=False):
    body = f"""<div style="width: {W}px; height: {H}px; box-sizing: border-box; padding: 44px; background: {PAPER}; display: flex; flex-direction: column; gap: 18px; overflow: hidden">
{header(m, n, qr)}
<div style="background: {INK}; color: {PAPER}; padding: 14px 18px; {SANS}; font-size: 14px; line-height: 1.5">{m['intro']}</div>
{suspect(c['name'], c['role'], c['quote'], m['slug'] + '/' + slugify(c['name']))}
<div style="flex: 1; min-height: 0; display: flex; flex-direction: column">
<div style="align-self: flex-start; background: {RED}; color: #FFFFFF; {SANS}; font-size: 12px; font-weight: 700; letter-spacing: 0.14em; padding: 6px 12px">EVIDENCE #{n} · {c['label']}</div>
<div style="flex: 1; min-height: 0; background: {CARD}; border: 1.5px solid {INK}; padding: 18px 20px; box-sizing: border-box; overflow: hidden">{c['evidence']}</div>
</div>
{footer(n, qr)}
</div>"""
    return HEAD.format(title=f"Clue {n} – {c['name']}") + body + TAIL.format(w=W, h=H)

def answer_sheet(m):
    names = sorted([c['name'] for c in m['clues']], key=str.lower)   # alphabetical – no positional hint
    boxes = "".join(f'<div style="display: flex; align-items: center; gap: 8px; {SANS}; font-size: 14px; color: {INK}"><div style="width: 16px; height: 16px; border: 2px solid {INK}; flex-shrink: 0"></div>{x}</div>' for x in names)
    line = f'<div style="border-bottom: 1.5px solid {INK}; height: 26px"></div>'
    card = f"""<div style="flex: 1; display: flex; flex-direction: column; gap: 12px; border: 3px solid {INK}; background: {CARD}; padding: 22px 26px; box-sizing: border-box">
<div style="display: flex; justify-content: space-between; align-items: baseline">
<div style="{TW}; font-size: 28px; color: {INK}">ANSWER CARD</div>
<div style="{SANS}; font-size: 12px; font-weight: 700; letter-spacing: 0.16em; color: {RED}">{m['title_plain'].upper()}</div>
</div>
<div style="display: flex; gap: 12px; align-items: flex-end"><div style="{SANS}; font-size: 13px; font-weight: 600; color: {MUTED}; width: 90px">Detective</div><div style="flex: 1; border-bottom: 1.5px solid {INK}; height: 22px"></div></div>
<div style="{SANS}; font-size: 13px; font-weight: 700; letter-spacing: 0.1em; color: {INK}">WHO IS THE {m.get('who', 'killer').upper()}? (tick one)</div>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px">{boxes}</div>
<div style="{SANS}; font-size: 13px; font-weight: 700; letter-spacing: 0.1em; color: {INK}; margin-top: 4px">MOTIVE</div>
{line}
<div style="{SANS}; font-size: 13px; font-weight: 700; letter-spacing: 0.1em; color: {INK}; margin-top: 4px">WHICH EVIDENCE GIVES THE {m.get('who', 'killer').upper()} AWAY?</div>
{line}{line}
</div>"""
    body = f"""<div style="width: {W}px; height: {H}px; box-sizing: border-box; padding: 44px; background: {PAPER}; display: flex; flex-direction: column">
{card}
<div style="height: 44px; display: flex; align-items: center; gap: 10px"><div style="flex: 1; border-top: 1.5px dashed {MUTED}"></div><div style="{SANS}; font-size: 12px; color: {MUTED}">cut here</div><div style="flex: 1; border-top: 1.5px dashed {MUTED}"></div></div>
{card}
</div>"""
    return HEAD.format(title="Answer card") + body + TAIL.format(w=W, h=H)

def solution(m):
    s = m['solution']
    def sect(t, b): return f'<div style="display: flex; flex-direction: column; gap: 6px"><div style="{SANS}; font-size: 13px; font-weight: 700; letter-spacing: 0.12em; color: {RED}">{t}</div>{b}</div>'
    def p(t): return f'<div style="{SANS}; font-size: 14px; line-height: 1.5; color: {INK}">{t}</div>'
    def li(items): return "".join(f'<div style="display: flex; gap: 10px; {SANS}; font-size: 14px; line-height: 1.5; color: {INK}"><div style="color: {RED}; font-weight: 700">{i+1}.</div><div>{t}</div></div>' for i, t in enumerate(items))
    setup = ["Print clues 1–6 on A4, or scale up to A3, and put them up in 6 different places.",
             "Optionally, write a small hint to the next location in the box at the bottom of each poster.",
             "Print the answer cards, cut them in half and hand them out. Keep this page hidden until the big reveal."]
    body = f"""<div style="width: {W}px; height: {H}px; box-sizing: border-box; padding: 56px; background: {PAPER}; display: flex; flex-direction: column; gap: 18px; overflow: hidden">
<div style="display: flex; justify-content: space-between; align-items: flex-start">
<h1 style="margin: 0; {TW}; font-size: 40px; font-weight: 400; color: {INK}; line-height: 1.05">SOLUTION</h1>
<div style="transform: rotate(3deg); border: 3px solid {RED}; color: {RED}; padding: 6px 12px; {TW}; font-size: 18px">HOST ONLY</div>
</div>
<div style="background: {INK}; color: {PAPER}; padding: 16px 20px; {TW}; font-size: 24px">The {m.get('who', 'killer')} is {s['killer'].upper()}</div>
{sect("MOTIVE", p(s['motive']))}
{sect("HOW THEY GIVE THEMSELVES AWAY", li(s['proof']))}
{sect("THE OTHERS ARE CLEARED", li(s['cleared']))}
{sect("HOW TO SET IT UP", li(setup))}
</div>"""
    return HEAD.format(title="Solution – host only") + body + TAIL.format(w=W, h=H)

def build(m, root):
    proj = f"{root}/project"
    os.makedirs(proj, exist_ok=True)
    order = []
    for i, c in enumerate(m['clues']):
        fn = "Main.dc.html" if i == 0 else f"Clue-{i+1}.dc.html"
        open(f"{proj}/{fn}", "w").write(poster(m, i + 1, c))
        order.append(fn)
    open(f"{proj}/Answer-card.dc.html", "w").write(answer_sheet(m))
    open(f"{proj}/Solution.dc.html", "w").write(solution(m))
    order.append("Answer-card.dc.html")
    boards = {}
    for i, fn in enumerate(order):
        t = "Answer card (2 per sheet)" if fn.startswith("Answer") else f"Clue {i+1}"
        boards[fn] = {"x": (i % 4) * (W + 80), "y": (i // 4) * (H + 120), "w": W, "h": H, "title": t, "page": "posters"}
    boards["Solution.dc.html"] = {"x": 0, "y": 0, "w": W, "h": H, "title": "Solution – host only", "page": "host"}
    order.append("Solution.dc.html")
    canvas = {"v": 3, "createdOnFiles": {"v": 1, "at": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")},
              "title": m['canvas_title'], "launch": {"view": "canvas", "page": "posters"},
              "pages": [{"id": "posters", "name": "Posters and answer cards"}, {"id": "host", "name": "Solution (host only)"}],
              "boards": boards, "order": order, "notes": {}, "designSystems": []}
    json.dump(canvas, open(f"{proj}/canvas.json", "w"), ensure_ascii=False, indent=1)
    return order
