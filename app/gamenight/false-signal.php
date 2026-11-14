<?php
// Game Night case 004: False Signal. Server-side only. Translated and adapted from the Danish beta 'Falsk signal'.
return [
 'slug' => 'false-signal',
 'no' => '004',
 'title' => 'False Signal',
 'tagline' => 'Live on air, the donation code changed. Everyone blames a hacker.',
 'teaser' => 'During a nationwide charity concert, the donation QR code in the livestream suddenly points to a fake payment page. The crew blames an unknown hacker. The logs disagree.',
 'genre' => 'Fraud',
 'level' => 3,
 'minutes' => [90, 120],
 'players' => [2, 6],
 'revision' => '1.0',
 'caseref' => 'AUR-2026-0424',
 'stamp' => 'ON AIR',
 'envelope' => '#C7B8D6', 'flap' => '#A897BC',
 'cast' => true,
 'cover' => ['file' => 'false-signal/cover.jpg', 'prompt' => 'Cinematic illustration of a big charity concert seen from the back of a dark arena, a huge LED screen above the stage showing an abstract glowing square code pattern with a subtle red glitch distortion across it, silhouettes of a crowd holding up phones, purple and electric-blue stage lights, tense thriller mood, no readable text, no logos, 4:3'],
 'intro' => [
  'On Friday 24 April 2026, the <b>Aurora Foundation</b> holds a nationwide charity concert, streamed live. On screen, a QR code invites viewers to donate.',
  'At 20:12 the QR code in the broadcast graphic changes. Viewers think they are giving to the foundation – but the new code leads to a <b>fake payment page</b>. At 20:27 the foundation notices; at 20:30 the graphic is taken off air. The bank has frozen the money, so nothing has been withdrawn.',
  'Everyone on the production blames an unknown hacker. The foundation asks you to find out what really happened.',
 ],
 'mission' => [
  'Find out who changed the donation link, with what access and when.',
  'Work out who is behind the fake payment page – and whether that is the same person.',
  'Explain why it was done.',
  'Back up your accusation with at least four document numbers.',
 ],
 'questions' => [
  'Was the broadcast hacked – or was something changed through the normal system?',
  'What is the difference between an account name and the machine that used it?',
  'Who could physically reach the devices that made the change?',
  'Whose statement doesn’t match the door log?',
  'Who owns the fake payment page?',
  'Who did what, when – and why?',
 ],
 'suspects' => [
  ['id' => 'ida-kragh', 'name' => 'Ida Kragh', 'role' => 'Broadcast producer'],
  ['id' => 'mikkel-roed', 'name' => 'Mikkel Roed', 'role' => 'Head of finance and donations'],
  ['id' => 'theo-brandt', 'name' => 'Theo Brandt', 'role' => 'External livestream technician'],
  ['id' => 'sofie-lund', 'name' => 'Sofie Lund', 'role' => 'Head of communications'],
  ['id' => 'malik-osman', 'name' => 'Malik Osman', 'role' => 'Stage manager'],
  ['id' => 'eva-falk', 'name' => 'Eva Falk', 'role' => 'Former volunteer with an old grudge against the foundation'],
 ],
 'packets' => [
  'START' => ['label' => 'Start folder', 'docs' => ['A01', 'A02', 'A03', 'A04', 'A05', 'A06']],
  'B' => ['label' => 'Envelope B', 'when' => 'you can say what was actually changed in the broadcast', 'docs' => ['B01', 'B02', 'B03', 'B04', 'B05', 'B06']],
  'C' => ['label' => 'Envelope C', 'when' => 'you can name the device that created the fake graphic', 'docs' => ['C01', 'C02', 'C03', 'C04', 'C05', 'C06']],
 ],
 'docs' => [
  'A01' => ['kind' => 'report', 'title' => 'Incident report', 'meta' => 'Aurora Foundation · Friday 24 April 2026',
    'img' => ['file' => 'false-signal/stream-still.jpg', 'caption' => 'Screenshot of the livestream, 20:13', 'prompt' => 'Screenshot-style still of a concert livestream: a singer on a colourful stage, and in the lower right corner a neat donation overlay box with a square QR-code-like pattern and a heart icon, slight broadcast compression artefacts, no readable text, no logos'],
    'body' => '
    {{IMG}}
    <dl class="rows"><dt>20:12</dt><dd>The donation QR code in the broadcast graphic changes</dd><dt>20:27</dt><dd>The foundation notices that donations look wrong</dd><dt>20:30</dt><dd>The graphic is taken off air</dd></dl>
    <p class="note">The foundation’s official website and bank account were <b>not</b> compromised.</p>'],
  'A02' => ['kind' => 'report', 'title' => 'Approved donation text', 'meta' => 'Foundation sign-off, 3 April', 'body' => '
    <dl class="rows"><dt>Approved QR target</dt><dd>https://give.aurora.example/donate</dd><dt>Graphic template</dt><dd>DONATE-V4</dd><dt>Fake QR target</dt><dd><b>https://aurora-help.example/pay</b></dd></dl>
    <p class="note">Both addresses are fictional for this game.</p>'],
  'A03' => ['kind' => 'interview', 'title' => 'Note from the video technician', 'meta' => 'Theo Brandt · written 20:40', 'body' => '
    <p>“The video feed kept running without a single drop-out. All I saw was the donation graphic switching. That points to a normal graphics update, not someone hacking the cameras.”</p>'],
  'A04' => ['kind' => 'log', 'title' => 'Extract from the stream log', 'meta' => 'Broadcast playout', 'body' => '
    ' . gn_t([['20:09', 'DONATE overlay', 'V4'], ['20:12', 'DONATE overlay', '<b>V5</b>'], ['20:30', 'DONATE overlay', 'OFF']], ['Time', 'Element', 'Version']) . '
    <p class="note">The camera feeds show no gaps in the same period.</p>'],
  'A05' => ['kind' => 'report', 'title' => 'Foundation donation overview', 'body' => '
    <p>The official donation system received normal donations before 20:12. Between 20:12 and 20:30 the flow of new payments fell sharply.</p>
    <p class="note">The foundation has recorded no change to its own payment settings.</p>'],
  'A06' => ['kind' => 'photo', 'title' => 'Copy of the fake page', 'meta' => 'Saved by the foundation at 20:28', 'body' => '
    <p>The fake page uses the foundation’s name and colours. But on the payment receipts the recipient is called <b>Event Services Ltd</b>.</p>
    <p class="note">The payments sit in a temporary account that the bank has frozen.</p>'],
  'B01' => ['kind' => 'log', 'title' => 'Graphics system change history', 'body' => '
    ' . gn_t([['19:41', 'V5 created', 'graphics-service', 'STUDIO-02'], ['19:48', 'V5 approved', 'graphics-service', 'STUDIO-02'], ['20:12', 'V5 sent live', 'graphics-service', 'AUTO-PLAY']], ['Time', 'Action', 'Account', 'Device']) . '
    <p class="note">AUTO-PLAY is the player: it sends out an approved version at a scheduled time. It cannot create or edit versions.</p>'],
  'B02' => ['kind' => 'report', 'title' => 'Access to the graphics system', 'body' => '
    <p>The account <b>graphics-service</b> is a shared technical service account. Only the workstation <b>STUDIO-02</b> may create new versions. Auto-play automatically sends out an approved version at its planned time.</p>
    <p>So the account name does <b>not</b> identify a physical person.</p>
    <p class="note">Communications (Sofie), stage crew (Malik) and all volunteer accounts – including Eva Falk’s, closed in March – have no access to the graphics system or to STUDIO-02.</p>'],
  'B03' => ['kind' => 'log', 'title' => 'Remote access log', 'meta' => 'STUDIO-02', 'body' => '
    ' . gn_t([['19:36', 'Remote session opened from tablet <b>PROD-TAB7</b>'], ['19:50', 'Remote session closed']], ['Time', 'Event']) . '
    <p class="note">No other remote sessions were recorded between 19:00 and 20:30. The production network only accepts registered tablets.</p>'],
  'B04' => ['kind' => 'list', 'title' => 'Equipment register', 'meta' => 'Production equipment, 24 April',
    'img' => ['file' => 'false-signal/prod-tab7.jpg', 'caption' => 'PROD-TAB7 on the production desk', 'prompt' => 'Photo of a rugged black production tablet with an equipment label sticker (unreadable) lying on a cluttered broadcast production desk next to a headset, cue sheets and a mixing console, dim control-room lighting with coloured monitor glow, no readable text'],
    'body' => '
    {{IMG}}
    ' . gn_t([['PROD-TAB7', 'Ida Kragh', '17:00', '22:02']], ['Tablet', 'Registered to', 'Handed out', 'Returned']) . '
    <p class="note">Ida may lend the tablet to others, but the equipment book records no hand-over.</p>'],
  'B05' => ['kind' => 'log', 'title' => 'Guard’s access log', 'meta' => 'All card swipes, 19:00–20:30', 'body' => '
    ' . gn_t([['19:31', 'IDA-11', 'Production room – in'], ['19:35', 'IDA-11', 'Production room – out'], ['19:52', 'IDA-11', 'Production room – in'], ['20:04', 'THEO-19', 'Tech room – in']], ['Time', 'Card', 'Door']) . '
    <p class="note">The guard checked the production room at 19:00: it was empty. These are <b>all</b> the card swipes between 19:00 and 20:30. Every door logs both in and out.</p>'],
  'B06' => ['kind' => 'interview', 'title' => 'Interviews: Ida and Theo', 'meta' => 'Taken at 21:15', 'body' => '
    <p><b>Ida Kragh:</b> “I was out by the stage for the whole soundcheck. I only popped into the production room before 19:35 and came back after 19:50. The tablet was lying on the table in there the whole time.”</p>
    <p><b>Theo Brandt:</b> “I could see the overlay on my monitors, but I don’t have STUDIO-02 access. I was setting up cameras until I went into the tech room.”</p>'],
  'C01' => ['kind' => 'log', 'title' => 'Graphics task list', 'meta' => 'Shared production to-do list', 'body' => '
    ' . gn_t([['18:55', 'Ida creates task: ‘Donation overlay on cue 20:12. Verify V4 before show.’'], ['19:51', 'Task marked <b>completed</b> – from <b>PROD-TAB7</b>']], ['Time', 'Entry']) . ''],
  'C02' => ['kind' => 'report', 'title' => 'Version V5 – metadata', 'body' => '
    <p>V5 was cloned from V4, but the QR target was changed to <b>aurora-help.example/pay</b>. Logo, colours and body text are unchanged.</p>
    <p class="note">The change was made by hand, from the active remote session, at 19:41.</p>'],
  'C03' => ['kind' => 'audit', 'title' => 'Account check at the bank', 'body' => '
    <dl class="rows"><dt>Company</dt><dd>Event Services Ltd</dd><dt>Registered</dt><dd>Six weeks earlier</dd><dt>Representative</dt><dd><b>Mikkel Roed</b></dd></dl>
    <p>The bank says only Mikkel had control of the account. The payments were held automatically before anyone could withdraw them.</p>'],
  'C04' => ['kind' => 'messages', 'title' => 'Draft in Mikkel’s mailbox', 'meta' => 'Unsent draft, 18:20', 'body' => '
    <p class="quote">“Ida, we can let the graphics team test the new payment page after the concert. No live changes without written approval.”</p>
    <p class="note">No later approval has been found.</p>'],
  'C05' => ['kind' => 'messages', 'title' => 'Chat between Ida and Mikkel', 'body' => '
    <div class="chat"><p class="msg out"><span>18:33 · Ida → Mikkel</span>Why does your company have a page with the foundation’s name on it?</p>
    <p class="msg in"><span>18:37 · Mikkel → Ida</span>It’s a test proposal. Don’t touch it. I’ll take it down tomorrow.</p>
    <p class="msg out"><span>19:55 · Ida → Mikkel</span>I’ve made sure we’ll get proof tonight.</p></div>
    <p class="note">Mikkel did not reply.</p>'],
  'C06' => ['kind' => 'lab', 'title' => 'Forensic note on the tablet', 'meta' => 'PROD-TAB7, examined 25 April', 'body' => '
    <p>On PROD-TAB7 there is an unsent note, created at <b>19:44</b>:</p>
    <p class="handwriting">Show the fake page live and get Mikkel exposed. Take a screenshot. Remove V5 straight after.</p>
    <p class="note">No logs show that another user took over the tablet.</p>'],
 ],
 'checkpoints' => [
  'A' => ['title' => 'Hack or update?', 'prompt' => 'Was the broadcast hacked – or was something changed through the normal system?',
          'gate' => ['q' => 'What was actually manipulated in the broadcast?', 'choices' => ['The foundation’s bank account', 'The target address of the QR code in the donation graphic', 'The cameras’ video feed'], 'answer' => 1,
                     'ok' => 'The graphic switched from V4 to V5 – the cameras and the foundation’s own systems were never touched. Open envelope B.'],
          'hints' => ['Decide whether the TV picture or the foundation’s payment system was actually changed.', 'Compare A01, A03 and A04: the video ran on, the overlay version changed.']],
  'B' => ['title' => 'Account and machine', 'prompt' => 'Which account – and which machine – changed the graphic?',
          'gate' => ['q' => 'Which device started the change to V5?', 'choices' => ['Ida’s tablet PROD-TAB7, through a remote session on STUDIO-02', 'Theo’s laptop in the tech room', 'The foundation’s own server'], 'answer' => 0,
                     'ok' => 'Auto-play only played what had been approved. The edit was made in the remote session from PROD-TAB7. Open envelope C.'],
          'hints' => ['Tell the difference between an account name and the machine that actually sent the update.', 'See B01 and B03. Auto-play is only the player – who was connected to STUDIO-02 at 19:41?']],
  'final' => ['title' => 'The accusation', 'prompt' => 'Who put the fake QR code on air, who owns the fake page – and why?',
          'hints' => ['Combine door cards, the remote session and the notes – one log is not enough. Where was the tablet at 19:51?', 'C03 explains the account; C01 and C06 explain the live change.']],
 ],
 'accuse' => [
  'culprit_q' => 'Who put the fake QR code on air?',
  'wrong' => 'That’s not the person who sent the fake graphic live.',
  'items' => ['access' => ['The access', 'How was version V5 created?', 4], 'owner' => ['The fake page', 'Who set up the fake payment page and its account?', 4], 'motive' => ['The motive', 'Why did the culprit put it on air?', 3]],
 ],
 'choices' => [
  'access' => [
   'a' => 'Theo hacked the camera feed from the tech room.',
   'b' => 'From Ida’s tablet PROD-TAB7, through a remote session on STUDIO-02.',
   'c' => 'Someone broke into the foundation’s payment server.',
   'd' => 'Mikkel logged in to the shared graphics-service account from his office.',
  ],
  'owner' => [
   'a' => 'Ida Kragh.',
   'b' => 'Theo Brandt.',
   'c' => 'Mikkel Roed.',
   'd' => 'Eva Falk.',
  ],
  'motive' => [
   'a' => 'To pocket the donations.',
   'b' => 'To expose Mikkel’s suspicious page live and get proof – a reckless way to do it.',
   'c' => 'It happened by accident during a test.',
   'd' => 'Revenge on the foundation for an old dispute.',
  ],
 ],
 'worksheet' => ['What was actually changed in the broadcast?', 'Which device and access made the change?', 'Who put the fake code on air?', 'Who set up the fake page and account?', 'Why was it done?'],
 'solution_title' => 'What really happened on the night of the concert',
];
