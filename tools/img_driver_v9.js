// window.__queue items: [file, kind(X escape 16:9 | P portrait 1:1 | S cover 4:3), brief]
(() => {
  const ST = { X: 'Painted, cinematic noir illustration in the Six Clues house style. No people, no readable text, no logos. Objects MUST sit exactly where described – players click on those areas. Bottom 25 % quieter floor.',
    P: 'Style: head-and-shoulders portrait in a painterly graphic-novel noir style, muted palette of ink black and warm paper cream with one small deep red detail (NOT a scarf – e.g. a pin, tie, lipstick, flower, piping or nothing at all), plain warm-grey background, soft side light. Make this person clearly different from earlier portraits: choose a believable age for the role (anything from 18 to 85), varied ethnicity, build, face shape, hair (or baldness), glasses or not, and clothing that fits the job and setting exactly. Fictional person, no text.',
    E: 'Style: realistic photograph, slightly faded and grainy like real evidence, natural light for the time of day, same muted noir palette as the rest of the site; fictional people, faces small or turned away, no readable text, numbers or logos.',
    S: 'Style: cinematic, slightly grainy editorial photo-illustration with a film-noir mood; muted palette of ink black, warm paper cream and one deep red accent; fictional, no recognisable real people, no brand logos, no readable text or numbers.' };
  const FMT = { X: '16:9 liggende (1600x900)', P: 'kvadratisk (1024x1024)', S: '4:3 liggende (1600x1200)', E: '4:3 liggende (1024x768)' };
  window.__msg = ([f, k, b]) => `Lav ét billede: ${f}.jpg – ${FMT[k]}. Alt du skal bruge står her; hent ikke noget og spørg ikke – bare generér.\n\n${b}\n\n${ST[k]}\n\nSkriv bagefter præcis: "${f}.jpg er genereret".`;
  for (const k of ['__autoT', '__capT', '__badgeT', '__sendFixT', '__bakT']) if (window[k]) clearInterval(window[k]);
  const busy = () => !!document.querySelector('[data-testid="stop-button"]') || [...document.querySelectorAll('[data-talvt-turn-state]')].some(t => t.dataset.talvtTurnState !== 'complete');
  const bodies = () => [...document.querySelectorAll('[data-talvt-turn-state]')].filter(t => !t.parentElement.closest('[data-talvt-turn-state]'));
  const lastBody = () => bodies().slice(-1)[0];
  const ed = () => document.querySelector('.ProseMirror');
  const sendText = async t => { const e = ed(); if (!e) return false; e.focus(); document.execCommand('selectAll'); document.execCommand('insertText', false, t); await new Promise(r => setTimeout(r, 900)); const b = [...document.querySelectorAll('button[aria-label="Send"], button[aria-label="Send prompt"], [data-testid="send-button"]')].find(x => x.offsetParent && !x.disabled); if (b) { b.click(); return true; } return false; };
  if (!window.__keepAwake) { try { const ac = new AudioContext(), o = ac.createOscillator(), g = ac.createGain(); g.gain.value = 0.0005; o.connect(g); g.connect(ac.destination); o.start(); window.__keepAwake = ac; } catch (e) {} }
  const A = window.__auto = { v: 9, sent: 0, busySince: 0, idleSince: 0, paused: '', tries: 0, cur: '' };
  window.__queue = window.__queue || [];
  window.__autoT = setInterval(async () => {
    if (A.paused) return;
    const now = Date.now();
    if (busy()) { A.idleSince = 0; if (!A.busySince) A.busySince = now; if (now - A.busySince > 12 * 60000) { document.querySelector('[data-testid="stop-button"]')?.click(); A.busySince = 0; } return; }
    A.busySince = 0; if (!A.idleSince) { A.idleSince = now; return; }
    if (now - A.idleSince < 12000) return;
    A.idleSince = 0;
    if (/maksimale længde|maximum length/i.test(document.body.innerText.slice(-3000))) { const nb = document.querySelector('[aria-label="Ny chat"], [aria-label="New chat"]'); if (nb) { nb.click(); A.cur = ''; A.tries = 0; } else A.paused = 'chat full'; return; }
    const lb = lastBody(), txt = lb ? lb.innerText : '';
    if (A.cur && /grænse|limit|kvote|opbrugt|quota|prøv igen senere|try again later/i.test(txt) && !(lb && lb.querySelector('img'))) {
      A.paused = 'limit: ' + txt.slice(-90);
      let ms = 0; const mm = txt.match(/(\d+)\s*minut/i), hh = txt.match(/(\d+)\s*(timer|time|hours?)/i), hm = txt.match(/kl\.?\s*(\d{1,2})[.:](\d{2})/i);
      if (hh || mm) ms = ((hh ? +hh[1] * 60 : 0) + (mm ? +mm[1] : 0) + 2) * 60000;
      else if (hm) { const t = new Date(); t.setHours(+hm[1], +hm[2] + 3, 0, 0); if (t <= new Date()) t.setDate(t.getDate() + 1); ms = t - new Date(); }
      if (ms) { A.resumeAt = new Date(Date.now() + ms).toTimeString().slice(0, 5); clearTimeout(window.__resumeT); window.__resumeT = setTimeout(() => { A.cur = ''; A.tries = 0; A.paused = ''; A.resumeAt = ''; }, ms); }
      return; }
    const Q = window.__queue;
    if (A.cur && Q.length && Q[0][0] === A.cur) {
      if (txt.includes(A.cur) && lb.querySelector('img') && window.__cap && window.__cap.saved.has(A.cur.replace('/', '__'))) { Q.shift(); A.tries = 0; }
      else if (++A.tries >= 3) { (window.__failed = window.__failed || []).push(Q.shift()); A.tries = 0; }
    }
    if (!Q.length) { if ((window.__failed||[]).length) { Q.push(...window.__failed.splice(0)); } else { A.paused = 'queue empty'; return; } }
    A.cur = Q[0][0];
    if (await sendText(window.__msg(Q[0]))) A.sent++;
  }, 4000);
  const saved = new Set(JSON.parse(localStorage.getItem('__6cSaved') || '[]'));
  window.__cap = { saved };
  window.__capT = setInterval(async () => {
    if (busy()) return;
    for (const b of bodies().slice(-4)) {
      const m = b.innerText.match(/([a-z0-9-]+)\/([a-z0-9-]+)\.(?:jpg|png)\s*er genereret/i); if (!m) continue;
      const img = [...b.querySelectorAll('img')].filter(i => i.naturalWidth > 400).slice(-1)[0]; if (!img) continue;
      const key = m[1] + '__' + m[2]; if (saved.has(key)) continue;
      try { const r = await fetch(img.src, { credentials: 'include' }); const bl = await r.blob(); if (bl.size < 50000) continue;
        const a = document.createElement('a'); a.href = URL.createObjectURL(bl); a.download = '6clues__' + key + '.png'; document.body.appendChild(a); a.click(); a.remove();
        saved.add(key); localStorage.setItem('__6cSaved', JSON.stringify([...saved])); } catch (e) {}
    }
  }, 5000);
  window.__bakT = setInterval(() => { try { localStorage.setItem('__q_backup', JSON.stringify([...window.__queue, ...(window.__failed||[])])); } catch (e) {} }, 60000);
  window.__badgeT = setInterval(() => { let s = document.getElementById('__6cbadge'); if (!s) { s = document.createElement('div'); s.id = '__6cbadge'; s.style.cssText = 'position:fixed;top:6px;right:120px;z-index:99999;background:#222;color:#fff;font:12px sans-serif;padding:4px 8px;border-radius:6px'; document.body.appendChild(s); }
    s.textContent = `6clues auto (rør ikke denne fane): ${A.paused ? 'PAUSED (' + A.paused.slice(0, 40) + ')' : 'on'} · queue ${window.__queue.length} · sent ${A.sent} · saved ${saved.size} · failed ${(window.__failed || []).length}`; }, 2000);
})();
