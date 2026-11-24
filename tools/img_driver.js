/* Six Clues – ChatGPT image driver (v9).
 * Runs inside a chatgpt.com tab (logged in to Dennis' ChatGPT Plus). Generates the missing
 * mystery images one at a time, crops/resizes them to the site's size, saves them as JPG
 * and downloads them as  6c__<case>__<name>.jpg  (plus a copy in IndexedDB "6c"/"img").
 *
 * Start (see tools/IMAGE_CYCLE.md):
 *   1. paste this whole file into the tab's console / javascript tool
 *   2. __6cStart(null, {skipSaved: true})  – reads the missing keys from localStorage.__6c_missing
 *      ("case:name,name;case:name" – python3 tools/img_install.py --missing-compact prints it),
 *      or __6cStart([...keys]) with an explicit array.
 * The tab also keeps a copy of this driver in localStorage.__6c_driver, so after a reload:
 *      (0, eval)(localStorage.__6c_driver); __6cStart(null, {skipSaved: true})
 * The queue comes from localStorage.__q_backup ([key, kind, prompt] rows), filtered to MISSING.
 * State: window.__auto (true while running), __6c.queue / __6c.failed / __6c.log,
 * localStorage.__6cSaved (keys already downloaded), localStorage.__q (current queue).
 */
(() => {
  if (window.__6c && window.__6c.running) { console.log('[6c] already running'); return; }

  const STYLE_P = 'Style: head-and-shoulders portrait in a painterly graphic-novel noir style, muted palette of ink black and warm paper cream with one small deep red detail (NOT a scarf – e.g. a pin, tie, lipstick, flower, piping or nothing at all), plain warm-grey background, soft side light. Make this person clearly different from earlier portraits: choose a believable age for the role (anything from 18 to 85), varied ethnicity, build, face shape, hair (or baldness), glasses or not, and clothing that fits the job and setting exactly. Fictional person, no text.';
  const STYLE_E = 'Style: realistic photograph, slightly faded and grainy like real evidence, natural light for the time of day, same muted noir palette as the rest of the site; fictional people, faces small or turned away, no readable text, numbers or logos.';
  const STYLE_C = 'Style: cinematic, slightly grainy editorial photo-illustration with a film-noir mood; muted palette of ink black, warm paper cream and one deep red accent; fictional, no recognisable real people, no brand logos, no readable text or numbers.';
  const SPEC = {
    P: { w: 1024, h: 1024, max: 400e3, shape: 'kvadratisk (1024x1024)', style: STYLE_P },
    E: { w: 1024, h: 768, max: 300e3, shape: 'liggende 4:3 (1024x768)', style: STYLE_E },
    C: { w: 1600, h: 1200, max: 500e3, shape: 'liggende 4:3 (1600x1200)', style: STYLE_C },
  };
  const BADGE = '🤖 RØR IKKE DENNE FANE – 6c';
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const ls = (k, v) => v === undefined ? JSON.parse(localStorage.getItem(k) || 'null') : localStorage.setItem(k, JSON.stringify(v));
  const S = window.__6c = { running: false, queue: [], failed: [], log: [], current: null, version: 9 };
  const log = m => { const line = new Date().toISOString().slice(11, 19) + ' ' + m; S.log.push(line); if (S.log.length > 300) S.log.shift(); console.log('[6c] ' + line); };

  setInterval(() => { if (document.title !== BADGE) document.title = BADGE; }, 2000);

  function kindOf(row) { return row[0].endsWith('/cover') ? 'C' : (row[1] === 'E' || /\/photo-/.test(row[0]) ? 'E' : 'P'); }

  function promptFor(row) {
    const k = kindOf(row), sp = SPEC[k];
    let p = row[2].replace(/\s*Style:.*$/s, '').trim();
    return `Lav ét billede: ${row[0]}.jpg – ${sp.shape}. Alt du skal bruge står her; hent ikke noget og spørg ikke – bare generér.\n\n${p}\n\n${sp.style}\n\nSkriv bagefter præcis: "${row[0]}.jpg er genereret".`;
  }

  const composer = () => document.querySelector('div.ProseMirror[contenteditable="true"]');
  const btn = label => $$('button[aria-label]').find(b => b.getAttribute('aria-label') === label);
  const busy = () => !!$$('button[aria-label]').find(b => /^(Stop|Stop streaming|Stop generering|Stop med at streame)/i.test(b.getAttribute('aria-label')));

  async function newChat() {
    const b = btn('Ny chat') || btn('New chat');
    if (b) b.click(); else history.pushState({}, '', '/');
    for (let i = 0; i < 30; i++) { await sleep(500); const c = composer(); if (c && location.pathname === '/' && !$$('img').some(x => x.offsetParent !== null && /^(Genereret billede|Generated image)/i.test(x.alt || ''))) return c; }
    throw new Error('new chat did not open');
  }

  async function send(text) {
    const c = composer(); c.focus();
    document.execCommand('selectAll'); document.execCommand('delete');
    const dt = new DataTransfer(); dt.setData('text/plain', text);
    c.dispatchEvent(new ClipboardEvent('paste', { clipboardData: dt, bubbles: true, cancelable: true }));
    await sleep(700);
    if (!c.innerText.includes(text.slice(0, 30))) { document.execCommand('insertText', false, text); await sleep(500); }
    for (let i = 0; i < 20; i++) { const s = btn('Send') || btn('Send prompt') || document.querySelector('[data-testid="send-button"]'); if (s && !s.disabled) { s.click(); return; } await sleep(500); }
    throw new Error('send button not found');
  }

  // ChatGPT has several <main> elements and no role attributes any more: look at the whole page.
  // Each image gets its own fresh chat, so the only large visible generated image is ours (old chats stay in the DOM, hidden).
  function resultImage() {
    const imgs = $$('img').filter(i => i.complete && i.naturalWidth >= 512 && i.offsetParent !== null && (/^(Genereret billede|Generated image)/i.test(i.alt || '') || !/avatar|profile/i.test(i.src)));
    return imgs.sort((a, b) => b.naturalWidth * b.naturalHeight - a.naturalWidth * a.naturalHeight)[0] || null;
  }

  async function waitImage() {
    const t0 = Date.now(); let lastSrc = null, stable = 0;
    while (Date.now() - t0 < 8 * 60e3) {
      await sleep(4000);
      const txt = document.body.innerText;
      if (/grænse for billed|image generation limit|nået din grænse|reached your limit|try again (later|in)|prøv igen (senere|om)/i.test(txt.slice(-1500))) throw Object.assign(new Error('rate limit'), { limit: true });
      const im = resultImage();
      if (im && !busy()) { if (im.src === lastSrc) { if (++stable >= 2) return im; } else { lastSrc = im.src; stable = 0; } }
    }
    throw new Error('timeout waiting for image');
  }

  async function toJpeg(img, k) {
    const sp = SPEC[k];
    const blob = await (await fetch(img.src, { credentials: 'include' })).blob();
    const bmp = await createImageBitmap(blob);
    const cv = document.createElement('canvas'); cv.width = sp.w; cv.height = sp.h;
    const g = cv.getContext('2d');
    const s = Math.max(sp.w / bmp.width, sp.h / bmp.height), dw = bmp.width * s, dh = bmp.height * s;
    g.drawImage(bmp, (sp.w - dw) / 2, (sp.h - dh) / 2, dw, dh);
    for (let q = 0.82; q >= 0.5; q -= 0.06) {
      const out = await new Promise(r => cv.toBlob(r, 'image/jpeg', q));
      if (out.size <= sp.max || q < 0.56) return out;
    }
  }

  function idb() {
    return new Promise((res, rej) => { const r = indexedDB.open('6c', 1); r.onupgradeneeded = () => r.result.createObjectStore('img'); r.onsuccess = () => res(r.result); r.onerror = () => rej(r.error); });
  }
  async function idbPut(key, blob) { const db = await idb(); await new Promise((res, rej) => { const tx = db.transaction('img', 'readwrite'); tx.objectStore('img').put(blob, key); tx.oncomplete = res; tx.onerror = () => rej(tx.error); }); }
  window.__6cGet = async key => { const db = await idb(); return new Promise(res => { const r = db.transaction('img').objectStore('img').get(key); r.onsuccess = () => res(r.result); }); };
  window.__6cKeys = async () => { const db = await idb(); return new Promise(res => { const r = db.transaction('img').objectStore('img').getAllKeys(); r.onsuccess = () => res(r.result); }); };
  window.__6cB64 = async key => { const b = await window.__6cGet(key); if (!b) return null; const a = new Uint8Array(await b.arrayBuffer()); let s = ''; for (let i = 0; i < a.length; i += 0x8000) s += String.fromCharCode(...a.subarray(i, i + 0x8000)); return btoa(s); };

  function download(key, blob) {
    const a = document.createElement('a'); a.href = URL.createObjectURL(blob);
    a.download = '6c__' + key.replace('/', '__') + '.jpg'; document.body.appendChild(a); a.click();
    setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 5000);
  }

  async function one(row) {
    const k = kindOf(row);
    S.current = row[0]; log('start ' + row[0] + ' (' + k + ')');
    await newChat();
    await send(promptFor(row));
    const im = await waitImage();
    const jpg = await toJpeg(im, k);
    await idbPut(row[0], jpg);
    download(row[0], jpg);
    const saved = new Set(ls('__6cSaved') || []); saved.add(row[0].replace('/', '__')); ls('__6cSaved', [...saved]);
    log('done ' + row[0] + ' ' + Math.round(jpg.size / 1024) + ' KB');
  }

  async function loop() {
    S.running = window.__auto = true;
    while (S.running && S.queue.length) {
      const row = S.queue[0];
      try { await one(row); S.queue.shift(); }
      catch (e) {
        log('FAIL ' + row[0] + ': ' + e.message);
        if (e.limit) { log('rate limit – pausing 45 min'); await sleep(45 * 60e3); continue; }
        S.queue.shift(); row.tries = (row.tries || 0) + 1;
        if (row.tries < 3) S.queue.push(row); else S.failed.push(row);
      }
      ls('__q', S.queue);
      S.current = null;
      if (S.queue.length) await sleep(20e3 + Math.random() * 20e3);
    }
    S.running = window.__auto = false; log('stopped; left ' + S.queue.length + ', failed ' + S.failed.length);
  }

  window.__6cStart = (missing, opts = {}) => {
    if (!missing) missing = (localStorage.getItem('__6c_missing') || '').split(';').filter(Boolean).flatMap(g => { const [c, n] = g.split(':'); return n.split(',').map(x => c + '/' + x); });
    const want = new Set(missing);
    const src = ls('__q_backup') || [];
    const have = new Set(src.map(r => r[0]));
    S.queue = src.filter(r => want.has(r[0]));
    (opts.extra || []).forEach(r => { if (!have.has(r[0]) && want.has(r[0])) S.queue.push(r); });
    if (opts.skipSaved) { const sv = new Set(ls('__6cSaved') || []); S.queue = S.queue.filter(r => !sv.has(r[0].replace('/', '__'))); }
    if (opts.limit) S.queue = S.queue.slice(0, opts.limit);
    ls('__q', S.queue); log('queue ' + S.queue.length + ' of ' + missing.length + ' missing');
    loop();
    return S.queue.length;
  };
  // Recovery: save the image currently shown on the page under KEY (e.g. after a reload mid-generation).
  window.__6cGrab = async key => {
    const im = resultImage(); if (!im) return 'no image on page';
    const k = kindOf([key, /\/photo-/.test(key) ? 'E' : 'P']); const jpg = await toJpeg(im, k);
    await idbPut(key, jpg); download(key, jpg);
    const saved = new Set(ls('__6cSaved') || []); saved.add(key.replace('/', '__')); ls('__6cSaved', [...saved]);
    S.queue = S.queue.filter(r => r[0] !== key); ls('__q', S.queue);
    return 'saved ' + key + ' ' + Math.round(jpg.size / 1024) + ' KB';
  };
  window.__6cStop = () => { S.running = false; return 'stopping after current image'; };
  window.__6cRequeue = () => { S.queue.push(...S.failed.map(r => (r.tries = 0, r))); S.failed = []; if (!S.running) loop(); return S.queue.length; };
  window.__6cStatus = () => ({ running: S.running, current: S.current, left: S.queue.length, failed: S.failed.map(r => r[0]), log: S.log.slice(-8) });
  log('driver v9 loaded');
})();
