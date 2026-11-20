<?php
declare(strict_types=1);

$cfgFile = __DIR__ . '/config.php';
if (!is_file($cfgFile)) {
    http_response_code(500);
    exit('Missing app/config.php – copy app/config.sample.php and fill it in.');
}
$CFG = require $cfgFile;

require_once __DIR__ . '/smtp.php';
function cfg(string $k, $default = null) { global $CFG; return $CFG[$k] ?? $default; }
function e($s): string { return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8'); }
function url(string $path = '/'): string { return rtrim((string)cfg('base_url'), '/') . $path; }
function redirect(string $path): never { header('Location: ' . $path, true, 303); exit; }

// ---------- session ----------
$secure = (($_SERVER['HTTPS'] ?? '') === 'on') || (($_SERVER['HTTP_X_FORWARDED_PROTO'] ?? '') === 'https');
session_name('sixclues');
session_set_cookie_params(['lifetime' => 60 * 60 * 24 * 60, 'path' => '/', 'secure' => $secure, 'httponly' => true, 'samesite' => 'Lax']);
session_start();

function csrf_token(): string {
    if (empty($_SESSION['csrf'])) $_SESSION['csrf'] = bin2hex(random_bytes(16));
    return $_SESSION['csrf'];
}
function csrf_field(): string { return '<input type="hidden" name="csrf" value="' . e(csrf_token()) . '">'; }
function csrf_check(): void {
    if (!hash_equals($_SESSION['csrf'] ?? '', (string)($_POST['csrf'] ?? ''))) {
        http_response_code(400);
        exit('Your session expired. Please go back and try again.');
    }
}
function flash(?string $msg = null): ?string {
    if ($msg !== null) { $_SESSION['flash'] = $msg; return null; }
    $m = $_SESSION['flash'] ?? null; unset($_SESSION['flash']); return $m;
}

// ---------- database ----------
function db(): PDO {
    static $pdo = null;
    if ($pdo) return $pdo;
    $dsn = (string)cfg('db_dsn');
    if (str_starts_with($dsn, 'sqlite:')) {
        $dir = dirname(substr($dsn, 7));
        if (!is_dir($dir)) @mkdir($dir, 0700, true);
    }
    $pdo = new PDO($dsn, (string)cfg('db_user', ''), (string)cfg('db_pass', ''), [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
    migrate($pdo);
    return $pdo;
}

function migrate(PDO $pdo): void {
    $mysql = $pdo->getAttribute(PDO::ATTR_DRIVER_NAME) === 'mysql';
    $id = $mysql ? 'INT UNSIGNED AUTO_INCREMENT PRIMARY KEY' : 'INTEGER PRIMARY KEY AUTOINCREMENT';
    $engine = $mysql ? ' ENGINE=InnoDB DEFAULT CHARSET=utf8mb4' : '';
    $pdo->exec("CREATE TABLE IF NOT EXISTS users (
        id $id,
        google_sub VARCHAR(64) NOT NULL UNIQUE,
        email VARCHAR(255) NOT NULL,
        name VARCHAR(255) NOT NULL DEFAULT '',
        picture VARCHAR(500) NOT NULL DEFAULT '',
        newsletter TINYINT NOT NULL DEFAULT 0,
        newsletter_at DATETIME NULL,
        source VARCHAR(100) NOT NULL DEFAULT '',
        created_at DATETIME NOT NULL,
        last_login_at DATETIME NOT NULL
    )$engine");
    $pdo->exec("CREATE TABLE IF NOT EXISTS attempts (
        id $id,
        user_id INT NOT NULL,
        slug VARCHAR(100) NOT NULL,
        guess VARCHAR(100) NOT NULL,
        correct TINYINT NOT NULL,
        created_at DATETIME NOT NULL
    )$engine");
    $pdo->exec("CREATE TABLE IF NOT EXISTS login_tokens (
        token_hash CHAR(64) NOT NULL PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        name VARCHAR(255) NOT NULL DEFAULT '',
        newsletter TINYINT NOT NULL DEFAULT 0,
        next_path VARCHAR(255) NOT NULL DEFAULT '/me',
        expires_at DATETIME NOT NULL,
        created_at DATETIME NOT NULL
    )$engine");
    $pdo->exec("CREATE TABLE IF NOT EXISTS newsletters (
        id $id,
        subject VARCHAR(255) NOT NULL,
        body TEXT NOT NULL,
        recipients INT NOT NULL DEFAULT 0,
        sent_at DATETIME NOT NULL
    )$engine");
    $pdo->exec("CREATE TABLE IF NOT EXISTS reviews (
        user_id INT NOT NULL,
        slug VARCHAR(100) NOT NULL,
        stars TINYINT NOT NULL,
        body VARCHAR(400) NOT NULL DEFAULT '',
        show_name TINYINT NOT NULL DEFAULT 0,
        approved TINYINT NOT NULL DEFAULT 0,
        created_at DATETIME NOT NULL,
        PRIMARY KEY (user_id, slug)
    )$engine");
    game_migrate($pdo, $id, $engine);
    gn_migrate($pdo, $id, $engine);
    escape_migrate($pdo, $id, $engine);
    $pdo->exec("CREATE TABLE IF NOT EXISTS remember_tokens (id $id, user_id INT NOT NULL, selector VARCHAR(24) NOT NULL UNIQUE, token_hash CHAR(64) NOT NULL, expires_at DATETIME NOT NULL)$engine");
    $pdo->exec("CREATE TABLE IF NOT EXISTS leaderboard (
        user_id INT NOT NULL PRIMARY KEY,
        alias VARCHAR(40) NOT NULL,
        created_at DATETIME NOT NULL
    )$engine");
    $pdo->exec("CREATE TABLE IF NOT EXISTS solves (
        user_id INT NOT NULL,
        slug VARCHAR(100) NOT NULL,
        solved_at DATETIME NOT NULL,
        attempts INT NOT NULL DEFAULT 1,
        gave_up TINYINT NOT NULL DEFAULT 0,
        PRIMARY KEY (user_id, slug)
    )$engine");
}
function now(): string { return gmdate('Y-m-d H:i:s'); }

// ---------- mysteries ----------
function mysteries(): array {
    static $all = null;
    if ($all === null) {
        $t = today();
        // A case goes public on its own day (as the daily case). Admins can preview upcoming cases.
        $all = array_values(array_filter(require __DIR__ . '/mysteries.php', fn($m) => ($m['public'] ?? '') <= $t || is_admin_session()));
    }
    return $all;
}
function mystery(string $slug): ?array {
    foreach (mysteries() as $m) if ($m['slug'] === $slug) return $m;
    return null;
}
function level_name(int $l): string { return [1 => 'Rookie', 2 => 'Detective', 3 => 'Mastermind'][$l] ?? "Level $l"; }

// ---------- users ----------
function current_user(): ?array {
    static $u = false;
    if ($u !== false) return $u;
    $u = null;
    if (empty($_SESSION['uid'])) remember_restore();
    if (!empty($_SESSION['uid'])) {
        $st = db()->prepare('SELECT * FROM users WHERE id = ?');
        $st->execute([$_SESSION['uid']]);
        $u = $st->fetch() ?: null;
    }
    return $u;
}
function is_admin_session(): bool {
    static $a = null;
    if ($a !== null) return $a;
    $a = false;
    if (empty($_SESSION['uid'])) return false;
    $st = db()->prepare('SELECT email FROM users WHERE id = ?'); $st->execute([$_SESSION['uid']]);
    return $a = in_array(strtolower((string)$st->fetchColumn()), array_map('strtolower', (array)cfg('admin_emails', [])), true);
}
function is_admin(): bool {
    $u = current_user();
    return $u && in_array(strtolower($u['email']), array_map('strtolower', (array)cfg('admin_emails', [])), true);
}
function login_user(array $p): void {
    $pdo = db();
    $st = $pdo->prepare('SELECT id FROM users WHERE google_sub = ?');
    $st->execute([$p['sub']]);
    $id = $st->fetchColumn();
    if (!$id) {
        $st = $pdo->prepare('SELECT id FROM users WHERE LOWER(email) = LOWER(?)');
        $st->execute([$p['email']]);
        $id = $st->fetchColumn();
        if ($id && str_starts_with($p['sub'], 'email:') === false) {
            $pdo->prepare('UPDATE users SET google_sub = ? WHERE id = ?')->execute([$p['sub'], $id]);
        }
    }
    if ($id) {
        $pdo->prepare("UPDATE users SET email = ?, name = CASE WHEN ? <> '' THEN ? ELSE name END, picture = CASE WHEN ? <> '' THEN ? ELSE picture END, last_login_at = ? WHERE id = ?")
            ->execute([$p['email'], $p['name'] ?? '', $p['name'] ?? '', $p['picture'] ?? '', $p['picture'] ?? '', now(), $id]);
        $_SESSION['ga_event'] = 'login';
    } else {
        $pdo->prepare('INSERT INTO users (google_sub, email, name, picture, source, created_at, last_login_at) VALUES (?,?,?,?,?,?,?)')
            ->execute([$p['sub'], $p['email'], $p['name'] ?? '', $p['picture'] ?? '', substr((string)($_SESSION['source'] ?? ''), 0, 100), now(), now()]);
        $id = $pdo->lastInsertId();
        $_SESSION['ga_event'] = 'sign_up';
    }
    session_regenerate_id(true);
    $_SESSION['uid'] = (int)$id;
    merge_guest_plays((int)$id);
    $want = $_POST['remember'] ?? ($_SESSION['remember_pref'] ?? '1');
    if ($want === '1') remember_issue((int)$id);
}

// ---------- "keep me signed in" (30 days, survives server-side session cleanup) ----------
const REMEMBER_DAYS = 30;
function remember_cookie(string $v, int $exp): void {
    $secure = (($_SERVER['HTTPS'] ?? '') === 'on') || (($_SERVER['HTTP_X_FORWARDED_PROTO'] ?? '') === 'https');
    setcookie('sx_remember', $v, ['expires' => $exp, 'path' => '/', 'secure' => $secure, 'httponly' => true, 'samesite' => 'Lax']);
}
function remember_issue(int $uid): void {
    $sel = bin2hex(random_bytes(9)); $tok = bin2hex(random_bytes(24)); $exp = time() + REMEMBER_DAYS * 86400;
    $pdo = db();
    $pdo->prepare('DELETE FROM remember_tokens WHERE expires_at < ?')->execute([now()]);
    $pdo->prepare('INSERT INTO remember_tokens (user_id, selector, token_hash, expires_at) VALUES (?,?,?,?)')->execute([$uid, $sel, hash('sha256', $tok), gmdate('Y-m-d H:i:s', $exp)]);
    remember_cookie($sel . ':' . $tok, $exp);
}
function remember_restore(): void {
    $c = (string)($_COOKIE['sx_remember'] ?? '');
    if (!preg_match('/^([a-f0-9]{18}):([a-f0-9]{48})$/', $c, $m)) return;
    $pdo = db();
    $st = $pdo->prepare('SELECT * FROM remember_tokens WHERE selector = ? AND expires_at >= ?');
    $st->execute([$m[1], now()]);
    $row = $st->fetch();
    if (!$row || !hash_equals($row['token_hash'], hash('sha256', $m[2]))) { remember_cookie('', time() - 3600); return; }
    // one-time token: rotate on use
    $pdo->prepare('DELETE FROM remember_tokens WHERE id = ?')->execute([$row['id']]);
    session_regenerate_id(true);
    $_SESSION['uid'] = (int)$row['user_id'];
    remember_issue((int)$row['user_id']);
}
function remember_clear(): void {
    $c = (string)($_COOKIE['sx_remember'] ?? '');
    if (preg_match('/^([a-f0-9]{18}):/', $c, $m)) db()->prepare('DELETE FROM remember_tokens WHERE selector = ?')->execute([$m[1]]);
    remember_cookie('', time() - 3600);
}

/** Verifies a Google Identity Services ID token with Google's tokeninfo endpoint. */
function verify_google_token(string $jwt): ?array {
    $ch = curl_init('https://oauth2.googleapis.com/tokeninfo?id_token=' . urlencode($jwt));
    curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 10]);
    $body = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    if ($code !== 200 || !$body) return null;
    $p = json_decode($body, true);
    if (!is_array($p)) return null;
    if (($p['aud'] ?? '') !== cfg('google_client_id')) return null;
    if (!in_array($p['iss'] ?? '', ['accounts.google.com', 'https://accounts.google.com'], true)) return null;
    if ((int)($p['exp'] ?? 0) < time()) return null;
    if (($p['email_verified'] ?? '') !== 'true' && ($p['email_verified'] ?? null) !== true) return null;
    return $p;
}

function user_progress(int $uid): array {
    $st = db()->prepare('SELECT slug, solved_at, attempts, gave_up FROM solves WHERE user_id = ?');
    $st->execute([$uid]);
    $out = [];
    foreach ($st->fetchAll() as $r) $out[$r['slug']] = $r;
    $st = db()->prepare('SELECT slug, COUNT(*) n FROM attempts WHERE user_id = ? GROUP BY slug');
    $st->execute([$uid]);
    foreach ($st->fetchAll() as $r) if (!isset($out[$r['slug']])) $out[$r['slug']] = ['open' => true, 'attempts' => (int)$r['n']];
    return $out;
}

/** Up to $n unsolved mysteries, closest to the player's current level first. */
function suggestions(?array $user, int $n = 3, string $except = ''): array {
    $prog = $user ? user_progress((int)$user['id']) : [];
    $best = 1;
    foreach (mysteries() as $m) if (isset($prog[$m['slug']]['solved_at']) && empty($prog[$m['slug']]['gave_up'])) $best = max($best, $m['level']);
    $target = min(3, $best + (count(array_filter($prog, fn($p) => isset($p['solved_at']))) >= 2 ? 1 : 0));
    $list = array_filter(mysteries(), fn($m) => $m['slug'] !== $except && !isset($prog[$m['slug']]['solved_at']));
    usort($list, fn($a, $b) => abs($a['level'] - $target) <=> abs($b['level'] - $target) ?: $a['level'] <=> $b['level']);
    return array_slice($list, 0, $n);
}

function send_login_link(string $email, string $name, bool $newsletter, string $next): bool {
    $token = bin2hex(random_bytes(24));
    db()->prepare('DELETE FROM login_tokens WHERE expires_at < ?')->execute([now()]);
    db()->prepare('INSERT INTO login_tokens (token_hash, email, name, newsletter, next_path, expires_at, created_at) VALUES (?,?,?,?,?,?,?)')
        ->execute([hash('sha256', $token), $email, $name, $newsletter ? 1 : 0, $next, gmdate('Y-m-d H:i:s', time() + 3600), now()]);
    $link = url('/auth/verify?t=' . $token);
    $site = (string)cfg('site_name');
    $from = (string)cfg('contact_email');
    $body = "Hi " . ($name ?: 'detective') . ",\r\n\r\nClick the link below to sign in to $site. It works for one hour.\r\n\r\n$link\r\n\r\nIf you didn't ask for this, just ignore this email.\r\n\r\n– $site";
    return smtp_send($email, "Your sign-in link for $site", $body, [$from, $site], ["Reply-To: $from"]);
}

function app_secret(): string {
    $s = (string)cfg('secret', '');
    if ($s !== '' && !str_starts_with($s, 'CHANGE-ME')) return $s;
    // Kept outside the web folder and outside git
    $f = dirname(__DIR__, 2) . '/data/secret.txt';
    if (!is_file($f)) { @mkdir(dirname($f), 0700, true); @file_put_contents($f, bin2hex(random_bytes(32))); }
    return trim((string)@file_get_contents($f)) ?: 'fallback';
}
function unsub_token(int $uid): string { return substr(hash_hmac('sha256', 'unsub:' . $uid, app_secret()), 0, 32); }
function unsub_url(int $uid): string { return url('/unsubscribe?u=' . $uid . '&t=' . unsub_token($uid)); }

function send_newsletter_mail(array $user, string $subject, string $body): bool {
    $site = (string)cfg('site_name');
    $from = (string)cfg('contact_email');
    $text = str_replace('{name}', $user['name'] ?: 'detective', $body);
    $unsub = unsub_url((int)$user['id']);
    $text .= "\r\n\r\n--\r\nYou get this email because you asked to hear about new mysteries on $site.\r\nUnsubscribe with one click: $unsub\r\n";
    return smtp_send($user['email'], $subject, $text, [$from, $site], ["Reply-To: $from", "List-Unsubscribe: <$unsub>", "List-Unsubscribe-Post: List-Unsubscribe=One-Click"]);
}

/** Approved reviews with first name, newest first. */
function reviews(?string $slug = null, int $limit = 6, int $minStars = 1): array {
    $sql = "SELECT r.*, u.name FROM reviews r JOIN users u ON u.id = r.user_id WHERE r.approved = 1 AND r.stars >= ? AND r.body <> ''" . ($slug ? ' AND r.slug = ?' : '') . ' ORDER BY r.created_at DESC LIMIT ' . (int)$limit;
    $st = db()->prepare($sql);
    $st->execute($slug ? [$minStars, $slug] : [$minStars]);
    return $st->fetchAll();
}
function first_name(string $n): string { $p = preg_split('/\s+/', trim($n)); return $p[0] ?? ''; }
function render_reviews(array $rs): string {
    if (!$rs) return '';
    $h = '<div class="reviews">';
    foreach ($rs as $r) {
        $m = mystery($r['slug']);
        $h .= '<figure class="review"><div class="stars" aria-label="' . (int)$r['stars'] . ' out of 5 stars">' . str_repeat('★', (int)$r['stars']) . str_repeat('☆', 5 - (int)$r['stars']) . '</div>'
            . '<blockquote>' . e($r['body']) . '</blockquote><figcaption>– ' . ($r['show_name'] ? e(first_name($r['name'])) : 'A detective')
            . ($m ? ', on <a href="/mysteries/' . e($m['slug']) . '">' . e($m['title']) . '</a>' : '') . '</figcaption></figure>';
    }
    return $h . '</div>';
}

/** Per-mystery play statistics: players, solved, solve rate (%), average guesses, average stars. */
function mystery_stats(): array {
    static $s = null;
    if ($s !== null) return $s;
    $s = [];
    try {
        $pdo = db();
        $players = $pdo->query('SELECT slug, COUNT(DISTINCT user_id) n FROM (SELECT slug, user_id FROM attempts UNION SELECT slug, user_id FROM solves) t GROUP BY slug')->fetchAll();
        foreach ($players as $r) $s[$r['slug']] = ['players' => (int)$r['n'], 'solved' => 0, 'rate' => null, 'avg_attempts' => null, 'stars' => null, 'ratings' => 0];
        foreach ($pdo->query('SELECT slug, SUM(CASE WHEN gave_up = 0 THEN 1 ELSE 0 END) solved, AVG(CASE WHEN gave_up = 0 THEN attempts END) a FROM solves GROUP BY slug')->fetchAll() as $r) {
            if (!isset($s[$r['slug']])) continue;
            $s[$r['slug']]['solved'] = (int)$r['solved'];
            $s[$r['slug']]['avg_attempts'] = $r['a'] !== null ? round((float)$r['a'], 1) : null;
        }
        foreach ($pdo->query('SELECT slug, AVG(stars) a, COUNT(*) n FROM reviews GROUP BY slug')->fetchAll() as $r) {
            if (!isset($s[$r['slug']])) continue;
            $s[$r['slug']]['stars'] = round((float)$r['a'], 1);
            $s[$r['slug']]['ratings'] = (int)$r['n'];
        }
        foreach ($s as $k => $v) $s[$k]['rate'] = $v['players'] ? (int)round($v['solved'] / $v['players'] * 100) : null;
    } catch (Throwable $e) { $s = []; }
    return $s;
}
const STATS_MIN_PLAYERS = 5;   // below this a mystery's numbers are not shown publicly


/** A suspect portrait for the posters (assets/img/m/<case>/<person>.jpg), or the grey silhouette while it is missing. */
/** Photo frames in evidence: the real photo when delivered, otherwise its label on grey. */
function photo_html(string $html): string {
    return preg_replace_callback('#\{\{PHOTO:([a-z0-9\-]+)/([a-z0-9\-]+)\|([^}]*)\}\}#', function ($mm) {
        $f = dirname(__DIR__) . '/assets/img/m/' . $mm[1] . '/photo-' . $mm[2] . '.jpg';
        if (is_file($f)) return '<img src="/assets/img/m/' . $mm[1] . '/photo-' . $mm[2] . '.jpg?v=' . filemtime($f) . '" alt="' . $mm[3] . '" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">';
        return $mm[3];
    }, $html);
}

function poster_html(string $html, string $answerUrl): string {
    $html = photo_html(str_replace('{{ANSWER_URL}}', e($answerUrl), $html));
    return preg_replace_callback('#\{\{FACE:([a-z0-9\-]+)/([a-z0-9\-]+)\}\}#', function ($mm) {
        $f = dirname(__DIR__) . '/assets/img/m/' . $mm[1] . '/' . $mm[2] . '.jpg';
        if (is_file($f)) return '<img src="/assets/img/m/' . $mm[1] . '/' . $mm[2] . '.jpg?v=' . filemtime($f) . '" alt="" style="width:100%;height:100%;object-fit:cover;object-position:50% 20%;display:block" loading="lazy">';
        return '<svg width="120" height="130" viewBox="0 0 120 130" aria-hidden="true"><circle cx="60" cy="44" r="30" fill="#B9B0A2"></circle><path d="M8 130 C8 92 30 80 60 80 C90 80 112 92 112 130 Z" fill="#B9B0A2"></path></svg>';
    }, $html);
}

/** A daily mystery's cover illustration (assets/img/m/<case>/cover.jpg), or null while it is missing. */
function mystery_cover_url(string $slug): ?string {
    $f = dirname(__DIR__) . '/assets/img/m/' . $slug . '/cover.jpg';
    return is_file($f) ? '/assets/img/m/' . $slug . '/cover.jpg?v=' . filemtime($f) : null;
}
