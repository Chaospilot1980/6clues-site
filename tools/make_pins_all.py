"""Generate pins for landing pages, Christmas page, game nights and live escape rooms -> assets/img/pins/"""
import os, re, json, subprocess, glob
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = R + '/assets/img/pins/'; os.makedirs(out, exist_ok=True)
def pin(bg, name, kicker, title, footer='Free to play · 6clues.com'):
    dst = out + name + '.jpg'
    if os.path.exists(dst) and os.path.getmtime(dst) > os.path.getmtime(bg): return
    subprocess.run(['python3', R + '/tools/make_pin.py', bg, dst, kicker, title, footer], check=True)
E = R + '/assets/img/escape/'
first = lambda d: sorted(glob.glob(E + d + '/*.jpg'))[0]
landings = {
  'free-escape-rooms-for-kids': (E + 'the-clockmakers-last-hour', 'Family escape games', 'Free Escape Rooms for Kids'),
  'classroom-escape-room': (E + 'the-codebreakers-hut', 'For teachers · free', 'Free Classroom Escape Rooms'),
  'christmas-escape-room': (R + '/assets/img/gn/the-christmas-market-cash-box/cover.jpg', 'Holiday escape games', 'Free Christmas Escape Rooms'),
  'murder-mystery-for-kids': (R + '/assets/img/m/the-counterfeit-christmas/cover.jpg', 'Kids’ whodunits · free', 'Detective Mysteries for Kids'),
  'whodunit-puzzles-for-adults': (R + '/assets/img/m/death-in-the-snow/cover.jpg', 'Mastermind cases', 'Hard Whodunit Puzzles for Adults'),
  'printable-murder-mystery-games': (R + '/assets/img/gn/overboard-at-midnight/cover.jpg', 'Print & play', 'Free Printable Murder Mystery Games'),
  'how-to-host-a-murder-mystery-party': (R + '/assets/img/gn/the-last-invitation/cover.jpg', 'Party guide', 'How to Host a Murder Mystery Party'),
  'detective-games-online': (R + '/assets/img/escape/the-detective-academy/evidence.jpg', 'Play free online', 'Free Detective Games Online'),
  'christmas-murder-mystery': (R + '/assets/img/m/death-at-the-winter-circus/cover.jpg', 'Holiday whodunits', 'Free Christmas Murder Mystery Games'),
}
for slug, (bg, k, t) in landings.items():
    if os.path.isdir(bg): bg = first(bg[len(E):])
    if os.path.exists(bg): pin(bg, 'page-' + slug, k, t)
for c in glob.glob(R + '/assets/img/gn/*/cover.jpg'):
    slug = c.split('/')[-2]; php = R + '/app/gamenight/' + slug + '.php'
    m = re.search(r"'title'\s*=>\s*'([^']+)'", open(php).read()) if os.path.exists(php) else None
    pin(c, 'gn-' + slug, 'Printable murder mystery game', (m.group(1) if m else slug.replace('-', ' ').title()), 'Free game night case · 6clues.com')
esc = open(R + '/app/escape.php').read()
for d in os.listdir(E):
    m = re.search(r"'" + d + r"' => \[\s*'title' => '([^']+)'", esc)
    if m and glob.glob(E + d + '/*.jpg'): pin(first(d), 'esc-' + d, 'Free online escape room', m.group(1).replace('’', "'"))
print(len(os.listdir(out)), 'pins')
