<?php
// Game Night case 019: The Christmas Market Cash Box. Server-side only.
return [
 'slug' => 'the-christmas-market-cash-box',
 'no' => '019',
 'title' => 'The Christmas Market Cash Box',
 'tagline' => 'The charity takings vanish while the whole town sings round the tree.',
 'teaser' => 'On the busiest night of the Christmas market, the charity cash box – £8,200 for the children’s hospice – disappears from the organiser’s cabin. Everyone was singing carols. Almost everyone.',
 'genre' => 'Theft',
 'level' => 2,
 'minutes' => [75, 105],
 'players' => [2, 8],
 'revision' => '1.0',
 'caseref' => 'XMK-2026-1206',
 'stamp' => 'THEFT',
 'envelope' => '#E7C9C1', 'flap' => '#D4A79B',
 'cast' => true,
 'cover' => ['file' => 'the-christmas-market-cash-box/cover.jpg', 'prompt' => 'Cinematic illustration of a snowy town Christmas market at night, wooden stalls with fairy lights, a big decorated tree in the square, and in the foreground a small wooden office cabin with its door ajar and an empty open cash box on the counter inside, cosy yet suspicious mood, warm gold and deep green palette, no people, no text, 4:3'],
 'intro' => [
  'Saturday night at the <b>Ashby Christmas Market</b>. Forty stalls, mulled wine, a Santa’s grotto and, at seven o’clock, the big lights switch-on. All evening the stalls drop their charity takings into a cash box in the organiser’s cabin.',
  'At 19:15 the organiser goes to bank the money. The cabin is shut, the keypad untouched – and the cash box, with <b>£8,200</b> for the children’s hospice, has gone. The market committee has asked you to find it before Monday’s newspaper does.',
 ],
 'mission' => [
  'Work out when the cash box was taken.',
  'Work out who could get into the cabin.',
  'Name the thief – and the reason.',
  'Back up your accusation with at least four document numbers.',
 ],
 'questions' => [
  'When was the cash box last seen – and when did the cabin door open?',
  'Who knew the keypad code?',
  'Where was each of them at that moment?',
  'Whose alibi has a gap in it?',
  'Who needed money badly?',
  'Which suspicious things were innocent?',
 ],
 'suspects' => [
  ['id' => 'harry-knight', 'name' => 'Harry Knight', 'role' => 'Santa'],
  ['id' => 'maggie-flynn', 'name' => 'Maggie Flynn', 'role' => 'Market organiser'],
  ['id' => 'noah-price', 'name' => 'Noah Price', 'role' => 'Organiser’s assistant'],
  ['id' => 'raj-patel', 'name' => 'Raj Patel', 'role' => 'Security guard'],
  ['id' => 'elsa-berg', 'name' => 'Elsa Berg', 'role' => 'Mulled wine stall'],
  ['id' => 'lucy-green', 'name' => 'Lucy Green', 'role' => 'Choir leader'],
 ],
 'packets' => [
  'START' => ['label' => 'Start folder', 'docs' => ['A01', 'A02', 'A03', 'A04', 'A05', 'A06']],
  'B' => ['label' => 'Envelope B', 'when' => 'you can say when the cash box was taken', 'docs' => ['B01', 'B02', 'B03', 'B04', 'B05', 'B06']],
  'C' => ['label' => 'Envelope C', 'when' => 'you can say who could have taken it', 'docs' => ['C01', 'C02', 'C03', 'C04', 'C05', 'C06']],
 ],
 'docs' => [
  'A01' => ['kind' => 'report', 'title' => 'Theft report', 'meta' => 'Ashby Christmas Market · Saturday', 'body' => '
    <dl class="rows"><dt>18:30</dt><dd>Maggie counts the box: £8,200. Locks the cabin.</dd><dt>19:15</dt><dd>Maggie returns to bank the money – box gone</dd></dl>
    <p class="note">No damage to the door, the keypad or the window.</p>'],
  'A02' => ['kind' => 'log', 'title' => 'Cabin keypad log', 'meta' => 'Organiser’s cabin', 'body' => '
    ' . gn_t([['18:30', 'Locked', 'Code entered'], ['18:42', '<b>Opened</b>', 'Code entered'], ['18:45', 'Locked', 'Code entered'], ['19:15', 'Opened', 'Code entered']], ['Time', 'Door', 'Method']) . '
    <p class="note">The keypad does not record whose code was used – there is only one code.</p>'],
  'A03' => ['kind' => 'photo', 'title' => 'The cabin', 'meta' => 'Police photo, Saturday 19:40', 'img' => ['file' => 'the-christmas-market-cash-box/cabin.jpg', 'caption' => 'Inside the organiser’s cabin', 'prompt' => 'Inside a small wooden Christmas market office cabin at night, a desk with an empty space where a box stood, a red Santa sack hanging on a hook in the corner, a string of fairy lights, a window onto the snowy market, documentary photo style, no readable text, 4:3'], 'body' => '
    <p>The desk where the cash box stood. On a hook in the corner: <b>Santa’s spare sack</b> and a box of sweets for the grotto.</p>
    {{IMG}}'],
  'A04' => ['kind' => 'calendar', 'title' => 'Evening programme', 'meta' => 'Market poster', 'body' => '
    <dl class="rows"><dt>16:00–20:00</dt><dd>Santa’s grotto (bookings via the photographer)</dd><dt>18:30–19:00</dt><dd>Carols round the tree – Ashby Community Choir</dd><dt>19:00</dt><dd>Lights switch-on by the organiser</dd></dl>'],
  'A05' => ['kind' => 'interview', 'title' => 'The organiser', 'meta' => 'Maggie Flynn', 'body' => '
    <p>“The code is 2512 – Christmas Day, I know, I know. Only the people who need the cabin have it: me, Noah, Raj for his rounds, and Harry, because Santa keeps his spare sack and the sweets in there.”</p>'],
  'A06' => ['kind' => 'list', 'title' => 'Market map notes', 'meta' => 'Committee', 'body' => '
    ' . gn_t([['Organiser’s cabin', 'Behind the grotto, 20 m'], ['Santa’s grotto', 'Corner of the square'], ['Christmas tree & stage', 'Centre of the square'], ['Entrance gate', 'North side'], ['Car park', '400 m south']], ['Place', 'Where']) . ''],
  'B01' => ['kind' => 'report', 'title' => 'Stage video', 'meta' => 'Live stream, town Facebook page', 'body' => '
    <p>18:30–19:05: Lucy Green conducting the choir at the tree. <b>Maggie Flynn</b> beside the stage with the microphone, introducing each carol, the whole time.</p>'],
  'B02' => ['kind' => 'receipt', 'title' => 'Entrance gate till', 'meta' => 'Tickets', 'body' => '
    ' . gn_t([['18:35', 'Family ticket', 'N. Price'], ['18:41', '2 adults', 'N. Price'], ['18:44', '1 adult', 'N. Price'], ['18:50', 'Family ticket', 'N. Price']], ['Time', 'Sale', 'Served by']) . ''],
  'B03' => ['kind' => 'log', 'title' => 'Security radio log', 'meta' => 'Raj Patel', 'body' => '
    <dl class="rows"><dt>18:36</dt><dd>“Walking to car park – complaint about blocked exit.”</dd><dt>18:43</dt><dd>“At car park, moving a van.” (car park camera confirms)</dd><dt>18:58</dt><dd>“Back in the square.”</dd></dl>'],
  'B04' => ['kind' => 'list', 'title' => 'Grotto photo bookings', 'meta' => 'Grotto photographer', 'body' => '
    ' . gn_t([['18:20', 'The Ahmeds'], ['18:28', 'The Coopers'], ['18:35–18:52', '<b>“Santa is feeding the reindeer – back soon!”</b>'], ['18:52', 'The Lis'], ['19:00', 'The Murphys']], ['Time', 'Family']) . ''],
  'B05' => ['kind' => 'interview', 'title' => 'The mulled wine seller', 'meta' => 'Elsa Berg', 'body' => '
    <p>“I was at my stall all night – my till shows it. About twenty to seven I saw Santa walking round the back of the grotto towards the cabins with his sack over his shoulder. I thought he was fetching more sweets.”</p>
    <p class="note">Elsa’s stall till: sales every few minutes from 18:00 to 19:30.</p>'],
  'B06' => ['kind' => 'interview', 'title' => 'The choir leader', 'meta' => 'Lucy Green', 'body' => '
    <p>“Last year someone said I pocketed the choir’s collection. It wasn’t true then and it isn’t true now. I was conducting thirty singers in front of the whole town.”</p>'],
  'C01' => ['kind' => 'interview', 'title' => 'Santa’s statement', 'meta' => 'Harry Knight', 'body' => '
    <p>“I was in the grotto the whole evening, children on my knee one after another. Ask the photographer – she has every family booked. I never went near the cabin after four o’clock.”</p>'],
  'C02' => ['kind' => 'letter', 'title' => 'Letter in Harry’s coat', 'meta' => 'From his landlord', 'body' => '
    <p class="handwriting">Mr Knight – you are now £2,900 behind with the rent. If it is not paid in full by Monday 8 December I will start eviction proceedings. This is your final warning.</p>'],
  'C03' => ['kind' => 'report', 'title' => 'Search of the grotto', 'meta' => 'Police, Saturday 20:15', 'body' => '
    <p>Behind the grotto’s back curtain: Santa’s main sack. Inside, under the sweets: <b>three paper money bands</b> printed “Ashby Market – Charity”, and £600 in notes.</p>'],
  'C04' => ['kind' => 'interview', 'title' => 'The assistant', 'meta' => 'Noah Price', 'body' => '
    <p>“Yes, I know the code, and yes, I’m broke – I’m a student. But I was on the gate all evening selling tickets. I couldn’t leave it for a second; there were queues.”</p>'],
  'C05' => ['kind' => 'note', 'title' => 'Cash-box bands', 'meta' => 'Market treasurer', 'body' => '
    <p>All charity money is banded in £200 bundles with printed paper bands “Ashby Market – Charity”. The bands are kept in the cash box itself and nowhere else.</p>'],
  'C06' => ['kind' => 'interview', 'title' => 'The photographer', 'meta' => 'Grotto bookings', 'body' => '
    <p>“Harry put up the reindeer sign at twenty-five to seven and went out the back. He was gone about a quarter of an hour. He came back a bit out of breath and wouldn’t stop fiddling with his sack.”</p>'],
 ],
 'checkpoints' => [
  'A' => ['title' => 'The moment', 'prompt' => 'When was the cash box taken?',
          'gate' => ['q' => 'When did it happen?', 'choices' => ['Before 18:30', 'Between 18:42 and 18:45', 'At 19:15'], 'answer' => 1,
                     'ok' => 'The box was counted at 18:30, and the only time the cabin opened before 19:15 was 18:42–18:45. Open envelope B.'],
          'hints' => ['There was no forced entry – look at the keypad.', 'A01 and A02: one opening between the count and the discovery.']],
  'B' => ['title' => 'The code holders', 'prompt' => 'Which of the four people with the code has no alibi at 18:42?',
          'gate' => ['q' => 'Who could have opened the cabin?', 'choices' => ['Maggie', 'Noah', 'Raj', 'Harry'], 'answer' => 3,
                     'ok' => 'Maggie was on stage, Noah at the gate and Raj in the car park. Santa had put up his “reindeer” sign from 18:35 to 18:52. Open envelope C.'],
          'hints' => ['A05 names the four people with the code.', 'B01, B02 and B03 place three of them; B04 shows a gap for the fourth.']],
  'final' => ['title' => 'The accusation', 'prompt' => 'Who took the cash box, and why?',
          'hints' => ['Compare Santa’s story with the bookings and the photographer.', 'C01 against B04 and C06; C03 and C05 link the sack to the cash box; C02 is the reason.']],
 ],
 'accuse' => [
  'culprit_q' => 'Who stole the charity cash box?',
  'wrong' => 'That’s not the person who opened the cabin.',
  'items' => ['when' => ['The moment', 'When was it taken?', 4], 'how' => ['The method', 'How was it done?', 4], 'motive' => ['The motive', 'Why was it done?', 3]],
 ],
 'choices' => [
  'when' => [
   'a' => 'Before Maggie’s count at 18:30.',
   'b' => 'Between 18:42 and 18:45, during the carols.',
   'c' => 'During the lights switch-on at 19:00.',
   'd' => 'At 19:15, when Maggie returned.',
  ],
  'how' => [
   'a' => 'The window was forced.',
   'b' => 'Santa put up his “reindeer” sign, slipped round to the cabin, used the code and carried the money away in his sack.',
   'c' => 'Noah left the gate and used the code.',
   'd' => 'Raj used his round to open the cabin.',
  ],
  'motive' => [
   'a' => 'To embarrass the organiser.',
   'b' => 'To pay £2,900 of overdue rent before he was evicted.',
   'c' => 'To pay for his studies.',
   'd' => 'Revenge for last year’s collection rumour.',
  ],
 ],
 'worksheet' => ['Who did it?', 'When was the cash box taken?', 'How was it done?', 'Why?', 'Which details were red herrings?'],
 'solution_title' => 'What really happened at the Christmas market',
];
