<?php
declare(strict_types=1);
/* Escape rooms: point-and-click puzzle rooms played in the browser. Sign-in required, free.
 * The room itself (scenes, puzzles, hints) lives in assets/js/escape-<slug>.js; the server stores progress and finish times. */

const ESCAPE_ROOMS = [
    'the-clockmakers-last-hour' => [
        'title' => 'The Clockmaker’s Last Hour',
        'tagline' => 'One hour until midnight. Find the heart of the house.',
        'teaser' => 'Copenhagen, New Year’s Eve 1931. A master clockmaker has died, and his will hides his workshop behind ten riddles. You have until the great clock strikes twelve.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 3, 'puzzles' => 10, 'status' => 'New', 'level' => 1,
    ],
    'the-last-night-train' => [
        'title' => 'The Last Night Train',
        'tagline' => 'A courier vanishes on the Orient Express. One hour to the frontier.',
        'teaser' => 'Simplon-Orient-Express, 1934. The courier you were sent to meet has vanished from compartment 7, leaving a briefcase with three dials. At 06:00 the customs men board. Harder: three trails at once, and decoys along the way.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 13, 'status' => 'New', 'level' => 2,
    ],
    'the-lighthouse-at-gull-rock' => [
        'title' => 'The Lighthouse at Gull Rock',
        'tagline' => 'A storm, a dark tower, a ship due at the reef at two.',
        'teaser' => 'Cornwall, 15 November 1912. The keeper has vanished, the light is out and the steamer Marigold passes the reef at 02:00. Not everything written in this cottage is true.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 13, 'status' => 'New', 'level' => 2,
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
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 12, 'status' => 'New', 'level' => 2, 'engine' => true,
    ],
    'the-codebreakers-hut' => [
        'title' => 'The Codebreakers’ Hut',
        'tagline' => 'A convoy at sea, a mole in the hut and one hour until six.',
        'teaser' => 'Buckinghamshire, May 1943. The Commander ran out into the night with an intercept and never came back. Somebody has sabotaged the machines – and a convoy is sailing into a trap.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 12, 'status' => 'New', 'level' => 2, 'engine' => true,
    ],
    'the-seance' => [
        'title' => 'The Séance',
        'tagline' => 'At midnight the spirits will ask for a fortune. You know it’s a trick.',
        'teaser' => 'Belgravia, Halloween 1888. A famous medium will make Lady Ashworth’s dead husband speak – and at midnight she signs away everything. You have been locked in the parlour for asking questions.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 3, 'puzzles' => 12, 'status' => 'New', 'level' => 2, 'engine' => true,
    ],
    'santas-locked-workshop' => [
        'title' => 'Santa’s Locked Workshop',
        'tagline' => 'The sleigh leaves at seven. You are locked in.',
        'teaser' => 'The North Pole, Christmas Eve. Santa has a cold, the elves are at the party, and the newest elf is locked in the workshop. Find the key, the map and the bells before the sleigh is late. A family room for first-timers.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 3, 'puzzles' => 9, 'status' => 'New', 'level' => 1, 'engine' => true,
    ],
    'the-pirates-cove' => [
        'title' => 'The Pirate’s Cove',
        'tagline' => 'The tide is coming in. The treasure is somewhere in the dark.',
        'teaser' => 'Cornwall, 1721. You followed an old map into a smugglers’ cave and the tide has cut you off. Find Captain Blackwater’s treasure and his rowing boat before the cave floods. A family room for first-timers.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 3, 'puzzles' => 10, 'status' => 'New', 'level' => 1, 'engine' => true,
    ],
    'countdown-on-the-space-station' => [
        'title' => 'Countdown on the Space Station',
        'tagline' => 'The last capsule leaves in one hour. The power is out.',
        'teaser' => 'Star Station Lyra, 2049. A meteor storm has cut the power and the crew have gone home without you. Get the lights back, find the navigation chip and fly the last capsule home. A family room for first-timers.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 3, 'puzzles' => 9, 'status' => 'New', 'level' => 1, 'engine' => true,
    ],
    'the-enchanted-library' => [
        'title' => 'The Enchanted Library',
        'tagline' => 'When the last candle goes out, you stay for a hundred years.',
        'teaser' => 'A rainy afternoon in the old town library – and the door has vanished behind you. Talking owls, back-to-front writing and a magic circle: find the spell that takes you home. A family room for first-timers.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 3, 'puzzles' => 8, 'status' => 'New', 'level' => 1, 'engine' => true,
    ],
    'the-dinosaur-dig' => [
        'title' => 'The Dinosaur Dig',
        'tagline' => 'A sandstorm is coming. The jeep key is locked away.',
        'teaser' => 'The badlands, high summer. The professor has gone to town and a sandstorm is rolling in. Dig up the fossils, get the radio working and find the jeep key before the storm hits. A family room for first-timers.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 3, 'puzzles' => 7, 'status' => 'New', 'level' => 1, 'engine' => true,
    ],
    'the-speakeasy-raid' => [
        'title' => 'The Speakeasy Raid',
        'tagline' => 'The Feds raid at one. The real ledger is still hidden.',
        'teaser' => 'Chicago, February 1927. You are an undercover reporter at the Blue Parrot, the speakeasy where the mayor’s men drink for free. Find the boss’s real ledger and get out through the tunnel before the police storm in. Harder: decoy menus and a fake account book.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 10, 'status' => 'New', 'level' => 2, 'engine' => true,
    ],
    'the-last-dive' => [
        'title' => 'The Last Dive',
        'tagline' => 'A hundred metres down. One hour of air.',
        'teaser' => 'North Atlantic, October 1962. A gas leak has knocked out the crew of HMS Narwhal and the submarine lies on the seabed, slowly flooding. Seal the leak, restore the power and blow the right ballast tanks. Harder: old orders and crossed-out diagrams.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 9, 'status' => 'New', 'level' => 2, 'engine' => true,
    ],
    'the-inventors-laboratory' => [
        'title' => 'The Inventor’s Laboratory',
        'tagline' => 'At midnight the thieves come. The door needs lightning.',
        'teaser' => 'London, New Year’s Eve 1895. Professor Thornbury’s rival is coming for her great invention at midnight – and the door only opens when lightning drives the gears. Rebuild her machine in time. Harder: wrong cards, wrong lights, wrong order.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 8, 'status' => 'New', 'level' => 2, 'engine' => true,
    ],
    'the-sheriffs-jail' => [
        'title' => 'The Sheriff’s Jail',
        'tagline' => 'Framed for a bank robbery. The judge arrives at noon.',
        'teaser' => 'Copper Creek, Arizona, 1881. You woke up in jail for a robbery you didn’t commit, and the hanging judge rides in at noon. Escape the cell, find the real robber and the stolen gold, and ride for the marshal. Harder: three wanted posters, one robber.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 7, 'status' => 'New', 'level' => 2, 'engine' => true, 'draft' => true,
    ],
    'christmas-eve-at-holly-manor' => [
        'title' => 'Christmas Eve at Holly Manor',
        'tagline' => 'The diamond star is gone. The thief leaves at midnight.',
        'teaser' => 'Yorkshire, Christmas Eve 1923. The lights went out at nine, and the family’s diamond brooch vanished from the top of the tree. Find the star, unmask the lying guest and open the locked front door before the midnight sleigh. Harder: one guest’s story doesn’t add up.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 7, 'status' => 'New', 'level' => 2, 'engine' => true, 'draft' => true,
    ],
    'the-candy-factory' => [
        'title' => 'The Candy Factory',
        'tagline' => 'The gates open in an hour. The recipe is locked away.',
        'teaser' => 'Fizzwhistle’s Sweet Factory, opening day. The owner has vanished and the secret Rainbow Chew recipe is locked in his office. Dig through a sugar mountain, mix the syrups and crack the gumball safe. A family room for first-timers.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 3, 'puzzles' => 6, 'status' => 'New', 'level' => 1, 'engine' => true, 'draft' => true,
    ],
    'the-zoo-after-dark' => [
        'title' => 'The Zoo After Dark',
        'tagline' => 'Locked in the zoo at night. The alarm goes on in an hour.',
        'teaser' => 'You stayed too long at the penguin pool and the City Zoo has closed behind you. Feed the penguins, brave the dark reptile house and find the keeper’s keycard before the night alarm comes on. A family room for first-timers.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 3, 'puzzles' => 6, 'status' => 'New', 'level' => 1, 'engine' => true, 'draft' => true,
    ],
    'the-snowmans-secret' => [
        'title' => 'The Snowman’s Secret',
        'tagline' => 'The village lights go on at six. The golden key is missing.',
        'teaser' => 'Little Frostwick, Christmas Eve. The golden key for the village Christmas lights has gone missing, and the whole village gathers at six. Give the snowman his nose back and follow the clues. A short, gentle room for families.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 3, 'puzzles' => 5, 'status' => 'New', 'level' => 1, 'engine' => true, 'draft' => true,
    ],
    'the-detective-academy' => [
        'title' => 'The Detective Academy',
        'tagline' => 'Final exam: find out who stole the Golden Badge.',
        'teaser' => 'Exam day at the Detective Academy, and the Golden Badge has been stolen from its case. Use your magnifying glass, read the evidence and name the thief to pass. A family room for first-timers and young detectives.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 3, 'puzzles' => 6, 'status' => 'New', 'level' => 1, 'engine' => true, 'draft' => true,
    ],
    'the-castaway-island' => [
        'title' => 'The Castaway Island',
        'tagline' => 'A ship passes once a day. Light the signal fire.',
        'teaser' => 'Shipwrecked on a tiny tropical island, you have one hour before the daily ship sails past. Trade with a cheeky monkey, open the parrot door and build a signal fire that shines for miles. A family room for first-timers.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 3, 'puzzles' => 6, 'status' => 'New', 'level' => 1, 'engine' => true, 'draft' => true,
    ],
    'the-venetian-masquerade' => [
        'title' => 'The Venetian Masquerade',
        'tagline' => 'At midnight the masks come off – and the guards come for you.',
        'teaser' => 'Venice, Carnival 1756. A masked guest snatched the Doge’s sealed letter from your hands, and now you are the suspect. Unmask the spy, crack the cipher and escape by gondola before midnight. Harder: crossed-out music and a ballroom full of masks.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 7, 'status' => 'New', 'level' => 2, 'engine' => true, 'draft' => true,
    ],
    'the-berlin-safehouse' => [
        'title' => 'The Berlin Safehouse',
        'tagline' => 'A wall is going up tonight. At dawn the last way out closes.',
        'teaser' => 'East Berlin, 13 August 1961. Soldiers are building a wall through the city and your contact never came. Find the microfilm, develop it, forge your papers and reach the tunnel before dawn. Harder: test broadcasts and the wrong records.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 6, 'status' => 'New', 'level' => 2, 'engine' => true, 'draft' => true,
    ],
    'the-jaguar-temple' => [
        'title' => 'The Jaguar Temple',
        'tagline' => 'The door shut behind you. The river floods at sunset.',
        'teaser' => 'Yucatán, 1925. Your mentor vanished searching for the lost Jaguar Temple – and its stone door has just sealed behind you. Read Maya numbers, turn the great calendar and wake the jaguar before the river floods. Harder: looters left false signs.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 6, 'status' => 'New', 'level' => 2, 'engine' => true, 'draft' => true,
    ],
    'the-castle-under-siege' => [
        'title' => 'The Castle Under Siege',
        'tagline' => 'A traitor opens the gate at midnight. Light the beacon first.',
        'teaser' => 'Castle Ravenmoor, 1450. An army camps below the walls and one of the four knights plans to open the gate at midnight. Read the heraldry, open the first lord’s tomb, light the beacon and name the traitor. Harder: four knights, one boar.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 6, 'status' => 'New', 'level' => 2, 'engine' => true, 'draft' => true,
    ],
    'the-midnight-bank-job' => [
        'title' => 'The Midnight Bank Job',
        'tagline' => 'A gang is tunnelling into the vault. The alarm is dead.',
        'teaser' => 'New York, 1935. You are the night watchman, the phone is cut, the alarm fuse is gone – and someone is digging into the vault. Lock the time lock, fix the alarm and call the police before the gang breaks through. Harder: there is an inside man.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 7, 'status' => 'New', 'level' => 2, 'engine' => true, 'draft' => true,
    ],
    'the-north-pole-post-office' => [
        'title' => 'The North Pole Post Office',
        'tagline' => 'A lost letter, a golden stamp and a sleigh that leaves at midnight.',
        'teaser' => 'Find a lost letter to Santa, get it stamped and onto the sleigh before midnight – a free Christmas escape room for families.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 3, 'puzzles' => 6, 'status' => 'New', 'level' => 1, 'engine' => true, 'draft' => true,
    ],
    'the-gingerbread-house' => [
        'title' => 'The Gingerbread House',
        'tagline' => 'Locked inside a life-size gingerbread house – and the judges come at noon.',
        'teaser' => 'Trapped inside Grandma Ginny’s giant gingerbread house: mend the stairs, crack the cookie code and find the sugar key. Free family escape room.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 3, 'puzzles' => 7, 'status' => 'New', 'level' => 1, 'engine' => true, 'draft' => true,
    ],
    'the-christmas-market-heist' => [
        'title' => 'The Christmas Market Heist',
        'tagline' => 'Someone stole the golden star off the market tree. One stallholder is lying.',
        'teaser' => 'The golden star is gone from the Christmas market tree. Check the alibis, crack the carousel and find the thief before the lights go on.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 4, 'puzzles' => 5, 'status' => 'New', 'level' => 2, 'engine' => true, 'draft' => true,
    ],
    'the-misers-christmas-eve' => [
        'title' => 'The Miser’s Christmas Eve',
        'tagline' => 'London, 1843. The clerks’ Christmas wages are locked in a miser’s safe.',
        'teaser' => 'Victorian London, Christmas Eve: open old Mr Grimble’s safe and get the clerks’ wages home before midnight. A free online escape room.',
        'minutes' => 60, 'players' => '1–4', 'rooms' => 3, 'puzzles' => 7, 'status' => 'New', 'level' => 2, 'engine' => true, 'draft' => true,
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

/** Cover picture for an escape room: its most striking scene (falls back to the first scene file). */
function escape_cover(string $slug): ?string {
    $pick = ['the-clockmakers-last-hour' => 'tower', 'the-last-night-train' => 'compartment', 'the-lighthouse-at-gull-rock' => 'lamp',
             'after-hours-at-the-museum' => 'hall', 'the-alchemists-attic' => 'attic', 'the-sealed-tomb' => 'burial', 'the-polar-night' => 'hut',
             'the-last-airship' => 'lounge', 'the-codebreakers-hut' => 'hut', 'the-seance' => 'parlour', 'santas-locked-workshop' => 'workshop', 'the-pirates-cove' => 'grotto', 'countdown-on-the-space-station' => 'cockpit', 'the-enchanted-library' => 'tower', 'the-dinosaur-dig' => 'pit', 'the-speakeasy-raid' => 'bar', 'the-last-dive' => 'control', 'the-inventors-laboratory' => 'workshop', 'the-sheriffs-jail' => 'office', 'christmas-eve-at-holly-manor' => 'drawing', 'the-candy-factory' => 'floor', 'the-zoo-after-dark' => 'pool', 'the-snowmans-secret' => 'square', 'the-detective-academy' => 'evidence', 'the-castaway-island' => 'beach', 'the-venetian-masquerade' => 'ballroom', 'the-berlin-safehouse' => 'flat', 'the-jaguar-temple' => 'throne', 'the-castle-under-siege' => 'tower', 'the-midnight-bank-job' => 'vault', 'the-north-pole-post-office' => 'sorting', 'the-gingerbread-house' => 'kitchen', 'the-christmas-market-heist' => 'square', 'the-misers-christmas-eve' => 'office'];
    $dir = dirname(__DIR__) . '/assets/img/escape/' . $slug . '/';
    $f = isset($pick[$slug]) && is_file($dir . $pick[$slug] . '.jpg') ? $pick[$slug] . '.jpg' : (basename((string)(glob($dir . '*.jpg')[0] ?? '')) ?: null);
    return $f ? '/assets/img/escape/' . $slug . '/' . $f : null;
}
