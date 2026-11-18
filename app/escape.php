<?php
declare(strict_types=1);
/* Escape rooms: point-and-click puzzle rooms played in the browser. Sign-in required, free.
 * The room itself (scenes, puzzles, hints) lives in assets/js/escape-<slug>.js; the server stores progress and finish times. */

const ESCAPE_ROOMS = [
    'the-clockmakers-last-hour' => [
        'title' => 'The Clockmaker’s Last Hour',
        'tagline' => 'One hour until midnight. Find the heart of the house.',
        'teaser' => 'Copenhagen, New Year’s Eve 1931. A master clockmaker has died, and his will hides his workshop behind ten riddles. You have until the great clock strikes twelve.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 3, 'puzzles' => 10, 'status' => 'Prototype', 'level' => 1,
    ],
    'the-last-night-train' => [
        'title' => 'The Last Night Train',
        'tagline' => 'A courier vanishes on the Orient Express. One hour to the frontier.',
        'teaser' => 'Simplon-Orient-Express, 1934. The courier you were sent to meet has vanished from compartment 7, leaving a briefcase with three dials. At 06:00 the customs men board. Harder: three trails at once, and decoys along the way.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 13, 'status' => 'Prototype', 'level' => 2,
    ],
    'the-lighthouse-at-gull-rock' => [
        'title' => 'The Lighthouse at Gull Rock',
        'tagline' => 'A storm, a dark tower, a ship due at the reef at two.',
        'teaser' => 'Cornwall, 15 November 1912. The keeper has vanished, the light is out and the steamer Marigold passes the reef at 02:00. Not everything written in this cottage is true.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 13, 'status' => 'Prototype', 'level' => 2,
    ],
    'after-hours-at-the-museum' => [
        'title' => 'After Hours at the Museum',
        'tagline' => 'Locked in with the dinosaurs. The meteorite is a fake.',
        'teaser' => 'London, November 1958. You hid in the museum at closing time to prove the famous Kensington meteorite has been swapped for a fake. At 23:00 the thief comes back for the real one.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 13, 'status' => 'New', 'level' => 2, 'engine' => true,
    ],
    'the-alchemists-attic' => [
        'title' => 'The Alchemist’s Attic',
        'tagline' => 'The emperor was poisoned. Your master is in chains. Dawn is coming.',
        'teaser' => 'Prague Castle, 1610. A poison recipe in your master’s name, a chest only the four elements can open – and one hour before the guards come for the apprentice.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 13, 'status' => 'New', 'level' => 2, 'engine' => true,
    ],
    'the-sealed-tomb' => [
        'title' => 'The Sealed Tomb',
        'tagline' => 'Someone rolled the stone back. Your lamp has an hour of oil.',
        'teaser' => 'Valley of the Kings, November 1922. A rival expedition has sealed you inside a newly opened tomb. Somewhere, the workmen of three thousand years ago left another way out.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 13, 'status' => 'New', 'level' => 2, 'engine' => true,
    ],
    'the-polar-night' => [
        'title' => 'The Polar Night',
        'tagline' => 'No sun for weeks. No power. One plane, at one o’clock.',
        'teaser' => 'Svalbard, January 1958. The station chief went out to check the aerial and never came back – then the lights died. The last plane of the winter flies over at 01:00.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 13, 'status' => 'New', 'level' => 2, 'engine' => true,
    ],
    'the-last-airship' => [
        'title' => 'The Last Airship',
        'tagline' => 'The navigator is gone, the crew is locked in, and the ship is turning in the dark.',
        'teaser' => 'Over the North Atlantic, May 1936. The giant airship Valkyrie is drifting off course with her ballast draining away. One passenger aboard is not who he says.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 12, 'status' => 'New', 'level' => 2, 'engine' => true, 'draft' => true,
    ],
];
const ESCAPE_LIMIT_MS = 3600000;

/* Draft rooms (no artwork yet) are only visible to admins. */
function escape_rooms(): array { return array_filter(ESCAPE_ROOMS, fn($r) => empty($r['draft']) || is_admin()); }
function escape_room(string $slug): ?array { return escape_rooms()[$slug] ?? null; }

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
