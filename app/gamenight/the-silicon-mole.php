<?php
// Game Night case 011: The Silicon Mole. Server-side only. Adapted from the 6CLUES premium beta set (2026).
return [
  "slug" => 'the-silicon-mole',
  "no" => '011',
  "title" => 'The Silicon Mole',
  "tagline" => 'A chip design leaks overnight. Every log points at the wrong man.',
  "teaser" => 'The secret design of a new chip leaks the night before launch. The door log blames a respected engineer – but the transfer came through someone else’s account.',
  "genre" => 'Corporate espionage',
  "level" => 1,
  "minutes" => [60, 90],
  "players" => [2, 6],
  "revision" => '1.0',
  "caseref" => 'XT-0614',
  "stamp" => 'LEAKED',
  "envelope" => '#BFC6CC',
  "flap" => '#9EA8B0',
  "cover" => [
   "file" => 'the-silicon-mole/cover.jpg',
   "prompt" => 'Night view of a glass high-rise technology campus in Shenzhen, one lit office floor, rain on the window, cool blue palette with one red accent light, corporate espionage mood, no people, no text, 4:3',
  ],
  "intro" => ['On the night of 14 June, the CAD files for <b>Project X9</b> – X-Tech’s new semiconductor prototype in Shenzhen – are copied out of the approved repository. At 08:20 the next morning a competitor shows slides with the same secret measurements.', 'The security report blames senior engineer <b>Jian Wu</b>: his badge was logged near the archive at the exact minute of the leak. But the transfer itself came through a remote maintenance account, and a huge supplier payment that same night has the board worried.', 'Who really took the design, how was the engineer framed – and which alarming records have nothing to do with it?'],
  "mission" => ['Find out who actually transferred the X9 design.', 'Explain how Jian Wu came to look guilty.', 'Sort the real clues from the alarming but unrelated records.', 'Back up your accusation with at least three document numbers.'],
  "questions" => ['What exactly was copied, and when?', 'Does a badge record prove who was holding the badge?', 'Which record describes the file transfer itself?', 'Where was the owner of the maintenance account during the transfer?', 'Why was the security report changed?', 'Who benefits from the leak?'],
  "suspects" => [[
    "id" => 'jian-wu',
    "name" => 'Jian Wu',
    "role" => 'Senior engineer',
   ], [
    "id" => 'lin-mei',
    "name" => 'Lin Mei',
    "role" => 'Security lead',
   ], [
    "id" => 'aaron-vale',
    "name" => 'Aaron Vale',
    "role" => 'External consultant',
   ], [
    "id" => 'xu-fei',
    "name" => 'Xu Fei',
    "role" => 'Procurement officer',
   ], [
    "id" => 'chen-rui',
    "name" => 'Chen Rui',
    "role" => 'Junior developer',
   ]],
  "packets" => [
   "START" => [
    "label" => 'Envelope A',
    "docs" => ['E01', 'E02', 'E03', 'E04', 'E05'],
   ],
   "B" => [
    "label" => 'Envelope B',
    "when" => 'you can explain why the badge record does not prove who was there',
    "docs" => ['E06', 'E07', 'E08', 'E09', 'E10'],
   ],
   "C" => [
    "label" => 'Envelope C',
    "when" => 'you have found the record that describes the file transfer itself',
    "docs" => ['E11', 'E12', 'E13', 'E14', 'E15'],
   ],
  ],
  "docs" => [
   "E01" => [
    "kind" => 'report',
    "title" => 'Breach declaration',
    "meta" => 'X-Tech · 15 June',
    "body" => '<p>Project X9 prototype CAD files were copied outside the approved repository at <b>23:47 on 14 June</b>.</p><p>At 08:20 the next day a public competitor presentation showed matching, non-public measurements.</p>',
   ],
   "E02" => [
    "kind" => 'log',
    "title" => 'Door access log',
    "meta" => 'Security system · 14 June',
    "body" => '<table class="log"><tr><td>21:17</td><td>E-204</td><td>entered design floor</td></tr><tr><td>22:08</td><td>E-204</td><td>entered again</td></tr><tr><td>23:47</td><td>E-204</td><td>recorded near the archive</td></tr><tr><td>00:12</td><td>E-217</td><td>entered the security office</td></tr></table><p class="note">Badge E-204 is issued to Jian Wu.</p>',
    "img" => [
     "file" => 'the-silicon-mole/access-log.jpg',
     "caption" => 'Access reader and log screen',
     "prompt" => 'Illustration: Access reader and log screen, film-noir evidence photo, no text',
    ],
   ],
   "E03" => [
    "kind" => 'interview',
    "title" => 'Interview: Jian Wu',
    "meta" => '16 June',
    "body" => '<p>“I worked until 22:20. My badge was on the shared charging tray from 22:25 until the morning. I was at home during the breach.”</p><p>“Lin told me I would be dismissed unless I accepted responsibility.”</p>',
   ],
   "E04" => [
    "kind" => 'report',
    "title" => 'Remote account schedule',
    "meta" => 'IT administration · 14 June',
    "body" => '<dl class="rows"><dt>Account</dt><dd>EXT-AV – maintenance</dd><dt>Assigned to</dt><dd>Consultant Aaron Vale only</dd><dt>Session</dt><dd>23:30–00:00</dd><dt>Scope</dt><dd>Diagnostics</dd></dl><p class="note">File exports were explicitly prohibited.</p>',
   ],
   "E05" => [
    "kind" => 'log',
    "title" => 'Video call metadata',
    "meta" => 'Hong Kong client · 14 June',
    "body" => '<p>Aaron Vale joined the call from 23:30 to 23:58. Camera off after 23:41; microphone muted. His “present” indicator stayed green the whole time.</p><p class="note">Nobody confirms speaking to him between 23:42 and 23:55.</p>',
   ],
   "E06" => [
    "kind" => 'log',
    "title" => 'Repository audit trace',
    "meta" => 'Automated · digitally signed',
    "body" => '<table class="log"><tr><td>23:46:58</td><td>Account EXT-AV requested X9/CAD/master</td></tr><tr><td>23:47:09</td><td>Service gateway issued transfer token <b>9F2</b></td></tr><tr><td>23:47:31</td><td>External destination connected using token 9F2</td></tr></table><p class="note">No command came from Jian Wu’s engineer account.</p>',
    "img" => [
     "file" => 'the-silicon-mole/cad-laptop.jpg',
     "caption" => 'The X9 design on screen',
     "prompt" => 'Illustration: The X9 design on screen, film-noir evidence photo, no text',
    ],
   ],
   "E07" => [
    "kind" => 'report',
    "title" => 'Security report – version history',
    "meta" => 'Document history',
    "body" => '<dl class="rows"><dt>Version A</dt><dd>15 June, 01:02 – “remote account EXT-AV transfer”. Audit trace attached.</dd><dt>Version B</dt><dd>15 June, 02:24, saved by Lin Mei – “badge E-204 caused breach”. Audit trace removed.</dd></dl>',
   ],
   "E08" => [
    "kind" => 'interview',
    "title" => 'Interview: Lin Mei',
    "meta" => '16 June',
    "body" => '<p>“I changed the summary because I thought the badge event had to be decisive. I was wrong.”</p><p>“I hid the remote trace because I was afraid our maintenance controls would be blamed. I received no money and had no contact with the competitor.”</p>',
   ],
   "E09" => [
    "kind" => 'audit',
    "title" => 'Supplier payment',
    "meta" => 'Finance · 14 June',
    "body" => '<dl class="rows"><dt>Amount</dt><dd>CNY 2,800,000 at 23:56</dd><dt>Payee</dt><dd>SKYRIDGE TECH – fabrication deposit</dd><dt>Order</dt><dd>PO-991 issued 3 June</dd><dt>Delivery</dt><dd>Acceptance signed 12 June</dd><dt>Approval</dt><dd>Invoice approved by two officers</dd></dl><p class="note">The amount is large, but it matches the contract milestone.</p>',
   ],
   "E10" => [
    "kind" => 'audit',
    "title" => 'Consultant invoice history',
    "meta" => 'Accounts payable',
    "body" => '<p>On 15 June Aaron Vale submitted a new offshore consulting invoice for <b>USD 310,000</b>, marked “competitive intelligence research”.</p><p>No X-Tech contract approved such a service. His accounting contact asked for payment through an unrelated company.</p>',
   ],
   "E11" => [
    "kind" => 'photo',
    "title" => 'Badge tray camera',
    "meta" => 'Video stills · 14 June',
    "body" => '<p>At 22:27 Jian places badge E-204 on the shared visitor-desk tray. At 23:43 a hooded maintenance visitor briefly moves the badges. The image does not show a face.</p><p class="note">A visitor badge was issued to Aaron Vale at 22:58.</p>',
    "img" => [
     "file" => 'the-silicon-mole/badge-tray.jpg',
     "caption" => 'Badge tray camera, 23:43',
     "prompt" => 'Grainy CCTV still from above of an office visitor desk with a tray of plastic ID badges, a hooded figure in a maintenance jacket reaching for the badges, face not visible, blue-grey security-camera look, no readable text',
    ],
   ],
   "E12" => [
    "kind" => 'log',
    "title" => 'Visitor and network log',
    "meta" => 'Reception · network join',
    "body" => '<table class="log"><tr><td>22:58</td><td>Visitor Aaron Vale checks in</td></tr><tr><td>23:31</td><td>EXT-AV VPN session starts from the on-site guest network – device: his temporary laptop</td></tr><tr><td>00:06</td><td>Aaron Vale checks out</td></tr></table><p class="note">The Hong Kong video call stayed connected over the same laptop.</p>',
   ],
   "E13" => [
    "kind" => 'lab',
    "title" => 'Device artifact',
    "meta" => 'Internal forensics',
    "body" => '<p>Temporary laptop AV-17 still holds the destination host <b>export-gateway.example</b> and token reference <b>9F2</b>. The laptop was returned to the company on 16 June.</p><p class="note">Jian’s laptop contains no trace of token 9F2.</p>',
   ],
   "E14" => [
    "kind" => 'interview',
    "title" => 'Statement: Chen Rui',
    "meta" => '16 June',
    "body" => '<p>“My deployment log says no X9 file was built after 21:30.”</p><p>“I kept the audit receipt because Lin asked me to remove its link from a dashboard. I did not delete the signed record underneath.”</p>',
   ],
   "E15" => [
    "kind" => 'log',
    "title" => 'External gateway receipt',
    "meta" => 'Automated receipt · 15 June',
    "body" => '<p>export-gateway.example acknowledged a completed archive transfer at <b>23:47:31</b> with session token <b>9F2</b>. The manifest lists X9/CAD/master and five restricted design files.</p><p class="note">The receipt does not name any person.</p>',
   ],
  ],
  "checkpoints" => [
   "A" => [
    "title" => 'The badge and the account',
    "prompt" => 'The door log puts Jian’s badge near the archive at 23:47. Does that prove Jian took the design?',
    "gate" => [
     "q" => 'What does a badge record actually prove?',
     "choices" => ['That the badge owner was standing there', 'That the badge was used – not who was holding it', 'That the files were copied with that badge'],
     "answer" => 1,
     "ok" => 'Right – a badge is not a face. And Jian says his badge was on a shared tray. Open envelope B.',
    ],
    "hints" => ['Which record describes the file transfer rather than a door opening?', 'Look at who the remote account EXT-AV belongs to – and what his video call really shows after 23:41.'],
   ],
   "B" => [
    "title" => 'The trustworthy log',
    "prompt" => 'Two versions of the security report tell different stories. Which record can you trust?',
    "gate" => [
     "q" => 'Which record names the account that requested the files?',
     "choices" => ['The door access log (E02)', 'The signed repository audit trace (E06)', 'Lin’s version B of the report (E07)'],
     "answer" => 1,
     "ok" => 'Yes – the signed trace names EXT-AV and token 9F2, not Jian. Open envelope C.',
    ],
    "hints" => ['Compare the remote account, the visitor log and the call metadata.', 'Lin hid the trace – but does that make her the thief?'],
   ],
   "final" => [
    "title" => 'The accusation',
    "prompt" => 'Who transferred the X9 design, how was Jian framed, and which records were red herrings?',
    "hints" => ['Find the unique token that appears both on the export and on a specific device.', 'E06 + E12 + E13 + E15 tie the transfer to one laptop.'],
   ],
  ],
  "accuse" => [
   "culprit_q" => 'Who leaked the X9 design?',
   "wrong" => 'That’s not the person who transferred the design.',
   "items" => [
    "method" => ['The method', 'How was the design taken out?', 4],
    "frame" => ['The frame-up', 'Why did Jian Wu look guilty?', 4],
    "herring" => ['The red herring', 'What about the CNY 2.8 million payment?', 3],
   ],
  ],
  "choices" => [
   "method" => [
    "a" => 'Jian copied the files with his badge at the archive.',
    "b" => 'Through maintenance account EXT-AV from the temporary laptop on site, with transfer token 9F2.',
    "c" => 'Lin Mei sent the files when she edited the report.',
    "d" => 'Chen Rui built and uploaded a new X9 file after 21:30.',
   ],
   "frame" => [
    "a" => 'Jian really was in the building at 23:47.',
    "b" => 'His badge, left on the shared tray, was moved at 23:43 – and Lin rewrote the report to blame the badge.',
    "c" => 'Jian’s laptop held token 9F2.',
    "d" => 'The competitor named Jian as their source.',
   ],
   "herring" => [
    "a" => 'It was the payment for the stolen design.',
    "b" => 'It was a legitimate, pre-approved contract milestone with no link to the leak.',
    "c" => 'It was Lin Mei’s bribe.',
    "d" => 'It was Aaron Vale’s consulting fee.',
   ],
  ],
  "worksheet" => ['What happened?', 'Who was responsible – and what was the motive?', 'Which documents prove it? Name at least three.', 'Which misleading explanation did you rule out, and why?', 'What should happen now?'],
  "solution_title" => 'How the X9 design really left X-Tech',
 ];
