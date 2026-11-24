<?php
/**
 * Keyword landing pages: each collects the live games that fit one search intent
 * (kids, classroom, Christmas, adults, printable…). Only live content is listed –
 * drafts and cases without art stay hidden, exactly as on the main pages.
 */

const CHRISTMAS_RE = '/christmas|santa|snow|winter|festive|frost|mince|carol|sleigh|holly|gingerbread|north pole/i';

function escape_card(string $slug, array $r): string {
    $cv = escape_cover($slug);
    return '<article class="card' . ($cv ? ' has-cover' : '') . '">'
        . ($cv ? '<a class="card-cover" href="/escape/' . e($slug) . '" tabindex="-1" aria-hidden="true"><img src="' . e($cv) . '" alt="" loading="lazy"></a>' : '')
        . '<div class="card-top"><span class="badge">Level ' . (int)($r['level'] ?? 1) . '</span><span class="badge badge-crime">Escape room</span></div>'
        . '<h3><a href="/escape/' . e($slug) . '">' . e($r['title']) . '</a></h3><p>' . e($r['teaser']) . '</p>'
        . '<p class="card-stats">' . (int)$r['minutes'] . ' min · ' . e($r['players']) . ' players · ' . (int)$r['rooms'] . ' rooms</p></article>';
}

/** slug => [title, h1, kicker, description, lead html, sections (callable returning html), faq] */
function landings(): array {
    $esc = fn(callable $f) => array_filter(escape_rooms(), fn($r, $s) => $f($r, $s), ARRAY_FILTER_USE_BOTH);
    $mys = fn(callable $f) => array_values(array_filter(mysteries(), $f));
    $escGrid = fn(array $rooms) => $rooms ? '<div class="grid">' . implode('', array_map(fn($s) => escape_card($s, $rooms[$s]), array_keys($rooms))) . '</div>' : '';
    $mysGrid = function (array $ms) { $u = current_user(); $prog = $u ? user_progress((int)$u['id']) : []; return $ms ? '<div class="grid">' . implode('', array_map(fn($m) => mystery_card($m, $prog), $ms)) . '</div>' : ''; };
    $gnGrid = function (callable $f) { $u = current_user(); $c = array_values(array_filter(array_map('gn_case', gn_slugs()), fn($c) => $c && $f($c))); return $c ? '<div class="grid">' . implode('', array_map(fn($x) => gn_card($x, $u), $c)) . '</div>' : ''; };
    $isXmas = fn(string $t) => (bool)preg_match(CHRISTMAS_RE, $t);

    return [
        'free-escape-rooms-for-kids' => [
            'title' => 'Free Online Escape Rooms for Kids – Play in Your Browser',
            'h1' => 'Free online escape rooms for kids',
            'kicker' => 'Family escape games · free',
            'description' => 'Free online escape rooms for kids and families: friendly point-and-click puzzles with pirates, dinosaurs, space stations and Santa’s workshop. Nothing to download.',
            'lead' => 'Gentle escape games for children from about 7, and for families playing together around one screen. No scary stuff – just pirates, dinosaurs, robots, reindeer and a lot of clever locks. Every room has hints, so nobody gets stuck for long.',
            'sections' => fn() => [
                ['Escape rooms for kids', 'Level 1 rooms – short, friendly and full of hints.', $escGrid($esc(fn($r) => (int)($r['level'] ?? 1) === 1))],
                ['Ready for more?', 'Older kids can try the level 1 detective cases: six clues, one culprit.', $mysGrid(array_slice($mys(fn($m) => (int)$m['level'] === 1), 0, 6))],
            ],
            'faq' => [
                ['What age are these escape rooms for?', 'The level 1 rooms work well from about age 7 with a grown-up, and from 9–10 on their own. Reading is needed, so younger children enjoy them most as a family.'],
                ['Are they really free?', 'Yes. Every escape room is free to play in the browser. A free sign-in saves progress so you can stop and come back.'],
                ['Can we play on a tablet?', 'Yes – the rooms work on tablets, phones, laptops and on a TV screen.'],
            ],
        ],
        'classroom-escape-room' => [
            'title' => 'Free Classroom Escape Rooms & Detective Games for Students',
            'h1' => 'Free classroom escape rooms and detective games',
            'kicker' => 'For teachers · free',
            'description' => 'Free digital escape rooms and printable detective mysteries for the classroom. Logic, reading and teamwork – play on the board or print the clues. No sign-up for mysteries.',
            'lead' => 'Looking for a free escape room or detective activity for your class? Put a room on the interactive whiteboard and let the class vote on every move, or print a mystery case and let teams work through the six clues. Great for the last lesson before a holiday, reading practice and logical reasoning.',
            'sections' => fn() => [
                ['Escape rooms for the whiteboard', 'Short level 1 rooms – about 30–45 minutes as a class.', $escGrid($esc(fn($r) => (int)($r['level'] ?? 1) === 1))],
                ['Printable detective cases', 'Each case is one page per clue: print a set per team. Level 1 is ideal for ages 9–12.', $mysGrid(array_slice($mys(fn($m) => (int)$m['level'] === 1), 0, 9))],
            ],
            'faq' => [
                ['How do I run an escape room with a whole class?', 'Show the room on the board. Split the class into teams that each research one part of the room, then vote on what to try. One pupil “drives” the mouse.'],
                ['Do pupils need accounts?', 'No. Printable mysteries need nothing at all. For escape rooms, the teacher can sign in once (free) on the classroom computer.'],
                ['Which subjects do they fit?', 'Reading comprehension, logic and maths reasoning, and history – several rooms are set in the past, from a medieval castle to 1920s Chicago.'],
            ],
        ],
        'christmas-murder-mystery-for-kids' => [
            'title' => 'Christmas Murder Mystery for Kids – Free Printable Detective Games',
            'h1' => 'Christmas mystery games for kids',
            'kicker' => 'Festive whodunits for kids · free',
            'description' => 'Free Christmas mystery games for kids: who sabotaged the snowman, stole the nativity star or ate the gingerbread? Printable family-friendly whodunits and Christmas escape rooms.',
            'lead' => 'A Christmas murder mystery for kids without the murder: these festive cases are about sabotaged snowmen, missing presents and stolen nativity stars. Six clues, one culprit – print the clue cards for a Christmas party, or solve them together on the sofa.',
            'sections' => fn() => [
                ['Christmas mysteries for kids', 'Level 1 festive cases – thefts and pranks, nothing scary. Great from about age 8.', $mysGrid($mys(fn($m) => (int)$m['level'] === 1 && $isXmas($m['title'] . ' ' . $m['teaser'])))],
                ['Christmas escape rooms for families', 'Short, friendly rooms with hints – play on a tablet or the TV. Older kids and adults: see all <a href="/christmas-murder-mystery">Christmas murder mysteries</a> and <a href="/christmas-escape-room">Christmas escape rooms</a>.', $escGrid($esc(fn($r, $s) => (int)($r['level'] ?? 1) === 1 && $isXmas($r['title'] . ' ' . $r['teaser'] . ' ' . $s)))],
            ],
            'faq' => [
                ['Is a Christmas murder mystery OK for kids?', 'Our kids’ cases have no murders at all – the “crimes” are things like a sabotaged snowman or a missing nativity star. They are written for ages 8 and up.'],
                ['How do we play at a Christmas party?', 'Print a case, hide the six clue cards around the room and let the children hunt for them. When all six are found, they compare the clues and name the culprit.'],
                ['Are they free?', 'Yes. Every mystery and escape room on Six Clues is free to play and print.'],
            ],
        ],
        'christmas-escape-room' => [
            'title' => 'Free Christmas Escape Rooms Online – Family Games, No Download',
            'h1' => 'Free Christmas escape rooms',
            'kicker' => 'Holiday escape games · free',
            'description' => 'Play free Christmas escape rooms online: Santa’s locked workshop, a gingerbread house, a Christmas market heist and more. For kids, families and adults – no download.',
            'lead' => 'Festive escape games for the whole family: a locked toy workshop at the North Pole, a snowy village that needs its Christmas lights, and a country house on Christmas Eve where the diamond star has been stolen from the tree.',
            'sections' => fn() => [
                ['Christmas escape rooms', 'From family-friendly to tricky.', $escGrid($esc(fn($r, $s) => $isXmas($r['title'] . ' ' . $r['teaser'] . ' ' . $s)))],
                ['Christmas murder mysteries', 'Printable festive whodunits – see all on our <a href="/christmas-murder-mystery">Christmas murder mystery</a> page.', $mysGrid(array_slice($mys(fn($m) => $isXmas($m['title'] . ' ' . $m['teaser'])), 0, 9))],
            ],
            'faq' => [
                ['Are the Christmas escape rooms free?', 'Yes, all of them. Play in the browser – no download.'],
                ['Are they suitable for kids?', 'Santa’s Locked Workshop and The Snowman’s Secret are level 1 and made for families. Christmas Eve at Holly Manor is level 2 – better for teens and adults.'],
            ],
        ],
        'murder-mystery-games-for-adults' => [
            'title' => 'Murder Mystery Games for Adults – Free, Hard Whodunits Online',
            'h1' => 'Murder mystery games for adults',
            'kicker' => 'Hard cases · free',
            'description' => 'Free murder mystery games for adults: hard level 3 whodunits with alibis, timelines and red herrings. Play online or print the case files for a dinner party or game night.',
            'lead' => 'These are the cases written to fool grown-ups: real murders, overlapping alibis, forged timelines and at least one red herring per case. Six clues, five suspects, one culprit – and no hints unless you ask. Play solo online, or print the case file for a dinner party.',
            'sections' => fn() => [
                ['Hardest murder mysteries (level 3)', 'Full murders with timelines, phone records and alibis to break. Best for experienced armchair detectives.', $mysGrid($mys(fn($m) => (int)$m['level'] === 3))],
                ['Warm-up cases (level 2)', 'Trickier than they look – a good place to start a game night before the hard ones. For printed party versions, see our <a href="/printable-murder-mystery-games">printable murder mystery games</a> and <a href="/how-to-host-a-murder-mystery-party">how to host a murder mystery party</a>.', $mysGrid($mys(fn($m) => (int)$m['level'] === 2))],
                ['Hard escape rooms', 'Point-and-click escape rooms for adults – codes, locks and a story to unravel. More in our <a href="/escape-room-at-home">escape room at home</a> collection.', $escGrid($esc(fn($r, $s) => (int)($r['level'] ?? 1) >= 3))],
            ],
            'faq' => [
                ['Are these murder mystery games really for adults?', 'Yes. Level 3 cases involve real murders, false alibis and deliberate red herrings. They contain no graphic violence, but they are written to challenge adults rather than children.'],
                ['Can we play as a group at a dinner party?', 'Yes. Print the case file, give each guest a suspect statement to read out, and let the table argue over the clues before revealing the solution.'],
                ['Are they free?', 'Yes. Every mystery and escape room on Six Clues is free to play online and to print.'],
            ],
        ],
        'murder-mystery-for-kids' => [
            'title' => 'Free Mystery Games for Kids – Printable & Online Detective Puzzles',
            'h1' => 'Printable mystery games for kids',
            'kicker' => 'Kids’ whodunits · free',
            'description' => 'Free printable mystery games for kids: family-friendly whodunits with stolen cakes, missing pets and sabotaged snowmen. Print the six clue cards or play online.',
            'lead' => 'No gore, no fear – just proper detective work. These level 1 cases are about stolen trophies, sabotaged snowmen and missing guinea pigs. Each case has six clues and one culprit: read the statements, spot the lie and name the guilty one.',
            'sections' => fn() => [
                ['Family-friendly mysteries', 'Level 1 cases – great from about age 8. In December, try our <a href="/christmas-murder-mystery-for-kids">Christmas mystery games for kids</a>.', $mysGrid($mys(fn($m) => (int)$m['level'] === 1))],
                ['Detective escape room', 'Can your young detective pass the final exam?', $escGrid($esc(fn($r, $s) => $s === 'the-detective-academy'))],
            ],
            'faq' => [
                ['What age is a kids’ murder mystery for?', 'Our level 1 cases are written for ages 8 and up – the “crimes” are thefts and pranks, never anything scary.'],
                ['Can I print them for a party?', 'Yes. Every case has a print version: hide the six clue cards around the room and let the kids hunt for them.'],
            ],
        ],
        'whodunit-puzzles-for-adults' => [
            'title' => 'Hard Whodunit Puzzles for Adults – Free Murder Mysteries',
            'h1' => 'Hard whodunit puzzles for adults',
            'kicker' => 'Mastermind cases · free',
            'description' => 'Hard, fair-play whodunit puzzles for adults: timelines, alibis and evidence that only fits one suspect. Free murder mysteries to solve online or print.',
            'lead' => 'For readers who always guess the killer by chapter three. These level 3 cases are built like proper fair-play mysteries: every alibi can be checked against a log, a receipt or a timetable – and exactly one suspect’s story falls apart.',
            'sections' => fn() => [
                ['Mastermind cases', 'Level 3 – timelines, decoys and one lie.', $mysGrid($mys(fn($m) => (int)$m['level'] === 3))],
                ['Hard escape rooms', 'Level 2 rooms with false trails.', $escGrid($esc(fn($r) => (int)($r['level'] ?? 1) >= 2))],
            ],
            'faq' => [
                ['Are the puzzles fair?', 'Yes. Every solution follows from the six clues alone – no hidden information and no trick endings.'],
                ['How long does a level 3 case take?', 'Usually 15–30 minutes. Check the timelines carefully – the lie is always in the details.'],
            ],
        ],
        'printable-murder-mystery-games' => [
            'title' => 'Free Printable Murder Mystery & Detective Games (PDF-Ready)',
            'h1' => 'Free printable murder mystery and detective games',
            'kicker' => 'Print & play · free',
            'description' => 'Free printable murder mystery and detective games: full case files with sealed envelopes for game night, plus 200 short whodunits you can print clue by clue.',
            'lead' => 'Everything on Six Clues can be printed. Game Night case files are complete printable murder mystery games for 2–8 players with sealed envelopes. The short cases print one page per clue – perfect for a party, a classroom or a rainy afternoon.',
            'sections' => fn() => [
                ['Game Night case files', 'Full printable cases with envelopes, for 2–8 players. Want a real challenge? Try our <a href="/murder-mystery-games-for-adults">murder mystery games for adults</a>.', $gnGrid(fn($c) => true)],
                ['Short printable cases', 'Six clues each – the newest ones first.', $mysGrid(array_slice(array_reverse(mysteries()), 0, 12))],
            ],
            'faq' => [
                ['How do I print a case?', 'Open any case and choose “Print”. Your browser can save it as a PDF too.'],
                ['How many players?', 'Short cases work for 1–6 players. Game Night case files are designed for 2–8.'],
            ],
        ],
        'how-to-host-a-murder-mystery-party' => [
            'title' => 'How to Host a Murder Mystery Party (Free Printable Game Inside)',
            'h1' => 'How to host a murder mystery party',
            'kicker' => 'Party guide · free printable games',
            'description' => 'How to host a murder mystery party at home in 6 easy steps: pick a case, print it, set the scene and solve it together. Includes free printable murder mystery games.',
            'lead' => 'You don’t need actors, costumes or a big budget. All you need is a printer, a table, a few friends and a good case. Here is how to host a murder mystery party in an evening – with free printable games to start from.',
            'sections' => fn() => [
                ['The 6 steps', 'From invitation to “It was the butler!”', '<ol class="howto">'
                    . '<li><b>Pick a case for your group.</b> Easy cases suit families and first-timers; hard cases suit puzzle lovers. Game Night case files work for 2–8 players.</li>'
                    . '<li><b>Print it the day before.</b> Print the case file and put each envelope’s pages in a real envelope. Write the envelope number on the front and seal it.</li>'
                    . '<li><b>Set the scene.</b> Dim the lights, put on some quiet jazz or a crackling-fire video, and lay the case file in the middle of the table. A themed drink or snack helps a lot.</li>'
                    . '<li><b>Read the briefing aloud.</b> The host reads the opening page so everyone starts with the same facts. Then hand out the documents and let people split them up.</li>'
                    . '<li><b>Open envelopes as the evidence builds up.</b> Only open the next envelope when the group has a theory. Arguing about the timeline is half the fun.</li>'
                    . '<li><b>Make the accusation.</b> Everyone writes down a name, a motive and the clue that proves it – then open the solution together.</li>'
                    . '</ol>'],
                ['Free printable murder mystery games to start with', 'Full cold case files with sealed envelopes.', $gnGrid(fn($c) => true)],
                ['Short on time?', 'These short whodunits take 15–30 minutes – a great warm-up or a party for kids.', $mysGrid(array_slice($mys(fn($m) => (int)$m['level'] <= 2), 0, 6))],
            ],
            'faq' => [
                ['How many people do I need for a murder mystery party?', 'Two is enough, but 4–6 is the sweet spot: enough people to split up the documents and argue about the suspects.'],
                ['How long does a murder mystery party take?', 'Plan 1½–2½ hours for a Game Night case file, including food and the big reveal.'],
                ['Do guests have to dress up or act?', 'No. With our case files everyone plays the detectives together – no scripts or roles to learn. Dressing up is a fun extra, not a must.'],
                ['Can I host one for kids?', 'Yes – choose an easy case, or one of the level 1 mysteries for kids: thefts and pranks, nothing scary.'],
            ],
        ],
        'black-friday-murder-mystery' => [
            'title' => 'Black Friday Murder Mystery & Escape Room – Free',
            'h1' => 'Black Friday mysteries and escape rooms',
            'kicker' => 'Black Friday · free',
            'description' => 'Free Black Friday murder mystery games and a Black Friday escape room: stolen deals, fake orders and a midnight sale that ends in murder. Play online or print.',
            'lead' => 'The best Black Friday deal is free: a stolen teddy, ten vanished half-price TVs and a murder at the midnight sale – plus an escape room where you’re locked inside the mall after closing.',
            'sections' => fn() => [
                ['Black Friday escape room', 'Locked in after closing – find a way out.', $escGrid($esc(fn($r, $s) => (bool)preg_match(seasons()['black-friday'][4], $r['title'] . ' ' . $s)))],
                ['Black Friday mysteries', 'From family-friendly to fiendish.', $mysGrid($mys(fn($m) => (bool)preg_match(seasons()['black-friday'][4], $m['title'] . ' ' . $m['teaser'])))],
            ],
            'faq' => [
                ['Is this really free on Black Friday?', 'Yes – and every other day. No sign-up needed for the mysteries.'],
                ['Is it suitable for kids?', 'The Black Friday Teddy and Locked In the Mall are level 1 and made for families. Death at the Midnight Sale is a level 3 murder for adults.'],
            ],
        ],
        'detective-games-online' => [
            'title' => 'Free Detective Games Online – Solve Mysteries in Your Browser',
            'h1' => 'Free detective games online',
            'kicker' => 'Detective games · free',
            'description' => 'Free detective games to play online: whodunit mysteries with six clues, a daily case, point-and-click escape rooms and printable cold case files. No download needed.',
            'lead' => 'Read the statements, check the evidence, catch the lie and name the culprit. Every Six Clues case is a short detective game you can play in your browser – from easy thefts for beginners to fiendish murders for seasoned sleuths. A new case comes out every day.',
            'sections' => fn() => [
                ['Start here: easy detective cases', 'Short and fair – perfect for your first case.', $mysGrid(array_slice($mys(fn($m) => (int)$m['level'] === 1), 0, 6))],
                ['For experienced detectives', 'Harder cases with tighter alibis and more red herrings.', $mysGrid(array_slice($mys(fn($m) => (int)$m['level'] === 3), 0, 6))],
                ['Point-and-click detective escape rooms', 'Search the room, find the clues, crack the locks.', $escGrid($esc(fn($r, $s) => (bool)preg_match('/detective|heist|bank|safehouse|codebreak|séance|seance|market|museum|train/i', $r['title'] . ' ' . $s)))],
                ['Detective cases to print', 'Cold case files with sealed envelopes – for a game night at home.', $gnGrid(fn($c) => true)],
            ],
            'faq' => [
                ['How does a Six Clues detective game work?', 'Each case has six clues: witness statements and evidence like receipts, logs and notes. One statement contradicts the evidence – find it, and you have your culprit.'],
                ['Are the detective games free?', 'Yes. Every case and escape room is free in the browser. A free account saves your progress and streak.'],
                ['Is there a daily detective game?', 'Yes – a new case unlocks every day, the same for everyone, so you can compare with friends.'],
                ['Can I play on my phone?', 'Yes, the games work on phones, tablets and computers.'],
            ],
        ],
        'escape-room-at-home' => [
            'title' => 'Escape Room at Home – Free Online & Printable Games',
            'h1' => 'Escape room at home – free',
            'kicker' => 'Play at home · free',
            'description' => 'Do an escape room at home for free: 35 online escape rooms to play in your browser on a TV or laptop, plus printable mystery case files for the kitchen table. Hints included.',
            'lead' => 'No booking, no travel, no cost. Put an online escape room on the TV, gather the family on the sofa and solve it together – or print a cold case file and spread the evidence across the kitchen table. Every game has built-in hints, so nobody gets stuck for long.',
            'sections' => fn() => [
                ['Escape rooms for the whole family', 'Easy rooms – great for kids and first-timers.', $escGrid($esc(fn($r, $s) => (int)$r['level'] === 1))],
                ['Harder escape rooms for teens and adults', 'More rooms, trickier locks.', $escGrid($esc(fn($r, $s) => (int)$r['level'] >= 2))],
                ['Printable mystery games for the table', 'Cold case files with sealed envelopes – print, play, solve.', $gnGrid(fn($c) => true)],
            ],
            'faq' => [
                ['How do I do an escape room at home?', 'Open one of the online rooms on a laptop or put it on the TV, and solve it together. One person clicks, everyone else shouts ideas. A room takes 20–40 minutes.'],
                ['Is it really free?', 'Yes – all escape rooms and mysteries on Six Clues are free, with no sign-up needed to play.'],
                ['How many people can play?', 'Any number – it works for one player, a couple or a whole family around the TV. For bigger groups, a printable case file lets everyone hold a piece of evidence.'],
                ['Are the escape rooms suitable for kids?', 'Level 1 rooms are made for families with children around 7 and up. Level 2 rooms suit teens and adults.'],
            ],
        ],
        'new-years-eve-murder-mystery' => [
            'title' => 'New Year’s Eve Murder Mystery & Escape Room – Free Party Games',
            'h1' => 'New Year’s Eve murder mystery games',
            'kicker' => 'New Year’s Eve · free',
            'description' => 'Free New Year’s Eve murder mystery games and escape rooms: count down to midnight with a whodunit. Play online or print the clues for your NYE party.',
            'lead' => 'Looking for something to do before the countdown? Solve a murder while the clock ticks towards midnight. These free mysteries and escape rooms fit a New Year’s Eve party perfectly – print the clues for the table, or put an escape room on the TV and race the clock together.',
            'sections' => fn() => [
                ['New Year mysteries', 'Midnight, fireworks and one guest with something to hide.', $mysGrid($mys(fn($m) => (bool)preg_match('/new year|midnight|countdown|fireworks|champagne|clock/i', $m['title'] . ' ' . $m['teaser'])))],
                ['Race-the-clock escape rooms', 'Beat the timer before midnight strikes.', $escGrid($esc(fn($r, $s) => (bool)preg_match('/clock|midnight|countdown|last hour|night/i', $r['title'] . ' ' . $r['teaser'] . ' ' . $s)))],
                ['Printable party games for the table', 'Cold case files with sealed envelopes – open one at each toast.', $gnGrid(fn($c) => true)],
            ],
            'faq' => [
                ['How do I run a murder mystery on New Year’s Eve?', 'Print a case file, put the envelopes on the table and open one every half hour. Make the accusation just before midnight and reveal the culprit with the countdown.'],
                ['Is it free?', 'Yes – all games on Six Clues are free to play online or print.'],
                ['Does it work for a big party?', 'Yes. Split guests into teams of 3–5, give each team a copy of the evidence and see who names the culprit first.'],
            ],
        ],
    ];
}

function landing_page(string $slug): void {
    $L = landings()[$slug] ?? null;
    if (!$L) { not_found(); return; }
    page_start(['title' => $L['title'], 'path' => '/' . $slug, 'description' => $L['description']]);
    echo '<section class="gn-hero"><div class="wrap"><p class="kicker">' . e($L['kicker']) . '</p><h1>' . e($L['h1']) . '</h1><p class="lead">' . e($L['lead']) . '</p></div></section>';
    foreach (($L['sections'])() as [$h, $intro, $html]) {
        if ($html === '') continue;
        echo '<section class="wrap"><h2>' . e($h) . '</h2><p>' . $intro . '</p>' . $html . '</section>';
    }
    $others = array_diff(array_keys(landings()), [$slug]);
    echo '<section class="wrap"><p>More free games: ' . implode(' · ', array_map(fn($s) => '<a href="/' . e($s) . '">' . e(landings()[$s]['h1']) . '</a>', $others)) . ' · <a href="/christmas-murder-mystery">Christmas murder mysteries</a> · <a href="/escape">all escape rooms</a> · <a href="/mysteries">all mysteries</a></p></section>';
    echo pin_box('page-' . $slug, '/' . $slug, $L['description']);
    echo faq_block($L['faq'], $L['h1'] . ' – questions');
    page_end();
}

/** Pinterest-friendly tall image + save button (only if the pin image exists). */
function pin_box(string $name, string $path, string $desc): string {
    $f = '/assets/img/pins/' . $name . '.jpg';
    if (!is_file(dirname(__DIR__) . $f)) return '';
    $href = 'https://www.pinterest.com/pin/create/button/?url=' . rawurlencode(url($path)) . '&media=' . rawurlencode(url($f)) . '&description=' . rawurlencode($desc);
    return '<section class="wrap pinbox"><a href="' . e($href) . '" target="_blank" rel="noopener"><img src="' . e($f) . '" alt="' . e($desc) . '" width="200" height="300" loading="lazy"></a><div><h2>Save it for later</h2><p>Planning a game night, a party or a rainy afternoon? Save this to Pinterest so you can find it again.</p><p><a class="btn btn-ghost" href="' . e($href) . '" target="_blank" rel="noopener">Save to Pinterest</a></p></div></section>';
}

/** Seasonal hub: every season with live content, ordered so the current/next season comes first. */
function seasons(): array {
    return [
        'black-friday' => ['Black Friday', '11-15', '11-30', '/black-friday-murder-mystery', '/black.friday|doorbuster|midnight sale|locked in the mall/i',
            'Bargain-hunting gone wrong: stolen deals, fake orders and a midnight sale that ends in murder.'],
        'christmas' => ['Christmas', '11-15', '12-26', '/christmas-murder-mystery', CHRISTMAS_RE,
            'Festive whodunits and Christmas escape rooms – from Santa’s workshop to a stolen star on Christmas Eve.'],
        'new-year' => ['New Year’s Eve', '12-20', '01-05', '/new-years-eve-murder-mystery', '/new year/i',
            'Count down to midnight with a puzzle – perfect for a New Year’s Eve party.'],
        'valentine' => ['Valentine’s Day', '01-25', '02-15', null, '/valentine|wedding|love letter/i',
            'Love letters, wedding dramas and broken hearts – mysteries for date night.'],
        'easter' => ['Easter', '03-10', '04-25', null, '/easter/i',
            'Egg hunts with a twist – Easter mysteries for the whole family.'],
        'halloween' => ['Halloween', '10-01', '11-01', null, '/halloween|haunted|ghost|pumpkin|séance|seance|witch/i',
            'Spooky (but never gory) mysteries and escape rooms for Halloween night.'],
    ];
}

function season_content(string $re): array {
    $esc = array_filter(escape_rooms(), fn($r, $s) => preg_match($re, $r['title'] . ' ' . $r['teaser'] . ' ' . $s), ARRAY_FILTER_USE_BOTH);
    $mys = array_values(array_filter(mysteries(), fn($m) => preg_match($re, $m['title'] . ' ' . $m['teaser'])));
    $gns = array_values(array_filter(array_map('gn_case', gn_slugs()), fn($c) => $c && preg_match($re, $c['title'] . ' ' . $c['teaser'])));
    return [$esc, $mys, $gns];
}

/** Days until the season starts (0 if it is on now). */
function season_distance(string $from, string $to): int {
    $md = date('m-d'); $on = $from <= $to ? ($md >= $from && $md <= $to) : ($md >= $from || $md <= $to);
    if ($on) return 0;
    $start = strtotime(date('Y') . '-' . $from); if ($start < time()) $start = strtotime((date('Y') + 1) . '-' . $from);
    return (int)ceil(($start - time()) / 86400);
}

function seasonal_page(): void {
    $u = current_user(); $prog = $u ? user_progress((int)$u['id']) : [];
    $list = [];
    foreach (seasons() as $k => $s) { [$esc, $mys, $gns] = season_content($s[4]); if ($esc || $mys || $gns) $list[$k] = [$s, $esc, $mys, $gns, season_distance($s[1], $s[2])]; }
    uasort($list, fn($a, $b) => $a[4] <=> $b[4]);
    page_start(['title' => 'Seasonal Mystery Games – Christmas, Black Friday, Halloween & More', 'path' => '/seasonal',
        'description' => 'Free seasonal murder mystery games and escape rooms: Christmas, Black Friday, New Year’s Eve, Valentine’s Day, Easter and Halloween. Play online or print.']);
    echo '<section class="gn-hero"><div class="wrap"><p class="kicker">Seasonal · free</p><h1>Seasonal mysteries & escape rooms</h1><p class="lead">A puzzle for every party of the year. Here you’ll find our holiday specials – the season that’s on right now comes first.</p>';
    echo '<p>' . implode(' · ', array_map(fn($k) => '<a href="#' . $k . '">' . e(seasons()[$k][0]) . '</a>', array_keys($list))) . '</p></div></section>';
    foreach ($list as $k => [$s, $esc, $mys, $gns, $d]) {
        $badge = $d === 0 ? '<span class="badge">On now</span> ' : ($d <= 45 ? '<span class="badge">In ' . $d . ' days</span> ' : '');
        echo '<section class="wrap" id="' . $k . '"><h2>' . $badge . e($s[0]) . '</h2><p>' . e($s[5]) . ($s[3] ? ' <a href="' . e($s[3]) . '">See all ' . e($s[0]) . ' games →</a>' : '') . '</p>';
        $cards = '';
        foreach (array_slice($esc, 0, 6, true) as $slug => $r) $cards .= escape_card($slug, $r);
        foreach ($gns as $c) $cards .= gn_card($c, $u);
        foreach (array_slice($mys, 0, max(3, 9 - count($esc))) as $m) $cards .= mystery_card($m, $prog);
        echo '<div class="grid">' . $cards . '</div></section>';
    }
    echo faq_block([
        ['Are the seasonal games free?', 'Yes – every mystery and escape room on Six Clues is free to play online or print.'],
        ['Which seasonal games work for kids?', 'Look for level 1: those are family-friendly, with thefts and pranks instead of anything scary.'],
        ['Do you add new seasonal games?', 'Yes – new holiday mysteries and escape rooms appear before each season.'],
    ], 'Seasonal games – questions');
    page_end();
}
