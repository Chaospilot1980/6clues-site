/* Six Clues escape room #1 – The Clockmaker's Last Hour (prototype).
 * Scenes are SVG placeholders. Drop real art in /assets/img/escape/the-clockmakers-last-hour/<room>.jpg (1600x900)
 * and the voice in /assets/audio/escape/the-clockmakers-last-hour/record.mp3 – they are picked up automatically. */
(() => {
'use strict';
const root = document.getElementById('escape');
const SLUG = root.dataset.slug, CSRF = root.dataset.csrf, NAME = root.dataset.name || 'Detective';
const LIMIT = 3600000, IMG = '/assets/img/escape/' + SLUG + '/', AUDIO = '/assets/audio/escape/' + SLUG + '/';
const fresh = () => ({ v: 1, room: 'workshop', inv: [], flags: {}, notes: [], elapsed: 0, penalty: 0, hints: {}, hintCount: 0, started: false, over: false });
let S = Object.assign(fresh(), window.ESCAPE_STATE || {});
let sel = null, paused = false, dirty = false, last = performance.now(), finished = false;

/* ---------------- items ---------------- */
const ITEMS = {
  screwdriver: ['🪛', 'Screwdriver', 'A small brass screwdriver from Elias’s coat pocket.'],
  loupe: ['🔍', 'Watchmaker’s loupe', 'A loupe for reading the very small.'],
  photoL: ['🖼️', 'Torn photo (left)', 'A young Elias on a quay. On the back, in pencil: “Ber…”'],
  photoR: ['🖼️', 'Torn photo (right)', 'A harbour and a church spire. On the back: “…gen · 4:20 pm · 1902”'],
  photo: ['🖼️', 'Photograph', 'Elias at 25 on a quay. On the back: “Bergen · 4:20 pm · 1902 – the day I learned to listen.”'],
  studyKey: ['🗝️', 'Small iron key', 'It was hidden behind the cuckoo. The bow is shaped like a book.'],
  needle: ['📍', 'Gramophone needle', 'A steel needle in a little paper envelope marked “for the last record”.'],
  weight: ['⚖️', 'Pendulum weight', 'A heavy brass bob with a hook.'],
  sketch: ['📜', 'Gear sketch', 'Three circles drawn on pegs A, B and C: a middle-sized one, a small one, a large one.'],
  towerKey: ['🔑', 'Tower key', 'A long key stamped with a tiny clock face.'],
};
const has = i => S.inv.includes(i);
const give = i => { if (!has(i)) S.inv.push(i); dirty = true; renderInv(); };
const take = i => { S.inv = S.inv.filter(x => x !== i); if (sel === i) sel = null; dirty = true; renderInv(); };
const F = S.flags;
const note = (id, text) => { if (!S.notes.find(n => n.id === id)) { S.notes.push({ id, text }); dirty = true; flashBtn('nb'); } };

/* ---------------- drawing helpers ---------------- */
const clock = (cx, cy, r, h, m, rim, face = '#efe3c4') => {
  const ha = ((h % 12) + m / 60) * 30 - 90, ma = m * 6 - 90, rad = a => a * Math.PI / 180;
  let ticks = '';
  for (let i = 0; i < 12; i++) { const a = rad(i * 30); ticks += `<line x1="${cx + Math.cos(a) * r * .8}" y1="${cy + Math.sin(a) * r * .8}" x2="${cx + Math.cos(a) * r * .9}" y2="${cy + Math.sin(a) * r * .9}" stroke="#3a2a1a" stroke-width="${i % 3 ? 2 : 4}"/>`; }
  for (let n = 1; n <= 12; n++) { const a = rad(n * 30 - 90); ticks += `<text x="${cx + Math.cos(a) * r * .64}" y="${cy + Math.sin(a) * r * .64 + r * .07}" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="${r * .2}" fill="#2a1c10">${n}</text>`; }
  return `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${rim}"/><circle cx="${cx}" cy="${cy}" r="${r * .86}" fill="${face}"/>${ticks}
   <line x1="${cx}" y1="${cy}" x2="${cx + Math.cos(rad(ma)) * r * .76}" y2="${cy + Math.sin(rad(ma)) * r * .76}" stroke="#7a6a58" stroke-width="${r * .03}" stroke-linecap="round"/>
   <line x1="${cx}" y1="${cy}" x2="${cx + Math.cos(rad(ha)) * r * .4}" y2="${cy + Math.sin(rad(ha)) * r * .4}" stroke="#1d140c" stroke-width="${r * .12}" stroke-linecap="round"/>
   <circle cx="${cx}" cy="${cy}" r="${r * .06}" fill="#1d140c"/>`;
};
const label = (x, y, t) => `<text x="${x}" y="${y}" class="lbl" text-anchor="middle">${t}</text>`;
const door = (x, y, w, h, open, t) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="6" fill="${open ? '#140d08' : '#4a3020'}" stroke="#2a1a10" stroke-width="8"/>
  ${open ? '' : `<rect x="${x + 20}" y="${y + 24}" width="${w - 40}" height="${h * .38}" fill="none" stroke="#2a1a10" stroke-width="4"/><rect x="${x + 20}" y="${y + h * .5}" width="${w - 40}" height="${h * .42}" fill="none" stroke="#2a1a10" stroke-width="4"/><circle cx="${x + w - 26}" cy="${y + h * .5}" r="9" fill="#c9a24a"/>`}${label(x + w / 2, y - 14, t)}`;

/* ---------------- rooms ---------------- */
const ROOMS = {
  workshop: {
    name: 'The workshop',
    bg: () => `<rect width="1600" height="900" fill="#2b1d14"/>
      ${Array.from({ length: 16 }, (_, i) => `<rect x="${i * 100}" y="0" width="98" height="640" fill="${i % 2 ? '#33231a' : '#2f2018'}"/>`).join('')}
      <rect y="640" width="1600" height="260" fill="#1d130d"/><rect x="560" y="70" width="230" height="170" fill="#0e1626" stroke="#4a3020" stroke-width="12"/>
      <circle cx="730" cy="115" r="22" fill="#e9e4cf"/>${Array.from({ length: 14 }, (_, i) => `<circle cx="${575 + (i * 37) % 200}" cy="${85 + (i * 53) % 140}" r="3" fill="#fff" opacity=".7"/>`).join('')}
      <line x1="675" y1="70" x2="675" y2="240" stroke="#4a3020" stroke-width="8"/>
      <ellipse cx="800" cy="0" rx="500" ry="380" fill="url(#lamp)"/>`,
    spots: [
      { id: 'clockwall', x: 60, y: 60, w: 470, h: 330, art: () => `<rect x="70" y="70" width="450" height="310" fill="#3b2a1d" rx="8"/>
          ${clock(150, 160, 62, 7, 5, '#a3322b')}${clock(300, 160, 62, 1, 10, '#2e5a9a')}${clock(450, 160, 62, 9, 15, '#3f7a3a')}${clock(225, 300, 62, 3, 20, '#c8a02a')}${clock(375, 300, 62, 12, 0, '#6b5a48')}${label(295, 400, 'Clock wall')}`, act: () => openClockWall() },
      { id: 'cuckoo', x: 860, y: 60, w: 210, h: 330, art: () => `<path d="M880 150 L965 80 L1050 150 Z" fill="#5a3a22"/><rect x="895" y="150" width="140" height="170" fill="#6b4528"/>${clock(965, 225, 48, 11, 55, '#8a6a3a')}
          <rect x="945" y="160" width="40" height="22" fill="#1d140c"/>${F.cuckooOpen ? '<rect x="900" y="300" width="130" height="16" fill="#140d08"/>' : ''}<line x1="940" y1="320" x2="940" y2="380" stroke="#8a7a5a" stroke-width="3"/><line x1="990" y1="320" x2="990" y2="370" stroke="#8a7a5a" stroke-width="3"/><path d="M932 380 l8 -10 l8 10 z M982 370 l8 -10 l8 10z" fill="#8a6a3a"/>${label(965, 70, 'Cuckoo clock')}`,
        act: () => F.cuckooOpen ? say('The back panel hangs open. Nothing more inside.') : say('Four tiny screws hold the back panel. Something rattles inside when you tilt it.'),
        use: { screwdriver: () => { F.cuckooOpen = 1; take('screwdriver'); give('studyKey'); say('You unscrew the back panel. Behind the bellows: a small iron key with a book-shaped bow.'); return true; } } },
      { id: 'coat', x: 1110, y: 120, w: 150, h: 330, art: () => `<circle cx="1185" cy="130" r="9" fill="#c9a24a"/><path d="M1185 135 L1130 190 L1120 430 L1250 430 L1240 190 Z" fill="#2c3440"/><path d="M1185 140 L1165 260 L1185 300 L1205 260 Z" fill="#232a33"/><rect x="1140" y="330" width="40" height="34" fill="#232a33"/>${label(1185, 460, 'Elias’s coat')}`,
        act: () => { if (F.coat) return say('Empty pockets now. It smells of oil and pipe smoke.'); F.coat = 1; give('screwdriver'); say('In the inside pocket: a small brass screwdriver.'); } },
      { id: 'bench', x: 300, y: 470, w: 760, h: 200, art: () => `<rect x="300" y="500" width="760" height="40" fill="#5b3c25"/><rect x="320" y="540" width="720" height="130" fill="#4a3020"/>
          <rect x="430" y="570" width="200" height="70" fill="${F.drawerOpen ? '#140d08' : '#5b3c25'}" stroke="#2a1a10" stroke-width="4"/>${F.drawerOpen ? '' : '<rect x="490" y="595" width="80" height="22" fill="#1d140c"/><circle cx="505" cy="606" r="4" fill="#c9a24a"/><circle cx="522" cy="606" r="4" fill="#c9a24a"/><circle cx="539" cy="606" r="4" fill="#c9a24a"/><circle cx="556" cy="606" r="4" fill="#c9a24a"/>'}
          ${label(530, 665, 'Drawer')}<rect x="760" y="478" width="90" height="22" fill="#c9a24a"/>${label(805, 470, 'Brass plate')}<rect x="900" y="470" width="110" height="30" fill="#d9ccaa" transform="rotate(-6 955 485)"/>${label(955, 460, 'Letter')}`,
        act: () => openBench() },
      { id: 'toStudy', x: 1330, y: 180, w: 200, h: 470, art: () => door(1340, 200, 180, 440, F.studyOpen, F.studyOpen ? 'To the study →' : 'Study door'),
        act: () => F.studyOpen ? go('study') : say('Locked. The keyhole is small and old-fashioned.'),
        use: { studyKey: () => { F.studyOpen = 1; take('studyKey'); say('The key turns with a dry click. The study door swings open.'); return true; } } },
    ],
  },
  study: {
    name: 'The study',
    bg: () => `<rect width="1600" height="900" fill="#1e2420"/>${Array.from({ length: 9 }, (_, i) => `<rect x="${i * 180}" y="0" width="176" height="640" fill="#232b26"/>`).join('')}
      <rect y="640" width="1600" height="260" fill="#2a1c13"/><ellipse cx="800" cy="900" rx="700" ry="140" fill="#4a1e1e" opacity=".7"/><ellipse cx="900" cy="0" rx="560" ry="400" fill="url(#lamp)"/>`,
    spots: [
      { id: 'back', x: 20, y: 760, w: 220, h: 110, art: () => `<text x="40" y="830" class="lbl big">← Workshop</text>`, act: () => go('workshop') },
      { id: 'shelf', x: 60, y: 80, w: 360, h: 560, art: () => `<rect x="70" y="80" width="340" height="560" fill="#3b2a1d"/>${[0, 1, 2, 3].map(r => `<rect x="70" y="${200 + r * 130}" width="340" height="12" fill="#2a1a10"/>` + Array.from({ length: 9 }, (_, i) => `<rect x="${85 + i * 35}" y="${110 + r * 130 + (i * 7) % 20}" width="28" height="${88 - (i * 7) % 20}" fill="${['#7a2a22', '#2a4a6a', '#5a5a2a', '#6a4a2a', '#3a3a5a', '#7a5a2a', '#2a5a3a', '#5a2a4a', '#8a6a3a'][(i + r * 2) % 9]}"/>`).join('')).join('')}${label(240, 70, 'Bookshelf')}`, act: () => openShelf() },
      { id: 'globe', x: 470, y: 330, w: 220, h: 330, art: () => `<line x1="580" y1="560" x2="580" y2="640" stroke="#5b3c25" stroke-width="16"/><ellipse cx="580" cy="645" rx="70" ry="14" fill="#5b3c25"/><circle cx="580" cy="460" r="100" fill="#2f5a6a"/><path d="M520 420 q30 -40 70 -10 q20 40 -20 60 q-40 10 -50 -50z M600 480 q30 -10 40 30 q-30 30 -50 0z" fill="#8a7a4a"/><circle cx="580" cy="460" r="108" fill="none" stroke="#c9a24a" stroke-width="8"/>${F.globeOpen ? '<rect x="550" y="540" width="60" height="22" fill="#140d08"/>' : ''}${label(580, 340, 'Globe')}`, act: () => openGlobe() },
      { id: 'gramophone', x: 720, y: 330, w: 260, h: 330, art: () => `<rect x="740" y="520" width="220" height="120" fill="#5b3c25"/><ellipse cx="850" cy="520" rx="100" ry="18" fill="#1d140c"/><path d="M870 510 L930 400 Q990 330 960 470 Z" fill="#c9a24a"/><line x1="900" y1="505" x2="880" y2="460" stroke="#888" stroke-width="5"/>${label(850, 680, 'Gramophone')}`,
        act: () => F.needle ? playRecord() : say('A gramophone with a record already on the platter. The tone arm has no needle.'),
        use: { needle: () => { F.needle = 1; take('needle'); playRecord(); return true; } } },
      { id: 'safe', x: 1010, y: 120, w: 260, h: 300, art: () => `<rect x="1020" y="130" width="240" height="280" fill="${F.safeOpen ? '#2a2a2a' : '#4a4a48'}" stroke="#222" stroke-width="10" rx="6"/>${F.safeOpen ? '<rect x="1040" y="150" width="200" height="240" fill="#111"/>' : '<circle cx="1140" cy="260" r="50" fill="#6a6a66"/><circle cx="1140" cy="260" r="10" fill="#222"/><rect x="1210" y="240" width="20" height="40" fill="#333"/>'}${label(1140, 115, 'Wall safe')}`, act: () => F.safeOpen ? say('The safe is empty now.') : openSafe() },
      { id: 'chest', x: 1010, y: 520, w: 280, h: 160, art: () => `<rect x="1020" y="560" width="260" height="110" fill="#5a3a22" stroke="#2a1a10" stroke-width="6"/><path d="M1020 560 q130 -60 260 0" fill="#6b4528" stroke="#2a1a10" stroke-width="6"/><rect x="1135" y="575" width="30" height="36" fill="#c9a24a"/>${label(1150, 700, 'Chest')}`,
        act: () => { say('A heavy padlock. A brass tag: “Property of H. Krag”. The landlord’s chest – not Elias’s riddle.'); note('chest', 'The locked chest belongs to the landlord, H. Krag. Not part of Elias’s trail.'); } },
      { id: 'toTower', x: 1330, y: 160, w: 210, h: 490, art: () => door(1340, 180, 190, 460, F.towerOpen, F.towerOpen ? 'Up to the tower →' : 'Narrow door'),
        act: () => F.towerOpen ? go('tower') : say('A narrow door. Behind it you can hear the slow tick of something enormous. Locked.'),
        use: { towerKey: () => { F.towerOpen = 1; take('towerKey'); say('The long key fits. Stairs spiral up into the dark – and the ticking grows louder.'); return true; } } },
    ],
  },
  tower: {
    name: 'The clock tower',
    bg: () => `<rect width="1600" height="900" fill="#14161c"/><circle cx="800" cy="380" r="330" fill="#d9cfb2" opacity=".14"/><circle cx="800" cy="380" r="300" fill="none" stroke="#5a5040" stroke-width="10"/>
      ${Array.from({ length: 12 }, (_, i) => { const a = i * Math.PI / 6; return `<rect x="790" y="95" width="20" height="44" fill="#5a5040" transform="rotate(${i * 30} 800 380)"/>`; }).join('')}
      <rect y="720" width="1600" height="180" fill="#0d0e12"/>${Array.from({ length: 8 }, (_, i) => `<rect x="${i * 210}" y="0" width="14" height="720" fill="#20232b"/>`).join('')}`,
    spots: [
      { id: 'down', x: 20, y: 760, w: 260, h: 110, art: () => `<text x="40" y="830" class="lbl big">← Down to study</text>`, act: () => go('study') },
      { id: 'hook', x: 160, y: 120, w: 220, h: 560, art: () => `<line x1="270" y1="120" x2="270" y2="${F.weightHung ? 560 : 300}" stroke="#8a7a5a" stroke-width="6"/>${F.weightHung ? '<circle cx="270" cy="600" r="50" fill="#c9a24a"/>' : '<path d="M262 300 q8 24 16 0" fill="none" stroke="#8a7a5a" stroke-width="6"/>'}${label(270, 110, F.weightHung ? 'Pendulum' : 'Empty pendulum rod')}`,
        act: () => say(F.weightHung ? 'The pendulum swings, slow and heavy. Tick… tock…' : 'The pendulum rod ends in an empty hook. Without a weight, nothing in the tower can move.'),
        use: { weight: () => { F.weightHung = 1; take('weight'); say('You hang the brass weight. The pendulum begins to swing – but the gear train beside it is missing its wheels.'); return true; } } },
      { id: 'gears', x: 560, y: 470, w: 480, h: 220, art: () => `<rect x="570" y="480" width="460" height="200" fill="#2a2620" stroke="#4a4030" stroke-width="6"/>${['A', 'B', 'C'].map((p, i) => `<circle cx="${660 + i * 140}" cy="580" r="${F.gearsDone ? [44, 28, 60][i] : 8}" fill="${F.gearsDone ? '#c9a24a' : '#8a7a5a'}"/><text x="${660 + i * 140}" y="670" fill="#bba" font-size="26" text-anchor="middle">${p}</text>`).join('')}${label(800, 465, 'Gear train')}`,
        act: () => F.weightHung ? openGears() : say('Three empty pegs, A, B and C, and a box of loose brass wheels. Nothing will turn until the pendulum has its weight.') },
      { id: 'face', x: 600, y: 90, w: 400, h: 340, art: () => `${clock(800, 260, 150, F.hands ? F.hands[0] : 12, F.hands ? F.hands[1] : 0, '#5a5040', '#cfc4a4')}${label(800, 80, 'Clock mechanism')}`,
        act: () => F.gearsDone ? openHands() : say('The hands of the great clock are coupled to the gear train. Nothing moves yet.') },
      { id: 'heart', x: 1180, y: 300, w: 300, h: 380, art: () => `<rect x="1200" y="320" width="260" height="340" fill="#3b2a1d" stroke="#c9a24a" stroke-width="${F.won ? 10 : 4}"/><path d="M1330 430 c-40 -50 -100 0 -60 50 l60 60 l60 -60 c40 -50 -20 -100 -60 -50z" fill="${F.won ? '#c9372b' : '#5a2a22'}"/>${label(1330, 300, 'Brass door')}`,
        act: () => F.won ? win() : say('A small brass door with a heart engraved on it. No keyhole – only a tiny dial that turns with the great clock.') },
    ],
  },
};

/* ---------------- shell ---------------- */
root.innerHTML = `
<header class="bar"><a class="logo" href="/escape/${SLUG}">Six Clues</a><span id="room"></span><span id="timer" class="timer">60:00</span>
  <span class="btns"><button id="hint">💡 Hint</button><button id="nb">📓 Notebook</button><button id="pause" aria-label="Pause">⏸ Pause</button></span></header>
<div class="stage-wrap"><svg id="stage" viewBox="0 0 1600 900" role="img" aria-label="Escape room scene"></svg></div>
<footer class="dock"><p id="msg" role="status" aria-live="polite"></p><div id="inv" class="inv"></div></footer>
<div id="modal" class="modal" hidden><div class="sheet"><button class="x" aria-label="Close">✕</button><div id="mbody"></div></div></div>
<div id="cover" class="cover" hidden></div>`;
const $ = id => document.getElementById(id);
const say = t => { $('msg').textContent = t; };
const flashBtn = id => { const b = $(id); b.classList.remove('ping'); void b.offsetWidth; b.classList.add('ping'); };
const imgOk = {};
['workshop', 'study', 'tower'].forEach(r => { const im = new Image(); im.onload = () => { imgOk[r] = true; if (S.room === r) render(); }; im.src = IMG + r + '.jpg'; });

function render() {
  const R = ROOMS[S.room];
  $('room').textContent = R.name;
  const art = imgOk[S.room] ? `<image href="${IMG + S.room}.jpg" width="1600" height="900"/>` : R.bg();
  $('stage').innerHTML = `<defs><radialGradient id="lamp"><stop offset="0" stop-color="#ffcf7a" stop-opacity=".22"/><stop offset="1" stop-color="#ffcf7a" stop-opacity="0"/></radialGradient></defs>${art}` +
    R.spots.map(s => `<g class="hs${imgOk[S.room] ? ' photo' : ''}" data-id="${s.id}" tabindex="0" role="button" aria-label="${s.id}">${imgOk[S.room] ? '' : s.art()}<rect class="hit" x="${s.x}" y="${s.y}" width="${s.w}" height="${s.h}" rx="10"/></g>`).join('');
  $('stage').querySelectorAll('.hs').forEach(g => {
    const fire = () => clickSpot(R.spots.find(s => s.id === g.dataset.id));
    g.addEventListener('click', fire); g.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); fire(); } });
  });
}
function clickSpot(s) {
  if (!S.started || paused) return;
  if (sel) {
    const fn = s.use && s.use[sel];
    if (!(fn && fn())) say(`The ${ITEMS[sel][1].toLowerCase()} doesn’t do anything there.`);
    sel = null; renderInv(); render(); save(); check(); return;
  }
  s.act(); render(); dirty = true;
}
function renderInv() {
  $('inv').innerHTML = S.inv.map(i => `<button class="item${sel === i ? ' on' : ''}" data-i="${i}" title="${ITEMS[i][1]}"><span>${ITEMS[i][0]}</span><small>${ITEMS[i][1]}</small></button>`).join('') || '<p class="empty">Your pockets are empty.</p>';
  $('inv').querySelectorAll('.item').forEach(b => b.addEventListener('click', () => {
    const i = b.dataset.i;
    if (sel && sel !== i) { combine(sel, i); return; }
    sel = sel === i ? null : i;
    if (sel) say(`${ITEMS[i][2]} – Tap where to use it, or another item to combine.`);
    renderInv();
  }));
}
function combine(a, b) {
  const pair = [a, b].sort().join('+');
  if (pair === 'photoL+photoR') { take('photoL'); take('photoR'); give('photo'); sel = null; say('The torn edges match. ' + ITEMS.photo[2]); note('photo', 'Photograph: “Bergen · 4:20 pm · 1902 – the day I learned to listen.”'); }
  else if (pair === 'loupe+photoL' || pair === 'loupe+photoR') { say('Under the loupe the pencil is clearer, but half a word is still half a word.'); sel = null; }
  else { say('Those two don’t go together.'); sel = null; }
  renderInv(); save();
}
function go(r) { S.room = r; sel = null; render(); renderInv(); say(ROOMS[r].name + '.'); save(); }

/* ---------------- modal close-ups ---------------- */
function modal(html, onReady) { $('mbody').innerHTML = html; $('modal').hidden = false; onReady && onReady($('mbody')); }
function closeModal() { $('modal').hidden = true; render(); }
$('modal').querySelector('.x').addEventListener('click', closeModal);
$('modal').addEventListener('click', e => { if (e.target === $('modal')) closeModal(); });

function wheels(n, onTry, startVals) {
  const v = startVals || Array(n).fill(0);
  return { html: `<div class="wheels">${v.map((_, i) => `<div class="wheel"><button data-w="${i}" data-d="1">▲</button><b id="w${i}">0</b><button data-w="${i}" data-d="-1">▼</button></div>`).join('')}</div><button class="btn" id="try">Try the lock</button><p id="wres" class="res"></p>`,
    bind: m => { const draw = () => v.forEach((x, i) => { m.querySelector('#w' + i).textContent = x; });
      m.querySelectorAll('[data-w]').forEach(b => b.addEventListener('click', () => { const i = +b.dataset.w; v[i] = (v[i] + +b.dataset.d + 10) % 10; draw(); }));
      m.querySelector('#try').addEventListener('click', () => { if (!onTry(v.join(''))) { const r = m.querySelector('#wres'); r.textContent = 'Clunk. It doesn’t open.'; r.classList.remove('shake'); void r.offsetWidth; r.classList.add('shake'); } }); draw(); } };
}
function openClockWall() {
  note('rainbow', 'Note pinned under the clocks: “The hours count, the minutes don’t. Read them as the rainbow does.”');
  note('clocks', 'Clock wall (left to right, top to bottom): red rim 7:05 · blue rim 1:10 · green rim 9:15 · yellow rim 3:20 · plain clock 12:00');
  modal(`<h2>The clock wall</h2><svg viewBox="0 0 900 420" class="close">${clock(130, 140, 95, 7, 5, '#a3322b')}${clock(450, 140, 95, 1, 10, '#2e5a9a')}${clock(770, 140, 95, 9, 15, '#3f7a3a')}${clock(290, 320, 85, 3, 20, '#c8a02a')}${clock(610, 320, 85, 12, 0, '#6b5a48')}</svg>
    <p class="paper">The hours count, the minutes don’t.<br>Read them as the rainbow does.<br><i>– E.B.</i></p><p class="small">Five stopped clocks hang in a row: red, blue, green and yellow rims – and one plain clock with no colour at all.</p>`);
}
function openBench() {
  const plate = F.plateRead ? '<p class="paper">E. BRANDT &amp; SØN · EST. 1847</p>' : '<p>A small brass maker’s plate, engraved in letters far too tiny to read with the naked eye.</p>';
  if (F.drawerOpen) {
    modal(`<h2>The workbench</h2><p>The drawer stands open and empty.</p><h3>Brass plate</h3>${plate}<button class="btn" id="useLoupe"${has('loupe') && !F.plateRead ? '' : ' hidden'}>Use the loupe on the plate</button><h3>Letter</h3><button class="btn ghost" id="letter">Read the letter</button>`, bindBench);
    return;
  }
  const w = wheels(4, code => { if (code !== '7391') return false; F.drawerOpen = 1; give('loupe'); give('photoL'); note('drawer', 'Drawer opened with 7391.'); closeModal(); say('Click-click-click-CLACK. Inside the drawer: a watchmaker’s loupe and the left half of a torn photograph.'); save(); check(); return true; });
  modal(`<h2>The workbench</h2><h3>Drawer</h3><p>The drawer is held by a lock with four number wheels.</p>${w.html}<h3>Brass plate</h3>${plate}<button class="btn" id="useLoupe"${has('loupe') && !F.plateRead ? '' : ' hidden'}>Use the loupe on the plate</button><h3>Letter</h3><button class="btn ghost" id="letter">Read the letter</button>`, m => { w.bind(m); bindBench(m); });
}
function bindBench(m) {
  m.querySelector('#letter').addEventListener('click', () => { note('letter', 'Eviction letter from landlord H. Krag: the workshop will be sealed at midnight, 31 Dec 1931, “together with all contents”.'); m.querySelector('#letter').outerHTML = '<p class="paper">Hr. Brandt’s estate – NOTICE. The premises at Store Kongensgade 14, attic, will be sealed at midnight 31 December 1931, together with all contents. <i>– H. Krag, landlord</i></p>'; });
  const u = m.querySelector('#useLoupe'); u && u.addEventListener('click', () => { F.plateRead = 1; note('plate', 'Brass plate (read with the loupe): “E. Brandt & Søn · est. 1847”'); closeModal(); say('Through the loupe the letters swim into focus: E. BRANDT & SØN · EST. 1847.'); save(); check(); });
}
function openShelf() {
  const books = [['A Brief Hour', 'brief'], ['The Mechanics of Escapement', 'x1'], ['Nordic Harbours', 'x2'], ['Ledger 1929–1931', 'x3'], ['Grimm’s Tales', 'x4']];
  modal(`<h2>The bookshelf</h2><p>Most of the books are about clocks. A few spines catch your eye.</p><div class="books">${books.map(([t, k]) => `<button class="book" data-k="${k}">${t}</button>`).join('')}</div><p id="bres" class="res"></p>`, m => {
    m.querySelectorAll('.book').forEach(b => b.addEventListener('click', () => {
      const r = m.querySelector('#bres'), k = b.dataset.k;
      if (k === 'brief') {
        if (F.book) { r.textContent = 'The hollow in “A Brief Hour” is empty now.'; return; }
        F.book = 1; give('photoR'); note('book', 'Inside “A Brief Hour”: the right half of a torn photograph.'); r.textContent = 'The pages have been hollowed out. Inside: the right half of a torn photograph.'; save(); check();
      } else r.textContent = { x1: 'Dense diagrams, Elias’s notes in the margins. Nothing hidden.', x2: 'Picture plates of Norwegian ports. A pressed flower falls out – nothing else.', x3: 'Columns of debts, each line crossed out in red. Elias paid them all.', x4: 'A child’s book. “For Anna” on the flyleaf.' }[k];
    }));
  });
}
const CITIES = ['Copenhagen', 'Stockholm', 'Oslo', 'Hamburg', 'Bergen', 'London', 'Paris', 'Vienna', 'Prague', 'Geneva', 'Amsterdam', 'Riga'];
function openGlobe() {
  if (F.globeOpen) { modal('<h2>The globe</h2><p>The small compartment under the globe is open and empty.</p>'); return; }
  let i = 0;
  modal(`<h2>The globe</h2><p>A brass dial on the stand turns through city names. A tiny compartment sits under it.</p><div class="dial"><button id="dl">◀</button><b id="city"></b><button id="dr">▶</button></div><button class="btn" id="set">Set the dial</button><p id="gres" class="res"></p>`, m => {
    const draw = () => { m.querySelector('#city').textContent = CITIES[i]; };
    m.querySelector('#dl').addEventListener('click', () => { i = (i + CITIES.length - 1) % CITIES.length; draw(); });
    m.querySelector('#dr').addEventListener('click', () => { i = (i + 1) % CITIES.length; draw(); });
    m.querySelector('#set').addEventListener('click', () => {
      if (CITIES[i] !== 'Bergen') { m.querySelector('#gres').textContent = 'The dial clicks back to where it started.'; return; }
      F.globeOpen = 1; give('needle'); closeModal(); say('With a soft whirr the compartment slides open. Inside: a gramophone needle in an envelope – “for the last record”.'); save(); check();
    }); draw();
  });
}
function playRecord() {
  F.heard = 1;
  const text = '“If you hear this, my friend, I am gone and Krag is at the door. Don’t let him have it. Everything I loved is in the heart of this house. The safe remembers the year the house first ticked. And when you reach the top… set the time the way I set it on my best day. – Elias”';
  note('record', 'Elias on the record: “The safe remembers the year the house first ticked.” … “At the top, set the time the way I set it on my best day.”');
  modal(`<h2>The last record</h2><p class="small">The needle drops. Crackle… then an old man’s voice.</p><p class="paper voice">${text}</p>`);
  try { const a = new Audio(AUDIO + 'record.mp3'); a.play().catch(() => {}); } catch (e) {}
  save(); check();
}
function openSafe() {
  const w = wheels(4, code => { if (code !== '1847') return false; F.safeOpen = 1; give('weight'); give('sketch'); give('towerKey'); note('sketch', 'Gear sketch from the safe: peg A – middle-sized wheel, peg B – small wheel, peg C – large wheel.'); closeModal(); say('The bolts draw back with a heavy clunk. Inside: a brass pendulum weight, a folded gear sketch and a long key.'); save(); check(); return true; });
  modal(`<h2>The wall safe</h2><p>Four numbered wheels and a heavy handle.</p>${w.html}`, w.bind);
}
function openGears() {
  if (F.gearsDone) { modal('<h2>Gear train</h2><p>The wheels mesh perfectly and turn with the pendulum.</p>'); return; }
  const place = { A: null, B: null, C: null }; let pick = null; const G = { small: 'Small wheel', medium: 'Middle wheel', large: 'Large wheel' };
  modal(`<h2>The gear train</h2><p>Three pegs, three loose wheels. Pick a wheel, then a peg.</p><div class="gearbox" id="gb"></div><div class="pegs" id="pg"></div><button class="btn" id="spin">Release the pendulum</button><p id="ores" class="res"></p>`, m => {
    const draw = () => {
      m.querySelector('#gb').innerHTML = Object.keys(G).filter(g => !Object.values(place).includes(g)).map(g => `<button class="gear${pick === g ? ' on' : ''}" data-g="${g}"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="${{ small: 20, medium: 32, large: 44 }[g]}" fill="#c9a24a" stroke="#6a5020" stroke-width="5" stroke-dasharray="6 4"/></svg>${G[g]}</button>`).join('');
      m.querySelector('#pg').innerHTML = Object.keys(place).map(p => `<button class="peg" data-p="${p}"><b>${p}</b>${place[p] ? G[place[p]] : '—'}</button>`).join('');
      m.querySelectorAll('.gear').forEach(b => b.addEventListener('click', () => { pick = b.dataset.g; draw(); }));
      m.querySelectorAll('.peg').forEach(b => b.addEventListener('click', () => { const p = b.dataset.p; if (pick) { place[p] = pick; pick = null; } else place[p] = null; draw(); }));
    };
    m.querySelector('#spin').addEventListener('click', () => {
      if (place.A === 'medium' && place.B === 'small' && place.C === 'large') { F.gearsDone = 1; F.hands = [12, 0]; closeModal(); say('The pendulum swings, the wheels bite – and with a groan the great clock hands come free.'); save(); check(); }
      else m.querySelector('#ores').textContent = 'The wheels grind and jam. The pendulum stops.';
    }); draw();
  });
}
function openHands() {
  if (F.won) return win();
  const h = F.hands || [12, 0];
  modal(`<h2>The great clock</h2><p>The hands are free. Set the time.</p><svg viewBox="0 0 300 300" class="close small" id="hc"></svg><div class="dial"><span>Hour</span><button id="hm">◀</button><b id="hv"></b><button id="hp">▶</button></div><div class="dial"><span>Minutes</span><button id="mm">◀</button><b id="mv"></b><button id="mp">▶</button></div><button class="btn" id="setc">Let the clock run</button><p id="hres" class="res"></p>`, m => {
    const draw = () => { m.querySelector('#hc').innerHTML = clock(150, 150, 140, h[0], h[1], '#5a5040', '#cfc4a4'); m.querySelector('#hv').textContent = h[0]; m.querySelector('#mv').textContent = String(h[1]).padStart(2, '0'); };
    m.querySelector('#hm').addEventListener('click', () => { h[0] = h[0] === 1 ? 12 : h[0] - 1; draw(); });
    m.querySelector('#hp').addEventListener('click', () => { h[0] = h[0] === 12 ? 1 : h[0] + 1; draw(); });
    m.querySelector('#mm').addEventListener('click', () => { h[1] = (h[1] + 55) % 60; draw(); });
    m.querySelector('#mp').addEventListener('click', () => { h[1] = (h[1] + 5) % 60; draw(); });
    m.querySelector('#setc').addEventListener('click', () => {
      F.hands = h.slice(); dirty = true;
      if (h[0] === 4 && h[1] === 20) { F.won = 1; closeModal(); say('The tower shudders. Somewhere deep in the mechanism a bolt slides back… and the little brass heart door swings open.'); save(); setTimeout(win, 1600); }
      else m.querySelector('#hres').textContent = 'The clock ticks on. Nothing else happens.';
    }); draw();
  });
}

/* ---------------- hints ---------------- */
const STAGES = [
  ['drawer', () => F.drawerOpen, ['The drawer wants four digits. What in the workshop shows numbers?', 'Each coloured clock gives one digit – its hour. The note under the clocks tells you the order.', 'Rainbow order is red, yellow, green, blue: 7 – 3 – 9 – 1. The drawer code is 7391.']],
  ['study', () => F.studyOpen, ['The study door needs a key. Something in the workshop rattles.', 'Elias’s coat holds a tool. The cuckoo clock has screws in its back.', 'Take the screwdriver from the coat, use it on the cuckoo clock, then use the small key on the study door.']],
  ['photo', () => F.book && has('photo') || F.globeOpen, ['Half a photograph is only half an answer. Where could the other half be?', 'Books can hide more than words. One title is about time.', 'Open “A Brief Hour” on the bookshelf, then combine the two photo halves in your inventory.']],
  ['globe', () => F.globeOpen, ['The photograph names a place.', 'The globe has a city dial.', 'Turn the globe’s dial to Bergen.']],
  ['record', () => F.heard, ['You found a needle. What in the study plays with a needle?', 'The gramophone already has a record on it.', 'Use the needle on the gramophone and listen.']],
  ['safe', () => F.safeOpen, ['Elias said the safe remembers the year the house first ticked. When was the firm founded?', 'Something in the workshop is engraved, but the letters are tiny. You have a loupe.', 'Use the loupe on the brass plate on the workbench: “est. 1847”. The safe code is 1847.']],
  ['tower', () => F.towerOpen, ['Not everything from the safe is for the study.', 'One of the things in the safe is a key.', 'Use the long tower key on the narrow door in the study.']],
  ['weight', () => F.weightHung, ['Nothing up here moves. What does a clock need to run?', 'The pendulum rod has an empty hook.', 'Use the brass pendulum weight on the pendulum rod.']],
  ['gears', () => F.gearsDone, ['The gear train needs three wheels. You have a drawing.', 'Read the gear sketch from the safe in your notebook.', 'Peg A: middle wheel, peg B: small wheel, peg C: large wheel.']],
  ['hands', () => F.won, ['Elias asked you to set the time from his best day.', 'His best day is on the back of the photograph.', 'Set the great clock to 4:20.']],
];
function stage() { return STAGES.find(s => !s[1]()); }
$('hint').addEventListener('click', () => {
  if (!S.started || paused) return;
  const st = stage(); if (!st) return;
  const n = S.hints[st[0]] || 0;
  const shown = st[2].slice(0, n).map((t, i) => `<li>${t}</li>`).join('');
  const cost = n >= 2 ? 5 : 3;
  modal(`<h2>Hints</h2>${shown ? `<ol class="hints">${shown}</ol>` : '<p>Stuck? Hints come in three steps: a nudge, a clearer pointer, then the answer.</p>'}
    ${n < 3 ? `<button class="btn" id="more">${n === 2 ? 'Show the answer' : n ? 'A clearer hint' : 'Give me a nudge'} (+${cost} min)</button>` : '<p class="small">That’s everything for this step.</p>'}`, m => {
    const b = m.querySelector('#more'); b && b.addEventListener('click', () => { S.hints[st[0]] = n + 1; S.penalty += cost * 60000; S.hintCount++; save(); tick(); $('hint').click(); });
  });
});

/* ---------------- notebook ---------------- */
$('nb').addEventListener('click', () => {
  modal(`<h2>Notebook</h2>${S.notes.length ? `<ul class="notes">${S.notes.map(n => `<li>${n.text}</li>`).join('')}</ul>` : '<p>Nothing written down yet. Everything you read goes in here.</p>'}<hr><p class="small">Items: tap one to select it and read about it; tap a second item to combine; tap something in the room to use it there.</p><button class="btn ghost" id="restart">Restart from the beginning</button>`, m => {
    m.querySelector('#restart').addEventListener('click', () => { if (m.querySelector('#restart').dataset.sure) { post('restart').then(() => { S = fresh(); location.reload(); }); } else { m.querySelector('#restart').dataset.sure = 1; m.querySelector('#restart').textContent = 'Sure? Tap again to wipe your progress'; } });
  });
});

/* ---------------- timer, pause, save ---------------- */
const left = () => LIMIT - S.elapsed - S.penalty;
const fmt = ms => { const s = Math.max(0, Math.ceil(Math.abs(ms) / 1000)); return (ms < 0 ? '+' : '') + Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0'); };
function tick() {
  const now = performance.now();
  if (S.started && !paused && !finished) { S.elapsed += now - last; dirty = true; }
  last = now;
  const l = left(); $('timer').textContent = fmt(l); $('timer').classList.toggle('low', l < 300000);
  if (l <= 0 && !S.over && !finished) { S.over = true; save(); timesUp(); }
}
setInterval(tick, 250);
function setPause(p) {
  if (!S.started || finished) return;
  paused = p; tick();
  const c = $('cover');
  if (p) { c.innerHTML = `<div class="pausebox"><h2>Paused</h2><p>The clock has stopped. The room is hidden until you come back.</p><p class="big">${fmt(left())}</p><button class="btn btn-big" id="resume">Resume</button></div>`; c.hidden = false; c.querySelector('#resume').addEventListener('click', () => setPause(false)); save(); }
  else c.hidden = true;
}
$('pause').addEventListener('click', () => setPause(true));
document.addEventListener('visibilitychange', () => { if (document.hidden) setPause(true); });
document.addEventListener('keydown', e => { if (e.key === 'Escape') { if (!$('modal').hidden) closeModal(); } if (e.key === 'p' && $('modal').hidden) setPause(!paused); });

function post(action, extra = {}) {
  return fetch(location.pathname, { method: 'POST', headers: { 'Content-Type': 'application/json' }, keepalive: true, body: JSON.stringify(Object.assign({ csrf: CSRF, do: action, state: S }, extra)) }).catch(() => {});
}
function save() { if (S.started) { dirty = false; post('save'); } }
setInterval(() => { if (dirty && S.started && !finished) save(); }, 15000);
window.addEventListener('pagehide', () => { if (S.started && !finished) save(); });

function check() { renderInv(); }
function timesUp() {
  const c = $('cover');
  c.innerHTML = `<div class="pausebox"><h2>Midnight.</h2><p>The great clock strikes twelve. Downstairs, a key scrapes in the lock – Krag is coming with the bailiff.</p><p>You can keep playing to find the heart of the house, but your time won’t go on the leaderboard.</p><button class="btn btn-big" id="cont">Keep going</button> <button class="btn ghost" id="again">Start over</button></div>`;
  c.hidden = false;
  c.querySelector('#cont').addEventListener('click', () => { c.hidden = true; });
  c.querySelector('#again').addEventListener('click', () => post('restart').then(() => location.reload()));
}
function win() {
  if (finished) return;
  finished = true; tick();
  const t = S.elapsed + S.penalty;
  post('finish', { time_ms: Math.round(t), hints: S.hintCount, overtime: S.over });
  const c = $('cover');
  c.innerHTML = `<div class="pausebox win"><p class="kicker">The heart of the house</p><h2>You escaped, ${NAME}!</h2>
    <p>Behind the brass door: Elias’s gold pocket watch, still ticking – and the deed to the workshop, signed over to you. Krag can knock all he wants.</p>
    <p class="big">${S.over ? 'Overtime' : fmt(t) + ' used'}</p><p>${S.hintCount ? S.hintCount + ' hint' + (S.hintCount > 1 ? 's' : '') + ' (time added)' : 'No hints – impressive.'}</p>
    <p><a class="btn btn-big" href="/escape/${SLUG}">See the leaderboard</a></p><p class="small"><a href="/">Back to Six Clues</a></p></div>`;
  c.hidden = false;
}

/* ---------------- intro ---------------- */
function intro() {
  const c = $('cover');
  const resume = S.started;
  c.innerHTML = `<div class="pausebox intro"><p class="kicker">Copenhagen · 31 December 1931 · 11 pm</p><h2>The Clockmaker’s Last Hour</h2>
    ${resume ? `<p>Welcome back. The clock stopped at <b>${fmt(left())}</b> when you left.</p>` : `<p>Master clockmaker Elias Brandt is dead, and his will leaves you – his apprentice – “the heart of the house”. Nobody knows what that means.</p>
    <p>The landlord, Krag, has let you into the attic workshop for one hour. At midnight the bailiff seals it, contents and all. Then he locked the door behind you.</p>
    <p>Search the rooms, collect what you find and crack Elias’s locks before the great clock strikes twelve.</p>`}
    <button class="btn btn-big" id="go">${resume ? 'Resume' : 'Start the clock'}</button><p class="small">Pause any time with ⏸ – the room is hidden and the clock stops.</p></div>`;
  c.hidden = false;
  c.querySelector('#go').addEventListener('click', () => { S.started = true; last = performance.now(); c.hidden = true; say(resume ? ROOMS[S.room].name + '.' : 'The door clicks shut behind you. Somewhere above, something enormous ticks. Look around.'); save(); });
}

render(); renderInv(); tick(); intro();
if (S.over) say('Midnight has passed – you can still finish, but off the leaderboard.');
})();
