/* Six Clues escape room #2 – The Last Night Train (prototype, harder).
 * Scenes are SVG placeholders. Drop real art in /assets/img/escape/the-last-night-train/<room>.jpg (1600x900) – picked up automatically. */
(() => {
'use strict';
const root = document.getElementById('escape');
const SLUG = root.dataset.slug, CSRF = root.dataset.csrf, NAME = root.dataset.name || 'Detective';
const LIMIT = 3600000, IMG = '/assets/img/escape/' + SLUG + '/', AUDIO = '/assets/audio/escape/' + SLUG + '/';
const fresh = () => ({ v: 1, room: 'compartment', inv: [], flags: {}, notes: [], elapsed: 0, penalty: 0, hints: {}, hintCount: 0, started: false, over: false });
let S = Object.assign(fresh(), window.ESCAPE_STATE || {});
let sel = null, paused = false, dirty = false, last = performance.now(), finished = false;

/* ---------------- items ---------------- */
const ITEMS = {
  ticket: ['🎫', 'Courier’s ticket', 'Venezia – Istanbul, sleeping car, compartment 7. Three stations are punched: Niš, Plovdiv and Svilengrad.'],
  letter: ['✉️', 'Courier’s note', 'Found in the courier’s book. Three short lines, one for each lock on the briefcase.'],
  smallKey: ['🗝️', 'Small brass key', 'Tiny – too small for a door. It was hidden in the sugar bowl.'],
  watch: ['⌚', 'Pocket watch', 'Stopped at 2:47. Engraved inside the lid: “For the van – the hour I stopped. E.”'],
  morse: ['📇', 'Morse card', 'The conductor’s card with the Morse alphabet. It is copied into your notebook.'],
  stamp: ['🃏', 'Stamped card', 'A blank visiting card with one rubber stamp in violet ink: a key.'],
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
const wood = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 16 }, (_, i) => `<rect x="${i * 100}" y="0" width="96" height="660" fill="${i % 2 ? c2 : c1}"/>`).join('')}`;
const snowWin = (x, y, w, h) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="18" fill="#0b1422" stroke="#6b4a2a" stroke-width="12"/>${Array.from({ length: 22 }, (_, i) => `<circle cx="${x + 15 + (i * 53) % (w - 30)}" cy="${y + 15 + (i * 37) % (h - 30)}" r="${2 + i % 3}" fill="#dfe8f2" opacity=".75"/>`).join('')}<path d="M${x} ${y + h * .72} q${w * .3} -40 ${w * .55} -10 t${w * .45} 0 V${y + h} H${x}z" fill="#1b2533"/>`;
const ROOMS = {
  compartment: {
    name: 'Compartment 7',
    bg: () => `${wood('#3a2416', '#40291a')}<rect y="660" width="1600" height="240" fill="#2a1a10"/><rect x="0" y="640" width="1600" height="20" fill="#c9a24a" opacity=".5"/>${snowWin(560, 90, 480, 300)}<ellipse cx="800" cy="0" rx="560" ry="360" fill="url(#lamp)"/>`,
    spots: [
      { id: 'plaque', x: 130, y: 40, w: 230, h: 90, art: () => `<rect x="140" y="55" width="210" height="60" rx="6" fill="#c9a24a"/><text x="245" y="95" text-anchor="middle" font-family="Georgia" font-size="26" fill="#2a1a10">7 / 11</text>${label(245, 150, 'Door plaque')}`,
        act: () => { note('plaque', 'Door plaque: “Compagnie Internationale des Wagons-Lits · sleeping car 2 · compartment 7 of 11”.'); say('A brass plaque: Wagons-Lits, sleeping car 2 – compartment 7 of 11.'); } },
      { id: 'coat', x: 60, y: 170, w: 200, h: 420, art: () => `<circle cx="160" cy="185" r="9" fill="#c9a24a"/><path d="M160 190 L100 250 L90 560 L230 560 L220 250 Z" fill="#2c2f38"/><rect x="120" y="420" width="44" height="40" fill="#24262d"/>${label(160, 600, 'Courier’s coat')}`,
        act: () => { if (F.coat) return say('Only lint and a cloakroom token left in the pockets.'); F.coat = 1; give('ticket'); note('ticket', 'Courier’s ticket: Venezia → Istanbul. Punched over Niš, Plovdiv and Svilengrad.'); say('In the inside pocket: his ticket. Three stations have been punched.'); } },
      { id: 'rack', x: 1120, y: 40, w: 420, h: 200, art: () => `<rect x="1120" y="160" width="420" height="14" fill="#c9a24a"/><ellipse cx="1330" cy="140" rx="110" ry="26" fill="#6b2a2a"/><rect x="1220" y="80" width="220" height="64" rx="20" fill="#7a3030"/>${F.hatOpen ? '<ellipse cx="1330" cy="82" rx="100" ry="18" fill="#2a1010"/>' : '<rect x="1318" y="110" width="24" height="22" fill="#c9a24a"/>'}${label(1330, 210, 'Hatbox on the rack')}`,
        act: () => F.hatOpen ? say('The hatbox is empty now.') : say('A round hatbox with a tiny brass lock. It isn’t heavy enough for a hat.'),
        use: { smallKey: () => { F.hatOpen = 1; take('smallKey'); give('watch'); note('watch', 'Pocket watch from the hatbox: stopped at 2:47. Inside the lid: “For the van – the hour I stopped. E.”'); say('The little key fits. Inside, wrapped in a silk scarf: a gold pocket watch, stopped at 2:47.'); return true; } } },
      { id: 'berth', x: 300, y: 430, w: 600, h: 230, art: () => `<rect x="300" y="470" width="600" height="170" rx="12" fill="#5a1f22"/><rect x="300" y="450" width="600" height="40" rx="12" fill="#6b2528"/><rect x="420" y="430" width="120" height="34" fill="#2a3a4a" transform="rotate(-6 480 447)"/>${label(600, 690, 'Berth (a book lies on it)')}`,
        act: () => { if (F.book) return say('“The Mysterious Affair at the Frontier” – the courier’s place is still marked by a pencil.'); F.book = 1; give('letter'); note('letter', 'Courier’s note, tucked in his book:<br>I. Where we stood when the clock struck three.<br>II. What the wire told me.<br>III. What the man who isn’t there carries.'); say('A thin paperback. Tucked inside: a folded note in the courier’s hand – three short lines.'); } },
      { id: 'case', x: 950, y: 430, w: 300, h: 220, art: () => `<rect x="960" y="470" width="280" height="170" rx="12" fill="#5b3c25" stroke="#2a1a10" stroke-width="6"/><rect x="1060" y="450" width="80" height="28" rx="8" fill="none" stroke="#c9a24a" stroke-width="8"/>${[0, 1, 2].map(i => `<rect x="${990 + i * 80}" y="530" width="60" height="44" rx="6" fill="#c9a24a"/><text x="${1020 + i * 80}" y="561" text-anchor="middle" font-family="Georgia" font-size="22" fill="#2a1a10">${['I', 'II', 'III'][i]}</text>`).join('')}${label(1100, 680, 'The courier’s briefcase')}`,
        act: () => openCase() },
      { id: 'toDining', x: 1300, y: 300, w: 260, h: 380, art: () => door(1320, 320, 220, 340, true, 'Corridor → dining car') , act: () => go('dining') },
    ],
  },
  dining: {
    name: 'The dining car',
    bg: () => `${wood('#2e2016', '#33241a')}<rect y="660" width="1600" height="240" fill="#3a1414"/>${[300, 800, 1300].map(x => snowWin(x - 120, 70, 240, 170)).join('')}<ellipse cx="800" cy="0" rx="700" ry="380" fill="url(#lamp)"/>`,
    spots: [
      { id: 'back', x: 20, y: 760, w: 260, h: 110, art: () => `<text x="40" y="830" class="lbl big">← Compartment 7</text>`, act: () => go('compartment') },
      { id: 'timetable', x: 60, y: 270, w: 260, h: 300, art: () => `<rect x="70" y="280" width="240" height="280" fill="#e9dcb8" stroke="#6b4a2a" stroke-width="8"/>${Array.from({ length: 9 }, (_, i) => `<line x1="90" y1="${320 + i * 26}" x2="290" y2="${320 + i * 26}" stroke="#8a7a5a" stroke-width="3"/>`).join('')}${label(190, 600, 'Timetable')}`, act: () => openTimetable() },
      { id: 'map', x: 360, y: 270, w: 320, h: 230, art: () => `<rect x="370" y="280" width="300" height="200" fill="#d9c9a0" stroke="#6b4a2a" stroke-width="8"/><path d="M390 440 q60 -80 120 -40 t140 -90" fill="none" stroke="#7a2a22" stroke-width="5" stroke-dasharray="10 6"/>${[[400, 430], [470, 410], [530, 400], [590, 360], [640, 320]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="9" fill="#2a1a10"/>`).join('')}${label(520, 530, 'Route poster')}`, act: () => openMap() },
      { id: 'table', x: 720, y: 430, w: 380, h: 230, art: () => `<rect x="730" y="480" width="360" height="40" fill="#efe8d8"/><rect x="760" y="520" width="20" height="130" fill="#3a2416"/><rect x="1040" y="520" width="20" height="130" fill="#3a2416"/><ellipse cx="860" cy="470" rx="34" ry="14" fill="#d9d2c0"/><path d="M845 470 v-26 h30 v26" fill="#c9c2b0"/><circle cx="970" cy="465" r="22" fill="#a33" opacity=".6"/>${label(910, 690, 'Table (sugar bowl, menu)')}`,
        act: () => { if (F.sugar) return say('Just sugar cubes now. And a menu: Bouillon · Truite meunière · Crème brûlée.'); F.sugar = 1; give('smallKey'); say('Under the sugar cubes in the bowl: a tiny brass key.'); } },
      { id: 'lectern', x: 1130, y: 330, w: 200, h: 330, art: () => `<path d="M1150 360 h160 l-20 60 h-120 z" fill="#5b3c25"/><rect x="1215" y="420" width="30" height="230" fill="#4a3020"/><rect x="1165" y="340" width="130" height="30" fill="#e9dcb8" transform="rotate(-8 1230 355)"/>${label(1230, 690, 'Steward’s lectern')}`, act: () => openPassengers() },
      { id: 'conductor', x: 1360, y: 120, w: 140, h: 330, art: () => `<circle cx="1430" cy="135" r="8" fill="#c9a24a"/><path d="M1430 140 L1385 190 L1375 430 L1485 430 L1475 190 Z" fill="#1f2a44"/><rect x="1400" y="250" width="60" height="8" fill="#c9a24a"/>${label(1430, 460, 'Conductor’s jacket')}`,
        act: () => { if (F.morse) return say('The jacket is empty. A whistle on a cord, nothing else.'); F.morse = 1; give('morse'); note('morse', 'Morse card: A ·−  B −···  C −·−·  D −··  E ·  F ··−·  G −−·  H ····  I ··  J ·−−−  K −·−  L ·−··  M −−  N −·  O −−−  P ·−−·  Q −−·−  R ·−·  S ···  T −  U ··−  V ···−  W ·−−  X −··−  Y −·−−  Z −−··'); say('In the breast pocket: a worn card with the Morse alphabet. You copy it into your notebook.'); } },
      { id: 'toVan', x: 1520, y: 300, w: 80, h: 380, art: () => `<rect x="1525" y="320" width="70" height="340" fill="${F.vanOpen ? '#140d08' : '#4a3020'}" stroke="#2a1a10" stroke-width="6"/>${F.vanOpen ? '' : '<rect x="1535" y="470" width="50" height="40" rx="6" fill="#c9a24a"/>'}<text x="1560" y="300" text-anchor="middle" class="lbl">Van →</text>`,
        act: () => F.vanOpen ? go('van') : openVanDoor() },
    ],
  },
  van: {
    name: 'The mail & luggage van',
    bg: () => `<rect width="1600" height="900" fill="#1c1a17"/>${Array.from({ length: 10 }, (_, i) => `<rect x="${i * 170}" y="0" width="10" height="660" fill="#2c2924"/>`).join('')}<rect y="660" width="1600" height="240" fill="#141210"/><ellipse cx="800" cy="0" rx="500" ry="320" fill="url(#lamp)"/>`,
    spots: [
      { id: 'back', x: 20, y: 760, w: 260, h: 110, art: () => `<text x="40" y="830" class="lbl big">← Dining car</text>`, act: () => go('dining') },
      { id: 'luggage', x: 80, y: 240, w: 640, h: 420, art: () => [[100, 520, 200, 130, '#6b4a2a'], [320, 540, 170, 110, '#3a4a5a'], [510, 500, 190, 150, '#5a2a2a'], [150, 390, 170, 120, '#4a5a3a'], [380, 410, 230, 120, '#7a6a4a']].map(([x, y, w, h, c]) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="10" fill="${c}" stroke="#1a120a" stroke-width="5"/><rect x="${x + w / 2 - 25}" y="${y - 12}" width="50" height="16" rx="6" fill="none" stroke="#c9a24a" stroke-width="5"/><rect x="${x + 12}" y="${y + 14}" width="40" height="26" fill="#e9dcb8"/>`).join('') + label(400, 230, 'Luggage (tagged)'), act: () => openLuggage() },
      { id: 'telegraph', x: 900, y: 300, w: 420, h: 360, art: () => `<rect x="910" y="470" width="400" height="30" fill="#5b3c25"/><rect x="930" y="500" width="20" height="150" fill="#3a2416"/><rect x="1270" y="500" width="20" height="150" fill="#3a2416"/><rect x="980" y="400" width="140" height="70" rx="8" fill="#2a2a2a"/><circle cx="1050" cy="390" r="14" fill="#c9a24a"/><path d="M1140 460 q60 -10 90 0" fill="none" stroke="#e9dcb8" stroke-width="16"/><path d="M1140 440 q70 -20 120 -5" fill="none" stroke="#e9dcb8" stroke-width="12"/>${label(1110, 690, 'Telegraph & paper tapes')}`, act: () => openTelegraph() },
      { id: 'safe', x: 1360, y: 320, w: 200, h: 300, art: () => `<rect x="1370" y="330" width="180" height="280" fill="#3a3a38" stroke="#111" stroke-width="8"/><circle cx="1460" cy="460" r="36" fill="#555"/><text x="1460" y="560" text-anchor="middle" font-size="18" fill="#aaa" font-family="Georgia">POSTE</text>${label(1460, 650, 'Mail safe')}`,
        act: () => say('The railway mail safe. Its lock is sealed by the post office – not even the conductor can open it. Not your business tonight.') },
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
const SYMBOLS = [['star', '★', 'Star'], ['crown', '♛', 'Crown'], ['anchor', '⚓', 'Anchor'], ['lion', '🦁', 'Lion'], ['eagle', '🦅', 'Eagle'], ['bell', '🔔', 'Bell'], ['crescent', '☾', 'Crescent'], ['tower', '♜', 'Tower'], ['rose', '🌹', 'Rose'], ['key', '🔑', 'Key']];
const STOPS = [['Beograd', '15:52', '16:05', 'star'], ['Niš', '19:31', '19:48', 'crown'], ['Caribrod (frontier)', '21:10', '21:40', 'anchor'], ['Sofia', '22:52', '23:20', 'lion'], ['Plovdiv', '02:31', '03:09', 'eagle'], ['Svilengrad', '05:20', '05:45', 'bell'], ['Edirne (frontier)', '06:00', '06:40', 'crescent'], ['Istanbul Sirkeci', '13:45', '–', 'tower']];
function openTimetable() {
  note('timetable', 'Timetable, Simplon-Orient-Express, winter 1934:<br>' + STOPS.map(s => `${s[0]} arr. ${s[1]} · dep. ${s[2]}`).join('<br>'));
  modal(`<h2>Timetable – Simplon-Orient-Express</h2><p class="small">Winter service 1934 · eastbound · all times local</p><div class="paper"><table style="width:100%;border-collapse:collapse">${'<tr><th style="text-align:left">Station</th><th>arr.</th><th>dep.</th></tr>' + STOPS.map(s => `<tr><td>${s[0]}</td><td style="text-align:center">${s[1]}</td><td style="text-align:center">${s[2]}</td></tr>`).join('')}</table></div>`);
}
function openMap() {
  note('map', 'Route poster: each station has its town crest – ' + STOPS.map(s => `${s[0]}: ${SYMBOLS.find(x => x[0] === s[3])[2]}`).join(' · '));
  modal(`<h2>Route poster</h2><p class="small">“Venise – Constantinople. The crests of the towns along your journey.”</p><div class="crests">${STOPS.map(s => { const y = SYMBOLS.find(x => x[0] === s[3]); return `<div class="crest"><span>${y[1]}</span><b>${s[0]}</b><small>${y[2]}</small></div>`; }).join('')}</div>`);
}
const PASSENGERS = [['1', 'Mme Hélène Duval', 'Lyon'], ['2', 'Countess V. Orlova', 'Paris'], ['3', 'Dr. Felix Weiss', 'Vienna'], ['4', 'Mr. Arthur Hart', 'London'], ['5', 'Father Benedikt', 'Zagreb'], ['7', 'Mr. E. Novak', 'Venice'], ['8', 'Miss Clara Ward', 'Trieste'], ['9', 'Col. R. Ashby', 'Belgrade'], ['10', 'Mr. &amp; Mrs. Laszlo', 'Budapest'], ['11', 'Signor P. Conti', 'Milan'], ['12', 'Herr Viktor Lang', 'Belgrade']];
function openPassengers() {
  note('passengers', 'Steward’s dinner list (sleeping car 2): ' + PASSENGERS.map(p => `${p[0]} ${p[1]}`).join(' · '));
  modal(`<h2>Steward’s dinner list</h2><p class="small">Sleeping car 2 · first sitting 19:30</p><div class="paper"><table style="width:100%">${PASSENGERS.map(p => `<tr><td>Comp. ${p[0]}</td><td>${p[1]}</td><td>${p[2]}</td></tr>`).join('')}</table></div><p class="small">Compartment 6 is marked “vacant”.</p>`);
}
function openVanDoor() {
  const w = wheels(4, code => { if (code !== '0247') return false; F.vanOpen = 1; closeModal(); say('The four wheels click into place and the van door slides open. Cold air, the smell of coal and leather.'); save(); return true; });
  modal(`<h2>Door to the mail &amp; luggage van</h2><p>“Staff only.” A brass lock with four number wheels.</p>${w.html}`, w.bind);
}
const BAGS = [
  ['Duval', 'Hatbox and valise · Mme Duval · comp. 1', 'Silk dresses, a box of macarons. Nothing else.'],
  ['Orlova', 'Steamer trunk · Countess Orlova · comp. 2', 'Locked with a heavy padlock and a wax seal: “Do not touch.” It is not yours to open – and nothing points to it.'],
  ['Weiss', 'Doctor’s bag · Dr. Weiss · comp. 3', 'Stethoscope, bandages, a bottle of iodine.'],
  ['Hart', 'Golf bag · Mr. Hart · comp. 4', 'Clubs, tees and a guidebook to Constantinople.'],
  ['Lang', 'Small brown suitcase · Herr V. Lang · comp. 12', 'Almost weightless. No clothes at all – just one visiting card in the lid pocket.'],
];
function openLuggage() {
  modal(`<h2>Luggage, tagged by compartment</h2><div class="books">${BAGS.map(b => `<button class="book" data-b="${b[0]}">${b[1]}</button>`).join('')}</div><p id="lres" class="res" style="color:#e8d9b0"></p>`, m => {
    m.querySelectorAll('[data-b]').forEach(b => b.addEventListener('click', () => {
      const bag = BAGS.find(x => x[0] === b.dataset.b); m.querySelector('#lres').textContent = bag[2];
      if (bag[0] === 'Lang' && !F.stamp) { F.stamp = 1; give('stamp'); note('stamp', 'In Herr V. Lang’s empty suitcase (tag: comp. 12): a blank card stamped with a violet key.'); save(); }
    }));
  });
}
const TAPES = [['Tape marked “TEST · Sofia 23:05”', '·−·· / ·· / −−− / −·'], ['Tape marked “Comp. 7 · Plovdiv 02:40”', '·−· / −−− / ··· / ·']];
function openTelegraph() {
  note('tapes', 'Telegraph tapes: ' + TAPES.map(t => `${t[0]}: ${t[1]}`).join(' · '));
  modal(`<h2>The telegraph</h2><p>Two paper tapes hang from the receiver. The letters are separated by slashes.</p>${TAPES.map(t => `<p class="small">${t[0]}</p><p class="paper" style="font-size:1.4rem;letter-spacing:.08em">${t[1]}</p>`).join('')}${has('morse') ? '<p class="small">Your Morse card is in the notebook.</p>' : '<p class="small">Without a Morse alphabet this is just dots and dashes.</p>'}`);
}
function openCase() {
  if (F.won) return win();
  const v = S.caseDial || [0, 0, 0];
  modal(`<h2>The courier’s briefcase</h2><p>Three brass dials, marked I, II and III. Each turns through ten engraved symbols.</p><div class="wheels">${[0, 1, 2].map(i => `<div class="wheel"><small>${['I', 'II', 'III'][i]}</small><button data-c="${i}" data-d="1">▲</button><b id="c${i}" style="font-size:2rem"></b><i id="cn${i}" class="small"></i><button data-c="${i}" data-d="-1">▼</button></div>`).join('')}</div><button class="btn" id="tryc">Try the clasps</button><p id="cres" class="res"></p>`, m => {
    const draw = () => v.forEach((x, i) => { m.querySelector('#c' + i).textContent = SYMBOLS[x][1]; m.querySelector('#cn' + i).textContent = SYMBOLS[x][2]; });
    m.querySelectorAll('[data-c]').forEach(b => b.addEventListener('click', () => { const i = +b.dataset.c; v[i] = (v[i] + +b.dataset.d + SYMBOLS.length) % SYMBOLS.length; S.caseDial = v; dirty = true; draw(); }));
    m.querySelector('#tryc').addEventListener('click', () => {
      if (SYMBOLS[v[0]][0] === 'eagle' && SYMBOLS[v[1]][0] === 'rose' && SYMBOLS[v[2]][0] === 'key') { F.won = 1; closeModal(); say('Click – click – click. The clasps spring open.'); save(); setTimeout(win, 1200); }
      else { const r = m.querySelector('#cres'); r.textContent = 'The clasps stay shut.'; r.classList.remove('shake'); void r.offsetWidth; r.classList.add('shake'); }
    }); draw();
  });
}
function combine(a, b) { say('Those two don’t go together.'); sel = null; renderInv(); }

/* ---------------- hints ---------------- */
const STAGES = [
  ['hatbox', () => F.hatOpen, ['The hatbox on the rack has a tiny lock. Look for a tiny key – somewhere you wouldn’t look for keys.', 'Waiters hide things where guests never dig.', 'The small key is in the sugar bowl on the dining table. Use it on the hatbox.']],
  ['van', () => F.vanOpen, ['The van door wants four digits. Something you found speaks of the van.', 'The pocket watch: “For the van – the hour I stopped.”', 'The watch stopped at 2:47. Set the van door to 0 2 4 7.']],
  ['case', () => F.won, null],
];
const TRACKS = {
  I: ['Line I of the courier’s note: where the train stood when the clock struck three.', 'The timetable tells you where the train was at 03:00. The route poster gives every station a crest.', 'At 03:00 the train stood in Plovdiv (arr. 02:31, dep. 03:09). Plovdiv’s crest is the Eagle.'],
  II: ['Line II: “what the wire told me” – the telegraph in the van.', 'Two tapes hang there, but only one was meant for compartment 7. The conductor’s jacket has a Morse card.', 'The compartment 7 tape reads ·−· −−− ··· · = ROSE. (The test tape spells LION – a decoy.)'],
  III: ['Line III: “the man who isn’t there”. Check the steward’s list against the train itself.', 'The door plaque says compartment 7 of 11. One passenger on the list claims a compartment that doesn’t exist.', 'Herr V. Lang, compartment 12, doesn’t exist. His suitcase in the van holds a card stamped with a Key.'],
};
function stage() { return STAGES.find(s => !s[1]()); }
function hintStep(key, steps, back) {
  const n = S.hints[key] || 0, cost = n >= 2 ? 5 : 3;
  const shown = steps.slice(0, n).map(t => `<li>${t}</li>`).join('');
  return { html: `${shown ? `<ol class="hints">${shown}</ol>` : '<p>Hints come in three steps: a nudge, a clearer pointer, then the answer.</p>'}${n < 3 ? `<button class="btn" id="more">${n === 2 ? 'Show the answer' : n ? 'A clearer hint' : 'Give me a nudge'} (+${cost} min)</button>` : '<p class="small">That’s everything for this step.</p>'}${back ? '<button class="btn ghost" id="backh">← Other locks</button>' : ''}`,
    bind: (m, again) => { const b = m.querySelector('#more'); b && b.addEventListener('click', () => { S.hints[key] = n + 1; S.penalty += cost * 60000; S.hintCount++; save(); tick(); again(); }); const bb = m.querySelector('#backh'); bb && bb.addEventListener('click', () => $('hint').click()); } };
}
$('hint').addEventListener('click', () => {
  if (!S.started || paused) return;
  const st = stage(); if (!st) return;
  if (st[0] !== 'case') { const h = hintStep(st[0], st[2]); modal(`<h2>Hints</h2>${h.html}`, m => h.bind(m, () => $('hint').click())); return; }
  modal(`<h2>Hints – the briefcase</h2><p>The briefcase has three locks. Which one are you stuck on?</p>${['I', 'II', 'III'].map(k => `<button class="btn ghost" data-t="${k}">Lock ${k} (${S.hints['t' + k] || 0}/3 used)</button>`).join(' ')}`, m => {
    m.querySelectorAll('[data-t]').forEach(b => b.addEventListener('click', () => {
      const k = b.dataset.t, open = () => { const h = hintStep('t' + k, TRACKS[k], true); modal(`<h2>Hints – lock ${k}</h2>${h.html}`, mm => h.bind(mm, open)); }; open();
    }));
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
  c.innerHTML = `<div class="pausebox"><h2>06:00 – the frontier.</h2><p>Brakes scream; lanterns on the platform at Edirne. Customs officers are boarding.</p><p>You can keep playing to open the briefcase, but your time won’t go on the leaderboard.</p><button class="btn btn-big" id="cont">Keep going</button> <button class="btn ghost" id="again">Start over</button></div>`;
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
  c.innerHTML = `<div class="pausebox win"><p class="kicker">The briefcase is open</p><h2>You escaped, ${NAME}!</h2>
    <p>Inside: the courier’s papers, the photographs he risked everything for – and a note: “If you are reading this, I got off at Plovdiv. Get these to Istanbul. – E. Novak.” The train rolls on toward the frontier, and the papers are safe in your coat.</p>
    <p class="big">${S.over ? 'Overtime' : fmt(t) + ' used'}</p><p>${S.hintCount ? S.hintCount + ' hint' + (S.hintCount > 1 ? 's' : '') + ' (time added)' : 'No hints – impressive.'}</p>
    <p><a class="btn btn-big" href="/escape/${SLUG}">See the leaderboard</a></p><p class="small"><a href="/">Back to Six Clues</a></p></div>`;
  c.hidden = false;
}

/* ---------------- intro ---------------- */
function intro() {
  const c = $('cover');
  const resume = S.started;
  c.innerHTML = `<div class="pausebox intro"><p class="kicker">Simplon-Orient-Express · 1934 · 05:00</p><h2>The Last Night Train</h2>
    ${resume ? `<p>Welcome back. The clock stopped at <b>${fmt(left())}</b> when you left.</p>` : `<p>You were hired to meet a courier, Mr Novak, in compartment 7 of the night train to Istanbul. When you slide open the door, he is gone – his coat on the hook, his briefcase locked with three dials on the seat.</p>
    <p>At 06:00 the train reaches the frontier, and the customs men will search everything. You have one hour to find out what Novak left behind – and open the briefcase before they do.</p>
    <p>This one is harder: three trails run side by side, and not everything you find is meant for you.</p>`}
    <button class="btn btn-big" id="go">${resume ? 'Resume' : 'Start the clock'}</button><p class="small">Pause any time with ⏸ – the room is hidden and the clock stops.</p></div>`;
  c.hidden = false;
  c.querySelector('#go').addEventListener('click', () => { S.started = true; last = performance.now(); c.hidden = true; say(resume ? ROOMS[S.room].name + '.' : 'The compartment rocks gently. Snow streams past the window. Somewhere ahead, the engine whistles. Look around.'); save(); });
}

render(); renderInv(); tick(); intro();
if (S.over) say('The frontier has passed – you can still finish, but off the leaderboard.');
})();
