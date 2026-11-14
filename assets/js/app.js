(function () {
  // ---- QR codes on printable posters ----
  if (window.qrcode) {
    document.querySelectorAll('.qr[data-url]').forEach(function (el) {
      var q = qrcode(0, 'M');
      q.addData(el.getAttribute('data-url'));
      q.make();
      el.innerHTML = q.createSvgTag({ cellSize: 3, margin: 0, scalable: true });
    });
  }

  // ---- On-screen game: fit posters and switch clues ----
  var fits = document.querySelectorAll('.poster-fit');
  function fitPosters() {
    fits.forEach(function (f) {
      if (f.hidden) return;
      var s = Math.min(1, f.parentNode.clientWidth / 794);
      var inner = f.querySelector('.poster-inner');
      inner.style.transform = 'scale(' + s + ')';
      f.style.width = (794 * s) + 'px';
      f.style.height = (1123 * s) + 'px';
    });
  }
  if (fits.length) {
    var tabs = document.querySelectorAll('.clue-tab');
    var cur = 0;
    var show = function (n) {
      cur = ((n % fits.length) + fits.length) % fits.length;
      fits.forEach(function (f, i) { f.hidden = i !== cur; });
      document.querySelectorAll('[data-text]').forEach(function (t, i) { t.hidden = i !== cur; });
      tabs.forEach(function (t, i) { t.setAttribute('aria-selected', i === cur ? 'true' : 'false'); if (i === cur) t.classList.add('seen'); });
      fitPosters();
    };
    tabs.forEach(function (t) { t.addEventListener('click', function () { show(+t.getAttribute('data-clue')); }); });
    document.querySelectorAll('[data-step]').forEach(function (b) {
      b.addEventListener('click', function () { show(cur + (+b.getAttribute('data-step'))); document.querySelector('.clue-tabs').scrollIntoView({ behavior: 'smooth', block: 'start' }); });
    });
    window.addEventListener('resize', fitPosters);
    var board = document.querySelector('.board');
    show(+(board && board.getAttribute('data-start') || 0));
  }

  // ---- Google Analytics 4 with consent ----
  var GA = window.GA4_ID;
  var KEY = 'sc_consent';
  function getConsent() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function setConsent(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  var loaded = false;
  function loadGA() {
    if (!GA || loaded) return;
    loaded = true;
    gtag('consent', 'update', { analytics_storage: 'granted' });
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA);
    document.head.appendChild(s);
    gtag('js', new Date());
    gtag('config', GA);
    flushEvents();
  }
  var queue = [];
  function track(name, params) {
    if (!GA) return;
    if (loaded) gtag('event', name, params || {}); else queue.push([name, params]);
  }
  function flushEvents() { queue.forEach(function (e) { gtag('event', e[0], e[1] || {}); }); queue = []; }

  document.querySelectorAll('[data-ga-event]').forEach(function (el) {
    track(el.getAttribute('data-ga-event'), { page_path: location.pathname });
  });
  document.querySelectorAll('[data-ga-click]').forEach(function (el) {
    el.addEventListener('click', function () {
      track(el.getAttribute('data-ga-click'), { mystery: el.getAttribute('data-ga-mystery') || '' });
    });
  });

  var banner = document.getElementById('cookie');
  if (GA && banner) {
    var c = getConsent();
    if (c === 'granted') loadGA();
    else if (!c) banner.hidden = false;
    banner.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-consent]');
      if (!b) return;
      var v = b.getAttribute('data-consent');
      setConsent(v);
      banner.hidden = true;
      if (v === 'granted') loadGA();
    });
  }
  document.querySelectorAll('[data-cookie-settings]').forEach(function (a) {
    a.addEventListener('click', function (ev) {
      ev.preventDefault();
      if (banner) banner.hidden = false;
    });
  });

  // Mystery filters and sorting (home page)
  var form = document.querySelector('[data-filters]'), grid = document.querySelector('[data-grid]');
  if (form && grid) {
    var cards = Array.prototype.slice.call(grid.children), order = cards.slice();
    var params = new URLSearchParams(location.search);
    ['level', 'crime', 'sort'].forEach(function (k) {
      var v = params.get(k); if (!v) return;
      var el = form.querySelector('[name="' + k + '"][value="' + v + '"]') || (k === 'sort' && form.elements.sort);
      if (el && el.type === 'radio') el.checked = true; else if (el) el.value = v;
    });
    var num = function (c, k) { return parseFloat(c.getAttribute('data-' + k)) || 0; };
    var apply = function (track) {
      var f = new FormData(form), lvl = f.get('level') || '', crime = f.get('crime') || '', sort = f.get('sort') || '', hide = !!f.get('hide_done');
      var list = order.slice();
      var cmp = {
        'new': function (a, b) { return (b.getAttribute('data-added') || '').localeCompare(a.getAttribute('data-added') || ''); },
        popular: function (a, b) { return num(b, 'players') - num(a, 'players'); },
        easy: function (a, b) { return num(b, 'rate') - num(a, 'rate'); },
        hard: function (a, b) { var x = num(a, 'rate'), y = num(b, 'rate'); if (x < 0) x = 101; if (y < 0) y = 101; return x - y; },
        stars: function (a, b) { return num(b, 'stars') - num(a, 'stars'); }
      }[sort];
      if (cmp) list.sort(cmp);
      var shown = 0;
      list.forEach(function (c) {
        var ok = (!lvl || c.getAttribute('data-level') === lvl) && (!crime || c.getAttribute('data-crime') === crime) && !(hide && c.getAttribute('data-state') === 'done');
        c.hidden = !ok; if (ok) shown++;
        grid.appendChild(c);
      });
      var cnt = document.querySelector('[data-count]'); if (cnt) cnt.textContent = shown;
      var em = document.querySelector('[data-empty]'); if (em) em.hidden = shown > 0;
      var q = new URLSearchParams(); if (lvl) q.set('level', lvl); if (crime) q.set('crime', crime); if (sort) q.set('sort', sort);
      try { history.replaceState(null, '', location.pathname + (q.toString() ? '?' + q : '') + location.hash); } catch (e) {}
      if (track && window.gtag) gtag('event', 'filter_mysteries', { level: lvl || 'all', crime: crime || 'all', sort: sort || 'default' });
    };
    form.addEventListener('change', function () { apply(true); });
    apply(false);
  }

  // ---- Challenge a friend ----
  document.querySelectorAll('[data-share]').forEach(function (box) {
    var url = box.getAttribute('data-url'), text = box.getAttribute('data-text'), slug = box.getAttribute('data-mystery');
    var native = box.querySelector('[data-share-native]');
    var sent = function (ch) { track('challenge_shared', { method: ch, mystery: slug }); };
    if (native) {
      if (navigator.share) {
        native.addEventListener('click', function () {
          navigator.share({ title: 'Six Clues', text: text, url: url }).then(function () { sent('native'); }).catch(function () {});
        });
      } else native.hidden = true;
    }
    box.querySelectorAll('[data-share-ch]').forEach(function (a) { a.addEventListener('click', function () { sent(a.getAttribute('data-share-ch')); }); });
    var copy = box.querySelector('[data-copy]');
    if (copy) copy.addEventListener('click', function () {
      var done = function () { var o = box.querySelector('[data-copied]'); if (o) o.hidden = false; sent('copy'); };
      if (navigator.clipboard) navigator.clipboard.writeText(text + ' ' + url).then(done, function () { prompt('Copy this link:', url); });
      else { prompt('Copy this link:', url); done(); }
    });
  });
})();
