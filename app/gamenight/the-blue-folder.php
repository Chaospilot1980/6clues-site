<?php
// Game Night case 007: The Blue Folder. Server-side only. Translated and adapted from the Danish beta 'Den blaa mappe'.
return [
 'slug' => 'the-blue-folder',
 'no' => '007',
 'title' => 'The Blue Folder',
 'tagline' => 'A trade secret leaked. Everyone points at the same engineer.',
 'teaser' => 'A green-energy firm loses a huge contract when a rival unveils an almost identical design. The download log points straight at the chief engineer. Too straight?',
 'genre' => 'Espionage',
 'level' => 2,
 'minutes' => [100, 150],
 'players' => [2, 6],
 'revision' => '1.0',
 'caseref' => 'NV-441',
 'stamp' => 'LEAKED',
 'envelope' => '#9DB4D3', 'flap' => '#7E98BC',
 'cast' => true,
 'cover' => ['file' => 'the-blue-folder/cover.jpg', 'prompt' => 'Moody cinematic illustration of a blue cardboard document folder lying on a glass desk in a dark modern office at night, technical drawings of a battery cell spilling out, a laptop glow and city lights through a rainy window, cool blue palette with one warm desk lamp, corporate espionage thriller mood, no people, no readable text, 4:3'],
 'intro' => [
  'NordVektor, a green-energy company in Aarhus, loses a major contract when its rival <b>Helion</b> unveils an almost identical design on 17 September 2026 at 09:00.',
  'The security team quickly finds a download of the design from chief engineer <b>Nadia Lund</b>’s account the evening before. The case looks obvious. But Nadia insists that someone is planting evidence.',
  'Find the real leak – and decide who used the company’s trust as cover.',
 ],
 'mission' => [
  'Find out exactly which copy of the design leaked.',
  'Work out who passed it on, and how it reached the rival.',
  'Explain the download from Nadia’s account.',
  'Back up your accusation with at least four document numbers.',
 ],
 'questions' => [
  'What does a login really prove about who sat at the keyboard?',
  'Are the leaked file and the engineers’ file really the same?',
  'Who could reach each version of the design?',
  'Which trail does the paper copy leave?',
  'Who was paid – and by whom?',
  'Who did what, when – and why?',
 ],
 'suspects' => [
  ['id' => 'nadia-lund', 'name' => 'Nadia Lund', 'role' => 'Chief engineer – the first suspect'],
  ['id' => 'henrik-dahl', 'name' => 'Henrik Dahl', 'role' => 'Managing director'],
  ['id' => 'rikke-falck', 'name' => 'Rikke Falck', 'role' => 'Head of compliance'],
  ['id' => 'oskar-moller', 'name' => 'Oskar Moller', 'role' => 'IT administrator'],
  ['id' => 'lea-storm', 'name' => 'Lea Storm', 'role' => 'Sales director, ex-employee of the rival'],
  ['id' => 'emil-friis', 'name' => 'Emil Friis', 'role' => 'Intern on the launch material'],
 ],
 'packets' => [
  'START' => ['label' => 'Start folder', 'docs' => ['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07']],
  'B' => ['label' => 'Envelope B', 'when' => 'you can explain what the 21:13 login really shows', 'docs' => ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07']],
  'C' => ['label' => 'Envelope C', 'when' => 'you can say exactly which version of the design leaked', 'docs' => ['C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07']],
 ],
 'docs' => [
  'A01' => ['kind' => 'report', 'title' => 'Incident report NV-441', 'meta' => 'NordVektor security team', 'body' => '
    <dl class="rows"><dt>What</dt><dd>NordVektor’s design ‘VektorCell 4’ was shown by the rival Helion</dd><dt>When</dt><dd>17 September, 09:00</dd><dt>Download</dt><dd>16 September, <b>21:13</b>, user <b>NADIA.L</b></dd><dt>File fetched</dt><dd>VC4-42 from engineering/final</dd></dl>
    <p class="note">The rival’s file has the same diagrams as NordVektor’s internal design document.</p>'],
  'A02' => ['kind' => 'lab', 'title' => 'The file’s fingerprint', 'meta' => 'Checksum comparison', 'body' => '
    ' . gn_t([['Leaked PDF (shown by Helion)', '<b>8D42</b>', 'identical figures, different page numbers, one extra footnote'], ['NordVektor’s latest approved engineering PDF', '<b>4AC1</b>', '–']], ['File', 'Fingerprint', 'Note']) . '
    '],
  'A03' => ['kind' => 'calendar', 'title' => 'Nadia’s timeline', 'meta' => 'Wednesday 16 September', 'body' => '
    <table class="cal"><tr><td>20:48</td><td>Nadia leaves the building (door log).</td></tr><tr><td>20:57</td><td>Bus card swiped at Sondergade.</td></tr>
    <tr><td>21:04–21:31</td><td>Video call with her sister from her private tablet.</td></tr></table>
    <p class="note">Nadia denies any download.</p>'],
  'A04' => ['kind' => 'log', 'title' => 'VPN overview', 'meta' => '16 September', 'body' => '
    ' . gn_t([['21:13', 'Login as NADIA.L', 'From an IP the company knows as an external cloud server'], ['', 'Method', '<b>Token refresh</b> – no new password, no MFA'], ['', 'Token issued', '3 September, from the company’s test environment']], ['Time', 'Event', 'Details']) . ''],
  'A05' => ['kind' => 'list', 'title' => 'Access groups', 'meta' => 'Who can read what', 'body' => '
    ' . gn_t([['engineering/final', 'Nadia Lund (read)'], ['compliance/audit', 'Rikke Falck, Henrik Dahl (read)'], ['marketing/launch', 'Lea Storm, Emil Friis'], ['all areas', 'IT (Oskar) can manage access, but cannot read the encrypted audit archive without a separate key']], ['Area', 'Access']) . ''],
  'A06' => ['kind' => 'messages', 'title' => 'Henrik’s internal email', 'meta' => '16 September, 18:22', 'body' => '
    <p class="quote">“If we lose the Helion tender, we must be able to point to a concrete cause. I won’t accept rumours. Everything must be verified at log level.”</p>'],
  'A07' => ['kind' => 'note', 'title' => 'Lea’s meeting notes', 'meta' => 'Public conference, 9 September', 'body' => '
    <p>Lea met Helion’s sales director at a public industry conference. She says they only talked industry politics.</p>
    <p class="note">According to the conference’s open meeting calendar they sat together for 12 minutes.</p>'],
  'B01' => ['kind' => 'list', 'title' => 'Version list', 'meta' => 'VektorCell 4 design document', 'body' => '
    ' . gn_t([['engineering/final', 'VC4-42', '11 Sept', '16', 'none', '4AC1'], ['compliance/audit', '<b>VC4-42-A</b>', '14 Sept', '<b>17</b>', '‘Kestrel-7 test cell’', '<b>8D42</b>']], ['Area', 'Version', 'Exported', 'Pages', 'Footnote', 'Fingerprint']) . '
    <p class="note">The leaked PDF has 17 pages and the Kestrel-7 footnote.</p>'],
  'B02' => ['kind' => 'log', 'title' => 'Export journal', 'meta' => '16 September', 'body' => '
    ' . gn_t([['19:48', 'VC4-42-A exported from compliance/audit', 'user <b>RFALCK</b> · session C-884 · PDF/A · destination ‘internal review’']], ['Time', 'Event', 'Details']) . '
    <p class="note">No export from engineering/final after 17:30. (The 21:13 download from NADIA.L fetched the 16-page VC4-42.)</p>'],
  'B03' => ['kind' => 'calendar', 'title' => 'Compliance calendar', 'meta' => 'Rikke Falck · 16 September', 'body' => '
    <table class="cal"><tr><td>All day</td><td>Home office</td></tr><tr><td>19:40–20:02</td><td>Quarterly audit export</td></tr></table>
    <p class="note">The calendar entry was created three weeks earlier.</p>'],
  'B04' => ['kind' => 'log', 'title' => 'Test environment token list', 'body' => '
    ' . gn_t([['T-19', 'NADIA.L', '3 Sept', 'Automated regression tests', 'Renewable without MFA until 30 Sept']], ['Token', 'Linked to', 'Issued', 'Purpose', 'Rule']) . '
    <p class="note">Rikke approved the exception in change request CR-118.</p>'],
  'B05' => ['kind' => 'messages', 'title' => 'Change request CR-118', 'meta' => 'Comments, 2 September', 'body' => '
    <div class="chat"><p class="msg in"><span>Rikke Falck</span>Keep test token T-19 active for compliance verification.</p>
    <p class="msg out"><span>Oskar Moller</span>Security risk. The token must only be used in the sandbox.</p>
    <p class="msg in"><span>Rikke Falck</span>My responsibility.</p></div>'],
  'B06' => ['kind' => 'report', 'title' => 'Cloud provider account overview', 'body' => '
    <p>The external IP used at 21:13 belongs to NordVektor’s own <b>test sandbox</b>, set up in <b>Rikke’s department</b>.</p>
    '],
  'B07' => ['kind' => 'report', 'title' => 'Print service receipt', 'meta' => 'CopyPoint', 'body' => '
    <dl class="rows"><dt>16 Sept, 20:06</dt><dd>A 17-page file placed in the upload queue</dd><dt>Customer</dt><dd><b>RFalck Consulting</b></dd><dt>Collection code</dt><dd>K7</dd><dt>Paid</dt><dd>Private card ending 6208</dd></dl>'],
  'C01' => ['kind' => 'audit', 'title' => 'Rikke’s payment overview', 'body' => '
    <dl class="rows"><dt>15 Sept</dt><dd>RFalck Consulting receives <b>185,000 kr.</b> from Northcap Advisory for ‘market diligence’</dd><dt>Account</dt><dd>Opened three months ago</dd></dl>
    <p class="note">The payment is not registered as approved side employment.</p>'],
  'C02' => ['kind' => 'report', 'title' => 'Northcap registration', 'meta' => 'Public company register, 1 August', 'body' => '
    <p>Northcap Advisory is adviser to <b>Helion’s investor group</b> – not an independent technical auditor.</p>'],
  'C03' => ['kind' => 'photo', 'title' => 'CopyPoint collection log', 'meta' => '16 September',
    'img' => ['file' => 'the-blue-folder/copypoint-cam.jpg', 'caption' => 'CopyPoint counter camera, 20:29', 'prompt' => 'Grainy colour CCTV still from above a print-shop counter at night, a person in a long dark coat seen from behind and the side, face hidden by a raised collar, holding a bright yellow document folder, stacks of paper and a large copier in the background, security-camera look, no readable text'],
    'body' => '
    {{IMG}}
    <p><b>20:29</b>: code K7 collected by a person whose booking name is <b>R. Falck</b>.</p>
    <p class="note">The camera shows a dark coat and a yellow folder, but no certain face identification.</p>'],
  'C04' => ['kind' => 'interview', 'title' => 'Oskar’s statement', 'body' => '
    <p>“I warned about T-19, but I had no rights to compliance/audit. The fake engineering download is an attack on Nadia’s alibi. No technician can tell where someone physically was from a token refresh alone.”</p>'],
  'C05' => ['kind' => 'messages', 'title' => 'Email from the rival’s adviser', 'meta' => '16 September, 22:08 · to Rikke', 'body' => '
    <p class="quote">“Thank you for your technical assessment. We have received the PDF/A version including the Kestrel note. We assume your confidentiality still applies.”</p>
    <p class="note">The sender’s domain belongs to Northcap.</p>'],
  'C06' => ['kind' => 'report', 'title' => 'Conflict of interest policy', 'body' => '
    <p>Staff with compliance duties must declare in writing any paid work for companies with a financial interest in ongoing tenders.</p>
    <p class="note">NordVektor’s register holds no declaration from Rikke.</p>'],
  'C07' => ['kind' => 'note', 'title' => 'Nadia’s private note', 'body' => '
    <p>Nadia had complained about the compliance process before, so she had a possible motive to hurt Rikke. But she had no access to the 17-page version.</p>
    '],
 ],
 'checkpoints' => [
  'A' => ['title' => 'The obvious suspect', 'prompt' => 'The download came from Nadia’s account. Does that mean Nadia did it?',
          'gate' => ['q' => 'What does the 21:13 login really show?', 'choices' => ['Nadia typed her password and MFA code from home', 'An old test token in Nadia’s name was refreshed from a cloud server – not a new login by Nadia', 'Nadia was in the office at 21:13'], 'answer' => 1,
                     'ok' => 'A token refresh needs no password and no person – and Nadia was on a video call. Open envelope B.'],
          'hints' => ['Don’t put too much weight on the account name. How was the login made?', 'Read A04 next to A03: no password, no MFA, a test token – while Nadia was on a call.']],
  'B' => ['title' => 'Which version leaked?', 'prompt' => 'The diagrams match – but which exact file did the rival get?',
          'gate' => ['q' => 'Which copy of the design leaked?', 'choices' => ['The engineers’ 16-page VC4-42', 'The 17-page compliance copy VC4-42-A with the Kestrel-7 footnote', 'A draft from the intern’s launch material'], 'answer' => 1,
                     'ok' => '17 pages, the Kestrel-7 footnote and fingerprint 8D42 – the compliance copy, not Nadia’s file. Open envelope C.'],
          'hints' => ['Compare page count, footnote and fingerprint.', 'B01 lists both versions. Which one matches A02 – and who exported it (B02)?']],
  'final' => ['title' => 'The accusation', 'prompt' => 'Who leaked the design, how did it reach the rival – and what was the download from Nadia’s account?',
          'hints' => ['Follow both the document’s route and the money’s route.', 'B02, B07 and C03 follow the file; C01, C02 and C05 follow the money.']],
 ],
 'accuse' => [
  'culprit_q' => 'Who leaked the design?',
  'wrong' => 'That’s not the person who passed the design to the rival.',
  'items' => ['version' => ['The file', 'Which file leaked, and from where?', 4], 'route' => ['The route', 'How did the file reach the rival?', 4], 'decoy' => ['The decoy', 'What was the 21:13 download from Nadia’s account?', 3]],
 ],
 'choices' => [
  'version' => [
   'a' => 'The engineers’ 16-page VC4-42, downloaded from Nadia’s account.',
   'b' => 'The 17-page compliance copy VC4-42-A with the Kestrel-7 footnote, exported from compliance/audit.',
   'c' => 'A printout of the intern’s launch slides.',
   'd' => 'The file Lea showed at the conference on 9 September.',
  ],
  'route' => [
   'a' => 'Nadia emailed it from her private tablet.',
   'b' => 'Oskar copied it out of the encrypted archive.',
   'c' => 'It was printed at CopyPoint under code K7 and passed on through the adviser Northcap.',
   'd' => 'Lea handed it over at the public conference.',
  ],
  'decoy' => [
   'a' => 'Proof that Nadia leaked the design.',
   'b' => 'A decoy: an old test token kept alive under Rikke’s change request, refreshed from her department’s sandbox.',
   'c' => 'Oskar’s routine backup job.',
   'd' => 'Henrik checking the logs after his email.',
  ],
 ],
 'worksheet' => ['Which exact file leaked?', 'Who exported it, and how did it leave the company?', 'Who paid, and why?', 'What was the download from Nadia’s account?', 'Which details were red herrings?'],
 'solution_title' => 'What really leaked from NordVektor',
];
