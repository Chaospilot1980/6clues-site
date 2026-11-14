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
})();
