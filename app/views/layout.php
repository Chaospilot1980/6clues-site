<?php
/**
 * $meta keys: title, description, path, noindex (bool), jsonld (array|array[]), og_type
 */
function page_start(array $meta): void {
    $site = cfg('site_name');
    $title = isset($meta['title']) ? $meta['title'] . ' – ' . $site : $site . ' – ' . cfg('tagline');
    $desc = $meta['description'] ?? 'Free printable murder mystery games. Hang six clues around your home, party or office, follow the evidence and scan the code to name the culprit.';
    $canon = url($meta['path'] ?? '/');
    $user = current_user();
    $ga = (string)cfg('ga4_id', '');
    ?><!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title><?= e($title) ?></title>
<meta name="description" content="<?= e($desc) ?>">
<link rel="canonical" href="<?= e($canon) ?>">
<?php if (!empty($meta['noindex'])): ?><meta name="robots" content="noindex, nofollow">
<?php endif; ?>
<meta property="og:site_name" content="<?= e($site) ?>">
<meta property="og:type" content="<?= e($meta['og_type'] ?? 'website') ?>">
<meta property="og:title" content="<?= e($meta['title'] ?? $site) ?>">
<meta property="og:description" content="<?= e($desc) ?>">
<meta property="og:url" content="<?= e($canon) ?>">
<meta property="og:image" content="<?= e(url(($meta['og_image'] ?? null) ?: '/assets/img/og.png')) ?>">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/special-elite-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inter-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css?v=10">
<?php foreach ((array)($meta['jsonld'] ?? []) as $ld): ?>
<script type="application/ld+json"><?= json_encode($ld, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_HEX_TAG) ?></script>
<?php endforeach; ?>
<?php if ($ga): ?>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('consent', 'default', {ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'denied'});
window.GA4_ID = <?= json_encode($ga) ?>;
</script>
<?php endif; ?>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-row">
    <a class="logo" href="/"><span class="logo-mark" aria-hidden="true">6</span> <?= e($site) ?></a>
    <nav aria-label="Main">
      <a href="/#mysteries">Mysteries</a>
      <a href="/game-night">Game Night</a>
      <a href="/escape">Escape rooms</a>
      <a href="/rankings">Rankings</a>
      <a href="/#how">How it works</a>
      <?php if ($user): ?>
        <a href="/me">My cases</a>
        <?php if (is_admin()): ?><a href="/admin">Admin</a><?php endif; ?>
      <?php else: ?>
        <a class="btn btn-small" href="/login?next=<?= e(urlencode($meta['path'] ?? '/')) ?>">Sign in</a>
      <?php endif; ?>
    </nav>
  </div>
</header>
<main id="main">
<?php if ($f = flash()): ?><div class="wrap"><p class="flash" role="status"><?= e($f) ?></p></div><?php endif; ?>
<?php
}

function page_end(): void {
    $ev = $_SESSION['ga_event'] ?? null; unset($_SESSION['ga_event']);
    ?>
</main>
<footer class="site-footer">
  <div class="wrap footer-row">
    <p><strong><?= e(cfg('site_name')) ?></strong> – <?= e(cfg('tagline')) ?>. A new case every day.</p>
    <p><a href="/privacy">Privacy &amp; cookies</a> · <a href="#" data-cookie-settings>Cookie settings</a> · <a href="mailto:<?= e(cfg('contact_email')) ?>">Contact</a></p>
  </div>
</footer>
<?php if (cfg('ga4_id')): ?>
<div class="cookie" id="cookie" hidden>
  <p>We use Google Analytics cookies to see which mysteries people enjoy. No ads, no selling of data. <a href="/privacy">Read more</a></p>
  <div class="cookie-actions">
    <button class="btn btn-ghost" data-consent="denied">Decline</button>
    <button class="btn" data-consent="granted">Accept</button>
  </div>
</div>
<?php endif; ?>
<?php if ($ev): ?><span hidden data-ga-event="<?= e($ev) ?>"></span><?php endif; ?>
<script src="/assets/js/app.js?v=6" defer></script>
</body>
</html>
<?php
}

function badge_row(array $m): string {
    return '<span class="badge lvl lvl' . (int)$m['level'] . '">Level ' . (int)$m['level'] . ' · ' . e(level_name($m['level'])) . '</span> <span class="badge">' . e($m['crime']) . '</span>';
}

function mystery_card(array $m, array $prog = []): string {
    $p = $prog[$m['slug']] ?? null;
    $st = mystery_stats()[$m['slug']] ?? null;
    $show = $st && $st['players'] >= STATS_MIN_PLAYERS;
    $status = ''; $state = 'new';
    if ($p && isset($p['solved_at'])) { $status = !empty($p['gave_up']) ? '<span class="status">Solution revealed</span>' : '<span class="status solved">Solved</span>'; $state = 'done'; }
    elseif ($p) { $status = '<span class="status open">In progress</span>'; $state = 'open'; }
    $meta = '';
    if ($show) $meta = '<p class="card-stats">' . (int)$st['rate'] . '% solved · ' . (int)$st['players'] . ' players'
        . ($st['ratings'] >= 3 ? ' · ★ ' . number_format((float)$st['stars'], 1) : '') . '</p>';
    $data = ' data-level="' . (int)$m['level'] . '" data-crime="' . e(strtolower($m['crime'])) . '" data-state="' . $state . '"'
        . ' data-added="' . e($m['added'] ?? '') . '" data-players="' . ($st['players'] ?? 0) . '"'
        . ' data-rate="' . ($show ? (int)$st['rate'] : -1) . '" data-stars="' . ($st && $st['ratings'] >= 3 ? $st['stars'] : 0) . '"';
    $cv = mystery_cover_url($m['slug']);
    return '<article class="card' . ($cv ? ' has-cover' : '') . '"' . $data . '>' . ($cv ? '<a class="card-cover" href="/mysteries/' . e($m['slug']) . '" tabindex="-1" aria-hidden="true"><img src="' . e($cv) . '" alt="" loading="lazy"></a>' : '') . '<div class="card-top">' . badge_row($m) . $status . '</div>'
        . '<h3><a href="/mysteries/' . e($m['slug']) . '">' . e($m['title']) . '</a></h3>'
        . '<p>' . e($m['teaser']) . '</p>' . $meta . '</article>';
}
