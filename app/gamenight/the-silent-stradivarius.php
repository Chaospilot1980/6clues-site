<?php
// Game Night case 017: The Silent Stradivarius. Server-side only.
return [
 'slug' => 'the-silent-stradivarius',
 'no' => '017',
 'title' => 'The Silent Stradivarius',
 'tagline' => 'The concert was a triumph. The violin that played the second half was a fake.',
 'teaser' => 'A star soloist plays a priceless 1721 violin to a full hall. After the encore the foundation’s expert takes one look and goes pale: it is a brilliant copy. Somewhere between the first note and the last, someone swapped it.',
 'genre' => 'Theft',
 'level' => 2,
 'minutes' => [90, 120],
 'players' => [2, 6],
 'revision' => '1.0',
 'caseref' => 'HH-2026-1721',
 'stamp' => 'ART THEFT',
 'envelope' => '#D8CBB0', 'flap' => '#BFAE8C',
 'cast' => true,
 'cover' => ['file' => 'the-silent-stradivarius/cover.jpg', 'prompt' => 'Cinematic illustration of an empty concert hall stage after a performance, a single antique violin lying in an open velvet-lined case under a spotlight, rows of red seats in shadow, dramatic noir mood, warm gold and deep red palette, no people, no text, 4:3'],
 'intro' => [
  'Friday night at <b>Halvorsen Hall</b>. Soloist Ana Petrov plays the <b>“Aurora”</b>, a Stradivarius from 1721 lent to her by the Lindqvist Foundation. Standing ovation. Two encores.',
  'At 21:40 the foundation’s curator takes the violin back – and finds a superb modern copy in its case. The real Aurora, insured for €4 million, has vanished. The foundation wants it back quietly. You have one evening.',
 ],
 'mission' => [
  'Work out when the violin was swapped.',
  'Work out how the thief got to it.',
  'Name the thief – and the reason.',
  'Back up your accusation with at least four document numbers.',
 ],
 'questions' => [
  'Was the Aurora genuine at the start of the concert?',
  'Can you tell the real violin from the copy in a photo?',
  'Where was the violin during the interval – and who could open its room and its case?',
  'Where did such a perfect copy come from?',
  'Who says they were somewhere they were not?',
  'Which suspicious moments were innocent?',
 ],
 'suspects' => [
  ['id' => 'oskar-dahl', 'name' => 'Oskar Dahl', 'role' => 'Ana’s agent'],
  ['id' => 'ana-petrov', 'name' => 'Ana Petrov', 'role' => 'Soloist'],
  ['id' => 'clara-voss', 'name' => 'Clara Voss', 'role' => 'Foundation curator'],
  ['id' => 'felix-brandt', 'name' => 'Felix Brandt', 'role' => 'Violin maker'],
  ['id' => 'mei-lin', 'name' => 'Mei Lin', 'role' => 'Orchestra leader'],
  ['id' => 'jonas-eide', 'name' => 'Jonas Eide', 'role' => 'Stage manager'],
 ],
 'packets' => [
  'START' => ['label' => 'Start folder', 'docs' => ['A01', 'A02', 'A03', 'A04', 'A05', 'A06']],
  'B' => ['label' => 'Envelope B', 'when' => 'you can say when the violin was swapped', 'docs' => ['B01', 'B02', 'B03', 'B04', 'B05', 'B06']],
  'C' => ['label' => 'Envelope C', 'when' => 'you can say how the thief got to the violin', 'docs' => ['C01', 'C02', 'C03', 'C04', 'C05', 'C06']],
 ],
 'docs' => [
  'A01' => ['kind' => 'report', 'title' => 'Incident note', 'meta' => 'Halvorsen Hall · Friday', 'body' => '
    <dl class="rows"><dt>18:30</dt><dd>Curator inspects the Aurora and hands it to Ana</dd><dt>19:30</dt><dd>Concert begins – first half: Sibelius concerto</dd><dt>20:05–20:25</dt><dd>Interval – violin locked in its case in dressing room 4</dd><dt>20:25</dt><dd>Second half – Bruch concerto, two encores</dd><dt>21:40</dt><dd>Curator finds a copy in the case</dd></dl>'],
  'A02' => ['kind' => 'lab', 'title' => 'Curator’s check, 18:30', 'meta' => 'Clara Voss, Lindqvist Foundation', 'body' => '
    <p>Aurora examined in dressing room 4. Label, varnish and wood all genuine. Known marks present, including the <b>small chip on the left side of the scroll</b> (since 1890).</p>
    <p class="note">Signed and handed to the soloist at 18:35.</p>'],
  'A03' => ['kind' => 'photo', 'title' => 'Press photos', 'meta' => 'Hall photographer', 'img' => ['file' => 'the-silent-stradivarius/stage.jpg', 'caption' => 'Close-up of the scroll, 20:03', 'prompt' => 'Close-up photograph of the scroll and pegbox of an antique violin under warm stage light, a tiny chip in the varnish visible on the left side of the scroll, shallow depth of field, concert hall bokeh, no readable text, 4:3'], 'body' => '
    <p><b>20:03</b> – last bars of the Sibelius: chip on the scroll clearly visible.</p>
    <p><b>20:41</b> – Bruch, slow movement, same angle: <b>scroll undamaged</b>.</p>
    {{IMG}}'],
  'A04' => ['kind' => 'lab', 'title' => 'Expert opinion on the copy', 'meta' => 'Foundation expert, Saturday', 'body' => '
    <p>Superb workmanship. Varnish less than a month old. Every mark of the Aurora reproduced – <b>except the chip on the scroll</b>, which the maker seems to have missed.</p>
    <p class="note">This is the work of a top professional violin maker, made with the original to hand.</p>'],
  'A05' => ['kind' => 'interview', 'title' => 'The soloist', 'meta' => 'Ana Petrov', 'body' => '
    <p>“After the Sibelius I put the Aurora in its case, spun the lock and left it in room 4. Then I went straight to the green room for the radio interview. In the second half it felt… a little brighter. I put it down to nerves.”</p>'],
  'A06' => ['kind' => 'list', 'title' => 'Who was in the building', 'meta' => 'Backstage list', 'body' => '
    ' . gn_t([['Ana Petrov', 'Soloist', 'Dressing room 4'], ['Oskar Dahl', 'Agent', 'Artist pass'], ['Clara Voss', 'Curator', 'Seat 1-12, stalls'], ['Felix Brandt', 'Violin maker (guest)', 'Seat 14-3, stalls'], ['Mei Lin', 'Orchestra leader', 'Dressing room 5'], ['Jonas Eide', 'Stage manager', 'Master key']], ['Name', 'Role', 'Room / access']) . ''],
  'B01' => ['kind' => 'log', 'title' => 'Dressing room door log', 'meta' => 'Corridor B, electronic locks', 'body' => '
    ' . gn_t([['20:06', 'Room 4', 'Artist pass 1'], ['20:07', 'Room 5', 'Orchestra pass 17'], ['20:11', 'Room 4', '<b>Artist pass 2</b>'], ['20:14', 'Room 4', 'Artist pass 2 (exit)'], ['20:22', 'Room 4', 'Artist pass 1']], ['Time', 'Door', 'Opened by']) . '
    <p class="note">Master key: not used all evening.</p>'],
  'B02' => ['kind' => 'list', 'title' => 'Pass register', 'meta' => 'Stage door', 'body' => '
    ' . gn_t([['Artist pass 1', 'A. Petrov', '17:45'], ['Artist pass 2', 'O. Dahl', '17:50'], ['Orchestra pass 17', 'M. Lin', '18:10']], ['Pass', 'Signed out by', 'Time']) . '
    <p class="note">Passes are personal. None was reported lost.</p>'],
  'B03' => ['kind' => 'report', 'title' => 'Radio interview', 'meta' => 'Live stream, green room', 'body' => '
    <p>Ana Petrov on air with the presenter from <b>20:08 to 20:21</b>, on camera throughout.</p>
    <p class="note">The green room is on the floor above corridor B.</p>'],
  'B04' => ['kind' => 'note', 'title' => 'The violin case', 'meta' => 'Foundation case, combination lock', 'body' => '
    <p>Three-digit combination. Known to: <b>the soloist and her agent</b> (“in case Ana forgets it on tour”). The foundation keeps a sealed copy in Oslo.</p>'],
  'B05' => ['kind' => 'interview', 'title' => 'The orchestra leader', 'meta' => 'Mei Lin', 'body' => '
    <p>“Yes, I was in corridor B at the interval – my own room is number 5, I went to change a string. Ana and I don’t get on; everyone knows that. I never went near room 4.”</p>
    <p class="note">Her pass opened room 5 only (B01).</p>'],
  'B06' => ['kind' => 'interview', 'title' => 'The stage manager', 'meta' => 'Jonas Eide', 'body' => '
    <p>“The interval is my busiest twenty minutes – resetting the stage for the Bruch. I was on stage with the crew the whole time. My master key never left my belt.”</p>'],
  'C01' => ['kind' => 'interview', 'title' => 'The agent’s statement', 'meta' => 'Oskar Dahl', 'body' => '
    <p>“During the interval I was nowhere near room 4. Felix Brandt asked to borrow my pass to check a peg he was worried about, so I lent it to him around ten past eight. I was in the foyer bar the whole time.”</p>'],
  'C02' => ['kind' => 'receipt', 'title' => 'Foyer bar till', 'meta' => 'Interval', 'body' => '
    ' . gn_t([['20:06', 'Gin and tonic', 'Card – O. Dahl'], ['20:10', 'Glass of red, water', 'Card – F. Brandt'], ['20:12', 'Coffee', 'Card – C. Voss'], ['20:19', 'Champagne', 'Card – O. Dahl']], ['Time', 'Order', 'Paid']) . ''],
  'C03' => ['kind' => 'interview', 'title' => 'The violin maker', 'meta' => 'Felix Brandt', 'body' => '
    <p>“Borrow Oskar’s pass? Never. I spent the whole interval at the bar talking to Clara. And yes – a month ago Oskar paid me to make an exact copy of the Aurora ‘for insurance photographs’. He brought the original to my workshop for two days so I could measure it.”</p>
    <p class="note">Clara Voss confirms Felix was beside her at the bar from 20:08 to 20:24.</p>'],
  'C04' => ['kind' => 'receipt', 'title' => 'Workshop order', 'meta' => 'Brandt Violins', 'body' => '
    <dl class="rows"><dt>Customer</dt><dd>O. Dahl</dd><dt>Order</dt><dd>Exact copy of the “Aurora”, all marks reproduced</dd><dt>Price</dt><dd>€38,000</dd><dt>Collected</dt><dd>Thursday, by the customer</dd></dl>'],
  'C05' => ['kind' => 'letter', 'title' => 'Letter in Oskar’s hotel room', 'meta' => 'Sent from Geneva', 'body' => '
    <p class="handwriting">Dear Mr Dahl – my client’s offer stands: €1.5 million for the instrument we discussed, no questions and no paperwork. He understands your… difficulties with the bank. Delivery by Sunday.</p>'],
  'C06' => ['kind' => 'audit', 'title' => 'Insurance file', 'meta' => 'Lindqvist Foundation', 'body' => '
    <p>The Aurora’s insured value was raised from €3.2m to <b>€4m</b> in October – the routine five-yearly valuation, requested by the insurer, not by the curator.</p>
    <p class="note">The foundation itself receives nothing from a theft: the policy pays only to recover or replace the instrument.</p>'],
 ],
 'checkpoints' => [
  'A' => ['title' => 'The swap', 'prompt' => 'When was the real Aurora swapped for the copy?',
          'gate' => ['q' => 'When did it happen?', 'choices' => ['Before the concert', 'During the interval', 'After the encores'], 'answer' => 1,
                     'ok' => 'The chip is there at 20:03 and gone at 20:41 – the swap happened during the interval, in dressing room 4. Open envelope B.'],
          'hints' => ['The real violin has a mark the copy does not.', 'A02 and A04 describe the chip; A03 shows when it disappears.']],
  'B' => ['title' => 'The way in', 'prompt' => 'How did the thief get into room 4 and the case?',
          'gate' => ['q' => 'How did the thief get to the violin?', 'choices' => ['With the master key', 'With artist pass 2 and the case combination', 'Through room 5'], 'answer' => 1,
                     'ok' => 'Room 4 was opened at 20:11 by artist pass 2 – while Ana was on air upstairs. Only she and her agent know the combination. Open envelope C.'],
          'hints' => ['Look at who opened room 4 while Ana was busy.', 'B01 names the pass, B02 who signed it out, B03 where Ana was, B04 who knows the code.']],
  'final' => ['title' => 'The accusation', 'prompt' => 'Who stole the Aurora, and why?',
          'hints' => ['Does the pass holder’s story survive the bar till?', 'C01 against C02 and C03; C04 and C05 explain the copy and the reason.']],
 ],
 'accuse' => [
  'culprit_q' => 'Who stole the Aurora?',
  'wrong' => 'That’s not the person who swapped the violin.',
  'items' => ['when' => ['The moment', 'When was it swapped?', 4], 'how' => ['The method', 'How was it done?', 4], 'motive' => ['The motive', 'Why was it done?', 3]],
 ],
 'choices' => [
  'when' => [
   'a' => 'Before the concert, at the 18:30 check.',
   'b' => 'During the interval, at 20:11–20:14.',
   'c' => 'During the encores.',
   'd' => 'After the curator took the case back.',
  ],
  'how' => [
   'a' => 'With the stage manager’s master key.',
   'b' => 'With artist pass 2 and the case combination, swapping in a copy made by Felix Brandt.',
   'c' => 'Through dressing room 5 next door.',
   'd' => 'On stage, in front of the audience.',
  ],
  'motive' => [
   'a' => 'To ruin Ana’s career.',
   'b' => 'To sell the real violin to a collector for €1.5m and escape his debts.',
   'c' => 'To claim the €4m insurance.',
   'd' => 'To prove the copy was as good as the original.',
  ],
 ],
 'worksheet' => ['Who did it?', 'When was the violin swapped?', 'How was it done?', 'Why?', 'Which details were red herrings?'],
 'solution_title' => 'What really happened at Halvorsen Hall',
];
