<?php
declare(strict_types=1);
/*
 * The on-screen detective game: clues are revealed one at a time, the first accusation is the ranked one,
 * fewer clues = more points. Guests can play; the first FREE_RESULTS results are shown straight away,
 * after that the answer is locked in and shown once the player signs in (their guest plays move to the account).
 */

const POINTS = [1 => 100, 2 => 85, 3 => 70, 4 => 55, 5 => 40, 6 => 25];
const FREE_RESULTS = 2;
const LAUNCH_DATE = '2026-11-15';

function today(): string { return (new DateTime('now', new DateTimeZone('Europe/Copenhagen')))->format('Y-m-d'); }
function cph_date(string $utc): string {
    return (new DateTime($utc, new DateTimeZone('UTC')))->setTimezone(new DateTimeZone('Europe/Copenhagen'))->format('Y-m-d');
}
function daily_no(string $date): int { return (int)((strtotime($date) - strtotime(LAUNCH_DATE)) / 86400) + 1; }
function daily_mystery(?string $date = null): ?array {
    $date ??= today();
    foreach (mysteries() as $m) if (($m['daily'] ?? '') === $date) return $m;
    return null;
}
/** Today's daily case, or – if there is none – a library case featured for the day. */
function featured_mystery(): ?array {
    if ($d = daily_mystery()) return $d;
    $lib = array_values(array_filter(mysteries(), fn($m) => empty($m['daily']) && $m['level'] <= 2));
    return $lib ? $lib[crc32(today()) % count($lib)] : null;
}

function game_migrate(PDO $pdo, string $id, string $engine): void {
    $pdo->exec("CREATE TABLE IF NOT EXISTS plays (
        id $id,
        slug VARCHAR(100) NOT NULL,
        user_id INT NULL,
        guest_id VARCHAR(40) NULL,
        mode VARCHAR(10) NOT NULL DEFAULT 'screen',
        clues TINYINT NOT NULL DEFAULT 1,
        started_at DATETIME NOT NULL,
        answered_at DATETIME NULL,
        guess VARCHAR(255) NULL,
        correct TINYINT NULL,
        points INT NULL,
        ms INT NULL,
        challenge VARCHAR(12) NULL,
        revealed TINYINT NOT NULL DEFAULT 0
    )$engine");
    $pdo->exec('CREATE INDEX IF NOT EXISTS plays_slug ON plays (slug)');
    $pdo->exec('CREATE INDEX IF NOT EXISTS plays_user ON plays (user_id)');
    $pdo->exec('CREATE INDEX IF NOT EXISTS plays_guest ON plays (guest_id)');
    $pdo->exec("CREATE TABLE IF NOT EXISTS challenges (
        code VARCHAR(12) NOT NULL PRIMARY KEY,
        slug VARCHAR(100) NOT NULL,
        user_id INT NULL,
        guest_id VARCHAR(40) NULL,
        parent VARCHAR(12) NULL,
        created_at DATETIME NOT NULL
    )$engine");
    $pdo->exec("CREATE TABLE IF NOT EXISTS events (
        id $id, type VARCHAR(40) NOT NULL, ref VARCHAR(100) NULL, who VARCHAR(40) NULL, created_at DATETIME NOT NULL
    )$engine");
    $pdo->exec('CREATE INDEX IF NOT EXISTS events_type ON events (type, created_at)');
    $pdo->exec("CREATE TABLE IF NOT EXISTS friends (
        a INT NOT NULL, b INT NOT NULL, created_at DATETIME NOT NULL, PRIMARY KEY (a, b)
    )$engine");
}

// ---------- who is playing ----------
function guest_id(bool $create = false): ?string {
    $g = $_COOKIE['sc_g'] ?? '';
    if (preg_match('/^[a-f0-9]{32}$/', $g)) return $g;
    if (!$create) return null;
    $g = bin2hex(random_bytes(16));
    setcookie('sc_g', $g, ['expires' => time() + 400 * 86400, 'path' => '/', 'secure' => !empty($_SERVER['HTTPS']), 'httponly' => true, 'samesite' => 'Lax']);
    $_COOKIE['sc_g'] = $g;
    return $g;
}
/** The current player's ranked play for a mystery (the first one), or null. */
function my_play(string $slug): ?array {
    $u = current_user();
    if ($u) { $st = db()->prepare('SELECT * FROM plays WHERE slug = ? AND user_id = ? ORDER BY id LIMIT 1'); $st->execute([$slug, $u['id']]); }
    elseif ($g = guest_id()) { $st = db()->prepare('SELECT * FROM plays WHERE slug = ? AND guest_id = ? AND user_id IS NULL ORDER BY id LIMIT 1'); $st->execute([$slug, $g]); }
    else return null;
    return $st->fetch() ?: null;
}
function guest_revealed_count(string $g): int {
    $st = db()->prepare('SELECT COUNT(*) FROM plays WHERE guest_id = ? AND user_id IS NULL AND revealed = 1');
    $st->execute([$g]);
    return (int)$st->fetchColumn();
}

// ---------- playing ----------
function start_play(string $slug, ?string $challenge): array {
    if ($p = my_play($slug)) return $p;
    $u = current_user();
    $g = $u ? null : guest_id(true);
    db()->prepare('INSERT INTO plays (slug, user_id, guest_id, mode, clues, started_at, challenge) VALUES (?,?,?,?,?,?,?)')
        ->execute([$slug, $u['id'] ?? null, $g, 'screen', 1, now(), $challenge]);
    return my_play($slug);
}
function reveal_clue(array $p): void {
    if ($p['answered_at'] || $p['clues'] >= 6) return;
    db()->prepare('UPDATE plays SET clues = clues + 1 WHERE id = ? AND answered_at IS NULL')->execute([$p['id']]);
}
function accuse(array $p, array $m, string $guess): array {
    if ($p['answered_at']) return $p;
    $ok = $guess === $m['solution']['killer'];
    $pts = $ok ? POINTS[(int)$p['clues']] : 0;
    $ms = (int)((time() - strtotime($p['started_at'] . ' UTC')) * 1000);
    $u = current_user();
    $revealed = $u ? 1 : (guest_revealed_count((string)$p['guest_id']) < FREE_RESULTS ? 1 : 0);
    db()->prepare('UPDATE plays SET answered_at = ?, guess = ?, correct = ?, points = ?, ms = ?, revealed = ? WHERE id = ?')
        ->execute([now(), $guess, $ok ? 1 : 0, $pts, $ms, $revealed, $p['id']]);
    if ($u) record_classic((int)$u['id'], $m['slug'], $guess, $ok);
    if ($u && $p['challenge']) link_friends_by_challenge((string)$p['challenge'], (int)$u['id']);
    return my_play($m['slug']);
}
/** Keeps the older progress tables (solved list, reviews, case statistics) in step with ranked plays. */
function record_classic(int $uid, string $slug, string $guess, bool $ok): void {
    $pdo = db();
    $pdo->prepare('INSERT INTO attempts (user_id, slug, guess, correct, created_at) VALUES (?,?,?,?,?)')->execute([$uid, $slug, $guess, $ok ? 1 : 0, now()]);
    if ($ok) {
        $st = $pdo->prepare('SELECT 1 FROM solves WHERE user_id = ? AND slug = ?'); $st->execute([$uid, $slug]);
        if (!$st->fetchColumn()) {
            $n = $pdo->prepare('SELECT COUNT(*) FROM attempts WHERE user_id = ? AND slug = ?'); $n->execute([$uid, $slug]);
            $pdo->prepare('INSERT INTO solves (user_id, slug, solved_at, attempts, gave_up) VALUES (?,?,?,?,0)')->execute([$uid, $slug, now(), (int)$n->fetchColumn()]);
        }
    }
}
/** A first answer given on the printed version counts as a ranked play with all six clues. */
function record_print_play(int $uid, string $slug, string $guess, bool $ok): void {
    $st = db()->prepare('SELECT 1 FROM plays WHERE slug = ? AND user_id = ?'); $st->execute([$slug, $uid]);
    if ($st->fetchColumn()) return;
    db()->prepare('INSERT INTO plays (slug, user_id, mode, clues, started_at, answered_at, guess, correct, points, revealed) VALUES (?,?,?,?,?,?,?,?,?,1)')
        ->execute([$slug, $uid, 'print', 6, now(), now(), $guess, $ok ? 1 : 0, $ok ? POINTS[6] : 0]);
}

/** After sign-in: move this browser's guest plays to the account (unless the account already played that case). */
function merge_guest_plays(int $uid): void {
    $g = guest_id();
    if (!$g) return;
    $pdo = db();
    $st = $pdo->prepare('SELECT * FROM plays WHERE guest_id = ? AND user_id IS NULL'); $st->execute([$g]);
    foreach ($st->fetchAll() as $p) {
        $has = $pdo->prepare('SELECT 1 FROM plays WHERE slug = ? AND user_id = ?'); $has->execute([$p['slug'], $uid]);
        if ($has->fetchColumn()) continue;
        $pdo->prepare('UPDATE plays SET user_id = ?, revealed = CASE WHEN answered_at IS NULL THEN 0 ELSE 1 END WHERE id = ?')->execute([$uid, $p['id']]);
        if ($p['answered_at']) {
            record_classic($uid, $p['slug'], (string)$p['guess'], (bool)$p['correct']);
            if ($p['challenge']) link_friends_by_challenge((string)$p['challenge'], $uid);
        }
    }
    $pdo->prepare('UPDATE challenges SET user_id = ? WHERE guest_id = ? AND user_id IS NULL')->execute([$uid, $g]);
}

// ---------- results ----------
function percentile(array $p): ?int {
    $st = db()->prepare('SELECT COUNT(*) n, SUM(CASE WHEN points < ? THEN 1 ELSE 0 END) below FROM plays WHERE slug = ? AND answered_at IS NOT NULL AND id <> ?');
    $st->execute([(int)$p['points'], $p['slug'], $p['id']]);
    $r = $st->fetch();
    return (int)$r['n'] >= 3 ? (int)round($r['below'] / $r['n'] * 100) : null;
}
/** Days in a row with the daily case answered on its own day. One missed day per 7 is forgiven. */
function streak(int $uid): int {
    $st = db()->prepare('SELECT slug, answered_at FROM plays WHERE user_id = ? AND answered_at IS NOT NULL');
    $st->execute([$uid]);
    $days = [];
    foreach ($st->fetchAll() as $r) {
        $m = mystery($r['slug']);
        if ($m && ($m['daily'] ?? '') === cph_date($r['answered_at'])) $days[$m['daily']] = true;
    }
    $d = new DateTime(today());
    if (!isset($days[$d->format('Y-m-d')])) $d->modify('-1 day');
    $n = 0; $lastForgive = -99; $i = 0;
    while ($d->format('Y-m-d') >= LAUNCH_DATE) {
        if (isset($days[$d->format('Y-m-d')])) $n++;
        elseif ($i - $lastForgive >= 7 && $n > 0) $lastForgive = $i;
        else break;
        $d->modify('-1 day'); $i++;
    }
    return $n;
}
function player_name(?int $uid): string {
    if (!$uid) return 'A detective';
    $st = db()->prepare('SELECT name FROM users WHERE id = ?'); $st->execute([$uid]);
    $n = first_name((string)$st->fetchColumn());
    return $n !== '' ? $n : 'A detective';
}

// ---------- challenges and friends ----------
function create_challenge(string $slug, ?string $parent = null): string {
    $u = current_user();
    $g = $u ? null : guest_id(true);
    $st = db()->prepare('SELECT code FROM challenges WHERE slug = ? AND ' . ($u ? 'user_id = ?' : 'guest_id = ? AND user_id IS NULL') . ' ORDER BY created_at LIMIT 1');
    $st->execute([$slug, $u['id'] ?? $g]);
    if ($c = $st->fetchColumn()) return (string)$c;
    $alphabet = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
    do {
        $code = ''; for ($i = 0; $i < 6; $i++) $code .= $alphabet[random_int(0, strlen($alphabet) - 1)];
        $ex = db()->prepare('SELECT 1 FROM challenges WHERE code = ?'); $ex->execute([$code]);
    } while ($ex->fetchColumn());
    db()->prepare('INSERT INTO challenges (code, slug, user_id, guest_id, parent, created_at) VALUES (?,?,?,?,?,?)')
        ->execute([$code, $slug, $u['id'] ?? null, $g, $parent, now()]);
    return $code;
}
function challenge(string $code): ?array {
    $st = db()->prepare('SELECT * FROM challenges WHERE code = ?'); $st->execute([strtoupper($code)]);
    return $st->fetch() ?: null;
}
/** The challenger's ranked play for the challenge's mystery. */
function challenger_play(array $c): ?array {
    if ($c['user_id']) { $st = db()->prepare('SELECT * FROM plays WHERE slug = ? AND user_id = ? ORDER BY id LIMIT 1'); $st->execute([$c['slug'], $c['user_id']]); }
    else { $st = db()->prepare('SELECT * FROM plays WHERE slug = ? AND guest_id = ? ORDER BY id LIMIT 1'); $st->execute([$c['slug'], $c['guest_id']]); }
    return $st->fetch() ?: null;
}
function link_friends_by_challenge(string $code, int $uid): void {
    $c = challenge($code);
    if (!$c || !$c['user_id'] || (int)$c['user_id'] === $uid) return;
    $a = min($uid, (int)$c['user_id']); $b = max($uid, (int)$c['user_id']);
    $st = db()->prepare('SELECT 1 FROM friends WHERE a = ? AND b = ?'); $st->execute([$a, $b]);
    if (!$st->fetchColumn()) db()->prepare('INSERT INTO friends (a, b, created_at) VALUES (?,?,?)')->execute([$a, $b, now()]);
}
/** Who won: 1 = player a, -1 = player b, 0 = draw. Fewer clues wins, then faster time. */
function duel(array $a, array $b): int {
    if ((int)$a['correct'] !== (int)$b['correct']) return (int)$a['correct'] ? 1 : -1;
    if (!(int)$a['correct']) return 0;
    if ((int)$a['clues'] !== (int)$b['clues']) return (int)$a['clues'] < (int)$b['clues'] ? 1 : -1;
    if ((int)$a['ms'] && (int)$b['ms'] && (int)$a['ms'] !== (int)$b['ms']) return (int)$a['ms'] < (int)$b['ms'] ? 1 : -1;
    return 0;
}
function friend_ids(int $uid): array {
    $st = db()->prepare('SELECT CASE WHEN a = ? THEN b ELSE a END f FROM friends WHERE a = ? OR b = ?');
    $st->execute([$uid, $uid, $uid]);
    return array_map('intval', array_column($st->fetchAll(), 'f'));
}

// ---------- leaderboards ----------
/** Points per player. $since (UTC) limits to plays answered after it; $ids limits to those users. */
function board(?string $since = null, ?array $ids = null, bool $optedIn = true, int $limit = 25): array {
    $sql = 'SELECT p.user_id, SUM(p.points) pts, SUM(p.correct) solved, COUNT(*) played, AVG(CASE WHEN p.correct = 1 THEN p.clues END) avg_clues, u.name, l.alias
            FROM plays p JOIN users u ON u.id = p.user_id LEFT JOIN leaderboard l ON l.user_id = p.user_id
            WHERE p.answered_at IS NOT NULL AND p.user_id IS NOT NULL';
    $args = [];
    if ($since) { $sql .= ' AND p.answered_at >= ?'; $args[] = $since; }
    if ($ids !== null) { if (!$ids) return []; $sql .= ' AND p.user_id IN (' . implode(',', array_map('intval', $ids)) . ')'; }
    if ($optedIn) $sql .= ' AND l.alias IS NOT NULL';
    $sql .= ' GROUP BY p.user_id, u.name, l.alias ORDER BY pts DESC, solved DESC LIMIT ' . (int)$limit;
    $st = db()->prepare($sql); $st->execute($args);
    return $st->fetchAll();
}
function week_start_utc(): string {
    $d = new DateTime('monday this week', new DateTimeZone('Europe/Copenhagen'));
    if ((new DateTime('now', new DateTimeZone('Europe/Copenhagen')))->format('N') === '1') $d = new DateTime('today', new DateTimeZone('Europe/Copenhagen'));
    return $d->setTimezone(new DateTimeZone('UTC'))->format('Y-m-d H:i:s');
}
function clues_txt(array $p): string { return (int)$p['correct'] ? (int)$p['clues'] . ((int)$p['clues'] === 1 ? ' clue' : ' clues') : 'wrong'; }

/** Light first-party event log for the growth dashboard (no personal data beyond an opaque player key). */
function log_event(string $type, ?string $ref = null): void {
    $u = current_user();
    $who = $u ? 'u' . $u['id'] : (($g = guest_id()) ? 'g' . substr($g, 0, 12) : null);
    try { db()->prepare('INSERT INTO events (type, ref, who, created_at) VALUES (?,?,?,?)')->execute([$type, $ref, $who, now()]); } catch (Throwable $e) {}
}

/** Numbers for the admin growth dashboard. */
function growth_stats(): array {
    $pdo = db();
    $d7 = gmdate('Y-m-d H:i:s', time() - 7 * 86400);
    $one = fn(string $sql, array $a = []) => (function () use ($pdo, $sql, $a) { $s = $pdo->prepare($sql); $s->execute($a); return $s->fetchColumn(); })();
    $pk = "COALESCE('u' || user_id, 'g' || guest_id)";
    $started = (int)$one('SELECT COUNT(*) FROM plays WHERE mode = \'screen\' AND started_at >= ?', [$d7]);
    $done = (int)$one('SELECT COUNT(*) FROM plays WHERE mode = \'screen\' AND started_at >= ? AND answered_at IS NOT NULL', [$d7]);
    $players7 = (int)$one("SELECT COUNT(DISTINCT $pk) FROM plays WHERE started_at >= ?", [$d7]);
    $chal = (int)$one('SELECT COUNT(*) FROM challenges WHERE created_at >= ?', [$d7]);
    $shared = (int)$one("SELECT COUNT(*) FROM events WHERE type = 'challenge_shared' AND created_at >= ?", [$d7]);
    $opens = (int)$one("SELECT COUNT(*) FROM events WHERE type = 'challenge_opened' AND created_at >= ?", [$d7]);
    $viaChal = (int)$one('SELECT COUNT(*) FROM plays WHERE challenge IS NOT NULL AND started_at >= ?', [$d7]);
    // New players whose very first play came from a challenge link
    $firsts = $pdo->query("SELECT $pk k, MIN(id) first_id FROM plays GROUP BY $pk")->fetchAll();
    $ids = array_column($firsts, 'first_id');
    $newTotal = 0; $newViral = 0; $cohort = 0; $returned = 0;
    if ($ids) {
        $rows = $pdo->query('SELECT id, user_id, guest_id, started_at, challenge FROM plays WHERE id IN (' . implode(',', array_map('intval', $ids)) . ')')->fetchAll();
        $c0 = time() - 14 * 86400; $c1 = time() - 7 * 86400;
        foreach ($rows as $r) {
            $t = strtotime($r['started_at'] . ' UTC');
            if ($t >= time() - 7 * 86400) { $newTotal++; if ($r['challenge']) $newViral++; }
            if ($t >= $c0 && $t < $c1) {
                $cohort++;
                $q = $pdo->prepare('SELECT 1 FROM plays WHERE ' . ($r['user_id'] ? 'user_id = ?' : 'guest_id = ?') . ' AND started_at >= ? LIMIT 1');
                $q->execute([$r['user_id'] ?: $r['guest_id'], gmdate('Y-m-d H:i:s', $t + 7 * 86400)]);
                if ($q->fetchColumn()) $returned++;
            }
        }
    }
    $pct = fn($a, $b) => $b ? (int)round($a / $b * 100) : null;
    // Last 14 days
    $days = [];
    for ($i = 13; $i >= 0; $i--) {
        $from = gmdate('Y-m-d 00:00:00', time() - $i * 86400); $to = gmdate('Y-m-d 23:59:59', time() - $i * 86400);
        $days[] = [
            'day' => gmdate('D j M', time() - $i * 86400),
            'players' => (int)$one("SELECT COUNT(DISTINCT $pk) FROM plays WHERE started_at BETWEEN ? AND ?", [$from, $to]),
            'plays' => (int)$one('SELECT COUNT(*) FROM plays WHERE started_at BETWEEN ? AND ?', [$from, $to]),
            'done' => (int)$one('SELECT COUNT(*) FROM plays WHERE answered_at BETWEEN ? AND ?', [$from, $to]),
            'signups' => (int)$one('SELECT COUNT(*) FROM users WHERE created_at BETWEEN ? AND ?', [$from, $to]),
            'challenges' => (int)$one('SELECT COUNT(*) FROM challenges WHERE created_at BETWEEN ? AND ?', [$from, $to]),
        ];
    }
    return [
        'players_today' => $days[13]['players'],
        'players_7' => $players7,
        'completion' => $pct($done, $started), 'started' => $started, 'done' => $done,
        'd7' => $pct($returned, $cohort), 'cohort' => $cohort,
        'challenge_rate' => $pct($chal, $done), 'challenges' => $chal, 'shared' => $shared,
        'invite_conv' => $pct($viaChal, $opens), 'opens' => $opens, 'via' => $viaChal,
        'viral' => $players7 ? round($newViral / $players7, 2) : null, 'new' => $newTotal, 'new_viral' => $newViral,
        'signups_7' => (int)$one('SELECT COUNT(*) FROM users WHERE created_at >= ?', [$d7]),
        'gate_locks' => (int)$one('SELECT COUNT(*) FROM plays WHERE revealed = 0 AND answered_at IS NOT NULL AND user_id IS NULL'),
        'days' => $days,
    ];
}
