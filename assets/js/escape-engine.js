/* Six Clues escape engine (shared by rooms #4 onward).
 * A room file calls EscapeEngine(api => ({ start, items, rooms, stages, intro, timesUp, win, combine })).
 * Scenes: SVG placeholders from rooms[r].bg()/spot.art(); a real scene /assets/img/escape/<slug>/<room>.jpg (1600x900)
 * is used automatically, with invisible click boxes from spot.photo = [x, y, w, h]. */
(() => {
'use strict';
window.EscapeEngine = function (define) {
const root = document.getElementById('escape');
const SLUG = root.dataset.slug, CSRF = root.dataset.csrf, NAME = root.dataset.name || 'Detective';
const LIMIT = 3600000, IMG = '/assets/img/escape/' + SLUG + '/';
let G; // room definition
const fresh = () => ({ v: 1, room: G.start, inv: [], flags: {}, notes: [], elapsed: 0, penalty: 0, hints: {}, hintCount: 0, started: false, over: false });
let S, F, sel = null, paused = false, dirty = false, last = performance.now(), finished = false;

const $ = id => document.getElementById(id);
const say = t => { $('msg').textContent = t; };
const flashBtn = id => { const b = $(id); b.classList.remove('ping'); void b.offsetWidth; b.classList.add('ping'); };
const has = i => S.inv.includes(i);
const give = i => { if (!has(i)) S.inv.push(i); dirty = true; renderInv(); };
const take = i => { S.inv = S.inv.filter(x => x !== i); if (sel === i) sel = null; dirty = true; renderInv(); };
const note = (id, text) => { if (!S.notes.find(n => n.id === id)) { S.notes.push({ id, text }); dirty = true; flashBtn('nb'); } };
const label = (x, y, t) => `<text x="${x}" y="${y}" class="lbl" text-anchor="middle">${t}</text>`;
const door = (x, y, w, h, open, t) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="6" fill="${open ? '#140d08' : '#4a3020'}" stroke="#2a1a10" stroke-width="8"/>
  ${open ? '' : `<rect x="${x + 20}" y="${y + 24}" width="${w - 40}" height="${h * .38}" fill="none" stroke="#2a1a10" stroke-width="4"/><rect x="${x + 20}" y="${y + h * .5}" width="${w - 40}" height="${h * .42}" fill="none" stroke="#2a1a10" stroke-width="4"/><circle cx="${x + w - 26}" cy="${y + h * .5}" r="9" fill="#c9a24a"/>`}${label(x + w / 2, y - 14, t)}`;
const exit = (t, x = 40, y = 830) => `<text x="${x}" y="${y}" class="lbl big">${t}</text>`;
const paper = (x, y, w, h, lines = 6) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="#e9dcb8" stroke="#4a3a2a" stroke-width="6"/>${Array.from({ length: lines }, (_, i) => `<line x1="${x + 18}" y1="${y + 34 + i * (h - 50) / lines}" x2="${x + w - 18}" y2="${y + 34 + i * (h - 50) / lines}" stroke="#8a7a5a" stroke-width="3"/>`).join('')}`;

function modal(html, onReady) { $('mbody').innerHTML = html; $('modal').hidden = false; onReady && onReady($('mbody')); }
function closeModal() { $('modal').hidden = true; render(); }
const shake = el => { el.classList.remove('shake'); void el.offsetWidth; el.classList.add('shake'); };
/* number lock: digits wheels; check(code) returns true when solved */
function numLock(title, text, n, check, fail = 'Clunk. It doesn’t open.') {
  const v = Array(n).fill(0);
  modal(`<h2>${title}</h2><p>${text}</p><div class="wheels">${v.map((_, i) => `<div class="wheel"><button data-w="${i}" data-d="1">▲</button><b id="w${i}">0</b><button data-w="${i}" data-d="-1">▼</button></div>`).join('')}</div><button class="btn" id="try">Try</button><p id="wres" class="res"></p>`, m => {
    const draw = () => v.forEach((x, i) => { m.querySelector('#w' + i).textContent = x; });
    m.querySelectorAll('[data-w]').forEach(b => b.addEventListener('click', () => { const i = +b.dataset.w; v[i] = (v[i] + +b.dataset.d + 10) % 10; draw(); }));
    m.querySelector('#try').addEventListener('click', () => { if (check(v.join(''))) { closeModal(); save(); } else { const r = m.querySelector('#wres'); r.textContent = fail; shake(r); } }); draw();
  });
}
/* letter lock */
function wordLock(title, text, n, check, fail = 'It won’t open.') {
  const A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', v = Array(n).fill(0);
  modal(`<h2>${title}</h2><p>${text}</p><div class="wheels">${v.map((_, i) => `<div class="wheel"><button data-a="${i}" data-d="1">▲</button><b id="a${i}">A</b><button data-a="${i}" data-d="-1">▼</button></div>`).join('')}</div><button class="btn" id="tryl">Try</button><p id="ares" class="res"></p>`, m => {
    const draw = () => v.forEach((x, i) => { m.querySelector('#a' + i).textContent = A[x]; });
    m.querySelectorAll('[data-a]').forEach(b => b.addEventListener('click', () => { const i = +b.dataset.a; v[i] = (v[i] + +b.dataset.d + 26) % 26; draw(); }));
    m.querySelector('#tryl').addEventListener('click', () => { if (check(v.map(x => A[x]).join(''))) { closeModal(); save(); } else { const r = m.querySelector('#ares'); r.textContent = fail; shake(r); } }); draw();
  });
}
/* cycle selector: options per slot (array of arrays of labels); check(indices) */
function cycler(title, text, slots, check, fail = 'Nothing happens.', btn = 'Set') {
  const v = slots.map(() => 0);
  modal(`<h2>${title}</h2><p>${text}</p><div class="pegs">${slots.map((s, i) => `<button class="peg" data-c="${i}"><b>${s.name}</b><span id="cy${i}"></span></button>`).join('')}</div><button class="btn" id="cset">${btn}</button><p id="cres" class="res"></p>`, m => {
    const draw = () => v.forEach((x, i) => { m.querySelector('#cy' + i).textContent = slots[i].opts[x]; });
    m.querySelectorAll('[data-c]').forEach(b => b.addEventListener('click', () => { const i = +b.dataset.c; v[i] = (v[i] + 1) % slots[i].opts.length; draw(); }));
    m.querySelector('#cset').addEventListener('click', () => { if (check(v.map((x, i) => slots[i].opts[x]))) { closeModal(); save(); } else { const r = m.querySelector('#cres'); r.textContent = fail; shake(r); } }); draw();
  });
}
/* ordering: tap items in order */
function orderer(title, text, items, check, fail = 'Wrong order – everything resets.') {
  let pick = [];
  modal(`<h2>${title}</h2><p>${text}</p><div class="pegs">${items.map((t, i) => `<button class="peg" data-o="${i}"><b id="on${i}"></b><span>${t}</span></button>`).join('')}</div><p id="ores" class="res"></p>`, m => {
    const draw = () => items.forEach((_, i) => { const k = pick.indexOf(i); m.querySelector('#on' + i).textContent = k < 0 ? '·' : k + 1; });
    m.querySelectorAll('[data-o]').forEach(b => b.addEventListener('click', () => {
      const i = +b.dataset.o; if (pick.includes(i)) return; pick.push(i); draw();
      if (pick.length === items.length) { if (check(pick.map(k => items[k]))) { closeModal(); save(); } else { pick = []; const r = m.querySelector('#ores'); r.textContent = fail; shake(r); setTimeout(draw, 400); } }
    })); draw();
  });
}
function go(r) { S.room = r; sel = null; render(); renderInv(); say(G.rooms[r].name + '.'); save(); }

const api = { get S() { return S; }, get F() { return F; }, has, give, take, note, say, go, label, door, exit, paper, modal, closeModal, numLock, wordLock, cycler, orderer, save: () => save(), win: () => { F.won = 1; save(); setTimeout(win, 700); } };
G = define(api);
S = Object.assign(fresh(), window.ESCAPE_STATE || {});
F = S.flags;

/* ---------------- shell ---------------- */
root.innerHTML = `
<header class="bar"><a class="logo" href="/escape/${SLUG}">Six Clues</a><span id="room"></span><span id="timer" class="timer">60:00</span>
  <span class="btns"><button id="hint">💡 Hint</button><button id="nb">📓 Notebook</button><button id="pause" aria-label="Pause">⏸ Pause</button></span></header>
<div class="stage-wrap"><svg id="stage" viewBox="0 0 1600 900" role="img" aria-label="Escape room scene"></svg></div>
<footer class="dock"><p id="msg" role="status" aria-live="polite"></p><div id="inv" class="inv"></div></footer>
<div id="modal" class="modal" hidden><div class="sheet"><button class="x" aria-label="Close">✕</button><div id="mbody"></div></div></div>
<div id="cover" class="cover" hidden></div>`;
$('modal').querySelector('.x').addEventListener('click', closeModal);
$('modal').addEventListener('click', e => { if (e.target === $('modal')) closeModal(); });
const imgOk = {};
Object.keys(G.rooms).forEach(r => { const im = new Image(); im.onload = () => { imgOk[r] = true; if (S.room === r) render(); }; im.src = IMG + r + '.jpg?v=' + (G.v || 1); });

function render() {
  const R = G.rooms[S.room], ph = imgOk[S.room];
  $('room').textContent = R.name;
  const art = ph ? `<image href="${IMG + S.room}.jpg?v=${G.v || 1}" width="1600" height="900"/>` : R.bg();
  $('stage').innerHTML = `<defs><radialGradient id="lamp"><stop offset="0" stop-color="#ffcf7a" stop-opacity=".22"/><stop offset="1" stop-color="#ffcf7a" stop-opacity="0"/></radialGradient></defs>${art}` +
    R.spots.filter(s => !s.hide || !s.hide()).map(s => { const [x, y, w, h] = ph && s.photo ? s.photo : [s.x, s.y, s.w, s.h];
      return `<g class="hs${ph ? ' photo' : ''}" data-id="${s.id}" tabindex="0" role="button" aria-label="${s.id}">${ph ? '' : s.art()}<rect class="hit" x="${x}" y="${y}" width="${w}" height="${h}" rx="10"/></g>`; }).join('');
  $('stage').querySelectorAll('.hs').forEach(g => {
    const fire = () => clickSpot(R.spots.find(s => s.id === g.dataset.id));
    g.addEventListener('click', fire); g.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); fire(); } });
  });
}
function clickSpot(s) {
  if (!S.started || paused) return;
  if (sel) {
    const fn = s.use && s.use[sel];
    if (!(fn && fn())) say(`The ${G.items[sel][1].toLowerCase()} doesn’t do anything there.`);
    sel = null; renderInv(); render(); save(); return;
  }
  s.act(); render(); dirty = true;
}
function renderInv() {
  $('inv').innerHTML = S.inv.map(i => `<button class="item${sel === i ? ' on' : ''}" data-i="${i}" title="${G.items[i][1]}"><span>${G.items[i][0]}</span><small>${G.items[i][1]}</small></button>`).join('') || '<p class="empty">Your pockets are empty.</p>';
  $('inv').querySelectorAll('.item').forEach(b => b.addEventListener('click', () => {
    const i = b.dataset.i;
    if (sel && sel !== i) { const a = sel; sel = null; if (!(G.combine && G.combine(a, i))) say('Those two don’t go together.'); renderInv(); render(); save(); return; }
    sel = sel === i ? null : i;
    if (sel) say(`${G.items[i][2]} – Tap where to use it, or another item to combine.`);
    renderInv();
  }));
}

/* ---------------- hints ---------------- */
const stage = () => G.stages.find(s => !s[1]());
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
    m.querySelector('#restart').addEventListener('click', () => { if (m.querySelector('#restart').dataset.sure) { post('restart').then(() => location.reload()); } else { m.querySelector('#restart').dataset.sure = 1; m.querySelector('#restart').textContent = 'Sure? Tap again to wipe your progress'; } });
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

function timesUp() {
  const c = $('cover');
  c.innerHTML = `<div class="pausebox"><h2>${G.timesUp[0]}</h2><p>${G.timesUp[1]}</p><p>You can keep playing to finish, but your time won’t go on the leaderboard.</p><button class="btn btn-big" id="cont">Keep going</button> <button class="btn ghost" id="again">Start over</button></div>`;
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
  c.innerHTML = `<div class="pausebox win"><p class="kicker">${G.win[0]}</p><h2>You escaped, ${NAME}!</h2><p>${G.win[1]}</p>
    <p class="big">${S.over ? 'Overtime' : fmt(t) + ' used'}</p><p>${S.hintCount ? S.hintCount + ' hint' + (S.hintCount > 1 ? 's' : '') + ' (time added)' : 'No hints – impressive.'}</p>
    <p><button class="btn btn-big" id="shareEsc">Challenge a friend</button> <a class="btn btn-ghost" href="/escape/${SLUG}">See the leaderboard</a></p><p class="small"><a href="/escape">More escape rooms</a> · <a href="/">Back to Six Clues</a></p></div>`;
  c.hidden = false;
  const url = location.origin + '/escape/' + SLUG + '?src=share', title = document.title.split(' – ')[0];
  const text = `I escaped “${title}” in ${S.over ? 'overtime' : fmt(t)} with ${S.hintCount} hint${S.hintCount === 1 ? '' : 's'} 🔓 Can you beat me?`;
  $('shareEsc').addEventListener('click', () => {
    try { const f = new FormData(); f.append('t', 'challenge_shared'); f.append('r', 'esc-' + SLUG); navigator.sendBeacon('/event', f); } catch (e) {}
    if (navigator.share) navigator.share({ title: 'Six Clues escape room', text, url }).catch(() => {});
    else if (navigator.clipboard) navigator.clipboard.writeText(text + ' ' + url).then(() => { $('shareEsc').textContent = 'Copied – paste it to a friend!'; });
    else prompt('Copy this:', text + ' ' + url);
  });
}
function intro() {
  const c = $('cover'), resume = S.started;
  c.innerHTML = `<div class="pausebox intro"><p class="kicker">${G.intro[0]}</p><h2>${G.intro[1]}</h2>
    ${resume ? `<p>Welcome back. The clock stopped at <b>${fmt(left())}</b> when you left.</p>` : G.intro[2]}
    <button class="btn btn-big" id="go">${resume ? 'Resume' : 'Start the clock'}</button><p class="small">Pause any time with ⏸ – the room is hidden and the clock stops.</p></div>`;
  c.hidden = false;
  c.querySelector('#go').addEventListener('click', () => { S.started = true; last = performance.now(); c.hidden = true; say(resume ? G.rooms[S.room].name + '.' : G.intro[3]); save(); });
}
render(); renderInv(); tick(); intro();
if (S.over) say('Time is up – you can still finish, but off the leaderboard.');
window.__escape = { S: () => S, go, render };
};
})();
