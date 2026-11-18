<?php
// Game Night case 018: Overboard at Midnight. Server-side only.
return [
 'slug' => 'overboard-at-midnight',
 'no' => '018',
 'title' => 'Overboard at Midnight',
 'tagline' => 'A shipping heir goes missing on the night ferry. The sea keeps no witnesses – but the ship does.',
 'teaser' => 'On the overnight ferry from Kiel to Oslo, wealthy passenger Henrik Sand never turns up for breakfast. His bed has not been slept in, and one of his shoes lies by the rail on the aft deck. Someone sent him over the side in the dark.',
 'genre' => 'Murder',
 'level' => 3,
 'minutes' => [100, 140],
 'players' => [2, 6],
 'revision' => '1.0',
 'caseref' => 'MSN-2026-0712',
 'stamp' => 'MAN OVERBOARD',
 'envelope' => '#BFD0DA', 'flap' => '#9FB6C4',
 'cast' => true,
 'cover' => ['file' => 'overboard-at-midnight/cover.jpg', 'prompt' => 'Cinematic illustration of the empty aft deck of a large overnight ferry at night, a single leather shoe lying by the white railing, black sea and the ship’s churning wake under a cold moon, deck lamps glowing, noir mood, deep blue and amber palette, no people, no text, 4:3'],
 'intro' => [
  'The <b>MS Nordlys</b> sails from Kiel at 19:00 and reaches Oslo at 09:45. Among the passengers: <b>Henrik Sand</b>, 41, heir to a shipping fortune, travelling with his girlfriend, his half-sister and his business partner.',
  'At 07:10 Henrik is missing. His cabin bed is untouched, and at 05:30 a deckhand found one of his shoes by the rail on deck 7 aft. The captain has turned the ship around to search – and asked you to find out what happened before she docks.',
 ],
 'mission' => [
  'Work out where and when Henrik went over the side.',
  'Work out who was with him.',
  'Name the killer – and the reason.',
  'Back up your accusation with at least four document numbers.',
 ],
 'questions' => [
  'Where was Henrik last seen, and when?',
  'Who could reach deck 7 aft in the middle of the night?',
  'Who was out of their cabin – and who has a witness?',
  'Who is pointing the finger, and does their story hold?',
  'Who gains from Henrik’s death?',
  'Which suspicious moments were innocent?',
 ],
 'suspects' => [
  ['id' => 'paul-meyer', 'name' => 'Paul Meyer', 'role' => 'Business partner'],
  ['id' => 'ingrid-sand', 'name' => 'Ingrid Sand', 'role' => 'Half-sister'],
  ['id' => 'lea-horn', 'name' => 'Lea Horn', 'role' => 'Girlfriend'],
  ['id' => 'tomas-berg', 'name' => 'Tomas Berg', 'role' => 'Purser'],
  ['id' => 'svea-lund', 'name' => 'Svea Lund', 'role' => 'Bartender'],
  ['id' => 'karl-nyberg', 'name' => 'Karl Nyberg', 'role' => 'Deckhand'],
 ],
 'packets' => [
  'START' => ['label' => 'Start folder', 'docs' => ['A01', 'A02', 'A03', 'A04', 'A05', 'A06']],
  'B' => ['label' => 'Envelope B', 'when' => 'you can say where and when Henrik went overboard', 'docs' => ['B01', 'B02', 'B03', 'B04', 'B05', 'B06']],
  'C' => ['label' => 'Envelope C', 'when' => 'you can say who went out on deck with him', 'docs' => ['C01', 'C02', 'C03', 'C04', 'C05', 'C06']],
 ],
 'docs' => [
  'A01' => ['kind' => 'report', 'title' => 'Captain’s report', 'meta' => 'MS Nordlys · night crossing', 'body' => '
    <dl class="rows"><dt>05:30</dt><dd>Deckhand finds a man’s brown brogue by the rail, deck 7 aft</dd><dt>07:10</dt><dd>H. Sand misses breakfast; cabin 7112 empty, bed unslept</dd><dt>07:25</dt><dd>Ship turns back; search with coastguard</dd></dl>
    <p class="note">No man-overboard alarm was raised during the night.</p>'],
  'A02' => ['kind' => 'messages', 'title' => 'Henrik’s last messages', 'meta' => 'Recovered from his cloud backup', 'body' => '
    <div class="chat"><p class="msg out"><span>00:58 · Henrik → Lea</span>Going up to the back deck to sort out the money thing. Won’t be long. Don’t wait up.</p><p class="msg in"><span>01:02 · Lea</span>Ok. Be nice 😘 I’m still at the bar.</p></div>
    <p class="note">The phone’s last connection: 01:13, aft deck Wi-Fi point.</p>'],
  'A03' => ['kind' => 'photo', 'title' => 'Aft deck camera', 'meta' => 'Deck 7, camera 12 (night mode)', 'img' => ['file' => 'overboard-at-midnight/deck.jpg', 'caption' => 'Camera 12 at 01:14', 'prompt' => 'Grainy black and white night-vision CCTV still of a ferry’s aft deck, two blurred figures by the railing, one in a pale jacket, one in a dark hooded coat, faces not visible, ship wake behind, timestamp-style framing without readable text, 4:3'], 'body' => '
    <p><b>01:14</b> – two figures at the rail: one in a pale jacket, one in a <b>dark hooded coat</b>. Faces not visible.</p>
    <p><b>01:16</b> – only the figure in the dark coat, walking towards the deck door.</p>
    <p><b>01:17</b> – deck empty.</p>
    {{IMG}}'],
  'A04' => ['kind' => 'list', 'title' => 'Henrik’s party', 'meta' => 'Booking, deck 7 and 8', 'body' => '
    ' . gn_t([['Henrik Sand', '7112', 'Cream linen jacket at dinner'], ['Lea Horn', '7112', 'Girlfriend'], ['Ingrid Sand', '8020', 'Half-sister'], ['Paul Meyer', '7140', 'Business partner']], ['Name', 'Cabin', 'Note']) . ''],
  'A05' => ['kind' => 'report', 'title' => 'Dinner notes', 'meta' => 'Head waiter, Bistro Nord', 'body' => '
    <p>Table 9, 20:00–22:15. Henrik and Lea argued loudly about “that woman in Hamburg”; Lea left the table in tears for ten minutes. Henrik and Paul spoke quietly about “the October payment”. Ingrid left early, at 21:30, saying she was seasick.</p>'],
  'A06' => ['kind' => 'calendar', 'title' => 'Ship’s night routine', 'meta' => 'Passenger information', 'body' => '
    <dl class="rows"><dt>00:30</dt><dd>Casino closes</dd><dt>01:30</dt><dd>Nightclub bar closes</dd><dt>All night</dt><dd>Reception (deck 6) staffed by the purser</dd></dl>
    <p class="note">Outer deck doors open from inside with any cabin card; every swipe is logged.</p>'],
  'B01' => ['kind' => 'log', 'title' => 'Deck 7 aft door log', 'meta' => 'Card readers', 'body' => '
    ' . gn_t([['23:12', 'Crew 31', 'K. Nyberg'], ['01:09', 'Cabin 7112', 'Card 1 (H. Sand)'], ['01:11', 'Cabin 7140', 'P. Meyer'], ['01:16', 'Cabin 7140', 'P. Meyer (back inside)'], ['05:28', 'Crew 31', 'K. Nyberg']], ['Time', 'Card', 'Holder']) . ''],
  'B02' => ['kind' => 'log', 'title' => 'Cabin door log', 'meta' => 'Decks 7 and 8', 'body' => '
    ' . gn_t([['23:40', '8020', 'In'], ['00:50', '7140', 'Out'], ['00:55', '7112', 'Out'], ['01:19', '7140', 'In'], ['01:41', '7112', 'In'], ['07:30', '8020', 'Out']], ['Time', 'Cabin', 'Door']) . '
    <p class="note">Cabin 8020 was not opened between 23:40 and 07:30.</p>'],
  'B03' => ['kind' => 'receipt', 'title' => 'Nightclub bar till', 'meta' => 'Deck 9', 'body' => '
    ' . gn_t([['00:44', 'Mojito', 'Cabin 7112 – L. Horn'], ['01:05', 'Mojito', 'Cabin 7112 – L. Horn'], ['01:20', 'Water', 'Cabin 7112 – L. Horn'], ['01:28', 'Last orders', '–']], ['Time', 'Order', 'Charged to']) . '
    <p class="note">Bartender Svea Lund: “She sat at the bar from half twelve until we closed. Talked my ear off about her boyfriend.”</p>'],
  'B04' => ['kind' => 'log', 'title' => 'Reception log', 'meta' => 'Deck 6, purser on duty', 'body' => '
    <dl class="rows"><dt>00:45</dt><dd>Complaint, cabin 5022, noise – T. Berg</dd><dt>01:05</dt><dd>Lost-key request, cabin 6110 – T. Berg</dd><dt>01:20</dt><dd>Seasickness tablets, cabin 8021 – T. Berg</dd></dl>
    <p class="note">The purser holds a master card. It was not swiped anywhere on deck 7 that night.</p>'],
  'B05' => ['kind' => 'interview', 'title' => 'The deckhand', 'meta' => 'Karl Nyberg', 'body' => '
    <p>“I did my rounds at eleven and again at half five – that’s when I found the shoe. In between I was on the car deck, checking lashings. Nobody told me anything about a man in the water.”</p>
    <p class="note">Car deck log: K. Nyberg, 23:30–05:15.</p>'],
  'B06' => ['kind' => 'interview', 'title' => 'The half-sister', 'meta' => 'Ingrid Sand', 'body' => '
    <p>“Yes, I inherit the shares if Henrik dies – Father’s will. That doesn’t make me a murderer. I was sick as a dog all night and never left my cabin.”</p>'],
  'C01' => ['kind' => 'interview', 'title' => 'The business partner', 'meta' => 'Paul Meyer', 'body' => '
    <p>“I went out for a cigarette at about ten past one. Henrik was at the rail with a woman in a dark hooded coat – I assumed it was Lea and left them to it. I was back inside within a few minutes. When I left him he was alive.”</p>'],
  'C02' => ['kind' => 'report', 'title' => 'Search of cabin 7140', 'meta' => 'Ship’s security', 'body' => '
    <p>In the wardrobe: a <b>navy hooded coat</b>, still damp, with salt spray on the shoulders. One button torn off.</p>
    <p class="note">Found on deck 7 aft, by the rail: a navy coat button.</p>'],
  'C03' => ['kind' => 'audit', 'title' => 'Loan agreement', 'meta' => 'Sand Shipping / Meyer Logistics', 'body' => '
    <p>Henrik Sand lent Paul Meyer’s company <b>€2,000,000</b>. Repayment due 1 October. Unpaid.</p>
    <p class="note">Email, Henrik to Paul, 10 Nov: “Pay by Friday or my lawyers file on Monday. I won’t carry you any longer.”</p>'],
  'C04' => ['kind' => 'audit', 'title' => 'Partnership insurance', 'meta' => 'Joint venture policy', 'body' => '
    <p>Key-person cover on Henrik Sand: <b>€3,000,000</b>, paid to the joint venture – which Paul Meyer controls alone if Henrik dies. On his death the loan is also written off against the policy.</p>'],
  'C05' => ['kind' => 'interview', 'title' => 'The girlfriend', 'meta' => 'Lea Horn', 'body' => '
    <p>“We had a row at dinner, I admit it. But I was at the bar until it closed – ask Svea. I don’t even own a dark coat; I was wearing a red dress.”</p>'],
  'C06' => ['kind' => 'note', 'title' => 'Smokers’ corner', 'meta' => 'Ship’s rules', 'body' => '
    <p>Smoking is permitted only on <b>deck 9, port side</b>. Deck 7 aft is non-smoking and has no ashtrays.</p>
    <p class="note">No cigarette ends were found on deck 7 aft in the morning.</p>'],
 ],
 'checkpoints' => [
  'A' => ['title' => 'The last minutes', 'prompt' => 'Where and when did Henrik go over the side?',
          'gate' => ['q' => 'Where and when?', 'choices' => ['From his cabin balcony at 00:55', 'From deck 7 aft at about 01:15', 'From the car deck at 05:15'], 'answer' => 1,
                     'ok' => 'His phone went quiet at 01:13 on the aft deck, and at 01:16 only one figure walked away from the rail. Open envelope B.'],
          'hints' => ['Follow his messages and the camera.', 'A02 sends him to the back deck; A03 shows two figures at 01:14 and one at 01:16.']],
  'B' => ['title' => 'The other figure', 'prompt' => 'Who went out onto deck 7 aft with Henrik?',
          'gate' => ['q' => 'Whose card opened the deck door after Henrik’s?', 'choices' => ['Lea Horn’s', 'Paul Meyer’s', 'The purser’s master card'], 'answer' => 1,
                     'ok' => 'Paul’s card opened the aft door at 01:11 and came back in at 01:16 – the same minute the dark figure walked away. Open envelope C.'],
          'hints' => ['The aft door logs every card.', 'B01 lists the swipes; B02, B03 and B04 tell you where everyone else was.']],
  'final' => ['title' => 'The accusation', 'prompt' => 'Who killed Henrik Sand, and why?',
          'hints' => ['Test Paul’s story about a woman in a dark coat.', 'C01 against C02, C05 and C06; C03 and C04 give the reason.']],
 ],
 'accuse' => [
  'culprit_q' => 'Who killed Henrik Sand?',
  'wrong' => 'That’s not the person who was at the rail with Henrik.',
  'items' => ['where' => ['The place and time', 'Where and when did it happen?', 4], 'how' => ['The method', 'How was it done?', 4], 'motive' => ['The motive', 'Why was it done?', 3]],
 ],
 'choices' => [
  'where' => [
   'a' => 'In cabin 7112, at 00:55.',
   'b' => 'On deck 7 aft, between 01:11 and 01:16.',
   'c' => 'On the car deck, at 05:15.',
   'd' => 'In the nightclub, at 01:20.',
  ],
  'how' => [
   'a' => 'He fell while drunk, alone.',
   'b' => 'Paul followed him out with his own card, wearing his navy hooded coat, and pushed him over the rail.',
   'c' => 'The purser used his master card to reach the deck.',
   'd' => 'Lea slipped away from the bar and pushed him.',
  ],
  'motive' => [
   'a' => 'Jealousy over the woman in Hamburg.',
   'b' => 'To escape a €2m debt that was about to go to court, and collect €3m in insurance.',
   'c' => 'To inherit the family shares.',
   'd' => 'Revenge for a complaint to the shipping line.',
  ],
 ],
 'worksheet' => ['Who did it?', 'Where and when?', 'How was it done?', 'Why?', 'Which details were red herrings?'],
 'solution_title' => 'What really happened on the MS Nordlys',
];
