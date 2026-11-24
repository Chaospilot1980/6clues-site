<?php
declare(strict_types=1);
require __DIR__ . '/app/bootstrap.php';
require __DIR__ . '/app/game.php';
require __DIR__ . '/app/gamenight.php';
require __DIR__ . '/app/escape.php';
require __DIR__ . '/app/landing.php';
require __DIR__ . '/app/views/layout.php';

$path = parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH) ?: '/';
$path = '/' . trim(rawurldecode($path), '/');
$method = $_SERVER['REQUEST_METHOD'] ?? 'GET';

// Remember where a visitor came from (QR code, campaign) for the sign-up record
if (!empty($_GET['src'])) $_SESSION['source'] = substr(preg_replace('/[^a-z0-9_\-]/i', '', (string)$_GET['src']), 0, 50);

$routes = [
    '#^/$#'                                   => 'home',
    '#^/mysteries$#'                          => 'library',
    '#^/mysteries/([a-z0-9\-]+)$#'            => 'show',
    '#^/mysteries/([a-z0-9\-]+)/play$#'       => 'play',
    '#^/daily$#'                              => 'daily_redirect',
    '#^/game-night$#'                         => 'gn_index',
    '#^/christmas-murder-mystery$#'           => 'christmas_page',
    '#^/(free-escape-rooms-for-kids|classroom-escape-room|christmas-escape-room|murder-mystery-for-kids|whodunit-puzzles-for-adults|printable-murder-mystery-games|how-to-host-a-murder-mystery-party|black-friday-murder-mystery|detective-games-online|escape-room-at-home|new-years-eve-murder-mystery|christmas-murder-mystery-for-kids|murder-mystery-games-for-adults)$#' => 'landing_page',
    '#^/seasonal$#' => 'seasonal_page',
    '#^/escape$#'                             => 'escape_index',
    '#^/escape/([a-z0-9\-]+)$#'               => 'escape_landing',
    '#^/escape/([a-z0-9\-]+)/play$#'          => 'escape_play',
    '#^/game-night/([a-z0-9\-]+)$#'           => 'gn_landing',
    '#^/game-night/([a-z0-9\-]+)/print$#'     => 'gn_print',
    '#^/game-night/([a-z0-9\-]+)/play$#'      => 'gn_play',
    '#^/c/([A-Za-z0-9]{6})$#'                 => 'challenge_page',
    '#^/rematch/([A-Za-z0-9]{6})$#'           => 'rematch',
    '#^/c/([A-Za-z0-9]{6})/name$#'            => 'challenge_name',
    '#^/mysteries/([a-z0-9\-]+)/print$#'      => 'print_page',
    '#^/answer/([a-z0-9\-]+)$#'               => 'answer',
    '#^/login$#'                              => 'login',
    '#^/auth/google$#'                        => 'auth_google',
    '#^/auth/dev$#'                           => 'auth_dev',
    '#^/auth/email$#'                         => 'auth_email',
    '#^/auth/verify$#'                        => 'auth_verify',
    '#^/logout$#'                             => 'logout',
    '#^/me$#'                                 => 'me',
    '#^/welcome$#'                            => 'welcome_page',
    '#^/rankings$#'                           => 'rankings',
    '#^/me/leaderboard$#'                     => 'leaderboard_optin',
    '#^/admin$#'                              => 'admin',
    '#^/admin/subscribers\.csv$#'             => 'admin_csv',
    '#^/admin/newsletter$#'                   => 'admin_newsletter',
    '#^/unsubscribe$#'                        => 'unsubscribe',
    '#^/cron/deploy$#'                        => 'cron_deploy',
    '#^/review/([a-z0-9\-]+)$#'              => 'review',
    '#^/admin/reviews$#'                      => 'admin_reviews',
    '#^/admin/growth$#'                       => 'admin_growth',
    '#^/admin/outreach$#'                     => 'admin_outreach',
    '#^/hook/scanditech-enquiry$#'            => 'hook_scanditech_enquiry',
    '#^/admin/smtp$#'                         => 'admin_smtp',
    '#^/cron/smtp-test$#'                     => 'cron_smtp_test',
    '#^/event$#'                              => 'event_endpoint',
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
    page_start(['path' => '/', 'title' => 'Free Murder Mystery Games & Daily Detective Puzzles',
        'description' => 'Free murder mystery games and detective puzzles for adults and families. Solve a new whodunit every day online, print a murder mystery party game, or play a free online escape room.',
        'jsonld' => [
        ['@context' => 'https://schema.org', '@type' => 'WebSite', 'name' => $site, 'url' => url('/'), 'description' => 'Free murder mystery games, daily detective puzzles, printable mystery party games and online escape rooms.'],
        ['@context' => 'https://schema.org', '@type' => 'ItemList', 'name' => 'Murder mystery games',
         'itemListElement' => array_map(fn($m, $i) => ['@type' => 'ListItem', 'position' => $i + 1, 'url' => url('/mysteries/' . $m['slug']), 'name' => $m['title']], mysteries(), array_keys(mysteries()))],
    ]]);
    ?>
<?php $d = featured_mystery(); $dp = $d ? my_play($d['slug']) : null; $isD = $d && !empty($d['daily']); ?>
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="kicker">6 clues. 1 culprit. Can you crack the case?</p>
      <h1>Free murder mystery games &amp; daily detective puzzles</h1>
      <p class="lead">A new detective case every day. Open the clues one by one, and accuse the culprit as soon as you're sure – the fewer clues you need, the higher you score. Then challenge your friends to beat you.</p>
      <?php if ($d): ?>
        <p class="cta-row"><a class="btn btn-big" href="/mysteries/<?= e($d['slug']) ?>/play" data-ga-click="daily_cta" data-ga-mystery="<?= e($d['slug']) ?>"><?= $dp && $dp['answered_at'] ? 'See your result' : ($dp ? 'Continue the case' : ($isD ? 'Play today\'s mystery' : 'Play today\'s featured case')) ?></a></p>
        <p class="small">Free · no sign-up needed to play · <a href="#mysteries">or pick any case</a></p>
      <?php else: ?>
        <p class="cta-row"><a class="btn" href="#mysteries">Pick a mystery</a></p>
      <?php endif; ?>
      <?php if ($u && ($s = streak((int)$u['id'])) > 0): ?><p class="streak">🔥 <?= $s ?> day<?= $s > 1 ? 's' : '' ?> in a row – keep it going!</p><?php endif; ?>
    </div>
    <?php if ($d): ?>
    <a class="hero-card daily-card" href="/mysteries/<?= e($d['slug']) ?>/play">
      <?php if ($isD): ?><div class="stamp">DAILY<br><b>#<?= daily_no($d['daily']) ?></b><br><?= e(strtoupper(date('j M', strtotime($d['daily'])))) ?></div>
      <?php else: ?><div class="stamp">TODAY'S<br><b>CASE</b><br><?= e(strtoupper(date('j M'))) ?></div><?php endif; ?>
      <p class="small"><?= badge_row($d) ?></p>
      <h2><?= e($d['title']) ?></h2>
      <p class="type"><?= e($d['teaser']) ?></p>
    </a>
    <?php endif; ?>
  </div>
</section>

<section id="how" class="wrap steps">
  <h2>How it works</h2>
  <ol class="step-list">
    <li><b>Play today's case on screen</b> – or choose any case from the library. Level 1 is perfect for a first game; level 3 will fool most grown-up detectives.</li>
    <li><b>Print and hide six posters – or play on screen.</b> On paper, hide the clues around the house, garden or office. On screen, flip through the same six posters on your phone, tablet or TV. Each one has a witness, a statement and a piece of evidence.</li>
    <li><b>Compare the clues.</b> Times, alibis and small details only make sense when you put them together.</li>
    <li><b>Accuse the culprit.</b> On screen, fewer clues mean more points. On paper, scan the code on any poster. Sign in to see the solution, keep your streak and climb the rankings.</li>
    <li><b>Challenge your friends.</b> Send them the case with one tap and find out who's the best detective.</li>
  </ol>
</section>

<section id="mysteries" class="wrap">
  <?php
    $done = array_values(array_filter(mysteries(), fn($m) => isset($prog[$m['slug']]['solved_at'])));
    $open = array_values(array_filter(mysteries(), fn($m) => !isset($prog[$m['slug']]['solved_at'])));
    $next = $u ? suggestions($u, 3) : [];
    $nextSlugs = array_column($next, 'slug');
  ?>
  <?php if ($next): ?>
    <h2>Up next for you</h2>
    <div class="grid"><?php foreach ($next as $m) echo mystery_card($m, $prog); ?></div>
  <?php endif; ?>
  <h2><?= $u ? 'More cases to crack' : 'All mysteries' ?> <span class="count" data-count><?= count($open) - count($nextSlugs) ?></span></h2>
  <?php filter_bar((bool)$u); ?>
  <div class="grid" data-grid>
    <?php foreach ($open as $m) if (!in_array($m['slug'], $nextSlugs, true)) echo mystery_card($m, $prog); ?>
  </div>
  <?php if ($done): ?>
    <h2>Cases you've closed <span class="count"><?= count($done) ?></span></h2>
    <div class="grid grid-done" data-grid><?php foreach ($done as $m) echo mystery_card($m, $prog); ?></div>
  <?php endif; ?>
  <p class="empty" data-empty hidden>No cases match – try another search or filter.</p>
  <p class="small"><a href="/rankings">See the rankings: hardest cases and top detectives →</a></p>
</section>

<?php $gn = array_map('gn_case', gn_slugs()); usort($gn, fn($a, $b) => $a['level'] <=> $b['level']); ?>
<section class="gn-home">
  <div class="wrap gn-home-grid">
    <div>
      <p class="kicker">New · Game Night</p>
      <h2>Bring the mystery home to your table</h2>
      <p class="lead">Bigger cases for an evening with friends or family: print the case file, open sealed envelopes as the evidence builds up and crack it together. <?= count($gn) ?> free cases – easy, medium and hard.</p>
      <ul class="gn-facts"><li>⏱ 90–150 min</li><li>👥 2–6 detectives</li><li>🖨 Print at home</li></ul>
      <p class="cta-row"><a class="btn btn-big" href="/game-night" data-ga-click="gn_home_cta">Plan a Game Night</a></p>
    </div>
    <div class="gn-home-cases">
      <?php foreach (array_slice($gn, 0, 4) as $c): ?><a href="/game-night/<?= e($c['slug']) ?>"><?= gn_art($c) ?><span><b><?= e($c['title']) ?></b>Level <?= (int)$c['level'] ?> · <?= gn_level_name((int)$c['level']) ?></span></a><?php endforeach; ?>
    </div>
  </div>
</section>

<?php $rv = reviews(null, 3, 4); if ($rv): ?>
<section class="wrap"><h2>What detectives say</h2><?= render_reviews($rv) ?></section>
<?php endif; ?>

<?= faq_block([
  ['Are the murder mystery games really free?', 'Yes. Every daily mystery, every case in the <a href="/mysteries">library</a>, every <a href="/game-night">Game Night</a> case file and every <a href="/escape">online escape room</a> is free to play. You don\'t need an account for the mysteries; the escape rooms just ask for a free sign-in to save your progress.'],
  ['How does a Six Clues mystery work?', 'Each case has six clues – a witness, a statement and a piece of evidence on each. Compare times, alibis and details, then name the culprit. Play online clue by clue, or print the six clue posters for a murder mystery party.'],
  ['Can I print the murder mystery games?', 'Yes. Every case has a printable version with clue posters and a solution sheet, and the Game Night cases come as full printable cold case files with sealed envelopes.'],
  ['Are the mysteries suitable for kids and families?', 'Level 1 cases are family-friendly detective puzzles for ages 8 and up. Level 2 and 3 are trickier whodunits for teens and adults.'],
  ['Is there a new mystery every day?', 'Yes – a new daily mystery appears every day. Solve it with as few clues as you can and compare your score with friends.'],
]) ?>
<section class="wrap newsletter-box">
  <h2>A new case every day</h2>
  <p>Sign in once with Google or your email to save your progress. Tick the box when you submit an answer, and we'll email you about new mysteries now and then.</p>
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
        'title' => $m['title'] . ' – free murder mystery game (play online or print)',
        'description' => $m['teaser'] . ' A free level ' . $m['level'] . ' ' . strtolower($m['crime']) . ' whodunit: play it online clue by clue or print the six clue posters for a mystery party.',
        'path' => '/mysteries/' . $slug, 'og_type' => 'article',
        'og_image' => mystery_cover_url($slug) ? '/assets/img/m/' . $slug . '/cover.jpg' : null,
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
  <?php if ($cv = mystery_cover_url($m['slug'])): ?><img class="case-cover" src="<?= e($cv) ?>" alt="<?= e($m['title']) ?>"><?php endif; ?>
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
    $method = $_SERVER['REQUEST_METHOD'] ?? 'GET';
    if (!empty($_GET['c']) && ($c = challenge((string)$_GET['c'])) && $c['slug'] === $slug) $_SESSION['challenge'][$slug] = $c['code'];
    $code = $_SESSION['challenge'][$slug] ?? null;
    if ($method === 'POST') {
        csrf_check();
        $do = (string)($_POST['do'] ?? '');
        $p = my_play($slug);
        if ($do === 'start' && !$p) { start_play($slug, $code); $_SESSION['ga_event'] = 'game_started'; log_event('game_started', $slug); }
        elseif ($do === 'clue' && $p) { reveal_clue($p); $_SESSION['ga_event'] = 'clue_revealed'; }
        elseif ($do === 'accuse' && $p && !$p['answered_at']) {
            $guess = (string)($_POST['guess'] ?? '');
            if (!in_array($guess, array_column($m['suspects'], 'name'), true)) { flash('Pick one of the six suspects.'); redirect('/mysteries/' . $slug . '/play#board'); }
            $p = accuse($p, $m, $guess);
            $_SESSION['ga_event'] = 'game_completed';
        }
        redirect('/mysteries/' . $slug . '/play' . ($do === 'accuse' ? '#result' : '#board'));
    }
    $p = my_play($slug);
    $u = current_user();
    $answered = $p && $p['answered_at'];
    $shown = $answered ? 6 : (int)($p['clues'] ?? 0);
    $isDaily = ($m['daily'] ?? '') === today();
    $answer = url('/answer/' . $slug . '?src=screen');
    $c = $code ? challenge($code) : null;
    $cp = $c ? challenger_play($c) : null;
    page_start(['title' => ($isDaily ? 'Daily case #' . daily_no($m['daily']) . ': ' : '') . $m['title'] . ' – play online',
        'description' => 'Play ' . $m['title'] . ' on screen. Six clues, one culprit – crack the case with as few clues as you can.',
        'path' => '/mysteries/' . $slug . '/play']);
    ?>
<section class="wrap case play">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Mysteries</a> › <a href="/mysteries/<?= e($slug) ?>"><?= e($m['title']) ?></a> › Play</nav>
  <div class="play-head">
    <div>
      <?php if ($isDaily): ?><p class="kicker">Daily case #<?= daily_no($m['daily']) ?> · <?= e(date('j F', strtotime($m['daily']))) ?></p><?php endif; ?>
      <h1><?= e($m['title']) ?></h1>
      <p class="small"><?= badge_row($m) ?></p>
    </div>
    <?php if ($p && !$answered): ?><div class="points-now"><span>Worth now</span><b><?= POINTS[$shown] ?></b><span>points</span></div><?php endif; ?>
  </div>

  <?php if ($c && $cp && $cp['answered_at'] && (!$u || (int)$c['user_id'] !== (int)$u['id'])): ?>
    <div class="challenge-banner">🕵️ <b><?= e(challenger_name($c)) ?></b>
      <?= (int)$cp['correct'] ? 'cracked this case with <b>' . (int)$cp['clues'] . ' of 6 clues</b>. Can you do it with fewer?' : 'couldn\'t crack this one. Can you?' ?></div>
  <?php endif; ?>

  <?php if (!$p): ?>
    <div class="intro-card">
      <p class="lead"><?= $m['intro'] ?></p>
      <h2>How to play</h2>
      <ul class="rules">
        <li>Open the clues one at a time. Each clue is a suspect's statement and a piece of evidence.</li>
        <li>Accuse someone whenever you're sure. <b>The fewer clues you use, the more points you score:</b> 100 for 1 clue, then 85, 70, 55, 40 and 25 for all six.</li>
        <li>Only your first accusation counts. A wrong one scores 0.</li>
      </ul>
      <form method="post"><?= csrf_field() ?><input type="hidden" name="do" value="start"><button class="btn btn-big">Start investigating</button></form>
      <p class="small muted">Free – no sign-up needed to play. Prefer paper? <a href="/mysteries/<?= e($slug) ?>/print">Print the six posters</a>.</p>
    </div>
  <?php else: ?>
    <?php if ($answered) game_result($m, $p); ?>
    <div id="board" class="clue-tabs" role="tablist" aria-label="Clues">
      <?php for ($i = 0; $i < 6; $i++): $cl = $m['clues'][$i]; ?>
        <?php if ($i < $shown): ?>
          <button role="tab" class="clue-tab" data-clue="<?= $i ?>" aria-selected="false"><b><?= $i + 1 ?></b><span><?= e($cl['name']) ?></span></button>
        <?php else: ?>
          <span class="clue-tab locked" aria-label="Clue <?= $i + 1 ?> – locked"><b><?= $i + 1 ?></b><span>🔒 Locked</span></span>
        <?php endif; ?>
      <?php endfor; ?>
    </div>
    <div class="board" data-start="<?= $answered ? 0 : $shown - 1 ?>">
      <?php for ($i = 0; $i < $shown; $i++): ?>
        <div class="poster-fit" data-poster="<?= $i ?>" <?= $i !== ($answered ? 0 : $shown - 1) ? 'hidden' : '' ?>><div class="poster-inner"><?= poster_html($m['clues'][$i]['poster'], $answer) ?></div></div>
      <?php endfor; ?>
    </div>
    <details class="clue-texts">
      <summary>Hard to read? Show this clue as text</summary>
      <?php for ($i = 0; $i < $shown; $i++): $cl = $m['clues'][$i]; ?>
        <article class="clue" data-text="<?= $i ?>" <?= $i !== ($answered ? 0 : $shown - 1) ? 'hidden' : '' ?>><header><span class="clue-no">Clue <?= $i + 1 ?> of 6</span><h2><?= e($cl['name']) ?> <small><?= e($cl['role']) ?></small></h2></header>
        <blockquote>”<?= e($cl['quote']) ?>”</blockquote><p class="ev-label">Evidence #<?= $i + 1 ?> · <?= e($cl['label']) ?></p><div class="evidence"><?= photo_html($cl['evidence']) ?></div></article>
      <?php endfor; ?>
    </details>
    <?php if (!$answered): ?>
      <div class="game-actions">
        <?php if ($shown < 6): ?>
          <form method="post"><?= csrf_field() ?><input type="hidden" name="do" value="clue"><button class="btn btn-ghost">Open clue <?= $shown + 1 ?> <small>(case then worth <?= POINTS[$shown + 1] ?>)</small></button></form>
        <?php endif; ?>
        <a class="btn" href="#accuse">I know who did it</a>
      </div>
      <form id="accuse" method="post" class="answer-form accuse-box">
        <?= csrf_field() ?><input type="hidden" name="do" value="accuse">
        <fieldset>
          <legend>Who is the <?= e($m['who']) ?>? <small>Right now a correct answer scores <?= POINTS[$shown] ?> points.</small></legend>
          <div class="suspect-pick">
          <?php foreach ($m['suspects'] as $s): ?>
            <label><input type="radio" name="guess" value="<?= e($s['name']) ?>" required> <b><?= e($s['name']) ?></b> <span><?= e($s['role']) ?></span></label>
          <?php endforeach; ?>
          </div>
        </fieldset>
        <button class="btn btn-big">Accuse!</button>
        <p class="small muted">Your first accusation is final.</p>
      </form>
    <?php endif; ?>
  <?php endif; ?>
</section>
<script src="/assets/js/qrcode.js"></script>
<?php
    page_end();
}

function game_result(array $m, array $p): void {
    $u = current_user();
    $slug = $m['slug'];
    echo '<div id="result" class="result-card">';
    if (!(int)$p['revealed']) {
        echo '<div class="locked-result"><p class="big">🔒 Your accusation is locked in.</p><p class="lead">Sign in to find out if you cracked the case – and to save your points and streak.</p>';
        google_button('/mysteries/' . $slug . '/play');
        echo '<p class="small muted">Free. We only use your name and email. <a href="/privacy">Privacy</a>.</p></div></div>';
        return;
    }
    $pct = percentile($p);
    if ((int)$p['correct']) {
        echo '<p class="verdict-big">🎉 Congratulations, detective!</p>';
        echo '<p class="lead">You cracked <b>' . e($m['title']) . '</b> with <b>' . (int)$p['clues'] . ' of 6 clue' . ((int)$p['clues'] > 1 ? 's' : '') . '</b> – <b>' . (int)$p['points'] . ' points</b>.'
            . ($pct !== null ? ' That\'s better than <b>' . $pct . '%</b> of players.' : '') . '</p>';
    } else {
        echo '<p class="verdict-big">Not quite, detective.</p>';
        echo '<p class="lead">' . e((string)$p['guess']) . ' is innocent. No points this time – but you can still find the real ' . e($m['who']) . '.</p>';
    }
    if ($u && ($m['daily'] ?? '') === cph_date((string)$p['answered_at'])) {
        $s = streak((int)$u['id']);
        if ($s > 0) echo '<p class="streak">🔥 ' . $s . ' day' . ($s > 1 ? 's' : '') . ' in a row</p>';
    }
    // Duel with the challenger, if this game came from a challenge link
    if ($p['challenge'] && ($c = challenge((string)$p['challenge'])) && ($cp = challenger_play($c)) && $cp['answered_at'] && (int)$cp['id'] !== (int)$p['id']) {
        $w = duel($p, $cp);
        $them = challenger_name($c);
        echo '<div class="vs"><div><b>You</b><span>' . clues_txt($p) . '</span></div><div class="vs-mid">VS</div><div><b>' . e($them) . '</b><span>' . clues_txt($cp) . '</span></div></div>';
        echo '<p class="vs-verdict">' . ($w > 0 ? '🏆 You beat ' . e($them) . '!' : ($w < 0 ? e($them) . ' wins this one.' : 'It\'s a draw!')) . '</p>';
        echo '<p><a class="btn btn-ghost" href="/rematch/' . e($c['code']) . '">Rematch on a new case</a></p>';
    }
    $code = create_challenge($slug);
    $link = url('/c/' . $code);
    $isDaily = ($m['daily'] ?? '') !== '' && ($m['daily'] ?? '') === cph_date((string)$p['answered_at']);
    $text = ($isDaily ? 'Six Clues daily #' . daily_no($m['daily']) . ' 🕵️ ' : 'Six Clues 🕵️ ') . $m['title'] . "\n" . emoji_row($p)
        . ((int)$p['correct'] ? ' · ' . (int)$p['points'] . ' pts' : '') . "\n" . ((int)$p['correct'] ? 'Can you crack it with fewer clues?' : 'I got it wrong – can you crack it?');
    $c0 = challenge($code);
    ?>
  <div class="share-box" data-share data-url="<?= e($link) ?>" data-text="<?= e($text) ?>" data-mystery="<?= e($slug) ?>">
    <h2>Challenge a friend to beat your score</h2>
    <p>Who's the best detective among your friends? Send them this case – they'll see your score, but not the answer.</p>
    <p class="emoji-row" aria-label="Your result"><?= e(emoji_row($p)) ?></p>
    <?php if (!$u): ?>
      <form method="post" action="/c/<?= e($code) ?>/name" class="alias-form"><?= csrf_field() ?>
        <label>Your detective name <small>(so friends know who challenged them)</small>
        <span><input name="alias" maxlength="24" value="<?= e((string)($c0['alias'] ?? '')) ?>" placeholder="e.g. Dennis" autocomplete="nickname"><button class="btn btn-small btn-ghost">Save</button></span></label></form>
    <?php endif; ?>
    <button class="btn btn-big" data-share-native>Challenge a friend</button>
    <div class="share-links">
      <a class="btn btn-ghost btn-small" target="_blank" rel="noopener" data-share-ch="whatsapp" href="https://wa.me/?text=<?= rawurlencode($text . ' ' . $link) ?>">WhatsApp</a>
      <a class="btn btn-ghost btn-small" target="_blank" rel="noopener" data-share-ch="facebook" href="https://www.facebook.com/sharer/sharer.php?u=<?= rawurlencode($link) ?>">Facebook</a>
      <a class="btn btn-ghost btn-small" target="_blank" rel="noopener" data-share-ch="email" href="mailto:?subject=<?= rawurlencode('Can you beat me?') ?>&amp;body=<?= rawurlencode($text . "\n\n" . $link) ?>">Email</a>
      <button class="btn btn-ghost btn-small" data-copy>Copy link</button>
    </div>
    <p class="small muted copy-out" data-copied hidden>Link copied!</p>
  </div>
  <p class="result-links">
    <?php if ($u): ?><a class="btn" href="/answer/<?= e($slug) ?>"><?= (int)$p['correct'] ? 'Read the full solution' : 'Keep investigating' ?></a>
    <?php else: ?><a class="btn" href="/login?next=/answer/<?= e($slug) ?>">Sign in to save your points</a><?php endif; ?>
    <a class="btn btn-ghost" href="/rankings">Rankings</a>
  </p>
</div>
<?php
}

function challenge_page(string $code): void {
    $c = challenge($code);
    if (!$c || !($m = mystery($c['slug']))) { not_found(); return; }
    $_SESSION['challenge'][$m['slug']] = $c['code'];
    $u = current_user();
    $mine = ($u && (int)$c['user_id'] === (int)$u['id']) || (!$u && $c['guest_id'] && $c['guest_id'] === guest_id());
    $cp = challenger_play($c);
    $name = challenger_name($c);
    $p = my_play($m['slug']);
    $score = $cp && $cp['answered_at'] ? ((int)$cp['correct'] ? 'cracked it with ' . (int)$cp['clues'] . ' of 6 clues' : 'couldn\'t crack it') : 'is on the case';
    $_SESSION['ga_event'] = 'challenge_opened';
    if (!$mine) log_event('challenge_opened', $c['code']);
    page_start(['title' => $name . ' challenges you: ' . $m['title'], 'path' => '/c/' . $c['code'], 'noindex' => true,
        'description' => $name . ' ' . $score . '. Six clues, one culprit – can you beat that? Free to play.']);
    ?>
<section class="wrap narrow case challenge-page">
  <p class="kicker">You've been challenged!</p>
  <h1><?= e($m['title']) ?></h1>
  <p><?= badge_row($m) ?></p>
  <?php if ($mine): ?>
    <p class="lead">This is your challenge link. Send it to friends – everyone who plays shows up here.</p>
  <?php else: ?>
    <div class="vs"><div><b><?= e($name) ?></b><span><?= $cp && $cp['answered_at'] ? clues_txt($cp) : '–' ?></span></div><div class="vs-mid">VS</div><div><b>You</b><span><?= $p && $p['answered_at'] ? ((int)$p['revealed'] ? clues_txt($p) : '🔒') : 'not played' ?></span></div></div>
    <p class="lead"><b><?= e($name) ?></b> <?= $score ?>. Can you do it with fewer clues?</p>
    <p class="intro-text"><?= $m['intro'] ?></p>
    <p><a class="btn btn-big" href="/mysteries/<?= e($m['slug']) ?>/play?c=<?= e($c['code']) ?>"><?= $p ? 'Back to the case' : 'Accept the challenge' ?></a></p>
    <p class="small muted">Free to play – no sign-up needed to start.</p>
  <?php endif; ?>
  <?php
    $st = db()->prepare('SELECT * FROM plays WHERE challenge = ? AND answered_at IS NOT NULL AND revealed = 1 ORDER BY points DESC, ms ASC LIMIT 20');
    $st->execute([$c['code']]);
    $rows = $st->fetchAll();
    if ($rows): ?>
    <h2>Who has played this challenge</h2>
    <div class="table-wrap"><table><thead><tr><th>Detective</th><th class="num">Clues</th><th class="num">Points</th></tr></thead><tbody>
    <?php if ($cp && $cp['answered_at']): ?><tr><td><?= e($name) ?> (challenger)</td><td class="num"><?= (int)$cp['correct'] ? (int)$cp['clues'] : '–' ?></td><td class="num"><?= (int)$cp['points'] ?></td></tr><?php endif; ?>
    <?php foreach ($rows as $r): ?><tr><td><?= e(player_name($r['user_id'] ? (int)$r['user_id'] : null)) ?></td><td class="num"><?= (int)$r['correct'] ? (int)$r['clues'] : '–' ?></td><td class="num"><?= (int)$r['points'] ?></td></tr><?php endforeach; ?>
    </tbody></table></div>
  <?php endif; ?>
</section>
<?php
    page_end();
}

function challenge_name(string $code): void {
    $c = challenge($code);
    if (!$c || ($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') { not_found(); return; }
    csrf_check();
    if (!$c['user_id'] && $c['guest_id'] && $c['guest_id'] === guest_id()) {
        $a = clean_alias((string)($_POST['alias'] ?? ''));
        $_SESSION['alias'] = $a;
        db()->prepare('UPDATE challenges SET alias = ? WHERE guest_id = ? AND user_id IS NULL')->execute([$a !== '' ? $a : null, $c['guest_id']]);
        flash($a !== '' ? 'Saved – your friends will see “' . $a . '”.' : 'Name removed.');
    }
    redirect('/mysteries/' . $c['slug'] . '/play#result');
}

function rematch(string $code): void {
    $c = challenge($code);
    if (!$c) { not_found(); return; }
    $played = [];
    foreach ([['user_id', $c['user_id']], ['user_id', current_user()['id'] ?? null], ['guest_id', guest_id()]] as [$col, $v]) {
        if (!$v) continue;
        $st = db()->prepare("SELECT slug FROM plays WHERE $col = ?"); $st->execute([$v]);
        foreach ($st->fetchAll() as $r) $played[$r['slug']] = true;
    }
    $daily = daily_mystery();
    $pick = ($daily && !isset($played[$daily['slug']])) ? $daily : null;
    if (!$pick) {
        $pool = array_values(array_filter(mysteries(), fn($m) => !isset($played[$m['slug']]) && $m['level'] <= 2));
        if (!$pool) $pool = array_values(array_filter(mysteries(), fn($m) => !isset($played[$m['slug']])));
        if (!$pool) { flash('You two have played every case! New ones arrive daily.'); redirect('/'); }
        $pick = $pool[random_int(0, count($pool) - 1)];
    }
    flash('Rematch! Crack this case, then send your new challenge link to ' . challenger_name($c) . '.');
    redirect('/mysteries/' . $pick['slug'] . '/play');
}

function daily_redirect(): void {
    $m = featured_mystery();
    redirect($m ? '/mysteries/' . $m['slug'] . '/play' : '/#mysteries');
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
<div class="sheet"><?= poster_html($c['poster'], $answer) ?></div>
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
<label class="check remember"><input type="checkbox" id="remember-me" checked> This is a private computer – keep me signed in for 30 days</label>
<script>function rememberVal(){var c=document.getElementById('remember-me');return c&&c.checked?'1':'0';}</script>
<?php if ($cid): ?>
<form id="g-form" method="post" action="/auth/google"><?= csrf_field() ?><input type="hidden" name="credential" id="g-credential"><input type="hidden" name="remember" id="g-remember" value="1"><input type="hidden" name="next" value="<?= e($next) ?>"></form>
<div id="g_id_onload" data-client_id="<?= e($cid) ?>" data-callback="onGoogleSignIn" data-auto_prompt="false"></div>
<div class="g_id_signin" data-type="standard" data-size="large" data-theme="filled_black" data-text="continue_with" data-shape="rectangular"></div>
<script>function onGoogleSignIn(r){document.getElementById('g-credential').value=r.credential;document.getElementById('g-remember').value=rememberVal();document.getElementById('g-form').submit();}</script>
<script src="https://accounts.google.com/gsi/client" async></script>
<p class="or"><span>or use your email</span></p>
<?php endif; ?>
<form method="post" action="/auth/email" class="email-login" onsubmit="this.remember.value=rememberVal()">
  <?= csrf_field() ?><input type="hidden" name="next" value="<?= e($next) ?>"><input type="hidden" name="remember" value="1">
  <label>Your name <input name="name" autocomplete="name" required maxlength="80"></label>
  <label>Email <input type="email" name="email" autocomplete="email" required maxlength="190"></label>
  <label class="check"><input type="checkbox" name="newsletter" value="1"> <span><b>Yes, email me new mysteries</b> – a free new case about once a month. Unsubscribe with one click.</span></label>
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
    $_SESSION['remember_pref'] = (($_POST['remember'] ?? '0') === '1') ? '1' : '0';
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
    if ((int)$row['newsletter']) { db()->prepare('UPDATE users SET newsletter = 1, newsletter_at = COALESCE(newsletter_at, ?) WHERE id = ?')->execute([now(), $_SESSION['uid']]); unset($_SESSION['ask_newsletter']); }
    redirect(after_login(safe_next((string)$row['next_path'])));
}

function auth_google(): void {
    if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') redirect('/login');
    csrf_check();
    $next = (string)($_POST['next'] ?? '/me');
    if (!preg_match('#^/[a-z0-9/\-]*$#i', $next)) $next = '/me';
    $p = verify_google_token((string)($_POST['credential'] ?? ''));
    if (!$p) { flash('Google sign-in failed. Please try again.'); redirect('/login?next=' . urlencode($next)); }
    login_user($p);
    redirect(after_login($next));
}

function auth_dev(): void {
    if (!cfg('dev_login') || ($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') { not_found(); return; }
    csrf_check();
    $email = (string)($_POST['email'] ?? 'tester@example.com');
    login_user(['sub' => 'dev-' . md5($email), 'email' => $email, 'name' => 'Test Detective']);
    redirect((string)($_POST['next'] ?? '/me'));
}

function logout(): void {
    if (($_SERVER['REQUEST_METHOD'] ?? '') === 'POST') { csrf_check(); remember_clear(); $_SESSION = []; session_regenerate_id(true); }
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
            record_print_play($uid, $slug, $guess, $ok);
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
  <?php $pts = board(null, [(int)$u['id']], false); $s = streak((int)$u['id']); ?>
  <p><b><?= (int)($pts[0]['pts'] ?? 0) ?> points</b><?= $s ? ' · 🔥 ' . $s . ' day' . ($s > 1 ? 's' : '') . ' in a row' : '' ?> · <a href="/rankings?tab=friends">See how you rank among your friends →</a></p>
  <?php next_cases($u); ?>
  <h2>All cases</h2>
  <?php // open cases first, solved/closed cases at the bottom
  $all = mysteries();
  $sorted = array_merge(array_filter($all, fn($m) => !isset($prog[$m['slug']]['solved_at'])), array_filter($all, fn($m) => isset($prog[$m['slug']]['solved_at']))); ?>
  <div class="grid"><?php foreach ($sorted as $m) echo mystery_card($m, $prog); ?></div>
  <h2>Account</h2>
  <p>Signed in as <?= e($u['email']) ?>. New-mystery emails: <b><?= (int)$u['newsletter'] ? 'on' : 'off' ?></b>.</p>
  <form method="post" action="/logout"><?= csrf_field() ?><button class="btn btn-ghost">Sign out</button></form>
</section>
<?php
    page_end();
}

/* Newly signed-up players get one clear yes/no question about the newsletter (consent must be an active choice under GDPR). */
function after_login(string $next): string {
    if (empty($_SESSION['ask_newsletter'])) return $next;
    $u = current_user();
    if (!$u || (int)$u['newsletter']) { unset($_SESSION['ask_newsletter']); return $next; }
    return '/welcome?next=' . urlencode($next);
}

function welcome_page(): void {
    $u = current_user();
    $next = safe_next((string)($_GET['next'] ?? $_POST['next'] ?? '/me'));
    if (!$u) redirect('/login');
    if (($_SERVER['REQUEST_METHOD'] ?? '') === 'POST') {
        csrf_check();
        unset($_SESSION['ask_newsletter']);
        if (($_POST['choice'] ?? '') === 'yes') {
            db()->prepare('UPDATE users SET newsletter = 1, newsletter_at = COALESCE(newsletter_at, ?) WHERE id = ?')->execute([now(), (int)$u['id']]);
            $_SESSION['ga_event'] = 'newsletter_signup';
            flash('Great – you will get the next new mystery by email.');
        }
        redirect($next);
    }
    page_start(['title' => 'Welcome, detective', 'noindex' => true, 'path' => '/welcome']);
    ?>
<section class="wrap narrow case" style="text-align:center">
  <h1>Welcome, <?= e(explode(' ', trim($u['name'] ?: 'detective'))[0]) ?>!</h1>
  <p class="lead">Want the next case delivered to your inbox? We send one free new mystery about once a month – nothing else.</p>
  <form method="post" action="/welcome" style="display:flex;flex-direction:column;gap:12px;align-items:center;margin-top:28px">
    <?= csrf_field() ?><input type="hidden" name="next" value="<?= e($next) ?>">
    <button class="btn" name="choice" value="yes" style="min-width:280px">Yes, send me new mysteries</button>
    <button class="btn btn-ghost" name="choice" value="no" style="min-width:280px">No thanks</button>
  </form>
  <p class="small muted" style="margin-top:18px">One-click unsubscribe in every email. See our <a href="/privacy">privacy policy</a>.</p>
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
    $recent = $pdo->query('SELECT name, email, source, newsletter, created_at, last_login_at, google_sub FROM users ORDER BY created_at DESC LIMIT 50')->fetchAll();
    page_start(['title' => 'Admin', 'noindex' => true, 'path' => '/admin']);
    ?>
<section class="wrap case">
  <h1>Admin</h1>
  <div class="stats">
    <div><b><?= $users ?></b><span>signed-up players</span></div>
    <div><b><?= $subs ?></b><span>newsletter subscribers</span></div>
    <div><b><?= (int)$week->fetchColumn() ?></b><span>new players last 7 days</span></div>
  </div>
  <p><a class="btn" href="/admin/growth">Growth dashboard</a> <a class="btn" href="/admin/reviews">Reviews</a> <a class="btn" href="/admin/newsletter">Write newsletter</a> <a class="btn btn-ghost" href="/admin/subscribers.csv">Download subscribers (CSV)</a></p>
  <h2>Latest sign-ups</h2>
  <div class="table-wrap"><table>
    <thead><tr><th>Signed up (UTC)</th><th>Name</th><th>Email</th><th>Via</th><th>Newsletter</th><th>Came from</th><th>Last login</th></tr></thead>
    <tbody>
    <?php foreach ($recent as $r): ?>
      <tr><td><?= e(substr((string)$r['created_at'], 0, 16)) ?></td><td><?= e($r['name']) ?></td><td><?= e($r['email']) ?></td>
      <td><?= str_starts_with((string)$r['google_sub'], 'email:') ? 'Email link' : 'Google' ?></td>
      <td><?= (int)$r['newsletter'] ? 'Yes' : '–' ?></td><td><?= e($r['source'] ?: 'direct / search') ?></td><td><?= e(substr((string)$r['last_login_at'], 0, 16)) ?></td></tr>
    <?php endforeach; ?>
    </tbody></table></div>
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
  <p>We use one necessary session cookie to keep you signed in, and one cookie that remembers the cases you play before you sign in, so your answers and points are not lost. With your permission we also use Google Analytics cookies to count visits and see which mysteries are popular. You can change your choice under “Cookie settings” at the bottom of every page.</p>
  <h2>Who processes your data</h2>
  <p>Our website and database are hosted by Simply.com in the EU. Google sign-in is provided by Google. Analytics (only with consent) is provided by Google.</p>
  <h2>Your rights</h2>
  <p>You can ask to see, correct or delete your data at any time by emailing <a href="mailto:<?= $mail ?>"><?= $mail ?></a>. You can also complain to your national data protection authority.</p>
</section>
<?php
    page_end();
}

function christmas_page(): void {
    $u = current_user();
    $prog = $u ? user_progress((int)$u['id']) : [];
    $re = '/christmas|santa|snow|winter|festive|frost|mince|carol/i';
    $ms = array_values(array_filter(mysteries(), fn($m) => preg_match($re, $m['title'] . ' ' . $m['teaser'])));
    $gns = array_values(array_filter(array_map('gn_case', gn_slugs()), fn($c) => $c && preg_match($re, $c['title'] . ' ' . $c['teaser'])));
    page_start(['title' => 'Free Christmas Murder Mystery Games (Printable)', 'path' => '/christmas-murder-mystery',
        'description' => 'Free Christmas murder mystery games for your holiday party: printable festive whodunits, a Christmas game night case file and online detective puzzles for families and adults.']);
    ?>
<section class="gn-hero">
  <div class="wrap">
    <p class="kicker">Holiday whodunits · free</p>
    <h1>Free Christmas murder mystery games</h1>
    <p class="lead">Looking for a Christmas murder mystery game for the family, the office party or a festive game night? These free whodunits are set at Christmas markets, snowy villages and winter fairs. Print the clues and hide them under the tree, or play online on the sofa.</p>
  </div>
</section>
<?php $xr = array_filter(escape_rooms(), fn($r, $s) => preg_match(CHRISTMAS_RE, $r['title'] . ' ' . $r['teaser'] . ' ' . $s), ARRAY_FILTER_USE_BOTH); if ($xr): ?>
<section class="wrap"><h2>Christmas escape rooms</h2><p>Play online – from Santa’s workshop to a stolen star on Christmas Eve. More on our <a href="/christmas-escape-room">Christmas escape room</a> page.</p><div class="grid"><?php foreach ($xr as $s => $r) echo escape_card($s, $r); ?></div></section>
<?php endif; ?>
<?php if ($gns): ?>
<section class="wrap"><h2>Christmas game night case files</h2><p>Full printable cold case files with sealed envelopes – for 2–8 players.</p><div class="grid"><?php foreach ($gns as $c) echo gn_card($c, $u); ?></div></section>
<?php endif; ?>
<section class="wrap"><h2>Festive mysteries to play online or print</h2><p>Each case has six clues and one culprit. Level 1 cases are family-friendly (see <a href="/christmas-murder-mystery-for-kids">Christmas mysteries for kids</a>); level 3 will fool the grown-ups.</p>
  <div class="grid"><?php foreach ($ms as $m) echo mystery_card($m, $prog); ?></div>
  <p>Want more? Browse all <a href="/mysteries">free murder mystery games</a>, the <a href="/game-night">Game Night case files</a> or our <a href="/escape">free online escape rooms</a>.</p>
</section>
<?= faq_block([
  ['How do I host a Christmas murder mystery party?', 'Pick a case, print the clues and hide them around the room or under the tree. Your guests find the clues, compare the alibis and vote on the culprit – then reveal the solution. It takes 15 minutes to set up.'],
  ['Are these Christmas murder mysteries suitable for kids?', 'The level 1 cases are family-friendly detective puzzles with no gore – great for children from about 8. Level 2 and 3 cases are aimed at teens and adults.'],
  ['Are they really free?', 'Yes – every case, printable and online, is free. No download or sign-up needed.'],
], 'Christmas murder mystery – questions') ?>
<?= pin_box('page-christmas-murder-mystery', '/christmas-murder-mystery', 'Free Christmas murder mystery games – printable whodunits and Christmas escape rooms.') ?>
<?php
    page_end();
}

/** Admin: store the SMTP mailbox password (typed by the site owner) outside the web root, and send a test mail. */
function admin_smtp(): void {
    if (!is_admin()) { not_found(); return; }
    $f = dirname(__DIR__) . '/data/smtp.json'; $msg = '';
    if ($_SERVER["REQUEST_METHOD"] === "POST") { csrf_check();
        if (($_POST['pass'] ?? '') !== '') {
            @mkdir(dirname($f), 0700, true);
            file_put_contents($f, json_encode(['host' => 'websmtp.simply.com', 'port' => 587, 'user' => trim((string)($_POST['user'] ?? '')) ?: 'mail@6clues.com', 'pass' => (string)$_POST['pass']]));
            @chmod($f, 0600);
        }
        $u = current_user();
        $ok = smtp_send($u['email'], 'Six Clues SMTP test', "If you can read this, 6clues.com can send mail.\n\n– Six Clues", [(string)cfg('contact_email'), 'Six Clues']);
        $msg = $ok ? 'Saved – test mail sent to ' . $u['email'] . '.' : 'Saved, but sending failed: ' . ($GLOBALS['smtp_error'] ?? '?');
    }
    page_start(['title' => 'Mail settings', 'noindex' => true, 'path' => '/admin/smtp']);
    echo '<section class="wrap narrow"><h1>Mail settings</h1><p>Mail is sent through websmtp.simply.com as <b>' . e(cfg('contact_email')) . '</b>. Status: ' . (($sc = smtp_conf()) ? 'password saved for login <b>' . e($sc['user']) . '</b>' : '<b>no password yet</b>') . '. Leave the password empty to just send a new test.</p>';
    if ($msg) echo '<p class="lead">' . e($msg) . '</p>';
    echo '<form method="post"><input type="hidden" name="csrf" value="' . e(csrf_token()) . '"><label>Mailbox (login)<br><input name="user" value="mail@6clues.com" style="width:100%"></label><label>Mailbox password<br><input type="password" name="pass" autocomplete="new-password" style="width:100%"></label><p><button class="btn">Save and send test mail</button></p></form></section>';
    page_end();
}

/** Diagnostic: sends a test mail to the first admin address (max once per 2 minutes) and reports the result. Shows the login name, never the password. */
function cron_smtp_test(): void {
    header('Content-Type: text/plain; charset=utf-8');
    $stamp = dirname(__DIR__) . '/data/smtp-test.stamp';
    if (is_file($stamp) && time() - filemtime($stamp) < 120) { echo "wait\n"; return; }
    @touch($stamp);
    $c = smtp_conf();
    echo 'login: ' . ($c ? $c['user'] . ' (password length ' . strlen($c['pass']) . ', ends with space: ' . (preg_match('/\s$/', $c['pass']) ? 'yes' : 'no') . ')' : 'none') . "\n";
    $to = ((array)cfg('admin_emails', []))[0] ?? '';
    $ok = smtp_send($to, 'Six Clues SMTP test', "If you can read this, 6clues.com can send mail.\n\n– Six Clues", [(string)cfg('contact_email'), 'Six Clues']);
    echo $ok ? "sent OK\n" : 'failed: ' . ($GLOBALS['smtp_error'] ?? '?') . "\n";
}

/** Link-building outreach: admin-only. POST JSON {to, subject, body} sends one personal mail from hello@6clues.com; GET lists the log. */
function admin_outreach(): void {
    $key = (string)($_SERVER['HTTP_X_OUTREACH_KEY'] ?? '');
    if (!is_admin() && !($key !== '' && hash_equals('6111ebe92422a8684a252eae378ca7e92e5ce3a7dac3caa1b0efd5e81e5e1c2c', hash('sha256', $key)))) { not_found(); return; }
    header('Content-Type: application/json; charset=utf-8');
    $log = dirname(__DIR__) . '/data/outreach.log';
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
        echo json_encode(['log' => is_file($log) ? array_map('json_decode', file($log, FILE_IGNORE_NEW_LINES)) : []], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
        return;
    }
    $in = json_decode((string)file_get_contents('php://input'), true) ?: [];
    $to = trim((string)($in['to'] ?? '')); $subject = trim((string)($in['subject'] ?? '')); $body = trim((string)($in['body'] ?? ''));
    if (!filter_var($to, FILTER_VALIDATE_EMAIL) || $subject === '' || $body === '' || preg_match('/[\r\n]/', $to . $subject)) { http_response_code(400); echo '{"ok":false,"error":"bad input"}'; return; }
    if (is_file($log) && str_contains((string)file_get_contents($log), '"to":"' . $to . '"')) { http_response_code(409); echo '{"ok":false,"error":"already contacted"}'; return; }
    $from = (string)cfg('contact_email');
    $ok = smtp_send($to, $subject, $body, [$from, 'Dennis, Six Clues'], ["Reply-To: $from"]);
    @mkdir(dirname($log), 0755, true);
    file_put_contents($log, json_encode(['at' => gmdate('c'), 'to' => $to, 'subject' => $subject, 'ok' => $ok], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n", FILE_APPEND);
    echo json_encode(['ok' => $ok, 'error' => $ok ? null : ($GLOBALS['smtp_error'] ?? null)]);
}

/** Relay for the scanditech.es contact form (its host cannot deliver mail() to Microsoft 365). Key hash only; key lives on scanditech server. */
function hook_scanditech_enquiry(): void {
    header('Content-Type: application/json; charset=utf-8');
    $in = json_decode((string)file_get_contents('php://input'), true) ?: [];
    if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST' || !hash_equals('d0a9ed72b12c6bb6082bbfaa13b4be01b2a04bc0a8ba20776be59d3f0c5a9027', hash('sha256', (string)($in['key'] ?? '')))) { http_response_code(404); echo '{"ok":false}'; return; }
    $clean = fn($k, $n) => trim(mb_substr(str_replace(["\r", "\n"], ' ', (string)($in[$k] ?? '')), 0, $n));
    $name = $clean('name', 120); $email = $clean('email', 190); $phone = $clean('phone', 40);
    $msg = trim(mb_substr((string)($in['message'] ?? ''), 0, 5000));
    if ($name === '' || !filter_var($email, FILTER_VALIDATE_EMAIL) || $msg === '') { http_response_code(400); echo '{"ok":false,"error":"bad input"}'; return; }
    $body = "New enquiry from scanditech.es" . (($in['lang'] ?? '') === 'es' ? ' (Spanish page)' : '') . "\n\nName: $name\nEmail: $email\nPhone: " . ($phone ?: '-') . "\n\nAbout the project:\n$msg\n\nReply directly to this email to answer $name.\n";
    $ok = smtp_send('dnh@scanditech.es', 'Website enquiry - ' . $name, $body, [(string)cfg('contact_email'), 'Scanditech website'], ["Reply-To: $name <$email>"]);
    echo json_encode(['ok' => $ok, 'error' => $ok ? null : ($GLOBALS['smtp_error'] ?? null)]);
}

/** FAQ block with FAQPage structured data. $qa = [[question, answer-html], ...] */
function faq_block(array $qa, string $heading = 'Questions & answers'): string {
    $ld = ['@context' => 'https://schema.org', '@type' => 'FAQPage', 'mainEntity' => array_map(fn($x) => ['@type' => 'Question', 'name' => $x[0], 'acceptedAnswer' => ['@type' => 'Answer', 'text' => strip_tags($x[1])]], $qa)];
    $h = '<section class="wrap faq"><h2>' . e($heading) . '</h2>';
    foreach ($qa as $x) $h .= '<details><summary>' . e($x[0]) . '</summary><p>' . $x[1] . '</p></details>';
    return $h . '<script type="application/ld+json">' . json_encode($ld, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . '</script></section>';
}

function sitemap(): void {
    header('Content-Type: application/xml; charset=utf-8');
    echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n" . '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' . "\n";
    $urls = ['/', '/mysteries', '/game-night', '/escape', '/seasonal', '/christmas-murder-mystery', '/rankings', '/privacy'];
    foreach (array_keys(landings()) as $l) $urls[] = '/' . $l;
    foreach (gn_slugs() as $g) $urls[] = '/game-night/' . $g;
    foreach (ESCAPE_ROOMS as $s => $r) if (empty($r['draft'])) $urls[] = '/escape/' . $s;
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
    @set_time_limit(300);
    $t0 = time();
    $repo = (string)cfg('deploy_repo', 'Chaospilot1980/6clues-site');
    $data = dirname(__DIR__) . '/data';
    if (!is_dir($data)) @mkdir($data, 0700, true);
    $lock = $data . '/deploy.lock';
    if (is_file($lock) && time() - filemtime($lock) < 120) { echo "busy\n"; return; }
    $get = function (string $u, array $headers = [], int $timeout = 30) {
        $ch = curl_init($u);
        curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_FOLLOWLOCATION => true, CURLOPT_TIMEOUT => $timeout, CURLOPT_USERAGENT => 'sixclues-deploy', CURLOPT_HTTPHEADER => $headers]);
        $b = curl_exec($ch); $c = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        return $c === 200 ? $b : null;
    };
    // Current commit on main (API is not CDN-cached, so a fresh push is seen at once).
    $sha = trim((string)$get("https://api.github.com/repos/$repo/commits/main", ['Accept: application/vnd.github.sha']));
    if (!preg_match('/^[0-9a-f]{40}$/', $sha)) { echo "could not read remote commit\n"; return; }
    $shaFile = $data . '/deployed_sha';
    if ($sha === trim((string)@file_get_contents($shaFile)) && empty($_GET['force'])) { echo "up to date (" . substr($sha, 0, 7) . ")\n"; return; }
    $tree = json_decode((string)$get("https://api.github.com/repos/$repo/git/trees/$sha?recursive=1"), true);
    if (empty($tree['tree']) || !empty($tree['truncated'])) { echo "could not read tree\n"; return; }
    touch($lock);
    // Compare every file with its git blob hash; download only what differs.
    $cacheFile = $data . '/deploy_blobs.json';
    $cache = json_decode((string)@file_get_contents($cacheFile), true) ?: [];
    $blobsha = function (string $path) use (&$cache): ?string {
        if (!is_file($path)) return null;
        $st = stat($path); $key = $st['size'] . ':' . $st['mtime'];
        if (($cache[$path][0] ?? '') === $key) return $cache[$path][1];
        $h = sha1('blob ' . $st['size'] . "\0" . file_get_contents($path));
        $cache[$path] = [$key, $h];
        return $h;
    };
    $n = 0; $fail = 0; $left = 0; $indexSha = null;
    foreach ($tree['tree'] as $it) {
        if (($it['type'] ?? '') !== 'blob') continue;
        $rel = (string)$it['path'];
        if (str_contains($rel, '..') || str_starts_with($rel, '.github/') || str_starts_with($rel, 'sites/')) continue;
        if ($rel === 'index.php') { $indexSha = $it['sha']; continue; }
        $dest = __DIR__ . '/' . $rel;
        if ($blobsha($dest) === $it['sha']) continue;
        if (time() - $t0 > 200) { $left++; continue; }
        $body = $get("https://raw.githubusercontent.com/$repo/$sha/" . implode('/', array_map('rawurlencode', explode('/', $rel))));
        if ($body === null) { $fail++; continue; }
        if (!is_dir(dirname($dest))) @mkdir(dirname($dest), 0755, true);
        if (file_put_contents($dest . '.tmp', $body) !== false && rename($dest . '.tmp', $dest)) { $n++; unset($cache[$dest]); } else $fail++;
        touch($lock);
    }
    if (!$fail && !$left && $indexSha && $blobsha(__DIR__ . '/index.php') !== $indexSha) {
        $body = $get("https://raw.githubusercontent.com/$repo/$sha/index.php");
        if ($body !== null && file_put_contents(__DIR__ . '/index.php.new', $body) !== false && rename(__DIR__ . '/index.php.new', __DIR__ . '/index.php')) { $n++; unset($cache[__DIR__ . '/index.php']); } else $fail++;
    }
    file_put_contents($cacheFile, json_encode($cache));
    if (!$fail && !$left) file_put_contents($shaFile, $sha);
    @unlink($lock);
    if (function_exists('opcache_reset')) @opcache_reset();
    echo ($fail || $left ? "partial deploy" : "deployed") . " " . substr($sha, 0, 7) . " ($n files updated" . ($fail ? ", $fail failed" : '') . ($left ? ", $left left – run again" : '') . ")\n";
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
  <label class="search"><span>Search</span><input type="search" name="q" placeholder="Title, place, crime…" autocomplete="off"></label>
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
    $u = current_user();
    $in = false;
    if ($u) { $q = db()->prepare('SELECT alias FROM leaderboard WHERE user_id = ?'); $q->execute([$u['id']]); $in = $q->fetchColumn(); }
    $tab = (string)($_GET['tab'] ?? 'week');
    if (!in_array($tab, ['week', 'friends', 'all'], true)) $tab = 'week';
    if ($tab === 'friends') $rows = $u ? board(null, array_merge([(int)$u['id']], friend_ids((int)$u['id'])), false) : [];
    else $rows = board($tab === 'week' ? week_start_utc() : null);
    page_start(['title' => 'Rankings – top detectives and hardest cases', 'path' => '/rankings',
        'description' => 'Who are the best detectives on Six Clues this week? See the weekly leaderboard, challenge your friends and find the hardest murder mysteries to crack.']);
    ?>
<section class="wrap case">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Mysteries</a> › Rankings</nav>
  <h1>Rankings</h1>
  <p>Every case you play on screen scores points: 100 if you crack it with 1 clue, then 85, 70, 55, 40 – and 25 with all six. A wrong first accusation scores 0.</p>
  <nav class="tabs" aria-label="Leaderboards">
    <a href="/rankings?tab=week" <?= $tab === 'week' ? 'aria-current="page"' : '' ?>>This week</a>
    <a href="/rankings?tab=friends" <?= $tab === 'friends' ? 'aria-current="page"' : '' ?>>Friends</a>
    <a href="/rankings?tab=all" <?= $tab === 'all' ? 'aria-current="page"' : '' ?>>All time</a>
  </nav>
  <?php if ($tab === 'friends' && !$u): ?>
    <p>Sign in to see how you rank against your friends. Everyone you challenge – or who challenges you – becomes a friend here.</p>
    <p><a class="btn" href="/login?next=/rankings?tab=friends">Sign in</a></p>
  <?php elseif ($tab === 'friends' && count($rows) < 2): ?>
    <p>No friends here yet. Solve a case and press <b>Challenge a friend</b> – everyone who plays your challenge shows up on this list.</p>
    <?php $d = daily_mystery(); if ($d): ?><p><a class="btn" href="/mysteries/<?= e($d['slug']) ?>/play">Play today's case</a></p><?php endif; ?>
  <?php elseif (!$rows): ?>
    <p><?= $tab === 'week' ? 'The week has just started – no detectives on the board yet. Be the first!' : 'No detectives on the board yet – be the first.' ?></p>
  <?php else: ?>
  <div class="table-wrap"><table><thead><tr><th class="num">#</th><th>Detective</th><th class="num">Cases cracked</th><th class="num">Avg. clues</th><th class="num">Points</th></tr></thead><tbody>
  <?php foreach ($rows as $n => $r): $me = $u && (int)$r['user_id'] === (int)$u['id']; ?>
    <tr<?= $me ? ' class="me"' : '' ?>><td class="num"><?= $n + 1 ?></td><td><?= e($tab === 'friends' ? ($me ? 'You' : (first_name((string)$r['name']) ?: 'A detective')) : (string)$r['alias']) ?></td><td class="num"><?= (int)$r['solved'] ?></td><td class="num"><?= $r['avg_clues'] !== null ? number_format((float)$r['avg_clues'], 1) : '–' ?></td><td class="num"><b><?= (int)$r['pts'] ?></b></td></tr>
  <?php endforeach; ?>
  </tbody></table></div>
  <?php endif; ?>
  <?php if ($tab !== 'friends'): ?>
    <?php if ($u): ?>
      <form method="post" action="/me/leaderboard" class="inline-form"><?= csrf_field() ?>
        <?php if ($in): ?><p>You're on the public boards as <b><?= e($in) ?></b>.</p><button class="btn btn-ghost" name="do" value="leave">Leave the boards</button>
        <?php else: ?><p class="small">The weekly and all-time boards only show detectives who choose to join.</p><label>Your detective name <input name="alias" maxlength="30" required value="<?= e(first_name($u['name'] ?: '')) ?>"></label> <button class="btn" name="do" value="join">Join the boards</button><?php endif; ?>
      </form>
    <?php else: ?><p><a class="btn" href="/login?next=/rankings">Sign in to join the boards</a></p><?php endif; ?>
  <?php endif; ?>
  <h2>The cases</h2>
  <?php if (count($ms) < 3): ?>
    <p>Not enough detectives have played yet to rank the cases. Each case needs at least <?= STATS_MIN_PLAYERS ?> players.</p>
  <?php else: ?>
  <div class="rank-grid">
    <?php rank_list('Hardest to crack', $by('rate', 1), fn($m) => $st[$m['slug']]['rate'] . '% solved'); ?>
    <?php rank_list('Easiest', $by('rate', -1), fn($m) => $st[$m['slug']]['rate'] . '% solved'); ?>
    <?php rank_list('Most played', $by('players', -1), fn($m) => $st[$m['slug']]['players'] . ' players'); ?>
  </div>
  <?php endif; ?>
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

function event_endpoint(): void {
    $t = (string)($_POST['t'] ?? '');
    if (($_SERVER['REQUEST_METHOD'] ?? '') === 'POST' && in_array($t, ['challenge_shared', 'print_opened'], true)) log_event($t, substr((string)($_POST['r'] ?? ''), 0, 100));
    http_response_code(204);
}

function admin_growth(): void {
    if (!is_admin()) { not_found(); return; }
    $g = growth_stats();
    $tile = function (string $label, $value, string $sub, ?string $goal = null) {
        echo '<div class="kpi"><span class="kpi-label">' . e($label) . '</span><b>' . ($value === null ? '–' : e((string)$value)) . '</b><span class="kpi-sub">' . e($sub) . '</span>'
            . ($goal ? '<span class="kpi-goal">Goal ' . e($goal) . '</span>' : '') . '</div>';
    };
    page_start(['title' => 'Growth', 'noindex' => true, 'path' => '/admin/growth']);
    $max = max(1, max(array_column($g['days'], 'players')));
    ?>
<section class="wrap case">
  <nav class="crumbs"><a href="/admin">Admin</a> › Growth</nav>
  <h1>Growth dashboard</h1>
  <p class="small muted">Last 7 days unless stated. Players include guests (one per browser).</p>
  <div class="kpis">
    <?php $tile('Daily players', $g['players_today'], 'today · ' . $g['players_7'] . ' in 7 days'); ?>
    <?php $tile('Completion rate', $g['completion'] === null ? null : $g['completion'] . '%', $g['done'] . ' of ' . $g['started'] . ' started games', '70%'); ?>
    <?php $tile('D7 retention', $g['d7'] === null ? null : $g['d7'] . '%', 'back after 7 days · cohort ' . $g['cohort'], '20%'); ?>
    <?php $tile('Challenge rate', $g['challenge_rate'] === null ? null : $g['challenge_rate'] . '%', $g['challenges'] . ' challenge links · ' . $g['shared'] . ' shares', '15%'); ?>
    <?php $tile('Invite conversion', $g['invite_conv'] === null ? null : $g['invite_conv'] . '%', $g['via'] . ' games from ' . $g['opens'] . ' link visits', '50%'); ?>
    <?php $tile('Viral coefficient', $g['viral'], $g['new_viral'] . ' of ' . $g['new'] . ' new players came via a friend'); ?>
    <?php $tile('Sign-ups', $g['signups_7'], 'new accounts in 7 days'); ?>
    <?php $tile('Locked answers', $g['gate_locks'], 'guests stopped at the sign-in wall (all time)'); ?>
  </div>
  <h2>Daily players – last 14 days</h2>
  <div class="bars" role="img" aria-label="Daily players for the last 14 days">
    <?php foreach ($g['days'] as $d): ?><div class="bar"><span style="height:<?= round($d['players'] / $max * 100) ?>%"><i><?= $d['players'] ?></i></span><small><?= e(substr($d['day'], 0, 6)) ?></small></div><?php endforeach; ?>
  </div>
  <div class="table-wrap"><table><thead><tr><th>Day</th><th class="num">Players</th><th class="num">Games started</th><th class="num">Finished</th><th class="num">Challenges</th><th class="num">Sign-ups</th></tr></thead><tbody>
  <?php foreach (array_reverse($g['days']) as $d): ?><tr><td><?= e($d['day']) ?></td><td class="num"><?= $d['players'] ?></td><td class="num"><?= $d['plays'] ?></td><td class="num"><?= $d['done'] ?></td><td class="num"><?= $d['challenges'] ?></td><td class="num"><?= $d['signups'] ?></td></tr><?php endforeach; ?>
  </tbody></table></div>
  <p class="small muted">Goals are first test targets, not forecasts. If completion is low, improve the cases before buying traffic.</p>
</section>
<?php
    page_end();
}

// ===================== GAME NIGHT =====================

function gn_card(array $c, ?array $u): string {
    $s = $u ? gn_session((int)$u['id'], $c['slug']) : null;
    $mine = $s && $s['score'] !== null ? '<span class="badge badge-done">Your table: ' . (int)$s['score'] . '/20</span>' : ($s ? '<span class="badge">In progress</span>' : '');
    return '<article class="card gn-card gn-level-' . (int)$c['level'] . '"><a class="gn-card-cover" href="/game-night/' . e($c['slug']) . '" tabindex="-1" aria-hidden="true">' . gn_art($c) . '</a>'
        . '<div class="card-top"><span class="badge">Case No. ' . e($c['no']) . '</span><span class="badge gn-lvl">Level ' . (int)$c['level'] . ' · ' . gn_level_name((int)$c['level']) . '</span><span class="badge badge-crime">' . e($c['genre']) . '</span>' . $mine . '</div>'
        . '<h3><a href="/game-night/' . e($c['slug']) . '">' . e($c['title']) . '</a></h3>'
        . '<p>' . e($c['teaser']) . '</p>'
        . '<p class="card-stats">' . $c['minutes'][0] . '–' . $c['minutes'][1] . ' min · ' . $c['players'][0] . '–' . $c['players'][1] . ' players · ' . count($c['docs']) . ' documents</p></article>';
}

function gn_index(): void {
    $u = current_user();
    $cases = array_map('gn_case', gn_slugs());
    usort($cases, fn($a, $b) => [$a['level'], $a['no']] <=> [$b['level'], $b['no']]);
    $lvl = (int)($_GET['level'] ?? 0);
    $shown = $lvl ? array_values(array_filter($cases, fn($c) => (int)$c['level'] === $lvl)) : $cases;
    $feat = gn_case('the-last-invitation') ?: $cases[0];
    page_start(['title' => 'Free Printable Murder Mystery Games for Game Night', 'path' => '/game-night',
        'description' => 'Free printable murder mystery games for game night: print a cold case file, open the sealed envelopes and solve it together. Easy to hard cases for 2–6 players, adults and families.']);
    ?>
<section class="gn-hero">
  <div class="wrap hero-grid">
    <div>
      <p class="kicker">Game Night · one evening, one table, one case</p>
      <h1>Free printable murder mystery games for game night</h1>
      <p class="lead">Each Game Night case is a complete cold case file – police reports, interviews, logs and lab results – plus sealed envelopes you open as the evidence builds up. Print it at home, pour the drinks and solve the murder mystery as a team. Perfect for a <a href="/how-to-host-a-murder-mystery-party">murder mystery party</a>, date night or family game night – or try our <a href="/christmas-murder-mystery">Christmas murder mysteries</a>.</p>
      <ul class="gn-facts"><li>⏱ 90–150 minutes</li><li>👥 2–6 detectives</li><li>🖨 Print at home</li><li>✉️ Sealed envelopes</li></ul>
      <p class="cta-row"><a class="btn btn-big" href="#cases">Choose a case</a></p>
    </div>
    <div class="gn-stack" aria-hidden="true">
      <?php foreach (array_slice($cases, 0, 3) as $i => $c) echo '<div class="gn-stack-' . $i . '">' . gn_art($c) . '</div>'; ?>
    </div>
  </div>
</section>
<section class="wrap" id="cases">
  <h2>Choose your level</h2>
  <div class="gn-levels" role="tablist">
    <a href="/game-night#cases" class="<?= $lvl ? '' : 'on' ?>"><b>All cases</b><span><?= count($cases) ?> cases</span></a>
    <?php foreach ([1 => 'First game night? Clear trails and one big twist.', 2 => 'Tricky timelines and a few red herrings.', 3 => 'Layered lies. For tables that love a fight.'] as $l => $txt):
      $n = count(array_filter($cases, fn($c) => (int)$c['level'] === $l)); ?>
      <a href="/game-night?level=<?= $l ?>#cases" class="lv<?= $l ?> <?= $lvl === $l ? 'on' : '' ?>"><b>Level <?= $l ?> · <?= gn_level_name($l) ?></b><span><?= e($txt) ?></span><small><?= $n ?> case<?= $n === 1 ? '' : 's' ?></small></a>
    <?php endforeach; ?>
  </div>
  <div class="grid gn-grid">
    <?php foreach ($shown as $c) echo gn_card($c, $u); ?>
    <article class="card gn-card gn-soon"><div class="card-top"><span class="badge">Coming soon</span></div><h3>More cases on the way</h3><p>Five new Game Night cases are being prepared right now. Sign in and tick the email box, and we'll tell you when they're ready.</p></article>
  </div>
</section>
<section class="wrap narrow">
  <h2>How Game Night works</h2>
  <ol class="step-list">
    <li><b>Pick a case and print it</b> – about 20–35 A4 pages. Sort them into a START folder and envelopes B and C. The first pages tell you how.</li>
    <li><b>Investigate at the table.</b> Share out the documents, compare times and statements, and argue it out. The paper is the game – one phone on the table is all you need.</li>
    <li><b>Open the envelopes</b> when you've cracked each checkpoint. The site checks your answer and gives hints if you're stuck (each costs a point).</li>
    <li><b>Make your accusation together</b> and score up to 20 points. Then reveal the full solution and see where your table lands in the hall of fame.</li>
  </ol>
  <p class="small muted">All names, companies and events in Game Night cases are fictional.</p>
</section>
<?php
?>
<?= faq_block([
  ['Are the printable murder mystery games free?', 'Yes. Every Game Night case file is free to print and play – no sign-up needed to read the case, and the online answer check is free too.'],
  ['How many players do I need?', 'Most cases work for 2–6 players. Work as one team, or split the documents between you and argue it out.'],
  ['How long does a Game Night case take?', 'Plan 60–150 minutes depending on the level. Level 1 is a relaxed first game night; level 3 cases are layered cold case files for experienced detectives.'],
  ['How do the sealed envelopes work?', 'You start with the first folder. When your table can answer a checkpoint question, you open the next envelope with new evidence – just like a real investigation.'],
  ['Can we play a murder mystery party with these?', 'Yes – print the case file, set the table, and let your guests be the detectives. It\'s a murder mystery party where everyone investigates instead of acting.'],
]) ?>
<?php
    page_end();
}

function gn_landing(string $slug): void {
    $c = gn_case($slug);
    if (!$c) { not_found(); return; }
    $u = current_user();
    $s = $u ? gn_session((int)$u['id'], $slug) : null;
    $hall = gn_hall($slug);
    $env = count($c['packets']) - 1;
    page_start(['title' => $c['title'] . ' – Game Night mystery', 'path' => '/game-night/' . $slug,
        'description' => $c['tagline'] . ' A free printable mystery game for ' . $c['players'][0] . '–' . $c['players'][1] . ' players, ' . $c['minutes'][0] . '–' . $c['minutes'][1] . ' minutes.']);
    ?>
<section class="gn-hero">
  <div class="wrap hero-grid">
    <div>
      <nav class="crumbs crumbs-light"><a href="/game-night">Game Night</a> › Case No. <?= e($c['no']) ?></nav>
      <p class="kicker">Level <?= (int)$c['level'] ?> · <?= gn_level_name((int)$c['level']) ?> · <?= e($c['genre']) ?></p>
      <h1><?= e($c['title']) ?></h1>
      <p class="gn-tagline"><?= e($c['tagline']) ?></p>
      <ul class="gn-facts"><li>⏱ <?= $c['minutes'][0] ?>–<?= $c['minutes'][1] ?> min</li><li>👥 <?= $c['players'][0] ?>–<?= $c['players'][1] ?> detectives</li><li>📄 <?= count($c['docs']) ?> documents</li><li>✉️ <?= $env ?> envelopes</li></ul>
      <p class="cta-row">
        <?php if (!$u): ?><a class="btn btn-big" href="/login?next=/game-night/<?= e($slug) ?>">Sign in to play – it's free</a>
        <?php else: ?><a class="btn btn-big" href="/game-night/<?= e($slug) ?>/print" data-ga-click="gn_print">1. Print the case file</a> <a class="btn btn-ghost-light btn-big" href="/game-night/<?= e($slug) ?>/play"><?= $s ? '2. Continue your game' : '2. Start the investigation' ?></a><?php endif; ?>
      </p>
    </div>
    <div class="gn-cover"><?= gn_art($c) ?></div>
  </div>
</section>
<section class="wrap narrow case">
  <h2>The case</h2>
  <?php foreach ($c['intro'] as $p) echo '<p>' . $p . '</p>'; ?>
  <h2>Your mission</h2>
  <ul><?php foreach ($c['mission'] as $m) echo '<li>' . e($m) . '</li>'; ?></ul>
  <h2>The people in the case</h2>
  <ul class="gn-people"><?php foreach ($c['suspects'] as $p) echo '<li>' . gn_portrait($slug, $p) . '<div><b>' . e($p['name']) . '</b><span>' . e($p['role']) . '</span></div></li>'; ?></ul>
  <h2>How Game Night works</h2>
  <ol class="step-list">
    <li><b>Print the case file</b> (<?= count($c['docs']) ?> documents) and sort it into the START folder and <?= $env ?> sealed envelopes. The first page tells you how.</li>
    <li><b>Investigate at the table.</b> Share out the documents, compare times and statements, and argue it out. Your phone just stays on the table.</li>
    <li><b>Open the envelopes</b> when you've cracked each checkpoint. The site checks your answer and gives hints if you get stuck (each costs a point).</li>
    <li><b>Make your accusation together</b>: the culprit, three key questions and at least four pieces of evidence. You score up to 20 points – then reveal the full solution.</li>
  </ol>
  <h2>Hall of fame</h2>
  <?php if ($hall): ?>
  <div class="table-wrap"><table><thead><tr><th class="num">#</th><th>Table</th><th class="num">Score</th><th class="num">Time</th></tr></thead><tbody>
  <?php foreach ($hall as $n => $h): ?><tr><td class="num"><?= $n + 1 ?></td><td><?= e(gn_table_name($h)) ?></td><td class="num"><b><?= (int)$h['score'] ?></b>/20</td><td class="num"><?= ($m = gn_minutes($h)) !== null ? $m . ' min' : '–' ?></td></tr><?php endforeach; ?>
  </tbody></table></div>
  <?php else: ?><p>No table has cracked this case yet. Will yours be the first?</p><?php endif; ?>
  <p class="small muted">All names, companies and events in this game are fictional.</p>
</section>
<?= pin_box('gn-' . $slug, '/game-night/' . $slug, 'Free printable murder mystery game: ' . $c['title'] . ' – a complete case file for game night.') ?>
<?php
    page_end();
}

function gn_print(string $slug): void {
    $c = gn_case($slug);
    if (!$c) { not_found(); return; }
    if (!current_user()) redirect('/login?next=/game-night/' . $slug . '/print');
    $play = url('/game-night/' . $slug . '/play');
    $sheet = function (string $packet, string $id, string $title, string $inner, string $meta = '', string $kind = 'report') use ($c) {
        echo '<div class="sheet gn-sheet gn-' . e($kind) . '"><div class="gn-doc"><header class="gn-doc-head"><span class="gn-id">' . e($id) . '</span><span class="gn-packet">' . e($packet) . '</span><span class="gn-caseno">CASE ' . e($c['caseref']) . '</span></header>'
            . '<h2>' . e($title) . '</h2>' . ($meta ? '<p class="gn-meta">' . e($meta) . '</p>' : '') . '<div class="gn-body">' . $inner . '</div>'
            . '<footer class="gn-doc-foot">SIX CLUES · ' . e(strtoupper($c['title'])) . ' · FICTIONAL CASE PROP</footer></div></div>';
    };
    $keys = array_keys($c['packets']);
    ?><!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title><?= e($c['title']) ?> – Game Night case file</title><meta name="robots" content="noindex">
<link rel="stylesheet" href="/assets/css/print.css?v=2"><link rel="stylesheet" href="/assets/css/gamenight.css?v=3">
</head><body>
<div class="toolbar"><p><b><?= e($c['title']) ?></b> – case file, <?= count($c['docs']) + 3 + count($keys) ?> A4 pages. Print on A4, margins <i>None</i>, scale 100%. The solution is <b>not</b> in this file.</p><button onclick="window.print()">Print case file</button></div>

<div class="sheet gn-sheet gn-coverpage"><div class="gn-doc">
  <p class="gn-kicker">SIX CLUES · GAME NIGHT · CASE No. <?= e($c['no']) ?> · LEVEL <?= (int)$c['level'] ?></p>
  <h1><?= e($c['title']) ?></h1>
  <p class="gn-tag"><?= e($c['tagline']) ?></p>
  <div class="gn-cover-wrap"><?= gn_art($c) ?></div>
  <p class="gn-facts-print"><?= $c['players'][0] ?>–<?= $c['players'][1] ?> detectives · <?= $c['minutes'][0] ?>–<?= $c['minutes'][1] ?> minutes · print and play</p>
  <?php foreach ($c['intro'] as $p) echo '<p>' . $p . '</p>'; ?>
  <h3>Your mission</h3><ul><?php foreach ($c['mission'] as $m) echo '<li>' . e($m) . '</li>'; ?></ul>
</div></div>

<div class="sheet gn-sheet"><div class="gn-doc">
  <h2>Before you start</h2>
  <ol class="gn-prep">
    <li>Put documents <b><?= e(gn_doc_range($c['packets']['START']['docs'])) ?></b> in a folder marked <b>START</b>.</li>
    <?php foreach (array_slice($keys, 1) as $k): ?><li>Put <b><?= e(gn_doc_range($c['packets'][$k]['docs'])) ?></b> in a closed envelope marked <b><?= e($k) ?></b>. The label is on the page before the set.</li><?php endforeach; ?>
    <li>Put the investigation sheet (last page) on the table.</li>
    <li>Read the cover page aloud, share out the START documents and investigate. Take notes, compare statements and argue freely.</li>
    <?php foreach (array_slice($keys, 1) as $k): ?><li>Open envelope <b><?= e($k) ?></b> when <?= e($c['packets'][$k]['when']) ?> – or after 25 minutes.</li><?php endforeach; ?>
    <li>Agree on one accusation together. Then enter it online for your score and the solution.</li>
  </ol>
  <h3>Questions to guide you</h3><ol><?php foreach ($c['questions'] as $q) echo '<li>' . e($q) . '</li>'; ?></ol>
  <div class="gn-online"><div class="qr" data-url="<?= e($play) ?>"></div><p><b>Online helper</b><br>Checkpoints, hints and your score:<br><?= e(preg_replace('#^https?://#', '', $play)) ?></p></div>
</div></div>

<?php if ($c['cast'] ?? true): ?>
<div class="sheet gn-sheet"><div class="gn-doc">
  <header class="gn-doc-head"><span class="gn-id">CAST</span><span class="gn-packet">START</span><span class="gn-caseno">CASE <?= e($c['caseref']) ?></span></header>
  <h2>The people in the case</h2>
  <div class="gn-body"><div class="gn-castgrid"><?php foreach ($c['suspects'] as $p) echo '<div>' . gn_portrait($slug, $p) . '<b>' . e($p['name']) . '</b><span>' . e($p['role']) . '</span></div>'; ?></div>
  <p class="note">Everyone may know something. A suspicious act is not necessarily the crime you are looking for.</p></div>
  <footer class="gn-doc-foot">SIX CLUES · <?= e(strtoupper($c['title'])) ?> · FICTIONAL CASE PROP</footer>
</div></div>
<?php endif; ?>

<?php foreach ($c['packets'] as $pk => $p):
  if ($pk !== 'START'): ?>
<div class="sheet gn-sheet gn-envelope"><div class="gn-doc"><p class="gn-kicker">CUT OUT AND STICK ON THE ENVELOPE</p>
  <div class="gn-env-label"><b>ENVELOPE <?= e($pk) ?></b><span><?= e($c['title']) ?> · documents <?= e(gn_doc_range($p['docs'])) ?></span>
  <em>Do not open until <?= e($p['when']) ?> – or 25 minutes have passed.</em></div>
</div></div>
  <?php endif;
  foreach ($p['docs'] as $id) { $d = $c['docs'][$id]; $sheet($p['label'], $id, $d['title'], gn_doc_body($d), $d['meta'] ?? '', $d['kind']); }
endforeach; ?>

<div class="sheet gn-sheet gn-worksheet"><div class="gn-doc">
  <header class="gn-doc-head"><span class="gn-id">FINAL</span><span class="gn-packet">Investigation sheet</span></header>
  <h2>Our conclusion</h2>
  <?php foreach ($c['worksheet'] as $q): ?>
    <p class="gn-q"><?= e($q) ?></p><div class="gn-line"></div><div class="gn-line"></div>
  <?php endforeach; ?>
  <p class="gn-q">Which documents prove your case?</p><p class="gn-boxes">____ &nbsp; ____ &nbsp; ____ &nbsp; ____ &nbsp; ____</p>
  <p class="gn-stop">STOP. Enter your accusation online for your score and the solution:<br><?= e(preg_replace('#^https?://#', '', $play)) ?></p>
</div></div>
<script src="/assets/js/qrcode.js"></script><script src="/assets/js/app.js?v=6"></script>
</body></html>
<?php
}

function gn_play(string $slug): void {
    $c = gn_case($slug);
    if (!$c) { not_found(); return; }
    $u = current_user();
    if (!$u) redirect('/login?next=/game-night/' . $slug . '/play');
    $uid = (int)$u['id'];
    $s = gn_session($uid, $slug);
    $pdo = db();
    $items = gn_items($c);
    $keys = array_keys($c['packets']);   // START, B, C
    if (($_SERVER['REQUEST_METHOD'] ?? '') === 'POST') {
        csrf_check();
        $do = (string)($_POST['do'] ?? '');
        $advance = function () use ($pdo, $s) {
            $pdo->prepare('UPDATE gn_sessions SET phase = ? WHERE id = ?')->execute([$s['phase'] === 'A' ? 'B' : 'final', $s['id']]);
            $_SESSION['ga_event'] = 'gn_checkpoint_advanced';
        };
        if ($do === 'start' || ($do === 'restart' && $s)) {
            if ($s) $pdo->prepare('UPDATE gn_sessions SET active = 0 WHERE id = ?')->execute([$s['id']]);
            $name = mb_substr(trim((string)preg_replace('/[^\p{L}\p{N} \'&._\-]/u', '', (string)($_POST['group_name'] ?? ''))), 0, 40);
            $pdo->prepare('INSERT INTO gn_sessions (user_id, slug, group_name, phase, hints, started_at) VALUES (?,?,?,?,?,?)')->execute([$uid, $slug, $name, 'A', '{}', now()]);
            $_SESSION['ga_event'] = 'gn_session_started';
        } elseif ($s && $do === 'hint' && isset($c['checkpoints'][$s['phase']])) {
            $cp = $s['phase']; $h = $s['hints'];
            $h[$cp] = min(count($c['checkpoints'][$cp]['hints']), (int)($h[$cp] ?? 0) + 1);
            $pdo->prepare('UPDATE gn_sessions SET hints = ? WHERE id = ?')->execute([json_encode($h), $s['id']]);
            $_SESSION['ga_event'] = 'gn_hint_revealed';
        } elseif ($s && $do === 'gate' && in_array($s['phase'], ['A', 'B'], true) && isset($c['checkpoints'][$s['phase']]['gate'])) {
            $g = $c['checkpoints'][$s['phase']]['gate'];
            if ((string)($_POST['answer'] ?? '') === (string)$g['answer']) { $advance(); flash('Correct! ' . $g['ok']); }
            else { flash('Not quite. Look at the documents again – or take a hint.'); $_SESSION['ga_event'] = 'gn_checkpoint_wrong'; }
        } elseif ($s && $do === 'advance' && in_array($s['phase'], ['A', 'B'], true)) {
            $advance();
        } elseif ($s && $do === 'accuse' && $s['phase'] === 'final') {
            $ids = array_column($c['suspects'], 'id');
            $ev = array_values(array_unique(array_filter((array)($_POST['evidence'] ?? []), fn($x) => isset($c['docs'][$x]))));
            $sub = ['culprit' => (string)($_POST['culprit'] ?? ''), 'evidence' => $ev];
            $ok = in_array($sub['culprit'], $ids, true) && count($ev) >= 4;
            foreach ($items as $k => $_) { $sub[$k] = (string)($_POST[$k] ?? ''); $ok = $ok && isset($c['choices'][$k][$sub[$k]]); }
            if (!$ok) {
                flash('Fill in every part of the accusation and tick at least four documents.');
                redirect('/game-night/' . $slug . '/play#accuse');
            }
            $r = gn_score($c, $sub, gn_hints_used($s));
            if ($s['score'] === null) {   // the first accusation is the one that counts
                $pdo->prepare('UPDATE gn_sessions SET phase = ?, submission = ?, score = ?, breakdown = ?, culprit_ok = ?, finished_at = ?, tries = tries + 1 WHERE id = ?')
                    ->execute(['done', json_encode($sub), $r['score'], json_encode($r['breakdown']), $r['culprit_ok'] ? 1 : 0, now(), $s['id']]);
            } else {
                $pdo->prepare('UPDATE gn_sessions SET phase = ?, culprit_ok = ?, tries = tries + 1 WHERE id = ?')->execute(['done', $r['culprit_ok'] ? 1 : 0, $s['id']]);
            }
            $_SESSION['ga_event'] = 'gn_final_submitted';
        } elseif ($s && $do === 'retry' && $s['phase'] === 'done') {
            $pdo->prepare('UPDATE gn_sessions SET phase = ? WHERE id = ?')->execute(['final', $s['id']]);
        } elseif ($s && $do === 'reveal' && !empty($_POST['confirm'])) {
            $pdo->prepare('UPDATE gn_sessions SET revealed = 1, phase = ?, finished_at = COALESCE(finished_at, ?) WHERE id = ?')->execute(['done', now(), $s['id']]);
            $_SESSION['ga_event'] = 'gn_solution_revealed';
        }
        redirect('/game-night/' . $slug . '/play');
    }
    page_start(['title' => $c['title'] . ' – Game Night', 'noindex' => true, 'path' => '/game-night/' . $slug . '/play']);
    $steps = ['A' => $c['packets'][$keys[0]]['label'], 'B' => $c['packets'][$keys[1]]['label'], 'final' => $c['packets'][$keys[2]]['label'], 'done' => 'Verdict'];
    $order = array_keys($steps);
    $nextPk = ['A' => $keys[1], 'B' => $keys[2]];
    ?>
<section class="wrap case gn-play">
  <nav class="crumbs"><a href="/game-night">Game Night</a> › <a href="/game-night/<?= e($slug) ?>"><?= e($c['title']) ?></a> › Investigation</nav>
  <?php if (!$s): ?>
    <div class="gn-panel">
      <h1>Ready, detectives?</h1>
      <p class="lead">Have you printed the case file and sorted it into the START folder and envelopes <?= e(implode(' and ', array_slice($keys, 1))) ?>? Then gather round.</p>
      <form method="post" class="inline-form"><?= csrf_field() ?><input type="hidden" name="do" value="start">
        <label>Name your table (optional – shown in the hall of fame)<input name="group_name" maxlength="40" placeholder="e.g. The Saturday Sleuths"></label>
        <button class="btn btn-big">Start the investigation</button></form>
      <p class="small"><a href="/game-night/<?= e($slug) ?>/print">Haven't printed it yet? Get the case file.</a></p>
    </div>
  <?php else:
    $idx = array_search($s['phase'], $order, true); ?>
    <ol class="gn-rail" aria-label="Progress">
      <?php foreach ($steps as $k => $label): $i = array_search($k, $order, true); ?>
        <li class="<?= $i < $idx ? 'done' : ($i === $idx ? 'now' : '') ?>"><span><?= $i + 1 ?></span><?= e($label) ?></li>
      <?php endforeach; ?>
    </ol>
    <p class="gn-table">🕵️ <?= e(gn_table_name($s + ['name' => $u['name']])) ?> · hints used: <?= gn_hints_used($s) ?></p>

    <?php if (in_array($s['phase'], ['A', 'B'], true)): $cp = $c['checkpoints'][$s['phase']]; $used = (int)($s['hints'][$s['phase']] ?? 0); $pk = $nextPk[$s['phase']]; ?>
      <?php if ($s['phase'] === 'B'): ?><div class="gn-open">✉️ <b>Envelope <?= e($keys[1]) ?> is open</b> – documents <?= e(gn_doc_range($c['packets'][$keys[1]]['docs'])) ?> join the investigation.</div><?php endif; ?>
      <div class="gn-panel">
        <p class="kicker">Checkpoint <?= $s['phase'] === 'A' ? 1 : 2 ?> · <?= e($cp['title']) ?></p>
        <h1 class="gn-prompt"><?= e($cp['prompt']) ?></h1>
        <?php if (isset($cp['gate'])): ?>
          <form method="post" class="gn-gate"><?= csrf_field() ?><input type="hidden" name="do" value="gate">
            <p><b><?= e($cp['gate']['q']) ?></b></p>
            <div class="gn-choices"><?php foreach ($cp['gate']['choices'] as $i => $t): ?><label><input type="radio" name="answer" value="<?= $i ?>" required> <?= e($t) ?></label><?php endforeach; ?></div>
            <button class="btn">✉️ Check our answer and open envelope <?= e($pk) ?></button>
          </form>
        <?php else: ?>
          <p>Talk it through at the table. When you can answer, open the next envelope.</p>
        <?php endif; ?>
        <?php for ($i = 0; $i < $used; $i++): ?><div class="gn-hint"><b>Hint <?= $i + 1 ?>:</b> <?= e($cp['hints'][$i]) ?></div><?php endfor; ?>
        <div class="gn-actions">
          <?php if ($used < count($cp['hints'])): ?><form method="post"><?= csrf_field() ?><input type="hidden" name="do" value="hint"><button class="btn btn-ghost">Show hint <?= $used + 1 ?> <small>(−1 point)</small></button></form><?php endif; ?>
          <?php if (!isset($cp['gate'])): ?><form method="post"><?= csrf_field() ?><input type="hidden" name="do" value="advance"><button class="btn">✉️ <?= e($cp['button']) ?></button></form><?php endif; ?>
        </div>
        <?php if (isset($cp['gate'])): ?><form method="post" class="gn-skip"><?= csrf_field() ?><input type="hidden" name="do" value="advance"><button class="linkbtn">Stuck for 25 minutes? Open envelope <?= e($pk) ?> anyway</button></form>
        <?php else: ?><p class="small muted"><?= e($cp['fallback']) ?></p><?php endif; ?>
      </div>

    <?php elseif ($s['phase'] === 'final'): $cp = $c['checkpoints']['final']; $used = (int)($s['hints']['final'] ?? 0); ?>
      <div class="gn-open">✉️ <b>Open envelope <?= e($keys[2]) ?></b> – documents <?= e(gn_doc_range($c['packets'][$keys[2]]['docs'])) ?>. You now have everything.</div>
      <div class="gn-panel">
        <p class="kicker">Final · <?= e($cp['title']) ?></p>
        <h1 class="gn-prompt"><?= e($cp['prompt']) ?></h1>
        <?php for ($i = 0; $i < $used; $i++): ?><div class="gn-hint"><b>Hint <?= $i + 1 ?>:</b> <?= e($cp['hints'][$i]) ?></div><?php endfor; ?>
        <?php if ($used < count($cp['hints'])): ?><form method="post" class="gn-actions"><?= csrf_field() ?><input type="hidden" name="do" value="hint"><button class="btn btn-ghost">Show hint <?= $used + 1 ?> <small>(−1 point)</small></button></form><?php endif; ?>
        <?php if ($s['score'] !== null): ?><p class="flash">Your score is locked from your first accusation (<?= (int)$s['score'] ?>/20). This attempt is just for the satisfaction of getting it right.</p><?php endif; ?>
      </div>
      <form id="accuse" method="post" class="gn-accuse"><?= csrf_field() ?><input type="hidden" name="do" value="accuse">
        <fieldset><legend><span>1</span> <?= e($c['accuse']['culprit_q']) ?> <small>6 points</small></legend><div class="suspect-pick">
          <?php foreach ($c['suspects'] as $p): ?><label><input type="radio" name="culprit" value="<?= e($p['id']) ?>" required> <?= gn_portrait($slug, $p) ?> <b><?= e($p['name']) ?></b> <span><?= e($p['role']) ?></span></label><?php endforeach; ?></div></fieldset>
        <?php $n = 1; foreach ($items as $k => [, $q, $pts]): $n++; ?>
          <fieldset><legend><span><?= $n ?></span> <?= e($q) ?> <small><?= $pts ?> points</small></legend><div class="gn-choices">
            <?php foreach ($c['choices'][$k] as $v => $t): ?><label><input type="radio" name="<?= e($k) ?>" value="<?= e($v) ?>" required> <?= e($t) ?></label><?php endforeach; ?></div></fieldset>
        <?php endforeach; $n++; ?>
        <fieldset><legend><span><?= $n ?></span> Which documents prove it? <small>Tick at least four · 3 points</small></legend><div class="gn-docs">
          <?php foreach ($c['docs'] as $id => $d): if (!empty($d['aid'])) continue; ?><label><input type="checkbox" name="evidence[]" value="<?= e($id) ?>"> <b><?= e($id) ?></b> <span><?= e($d['title']) ?></span></label><?php endforeach; ?></div></fieldset>
        <button class="btn btn-big">Make the accusation</button>
      </form>

    <?php else: /* done */ ?>
      <?php if (!$s['revealed']): ?>
        <div class="gn-panel gn-verdict <?= $s['culprit_ok'] ? 'ok' : 'no' ?>">
          <?php if ($s['score'] !== null): ?><div class="gn-score"><b><?= (int)$s['score'] ?></b><span>/ 20</span></div><?php endif; ?>
          <?php if ($s['culprit_ok']): ?>
            <h1>Case closed, detectives! 🎉</h1><p class="lead">You named the right culprit. Here's how your table scored:</p>
          <?php else: ?>
            <h1>The accusation doesn't hold up.</h1><p class="lead"><?= e($c['accuse']['wrong']) ?> Your score is locked in – but you can keep investigating, or reveal the solution.</p>
          <?php endif; ?>
          <?php if ($s['breakdown']): ?><table class="gn-break"><?php foreach ($s['breakdown'] as $row): ?><tr><td><?= e($row[0]) ?></td><td class="num"><?= $row[2] ? (int)$row[1] . ' / ' . (int)$row[2] : (int)$row[1] ?></td></tr><?php endforeach; ?></table><?php endif; ?>
          <div class="gn-actions">
            <?php if (!$s['culprit_ok']): ?><form method="post"><?= csrf_field() ?><input type="hidden" name="do" value="retry"><button class="btn">Keep investigating</button></form><?php endif; ?>
          </div>
          <form method="post" class="gn-reveal"><?= csrf_field() ?><input type="hidden" name="do" value="reveal">
            <label class="check"><input type="checkbox" name="confirm" value="1" required> Our table has finished investigating. Show the full solution.</label>
            <button class="btn btn-ghost">Reveal the solution</button></form>
        </div>
      <?php else: $sol = gn_solution($slug); ?>
        <div class="gn-panel gn-solution">
          <?php if ($s['score'] !== null): ?><div class="gn-score"><b><?= (int)$s['score'] ?></b><span>/ 20</span></div><?php endif; ?>
          <p class="kicker">The solution</p><h1><?= e($c['solution_title']) ?></h1>
          <?php foreach ($sol['summary'] as $p) echo '<p>' . $p . '</p>'; ?>
          <h2>The answers</h2>
          <ul class="gn-answers"><li><b><?= e($c['accuse']['culprit_q']) ?></b> <?= e(array_column($c['suspects'], 'name', 'id')[$sol['culprit']]) ?></li>
          <?php foreach ($items as $k => [, $q]) echo '<li><b>' . e($q) . '</b> ' . e($c['choices'][$k][$sol[$k]]) . '</li>'; ?>
          <li><b>Key documents:</b> <?= e(implode(', ', $sol['evidence'])) ?></li></ul>
          <h2>The chain of evidence</h2>
          <table class="gn-timeline"><?php foreach ($sol['timeline'] as [$t, $what, $src]): ?><tr><td class="mono"><?= e($t) ?></td><td><?= e($what) ?></td><td class="mono"><?= e($src) ?></td></tr><?php endforeach; ?></table>
          <h2>The conclusions</h2><ol><?php foreach ($sol['conclusions'] as [$t, $src]) echo '<li>' . e($t) . ' <span class="muted">(' . e($src) . ')</span></li>'; ?></ol>
          <h2>Why not the others?</h2><ul><?php foreach ($sol['others'] as $o) echo '<li>' . $o . '</li>'; ?></ul>
          <p class="note"><?= e($sol['fairness']) ?></p>
          <?php if ($s['breakdown']): ?><h2>Your table's score</h2><table class="gn-break"><?php foreach ($s['breakdown'] as $row): ?><tr><td><?= e($row[0]) ?></td><td class="num"><?= $row[2] ? (int)$row[1] . ' / ' . (int)$row[2] : (int)$row[1] ?></td></tr><?php endforeach; ?></table><?php endif; ?>
        </div>
      <?php endif; ?>
      <div class="share-box" data-share data-url="<?= e(url('/game-night/' . $slug)) ?>" data-text="<?= e($s['score'] !== null ? 'Our table scored ' . (int)$s['score'] . '/20 on the Game Night mystery "' . $c['title'] . '" 🕵️ Can your friends beat that?' : 'We just played the Game Night mystery "' . $c['title'] . '" 🕵️') ?>" data-mystery="gn-<?= e($slug) ?>">
        <h2>Challenge another table</h2><p>Send the case to friends and see who tops the hall of fame.</p>
        <button class="btn btn-big" data-share-native>Share the case</button>
        <div class="share-links"><a class="btn btn-ghost btn-small" target="_blank" rel="noopener" data-share-ch="whatsapp" href="https://wa.me/?text=<?= rawurlencode('Game Night mystery: ' . $c['title'] . ' ' . url('/game-night/' . $slug)) ?>">WhatsApp</a><button class="btn btn-ghost btn-small" data-copy>Copy link</button></div>
        <p class="small muted" data-copied hidden>Link copied!</p>
      </div>
      <p><a href="/game-night">Try another Game Night case →</a></p>
      <form method="post" class="gn-restart" onsubmit="return confirm('Start a new game with another table? Your result stays in the hall of fame.');"><?= csrf_field() ?><input type="hidden" name="do" value="restart"><button class="linkbtn">Start a new game for another table</button></form>
    <?php endif; ?>
  <?php endif; ?>
</section>
<?php
    page_end();
}

// ===================== ESCAPE ROOMS =====================

function escape_index(): void {
    page_start(['title' => 'Free Online Escape Rooms – Play in Your Browser', 'path' => '/escape',
        'jsonld' => [['@context' => 'https://schema.org', '@type' => 'ItemList', 'name' => 'Free online escape rooms',
            'itemListElement' => array_values(array_map(fn($s, $k) => ['@type' => 'ListItem', 'position' => $k + 1, 'url' => url('/escape/' . $s), 'name' => escape_rooms()[$s]['title']], array_keys(escape_rooms()), array_keys(array_keys(escape_rooms()))))]],
        'description' => 'Free online escape rooms: point-and-click escape games you play in your browser at home – nothing to download. Search the rooms, crack the locks and escape before time runs out.']);
    ?>
<section class="gn-hero esc-hero" style="background-image:linear-gradient(90deg,rgba(20,17,14,.92) 0%,rgba(20,17,14,.7) 50%,rgba(20,17,14,.2) 100%),url('<?= e(escape_cover('the-sealed-tomb') ?? '') ?>')">
  <div class="wrap">
    <p class="kicker">Sixty minutes. Can you get out?</p>
    <h1>Free online escape rooms</h1>
    <p class="lead">Point-and-click escape games you play in your browser – an escape room at home, alone or together around one screen. Nothing to download – just a free sign-in to save your progress. Search the rooms, combine what you find, crack the locks and beat the clock.</p>
  </div>
</section>
<section class="wrap">
  <p>Browse: <a href="/free-escape-rooms-for-kids">escape rooms for kids</a> · <a href="/christmas-escape-room">Christmas escape rooms</a> · <a href="/classroom-escape-room">for the classroom</a></p>
  <div class="grid">
  <?php foreach (escape_rooms() as $slug => $r): ?>
    <?php $cv = escape_cover($slug); ?><article class="card<?= $cv ? ' has-cover' : '' ?>"><?php if ($cv): ?><a class="card-cover" href="/escape/<?= e($slug) ?>" tabindex="-1" aria-hidden="true"><img src="<?= e($cv) ?>" alt="" loading="lazy"></a><?php endif; ?><div class="card-top"><span class="badge">Level <?= (int)($r['level'] ?? 1) ?></span><span class="badge badge-crime">Escape room</span><span class="badge"><?= e($r['status']) ?></span></div>
      <h3><a href="/escape/<?= e($slug) ?>"><?= e($r['title']) ?></a></h3><p><?= e($r['teaser']) ?></p>
      <p class="card-stats"><?= $r['minutes'] ?> min · <?= e($r['players']) ?> players · <?= $r['rooms'] ?> rooms · <?= $r['puzzles'] ?> puzzles</p></article>
  <?php endforeach; ?>
  </div>
</section>
<?php
?>
<?= faq_block([
  ['Are these online escape rooms free?', 'Yes, every escape room on Six Clues is free to play in your browser. There is nothing to download – you only sign in (free, with Google or your email) so your progress and time are saved.'],
  ['How long does an online escape room take?', 'Most rooms are designed for about 60 minutes. You can pause and come back later – your progress is saved to your free account.'],
  ['Can I play an escape room at home with friends?', 'Yes. Gather around one screen – a laptop, tablet or TV – and solve the puzzles together. They work on phones too.'],
  ['What if we get stuck?', 'Every room has hints. Use as many as you like – but the fewer you use, the better your time.'],
]) ?>
<?php
    page_end();
}

function escape_landing(string $slug): void {
    $r = escape_room($slug);
    if (!$r) { not_found(); return; }
    $u = current_user();
    $run = $u ? escape_run((int)$u['id'], $slug) : null;
    $board = escape_board($slug);
    page_start(['title' => $r['title'] . ' – free online escape room (level ' . (int)($r['level'] ?? 1) . ')', 'path' => '/escape/' . $slug, 'description' => $r['teaser'] . ' A free ' . $r['minutes'] . '-minute online escape room for ' . $r['players'] . ' players – play in your browser.',
        'og_image' => is_file(__DIR__ . '/assets/img/escape/' . $slug . '/og.jpg') ? '/assets/img/escape/' . $slug . '/og.jpg' : escape_cover($slug),
        'jsonld' => [['@context' => 'https://schema.org', '@type' => 'Game', 'name' => $r['title'], 'description' => $r['teaser'], 'url' => url('/escape/' . $slug), 'genre' => 'Escape room', 'isAccessibleForFree' => true, 'inLanguage' => 'en', 'publisher' => ['@type' => 'Organization', 'name' => cfg('site_name')]]]]);
    ?>
<?php $cv = escape_cover($slug); ?>
<section class="gn-hero esc-hero"<?= $cv ? ' style="background-image:linear-gradient(90deg,rgba(20,17,14,.92) 0%,rgba(20,17,14,.75) 45%,rgba(20,17,14,.25) 100%),url(\'' . e($cv) . '\')"' : '' ?>>
  <div class="wrap">
    <nav class="crumbs crumbs-light"><a href="/escape">Escape rooms</a> › <?= e($r['title']) ?></nav>
    <h1><?= e($r['title']) ?></h1>
    <p class="gn-tagline"><?= e($r['tagline']) ?></p>
    <ul class="gn-facts"><li>⭐ Level <?= (int)($r['level'] ?? 1) ?></li><li>⏱ <?= $r['minutes'] ?> minutes</li><li>👥 <?= e($r['players']) ?> players</li><li>🚪 <?= $r['rooms'] ?> rooms</li><li>🔒 <?= $r['puzzles'] ?> puzzles</li></ul>
    <p class="cta-row">
      <?php if (!$u): ?><a class="btn btn-big" href="/login?next=/escape/<?= e($slug) ?>/play">Sign in to play – it's free</a>
      <?php else: ?><a class="btn btn-big" href="/escape/<?= e($slug) ?>/play"><?= $run && !$run['finished_at'] ? 'Continue your escape' : 'Start the escape' ?></a><?php endif; ?>
    </p>
  </div>
</section>
<section class="wrap narrow case">
  <h2>The story</h2>
  <p><?= e($r['teaser']) ?></p>
  <?php if ($cv): ?><img class="esc-shot" src="<?= e($cv) ?>" alt="<?= e($r['title']) ?> – the first room" loading="lazy"><?php endif; ?>
  <h2>How to play</h2>
  <ul>
    <li>Click things in the room to look closer. Pick up what you find – it goes into your inventory at the bottom.</li>
    <li>To use an item, tap it in the inventory and then tap where to use it. Tap one item and then another to combine them.</li>
    <li>Everything you read is saved in your notebook. Stuck? A hint costs 3 minutes, the answer 5.</li>
    <li>Need a break? Press pause – the screen goes dark and the clock stops.</li>
  </ul>
  <h2>Fastest escapes</h2>
  <?php if ($board): ?>
  <div class="table-wrap"><table><thead><tr><th class="num">#</th><th>Detective</th><th class="num">Time</th></tr></thead><tbody>
  <?php foreach ($board as $n => $b): ?><tr><td class="num"><?= $n + 1 ?></td><td><?= e($b['alias'] ?: (first_name((string)$b['name']) ?: 'A detective')) ?></td><td class="num"><?= escape_clock((int)$b['t']) ?></td></tr><?php endforeach; ?>
  </tbody></table></div>
  <?php else: ?><p>Nobody has escaped yet. Will you be the first?</p><?php endif; ?>
</section>
<?= pin_box('esc-' . $slug, '/escape/' . $slug, 'Free online escape room: ' . $r['title'] . ' – play in your browser.') ?>
<?php
    page_end();
}

function escape_play(string $slug): void {
    $r = escape_room($slug);
    if (!$r) { not_found(); return; }
    $u = current_user();
    if (!$u) redirect('/login?next=/escape/' . $slug . '/play');
    $uid = (int)$u['id'];
    $pdo = db();
    if (($_SERVER['REQUEST_METHOD'] ?? '') === 'POST') {
        header('Content-Type: application/json');
        $in = json_decode((string)file_get_contents('php://input'), true) ?: [];
        if (!hash_equals((string)($_SESSION['csrf'] ?? ''), (string)($in['csrf'] ?? ''))) { http_response_code(403); echo '{"ok":false}'; return; }
        $run = escape_run($uid, $slug);
        $do = (string)($in['do'] ?? '');
        if ($do === 'restart') {
            if ($run) $pdo->prepare('UPDATE escape_runs SET active = 0 WHERE id = ?')->execute([$run['id']]);
            $run = null;
        }
        if (!$run && in_array($do, ['save', 'restart', 'finish'], true)) {
            $pdo->prepare('INSERT INTO escape_runs (user_id, slug, state, started_at, updated_at) VALUES (?,?,?,?,?)')->execute([$uid, $slug, '{}', now(), now()]);
            $run = escape_run($uid, $slug);
        }
        $state = json_encode($in['state'] ?? new stdClass());
        if (strlen($state) > 60000) { http_response_code(413); echo '{"ok":false}'; return; }
        if ($do === 'save' || $do === 'finish') $pdo->prepare('UPDATE escape_runs SET state = ?, updated_at = ? WHERE id = ?')->execute([$state, now(), $run['id']]);
        if ($do === 'finish' && !$run['finished_at']) {
            $t = (int)($in['time_ms'] ?? 0);
            $real = (time() - strtotime($run['started_at'] . ' UTC')) * 1000;
            // A finish counts only if the clock time is plausible: at least 3 minutes and not less than wall time allows.
            $ok = $t >= 180000 && $t <= $real + 600000 && empty($in['overtime']);
            $pdo->prepare('UPDATE escape_runs SET finished_at = ?, time_ms = ?, hints = ? WHERE id = ?')->execute([now(), $ok ? $t : null, (int)($in['hints'] ?? 0), $run['id']]);
            log_event('escape_finished', $slug);
        }
        echo json_encode(['ok' => true]);
        return;
    }
    $run = escape_run($uid, $slug);
    $state = $run ? (json_decode($run['state'], true) ?: new stdClass()) : new stdClass();
    if ($run && $run['finished_at']) $state = new stdClass();   // finished: a new run starts fresh
    if ($run && $run['finished_at']) { $pdo->prepare('UPDATE escape_runs SET active = 0 WHERE id = ?')->execute([$run['id']]); }
    ?><!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title><?= e($r['title']) ?> – Six Clues escape room</title><meta name="robots" content="noindex">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/css/escape.css?v=4">
</head><body>
<div id="escape" data-slug="<?= e($slug) ?>" data-csrf="<?= e(csrf_token()) ?>" data-name="<?= e(first_name((string)$u['name'])) ?>"></div>
<script>window.ESCAPE_STATE = <?= json_encode($state, JSON_HEX_TAG | JSON_HEX_AMP) ?>;</script>
<script src="/assets/js/escape-engine.js?v=3"></script>
<script src="/assets/js/escape-<?= e($slug) ?>.js?v=14"></script>
</body></html>
<?php
}


// ===================== LIBRARY (/mysteries) =====================
function library(): void {
    $u = current_user();
    $prog = $u ? user_progress((int)$u['id']) : [];
    $all = mysteries();
    page_start(['title' => 'Free Murder Mystery Games – Whodunit Puzzles to Play or Print', 'path' => '/mysteries',
        'description' => count($all) . ' free murder mystery games and detective puzzles. Play each whodunit online clue by clue, or print the six clue posters for a mystery party at home, school or the office.',
        'jsonld' => [['@context' => 'https://schema.org', '@type' => 'ItemList', 'name' => 'Free murder mystery games',
            'itemListElement' => array_map(fn($m, $k) => ['@type' => 'ListItem', 'position' => $k + 1, 'url' => url('/mysteries/' . $m['slug']), 'name' => $m['title']], $all, array_keys($all))]]]);
    ?>
<section class="wrap">
  <h1>Free murder mystery games</h1>
  <p class="lead">Every case is a complete whodunit: six clues, a handful of suspects and one culprit. Play online clue by clue – the fewer clues you need, the more points you score – or print the six clue posters and turn your living room, classroom or office into a crime scene.</p>
  <p>Easy cases (level 1) take 5–10 minutes; level 3 “Mastermind” cases hide the truth across four or more documents. New cases arrive as the <a href="/daily">daily mystery</a>, and there are longer <a href="/game-night">Game Night</a> cases for 2–6 players and free <a href="/escape">online escape rooms</a>.</p>
  <?php filter_bar((bool)$u); ?>
  <div class="grid" data-grid><?php foreach ($all as $m) echo mystery_card($m, $prog); ?></div>
  <p class="empty" data-empty hidden>No cases match – try another search or filter.</p>
</section>
<?php
    page_end();
}
