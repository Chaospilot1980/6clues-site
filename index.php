<?php
declare(strict_types=1);
require __DIR__ . '/app/bootstrap.php';
require __DIR__ . '/app/views/layout.php';

$path = parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH) ?: '/';
$path = '/' . trim(rawurldecode($path), '/');
$method = $_SERVER['REQUEST_METHOD'] ?? 'GET';

// Remember where a visitor came from (QR code, campaign) for the sign-up record
if (!empty($_GET['src'])) $_SESSION['source'] = substr(preg_replace('/[^a-z0-9_\-]/i', '', (string)$_GET['src']), 0, 50);

$routes = [
    '#^/$#'                                   => 'home',
    '#^/mysteries/([a-z0-9\-]+)$#'            => 'show',
    '#^/mysteries/([a-z0-9\-]+)/play$#'       => 'play',
    '#^/mysteries/([a-z0-9\-]+)/print$#'      => 'print_page',
    '#^/answer/([a-z0-9\-]+)$#'               => 'answer',
    '#^/login$#'                              => 'login',
    '#^/auth/google$#'                        => 'auth_google',
    '#^/auth/dev$#'                           => 'auth_dev',
    '#^/auth/email$#'                         => 'auth_email',
    '#^/auth/verify$#'                        => 'auth_verify',
    '#^/logout$#'                             => 'logout',
    '#^/me$#'                                 => 'me',
    '#^/rankings$#'                           => 'rankings',
    '#^/me/leaderboard$#'                     => 'leaderboard_optin',
    '#^/admin$#'                              => 'admin',
    '#^/admin/subscribers\.csv$#'             => 'admin_csv',
    '#^/admin/newsletter$#'                   => 'admin_newsletter',
    '#^/unsubscribe$#'                        => 'unsubscribe',
    '#^/cron/deploy$#'                        => 'cron_deploy',
    '#^/review/([a-z0-9\-]+)$#'              => 'review',
    '#^/admin/reviews$#'                      => 'admin_reviews',
    '#^/privacy$#'                            => 'privacy',
    '#^/sitemap\.xml$#'                       => 'sitemap',
    '#^/robots\.txt$#'                        => 'robots',
];
foreach ($routes as $re => $fn) {
    if (preg_match($re, $path, $mm)) { $fn(...array_slice($mm, 1)); exit; }
}
not_found();

// =====================================================================

function not_found(): void {
    http_response_code(404);
    page_start(['title' => 'Case not found', 'noindex' => true, 'path' => '/404']);
    echo '<section class="wrap narrow"><h1>Case not found</h1><p>This page has vanished without a trace.</p><p><a class="btn" href="/">Back to all mysteries</a></p></section>';
    page_end();
}

function need_mystery(string $slug): array {
    $m = mystery($slug);
    if (!$m) { not_found(); exit; }
    return $m;
}

function home(): void {
    $u = current_user();
    $prog = $u ? user_progress((int)$u['id']) : [];
    $site = cfg('site_name');
    page_start(['path' => '/', 'jsonld' => [
        ['@context' => 'https://schema.org', '@type' => 'WebSite', 'name' => $site, 'url' => url('/')],
        ['@context' => 'https://schema.org', '@type' => 'ItemList', 'name' => 'Murder mystery games',
         'itemListElement' => array_map(fn($m, $i) => ['@type' => 'ListItem', 'position' => $i + 1, 'url' => url('/mysteries/' . $m['slug']), 'name' => $m['title']], mysteries(), array_keys(mysteries()))],
    ]]);
    ?>
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="kicker">Case files · free to play</p>
      <h1>Free printable murder mysteries for parties, families and offices</h1>
      <p class="lead">Print six clue posters, hide them around the house, garden or office, and let your guests hunt for evidence. When they think they know who did it, they scan the code and name the culprit.</p>
      <p class="cta-row"><a class="btn" href="#mysteries">Pick a mystery</a> <a class="btn btn-ghost" href="#how">How it works</a></p>
    </div>
    <div class="hero-card" aria-hidden="true">
      <div class="stamp">CLUE<br><b>3</b><br>OF 6</div>
      <p class="type">”I saw her take two glasses from the kitchen – red nail polish, a gold bracelet…”</p>
      <p class="small">WITNESS STATEMENT · MARCO RUIZ</p>
    </div>
  </div>
</section>

<section id="how" class="wrap steps">
  <h2>How it works</h2>
  <ol class="step-list">
    <li><b>Choose a case.</b> Level 1 is perfect for a first game; level 3 will fool most grown-up detectives.</li>
    <li><b>Print and hide six posters – or play on screen.</b> On paper, hide the clues around the house, garden or office. On screen, flip through the same six posters on your phone, tablet or TV. Each one has a witness, a statement and a piece of evidence.</li>
    <li><b>Compare the clues.</b> Times, alibis and small details only make sense when you put them together.</li>
    <li><b>Scan the code and name the culprit.</b> Sign in with Google or your email to submit your answer, see the solution and keep track of the cases you've cracked.</li>
  </ol>
</section>

<section id="mysteries" class="wrap">
  <h2>All mysteries <span class="count" data-count><?= count(mysteries()) ?></span></h2>
  <?php filter_bar((bool)$u); ?>
  <div class="grid" data-grid>
    <?php foreach (mysteries() as $m) echo mystery_card($m, $prog); ?>
  </div>
  <p class="empty" data-empty hidden>No cases match – try another filter.</p>
  <p class="small"><a href="/rankings">See the rankings: hardest cases and top detectives →</a></p>
</section>

<?php $rv = reviews(null, 3, 4); if ($rv): ?>
<section class="wrap"><h2>What detectives say</h2><?= render_reviews($rv) ?></section>
<?php endif; ?>

<section class="wrap newsletter-box">
  <h2>New cases every month</h2>
  <p>Sign in once with Google or your email to save your progress. Tick the box when you submit an answer, and we'll email you when a new mystery is released.</p>
  <?php if (!$u): ?><p><a class="btn" href="/login?next=/me">Sign in</a></p><?php endif; ?>
</section>
<?php
    page_end();
}

function show(string $slug): void {
    $m = need_mystery($slug);
    $u = current_user();
    $prog = $u ? user_progress((int)$u['id']) : [];
    $p = $prog[$slug] ?? null;
    page_start([
        'title' => $m['title'] . ' – free printable mystery game',
        'description' => $m['teaser'] . ' A free level ' . $m['level'] . ' ' . strtolower($m['crime']) . ' mystery with six printable clue posters.',
        'path' => '/mysteries/' . $slug, 'og_type' => 'article',
        'jsonld' => [
            ['@context' => 'https://schema.org', '@type' => 'Game', 'name' => $m['title'], 'description' => $m['teaser'],
             'url' => url('/mysteries/' . $slug), 'genre' => 'Murder mystery', 'numberOfPlayers' => ['@type' => 'QuantitativeValue', 'minValue' => 1],
             'isAccessibleForFree' => true, 'inLanguage' => 'en', 'publisher' => ['@type' => 'Organization', 'name' => cfg('site_name')]],
            ['@context' => 'https://schema.org', '@type' => 'BreadcrumbList', 'itemListElement' => [
                ['@type' => 'ListItem', 'position' => 1, 'name' => 'Mysteries', 'item' => url('/')],
                ['@type' => 'ListItem', 'position' => 2, 'name' => $m['title'], 'item' => url('/mysteries/' . $slug)]]],
        ],
    ]);
    ?>
<section class="wrap case">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Mysteries</a> › <?= e($m['title']) ?></nav>
  <p><?= badge_row($m) ?></p>
  <h1><?= e($m['title']) ?></h1>
  <p class="lead"><?= e($m['teaser']) ?></p>
  <div class="briefing"><?= $m['intro'] ?></div>
  <?php if ($p && isset($p['solved_at'])): ?>
    <p class="flash">You've closed this case. <a href="/answer/<?= e($slug) ?>">See the solution</a></p>
  <?php endif; ?>
  <div class="choices">
    <a class="choice" href="/mysteries/<?= e($slug) ?>/print" data-ga-click="print_posters" data-ga-mystery="<?= e($slug) ?>">
      <b>Print the six posters</b><span>A4 or A3, with a QR code on every poster. Hide them in six places.</span></a>
    <a class="choice" href="/mysteries/<?= e($slug) ?>/play" data-ga-click="play_online" data-ga-mystery="<?= e($slug) ?>">
      <b>Play on screen</b><span>Flip through the six clue posters on your phone, tablet or TV – no printer needed.</span></a>
    <a class="choice" href="/answer/<?= e($slug) ?>">
      <b>Name the <?= e($m['who']) ?></b><span>Ready? Submit your answer and see the solution.</span></a>
  </div>
  <h2>The suspects</h2>
  <ul class="suspects">
    <?php foreach ($m['suspects'] as $s): ?><li><b><?= e($s['name']) ?></b><span><?= e($s['role']) ?></span></li><?php endforeach; ?>
  </ul>
  <h2>Hosting tips</h2>
  <ul class="tips">
    <li>Number the hiding places, or write a little hint to the next spot in the box at the bottom of each poster.</li>
    <li>Works for 2–30 players. Let teams compete, or play as one big detective squad.</li>
    <li>Allow 30–60 minutes for level 1 and up to 90 minutes for level 3.</li>
  </ul>
  <?php $rv = reviews($slug, 6); if ($rv): ?><h2>Player reviews</h2><?= render_reviews($rv) ?><?php endif; ?>
</section>
<?php
    page_end();
}

function play(string $slug): void {
    $m = need_mystery($slug);
    $answer = url('/answer/' . $slug . '?src=screen');
    page_start(['title' => $m['title'] . ' – play online', 'description' => 'Play ' . $m['title'] . ' on screen: flip through all six clue posters and work out who did it.', 'path' => '/mysteries/' . $slug . '/play']);
    ?>
<section class="wrap case play">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Mysteries</a> › <a href="/mysteries/<?= e($slug) ?>"><?= e($m['title']) ?></a> › Play on screen</nav>
  <div class="play-head">
    <h1><?= e($m['title']) ?></h1>
    <a class="btn" href="/answer/<?= e($slug) ?>">I know who did it</a>
  </div>
  <div class="clue-tabs" role="tablist" aria-label="Clues">
    <?php foreach ($m['clues'] as $i => $c): ?>
      <button role="tab" class="clue-tab" data-clue="<?= $i ?>" aria-selected="<?= $i === 0 ? 'true' : 'false' ?>"><b><?= $i + 1 ?></b><span><?= e($c['name']) ?></span></button>
    <?php endforeach; ?>
  </div>
  <div class="board">
    <?php foreach ($m['clues'] as $i => $c): ?>
      <div class="poster-fit" data-poster="<?= $i ?>" <?= $i ? 'hidden' : '' ?>><div class="poster-inner"><?= str_replace('{{ANSWER_URL}}', e($answer), $c['poster']) ?></div></div>
    <?php endforeach; ?>
  </div>
  <div class="play-nav">
    <button class="btn btn-ghost" data-step="-1">‹ Previous clue</button>
    <button class="btn btn-ghost" data-step="1">Next clue ›</button>
  </div>
  <details class="text-version">
    <summary>Read the clues as plain text</summary>
    <?php foreach ($m['clues'] as $i => $c): ?>
      <article class="clue"><header><span class="clue-no">Clue <?= $i + 1 ?> of 6</span><h2><?= e($c['name']) ?> <small><?= e($c['role']) ?></small></h2></header>
      <blockquote>”<?= e($c['quote']) ?>”</blockquote><p class="ev-label">Evidence #<?= $i + 1 ?> · <?= e($c['label']) ?></p><div class="evidence"><?= $c['evidence'] ?></div></article>
    <?php endforeach; ?>
  </details>
</section>
<script src="/assets/js/qrcode.js"></script>
<?php
    page_end();
}

function print_page(string $slug): void {
    $m = need_mystery($slug);
    $answer = url('/answer/' . $slug . '?src=qr');
    ?><!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title><?= e($m['title']) ?> – printable posters</title>
<meta name="robots" content="noindex">
<link rel="stylesheet" href="/assets/css/print.css?v=1">
</head><body>
<div class="toolbar">
  <p><b><?= e($m['title']) ?></b> – six A4 posters. Use your browser's print dialog: A4, margins <i>None</i>, scale 100% (or “Fit to page” for A3).</p>
  <button onclick="window.print()">Print posters</button>
</div>
<?php foreach ($m['clues'] as $c): ?>
<div class="sheet"><?= str_replace('{{ANSWER_URL}}', e($answer), $c['poster']) ?></div>
<?php endforeach; ?>
<script src="/assets/js/qrcode.js"></script>
<script src="/assets/js/app.js?v=2"></script>
</body></html>
<?php
}

function login(): void {
    $next = (string)($_GET['next'] ?? '/me');
    if (!preg_match('#^/[a-z0-9/\-]*$#i', $next)) $next = '/me';
    if (current_user()) redirect($next);
    page_start(['title' => 'Sign in', 'noindex' => true, 'path' => '/login']);
    echo '<section class="wrap narrow"><h1>Sign in</h1><p>Sign in to submit answers and keep track of the cases you have solved – with Google or just your email.</p>';
    google_button($next);
    echo '</section>';
    page_end();
}

function google_button(string $next): void {
    $cid = (string)cfg('google_client_id');
    ?>
<div class="login-box">
<?php if ($cid): ?>
<form id="g-form" method="post" action="/auth/google"><?= csrf_field() ?><input type="hidden" name="credential" id="g-credential"><input type="hidden" name="next" value="<?= e($next) ?>"></form>
<div id="g_id_onload" data-client_id="<?= e($cid) ?>" data-callback="onGoogleSignIn" data-auto_prompt="false"></div>
<div class="g_id_signin" data-type="standard" data-size="large" data-theme="filled_black" data-text="continue_with" data-shape="rectangular"></div>
<script>function onGoogleSignIn(r){document.getElementById('g-credential').value=r.credential;document.getElementById('g-form').submit();}</script>
<script src="https://accounts.google.com/gsi/client" async></script>
<p class="or"><span>or use your email</span></p>
<?php endif; ?>
<form method="post" action="/auth/email" class="email-login">
  <?= csrf_field() ?><input type="hidden" name="next" value="<?= e($next) ?>">
  <label>Your name <input name="name" autocomplete="name" required maxlength="80"></label>
  <label>Email <input type="email" name="email" autocomplete="email" required maxlength="190"></label>
  <label class="check"><input type="checkbox" name="newsletter" value="1"> Email me when a new mystery is released (about once a month).</label>
  <button class="btn">Send me a sign-in link</button>
  <p class="small muted">No password needed – we email you a link that signs you in.</p>
</form>
</div>
<?php if (cfg('dev_login')): ?>
<form method="post" action="/auth/dev" class="dev"><?= csrf_field() ?><input type="hidden" name="next" value="<?= e($next) ?>"><input name="email" value="tester@example.com" aria-label="Test email"><button class="btn btn-small">Dev login</button></form>
<?php endif;
}

function safe_next(string $n): string { return preg_match('#^/[a-z0-9/\-]*$#i', $n) ? $n : '/me'; }

function auth_email(): void {
    if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') redirect('/login');
    csrf_check();
    $next = safe_next((string)($_POST['next'] ?? '/me'));
    $email = trim((string)($_POST['email'] ?? ''));
    $name = trim(mb_substr((string)($_POST['name'] ?? ''), 0, 80));
    if (!filter_var($email, FILTER_VALIDATE_EMAIL) || $name === '') { flash('Please enter your name and a valid email address.'); redirect('/login?next=' . urlencode($next)); }
    $last = $_SESSION['last_link'] ?? 0;
    if (time() - $last < 30) { flash('We just sent you a link – please check your inbox (and spam folder).'); redirect('/login?next=' . urlencode($next)); }
    $_SESSION['last_link'] = time();
    $ok = send_login_link($email, $name, !empty($_POST['newsletter']), $next);
    page_start(['title' => 'Check your email', 'noindex' => true, 'path' => '/auth/email']);
    echo '<section class="wrap narrow"><h1>Check your email</h1>';
    echo $ok ? '<p class="lead">We sent a sign-in link to <b>' . e($email) . '</b>. Click it within an hour to continue. Can\'t find it? Check your spam folder.</p>'
             : '<p class="lead">Sorry, we could not send the email right now. Please try again in a moment, or continue with Google.</p>';
    echo '</section>';
    page_end();
}

function auth_verify(): void {
    $t = (string)($_GET['t'] ?? '');
    $st = db()->prepare('SELECT * FROM login_tokens WHERE token_hash = ? AND expires_at >= ?');
    $st->execute([hash('sha256', $t), now()]);
    $row = $st->fetch();
    if (!$row) { flash('That sign-in link has expired or was already used. Please request a new one.'); redirect('/login'); }
    db()->prepare('DELETE FROM login_tokens WHERE token_hash = ?')->execute([$row['token_hash']]);
    login_user(['sub' => 'email:' . strtolower($row['email']), 'email' => $row['email'], 'name' => $row['name']]);
    if ((int)$row['newsletter']) db()->prepare('UPDATE users SET newsletter = 1, newsletter_at = COALESCE(newsletter_at, ?) WHERE id = ?')->execute([now(), $_SESSION['uid']]);
    redirect(safe_next((string)$row['next_path']));
}

function auth_google(): void {
    if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') redirect('/login');
    csrf_check();
    $next = (string)($_POST['next'] ?? '/me');
    if (!preg_match('#^/[a-z0-9/\-]*$#i', $next)) $next = '/me';
    $p = verify_google_token((string)($_POST['credential'] ?? ''));
    if (!$p) { flash('Google sign-in failed. Please try again.'); redirect('/login?next=' . urlencode($next)); }
    login_user($p);
    redirect($next);
}

function auth_dev(): void {
    if (!cfg('dev_login') || ($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') { not_found(); return; }
    csrf_check();
    $email = (string)($_POST['email'] ?? 'tester@example.com');
    login_user(['sub' => 'dev-' . md5($email), 'email' => $email, 'name' => 'Test Detective']);
    redirect((string)($_POST['next'] ?? '/me'));
}

function logout(): void {
    if (($_SERVER['REQUEST_METHOD'] ?? '') === 'POST') { csrf_check(); $_SESSION = []; session_regenerate_id(true); }
    redirect('/');
}

function answer(string $slug): void {
    $m = need_mystery($slug);
    $u = current_user();
    $meta = ['title' => 'Name the ' . $m['who'] . ' – ' . $m['title'], 'noindex' => true, 'path' => '/answer/' . $slug];
    if (!$u) {
        page_start($meta);
        echo '<section class="wrap narrow case"><p>' . badge_row($m) . '</p><h1>' . e($m['title']) . '</h1>';
        echo '<p class="lead">Think you know who did it? Sign in to submit your answer, see the full solution and save your progress.</p>';
        google_button('/answer/' . $slug);
        echo '<p class="small muted">We only use your name and email address. See our <a href="/privacy">privacy policy</a>.</p></section>';
        page_end();
        return;
    }
    $uid = (int)$u['id'];
    $pdo = db();
    $result = null;
    if (($_SERVER['REQUEST_METHOD'] ?? '') === 'POST') {
        csrf_check();
        if (!empty($_POST['newsletter']) && !(int)$u['newsletter']) {
            $pdo->prepare('UPDATE users SET newsletter = 1, newsletter_at = ? WHERE id = ?')->execute([now(), $uid]);
            $u['newsletter'] = 1;
        }
        $st = $pdo->prepare('SELECT COUNT(*) FROM attempts WHERE user_id = ? AND slug = ?');
        $st->execute([$uid, $slug]);
        $tries = (int)$st->fetchColumn();
        $st = $pdo->prepare('SELECT 1 FROM solves WHERE user_id = ? AND slug = ?');
        $st->execute([$uid, $slug]);
        $done = (bool)$st->fetchColumn();
        if (($_POST['action'] ?? '') === 'reveal') {
            if (!$done) $pdo->prepare('INSERT INTO solves (user_id, slug, solved_at, attempts, gave_up) VALUES (?,?,?,?,1)')->execute([$uid, $slug, now(), $tries]);
            $_SESSION['ga_event'] = 'solution_revealed';
        } else {
            $guess = (string)($_POST['guess'] ?? '');
            $names = array_column($m['suspects'], 'name');
            if (!in_array($guess, $names, true)) { flash('Pick one of the suspects.'); redirect('/answer/' . $slug); }
            $ok = $guess === $m['solution']['killer'];
            $pdo->prepare('INSERT INTO attempts (user_id, slug, guess, correct, created_at) VALUES (?,?,?,?,?)')->execute([$uid, $slug, $guess, $ok ? 1 : 0, now()]);
            if ($ok && !$done) $pdo->prepare('INSERT INTO solves (user_id, slug, solved_at, attempts, gave_up) VALUES (?,?,?,?,0)')->execute([$uid, $slug, now(), $tries + 1]);
            $_SESSION['ga_event'] = $ok ? 'mystery_solved' : 'wrong_answer';
            $_SESSION['last_result'] = ['slug' => $slug, 'ok' => $ok, 'guess' => $guess];
        }
        redirect('/answer/' . $slug);
    }
    $res = $_SESSION['last_result'] ?? null;
    if ($res && $res['slug'] === $slug) unset($_SESSION['last_result']); else $res = null;
    $prog = user_progress($uid);
    $closed = isset($prog[$slug]['solved_at']);
    page_start($meta);
    ?>
<section class="wrap narrow case">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Mysteries</a> › <a href="/mysteries/<?= e($slug) ?>"><?= e($m['title']) ?></a> › Answer</nav>
  <h1><?= e($m['title']) ?></h1>
  <?php if ($res && !$res['ok']): ?>
    <div class="verdict wrong" role="alert"><b>Not quite.</b> <?= e($res['guess']) ?> has an alibi – look at the clues again. Times and small details matter.</div>
  <?php endif; ?>
  <?php if ($closed): $s = $m['solution']; $gaveUp = !empty($prog[$slug]['gave_up']); ?>
    <div class="verdict <?= $gaveUp ? '' : 'right' ?>"><?= $gaveUp ? '<b>Case closed.</b> Here is how it happened.' : '<b>Case solved!</b> Brilliant detective work.' ?></div>
    <div class="solution">
      <h2>The <?= e($m['who']) ?> is <?= e($s['killer']) ?></h2>
      <h3>Motive</h3><p><?= $s['motive'] ?></p>
      <h3>How the evidence gives it away</h3><ol><?php foreach ($s['proof'] as $x) echo "<li>$x</li>"; ?></ol>
      <h3>Why the others are innocent</h3><ul><?php foreach ($s['cleared'] as $x) echo "<li>$x</li>"; ?></ul>
    </div>
    <?php review_form($uid, $slug); ?>
    <?php next_cases($u, $slug); ?>
  <?php else: ?>
    <form method="post" class="answer-form">
      <?= csrf_field() ?>
      <fieldset>
        <legend>Who is the <?= e($m['who']) ?>?</legend>
        <div class="suspect-pick">
        <?php foreach ($m['suspects'] as $i => $s): ?>
          <label><input type="radio" name="guess" value="<?= e($s['name']) ?>" required> <b><?= e($s['name']) ?></b> <span><?= e($s['role']) ?></span></label>
        <?php endforeach; ?>
        </div>
      </fieldset>
      <?php if (!(int)$u['newsletter']): ?>
        <label class="check"><input type="checkbox" name="newsletter" value="1"> Email me when a new mystery is released (about once a month – unsubscribe any time).</label>
      <?php endif; ?>
      <button class="btn btn-big">Accuse!</button>
    </form>
    <form method="post" class="reveal" onsubmit="return confirm('Show the solution? This closes the case without solving it.');">
      <?= csrf_field() ?><input type="hidden" name="action" value="reveal"><button class="linkbtn">I give up – show me the solution</button>
    </form>
  <?php endif; ?>
</section>
<?php
    page_end();
}

function next_cases(?array $u, string $except = ''): void {
    $s = suggestions($u, 3, $except);
    if (!$s) { echo '<p class="flash">You have solved every case so far – new mysteries are on the way.</p>'; return; }
    echo '<h2>Your next case</h2><div class="grid">';
    foreach ($s as $m) echo mystery_card($m);
    echo '</div>';
}

function me(): void {
    $u = current_user();
    if (!$u) redirect('/login?next=/me');
    $prog = user_progress((int)$u['id']);
    $solved = count(array_filter($prog, fn($p) => isset($p['solved_at']) && empty($p['gave_up'])));
    page_start(['title' => 'My cases', 'noindex' => true, 'path' => '/me']);
    ?>
<section class="wrap case">
  <h1>Detective <?= e($u['name'] ?: $u['email']) ?></h1>
  <p class="lead"><?= $solved ?> of <?= count(mysteries()) ?> cases solved.</p>
  <div class="progress" role="img" aria-label="<?= $solved ?> of <?= count(mysteries()) ?> solved"><span style="width: <?= round($solved / max(1, count(mysteries())) * 100) ?>%"></span></div>
  <p><a href="/rankings">See where you rank among other detectives →</a></p>
  <?php next_cases($u); ?>
  <h2>All cases</h2>
  <div class="grid"><?php foreach (mysteries() as $m) echo mystery_card($m, $prog); ?></div>
  <h2>Account</h2>
  <p>Signed in as <?= e($u['email']) ?>. New-mystery emails: <b><?= (int)$u['newsletter'] ? 'on' : 'off' ?></b>.</p>
  <form method="post" action="/logout"><?= csrf_field() ?><button class="btn btn-ghost">Sign out</button></form>
</section>
<?php
    page_end();
}

function admin(): void {
    if (!is_admin()) { not_found(); return; }
    $pdo = db();
    $users = (int)$pdo->query('SELECT COUNT(*) FROM users')->fetchColumn();
    $subs = (int)$pdo->query('SELECT COUNT(*) FROM users WHERE newsletter = 1')->fetchColumn();
    $week = $pdo->prepare('SELECT COUNT(*) FROM users WHERE created_at >= ?');
    $week->execute([gmdate('Y-m-d H:i:s', time() - 7 * 86400)]);
    $rows = $pdo->query('SELECT slug, COUNT(*) total, SUM(CASE WHEN gave_up = 0 THEN 1 ELSE 0 END) solved, AVG(attempts) avg_attempts FROM solves GROUP BY slug')->fetchAll();
    $by = []; foreach ($rows as $r) $by[$r['slug']] = $r;
    $att = []; foreach ($pdo->query('SELECT slug, COUNT(DISTINCT user_id) players FROM attempts GROUP BY slug')->fetchAll() as $r) $att[$r['slug']] = $r['players'];
    $src = $pdo->query("SELECT source, COUNT(*) n FROM users GROUP BY source ORDER BY n DESC")->fetchAll();
    page_start(['title' => 'Admin', 'noindex' => true, 'path' => '/admin']);
    ?>
<section class="wrap case">
  <h1>Admin</h1>
  <div class="stats">
    <div><b><?= $users ?></b><span>signed-up players</span></div>
    <div><b><?= $subs ?></b><span>newsletter subscribers</span></div>
    <div><b><?= (int)$week->fetchColumn() ?></b><span>new players last 7 days</span></div>
  </div>
  <p><a class="btn" href="/admin/reviews">Reviews</a> <a class="btn" href="/admin/newsletter">Write newsletter</a> <a class="btn btn-ghost" href="/admin/subscribers.csv">Download subscribers (CSV)</a></p>
  <h2>Mysteries</h2>
  <div class="table-wrap"><table>
    <thead><tr><th>Mystery</th><th>Level</th><th class="num">Players</th><th class="num">Solved</th><th class="num">Revealed</th><th class="num">Avg. tries</th></tr></thead>
    <tbody>
    <?php foreach (mysteries() as $m): $r = $by[$m['slug']] ?? null; ?>
      <tr><td><?= e($m['title']) ?></td><td><?= $m['level'] ?></td><td class="num"><?= (int)($att[$m['slug']] ?? 0) ?></td>
      <td class="num"><?= (int)($r['solved'] ?? 0) ?></td><td class="num"><?= (int)($r ? $r['total'] - $r['solved'] : 0) ?></td>
      <td class="num"><?= $r ? number_format((float)$r['avg_attempts'], 1) : '–' ?></td></tr>
    <?php endforeach; ?>
    </tbody></table></div>
  <h2>Where players came from</h2>
  <ul><?php foreach ($src as $s) echo '<li>' . e($s['source'] ?: 'direct / search') . ': ' . (int)$s['n'] . '</li>'; ?></ul>
</section>
<?php
    page_end();
}

function admin_csv(): void {
    if (!is_admin()) { not_found(); return; }
    header('Content-Type: text/csv; charset=utf-8');
    header('Content-Disposition: attachment; filename="subscribers-' . gmdate('Y-m-d') . '.csv"');
    $out = fopen('php://output', 'w');
    fputcsv($out, ['email', 'name', 'subscribed_at_utc', 'signed_up_utc', 'source']);
    foreach (db()->query('SELECT email, name, newsletter_at, created_at, source FROM users WHERE newsletter = 1 ORDER BY newsletter_at') as $r) fputcsv($out, array_values($r));
    fclose($out);
}

function privacy(): void {
    page_start(['title' => 'Privacy & cookies', 'path' => '/privacy']);
    $c = e(cfg('company_name')); $mail = e(cfg('contact_email'));
    ?>
<section class="wrap narrow prose">
  <h1>Privacy &amp; cookies</h1>
  <p><?= e(cfg('site_name')) ?> is run by <?= $c ?>. Contact: <a href="mailto:<?= $mail ?>"><?= $mail ?></a>.</p>
  <h2>What we collect</h2>
  <p>When you sign in with Google we receive your name, email address and profile picture. When you sign in with email we store the name and email address you enter. We store which mysteries you have answered, your guesses and when you solved them, so we can show your progress. Statistics such as how many players solved a case are only shown as totals.</p>
  <h2>Ratings and the leaderboard</h2>
  <p>If you rate a case, we show your stars and comment with your first name, or as “A detective” if you choose that. The leaderboard only shows players who join it, under the detective name they choose. You can leave the board at any time on the Rankings page.</p>
  <h2>Emails about new mysteries</h2>
  <p>We only email you about new mysteries if you tick the box to say yes. You can say no at any time by clicking the unsubscribe link in an email or by writing to us.</p>
  <h2>Cookies</h2>
  <p>We use one necessary session cookie to keep you signed in. With your permission we also use Google Analytics cookies to count visits and see which mysteries are popular. You can change your choice under “Cookie settings” at the bottom of every page.</p>
  <h2>Who processes your data</h2>
  <p>Our website and database are hosted by Simply.com in the EU. Google sign-in is provided by Google. Analytics (only with consent) is provided by Google.</p>
  <h2>Your rights</h2>
  <p>You can ask to see, correct or delete your data at any time by emailing <a href="mailto:<?= $mail ?>"><?= $mail ?></a>. You can also complain to your national data protection authority.</p>
</section>
<?php
    page_end();
}

function sitemap(): void {
    header('Content-Type: application/xml; charset=utf-8');
    echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n" . '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' . "\n";
    $urls = ['/', '/rankings', '/privacy'];
    foreach (mysteries() as $m) { $urls[] = '/mysteries/' . $m['slug']; $urls[] = '/mysteries/' . $m['slug'] . '/play'; }
    foreach ($urls as $u) echo '  <url><loc>' . e(url($u)) . '</loc></url>' . "\n";
    echo '</urlset>';
}

function robots(): void {
    header('Content-Type: text/plain; charset=utf-8');
    echo "User-agent: *\nDisallow: /answer/\nDisallow: /me\nDisallow: /admin\nDisallow: /login\nDisallow: /auth/\nDisallow: /*/print$\n\nSitemap: " . url('/sitemap.xml') . "\n";
}

function default_newsletter(): array {
    $all = mysteries();
    $new = array_slice($all, -6);
    $lines = [];
    foreach ($new as $m) $lines[] = '- ' . $m['title'] . ' (level ' . $m['level'] . ', ' . strtolower($m['crime']) . '): ' . $m['teaser'] . "\n  " . url('/mysteries/' . $m['slug']);
    return ['New cases to crack on ' . cfg('site_name'),
        "Hi {name},\n\nWe've just opened " . count($new) . " new case files – all free, all printable:\n\n" . implode("\n\n", $lines) . "\n\nPrint the six clues, hide them around the house and see who cracks the case first.\n\nHappy sleuthing,\nThe " . cfg('site_name') . " team"];
}

function admin_newsletter(): void {
    if (!is_admin()) { not_found(); return; }
    $pdo = db();
    $msg = null;
    [$subject, $body] = default_newsletter();
    if (($_SERVER['REQUEST_METHOD'] ?? '') === 'POST') {
        csrf_check();
        $subject = trim((string)($_POST['subject'] ?? ''));
        $body = str_replace("\r\n", "\n", (string)($_POST['body'] ?? ''));
        $body = str_replace("\n", "\r\n", $body);
        if ($subject === '' || trim($body) === '') { $msg = 'Subject and text are required.'; }
        elseif (($_POST['action'] ?? '') === 'test') {
            $ok = send_newsletter_mail(current_user(), '[TEST] ' . $subject, $body);
            $msg = $ok ? 'Test sent to ' . current_user()['email'] . '.' : 'Could not send the test email.';
        } elseif (($_POST['action'] ?? '') === 'send' && ($_POST['confirm'] ?? '') === 'yes') {
            @set_time_limit(0);
            $n = 0;
            foreach ($pdo->query('SELECT * FROM users WHERE newsletter = 1')->fetchAll() as $u) {
                if (send_newsletter_mail($u, $subject, $body)) $n++;
                usleep(150000);
            }
            $pdo->prepare('INSERT INTO newsletters (subject, body, recipients, sent_at) VALUES (?,?,?,?)')->execute([$subject, $body, $n, now()]);
            $msg = "Newsletter sent to $n subscribers.";
        } else { $msg = 'Tick the confirmation box to send to everyone.'; }
        $body = str_replace("\r\n", "\n", $body);
    }
    $subs = (int)$pdo->query('SELECT COUNT(*) FROM users WHERE newsletter = 1')->fetchColumn();
    $past = $pdo->query('SELECT subject, recipients, sent_at FROM newsletters ORDER BY id DESC LIMIT 10')->fetchAll();
    page_start(['title' => 'Newsletter', 'noindex' => true, 'path' => '/admin/newsletter']);
    ?>
<section class="wrap narrow case">
  <nav class="crumbs"><a href="/admin">Admin</a> › Newsletter</nav>
  <h1>Newsletter</h1>
  <?php if ($msg): ?><p class="flash"><?= e($msg) ?></p><?php endif; ?>
  <p><?= $subs ?> subscribers. Use <code>{name}</code> for the reader's name. An unsubscribe link is added automatically.</p>
  <form method="post" class="email-login">
    <?= csrf_field() ?>
    <label>Subject <input name="subject" value="<?= e($subject) ?>" required></label>
    <label>Text <textarea name="body" rows="18" style="font:15px/1.5 var(--sans);padding:10px;border:1.5px solid var(--ink)"><?= e($body) ?></textarea></label>
    <p><button class="btn btn-ghost" name="action" value="test">Send test to me</button></p>
    <label class="check"><input type="checkbox" name="confirm" value="yes"> Yes, send this to all <?= $subs ?> subscribers now</label>
    <p><button class="btn" name="action" value="send">Send newsletter</button></p>
  </form>
  <?php if ($past): ?><h2>Sent</h2><ul><?php foreach ($past as $p) echo '<li>' . e($p['sent_at']) . ' UTC – ' . e($p['subject']) . ' (' . (int)$p['recipients'] . ')</li>'; ?></ul><?php endif; ?>
</section>
<?php
    page_end();
}

function unsubscribe(): void {
    $uid = (int)($_GET['u'] ?? 0);
    $ok = $uid > 0 && hash_equals(unsub_token($uid), (string)($_GET['t'] ?? ''));
    if ($ok) db()->prepare('UPDATE users SET newsletter = 0 WHERE id = ?')->execute([$uid]);
    if (($_SERVER['REQUEST_METHOD'] ?? '') === 'POST') { http_response_code($ok ? 200 : 400); exit; }
    page_start(['title' => 'Unsubscribed', 'noindex' => true, 'path' => '/unsubscribe']);
    echo '<section class="wrap narrow"><h1>' . ($ok ? 'You are unsubscribed' : 'Link not valid') . '</h1><p class="lead">'
       . ($ok ? 'You won\'t get any more emails about new mysteries. You can sign up again any time when you submit an answer.' : 'This unsubscribe link is not valid. Email us and we will remove you by hand.')
       . '</p><p><a class="btn" href="/">Back to the mysteries</a></p></section>';
    page_end();
}

/**
 * Pulls the latest version of the site from GitHub when VERSION has changed.
 * Called hourly by Simply.com's cron service. Safe to call publicly: it can only
 * install what is already on the public main branch, and runs at most every 2 minutes.
 */
function cron_deploy(): void {
    header('Content-Type: text/plain; charset=utf-8');
    @set_time_limit(120);
    $repo = (string)cfg('deploy_repo', 'Chaospilot1980/6clues-site');
    $data = dirname(__DIR__) . '/data';
    if (!is_dir($data)) @mkdir($data, 0700, true);
    $lock = $data . '/deploy.lock';
    if (is_file($lock) && time() - filemtime($lock) < 120) { echo "busy\n"; return; }
    touch($lock);
    $get = function (string $u) {
        $ch = curl_init($u);
        curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_FOLLOWLOCATION => true, CURLOPT_TIMEOUT => 60, CURLOPT_USERAGENT => 'sixclues-deploy']);
        $b = curl_exec($ch); $c = curl_getinfo($ch, CURLINFO_HTTP_CODE); curl_close($ch);
        return $c === 200 ? $b : null;
    };
    $remote = trim((string)$get("https://raw.githubusercontent.com/$repo/main/VERSION?" . time()));
    $local = trim((string)@file_get_contents(__DIR__ . '/VERSION'));
    if ($remote === '' ) { echo "could not read remote VERSION\n"; return; }
    if ($remote === $local && empty($_GET['force'])) { echo "up to date ($local)\n"; return; }
    $zip = $get("https://codeload.github.com/$repo/zip/refs/heads/main");
    if (!$zip) { echo "download failed\n"; return; }
    $tmp = $data . '/deploy-' . bin2hex(random_bytes(4));
    @mkdir($tmp, 0700, true);
    file_put_contents("$tmp/site.zip", $zip);
    $za = new ZipArchive();
    if ($za->open("$tmp/site.zip") !== true) { echo "bad zip\n"; return; }
    $za->extractTo("$tmp/x"); $za->close();
    $src = glob("$tmp/x/*", GLOB_ONLYDIR)[0] ?? null;
    if (!$src || !is_file("$src/index.php")) { echo "unexpected zip layout\n"; return; }
    $n = 0;
    $it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($src, FilesystemIterator::SKIP_DOTS), RecursiveIteratorIterator::SELF_FIRST);
    foreach ($it as $f) {
        $rel = substr($f->getPathname(), strlen($src) + 1);
        $dest = __DIR__ . '/' . $rel;
        if ($f->isDir()) { if (!is_dir($dest)) @mkdir($dest, 0755, true); continue; }
        if ($rel === 'index.php') continue; // replaced last
        if (@copy($f->getPathname(), $dest)) $n++;
    }
    copy("$src/index.php", __DIR__ . '/index.php.new') && rename(__DIR__ . '/index.php.new', __DIR__ . '/index.php') && $n++;
    $rm = function ($d) use (&$rm) { foreach (glob("$d/{,.}[!.,!..]*", GLOB_BRACE) ?: [] as $p) is_dir($p) ? $rm($p) : @unlink($p); @rmdir($d); };
    $rm($tmp);
    if (function_exists('opcache_reset')) @opcache_reset();
    echo "deployed $remote ($n files)\n";
}

function review_form(int $uid, string $slug): void {
    $st = db()->prepare('SELECT * FROM reviews WHERE user_id = ? AND slug = ?');
    $st->execute([$uid, $slug]);
    $r = $st->fetch();
    if ($r) { echo '<p class="flash">Thanks for rating this case ' . str_repeat('★', (int)$r['stars']) . '</p>'; return; }
    ?>
<form method="post" action="/review/<?= e($slug) ?>" class="review-form">
  <?= csrf_field() ?>
  <h2>How did you like this case?</h2>
  <div class="star-pick" role="radiogroup" aria-label="Stars">
    <?php for ($s = 5; $s >= 1; $s--): ?><input type="radio" id="s<?= $s ?>" name="stars" value="<?= $s ?>" required><label for="s<?= $s ?>" title="<?= $s ?> stars">★</label><?php endfor; ?>
  </div>
  <label>A few words for other players (optional, no spoilers!)<textarea name="body" maxlength="300" rows="3"></textarea></label>
  <label class="check"><input type="checkbox" name="show_name" value="1" checked> Show my first name with the review</label>
  <button class="btn">Send rating</button>
</form>
<?php
}

function review(string $slug): void {
    $m = need_mystery($slug);
    $u = current_user();
    if (!$u || ($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') redirect('/answer/' . $slug);
    csrf_check();
    $stars = max(1, min(5, (int)($_POST['stars'] ?? 0)));
    $body = trim(mb_substr((string)($_POST['body'] ?? ''), 0, 300));
    $auto = ($body === '' || !preg_match('#https?://|www\.|\.com|@#i', $body)) ? 1 : 0;
    $st = db()->prepare('SELECT 1 FROM reviews WHERE user_id = ? AND slug = ?');
    $st->execute([$u['id'], $slug]);
    if (!$st->fetchColumn()) {
        db()->prepare('INSERT INTO reviews (user_id, slug, stars, body, show_name, approved, created_at) VALUES (?,?,?,?,?,?,?)')
            ->execute([$u['id'], $slug, $stars, $body, !empty($_POST['show_name']) ? 1 : 0, $body === '' ? 1 : 0, now()]);
    }
    $_SESSION['ga_event'] = 'review_submitted';
    flash('Thanks for your rating!' . ($body !== '' ? ' Your words will appear once we have checked them for spoilers.' : ''));
    redirect('/answer/' . $slug);
}

function admin_reviews(): void {
    if (!is_admin()) { not_found(); return; }
    if (($_SERVER['REQUEST_METHOD'] ?? '') === 'POST') {
        csrf_check();
        [$uid, $slug] = explode('|', (string)($_POST['key'] ?? '|'), 2);
        if (($_POST['do'] ?? '') === 'approve') db()->prepare('UPDATE reviews SET approved = 1 WHERE user_id = ? AND slug = ?')->execute([(int)$uid, $slug]);
        if (($_POST['do'] ?? '') === 'reject') db()->prepare("UPDATE reviews SET approved = 0, body = '' WHERE user_id = ? AND slug = ?")->execute([(int)$uid, $slug]);
        redirect('/admin/reviews');
    }
    $rows = db()->query("SELECT r.*, u.name, u.email FROM reviews r JOIN users u ON u.id = r.user_id WHERE r.body <> '' ORDER BY r.approved ASC, r.created_at DESC LIMIT 200")->fetchAll();
    $avg = db()->query('SELECT slug, AVG(stars) a, COUNT(*) n FROM reviews GROUP BY slug ORDER BY a DESC')->fetchAll();
    page_start(['title' => 'Reviews', 'noindex' => true, 'path' => '/admin/reviews']);
    echo '<section class="wrap case"><nav class="crumbs"><a href="/admin">Admin</a> › Reviews</nav><h1>Reviews</h1><div class="table-wrap"><table><thead><tr><th>Mystery</th><th class="num">Stars</th><th>Text</th><th>By</th><th></th></tr></thead><tbody>';
    foreach ($rows as $r) {
        echo '<tr><td>' . e($r['slug']) . '</td><td class="num">' . (int)$r['stars'] . '</td><td>' . e($r['body']) . '</td><td>' . e($r['name']) . '</td><td>';
        if (!(int)$r['approved']) echo '<form method="post" style="display:inline">' . csrf_field() . '<input type="hidden" name="key" value="' . e($r['user_id'] . '|' . $r['slug']) . '"><button class="btn btn-small" name="do" value="approve">Approve</button> <button class="btn btn-small btn-ghost" name="do" value="reject">Reject</button></form>';
        else echo 'Live';
        echo '</td></tr>';
    }
    echo '</tbody></table></div><h2>Average rating</h2><ul>';
    foreach ($avg as $a) echo '<li>' . e($a['slug']) . ': ' . number_format((float)$a['a'], 1) . ' ★ (' . (int)$a['n'] . ')</li>';
    echo '</ul></section>';
    page_end();
}

function filter_bar(bool $signedIn): void {
    $crimes = [];
    foreach (mysteries() as $m) { $c = strtolower($m['crime']); $crimes[$c] = ($crimes[$c] ?? 0) + 1; }
    ksort($crimes);
    ?>
<form class="filters" data-filters onsubmit="return false" aria-label="Filter mysteries">
  <fieldset><legend>Difficulty</legend>
    <label><input type="radio" name="level" value="" checked> All</label>
    <?php foreach ([1, 2, 3] as $l): ?><label><input type="radio" name="level" value="<?= $l ?>"> <?= $l ?> · <?= e(level_name($l)) ?></label><?php endforeach; ?>
  </fieldset>
  <fieldset><legend>Crime</legend>
    <label><input type="radio" name="crime" value="" checked> All</label>
    <?php foreach ($crimes as $c => $n): ?><label><input type="radio" name="crime" value="<?= e($c) ?>"> <?= e(ucwords($c)) ?> <small><?= $n ?></small></label><?php endforeach; ?>
  </fieldset>
  <div class="filter-row">
    <label class="sort">Sort by
      <select name="sort">
        <option value="">Recommended</option>
        <option value="new">Newest</option>
        <option value="popular">Most played</option>
        <option value="easy">Highest solve rate</option>
        <option value="hard">Lowest solve rate</option>
        <option value="stars">Best rated</option>
      </select>
    </label>
    <?php if ($signedIn): ?><label class="check"><input type="checkbox" name="hide_done" value="1"> Hide cases I've finished</label><?php endif; ?>
  </div>
</form>
<?php
}

function rank_list(string $title, array $rows, callable $val): void { ?>
  <div class="rank-box"><h3><?= e($title) ?></h3><ol>
  <?php foreach ($rows as $m): ?><li><a href="/mysteries/<?= e($m['slug']) ?>"><?= e($m['title']) ?></a> <span><?= e($val($m)) ?></span></li><?php endforeach; ?>
  </ol></div>
<?php }

function rankings(): void {
    $st = mystery_stats();
    $ms = array_values(array_filter(mysteries(), fn($m) => ($st[$m['slug']]['players'] ?? 0) >= STATS_MIN_PLAYERS));
    $by = function (string $k, int $dir) use ($ms, $st): array {
        usort($ms, fn($x, $y) => $dir * (($st[$x['slug']][$k] ?? 0) <=> ($st[$y['slug']][$k] ?? 0)));
        return array_slice($ms, 0, 5);
    };
    $top = leaderboard(25);
    $u = current_user();
    $in = false;
    if ($u) { $q = db()->prepare('SELECT alias FROM leaderboard WHERE user_id = ?'); $q->execute([$u['id']]); $in = $q->fetchColumn(); }
    page_start(['title' => 'Rankings – hardest mysteries and top detectives', 'path' => '/rankings',
        'description' => 'Which free murder mysteries are the hardest to crack, which are most played, and who are the best detectives on Six Clues?']);
    ?>
<section class="wrap case">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Mysteries</a> › Rankings</nav>
  <h1>Rankings</h1>
  <h2>The cases</h2>
  <?php if (count($ms) < 3): ?>
    <p>Not enough detectives have played yet to rank the cases. Each case needs at least <?= STATS_MIN_PLAYERS ?> players. Solve a few and come back!</p>
  <?php else: ?>
  <div class="rank-grid">
    <?php rank_list('Hardest to crack', $by('rate', 1), fn($m) => $st[$m['slug']]['rate'] . '% solved'); ?>
    <?php rank_list('Easiest', $by('rate', -1), fn($m) => $st[$m['slug']]['rate'] . '% solved'); ?>
    <?php rank_list('Most played', $by('players', -1), fn($m) => $st[$m['slug']]['players'] . ' players'); ?>
  </div>
  <?php endif; ?>
  <h2>Top detectives</h2>
  <p>Points: solving a level 1 case scores 3 points on your first guess, 2 on your second and 1 after that. Level 2 cases are worth double, and level 3 cases triple. Only players who choose to join are shown.</p>
  <?php if ($top): ?>
  <div class="table-wrap"><table><thead><tr><th class="num">#</th><th>Detective</th><th class="num">Cases solved</th><th class="num">First-guess solves</th><th class="num">Points</th></tr></thead><tbody>
  <?php foreach ($top as $n => $r): ?><tr><td class="num"><?= $n + 1 ?></td><td><?= e($r['alias']) ?></td><td class="num"><?= $r['solved'] ?></td><td class="num"><?= $r['first'] ?></td><td class="num"><b><?= $r['points'] ?></b></td></tr><?php endforeach; ?>
  </tbody></table></div>
  <?php else: ?><p>No detectives on the board yet – be the first.</p><?php endif; ?>
  <?php if ($u): ?>
    <form method="post" action="/me/leaderboard" class="inline-form"><?= csrf_field() ?>
      <?php if ($in): ?><p>You're on the board as <b><?= e($in) ?></b>.</p><button class="btn btn-ghost" name="do" value="leave">Leave the board</button>
      <?php else: ?><label>Your detective name <input name="alias" maxlength="30" required value="<?= e(first_name($u['name'] ?: '')) ?>"></label> <button class="btn" name="do" value="join">Join the board</button><?php endif; ?>
    </form>
  <?php else: ?><p><a class="btn" href="/login?next=/rankings">Sign in to join the board</a></p><?php endif; ?>
</section>
<?php
    page_end();
}

function leaderboard_optin(): void {
    $u = current_user();
    if (!$u || ($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') redirect('/rankings');
    csrf_check();
    if (($_POST['do'] ?? '') === 'leave') {
        db()->prepare('DELETE FROM leaderboard WHERE user_id = ?')->execute([$u['id']]);
        flash('You have left the board.');
    } else {
        $alias = mb_substr(trim((string)preg_replace('/[^\p{L}\p{N} ._\-]/u', '', (string)($_POST['alias'] ?? ''))), 0, 30);
        if ($alias === '') { flash('Please choose a detective name.'); redirect('/rankings'); }
        db()->prepare('DELETE FROM leaderboard WHERE user_id = ?')->execute([$u['id']]);
        db()->prepare('INSERT INTO leaderboard (user_id, alias, created_at) VALUES (?,?,?)')->execute([$u['id'], $alias, now()]);
        $_SESSION['ga_event'] = 'leaderboard_join';
        flash('Welcome to the board, detective ' . $alias . '!');
    }
    redirect('/rankings');
}
