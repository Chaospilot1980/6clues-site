/* Six Clues escape room #3 – The Lighthouse at Gull Rock (prototype, level 2).
 * Scenes are SVG placeholders. Drop real art in /assets/img/escape/the-lighthouse-at-gull-rock/<room>.jpg (1600x900) – picked up automatically. */
(() => {
'use strict';
const root = document.getElementById('escape');
const SLUG = root.dataset.slug, CSRF = root.dataset.csrf, NAME = root.dataset.name || 'Detective';
const LIMIT = 3600000, IMG = '/assets/img/escape/' + SLUG + '/', AUDIO = '/assets/audio/escape/' + SLUG + '/';
const fresh = () => ({ v: 1, room: 'cottage', inv: [], flags: {}, notes: [], elapsed: 0, penalty: 0, hints: {}, hintCount: 0, started: false, over: false });
let S = Object.assign(fresh(), window.ESCAPE_STATE || {});
let sel = null, paused = false, dirty = false, last = performance.now(), finished = false;

/* ---------------- items ---------------- */
const ITEMS = {
  note: ['📝', 'Abel’s note', 'From the keeper’s oilskin: “Oil store opens at high water. – A.P.”'],
  letter: ['✉️', 'Shipping letter', 'Trinity House notice: the SS Marigold, official no. 4127, passes Gull Rock tonight about 02:00.'],
  realLog: ['📘', 'Real logbook', 'Abel’s true log, hidden behind the oil drums. The last page has a lens diagram.'],
  towerKey: ['🗝️', 'Tower key', 'A heavy iron key from inside the barometer case.'],
  oil: ['🛢️', 'Can of paraffin', 'A full can of lamp oil from the oil store.'],
  mantle: ['🕯️', 'Spare mantle', 'A new incandescent mantle in its box, from the radio hut drawer.'],
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
const stormWin = (x, y, w, h) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="#0c1622" stroke="#4a3a2a" stroke-width="12"/>${Array.from({ length: 18 }, (_, i) => `<line x1="${x + 10 + (i * 41) % (w - 20)}" y1="${y + 10 + (i * 29) % (h - 40)}" x2="${x + 2 + (i * 41) % (w - 20)}" y2="${y + 40 + (i * 29) % (h - 40)}" stroke="#9fb4c8" stroke-width="2" opacity=".6"/>`).join('')}<path d="M${x} ${y + h * .75} q${w * .25} -30 ${w * .5} 0 t${w * .5} 0 V${y + h} H${x}z" fill="#13202e"/>`;
const FLAGS = { G: '<rect width="60" height="40" fill="#e8c21a"/><rect x="10" width="10" height="40" fill="#1f4aa0"/><rect x="30" width="10" height="40" fill="#1f4aa0"/><rect x="50" width="10" height="40" fill="#1f4aa0"/>', U: '<rect width="60" height="40" fill="#fff"/><rect width="30" height="20" fill="#c4232b"/><rect x="30" y="20" width="30" height="20" fill="#c4232b"/>', L: '<rect width="60" height="40" fill="#e8c21a"/><rect x="30" width="30" height="20" fill="#111"/><rect y="20" width="30" height="20" fill="#111"/>', T: '<rect width="20" height="40" fill="#c4232b"/><rect x="20" width="20" height="40" fill="#fff"/><rect x="40" width="20" height="40" fill="#1f4aa0"/>', I: '<rect width="60" height="40" fill="#e8c21a"/><circle cx="30" cy="20" r="11" fill="#111"/>', D: '<rect width="60" height="40" fill="#1f4aa0"/><rect y="12" width="60" height="16" fill="#e8c21a"/>', E: '<rect width="60" height="20" fill="#1f4aa0"/><rect y="20" width="60" height="20" fill="#c4232b"/>', S: '<rect width="60" height="40" fill="#fff"/><rect x="18" y="10" width="24" height="20" fill="#1f4aa0"/>' };
const flag = (k, x = 0, y = 0, s = 1) => `<g transform="translate(${x} ${y}) scale(${s})"><rect x="-2" y="-2" width="64" height="44" fill="#333"/>${FLAGS[k]}</g>`;
const ROOMS = {
  cottage: {
    name: 'The keeper’s cottage',
    bg: () => `<rect width="1600" height="900" fill="#2c2620"/>${Array.from({ length: 8 }, (_, i) => `<rect x="0" y="${i * 82}" width="1600" height="78" fill="${i % 2 ? '#302922' : '#2a241e'}"/>`).join('')}<rect y="660" width="1600" height="240" fill="#1e1914"/>${stormWin(640, 80, 320, 240)}<ellipse cx="800" cy="0" rx="560" ry="360" fill="url(#lamp)"/>`,
    spots: [
      { id: 'oilskin', x: 40, y: 140, w: 180, h: 420, art: () => `<circle cx="130" cy="150" r="9" fill="#c9a24a"/><path d="M130 155 L80 210 L70 530 L190 530 L180 210 Z" fill="#c9a23a"/>${label(130, 570, 'Oilskin coat')}`,
        act: () => { if (F.coat) return say('Salt-stiff pockets, empty now.'); F.coat = 1; give('note'); note('note', 'Abel’s note (oilskin pocket): “Oil store opens at high water. – A.P.”'); say('In the oilskin’s pocket: a scrap of paper in the keeper’s hand.'); } },
      { id: 'tides', x: 250, y: 110, w: 260, h: 300, art: () => `<rect x="260" y="120" width="240" height="280" fill="#e9dcb8" stroke="#4a3a2a" stroke-width="8"/>${Array.from({ length: 8 }, (_, i) => `<line x1="280" y1="${160 + i * 28}" x2="480" y2="${160 + i * 28}" stroke="#8a7a5a" stroke-width="3"/>`).join('')}${label(380, 440, 'Tide table')}`, act: () => openTides() },
      { id: 'desk', x: 560, y: 420, w: 480, h: 240, art: () => `<rect x="560" y="470" width="480" height="40" fill="#5b3c25"/><rect x="580" y="510" width="440" height="140" fill="#4a3020"/><rect x="620" y="440" width="140" height="34" fill="#2a3a5a"/><rect x="800" y="446" width="110" height="26" fill="#e9dcb8" transform="rotate(5 855 459)"/><rect x="940" y="430" width="60" height="44" fill="#a33" opacity=".7"/>${label(800, 690, 'Desk: logbook, letter, child’s drawing')}`, act: () => openDesk() },
      { id: 'barometer', x: 1060, y: 110, w: 150, h: 330, art: () => `<rect x="1100" y="120" width="70" height="300" rx="34" fill="#6b4a2a" stroke="#2a1a10" stroke-width="6"/><circle cx="1135" cy="330" r="30" fill="#efe3c4"/><line x1="1135" y1="330" x2="1115" y2="312" stroke="#222" stroke-width="4"/>${label(1135, 460, 'Barometer')}`,
        act: () => { if (F.towerKey) return say('The barometer reads 968 mb and still falling.'); if (!F.realLog) return say('The barometer reads 968 mb and falling fast. A storm glass sits in its brass case.'); F.towerKey = 1; give('towerKey'); say('You open the barometer case as the true log says: an iron key hangs inside.'); } },
      { id: 'lantern', x: 1230, y: 470, w: 120, h: 190, art: () => `<rect x="1250" y="520" width="80" height="120" rx="10" fill="#3a3a38"/><rect x="1265" y="540" width="50" height="70" fill="#a33" opacity=".8"/>${label(1290, 690, 'Red lantern')}`,
        act: () => { note('lantern', 'A red hand lantern with a shutter, smelling of fresh paraffin – a wrecker’s trick to lure ships? It isn’t Abel’s.'); say('A red lantern with a sliding shutter, recently used. Not lighthouse issue – someone has been signalling from the cliffs.'); } },
      { id: 'toOil', x: 1380, y: 380, w: 200, h: 300, art: () => door(1390, 400, 180, 260, F.oilOpen, F.oilOpen ? 'Oil store →' : 'Oil store (lock)'), act: () => F.oilOpen ? go('oil') : openOilDoor() },
      { id: 'toRadio', x: 20, y: 600, w: 260, h: 260, art: () => `<text x="40" y="830" class="lbl big">${F.radioOpen ? '↓ Radio hut' : '↓ Path to radio hut (padlocked)'}</text>`, act: () => F.radioOpen ? go('radio') : openRadioLock() },
      { id: 'toTower', x: 1240, y: 60, w: 130, h: 330, art: () => door(1245, 80, 120, 290, F.towerOpen, F.towerOpen ? 'Tower ↑' : 'Tower door'),
        act: () => F.towerOpen ? go('lamp') : say('The iron door to the tower stairs is locked. Abel always carried the key.'),
        use: { towerKey: () => { F.towerOpen = 1; take('towerKey'); say('The iron key turns. 117 steps spiral up into the roar of the wind.'); return true; } } },
    ],
  },
  oil: {
    name: 'The oil store',
    bg: () => `<rect width="1600" height="900" fill="#1f1c18"/><rect y="660" width="1600" height="240" fill="#151310"/><ellipse cx="800" cy="0" rx="500" ry="320" fill="url(#lamp)"/>`,
    spots: [
      { id: 'back', x: 20, y: 760, w: 260, h: 110, art: () => `<text x="40" y="830" class="lbl big">← Cottage</text>`, act: () => go('cottage') },
      { id: 'drums', x: 120, y: 330, w: 440, h: 330, art: () => [0, 1, 2].map(i => `<rect x="${140 + i * 140}" y="380" width="120" height="270" rx="10" fill="#4a5a3a" stroke="#222" stroke-width="5"/><line x1="${140 + i * 140}" y1="460" x2="${260 + i * 140}" y2="460" stroke="#222" stroke-width="5"/>`).join('') + label(340, 690, 'Oil drums'),
        act: () => { if (F.realLog) return say('Just drums. You already found what Abel hid here.'); F.realLog = 1; give('realLog'); note('reallog', 'Abel’s TRUE log (hidden behind the drums): “14 Nov – barometer falling, gale by midnight. Treloar’s boat off the point again with no lights. If anything happens to me: spare tower key in the barometer case.” Back page: lens diagram – panel A ↑, B →, C ↓, D ←.'); say('Wedged behind the drums: a second logbook in Abel’s hand – the real one. And a last entry that changes everything.'); } },
      { id: 'tap', x: 640, y: 380, w: 300, h: 280, art: () => `<rect x="660" y="420" width="260" height="170" rx="10" fill="#6b4a2a"/><rect x="760" y="590" width="20" height="60" fill="#888"/><rect x="800" y="560" width="60" height="70" fill="#a33"/>${label(790, 690, 'Paraffin tank & can')}`,
        act: () => { if (has('oil') || F.oiled) return say('The tank drips. You already have what you need.'); give('oil'); say('You fill a can with paraffin from the tank.'); } },
      { id: 'chart', x: 1000, y: 120, w: 420, h: 300, art: () => `<rect x="1010" y="130" width="400" height="270" fill="#e9dcb8" stroke="#4a3a2a" stroke-width="8"/>${Object.keys(FLAGS).map((k, i) => flag(k, 1040 + (i % 4) * 92, 160 + Math.floor(i / 4) * 110, .9)).join('')}${label(1210, 440, 'Signal flag chart')}`, act: () => openChart() },
    ],
  },
  radio: {
    name: 'The radio hut',
    bg: () => `<rect width="1600" height="900" fill="#1a1f22"/><rect y="660" width="1600" height="240" fill="#121518"/>${stormWin(1150, 100, 300, 220)}<ellipse cx="700" cy="0" rx="500" ry="300" fill="url(#lamp)"/>`,
    spots: [
      { id: 'back', x: 20, y: 760, w: 260, h: 110, art: () => `<text x="40" y="830" class="lbl big">← Cottage</text>`, act: () => go('cottage') },
      { id: 'set', x: 300, y: 300, w: 520, h: 360, art: () => `<rect x="320" y="470" width="480" height="30" fill="#5b3c25"/><rect x="360" y="340" width="300" height="130" rx="8" fill="#2a2a2a"/>${[0, 1, 2].map(i => `<circle cx="${410 + i * 90}" cy="405" r="26" fill="#c9a24a"/>`).join('')}<rect x="680" y="440" width="90" height="30" fill="#888"/>${label(560, 690, 'Wireless set & drawer')}`, act: () => openDrawer() },
      { id: 'list', x: 880, y: 140, w: 240, h: 300, art: () => `<rect x="890" y="150" width="220" height="280" fill="#e9dcb8" stroke="#4a3a2a" stroke-width="6"/>${Array.from({ length: 9 }, (_, i) => `<line x1="910" y1="${190 + i * 26}" x2="1090" y2="${190 + i * 26}" stroke="#8a7a5a" stroke-width="3"/>`).join('')}${label(1000, 470, 'Admiralty list of lights')}`, act: () => openLights() },
    ],
  },
  lamp: {
    name: 'The lamp room',
    bg: () => `<rect width="1600" height="900" fill="#0d1218"/>${Array.from({ length: 8 }, (_, i) => `<rect x="${i * 200}" y="0" width="12" height="660" fill="#2a3440"/>`).join('')}<rect y="660" width="1600" height="240" fill="#0a0d11"/><circle cx="800" cy="360" r="${F.lit ? 260 : 120}" fill="${F.lit ? '#ffe9a0' : '#3a4450'}" opacity="${F.lit ? .55 : .5}"/>`,
    spots: [
      { id: 'down', x: 20, y: 760, w: 280, h: 110, art: () => `<text x="40" y="830" class="lbl big">← Down to cottage</text>`, act: () => go('cottage') },
      { id: 'lens', x: 560, y: 120, w: 480, h: 480, art: () => `${['A', 'B', 'C', 'D'].map((p, i) => `<rect x="${600 + (i % 2) * 210}" y="${160 + Math.floor(i / 2) * 210}" width="190" height="190" rx="14" fill="#9fc3d8" opacity=".35" stroke="#c9a24a" stroke-width="5"/><text x="${695 + (i % 2) * 210}" y="${265 + Math.floor(i / 2) * 210}" text-anchor="middle" font-size="60" fill="#e9dcb8">${['↑', '→', '↓', '←'][(F.panels || [1, 0, 3, 2])[i]]}</text><text x="${612 + (i % 2) * 210}" y="${190 + Math.floor(i / 2) * 210}" font-size="22" fill="#e9dcb8">${p}</text>`).join('')}${label(800, 640, F.lensOk ? 'Lens (aligned)' : 'Fresnel lens panels')}`, act: () => openLens() },
      { id: 'burner', x: 1120, y: 360, w: 260, h: 300, art: () => `<rect x="1170" y="420" width="160" height="220" rx="12" fill="#4a3a2a"/><circle cx="1250" cy="470" r="34" fill="${F.mantled ? '#efe3c4' : '#222'}"/>${label(1250, 690, `Burner${F.oiled ? ' · oil' : ''}${F.mantled ? ' · mantle' : ''}`)}`,
        act: () => openBurner(),
        use: { oil: () => { F.oiled = 1; take('oil'); say('You pour the paraffin into the burner reservoir.'); return true; }, mantle: () => { F.mantled = 1; take('mantle'); say('You fit the new mantle over the burner.'); return true; } } },
      { id: 'flasher', x: 200, y: 360, w: 300, h: 300, art: () => `<rect x="220" y="400" width="260" height="220" rx="10" fill="#3a3a38"/><circle cx="300" cy="500" r="40" fill="#c9a24a"/><circle cx="410" cy="500" r="40" fill="#c9a24a"/>${label(350, 690, 'Flash clockwork')}`, act: () => openFlasher() },
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
Object.keys(ROOMS).forEach(r => { const im = new Image(); im.onload = () => { imgOk[r] = true; if (S.room === r) render(); }; im.src = IMG + r + '.jpg'; });

const NAMES = { back: '← Back', down: '← Down', toDining: 'Corridor →', toVan: 'Van →', toEngine: 'Door to the tender', toStudy: 'Study door', toTower: 'Tower door', toOil: 'Oil store', toRadio: 'Radio hut' };
const spotName = s => { const m = (s.art ? s.art() : '').match(/class="lbl[^"]*"[^>]*>([^<]+)</); return (m ? m[1] : NAMES[s.id] || s.id).replace(/&amp;/g, '&'); };
function render() {
  const R = ROOMS[S.room];
  $('room').textContent = R.name;
  const art = imgOk[S.room] ? `<image href="${IMG + S.room}.jpg" width="1600" height="900"/>` : R.bg();
  $('stage').innerHTML = `<defs><radialGradient id="lamp"><stop offset="0" stop-color="#ffcf7a" stop-opacity=".22"/><stop offset="1" stop-color="#ffcf7a" stop-opacity="0"/></radialGradient></defs>${art}` +
    R.spots.map(s => `<g class="hs${imgOk[S.room] ? ' photo' : ''}" data-id="${s.id}" tabindex="0" role="button" aria-label="${s.id}">${imgOk[S.room] ? `<g class="tag"><rect x="${s.x + s.w / 2 - (spotName(s).length * 7.5 + 18)}" y="${s.y + s.h - 46}" width="${spotName(s).length * 15 + 36}" height="38" rx="19"/><text x="${s.x + s.w / 2}" y="${s.y + s.h - 20}" text-anchor="middle">${spotName(s)}</text></g>` : s.art()}<rect class="hit" x="${s.x}" y="${s.y}" width="${s.w}" height="${s.h}" rx="10"/></g>`).join('');
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
function openTides() {
  const rows = [['14 Nov', '00:51', '07:02', '13:12', '19:16'], ['15 Nov', '01:38', '07:51', '13:59', '20:02'], ['16 Nov', '02:24', '08:37', '14:44', '20:49']];
  note('tides', 'Tide table, Gull Rock (high/low water): ' + rows.map(r => `${r[0]}: HW ${r[1]} · LW ${r[2]} · HW ${r[3]} · LW ${r[4]}`).join(' / '));
  modal(`<h2>Tide table – Gull Rock</h2><p class="small">November 1912 · Greenwich mean time</p><div class="paper"><table style="width:100%">${'<tr><th>Date</th><th>High</th><th>Low</th><th>High</th><th>Low</th></tr>' + rows.map(r => `<tr>${r.map(c => `<td style="text-align:center">${c}</td>`).join('')}</tr>`).join('')}</table></div><p class="small">The clock on the wall says five to one in the morning. The calendar shows Friday 15 November.</p>`);
}
function openOilDoor() {
  const w = wheels(4, code => { if (code !== '0138') return false; F.oilOpen = 1; closeModal(); say('The four brass wheels line up and the oil-store bolt slides back.'); save(); return true; });
  modal(`<h2>Oil store door</h2><p>A combination lock of four wheels, stamped with a little wave.</p>${w.html}`, w.bind);
}
function openDesk() {
  if (!F.letter) { F.letter = 1; give('letter'); }
  note('forged', 'Logbook on the desk, last entry, 15 Nov 23:00: “Calm sea. Glass steady at 1021 mb. All well. Lamp lit.” – The handwriting is neat, unlike Abel’s other entries.');
  note('letter', 'Trinity House letter: “SS Marigold, official no. 4127, call sign MGQX, passes Gull Rock about 02:00 on 15 Nov. Keep the light.”');
  note('drawing', 'Child’s drawing on the desk: four flags in a row, signed “Tamsin, age 7 – Grandpa’s secret word for the hut”.');
  modal(`<h2>The keeper’s desk</h2><h3>Logbook</h3><p class="paper">15 Nov · 23:00 · Calm sea. Glass steady at 1021 mb. All well. Lamp lit.</p><h3>Letter from Trinity House</h3><p class="paper">The SS Marigold, official no. 4127, call sign MGQX, will pass Gull Rock about 02:00 on 15 November. Keep the light.</p><h3>Child’s drawing</h3><svg viewBox="0 0 320 70" class="close" style="max-width:420px">${['G', 'U', 'L', 'L'].map((k, i) => flag(k, 10 + i * 78, 12)).join('')}</svg><p class="small">“Tamsin, age 7 – Grandpa’s secret word for the hut.”</p>`);
}
function openChart() {
  note('chart', 'Signal flag chart: G yellow/blue stripes · U red/white quarters · L yellow/black quarters · T red-white-blue · I yellow with black ball · D blue-yellow-blue · E blue over red · S white with blue square.');
  modal(`<h2>International signal flags</h2><svg viewBox="0 0 440 210" class="close">${Object.keys(FLAGS).map((k, i) => flag(k, 20 + (i % 4) * 105, 20 + Math.floor(i / 4) * 100) + `<text x="${50 + (i % 4) * 105}" y="${82 + Math.floor(i / 4) * 100}" text-anchor="middle" fill="#efe3c4" font-family="Georgia" font-size="16">${k}</text>`).join('')}</svg>`);
}
function openRadioLock() {
  const A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', v = [0, 0, 0, 0];
  modal(`<h2>Radio hut padlock</h2><p>A letter padlock with four wheels.</p><div class="wheels">${v.map((_, i) => `<div class="wheel"><button data-a="${i}" data-d="1">▲</button><b id="a${i}">A</b><button data-a="${i}" data-d="-1">▼</button></div>`).join('')}</div><button class="btn" id="tryl">Try the padlock</button><p id="ares" class="res"></p>`, m => {
    const draw = () => v.forEach((x, i) => { m.querySelector('#a' + i).textContent = A[x]; });
    m.querySelectorAll('[data-a]').forEach(b => b.addEventListener('click', () => { const i = +b.dataset.a; v[i] = (v[i] + +b.dataset.d + 26) % 26; draw(); }));
    m.querySelector('#tryl').addEventListener('click', () => { if (v.map(x => A[x]).join('') === 'GULL') { F.radioOpen = 1; closeModal(); say('The padlock snaps open. You run through the rain to the radio hut.'); save(); go('radio'); } else m.querySelector('#ares').textContent = 'It won’t open.'; }); draw();
  });
}
function openDrawer() {
  if (F.drawer) return say('The wireless set is dead – the aerial blew down in the gale. The drawer is empty now.');
  const w = wheels(3, code => { if (code !== '127') return false; F.drawer = 1; give('mantle'); closeModal(); say('The drawer opens: a spare lamp mantle in its box.'); save(); return true; });
  modal(`<h2>Wireless set</h2><p>The set is dead – the aerial came down in the gale. Under it, a drawer with three number wheels and a brass label: <i>“Ship no. – last three”</i>.</p>${w.html}`, w.bind);
}
function openLights() {
  const L = [['Godrevy', 'Fl W 15s', 'one white flash every 15 s'], ['Gull Rock', 'Fl(2) W 10s', 'two white flashes every 10 s'], ['Pendeen', 'Iso W 4s', 'steady 2 s on, 2 s off'], ['St Ennis Head', 'Fl(3) W 15s', 'three white flashes every 15 s']];
  note('lights', 'Admiralty list of lights: ' + L.map(l => `${l[0]}: ${l[1]} (${l[2]})`).join(' · '));
  modal(`<h2>Admiralty list of lights</h2><div class="paper"><table style="width:100%">${L.map(l => `<tr><td>${l[0]}</td><td>${l[1]}</td><td class="small">${l[2]}</td></tr>`).join('')}</table></div><p class="small">Every lighthouse has its own character, so ships know which one they are seeing.</p>`);
}
const ARROWS = ['↑', '→', '↓', '←'];
function openLens() {
  if (F.lensOk) return say('The four panels are aligned. The beam will go out to sea.');
  const v = (F.panels || [1, 0, 3, 2]).slice();
  modal(`<h2>Fresnel lens</h2><p>Four heavy glass panels, each turning on a brass pin.</p><div class="pegs">${['A', 'B', 'C', 'D'].map((p, i) => `<button class="peg" data-p="${i}"><b>${p}</b><span id="pa${i}" style="font-size:2rem"></span></button>`).join('')}</div><button class="btn" id="setl">Lock the panels</button><p id="lres" class="res"></p>`, m => {
    const draw = () => v.forEach((x, i) => { m.querySelector('#pa' + i).textContent = ARROWS[x]; });
    m.querySelectorAll('[data-p]').forEach(b => b.addEventListener('click', () => { const i = +b.dataset.p; v[i] = (v[i] + 1) % 4; F.panels = v.slice(); dirty = true; draw(); }));
    m.querySelector('#setl').addEventListener('click', () => { if (v.join('') === '0123') { F.lensOk = 1; closeModal(); say('The panels click into place. The prisms catch the lamplight in one sharp line.'); save(); } else m.querySelector('#lres').textContent = 'The panels scatter the light in all directions.'; }); draw();
  });
}
function openBurner() {
  if (F.lit) return say('The lamp burns white and fierce.');
  const miss = [!F.oiled && 'no oil in the reservoir', !F.mantled && 'the mantle is torn to ash', !F.lensOk && 'the lens panels are knocked out of line'].filter(Boolean);
  if (miss.length) return say('The burner won’t light properly: ' + miss.join(', ') + '.');
  F.lit = 1; save(); say('You light the burner. A blinding white light fills the room – but it shines steady. A ship would not know it for Gull Rock.');
}
function openFlasher() {
  if (!F.lit) return say('Brass clockwork that turns a shutter around the lamp. Nothing to do until the lamp burns.');
  let fl = 1, per = 5;
  modal(`<h2>Flash clockwork</h2><p>Two brass dials: how many flashes, and how often the pattern repeats.</p><div class="dial"><span>Flashes</span><button id="fm">◀</button><b id="fv"></b><button id="fp">▶</button></div><div class="dial"><span>Every</span><button id="pm">◀</button><b id="pv"></b><button id="pp">▶</button></div><button class="btn" id="wind">Wind and release</button><p id="fres" class="res"></p>`, m => {
    const draw = () => { m.querySelector('#fv').textContent = fl; m.querySelector('#pv').textContent = per + ' s'; };
    m.querySelector('#fm').addEventListener('click', () => { fl = fl > 1 ? fl - 1 : 4; draw(); }); m.querySelector('#fp').addEventListener('click', () => { fl = fl < 4 ? fl + 1 : 1; draw(); });
    m.querySelector('#pm').addEventListener('click', () => { per = per > 5 ? per - 5 : 20; draw(); }); m.querySelector('#pp').addEventListener('click', () => { per = per < 20 ? per + 5 : 5; draw(); });
    m.querySelector('#wind').addEventListener('click', () => { if (fl === 2 && per === 10) { F.won = 1; closeModal(); save(); setTimeout(win, 900); } else m.querySelector('#fres').textContent = 'The light turns – but that is another lighthouse’s character. A ship could steer onto the reef.'; }); draw();
  });
}
function combine(a, b) { say('Those two don’t go together.'); sel = null; renderInv(); }

/* ---------------- hints ---------------- */
const STAGES = [
  ['oil', () => F.oilOpen, ['Abel left a note about the oil store in his coat.', '“High water” – the tide table on the wall. What night is it, and what time?', 'Tonight is 15 November, just before 01:00: high water 01:38. Oil store code 0138.']],
  ['radio', () => F.radioOpen, ['The hut padlock wants a four-letter word. A child knew it.', 'Tamsin drew four flags. The oil store has a chart of signal flags.', 'Yellow/blue stripes G, red/white U, yellow/black L, L: GULL.']],
  ['log', () => F.realLog, ['The logbook on the desk says the sea was calm. The barometer disagrees.', 'Someone wrote a false log. Abel may have hidden the real one where only he would look.', 'Look behind the oil drums in the oil store.']],
  ['tower', () => F.towerOpen, ['The true log says where the spare tower key is.', 'Something in the cottage has a brass case.', 'Open the barometer case for the key, then use it on the tower door.']],
  ['mantle', () => F.drawer, ['The lamp will need a new mantle. The radio hut has a numbered drawer.', '“Ship no. – last three”. Which ship, and which number?', 'The Marigold is official no. 4127 – drawer code 127.']],
  ['lens', () => F.lensOk, ['The lens panels are out of line. Abel drew how they should sit.', 'The back page of the true log has a lens diagram.', 'Set A ↑, B →, C ↓, D ← and lock them.']],
  ['lamp', () => F.lit, ['The burner needs three things: oil, a mantle and an aligned lens.', 'The oil store has a paraffin tank; the radio drawer has the mantle.', 'Use the paraffin and the mantle on the burner, align the lens, then light it.']],
  ['flash', () => F.won, ['A steady light isn’t enough – every lighthouse has its own signature.', 'The Admiralty list in the radio hut gives each light’s character.', 'Gull Rock is Fl(2) 10s: set 2 flashes every 10 seconds.']],
];
function stage() { return STAGES.find(s => !s[1]()); }
$('hint').addEventListener('click', () => {
  if (!S.started || paused) return;
  const st = stage(); if (!st) return;
  const n = S.hints[st[0]] || 0, cost = n >= 2 ? 5 : 3;
  const shown = st[2].slice(0, n).map(t => `<li>${t}</li>`).join('');
  modal(`<h2>Hints</h2>${shown ? `<ol class="hints">${shown}</ol>` : '<p>Hints come in three steps: a nudge, a clearer pointer, then the answer.</p>'}${n < 3 ? `<button class="btn" id="more">${n === 2 ? 'Show the answer' : n ? 'A clearer hint' : 'Give me a nudge'} (+${cost} min)</button>` : '<p class="small">That’s everything for this step.</p>'}`, m => {
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
  c.innerHTML = `<div class="pausebox"><h2>02:00.</h2><p>Out in the dark, a ship’s horn – far too close to the reef.</p><p>You can keep playing to light the lamp, but your time won’t go on the leaderboard.</p><button class="btn btn-big" id="cont">Keep going</button> <button class="btn ghost" id="again">Start over</button></div>`;
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
  c.innerHTML = `<div class="pausebox win"><p class="kicker">The light is burning</p><h2>You escaped, ${NAME}!</h2>
    <p>Two white flashes, every ten seconds, sweep across the storm. Far out, the Marigold’s lights swing away from the reef and steady on a safe course. At dawn the coastguard finds Abel Penhallow tied up in Jory Treloar’s boat shed – and Treloar’s red lantern explains the rest.</p>
    <p class="big">${S.over ? 'Overtime' : fmt(t) + ' used'}</p><p>${S.hintCount ? S.hintCount + ' hint' + (S.hintCount > 1 ? 's' : '') + ' (time added)' : 'No hints – impressive.'}</p>
    <p><a class="btn btn-big" href="/escape/${SLUG}">See the leaderboard</a></p><p class="small"><a href="/">Back to Six Clues</a></p></div>`;
  c.hidden = false;
}

/* ---------------- intro ---------------- */
function intro() {
  const c = $('cover');
  const resume = S.started;
  c.innerHTML = `<div class="pausebox intro"><p class="kicker">Gull Rock, Cornwall · 15 November 1912 · 00:55</p><h2>The Lighthouse at Gull Rock</h2>
    ${resume ? `<p>Welcome back. The clock stopped at <b>${fmt(left())}</b> when you left.</p>` : `<p>You are the relief keeper, rowed out through a rising gale. The tower is dark. Keeper Abel Penhallow is gone – his oilskin on the hook, his supper cold on the table.</p>
    <p>At about 02:00 the steamer Marigold passes the reef. Without the light, she will strike. You have one hour to find out what happened here and light the lamp.</p>
    <p>Level 2: not everything you read here is true.</p>`}
    <button class="btn btn-big" id="go">${resume ? 'Resume' : 'Start the clock'}</button><p class="small">Pause any time with ⏸ – the room is hidden and the clock stops.</p></div>`;
  c.hidden = false;
  c.querySelector('#go').addEventListener('click', () => { S.started = true; last = performance.now(); c.hidden = true; say(resume ? ROOMS[S.room].name + '.' : 'Rain hammers the window. The wind howls around the tower. Look around.'); save(); });
}

render(); renderInv(); tick(); intro();
if (S.over) say('02:00 has passed – you can still finish, but off the leaderboard.');
})();
