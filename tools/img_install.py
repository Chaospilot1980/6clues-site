"""Installs generated mystery images into assets/img/m/<case>/<name>.jpg.

Usage:
  python3 tools/img_install.py --missing-json        # print the still-missing keys as JSON
  python3 tools/img_install.py --missing-compact     # same, compact form for localStorage.__6c_missing
  python3 tools/img_install.py SRC [SRC ...]        # install files/folders/ZIPs, then run export.py
  python3 tools/img_install.py --no-export SRC ...

SRC may be files named 6c__<case>__<name>.(jpg|jpeg|png|webp), folders containing them,
ZIPs of them, or ZIPs/folders laid out as <case>/<name>.ext. Images are cropped to the site's
size (portraits 1024x1024, evidence photos 1024x768, covers 1600x1200) and saved as JPG under
the size limit. Existing images are never overwritten (use --force).
"""
import io, json, os, re, subprocess, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DEST = os.path.join(ROOT, "assets", "img", "m")
EXT = (".jpg", ".jpeg", ".png", ".webp")


def missing():
    subprocess.run([sys.executable, os.path.join(HERE, "m_images.py")], check=True, stdout=subprocess.DEVNULL)
    txt = open(os.path.join(HERE, "mystery_images.md"), encoding="utf-8").read()
    return [m[:-4] for m in re.findall(r"^### `([^`]+\.jpg)`", txt, re.M)]


def spec(key):
    name = key.split("/", 1)[1]
    if name == "cover":
        return 1600, 1200, 500_000
    if name.startswith("photo-"):
        return 1024, 768, 300_000
    return 1024, 1024, 400_000


def key_of(path):
    base = os.path.basename(path)
    stem, ext = os.path.splitext(base)
    if ext.lower() not in EXT:
        return None
    m = re.match(r"^6c__([a-z0-9\-]+)__([a-z0-9\-]+?)(?: \(\d+\))?$", stem)
    if m:
        return f"{m.group(1)}/{m.group(2)}"
    parent = os.path.basename(os.path.dirname(path))
    if re.fullmatch(r"[a-z0-9\-]+", parent or "") and re.fullmatch(r"[a-z0-9\-]+", stem):
        return f"{parent}/{stem}"
    return None


def sources(args):
    for a in args:
        if os.path.isdir(a):
            for d, _, fs in os.walk(a):
                for f in sorted(fs):
                    p = os.path.join(d, f)
                    if f.lower().endswith(".zip"):
                        yield from sources([p])
                    elif key_of(p):
                        yield key_of(p), lambda p=p: open(p, "rb").read()
        elif a.lower().endswith(".zip"):
            z = zipfile.ZipFile(a)
            for n in z.namelist():
                k = key_of(n)
                if k:
                    yield k, lambda n=n, z=z: z.read(n)
        elif key_of(a):
            yield key_of(a), lambda a=a: open(a, "rb").read()


def install(key, data, force=False):
    from PIL import Image
    out = os.path.join(DEST, key + ".jpg")
    if os.path.exists(out) and not force:
        return "exists"
    w, h, limit = spec(key)
    im = Image.open(io.BytesIO(data)).convert("RGB")
    s = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    l, t = (im.width - w) // 2, (im.height - h) // 2
    im = im.crop((l, t, l + w, t + h))
    for q in (82, 78, 72, 66, 60, 54):
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=q, optimize=True, progressive=True)
        if buf.tell() <= limit:
            break
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "wb").write(buf.getvalue())
    return f"ok {buf.tell() // 1024} KB"


def main():
    a = sys.argv[1:]
    if "--missing-json" in a:
        print(json.dumps(missing()))
        return
    if "--missing-compact" in a:
        groups = {}
        for k in missing():
            c, n = k.split("/", 1)
            groups.setdefault(c, []).append(n)
        print(";".join(c + ":" + ",".join(v) for c, v in groups.items()))
        return
    force = "--force" in a
    run_export = "--no-export" not in a
    srcs = [x for x in a if not x.startswith("--")]
    want = set(missing())
    n = 0
    for key, read in sources(srcs):
        if key not in want and not force:
            print(f"skip {key} (not missing)")
            continue
        r = install(key, read(), force)
        print(f"{key}: {r}")
        n += r.startswith("ok")
        want.discard(key)
    print(f"installed {n} image(s); {len(want)} still missing")
    if run_export and n:
        subprocess.run([sys.executable, os.path.join(HERE, "export.py")], check=True)


if __name__ == "__main__":
    main()
