<?php
// Game Night case 009: The Last Broadcast. Server-side only. Translated and adapted from the Danish beta 'Den sidste udsendelse'.
return [
 'slug' => 'the-last-broadcast',
 'no' => '009',
 'title' => 'The Last Broadcast',
 'tagline' => 'She vanished before midnight. Her voice went on air at 00:17.',
 'teaser' => 'A radio host disappears after a hard-hitting show about a private foundation. At 00:17 her voice comes over the air: “If I don’t come back, follow the money.”',
 'genre' => 'Disappearance',
 'level' => 3,
 'minutes' => [90, 140],
 'players' => [2, 6],
 'revision' => '1.0',
 'caseref' => 'CPH-2026-0520',
 'stamp' => 'ON AIR',
 'envelope' => '#BFC9B4', 'flap' => '#A2AF95',
 'cast' => true,
 'cover' => ['file' => 'the-last-broadcast/cover.jpg', 'prompt' => 'Cinematic illustration of an empty late-night radio studio, a vintage broadcast microphone on a boom arm in the foreground, a glowing red on-air lamp with no lettering, mixing desk lights blinking, a half-empty coffee cup and scattered papers, rain on a dark window with city lights beyond, deep red and teal palette, suspenseful noir mood, no people, no readable text, 4:3'],
 'intro' => [
  'On the night of Wednesday 20 May 2026, radio host <b>Vera Skov</b> leaves the station after a controversial show about a private charitable foundation. She never turns up for her morning shift.',
  'At <b>00:17</b> the station broadcasts a short message in her voice: <i>“If I don’t come back, follow the money. Someone has changed the archive.”</i> Her phone has been dead since 23:16. The police fear someone is holding her.',
  'But the sound file, the playout log and a handful of receipts tell a more tangled story. Two things are missing here: Vera, and the truth she was chasing.',
 ],
 'mission' => [
  'Find out how Vera could be heard on air at 00:17.',
  'Find out where Vera went – and whether she was taken.',
  'Find out what was being covered up, and who is responsible.',
  'Back up your conclusion with at least four document numbers.',
 ],
 'questions' => [
  'Does a voice on the radio prove where the speaker is at that moment?',
  'Who was in the building at 00:17?',
  'What – or who – is “N.”?',
  'What does the code N-730 mean across the documents?',
  'Why would two versions of the same annual report differ?',
  'Who lied, and what were they protecting?',
 ],
 'suspects' => [
  ['id' => 'vera-skov', 'name' => 'Vera Skov', 'role' => 'Investigative journalist and radio host'],
  ['id' => 'anton-vej', 'name' => 'Anton Vej', 'role' => 'Head of programmes, worried about the station’s future'],
  ['id' => 'selma-kruse', 'name' => 'Selma Kruse', 'role' => 'Sound engineer with access to the playout system'],
  ['id' => 'kasper-berg', 'name' => 'Kasper Berg', 'role' => 'Director of the foundation Vera was investigating'],
  ['id' => 'nora-dahl', 'name' => 'Nora Dahl', 'role' => 'Vera’s colleague and close friend'],
  ['id' => 'lukas-engel', 'name' => 'Lukas Engel', 'role' => 'Station temp who saw Vera leave'],
 ],
 'packets' => [
  'START' => ['label' => 'Start folder', 'docs' => ['S-01', 'S-02', 'S-03', 'S-04', 'S-05', 'S-06', 'S-07']],
  'B' => ['label' => 'Envelope B', 'when' => 'you can explain how Vera could be heard at 00:17 without anyone in the studio', 'docs' => ['B-01', 'B-02', 'B-03', 'B-04', 'B-05', 'B-06', 'B-07']],
  'C' => ['label' => 'Envelope C', 'when' => 'you can say what N-730 means', 'docs' => ['C-01', 'C-02', 'C-03', 'C-04', 'C-05', 'C-06', 'C-07']],
 ],
 'docs' => [
  'S-01' => ['kind' => 'report', 'title' => 'First police report', 'meta' => 'Thursday 21 May, 09:10', 'body' => '
    <dl class="rows"><dt>Missing</dt><dd>Vera Skov, 41, radio host</dd><dt>Last seen</dt><dd>20 May, 23:11 – leaving the station by the main door</dd><dt>Witness</dt><dd>Station temp Lukas Engel saw her leave alone, carrying a small suitcase</dd><dt>00:17</dt><dd>A recording of her voice is broadcast</dd></dl>
    <p class="note">No verified contact with Vera after 23:11. She did not turn up for her 07:00 shift.</p>'],
  'S-02' => ['kind' => 'report', 'title' => 'Transcript of the broadcast', 'meta' => 'Thursday 21 May, 00:17', 'body' => '
    <p class="quote">“If I don’t come back, follow the money. Someone has changed the archive.”</p>
    <p>In the background, the three notes of the station’s own break jingle can be heard.</p>'],
  'S-03' => ['kind' => 'log', 'title' => 'Door access log', 'meta' => 'Radio station, 20–21 May', 'body' => '
    ' . gn_t([['23:11', 'Vera Skov', 'Out – main door'], ['23:29', 'Selma Kruse', 'In – side door'], ['23:58', 'Selma Kruse', 'Out – side door'], ['00:17', '—', 'No access recorded']], ['Time', 'Card', 'Door']) . '
    <p class="note">The station’s playout system can run scheduled items with nobody in the building.</p>'],
  'S-04' => ['kind' => 'messages', 'title' => 'Email from the head of programmes', 'meta' => 'Anton Vej → Vera Skov, 19 May', 'body' => '
    <p class="quote">Vera, you can’t accuse the foundation without documents. We could lose our sponsorship. Careful wording is not censorship. – Anton</p>'],
  'S-05' => ['kind' => 'calendar', 'title' => 'Vera’s calendar', 'meta' => 'Latest entries', 'body' => '
    <p class="cal-day">Thursday 21 May</p>
    <table class="cal"><tr><td>07:00</td><td>Morning shift (studio 1)</td></tr><tr><td>07:30</td><td><b>Meeting N.</b></td></tr></table>
    <p class="note">‘N.’ could be her colleague Nora – but it could also be a place or someone else.</p>'],
  'S-06' => ['kind' => 'log', 'title' => 'Phone records', 'meta' => 'Vera’s mobile', 'body' => '
    ' . gn_t([['23:12', 'Last contact with the network, at the station'], ['23:16', 'Phone goes offline']], ['Time', 'Event']) . '
    <p class="note">No calls from any unknown person. The phone has not been found.</p>'],
  'S-07' => ['kind' => 'note', 'title' => 'Letter from Kasper Berg', 'meta' => 'Director, Lindholm Foundation · 18 May', 'body' => '
    <p class="quote">Your programme on 13 May contained serious untruths about the Lindholm Foundation. I demand a correction on air. Our annual report is public and speaks for itself. – Kasper Berg</p>
    <p class="note">The letter is sharp, but contains no concrete threat.</p>'],
  'B-01' => ['kind' => 'log', 'title' => 'Playout system log', 'meta' => 'Scheduling and playback', 'body' => '
    ' . gn_t([['20 May · 22:42', 'File <b>VERAS_NOTE_FINAL.wav</b> scheduled for 21 May, 00:17 · user <b>VSKOV</b>'], ['20 May · 23:29–23:58', 'Night playlist loaded · user SKRUSE · no changes to scheduled items'], ['21 May · 00:17', 'VERAS_NOTE_FINAL.wav played automatically · no manual start']], ['Time', 'Event']) . ''],
  'B-02' => ['kind' => 'lab', 'title' => 'Sound file metadata', 'meta' => 'VERAS_NOTE_FINAL.wav', 'body' => '
    <dl class="rows"><dt>Recorded</dt><dd>Edit suite 2, 20 May, 18:14</dd><dt>Last edited</dt><dd>20 May, 22:39</dd><dt>Profile</dt><dd>VSKOV</dd></dl>
    <p class="note">The background jingle is the station’s standard sound. It is no clue to where Vera was at midnight – it was mixed in during editing.</p>'],
  'B-03' => ['kind' => 'report', 'title' => 'The editing project', 'meta' => 'Edit suite 2', 'body' => '
    <p>The session holds two versions, both made on Vera’s own profile:</p>
    <ul class="plain"><li><b>NOTE_DRAFT:</b> “If I go quiet…”</li><li><b>NOTE_FINAL:</b> “If I don’t come back…”</li></ul>'],
  'B-04' => ['kind' => 'report', 'title' => 'Taxi receipt', 'meta' => '20 May, 23:24', 'body' => '
    <p>Cash fare from the station’s back street to the <b>ferry quay</b>.</p>
    <p class="note">The driver remembers a passenger in a dark jacket with a small suitcase, but can’t confirm who it was.</p>'],
  'B-05' => ['kind' => 'report', 'title' => 'Ferry terminal receipt', 'meta' => 'Overnight ferry to Osterby', 'body' => '
    <dl class="rows"><dt>Ticket bought</dt><dd>20 May, 23:52</dd><dt>Booking code</dt><dd><b>N-730</b></dd><dt>Departure</dt><dd>00:35 (arrives Osterby 07:00)</dd><dt>Name</dt><dd>V. S.</dd><dt>Payment</dt><dd>Gift card, registered the day before</dd></dl>'],
  'B-06' => ['kind' => 'calendar', 'title' => 'Nora’s calendar printout', 'meta' => 'Nora Dahl', 'body' => '
    <table class="cal"><tr><td>21 May · 07:30</td><td>“<b>N-730</b>, bring the originals”</td></tr></table>
    <p>An earlier event called “Vera / meeting” has been deleted.</p>
    <p class="note">Nora says she only deleted it so nobody else would see the appointment.</p>'],
  'B-07' => ['kind' => 'audit', 'title' => 'The foundation’s annual report – two versions', 'meta' => 'Lindholm Foundation, annual report 2025', 'body' => '
    ' . gn_t([['Version on the website today', '1.4 million kr. – “advisory services”'], ['Older archived copy (same date)', '1.4 million kr. – “payment to Brask Holding ApS (related party)”']], ['Source', 'Line in the accounts']) . '
    <p class="note">Same date, same amount – different text.</p>'],
  'C-01' => ['kind' => 'audit', 'title' => 'The auditor’s paper copy', 'meta' => 'Original auditor’s list', 'body' => '
    <p>The list shows <b>1.4 million kr.</b> transferred to Brask Holding ApS, a company owned by a member of the foundation’s board.</p>
    <p class="note">This is a possible conflict of interest – not, on its own, final proof of a crime.</p>'],
  'C-02' => ['kind' => 'log', 'title' => 'Archive server change log', 'meta' => 'Lindholm Foundation website', 'body' => '
    ' . gn_t([['19 May · 15:32', 'Web version of annual report 2025 replaced', 'User: Brightline Communications (external)', 'Approved by: <b>Kasper Berg</b>']], ['Time', 'Change', 'User', 'Approval']) . '
    <p class="note">The change removed the words “Brask Holding ApS (related party)”. It happened six days after Vera’s first programme and one day before her last.</p>'],
  'C-03' => ['kind' => 'messages', 'title' => 'Message from Vera to Nora', 'meta' => '20 May, 19:04', 'body' => '
    <div class="chat"><p class="msg out"><span>19:04 · Vera → Nora</span>I want to get away from the phones until the papers are with an independent editor. I’ll leave a trail so you know what to look into. Nobody must think I’ve been kidnapped.</p></div>'],
  'C-04' => ['kind' => 'messages', 'title' => 'Nora’s reply', 'meta' => '20 May, 19:12', 'body' => '
    <div class="chat"><p class="msg in"><span>19:12 · Nora → Vera</span>Fine. But don’t make it dramatic. I’ll take the first flight and meet you at 07:30 at the terminal in Osterby – booking N-730. I’ll bring the originals.</p></div>'],
  'C-05' => ['kind' => 'photo', 'img' => ['file' => 'the-last-broadcast/kiosk.jpg', 'caption' => 'Receipt photo, ferry terminal kiosk, 00:21', 'prompt' => 'Grainy night-time photo inside a small ferry terminal kiosk under harsh fluorescent light, a woman in a dark jacket with a small wheeled suitcase standing at the counter, her face turned away and half hidden by her collar, coffee machine and rack of snacks, a ferry visible through the window, documentary snapshot style, no readable text'], 'title' => 'Photo from the ferry kiosk', 'meta' => '21 May, 00:21', 'body' => '
    {{IMG}}
    <p>A receipt photo shows a woman in a dark jacket with a small suitcase. Her face is partly hidden. The receipt shows booking code <b>N-730</b>.</p>
    <p class="note">A later statement from Nora confirms that the traveller was Vera.</p>'],
  'C-06' => ['kind' => 'note', 'title' => 'Vera’s written statement', 'meta' => 'Sent through her lawyer, 22 May', 'body' => '
    <p class="quote">I travelled of my own free will to document a story without pressure. I planned the late broadcast myself, but the wording was careless and caused needless fear. Nobody kidnapped me. I am safe.</p>'],
  'C-07' => ['kind' => 'interview', 'title' => 'Statements: Anton and Selma', 'meta' => '21 May', 'body' => '
    <p><b>Selma Kruse:</b> “I came in at 23:29 to load the night playlist, like every Wednesday. Vera’s file was already scheduled – I didn’t make it or touch it.”</p>
    <p><b>Anton Vej:</b> “I wanted to avoid a legal fight, that’s true. But I have no access to put anything on the playout schedule, and I was at home all evening.”</p>'],
 ],
 'checkpoints' => [
  'A' => ['title' => 'The voice in the dark', 'prompt' => 'Vera left at 23:11. Nobody was in the building at 00:17. How could she be heard on air?',
          'gate' => ['q' => 'What is the most likely explanation for the broadcast at 00:17?', 'choices' => ['Vera was secretly in the studio at 00:17', 'The message was recorded earlier and played automatically', 'Someone broke in and played a stolen recording'], 'answer' => 1,
                     'ok' => 'No door opened at 00:17, and the playout system runs scheduled items on its own. Open envelope B.'],
          'hints' => ['A voice on the radio doesn’t prove where the speaker is at that moment.', 'Look at the door log in S-03 and its note.']],
  'B' => ['title' => 'The playback', 'prompt' => 'Who scheduled the message, and where did Vera go after 23:11?',
          'gate' => ['q' => 'What links Vera to the code N-730?', 'choices' => ['A car number plate seen near the station', 'Her ferry booking and her 07:30 meeting with Nora', 'A bank account at the foundation'], 'answer' => 1,
                     'ok' => 'N-730 is the ferry booking – and “N.” at 07:30 is Nora. Open envelope C.'],
          'hints' => ['Find what N-730 means across the documents.', 'Compare Vera’s calendar (S-05), the ferry receipt (B-05) and Nora’s calendar (B-06).']],
  'final' => ['title' => 'The accusation', 'prompt' => 'Vera wasn’t the only thing that went missing. Who covered up what – and how did Vera’s night really go?',
          'hints' => ['Compare the two versions of the same annual report.', 'Who approved the change on the archive server – and when?']],
 ],
 'accuse' => [
  'culprit_q' => 'Who is responsible for the cover-up Vera was chasing?',
  'wrong' => 'That person didn’t cover anything up.',
  'items' => ['voice' => ['The voice', 'How could Vera be heard at 00:17?', 4], 'where' => ['Vera’s night', 'What happened to Vera?', 4], 'what' => ['The cover-up', 'What was covered up?', 3]],
 ],
 'choices' => [
  'voice' => [
   'a' => 'She phoned in live from the ferry.',
   'b' => 'Selma played an old recording during her night shift.',
   'c' => 'Vera recorded it at 18:14 and scheduled it herself at 22:42 to play automatically.',
   'd' => 'A kidnapper forced her to record it and sent it to the station.',
  ],
  'where' => [
   'a' => 'She left of her own free will, took a taxi to the ferry quay and the 00:35 ferry on booking N-730 to meet Nora.',
   'b' => 'She was held captive near the station.',
   'c' => 'She was hiding in Nora’s flat in Copenhagen.',
   'd' => 'She was taken away by a man in the taxi.',
  ],
  'what' => [
   'a' => 'Vera’s own debts.',
   'b' => 'A secret sponsorship deal between the station and the foundation.',
   'c' => 'Selma deleting broadcast logs.',
   'd' => '1.4 million kroner paid to a holding company owned by a board member – hidden by changing the annual report online.',
  ],
 ],
 'worksheet' => ['How could Vera be heard at 00:17?', 'Where did Vera go – and why?', 'What does N-730 mean?', 'What was covered up?', 'Who is responsible for the cover-up?'],
 'solution_title' => 'What really happened on the night of the last broadcast',
];
