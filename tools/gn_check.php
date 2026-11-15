<?php
// Checks every Game Night case for structural and answer-key consistency.  Usage: php tools/gn_check.php [slug ...]
declare(strict_types=1);
function e($s): string { return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8'); }
const GN_TEST = true;
require __DIR__ . '/../app/gamenight.php';
$slugs = array_slice($argv, 1) ?: gn_slugs();
$bad = 0;
foreach ($slugs as $slug) {
    $err = [];
    $c = gn_case($slug);
    if (!$c) { echo "MISSING $slug\n"; $bad++; continue; }
    $k = gn_solution($slug);
    foreach (['slug', 'no', 'title', 'tagline', 'teaser', 'genre', 'level', 'minutes', 'players', 'caseref', 'intro', 'mission', 'questions', 'suspects', 'packets', 'docs', 'checkpoints', 'accuse', 'choices', 'worksheet', 'solution_title', 'cover'] as $f)
        if (!isset($c[$f])) $err[] = "missing field $f";
    if ($err) { echo "$slug: " . implode('; ', $err) . "\n"; $bad++; continue; }
    if ($c['slug'] !== $slug) $err[] = 'slug mismatch';
    if (!in_array($c['level'], [1, 2, 3], true)) $err[] = 'bad level';
    if (strlen($c['teaser']) > 220) $err[] = 'teaser too long';
    if (array_keys($c['packets']) !== ['START', 'B', 'C']) $err[] = 'packets must be START, B, C';
    foreach (['B', 'C'] as $p) if (empty($c['packets'][$p]['when'])) $err[] = "packet $p lacks 'when'";
    $inPk = array_merge(...array_map(fn($p) => $p['docs'], array_values($c['packets'])));
    if (count($inPk) !== count(array_unique($inPk))) $err[] = 'a document is in two packets';
    $diff = array_merge(array_diff($inPk, array_keys($c['docs'])), array_diff(array_keys($c['docs']), $inPk));
    if ($diff) $err[] = 'docs and packets differ: ' . implode(',', $diff);
    foreach ($c['docs'] as $id => $d) {
        foreach (['kind', 'title', 'body'] as $f) if (empty($d[$f])) $err[] = "$id lacks $f";
        if (!empty($d['img']) && (empty($d['img']['file']) || empty($d['img']['caption']) || empty($d['img']['prompt']))) $err[] = "$id img incomplete";
        if (!empty($d['img']) && !str_starts_with($d['img']['file'], $slug . '/')) $err[] = "$id img file must start with $slug/";
        libxml_use_internal_errors(true);
        $dom = new DOMDocument(); if (!$dom->loadHTML('<div>' . $d['body'] . '</div>')) $err[] = "$id html";
    }
    if (empty($c['cover']['file']) || empty($c['cover']['prompt'])) $err[] = 'cover incomplete';
    $ids = array_column($c['suspects'], 'id');
    if (count($ids) < 5 || count($ids) > 6 || count(array_unique($ids)) !== count($ids)) $err[] = 'need 5 or 6 unique suspects';
    if (!in_array($k['culprit'], $ids, true)) $err[] = 'culprit not a suspect';
    foreach (['A', 'B', 'final'] as $cp) {
        $x = $c['checkpoints'][$cp] ?? null;
        if (!$x) { $err[] = "checkpoint $cp missing"; continue; }
        if (count($x['hints'] ?? []) < 2) $err[] = "checkpoint $cp needs 2+ hints";
        if ($cp !== 'final') {
            $g = $x['gate'] ?? null;
            if (!$g) { if (empty($x['button'])) $err[] = "checkpoint $cp needs a gate or a button"; continue; }
            if (count($g['choices']) < 3 || !isset($g['choices'][$g['answer']]) || empty($g['ok'])) $err[] = "gate $cp invalid";
        }
    }
    $items = gn_items($c);
    $pts = 6 + 3 + array_sum(array_column($items, 2));
    if ($pts !== 20) $err[] = "points add up to $pts, not 20";
    foreach ($items as $ik => $_) {
        if (count($c['choices'][$ik] ?? []) !== 4) $err[] = "item $ik needs 4 choices";
        if (!isset($c['choices'][$ik][$k[$ik] ?? ''])) $err[] = "answer for $ik not a choice";
    }
    if (count($k['evidence']) < 5) $err[] = 'answer key needs 5+ evidence documents';
    foreach ($k['evidence'] as $ev) { if (!isset($c['docs'][$ev])) $err[] = "evidence $ev unknown"; elseif (!empty($c['docs'][$ev]['aid'])) $err[] = "evidence $ev is a game aid"; }
    foreach (['summary', 'conclusions', 'timeline', 'others', 'fairness'] as $f) if (empty($k[$f])) $err[] = "solution lacks $f";
    foreach ($k['timeline'] as $t) if (count($t) !== 3) $err[] = 'timeline rows need 3 cells';
    foreach ($k['conclusions'] as $t) if (count($t) !== 2) $err[] = 'conclusion rows need 2 cells';
    // a perfect accusation scores 20, a wrong culprit cannot win
    $sub = ['culprit' => $k['culprit'], 'evidence' => array_slice($k['evidence'], 0, 4)];
    foreach ($items as $ik => $_) $sub[$ik] = $k[$ik];
    $r = gn_score($c, $sub, 0);
    if ($r['score'] !== 20 || !$r['culprit_ok']) $err[] = 'perfect accusation scores ' . $r['score'];
    $text = json_encode($c, JSON_UNESCAPED_UNICODE);
    if (preg_match('/[æøåÆØÅ]/u', str_replace(($c['allow_letters'] ?? []), '', $text))) $err[] = 'Danish letters left in the case (check names/places)';
    echo $err ? "FAIL $slug\n  - " . implode("\n  - ", $err) . "\n" : "OK   $slug (level {$c['level']}, " . count($c['docs']) . " docs)\n";
    if ($err) $bad++;
}
exit($bad ? 1 : 0);
