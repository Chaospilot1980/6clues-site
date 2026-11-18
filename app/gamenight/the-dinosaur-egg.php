<?php
// Game Night case 020: The Dinosaur Egg. Server-side only.
return [
 'slug' => 'the-dinosaur-egg',
 'no' => '020',
 'title' => 'The Dinosaur Egg',
 'tagline' => 'Forty children sleep under a T. rex. In the morning, the museum’s fossil egg is gone.',
 'teaser' => 'At a family sleepover in the town museum, the star exhibit – a real 70-million-year-old dinosaur egg – vanishes from its locked case in the night. Nobody broke the glass. Somebody had the key.',
 'genre' => 'Museum theft',
 'level' => 1,
 'minutes' => [60, 90],
 'players' => [2, 8],
 'revision' => '1.0',
 'caseref' => 'TMM-2026-0070',
 'stamp' => 'THEFT',
 'envelope' => '#D9D4B4', 'flap' => '#C2BB8F',
 'cast' => true,
 'cover' => ['file' => 'the-dinosaur-egg/cover.jpg', 'prompt' => 'Cinematic illustration of a small town natural history museum at night, a big dinosaur skeleton silhouetted against tall windows, rows of empty sleeping bags on the floor, and an empty glass display case with a spotlight on a velvet nest where an egg should be, playful mystery mood, moonlit blue and warm torchlight palette, no people, no text, 4:3'],
 'intro' => [
  'Friday night is <b>Sleepover Night</b> at the Thornbury Town Museum: forty children and their grown-ups in sleeping bags under the T. rex, with torch trails and midnight snacks.',
  'In the morning the curator unlocks the Dinosaur Hall and stops dead. The glass case is closed and locked – but the museum’s <b>fossil dinosaur egg</b> is gone. She has asked you to find it before the families go home.',
 ],
 'mission' => [
  'Work out when the egg was taken.',
  'Work out how the case was opened.',
  'Name the thief – and the reason.',
  'Back up your accusation with at least four document numbers.',
 ],
 'questions' => [
  'When was the case opened?',
  'Was the glass broken, or was a key used?',
  'Who could get the key?',
  'Who says they were asleep – and who checked?',
  'Who wanted the egg?',
  'Which spooky night-time moments were innocent?',
 ],
 'suspects' => [
  ['id' => 'pam-hill', 'name' => 'Pam Hill', 'role' => 'Volunteer guide'],
  ['id' => 'dan-frost', 'name' => 'Dan Frost', 'role' => 'Night guard'],
  ['id' => 'grace-okafor', 'name' => 'Grace Okafor', 'role' => 'Sleepover leader'],
  ['id' => 'tom-wells', 'name' => 'Tom Wells', 'role' => 'Dad on the sleepover'],
  ['id' => 'zac-ahmed', 'name' => 'Zac Ahmed', 'role' => 'Student helper'],
  ['id' => 'ivy-lane', 'name' => 'Dr Ivy Lane', 'role' => 'Curator'],
 ],
 'packets' => [
  'START' => ['label' => 'Start folder', 'docs' => ['A01', 'A02', 'A03', 'A04', 'A05', 'A06']],
  'B' => ['label' => 'Envelope B', 'when' => 'you can say when the case was opened', 'docs' => ['B01', 'B02', 'B03', 'B04', 'B05', 'B06']],
  'C' => ['label' => 'Envelope C', 'when' => 'you can say how the case was opened', 'docs' => ['C01', 'C02', 'C03', 'C04', 'C05', 'C06']],
 ],
 'docs' => [
  'A01' => ['kind' => 'report', 'title' => 'Curator’s report', 'meta' => 'Thornbury Town Museum · Saturday', 'body' => '
    <dl class="rows"><dt>22:00</dt><dd>Lights out. Egg in its case – Grace shows it to the children by torchlight.</dd><dt>06:30</dt><dd>Curator finds the case locked and empty.</dd></dl>
    <p class="note">The glass is unbroken. The case can only be opened with its key.</p>'],
  'A02' => ['kind' => 'log', 'title' => 'Display case sensor', 'meta' => 'Case 1, Dinosaur Hall', 'body' => '
    ' . gn_t([['21:58', 'Lid closed', 'Normal'], ['<b>02:14</b>', '<b>Lid opened</b>', 'Alarm switched off for sleepover'], ['02:16', 'Lid closed', 'Normal']], ['Time', 'Event', 'Note']) . '
    <p class="note">The case alarm was switched off for the night so torches would not set it off.</p>'],
  'A03' => ['kind' => 'photo', 'title' => 'The empty case', 'meta' => 'Curator’s photo, 06:35', 'img' => ['file' => 'the-dinosaur-egg/case.jpg', 'caption' => 'Case 1 in the morning', 'prompt' => 'Photo of a museum glass display case in morning light, an empty velvet nest where a fossil egg should be, a small information card beside it, a dinosaur skeleton leg in the background, documentary style, no readable text, 4:3'], 'body' => '
    <p>The velvet nest is empty. Beside the case: a few <b>crumbs of gift-shop fudge</b>.</p>
    {{IMG}}'],
  'A04' => ['kind' => 'list', 'title' => 'Sleepover plan', 'meta' => 'Who slept where', 'body' => '
    ' . gn_t([['Ocean Gallery', 'Children, parents, Grace, Pam'], ['Dinosaur Hall', 'Nobody – too cold'], ['Front desk', 'Dan (night guard)'], ['Staff room', 'Zac (helper)']], ['Room', 'Sleeping there']) . ''],
  'A05' => ['kind' => 'note', 'title' => 'About the egg', 'meta' => 'Museum label', 'body' => '
    <p>Fossil egg of a duck-billed dinosaur, 70 million years old. Found in 1961 by the late <b>Arthur Hill</b>, who sold it to the museum for £50.</p>
    <p class="note">Insured value today: £12,000.</p>'],
  'A06' => ['kind' => 'calendar', 'title' => 'Night programme', 'meta' => 'Sleepover timetable', 'body' => '
    <dl class="rows"><dt>20:00</dt><dd>Torch trail with Grace and Zac</dd><dt>21:30</dt><dd>Midnight feast (early!) – fudge from the gift shop</dd><dt>22:00</dt><dd>Lights out</dd><dt>02:00</dt><dd>Grace’s headcount</dd><dt>07:00</dt><dd>Breakfast</dd></dl>'],
  'B01' => ['kind' => 'log', 'title' => 'Key box log', 'meta' => 'Staff corridor, coded key box', 'body' => '
    ' . gn_t([['18:05', 'Code 1 (curator)', 'Case keys checked'], ['02:11', '<b>Code 4</b>', 'Key “Case 1” taken'], ['02:19', 'Code 4', 'Key “Case 1” returned']], ['Time', 'Code', 'Action']) . ''],
  'B02' => ['kind' => 'list', 'title' => 'Key box codes', 'meta' => 'Curator’s list', 'body' => '
    ' . gn_t([['Code 1', 'Dr Ivy Lane, curator'], ['Code 2', 'Night guards'], ['Code 3', 'Cleaners'], ['Code 4', 'Volunteer guides']], ['Code', 'Used by']) . '
    <p class="note">Only one volunteer guide was in the building on Friday night.</p>'],
  'B03' => ['kind' => 'log', 'title' => 'Guard’s patrol checkpoints', 'meta' => 'Dan Frost', 'body' => '
    ' . gn_t([['01:50', 'Front desk'], ['02:05', 'Roof door, top floor'], ['02:12', 'Boiler room, basement'], ['02:25', 'Front desk']], ['Time', 'Checkpoint']) . '
    <p class="note">Dan’s round goes top floor → basement → front desk, and never passes the Dinosaur Hall.</p>'],
  'B04' => ['kind' => 'report', 'title' => 'Grace’s headcount', 'meta' => 'Ocean Gallery, 02:00', 'body' => '
    <p>All children asleep. Grown-ups: Tom Wells snoring (loudly!). Pam Hill’s sleeping bag – number 12 – <b>empty</b>. “Probably gone to the loo,” I wrote, and went back to bed.</p>'],
  'B05' => ['kind' => 'interview', 'title' => 'The dad', 'meta' => 'Tom Wells', 'body' => '
    <p>“I got up once in the night – about half past two – to find my daughter’s teddy. I walked past the Dinosaur Hall with my torch. The case looked closed. Spooky place at night!”</p>'],
  'B06' => ['kind' => 'interview', 'title' => 'The student helper', 'meta' => 'Zac Ahmed', 'body' => '
    <p>“I slept in the staff room. I played a game on my phone till about half two, I admit it. I never went anywhere near the dinosaurs.”</p>
    <p class="note">Game server: Zac online, staff-room Wi-Fi, 01:40–02:35.</p>'],
  'C01' => ['kind' => 'interview', 'title' => 'The volunteer guide', 'meta' => 'Pam Hill', 'body' => '
    <p>“I slept right through, in my sleeping bag next to the children. I never woke up once. And I certainly never touched the key box.”</p>'],
  'C02' => ['kind' => 'messages', 'title' => 'Messages on Pam’s phone', 'meta' => 'Thursday', 'body' => '
    <div class="chat"><p class="msg in"><span>Thu 19:02 · Collector</span>Mrs Hill, my offer for your father’s egg stands: £8,000, cash, no questions.</p><p class="msg out"><span>Thu 19:10 · Pam</span>Dad was cheated – £50! It should be ours. Leave it with me. Saturday.</p></div>'],
  'C03' => ['kind' => 'report', 'title' => 'Search of the bags', 'meta' => 'Police, Saturday 08:00', 'body' => '
    <p>In Pam Hill’s overnight bag, wrapped in a museum gift-shop T-shirt: a round <b>fossil egg</b>. A half-eaten bag of gift-shop fudge in the side pocket.</p>'],
  'C04' => ['kind' => 'interview', 'title' => 'The sleepover leader', 'meta' => 'Grace Okafor', 'body' => '
    <p>“Everyone had fudge – it was the midnight feast. I did the headcount at two and went straight back to sleep; I was shattered. I don’t even know the key box code.”</p>'],
  'C05' => ['kind' => 'interview', 'title' => 'The curator', 'meta' => 'Dr Ivy Lane', 'body' => '
    <p>“I went home at half six on Friday evening and came back at half six in the morning. Pam has asked me twice this year to ‘give Dad’s egg back’. I had to say no – it belongs to the town.”</p>
    <p class="note">Alarm company: museum front door not opened between 18:30 and 06:30 except by the guard from inside.</p>'],
  'C06' => ['kind' => 'interview', 'title' => 'The night guard', 'meta' => 'Dan Frost', 'body' => '
    <p>“My code is 2, not 4. I was down in the boiler room at ten past two – that’s on the checkpoint log. The only thing I took from the gift shop was a cup of tea.”</p>'],
 ],
 'checkpoints' => [
  'A' => ['title' => 'The moment', 'prompt' => 'When was the egg taken?',
          'gate' => ['q' => 'When was the case opened?', 'choices' => ['Before lights out', 'At 02:14', 'At 06:30'], 'answer' => 1,
                     'ok' => 'The lid sensor shows the case open from 02:14 to 02:16. Open envelope B.'],
          'hints' => ['The glass is not broken – look at the case sensor.', 'A02 shows exactly one opening in the night.']],
  'B' => ['title' => 'The key', 'prompt' => 'How was the case opened – and whose code was used?',
          'gate' => ['q' => 'How was the case opened?', 'choices' => ['With the guard’s code', 'With the volunteer guides’ code 4', 'With the curator’s code'], 'answer' => 1,
                     'ok' => 'Code 4 took the case key at 02:11 and returned it at 02:19 – and only one volunteer guide was there that night. Open envelope C.'],
          'hints' => ['Someone used the key box just before the case opened.', 'B01 shows the code; B02 shows whose it is.']],
  'final' => ['title' => 'The accusation', 'prompt' => 'Who took the dinosaur egg, and why?',
          'hints' => ['Does the guide’s story match the headcount?', 'C01 against B04; C02 and C03 give the reason and the proof.']],
 ],
 'accuse' => [
  'culprit_q' => 'Who stole the dinosaur egg?',
  'wrong' => 'That’s not the person who opened the case.',
  'items' => ['when' => ['The moment', 'When was it taken?', 4], 'how' => ['The method', 'How was it done?', 4], 'motive' => ['The motive', 'Why was it done?', 3]],
 ],
 'choices' => [
  'when' => [
   'a' => 'Before lights out.',
   'b' => 'At 02:14, in the middle of the night.',
   'c' => 'During the torch trail.',
   'd' => 'At breakfast.',
  ],
  'how' => [
   'a' => 'The glass was broken and replaced.',
   'b' => 'Using the volunteer guides’ code 4 to take the case key from the key box.',
   'c' => 'With the guard’s master key.',
   'd' => 'The curator never locked it.',
  ],
  'motive' => [
   'a' => 'To win a bet with the children.',
   'b' => 'She felt her father had been cheated – and a collector offered her £8,000.',
   'c' => 'To claim the insurance.',
   'd' => 'To hide it as a prank.',
  ],
 ],
 'worksheet' => ['Who did it?', 'When was the egg taken?', 'How was the case opened?', 'Why?', 'Which details were red herrings?'],
 'solution_title' => 'What really happened at Sleepover Night',
];
