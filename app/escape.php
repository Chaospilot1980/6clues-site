<?php
declare(strict_types=1);
/* Escape rooms: point-and-click puzzle rooms played in the browser. Sign-in required, free.
 * The room itself (scenes, puzzles, hints) lives in assets/js/escape-<slug>.js; the server stores progress and finish times. */

const ESCAPE_ROOMS = [
    'the-clockmakers-last-hour' => [
        'title' => 'The Clockmaker’s Last Hour',
        'tagline' => 'One hour until midnight. Find the heart of the house.',
        'teaser' => 'Copenhagen, New Year’s Eve 1931. A master clockmaker has died, and his will hides his workshop behind ten riddles. You have until the great clock strikes twelve.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 3, 'puzzles' => 10, 'status' => 'Prototype',
    ],
];
const ESCAPE_LIMIT_MS = 3600000;

function escape_room(string $slug): ?array { return ESCAPE_ROOMS[$slug] ?? null; }

function escape_migrate(PDO $pdo, string $id, string $engine): void {
    $pdo->exec("CREATE TABLE IF NOT EXISTS escape_runs (
        id $id,
        user_id INT NOT NULL,
        slug VARCHAR(100) NOT NULL,
        state TEXT NOT NULL,
        started_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        finished_at DATETIME NULL,
        time_ms INT NULL,
        hints INT NULL,
        active TINYINT NOT NULL DEFAULT 1
    )$engine");
    $pdo->exec('CREATE INDEX IF NOT EXISTS escape_user ON escape_runs (user_id, slug)');
}

function escape_run(int $uid, string $slug): ?array {
    $st = db()->prepare('SELECT * FROM escape_runs WHERE user_id = ? AND slug = ? AND active = 1 ORDER BY id DESC LIMIT 1');
    $st->execute([$uid, $slug]);
    return $st->fetch() ?: null;
}

/** Fastest finished runs inside the time limit, best per player. */
function escape_board(string $slug, int $limit = 10): array {
    $st = db()->prepare('SELECT r.user_id, MIN(r.time_ms) t, u.name, l.alias FROM escape_runs r JOIN users u ON u.id = r.user_id
        LEFT JOIN leaderboard l ON l.user_id = r.user_id
        WHERE r.slug = ? AND r.time_ms IS NOT NULL AND r.time_ms <= ? GROUP BY r.user_id, u.name, l.alias ORDER BY t ASC LIMIT ' . (int)$limit);
    $st->execute([$slug, ESCAPE_LIMIT_MS]);
    return $st->fetchAll();
}
function escape_clock(int $ms): string { $s = intdiv($ms, 1000); return sprintf('%d:%02d', intdiv($s, 60), $s % 60); }
