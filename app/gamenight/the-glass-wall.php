<?php
// Game Night case 003: The Glass Wall. Server-side only. Translated and adapted from the Danish beta 'Glasvaeggen'.
return [
 'slug' => 'the-glass-wall',
 'no' => '003',
 'title' => 'The Glass Wall',
 'tagline' => 'The case was never opened. The masterpiece inside is a fake.',
 'teaser' => 'At the opening of a special exhibition, curators discover that a rare glass sculpture is a copy. No alarm, no broken lock – the original vanished somewhere between a check and the party.',
 'genre' => 'Museum theft',
 'level' => 1,
 'minutes' => [90, 120],
 'players' => [2, 6],
 'revision' => '1.0',
 'caseref' => 'GLW-2026-0312',
 'stamp' => 'FAKE',
 'envelope' => '#A9C7C2', 'flap' => '#86ABA5',
 'cast' => true,
 'cover' => ['file' => 'the-glass-wall/cover.jpg', 'prompt' => 'Cinematic illustration of a delicate abstract glass sculpture glowing inside a museum display case during an evening reception, blurred guests with champagne glasses in the background, a single blue glass thread running through the sculpture, teal and gold palette, elegant mystery mood, no faces, no text, 4:3'],
 'intro' => [
  'At 20:17, during the opening of a special exhibition at an art museum in Aarhus, the curators discover that a rare glass sculpture in display case M4 is a <b>copy</b>.',
  'The alarm never went off, and the case was never opened during the reception. Somewhere between a safety check in the afternoon and the party in the evening, the original vanished.',
 ],
 'mission' => [
  'Find out who removed the original sculpture.',
  'Explain how the swap was hidden – and when it really happened.',
  'Find out where the original was taken.',
  'Back up your accusation with at least four document numbers.',
 ],
 'questions' => [
  'Which object was really in the case before the reception?',
  'What do the weights of the transport box tell you?',
  'Who had a key and access to the workshop – and when?',
  'Which reports can be trusted, and which were written to mislead?',
  'Did anything else leave the workshop that afternoon?',
  'Who did what, when – and why?',
 ],
 'suspects' => [
  ['id' => 'sara-munk', 'name' => 'Sara Munk', 'role' => 'Conservator, responsible for condition reports'],
  ['id' => 'bo-vester', 'name' => 'Bo Vester', 'role' => 'Head of security, checked the access cards'],
  ['id' => 'lena-holm', 'name' => 'Lena Holm', 'role' => 'Curator of a financially pressed exhibition'],
  ['id' => 'emil-rahbek', 'name' => 'Emil Rahbek', 'role' => 'Transport manager with access to packing boxes'],
  ['id' => 'nadia-beck', 'name' => 'Nadia Beck', 'role' => 'Private collector, guest at the opening'],
  ['id' => 'jonas-friis', 'name' => 'Jonas Friis', 'role' => 'Photographer and external supplier'],
 ],
 'packets' => [
  'START' => ['label' => 'Start folder', 'docs' => ['A01', 'A02', 'A03', 'A04', 'A05', 'A06']],
  'B' => ['label' => 'Envelope B', 'when' => 'you agree which object was in the case before the reception began', 'docs' => ['B01', 'B02', 'B03', 'B04', 'B05', 'B06']],
  'C' => ['label' => 'Envelope C', 'when' => 'you can explain which part of the transport gives the swap away', 'docs' => ['C01', 'C02', 'C03', 'C04', 'C05', 'C06']],
 ],
 'docs' => [
  'A01' => ['kind' => 'report', 'title' => 'The report', 'meta' => 'Police note · opening night', 'body' => '
    <p>At 20:17 curator Lena Holm notices that the sculpture <b>‘The Glass Wall’</b> in display case M4 has a <b>matt scratch</b> on its base. The original has a <b>blue glass thread</b> in exactly that position.</p>
    <dl class="rows"><dt>Lock on M4</dt><dd>Intact</dd><dt>Alarm</dt><dd>No alarm registered after 18:00</dd><dt>Opening began</dt><dd>19:30</dd></dl>
    <p class="note">The case was not opened during the reception. When was the copy put in?</p>'],
  'A02' => ['kind' => 'list', 'title' => 'The object card', 'meta' => 'Collection register', 'body' => '
    <dl class="rows"><dt>Original</dt><dd>Registered mass <b>1,840 g</b>. A blue glass thread on the underside and a small maker’s mark <b>G17</b>.</dd>
    <dt>Approved copy</dt><dd>Mass <b>1,005 g</b>. A matt scratch on the base. Normally used for transport tests.</dd></dl>
    <p class="note">From a distance the two are almost impossible to tell apart.</p>'],
  'A03' => ['kind' => 'log', 'title' => 'Display case access log', 'meta' => 'Case M4 · electronic lock', 'body' => '
    ' . gn_t([['16:12', 'M4 opened', 'LENA-04'], ['16:28', 'M4 locked', 'LENA-04'], ['18:07', 'Self-test passed', 'SYSTEM'], ['16:28–20:17', 'No further openings', '—']], ['Time', 'Action', 'Card']) . '
    <p class="note">The case was opened exactly once that day: by Lena, between 16:12 and 16:28.</p>'],
  'A04' => ['kind' => 'report', 'title' => 'Security control room summary', 'meta' => 'Statement from Bo Vester', 'body' => '
    <p>Bo: “From 18:00 every alarm loop was active. If anyone had opened the case, we would know.”</p>
    <p>He also states that transport box <b>T12</b> was moved from the workshop to the exhibition hall between 15:35 and 16:05.</p>'],
  'A05' => ['kind' => 'photo', 'title' => 'The photographer’s contact sheet', 'meta' => 'Jonas Friis · six frames', 'img' => ['file' => 'the-glass-wall/contact-sheet.jpg', 'caption' => 'Frame 4, 16:24 – the base of the sculpture in case M4', 'prompt' => 'Close-up product photograph of the base of an abstract glass sculpture standing in a museum display case, a clearly visible matt scratch on the clear glass base and no coloured thread, soft gallery lighting, shallow depth of field, documentary style, no text'], 'body' => '
    <p>Jonas took six pictures at <b>16:24</b>, after the object had been placed in the case. In frame 4 the matt scratch is clearly visible – but <b>not</b> the blue glass thread.</p>
    {{IMG}}
    <p class="note">The photo times are confirmed by the file order on the camera’s memory card.</p>'],
  'A06' => ['kind' => 'interview', 'title' => 'Interviews: Lena and Jonas', 'meta' => 'Opening night, 21:00', 'body' => '
    <p><b>Lena:</b> “I opened the case at 16:12 because the workshop had reported the object ready. I took it out of T12 and put it in. I couldn’t tell the original from the copy at a distance.”</p>
    <p><b>Jonas:</b> “I photographed it straight away, just before it was locked. The scratch was already there.”</p>'],
  'B01' => ['kind' => 'log', 'title' => 'Shipping journal, box T12', 'meta' => 'Weighed on calibrated scales', 'body' => '
    ' . gn_t([['09:05', '7,440 g', 'Box with the original'], ['15:46', '6,605 g', 'Box returned from the workshop'], ['17:08', '5,600 g', 'Empty box to depot D2']], ['Time', 'Registered mass', 'Note']) . ''],
  'B02' => ['kind' => 'audit', 'title' => 'Box tare and contents', 'meta' => 'Transport department', 'body' => '
    <dl class="rows"><dt>Empty T12</dt><dd><b>5,600 g</b></dd><dt>Other parts</dt><dd>None – nothing else travels in the box</dd></dl>
    <p>At the morning check the original lay in T12. The scales were calibrated the same morning.</p>
    <p class="note">Subtract the box. What was inside it at 09:05 – and at 15:46?</p>'],
  'B03' => ['kind' => 'report', 'title' => 'Keys and access roles', 'meta' => 'Key register, box T12', 'body' => '
    <p>T12 has two keys. They were issued to conservator <b>Sara Munk</b> and transport manager <b>Emil Rahbek</b>.</p>
    <p>Emil handed in his key at 11:10 in a <b>sealed key bag</b>. The seal was broken at 17:20 by Bo.</p>
    <p>Sara’s key was not handed in until <b>18:25</b>.</p>'],
  'B04' => ['kind' => 'log', 'title' => 'Workshop log', 'meta' => 'Conservation workshop · door register', 'body' => '
    ' . gn_t([['13:54', 'Sara receives T12 from the transport team. Emil delivers it to the door but is not let in.'], ['15:33', 'Sara hands the closed box to an internal porter.']], ['Time', 'Event']) . '
    <p class="note">Nobody else was registered inside the workshop between 13:54 and 15:33.</p>'],
  'B05' => ['kind' => 'report', 'title' => 'Workshop condition report', 'meta' => 'Signed 15:21', 'img' => ['file' => 'the-glass-wall/condition-photo.jpg', 'caption' => 'Photo attached to the condition report', 'prompt' => 'Close-up photograph of the underside of a clear glass sculpture with a fine cobalt-blue glass thread running through it, on a white conservation table under a ring light, clinical museum-lab style, no text'], 'body' => '
    <p class="quote">“Original checked. Blue thread G17 verified. No change in mass.” – S. Munk</p>
    {{IMG}}
    <p class="note">The attached photo shows the underside of an object – but the image file was created the <b>week before</b>.</p>'],
  'B06' => ['kind' => 'messages', 'title' => 'Nadia’s messages', 'meta' => 'Handed over by Lena', 'body' => '
    <div class="chat"><p class="msg in"><span>14:40 · Nadia Beck → Lena</span>I’d gladly pay for a private viewing.</p>
    <p class="msg out"><span>15:02 · Lena → Nadia Beck</span>There’s no access outside the museum’s policy.</p></div>
    <p class="note">Nadia’s phone is first registered on the museum’s guest Wi-Fi in reception at <b>19:22</b>.</p>'],
  'C01' => ['kind' => 'report', 'title' => 'Service trolley receipt', 'meta' => 'Internal porter', 'body' => '
    <p>At 15:39 a service trolley carried <b>two closed boxes</b> from the workshop to the goods lift. The porter wrote:</p>
    <p class="handwriting">S. Munk: one box to display case, one marked RETURN FILTER to service dept.</p>
    <p class="note">Only T12 was registered in advance in the transport plan.</p>'],
  'C02' => ['kind' => 'log', 'title' => 'Service department log', 'meta' => 'Service shelf 3', 'body' => '
    ' . gn_t([['16:02', 'Box ‘RETURN FILTER’ received on service shelf 3. Not opened.'], ['18:31', 'Moved to depot D2 after an email from Sara.']], ['Time', 'Event']) . '
    <p class="quote">Sara’s email: “Must not be opened before Monday because of a dust sample.”</p>'],
  'C03' => ['kind' => 'audit', 'title' => 'Inventory list: RETURN FILTER', 'meta' => 'Black service box', 'body' => '
    <dl class="rows"><dt>Space inside</dt><dd>Room for an object of 30 × 18 × 12 cm</dd><dt>Registered total</dt><dd><b>2,790 g</b></dd><dt>Empty box + filter</dt><dd>950 g</dd></dl>
    <p class="note">What weighs the difference?</p>'],
  'C04' => ['kind' => 'messages', 'title' => 'Email to a private address', 'meta' => 'Unsent draft in Sara’s work email', 'body' => '
    <p class="quote">“I can get it out of the museum flow without breaking the alarm. We won’t talk price yet. Once the control copy is in place, I have a few days.”</p>
    <p class="note">The recipient field was empty.</p>'],
  'C05' => ['kind' => 'interview', 'title' => 'Interview: Emil Rahbek', 'meta' => 'Transport manager', 'body' => '
    <p>“I only moved the box Sara gave me. I was never inside the workshop, and my key was sealed in its bag all afternoon. I thought RETURN FILTER was rubbish from building the exhibition.”</p>'],
  'C06' => ['kind' => 'report', 'title' => 'Final checkpoint', 'meta' => 'Monday, 08:10 · filmed by the police', 'body' => '
    <p>The police open RETURN FILTER on camera. The sculpture with the blue glass thread and the mark <b>G17</b> lies inside the dust filter.</p>
    <p class="note">There is no sign that the box was opened after Sara’s email.</p>'],
 ],
 'checkpoints' => [
  'A' => ['title' => 'The case that was never opened', 'prompt' => 'The case was only opened once that day. So when did the copy go in?',
          'gate' => ['q' => 'Which object was in case M4 when Jonas took his photos at 16:24?', 'choices' => ['The original', 'The copy', 'It can’t be decided'], 'answer' => 1,
                     'ok' => 'Frame 4 shows the matt scratch and no blue thread – the copy went into the case in the afternoon, long before the reception. Open envelope B.'],
          'hints' => ['Follow the weight, the seals and the case log – the reception is a red herring.', 'Compare the object card (A02) with the photo from 16:24 (A05).']],
  'B' => ['title' => 'Weight and access', 'prompt' => 'Which link in the transport chain gives the swap away – and who had the box at that time?',
          'gate' => ['q' => 'What do the weights of T12 tell you?', 'choices' => ['The original was sent back in T12', 'The copy was already in T12 when it left the workshop', 'The scales were out of order'], 'answer' => 1,
                     'ok' => '6,605 − 5,600 = 1,005 g: the copy. The swap happened before T12 left the workshop. Open envelope C.'],
          'hints' => ['Compare the morning weighing and the return weighing of the same box.', '6,605 − 5,600 = 1,005 grams. Who had the box between 13:54 and 15:33?']],
  'final' => ['title' => 'The accusation', 'prompt' => 'Who organised the swap, how was it hidden, and where did the original go?',
          'hints' => ['Ask who controlled both the condition report and the box key.', 'Put B03, B04, C01 and C03 side by side.']],
 ],
 'accuse' => [
  'culprit_q' => 'Who swapped the Glass Wall?',
  'wrong' => 'That’s not the person who swapped the sculpture.',
  'items' => ['where' => ['The swap', 'When and where was the original swapped?', 4], 'trace' => ['The giveaway', 'Which record gives the swap away?', 4], 'hide' => ['The hiding place', 'Where did the original go?', 3]],
 ],
 'choices' => [
  'where' => [
   'a' => 'During the opening reception, inside the locked case.',
   'b' => 'In the workshop, before the box left at 15:33.',
   'c' => 'When Lena opened the case at 16:12.',
   'd' => 'In depot D2 that evening.',
  ],
  'trace' => [
   'a' => 'The alarm log – the case was opened during the reception.',
   'b' => 'T12’s weights: 6,605 g minus 5,600 g is exactly the copy’s 1,005 g.',
   'c' => 'Nadia’s message to Lena.',
   'd' => 'Bo breaking the seal on Emil’s key bag.',
  ],
  'hide' => [
   'a' => 'Back to the lender in box T12.',
   'b' => 'Out of the building in Nadia’s handbag.',
   'c' => 'Into the extra service box RETURN FILTER, then to depot D2.',
   'd' => 'Into the photographer’s camera bag.',
  ],
 ],
 'worksheet' => ['Who swapped the sculpture?', 'When and where did the swap happen?', 'Which record gives it away?', 'Where did the original go?', 'Which details were red herrings?'],
 'solution_title' => 'What really happened to the Glass Wall',
];
