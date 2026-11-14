<?php
// Game Night case 005: Still Water. Server-side only. Translated and adapted from the Danish beta 'Stille vand'.
return [
 'slug' => 'still-water',
 'no' => '005',
 'title' => 'Still Water',
 'tagline' => 'A pump stops in the night. The backup never starts. It was no accident.',
 'teaser' => 'A night test at the Sondervig wastewater plant goes wrong: the main pump stops for 21 minutes and the backup stays silent. Management calls it a technical fault. An anonymous employee disagrees.',
 'genre' => 'Sabotage',
 'level' => 1,
 'minutes' => [100, 140],
 'players' => [2, 6],
 'revision' => '1.0',
 'caseref' => 'SDV-2026-0219',
 'stamp' => 'SABOTAGE',
 'envelope' => '#B8C9A8', 'flap' => '#97AC86',
 'cast' => true,
 'cover' => ['file' => 'still-water/cover.jpg', 'prompt' => 'Cinematic night illustration of a wastewater treatment plant by a fjord, round concrete basins reflecting orange floodlights, a small pump house with one red warning light, mist over dark still water, industrial noir mood, deep green and amber palette, no people, no text, 4:3'],
 'intro' => [
  'At 02:14 one night at the <b>Sondervig wastewater plant</b>, main pump P1 stops. For 21 minutes the level in basin 3 rises dangerously, reaching 91 % of capacity. Nobody is hurt and no wastewater reaches the fjord.',
  'But the backup pump P2 – which should start automatically – never does. Management calls it a technical accident. An anonymous employee asks you to look into it.',
 ],
 'mission' => [
  'Find the deliberate act behind the stop.',
  'Find out who carried it out.',
  'Explain why the automatic safety measures did not work – and why.',
  'Back up your accusation with at least four document numbers.',
 ],
 'questions' => [
  'Was this a power failure or a controlled stop?',
  'Why did the backup pump stay silent?',
  'What was actually planned for that night?',
  'Whose account appears in the control system – and from which computer?',
  'Who had something to gain from a dramatic failure?',
  'Who did what, when – and why?',
 ],
 'suspects' => [
  ['id' => 'karin-dam', 'name' => 'Karin Dam', 'role' => 'Operations manager'],
  ['id' => 'oliver-sahl', 'name' => 'Oliver Sahl', 'role' => 'Electrician'],
  ['id' => 'freja-nissen', 'name' => 'Freja Nissen', 'role' => 'Environmental analyst'],
  ['id' => 'henrik-lund', 'name' => 'Henrik Lund', 'role' => 'Project manager, new pump station'],
  ['id' => 'asta-winther', 'name' => 'Asta Winther', 'role' => 'Night guard'],
  ['id' => 'rune-kjaer', 'name' => 'Rune Kjaer', 'role' => 'External service technician'],
 ],
 'packets' => [
  'START' => ['label' => 'Start folder', 'docs' => ['A01', 'A02', 'A03', 'A04', 'A05', 'A06']],
  'B' => ['label' => 'Envelope B', 'when' => 'you can say what kind of event stopped pump P1', 'docs' => ['B01', 'B02', 'B03', 'B04', 'B05', 'B06']],
  'C' => ['label' => 'Envelope C', 'when' => 'you can explain why the backup pump P2 did not start', 'docs' => ['C01', 'C02', 'C03', 'C04', 'C05', 'C06']],
 ],
 'docs' => [
  'A01' => ['kind' => 'report', 'title' => 'Operations incident', 'meta' => 'Duty report', 'body' => '
    <dl class="rows"><dt>02:14</dt><dd>Main pump <b>P1</b> stops</dd><dt>02:35</dt><dd>P1 restarted</dd><dt>Basin 3</dt><dd>Reaches <b>91 %</b> of capacity</dd><dt>Backup pump P2</dt><dd>Does <b>not</b> start</dd></dl>
    <p class="note">No discharge to the fjord has been recorded.</p>'],
  'A02' => ['kind' => 'log', 'title' => 'SCADA event printout', 'meta' => 'Control system · plant time', 'body' => '
    ' . gn_t([['02:13:58', 'P1: remote STOP command received'], ['02:14:01', 'P1: confirmed STOP'], ['02:14:02', 'P2: standby inhibited by <b>TEST_LOCK</b>'], ['02:35:11', 'P1: remote START command received']], ['Time', 'Event']) . ''],
  'A03' => ['kind' => 'report', 'title' => 'Electrician’s report', 'meta' => 'Oliver Sahl · written the next morning', 'body' => '
    <p>Oliver went through the plant’s voltage logs the next morning. Both pumps had <b>stable voltage</b> throughout the incident. The main fuses and the emergency generator were intact.</p>
    <p class="quote">“This is not a power failure. The controller accepted a stop command.”</p>'],
  'A04' => ['kind' => 'report', 'title' => 'Operating manual, P1/P2', 'meta' => 'Extract', 'body' => '
    <p>Normally P2 starts after <b>30 seconds</b> if P1 stops and basin 3 is above 65 %.</p>
    <p><b>TEST_LOCK</b> only blocks P2 during an <b>approved, planned test</b>. During such a test a technician must stand by the pump.</p>'],
  'A05' => ['kind' => 'interview', 'title' => 'The night guard’s observation', 'meta' => 'Asta Winther', 'img' => ['file' => 'still-water/control-room.jpg', 'caption' => 'The control room screen seen from basin 3', 'prompt' => 'Night view through a large window into an empty industrial control room, a wall of monitors with one screen glowing red, reflections of floodlights on the glass, wet concrete walkway in the foreground, moody blue-green palette, no people, no readable text'], 'body' => '
    <p>“I was by basin 3 from 02:05 to 02:20. I saw nobody at the physical pump panels. I heard no power alarms, but through the window the control room screen flashed red at 02:14.”</p>
    {{IMG}}'],
  'A06' => ['kind' => 'calendar', 'title' => 'Test calendar', 'meta' => 'Approved plan for the night', 'body' => '
    <p class="quote">“Test of level sensor N3. No stopping of pumps. No change to TEST_LOCK.”</p>
    <p class="note">Signed the day before by operations manager Karin and electrician Oliver.</p>'],
  'B01' => ['kind' => 'log', 'title' => 'Control system access log', 'meta' => 'SCADA audit', 'body' => '
    ' . gn_t([['01:58', 'Remote session opened', 'HENRIK-PRJ'], ['02:10', 'TEST_LOCK activated', 'HENRIK-PRJ'], ['02:13', 'P1 remote STOP queued', 'HENRIK-PRJ'], ['02:35', 'P1 START queued', 'HENRIK-PRJ'], ['02:42', 'Session closed', 'HENRIK-PRJ']], ['Time', 'Event', 'Operator']) . '
    <p class="note">No other operator account was logged in between 01:00 and 03:00.</p>'],
  'B02' => ['kind' => 'report', 'title' => 'Remote access policy', 'meta' => 'IT and operations', 'body' => '
    <p>HENRIK-PRJ has temporary test access to SCADA from an approved service computer. The account is <b>personally issued</b> and may not be shared.</p>
    <p>Any change that stops production needs a <b>second approver</b>.</p>
    <p class="note">Night guards and external suppliers have no SCADA accounts.</p>'],
  'B03' => ['kind' => 'report', 'title' => 'Change ticket #771', 'meta' => 'Created the day before, 17:20', 'body' => '
    <dl class="rows"><dt>Created by</dt><dd>Henrik Lund</dd><dt>Title</dt><dd>“Simulated pump failure for approval of new project”</dd><dt>Approver</dt><dd><b>— empty —</b></dd></dl>
    <p class="note">The attached test plan only mentions a simulation in an offline test environment.</p>'],
  'B04' => ['kind' => 'log', 'title' => 'Network journal', 'meta' => 'VPN and key fobs', 'body' => '
    ' . gn_t([['23:17', 'Key fob for service computer SCADA-SVC1 collected by <b>Henrik</b>'], ['01:58', 'SCADA-SVC1 connects via VPN from the company’s meeting room'], ['03:10', 'SCADA-SVC1 returned']], ['Time', 'Event']) . ''],
  'B05' => ['kind' => 'report', 'title' => 'The external supplier', 'meta' => 'Rune Kjaer', 'body' => '
    <p>Rune serviced P2 the week before. That night he was on a ferry from 01:30 to 04:00. His company account was deactivated the day before the test and does not appear in any log.</p>
    <p class="note">An invoice for a new relay switch was only issued after the incident.</p>'],
  'B06' => ['kind' => 'interview', 'title' => 'Staff statements', 'meta' => 'The morning after', 'body' => '
    <p><b>Karin:</b> “Henrik had asked to see how the emergency function would behave, but I never gave permission to stop P1.”</p>
    <p><b>Oliver:</b> “I only knew about the level-sensor test. I had been at home since 22:00.”</p>
    <p><b>Henrik:</b> “I was asleep at home from midnight. If my account was used, somebody must have misused it.”</p>'],
  'C01' => ['kind' => 'audit', 'title' => 'Project status – internal audit', 'meta' => 'Project ‘Pump 2027’', 'body' => '
    <p>Henrik’s project <b>‘Pump 2027’</b> was 11 weeks late. An audit report the next morning was to decide whether investment in new controls was needed.</p>
    <p class="note">Henrik had bonus targets linked to the project being approved.</p>'],
  'C02' => ['kind' => 'note', 'title' => 'Draft presentation', 'meta' => 'Slide in Henrik’s folder · last edited 01:42', 'body' => '
    <p class="quote">“Current plant: documented critical instability. The backup function fails under load. Recommendation: approve new controls immediately.”</p>
    <p class="note">At 01:42 the incident had not yet happened.</p>'],
  'C03' => ['kind' => 'report', 'title' => 'Technical signature', 'meta' => 'Audit chain', 'body' => '
    <p>The commands in the audit log are signed by <b>HENRIK-PRJ</b> and by the device certificate of <b>SCADA-SVC1</b>. The log chain is unbroken.</p>
    <p class="note">The access system shows the service computer was on the meeting-room network throughout the session.</p>'],
  'C04' => ['kind' => 'note', 'title' => 'Handwritten note', 'meta' => 'Found in the meeting room · Henrik’s handwriting', 'body' => '
    <p class="handwriting">02:10 lock P2; 02:14 stop P1; 02:35 start. Max 25 min. No risk if B3 under 70 %.</p>
    <p class="note">At 02:05 the level in basin 3 was already 73 %.</p>'],
  'C05' => ['kind' => 'messages', 'title' => 'The environmental analyst’s readings', 'meta' => 'Freja Nissen', 'body' => '
    <p>Freja recorded basin 3 at <b>73 %</b> at 02:05.</p>
    <div class="chat"><p class="msg out"><span>02:07 · Freja → Henrik · delivered 02:07</span>Don’t run any pump test now – the load is higher than forecast.</p></div>'],
  'C06' => ['kind' => 'report', 'title' => 'Follow-up safety report', 'meta' => 'Independent inspection', 'body' => '
    <p>Both pumps worked mechanically. The incident was caused by a remote stop command and a manual TEST_LOCK at the same time.</p>
    <p class="note">No component fault can explain the combined sequence.</p>'],
 ],
 'checkpoints' => [
  'A' => ['title' => 'The stop', 'prompt' => 'Why did main pump P1 stop – and what is the difference between a power failure and a controlled stop?',
          'gate' => ['q' => 'What kind of event stopped P1?', 'choices' => ['A power failure', 'A remote command', 'A mechanical breakdown'], 'answer' => 1,
                     'ok' => 'The SCADA log shows a remote STOP, and the voltage was stable. Someone gave an order. Open envelope B.'],
          'hints' => ['The difference between a physical power cut and a controlled stop is central.', 'A02 says remote STOP; A03 says stable voltage.']],
  'B' => ['title' => 'The backup', 'prompt' => 'Why did backup pump P2 not start – and who changed the setting?',
          'gate' => ['q' => 'Why did backup pump P2 not start?', 'choices' => ['TEST_LOCK had been switched on', 'Its motor had burnt out', 'The water level was too low'], 'answer' => 0,
                     'ok' => 'TEST_LOCK blocked P2 – and it was switched on at 02:10, against the approved plan. Open envelope C.'],
          'hints' => ['Compare the approved test plan with the actual configuration history.', 'P2’s status is in A02, and who changed it is in B01.']],
  'final' => ['title' => 'The accusation', 'prompt' => 'Who created the double failure, how – and why?',
          'hints' => ['Look at approvals, alibis and a hidden presentation.', 'Use B01, B03, B04 and C03 – then C02 for the motive.']],
 ],
 'accuse' => [
  'culprit_q' => 'Who caused the pump failure?',
  'wrong' => 'That’s not the person who stopped the pumps.',
  'items' => ['stop' => ['The stop', 'Why did main pump P1 stop?', 4], 'lock' => ['The backup', 'Why did backup pump P2 not start?', 4], 'motive' => ['The motive', 'Why did the culprit do it?', 3]],
 ],
 'choices' => [
  'stop' => [
   'a' => 'A power cut.',
   'b' => 'A remote STOP command sent through the control system.',
   'c' => 'A mechanical breakdown.',
   'd' => 'The level-sensor test went wrong.',
  ],
  'lock' => [
   'a' => 'Its motor had burnt out.',
   'b' => 'The water level was too low to trigger it.',
   'c' => 'TEST_LOCK had been switched on without approval.',
   'd' => 'Rune’s new relay was faulty.',
  ],
  'motive' => [
   'a' => 'To cover up a mistake in the level-sensor test.',
   'b' => 'To stage a crisis so the delayed ‘Pump 2027’ project would be approved – with a bonus attached.',
   'c' => 'To damage the plant for a rival company.',
   'd' => 'Revenge for being passed over for promotion.',
  ],
 ],
 'worksheet' => ['Who caused the failure?', 'Why did P1 stop?', 'Why did P2 not start?', 'Why did the culprit do it?', 'Which details were red herrings?'],
 'solution_title' => 'What really happened at the Sondervig plant',
];
