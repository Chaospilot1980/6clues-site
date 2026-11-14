"""Renders every poster in headless Chrome and reports text that overflows its box.

Usage: python3 tools/check_layout.py [slug ...]
Needs: pip install playwright, and Google Chrome at /usr/bin/google-chrome (or set CHROME=path).
"""
import os, re, sys, subprocess, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from export import load_all  # noqa: E402
from lib import poster  # noqa: E402

FONTS = os.path.join(ROOT, "assets", "fonts")
FONT_CSS = "".join(
    f"@font-face{{font-family:{fam};font-weight:{w};src:url('file://{FONTS}/{f}')}}"
    for fam, w, f in [("'Special Elite'", 400, "special-elite-latin-400-normal.woff2"),
                      ("Inter", 400, "inter-latin-400-normal.woff2"), ("Inter", 600, "inter-latin-600-normal.woff2"),
                      ("Inter", 700, "inter-latin-700-normal.woff2"),
                      ("'Courier Prime'", 400, "courier-prime-latin-400-normal.woff2"),
                      ("'Courier Prime'", 700, "courier-prime-latin-700-normal.woff2")])

CHECK_JS = """() => {
  const bad = [];
  document.querySelectorAll('.sheet').forEach((s, i) => {
    s.querySelectorAll('div').forEach(d => {
      const st = getComputedStyle(d);
      if ((st.overflow === 'hidden') && d.scrollHeight > d.clientHeight + 2 && d.clientHeight > 50)
        bad.push({poster: i + 1, over: d.scrollHeight - d.clientHeight});
    });
  });
  return bad;
}"""


def main(slugs):
    from playwright.sync_api import sync_playwright
    ms = [m for m in load_all() if not slugs or m["slug"] in slugs]
    problems = 0
    with sync_playwright() as p:
        br = p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"))
        pg = br.new_page(viewport={"width": 900, "height": 1200})
        for m in ms:
            sheets = []
            for i, c in enumerate(m["clues"]):
                html = poster(m, i + 1, c, qr=True)
                body = html.split("<x-dc>", 1)[1].split("</x-dc>", 1)[0]
                body = re.sub(r"<helmet>.*?</helmet>", "", body, flags=re.S)
                sheets.append(f"<div class='sheet' style='width:794px;height:1123px'>{body}</div>")
            doc = f"<html><head><meta charset='utf-8'><style>{FONT_CSS} body{{margin:0}}</style></head><body>{''.join(sheets)}</body></html>"
            with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
                f.write(doc)
            pg.goto("file://" + f.name)
            pg.wait_for_timeout(300)
            bad = pg.evaluate(CHECK_JS)
            if bad:
                problems += 1
                print(f"OVERFLOW {m['slug']}: " + ", ".join(f"clue {b['poster']} +{b['over']}px" for b in bad))
        br.close()
    print("Layout OK" if not problems else f"{problems} mystery(ies) overflow – shorten the text or evidence rows")
    return problems


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1:]) else 0)
