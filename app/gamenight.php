<?php
declare(strict_types=1);
/* Game Night: a longer print-first case for 2–6 players around one table. The website is the helper:
 * checkpoints with hints, sealed envelopes, a shared accusation scored out of 20, and the solution behind a spoiler check.
 * Sign-in is required to print and to play. The answer key is only read server-side. */

const GN_HINT_COST = 1;

function gn_slugs(): array {
    $out = [];
    foreach (glob(__DIR__ . '/gamenight/*.php') as $f) {
        if (str_ends_with($f, '.solution.php')) continue;
        $slug = basename($f, '.php');
        // New cases stay hidden from visitors until their cover image exists (admins always see them).
        if ($slug !== 'false-signal' && !is_file(dirname(__DIR__) . '/assets/img/gn/' . $slug . '/cover.jpg') && !(function_exists('is_admin') && is_admin())) continue;
        $out[] = $slug;
    }
    sort($out);
    return $out;
}
function gn_case(string $slug): ?array {
    if (!preg_match('/^[a-z0-9\-]+$/', $slug) || !in_array($slug, gn_slugs(), true)) return null;
    $c = require __DIR__ . '/gamenight/' . $slug . '.php';
    usort($c['suspects'], fn($a, $b) => strcasecmp($a['name'], $b['name']));   // alphabetical – the order never hints at the culprit
    return $c;
}
function gn_solution(string $slug): array { return require __DIR__ . '/gamenight/' . $slug . '.solution.php'; }

function gn_migrate(PDO $pdo, string $id, string $engine): void {
    $pdo->exec("CREATE TABLE IF NOT EXISTS gn_sessions (
        id $id,
        user_id INT NOT NULL,
        slug VARCHAR(100) NOT NULL,
        group_name VARCHAR(60) NOT NULL DEFAULT '',
        phase VARCHAR(10) NOT NULL DEFAULT 'A',
        hints TEXT NOT NULL,
        started_at DATETIME NOT NULL,
        finished_at DATETIME NULL,
        submission TEXT NULL,
        score INT NULL,
        breakdown TEXT NULL,
        culprit_ok TINYINT NULL,
        tries INT NOT NULL DEFAULT 0,
        revealed TINYINT NOT NULL DEFAULT 0,
        active TINYINT NOT NULL DEFAULT 1
    )$engine");
    $pdo->exec('CREATE INDEX IF NOT EXISTS gn_user ON gn_sessions (user_id, slug)');
}

function gn_session(int $uid, string $slug): ?array {
    $st = db()->prepare('SELECT * FROM gn_sessions WHERE user_id = ? AND slug = ? AND active = 1 ORDER BY id DESC LIMIT 1');
    $st->execute([$uid, $slug]);
    $s = $st->fetch();
    if (!$s) return null;
    $s['hints'] = json_decode($s['hints'], true) ?: [];
    $s['submission'] = $s['submission'] ? json_decode($s['submission'], true) : null;
    $s['breakdown'] = $s['breakdown'] ? json_decode($s['breakdown'], true) : null;
    return $s;
}
function gn_hints_used(array $s): int { return array_sum(array_map('intval', $s['hints'])); }

/** The scored questions of a case besides the culprit: [key => [label, question, points]]. */
function gn_items(array $case): array {
    return $case['accuse']['items'] ?? ['motive' => ['Motive', 'What was the motive?', 4], 'door' => ['The locked door', 'How was the door locked?', 4], 'power' => ['The power cut', 'Why did the power go out?', 3]];
}
/** Scores an accusation out of 20: culprit 6, the case's questions (4 + 4 + 3), evidence 3 – minus hints, never below 0. */
function gn_score(array $case, array $sub, int $hints): array {
    $key = gn_solution($case['slug']);
    $hit = count(array_intersect($sub['evidence'], $key['evidence']));
    $b = ['culprit' => ['Culprit', $sub['culprit'] === $key['culprit'] ? 6 : 0, 6]];
    foreach (gn_items($case) as $k => [$label, , $pts]) $b[$k] = [$label, ($sub[$k] ?? '') === $key[$k] ? $pts : 0, $pts];
    $b['evidence'] = ['Evidence (' . $hit . ' key documents)', $hit >= 4 ? 3 : ($hit === 3 ? 2 : ($hit === 2 ? 1 : 0)), 3];
    $total = array_sum(array_column($b, 1));
    if ($hints) $b['hints'] = ['Hints used (' . $hints . ')', -$hints * GN_HINT_COST, 0];
    return ['breakdown' => $b, 'score' => max(0, $total - $hints * GN_HINT_COST), 'culprit_ok' => $sub['culprit'] === $key['culprit']];
}
function gn_level_name(int $l): string { return [1 => 'Easy', 2 => 'Medium', 3 => 'Hard'][$l] ?? 'Medium'; }
function gn_doc_range(array $docs): string { return count($docs) > 1 ? $docs[0] . '–' . end($docs) : (string)$docs[0]; }

function gn_hall(string $slug, int $limit = 10): array {
    $st = db()->prepare("SELECT g.*, u.name FROM gn_sessions g JOIN users u ON u.id = g.user_id WHERE g.slug = ? AND g.score IS NOT NULL
        ORDER BY g.score DESC, (julianday(g.finished_at) - julianday(g.started_at)) ASC LIMIT " . (int)$limit);
    $st->execute([$slug]);
    return $st->fetchAll();
}
function gn_table_name(array $s): string {
    if (trim((string)$s['group_name']) !== '') return (string)$s['group_name'];
    $n = first_name((string)($s['name'] ?? ''));
    return $n !== '' ? $n . '\'s table' : 'A detective table';
}
function gn_minutes(array $s): ?int {
    if (!$s['finished_at']) return null;
    return (int)round((strtotime($s['finished_at']) - strtotime($s['started_at'])) / 60);
}

// ---------- graphics (drawn in SVG, no images needed) ----------
function gn_cover_svg(array $case): string {
    return '<svg class="gn-cover-art" viewBox="0 0 400 300" role="img" aria-label="A sealed case envelope">
      <rect x="20" y="40" width="360" height="230" rx="4" fill="' . e($case['envelope'] ?? '#C9B48A') . '" stroke="#1E1B18" stroke-width="3"/>
      <path d="M20 44 L200 175 L380 44" fill="' . e($case['flap'] ?? '#B89F70') . '" stroke="#1E1B18" stroke-width="3"/>
      <rect x="40" y="200" width="150" height="46" fill="#F3EEE4" stroke="#1E1B18" stroke-width="2"/>
      <text x="50" y="220" font-family="Special Elite, monospace" font-size="13" fill="#1E1B18">CASE FILE · No. ' . e($case['no']) . '</text>
      <text x="50" y="238" font-family="Special Elite, monospace" font-size="11" fill="#5C554D"' . (mb_strlen($case['title']) > 18 ? ' textLength="130" lengthAdjust="spacingAndGlyphs"' : '') . '>' . e(strtoupper($case['title'])) . '</text>
      <g transform="translate(200 175)"><circle r="34" fill="#A4161A"/><circle r="26" fill="none" stroke="#7A0F12" stroke-width="3"/>
      <text y="12" text-anchor="middle" font-family="Special Elite, monospace" font-size="34" fill="#F3EEE4">6</text></g>
      <g transform="translate(318 92) rotate(12)"><rect x="-58" y="-20" width="116" height="40" fill="none" stroke="#A4161A" stroke-width="3"/>
      <text text-anchor="middle" y="7" font-family="Special Elite, monospace" font-size="18" fill="#A4161A"' . (mb_strlen($case['stamp'] ?? 'REOPENED') > 9 ? ' textLength="104" lengthAdjust="spacingAndGlyphs"' : '') . '>' . e($case['stamp'] ?? 'REOPENED') . '</text></g>
    </svg>';
}
function gn_floorplan_svg(): string {
    return '<svg class="floorplan" viewBox="0 0 520 330" role="img" aria-label="Ground floor plan of Villa Nordlys">
      <g font-family="Special Elite, monospace" font-size="13" fill="#1E1B18" stroke="#1E1B18">
      <rect x="10" y="10" width="500" height="310" fill="none" stroke-width="4"/>
      <rect x="170" y="10" width="190" height="100" fill="#EDE4D3" stroke-width="3"/><text x="230" y="58" stroke="none">STUDY</text>
      <line x1="230" y1="10" x2="300" y2="10" stroke="#A4161A" stroke-width="7"/><text x="232" y="28" stroke="none" font-size="10" fill="#A4161A">window</text>
      <rect x="360" y="10" width="150" height="230" fill="none" stroke-width="3"/><text x="380" y="125" stroke="none">EAST</text><text x="380" y="141" stroke="none">CORRIDOR</text>
      <line x1="340" y1="110" x2="360" y2="110" stroke-width="3"/><text x="300" y="128" stroke="none" font-size="10">door D1</text>
      <rect x="380" y="150" width="34" height="20" fill="#A4161A" stroke="none"/><text x="384" y="164" stroke="none" fill="#fff" font-size="11">K2</text>
      <rect x="10" y="10" width="160" height="230" fill="#E4EDE2" stroke-width="3"/><text x="28" y="110" stroke="none">CONSERVATORY</text><text x="28" y="126" stroke="none" font-size="10">terrace door ↙</text>
      <rect x="130" y="150" width="34" height="20" fill="#A4161A" stroke="none"/><text x="134" y="164" stroke="none" fill="#fff" font-size="11">K5</text>
      <rect x="170" y="110" width="190" height="130" fill="none" stroke-width="2"/><text x="240" y="180" stroke="none">HALL</text>
      <rect x="10" y="240" width="250" height="80" fill="none" stroke-width="3"/><text x="70" y="285" stroke="none">DINING ROOM</text>
      <rect x="260" y="240" width="150" height="80" fill="none" stroke-width="3"/><text x="300" y="285" stroke="none">KITCHEN</text>
      <rect x="410" y="240" width="100" height="80" fill="none" stroke-width="3"/><text x="420" y="280" stroke="none" font-size="11">PLANT ROOM</text>
      <text x="470" y="34" stroke="none" font-size="16">N ↑</text>
      </g></svg>';
}
/** Illustrations. An image is ['file' => 'slug/name.jpg', 'caption' => ..., 'prompt' => AI image prompt]. If the file exists in
 * assets/img/gn/ it is shown; otherwise a tidy placeholder frame (the prompt list lives in tools/gamenight_images.md). */
function gn_img_url(string $file): ?string {
    $p = dirname(__DIR__) . '/assets/img/gn/' . $file;
    return is_file($p) ? '/assets/img/gn/' . $file . '?v=' . filemtime($p) : null;
}
function gn_photo_placeholder(string $caption): string {
    return '<figure class="photo-ph"><div class="photo-ph-img"><svg viewBox="0 0 120 80" aria-hidden="true"><g fill="none" stroke="#8A8378" stroke-width="2"><rect x="8" y="12" width="104" height="60" rx="3"/><circle cx="60" cy="42" r="16"/><rect x="44" y="4" width="22" height="10"/></g></svg>
      <span>Photo · illustration coming soon</span></div><figcaption>' . e($caption) . '</figcaption></figure>';
}
function gn_img(array $im): string {
    $u = gn_img_url($im['file']);
    if (!$u) return gn_photo_placeholder($im['caption']);
    return '<figure class="photo-ph photo-real"><img src="' . e($u) . '" alt="' . e($im['caption']) . '" loading="lazy"><figcaption>' . e($im['caption']) . '</figcaption></figure>';
}
/** Cover art for cards and heroes: the case's own illustration if it exists, else the drawn envelope. */
function gn_art(array $case): string {
    $u = isset($case['cover']) ? gn_img_url($case['cover']['file']) : null;
    return $u ? '<img class="gn-art-img" src="' . e($u) . '" alt="" loading="lazy">' : gn_cover_svg($case);
}
function gn_doc_body(array $d): string {
    $b = str_replace('{{FLOORPLAN}}', gn_floorplan_svg(), $d['body']);
    if (!empty($d['img'])) {
        $f = gn_img($d['img']);
        $b = str_contains($b, '{{IMG}}') ? str_replace('{{IMG}}', $f, $b) : $f . $b;
    }
    return $b;
}

/** Small helper for case files: a log/table block. $rows are arrays of cells (HTML allowed). */
function gn_t(array $rows, array $head = [], string $title = ''): string {
    $h = $title !== '' ? '<p class="log-head">' . $title . '</p>' : '';
    $h .= '<table class="log">';
    if ($head) $h .= '<tr>' . implode('', array_map(fn($x) => '<th>' . $x . '</th>', $head)) . '</tr>';
    foreach ($rows as $r) $h .= '<tr>' . implode('', array_map(fn($x) => '<td>' . $x . '</td>', $r)) . '</tr>';
    return $h . '</table>';
}

/** A suspect's portrait (assets/img/gn/<case>/people/<id>.jpg) or a silhouette while it is missing. */
function gn_portrait(string $slug, array $p): string {
    $u = gn_img_url($slug . '/people/' . $p['id'] . '.jpg');
    if ($u) return '<img class="gn-face" src="' . e($u) . '" alt="' . e($p['name']) . '" loading="lazy">';
    return '<svg class="gn-face" viewBox="0 0 120 120" aria-hidden="true"><rect width="120" height="120" fill="#DDD5C7"/><circle cx="60" cy="48" r="24" fill="#B9B0A2"/><path d="M14 120 C14 88 34 78 60 78 C86 78 106 88 106 120 Z" fill="#B9B0A2"/></svg>';
}
