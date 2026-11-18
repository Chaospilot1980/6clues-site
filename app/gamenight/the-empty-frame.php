<?php
// Game Night case 015: The Empty Frame. Server-side only.
return [
 'slug' => 'the-empty-frame',
 'no' => '015',
 'title' => 'The Empty Frame',
 'tagline' => 'The frame is still on the wall. The painting is not. The alarm never made a sound.',
 'teaser' => 'At a glittering fundraiser, the Calder Art Museum’s most famous painting is found missing from its frame – in a gallery nobody entered all evening. Everyone assumes it was taken during the party. Everyone is wrong.',
 'genre' => 'Museum theft',
 'level' => 2,
 'minutes' => [100, 140],
 'players' => [2, 6],
 'revision' => '1.0',
 'caseref' => 'CAM-2026-1107',
 'stamp' => 'THEFT',
 'envelope' => '#C9B6D8', 'flap' => '#A994BC',
 'cast' => true,
 'cover' => ['file' => 'the-empty-frame/cover.jpg', 'prompt' => 'Cinematic night illustration of an elegant museum gallery, an ornate empty gilt picture frame on a dark red wall lit by a single spotlight, a velvet rope in front, distant party lights through a doorway, art-heist noir mood, deep burgundy and gold palette, no people, no text, 4:3'],
 'intro' => [
  'On Saturday night the <b>Calder Art Museum</b> holds its winter fundraiser: champagne, a charity auction and two hundred guests in evening dress. At 22:40 the director leads a group of donors into Gallery 4 – and stops dead.',
  'The heavy gilt frame of <b>“Girl with a Lantern”</b> (Hendrik Vos, 1662) still hangs on the wall. The painting itself is gone. The alarm never sounded. The police think a guest slipped away from the party. The insurer has asked you to find out what really happened.',
 ],
 'mission' => [
  'Find out when the painting really left the wall.',
  'Find out how it left the building.',
  'Name the thief – and the reason.',
  'Back up your accusation with at least four document numbers.',
 ],
 'questions' => [
  'Was Gallery 4 really guarded all evening?',
  'What does the alarm actually watch – the painting or the frame?',
  'Whose alarm code was used, and where was that person?',
  'What left the building that evening, and how heavy was it?',
  'Who needed money – and who only wanted the painting the honest way?',
  'Which suspicious sights were innocent?',
 ],
 'suspects' => [
  ['id' => 'isabel-crane', 'name' => 'Isabel Crane', 'role' => 'Museum director'],
  ['id' => 'marcus-webb', 'name' => 'Marcus Webb', 'role' => 'Head of security'],
  ['id' => 'lena-hartmann', 'name' => 'Dr Lena Hartmann', 'role' => 'Paintings conservator'],
  ['id' => 'tom-okafor', 'name' => 'Tom Okafor', 'role' => 'Catering manager'],
  ['id' => 'sophie-lind', 'name' => 'Sophie Lind', 'role' => 'Collector and donor'],
  ['id' => 'ravi-mehta', 'name' => 'Ravi Mehta', 'role' => 'Night guard'],
 ],
 'packets' => [
  'START' => ['label' => 'Start folder', 'docs' => ['A01', 'A02', 'A03', 'A04', 'A05', 'A06']],
  'B' => ['label' => 'Envelope B', 'when' => 'you can say when the painting really left the wall', 'docs' => ['B01', 'B02', 'B03', 'B04', 'B05', 'B06']],
  'C' => ['label' => 'Envelope C', 'when' => 'you can say how the painting left the building', 'docs' => ['C01', 'C02', 'C03', 'C04', 'C05', 'C06']],
 ],
 'docs' => [
  'A01' => ['kind' => 'report', 'title' => 'Incident report', 'meta' => 'Duty manager · Saturday night', 'body' => '
    <dl class="rows"><dt>22:40</dt><dd>Director Isabel Crane finds the frame in Gallery 4 <b>empty</b></dd><dt>Frame</dt><dd>Still on the wall, screws untouched</dd><dt>Canvas</dt><dd>Cut neatly from its stretcher – <b>gone</b></dd><dt>22:41</dt><dd>Alarm raised by hand; all exits closed</dd></dl>
    <p class="note">Guests searched as they left. Nothing found.</p>'],
  'A02' => ['kind' => 'log', 'title' => 'Alarm system printout', 'meta' => 'Gallery 4 · frame sensor G4-07', 'body' => '
    ' . gn_t([['17:40', 'G4-07 ARMED'], ['17:58', 'G4-07 MAINTENANCE MODE – code 4471'], ['18:20', 'G4-07 ARMED – code 4471'], ['22:41', 'Building alarm – manual']], ['Time', 'Event']) . '
    <p class="note">Frame sensors raise an alarm if a frame is lifted or tilted on the wall.</p>'],
  'A03' => ['kind' => 'calendar', 'title' => 'Fundraiser running order', 'meta' => 'Printed programme', 'body' => '
    <dl class="rows"><dt>17:30–18:00</dt><dd>Press preview, Gallery 4</dd><dt>19:00</dt><dd>Doors open – champagne in the Great Hall</dd><dt>21:00</dt><dd>Charity auction</dd><dt>22:30</dt><dd>Director’s private tour for top donors</dd></dl>
    <p class="note">Gallery 4 is roped off to guests during the party.</p>'],
  'A04' => ['kind' => 'photo', 'title' => 'Event photographer’s contact sheet', 'meta' => 'Three frames', 'img' => ['file' => 'the-empty-frame/preview.jpg', 'caption' => 'Press preview, 17:50', 'prompt' => 'Press preview in an elegant museum gallery, a small Dutch golden age painting of a girl holding a lantern in a large gilt frame on a dark red wall, a few journalists with cameras, warm spotlights, documentary photo style, no readable text, 4:3'], 'body' => '
    <p><b>17:50</b> – Press preview: “Girl with a Lantern” on the wall in Gallery 4.</p>
    <p><b>19:15</b> – Gallery 4 doorway, velvet rope across it, lights dimmed.</p>
    <p><b>22:30</b> – Tom Okafor crossing the service corridor with a stack of large flat boxes.</p>
    {{IMG}}'],
  'A05' => ['kind' => 'list', 'title' => 'Night guard’s round sheet', 'meta' => 'Ravi Mehta', 'body' => '
    ' . gn_t([['20:00', 'Gallery 4', 'Checked from the rope – OK'], ['21:00', 'Gallery 4', 'Checked from the rope – OK'], ['22:00', 'Gallery 4', 'Checked from the rope – OK']], ['Time', 'Room', 'Note']) . '
    <p class="note">During events, Gallery 4 lighting is turned down to 10 %.</p>'],
  'A06' => ['kind' => 'report', 'title' => 'Alarm code policy', 'meta' => 'Security handbook, extract', 'body' => '
    <p>Every member of staff who may switch sensors to maintenance mode has a <b>personal four-digit code</b>. Codes must never be written down or shared.</p>
    <dl class="rows"><dt>2210</dt><dd>I. Crane</dd><dt>4471</dt><dd>M. Webb</dd><dt>3906</dt><dd>R. Mehta</dd></dl>
    <p class="note">The conservator has no code; when she works on a hung painting, security switches the sensor for her.</p>'],
  'B01' => ['kind' => 'interview', 'title' => 'Head of security’s statement', 'meta' => 'Marcus Webb', 'body' => '
    <p>“I didn’t touch that sensor on Saturday. I left the building at half past five and went straight to the gym before the party. If my code was used, someone has it.”</p>
    ' . gn_t([['17:41', 'Front gate out', 'M. Webb'], ['17:52', 'Gym entry, Mill Street', 'M. Webb'], ['18:58', 'Gym exit', 'M. Webb'], ['19:10', 'Front gate in', 'M. Webb']], ['Time', 'Place', 'Card']) . ''],
  'B02' => ['kind' => 'photo', 'title' => 'Police photo – conservation studio', 'meta' => 'Taken Sunday morning', 'img' => ['file' => 'the-empty-frame/studio.jpg', 'caption' => 'The conservator’s workbench', 'prompt' => 'A paintings conservation studio workbench in a museum, magnifying lamp, brushes and solvents, an empty wooden easel, a small yellow sticky note stuck to the lamp, daylight from a high window, documentary photo, no readable text, 4:3'], 'body' => '
    <p>On the magnifying lamp above the conservator’s bench, a yellow sticky note:</p>
    <p class="handwriting">G4 alarm – 4471 (M.W. – don’t lose!)</p>
    {{IMG}}'],
  'B03' => ['kind' => 'log', 'title' => 'Studio door log', 'meta' => 'Conservation studio, 1st floor', 'body' => '
    ' . gn_t([['17:55', 'Door opened', 'L. Hartmann'], ['18:24', 'Door opened', 'L. Hartmann'], ['19:28', 'Door opened', 'L. Hartmann'], ['19:31', 'Door opened', 'Courier (visitor badge)']], ['Time', 'Event', 'Card']) . '
    <p class="note">The studio is on the same corridor as the back door of Gallery 4.</p>'],
  'B04' => ['kind' => 'interview', 'title' => 'The conservator’s statement', 'meta' => 'Dr Lena Hartmann', 'body' => '
    <p>“I was in my studio before the party, packing frame samples for our restorer in Antwerp. I never went into Gallery 4 – the painting was perfectly safe on the wall when I went down to the party at half past seven.”</p>'],
  'B05' => ['kind' => 'interview', 'title' => 'The night guard', 'meta' => 'Ravi Mehta', 'body' => '
    <p>“Gallery 4 was roped off and nearly dark. I checked from the rope every hour, like always. You can see the gold frame shining from there – I never thought to look closer.”</p>
    <p class="note">Ravi spent the party at the Great Hall doors; the doorman confirms it.</p>'],
  'B06' => ['kind' => 'report', 'title' => 'Catering delivery note', 'meta' => 'Tom Okafor', 'body' => '
    <p>Tom’s flat boxes at 22:30 held <b>48 empty canapé trays</b>, carried out to the van for collection. The van was searched at 22:50 and the trays counted.</p>
    <p class="note">Each box measured 60 × 40 cm. The painting measures 46 × 38 cm – but the boxes were searched and empty.</p>'],
  'C01' => ['kind' => 'log', 'title' => 'Courier manifest', 'meta' => 'Speedline Fine Art Transport', 'body' => '
    ' . gn_t([['19:31', 'Collection, conservation studio', 'Crate CS-12, “frame samples”', '18 kg'], ['—', 'Signed for by', 'L. Hartmann', ''], ['20:40', 'Address changed by phone', 'From: Antwerp restorer → To: 14 Quay Lane', '']], ['Time', 'Event', 'Item', 'Weight']) . ''],
  'C02' => ['kind' => 'list', 'title' => 'Earlier crates from the studio', 'meta' => 'Courier account history', 'body' => '
    ' . gn_t([['August', 'CS-09, frame samples', '3 kg'], ['September', 'CS-10, frame samples', '2 kg'], ['October', 'CS-11, frame samples', '4 kg']], ['Month', 'Crate', 'Weight']) . '
    <p class="note">Museum catalogue: “Girl with a Lantern”, oil on canvas, 46 × 38 cm. Crate CS-12 and its packing weigh about 4 kg empty; the canvas, rolled with padding, about 14 kg with its protective board.</p>'],
  'C03' => ['kind' => 'interview', 'title' => 'The Antwerp restorer', 'meta' => 'Phone note by the insurer', 'body' => '
    <p>“Frame samples? We never asked for any. We haven’t worked with the Calder since spring. No crate has arrived here.”</p>'],
  'C04' => ['kind' => 'messages', 'title' => 'Messages on the conservator’s phone', 'meta' => 'Recovered by the police', 'body' => '
    <div class="chat"><p class="msg in"><span>Fri 21:12 · “Q”</span>Our friend is impatient. Saturday as agreed?</p><p class="msg out"><span>Fri 21:15 · Lena</span>She travels Saturday evening, before the party. Quay Lane by ten. Then we are square.</p><p class="msg in"><span>Sat 22:05 · “Q”</span>Arrived. Beautiful. Debt cleared.</p></div>'],
  'C05' => ['kind' => 'audit', 'title' => 'Insurance file', 'meta' => 'Isabel Crane', 'body' => '
    <p>The museum raised the painting’s insurance from £2 m to £3.5 m last month. Board minutes: the increase was <b>demanded by the insurer</b> after a new valuation, and approved by the full board.</p>
    <p class="note">Isabel spent the whole party with donors in the Great Hall and ran the auction from 21:00.</p>'],
  'C06' => ['kind' => 'report', 'title' => 'The collector’s letter', 'meta' => 'Sophie Lind to the museum, two weeks earlier', 'body' => '
    <p class="quote">“If the museum is ever forced to sell ‘Girl with a Lantern’, I would pay a fair price and lend it straight back for public display.”</p>
    <p class="note">Sophie stood beside the auctioneer all evening, bidding for the charity lots – three photographs show her there between 21:00 and 22:30.</p>'],
 ],
 'checkpoints' => [
  'A' => ['title' => 'The time', 'prompt' => 'When did the painting really leave the wall – during the party, or before?',
          'gate' => ['q' => 'When did the painting leave Gallery 4?', 'choices' => ['During the party, around 22:30', 'Before the party, around 18:00', 'It was never there that day'], 'answer' => 1,
                     'ok' => 'The frame sensor was switched off from 17:58 to 18:20, and after that nobody looked closer than the rope. Open envelope B.'],
          'hints' => ['The alarm watches the frame. What happened to the alarm before the party?', 'A02: maintenance mode 17:58–18:20. A04 and A05: after 17:50, nobody saw the painting up close.']],
  'B' => ['title' => 'The route', 'prompt' => 'How did the painting leave the building, when every guest was searched?',
          'gate' => ['q' => 'How did the painting get out?', 'choices' => ['In the caterer’s flat boxes', 'In a courier crate from the conservation studio', 'Under a guest’s coat'], 'answer' => 1,
                     'ok' => 'Code 4471 was on a note in the conservation studio, and something left that studio by courier at 19:31. Open envelope C.'],
          'hints' => ['Who could have used Marcus’s code – and where was it written?', 'B02 shows where the code was kept; B03 shows who was in that room and who came to collect.']],
  'final' => ['title' => 'The accusation', 'prompt' => 'Who stole “Girl with a Lantern”, how – and why?',
          'hints' => ['Compare the weight of crate CS-12 with all the earlier crates.', 'C01, C02 and C03 show what was in the crate; C04 shows why.']],
 ],
 'accuse' => [
  'culprit_q' => 'Who stole the painting?',
  'wrong' => 'That’s not the person who took the painting.',
  'items' => ['when' => ['The time', 'When did the painting leave the wall?', 4], 'route' => ['The route', 'How did it leave the building?', 4], 'motive' => ['The motive', 'Why was it taken?', 3]],
 ],
 'choices' => [
  'when' => [
   'a' => 'During the director’s tour at 22:30.',
   'b' => 'Between 17:58 and 18:20, while the frame sensor was in maintenance mode.',
   'c' => 'During the charity auction at 21:00.',
   'd' => 'The night before the party.',
  ],
  'route' => [
   'a' => 'In Tom’s flat catering boxes.',
   'b' => 'Out through the roof, while the party was on.',
   'c' => 'Rolled up in courier crate CS-12, labelled “frame samples”, collected from the studio at 19:31.',
   'd' => 'Under a guest’s coat.',
  ],
  'motive' => [
   'a' => 'To claim the raised insurance money.',
   'b' => 'To pay off a debt to a buyer known as “Q”.',
   'c' => 'To make the museum sell the painting to a collector.',
   'd' => 'Revenge on the director.',
  ],
 ],
 'worksheet' => ['Who took the painting?', 'When did it leave the wall?', 'How did it leave the building?', 'Why?', 'Which details were red herrings?'],
 'solution_title' => 'What really happened at the Calder Art Museum',
];
