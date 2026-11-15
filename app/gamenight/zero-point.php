<?php
// Game Night case 002: Zero Point. Server-side only. Translated and adapted from the Danish beta 'Nulpunkt'.
return [
 'slug' => 'zero-point',
 'no' => '002',
 'title' => 'Zero Point',
 'tagline' => 'A meteorite vanishes from a locked case. The alarm never made a sound.',
 'teaser' => 'The star exhibit of Nordhavn Science House, the meteorite STARFALL, is gone. The case was never broken – and the weight sensor swears it never moved.',
 'genre' => 'Heist',
 'level' => 3,
 'minutes' => [90, 150],
 'players' => [2, 6],
 'revision' => '1.0',
 'caseref' => 'NSH-2026-1017',
 'stamp' => 'STOLEN',
 'envelope' => '#B9C3C9', 'flap' => '#9AA7AF',
 'cover' => ['file' => 'zero-point/cover.jpg', 'prompt' => 'Cinematic illustration of a dark, rough iron meteorite glowing softly under a spotlight inside a glass museum display case at night, empty modern science museum hall, cool blue and steel-grey palette with one warm accent light, mysterious heist mood, no people, no text, 4:3'],
 'intro' => [
  'At 21:09 on Saturday 17 October 2026, the police receive an alarm from a locked display case at <b>Nordhavn Science House</b>. The museum’s star exhibit, the meteorite <b>STARFALL</b>, is gone. In its place lies an object that looks just like it at first glance.',
  'STARFALL weighs exactly 1.840 kg, is on loan from a private collection and is insured for 3.8 million kroner. The museum closed to visitors at 20:00. The glass is intact, the lock is intact, and the weight sensor never raised an alarm.',
  'No murder this time – but plenty of lies, a vanished meteorite and digital traces that don’t tell the whole truth.',
 ],
 'mission' => [
  'Find out who removed the original meteorite.',
  'Pin down when it happened – to the minute if you can.',
  'Explain how the alarm and the weight sensor were fooled, and how STARFALL left the building.',
  'Back up your accusation with at least four document numbers.',
 ],
 'questions' => [
  'Who had a believable reason to be near case M-4 after closing?',
  'Which alarm might be a false trail?',
  'Can every clock in the building be trusted?',
  'What can a weight sensor actually tell you?',
  'Where did things leave the building that evening – and how heavy were they?',
  'Who did what, when – and why?',
 ],
 'suspects' => [
  ['id' => 'nora-berg', 'name' => 'Nora Berg', 'role' => 'Curator'],
  ['id' => 'leo-strand', 'name' => 'Leo Strand', 'role' => 'External technician'],
  ['id' => 'felix-holm', 'name' => 'Felix Holm', 'role' => 'Security guard'],
  ['id' => 'selma-juhl', 'name' => 'Selma Juhl', 'role' => 'Conservator'],
  ['id' => 'arman-shah', 'name' => 'Arman Shah', 'role' => 'IT security consultant'],
  ['id' => 'vera-lind', 'name' => 'Vera Lind', 'role' => 'Event coordinator'],
 ],
 'packets' => [
  'START' => ['label' => 'Start folder', 'docs' => ['S-01', 'S-02', 'S-03', 'S-04', 'S-05', 'S-06', 'S-07', 'S-08', 'S-09', 'S-10', 'S-11', 'S-12']],
  'B' => ['label' => 'Envelope B', 'when' => 'you can explain how STARFALL could vanish without a physical alarm', 'docs' => ['B-01', 'B-02', 'B-03', 'B-04', 'B-05', 'B-06', 'B-07', 'B-08']],
  'C' => ['label' => 'Envelope C', 'when' => 'you can name the minute the case was opened and who was there', 'docs' => ['C-01', 'C-02', 'C-03', 'C-04', 'C-05', 'C-06', 'C-07']],
 ],
 'docs' => [
  'S-01' => ['kind' => 'report', 'title' => 'How the case began', 'meta' => 'Nordhavn Science House · 17 October 2026', 'body' => '
    <p>At 21:09 the police receive an alarm from a locked display case at Nordhavn Science House. The museum’s star exhibit, the meteorite <b>STARFALL</b>, has disappeared. In the case lies an object that at first glance looks like the real meteorite.</p>
    <dl class="rows"><dt>Object</dt><dd>Meteorite STARFALL, on loan from a private collection</dd><dt>Weight</dt><dd>Exactly <b>1.840 kg</b></dd><dt>Insured for</dt><dd>3.8 million kroner</dd><dt>Museum closed</dt><dd>20:00</dd></dl>
    <p>Your task is to prove: Who removed the original? When did it happen? How was it done? And how did the meteorite leave the building?</p>
    '],
  'S-02' => ['kind' => 'plan', 'title' => 'Site plan', 'meta' => 'Simplified floor plan – not to scale', 'body' => '
    <ul class="plain"><li><b>North:</b> Public entrance → foyer → exhibition hall (display case <b>M-4</b>).</li>
    <li><b>West:</b> Exhibition hall → staff corridor → workshop (about 25 metres, about 1 minute).</li>
    <li><b>South:</b> Staff corridor → tech room → service gate (about 30 metres, about 1 minute).</li>
    <li><b>East:</b> Exhibition hall → control room (about 20 metres).</li></ul>
    <p>The service gate is used by suppliers. Camera <b>K-2</b> looks from the staff corridor towards the exhibition hall. Camera <b>K-3</b> looks towards the service gate.</p>
    <p class="note">Case M-4 can only be opened without the normal alarm with a valid technician badge <b>and</b> a time-limited permit from a curator.</p>'],
  'S-03' => ['kind' => 'list', 'title' => 'People in the building', 'meta' => 'Six people with access to the house', 'body' => '
    <table class="guests"><tr><td><b>Nora Berg</b></td><td>Curator. Has the authority to switch on service access to case M-4. Under pressure from the lender.</td></tr>
    <tr><td><b>Leo Strand</b></td><td>External technician. Working on sensors and controls this evening. Badge <b>L-17</b>.</td></tr>
    <tr><td><b>Felix Holm</b></td><td>Security guard. Responsible for surveillance, rounds and the service gate.</td></tr>
    <tr><td><b>Selma Juhl</b></td><td>Conservator. Makes test copies for teaching and exhibitions.</td></tr>
    <tr><td><b>Arman Shah</b></td><td>IT security consultant. Tests the alarm system’s digital events after closing time.</td></tr>
    <tr><td><b>Vera Lind</b></td><td>Event coordinator. Responsible for the evening’s suppliers and returning equipment.</td></tr></table>'],
  'S-04' => ['kind' => 'calendar', 'title' => 'Duty and activity plan', 'meta' => 'Extract from the internal calendar', 'body' => '
    <p class="cal-day">Saturday 17 October</p>
    <table class="cal"><tr><td>19:30</td><td>Last visitors and tidying up.</td></tr><tr><td>20:00</td><td>Museum closed to the public.</td></tr>
    <tr><td>20:20–20:40</td><td>Technician visit: adjust sensor module at M-4 (Leo). Nora to give time-limited service access.</td></tr>
    <tr><td>20:30–21:00</td><td>Felix: rounds of the west wing, check service gate.</td></tr>
    <tr><td>20:45–21:00</td><td>Collection of event equipment (Vera coordinates).</td></tr>
    <tr><td>21:05–21:15</td><td>Announced digital alarm test (Arman).</td></tr></table>
    <p class="note">No power cut is planned in the building.</p>'],
  'S-05' => ['kind' => 'report', 'title' => 'First police note', 'meta' => 'Written at 21:29', 'body' => '
    <p>The glass and lock of the case show no signs of force. A dark object about the size of STARFALL lies in the holder. It has a small shiny flat surface underneath.</p>
    <p>The guard called in the alarm after a digital <b>‘CASE TAMPER’</b> signal at 21:09. The monitoring centre registered <b>no</b> physical weight-sensor alarm at that time.</p>
    <p>The service gate is intact. There are no signs of a break-in from outside. The guard’s first theory is that a hacker opened the case remotely.</p>'],
  'S-06' => ['kind' => 'interview', 'title' => 'Interview: Nora Berg', 'meta' => 'Curator · 22:10', 'body' => '
    <p>“I approved Leo’s service access at 20:25. It was a routine calibration of temperature and weight. I had asked him to finish before 20:35. After that I was at my computer talking to the lender’s lawyer. I didn’t touch the case.”</p>
    <p>“We’ve discussed showing a replica before, but it was never approved. I would lose my job if the original disappeared.”</p>'],
  'S-07' => ['kind' => 'interview', 'title' => 'Interview: Leo Strand', 'meta' => 'Technician · 22:16', 'body' => '
    <p>“I was in the tech room from about 20:28 to 20:40 testing the air handling. I didn’t open the case – that wasn’t needed for the job at all. Afterwards I carried a box of broken lighting equipment to the service gate. I left the building before 21:00.”</p>
    <p>“I know Selma works with copies, but I’ve never had one in my hands. Ask the IT consultant if the system shows something wrong.”</p>'],
  'S-08' => ['kind' => 'interview', 'title' => 'Interview: Felix Holm', 'meta' => 'Security guard · 22:23', 'body' => '
    <p>“I checked the west wing at about 20:30. I saw Leo by the staff corridor, but I didn’t look at my watch. The service gate was opened for a bike courier. That was a planned collection Vera had put on the list.”</p>
    <p>“At 21:09 I saw the alarm on the screen. I was in the control room and found no damage. I never imagined the object could have been swapped.”</p>'],
  'S-09' => ['kind' => 'interview', 'title' => 'Interview: Selma Juhl', 'meta' => 'Conservator · 22:31', 'body' => '
    <p>“A week ago I made a teaching copy of STARFALL in resin and metal. It was for a school project, and it weighed exactly the same as the original. It usually sits in the workshop.”</p>
    <p>“I was having dinner in the staff kitchen from about 20:25 to 20:50. I don’t know of any permission to put the copy in the case.”</p>'],
  'S-10' => ['kind' => 'interview', 'title' => 'Interview: Arman Shah', 'meta' => 'IT security · 22:37', 'body' => '
    <p>“I was due to run an approved test of alarm signals after 21:05. I could only send simulated events. My account can’t operate the case’s mechanical lock.”</p>
    <p>“The alarm may well have been my test. That doesn’t mean I took anything. Look at the physical access logs, not just the alarms.”</p>'],
  'S-11' => ['kind' => 'interview', 'title' => 'Interview: Vera Lind', 'meta' => 'Event coordinator · 22:43', 'body' => '
    <p>“I had booked a bike courier to collect our used sound and lighting equipment at about 20:45. The courier company was told to collect one box at the service gate.”</p>
    <p>“I was in reception when the courier came. I didn’t approve anything special in the box, and I didn’t put the label on it.”</p>'],
  'S-12' => ['kind' => 'note', 'aid' => true, 'title' => 'Case journal – START', 'meta' => 'Your own notes', 'body' => '
    <div class="aid"><p><b>What is certain so far?</b></p><ol><li>Who has a believable reason to be close to M-4?</li><li>Which alarm could be a false trail?</li><li>Which three documents will you compare when you open envelope B?</li></ol></div>
    <p>When you have discussed the first evidence, open envelope B. No web access is needed.</p>'],
  'B-01' => ['kind' => 'log', 'title' => 'Access log, case M-4', 'meta' => 'Source: door controller · synchronised to network time (NTP)', 'body' => '
    ' . gn_t([['20:25:11', 'SERVICE PERMIT', 'Nora Berg · valid until 20:37:11'], ['20:30:54', 'TECH BADGE', 'L-17 · service panel activated'], ['20:32:08', '<b>LATCH OPEN</b>', 'service access approved'], ['20:33:42', 'LATCH CLOSED', 'service access approved'], ['20:34:09', 'LOAD BASELINE', '1.840 kg · calibration complete'], ['20:37:11', 'SERVICE PERMIT EXPIRED', ''], ['21:07:58', 'DIGITAL TAMPER EVENT', 'test channel']], ['Time', 'Event', 'Details']) . '
    <p class="note">No other openings of M-4 were recorded that evening. A load sensor only records weight – not which object is lying on it.</p>'],
  'B-02' => ['kind' => 'photo', 'img' => ['file' => 'zero-point/k2-still.jpg', 'caption' => 'Camera K-2 still, local time 20:26:42', 'prompt' => 'Grainy black-and-white CCTV still from a ceiling camera looking down a narrow museum staff corridor, a person in a dark technician jacket seen from behind carrying a black hard equipment case with a strip of orange tape on the handle, face not visible, timestamp overlay area left blank, security-camera look'], 'title' => 'Camera K-2: printout', 'meta' => 'System check carried out after the incident', 'body' => '
    <p>After a software update, camera K-2 had no access to network time. Its built-in clock ran exactly <b>four minutes slow</b> compared with the door controller.</p>
    ' . gn_t([['20:26:42', 'A person in a dark technician’s jacket with a rectangular equipment case walks from the workshop towards the exhibition hall.'], ['20:29:46', 'The same person walks from the exhibition hall towards the staff corridor with the case.']], ['K-2 local time', 'What the camera shows']) . '
    <p>The person’s face can’t be seen, but an <b>orange tape marking</b> is visible on the handle of the case. The clips are handed over in chronological order.</p>'],
  'B-03' => ['kind' => 'report', 'title' => 'Technical work order', 'meta' => 'WO-4421 · ordered by Nora', 'body' => '
    <dl class="rows"><dt>Task</dt><dd>Check M-4 temperature probe and calibrate the load cell. Requires the service panel to be switched on.</dd></dl>
    <p><b>Procedure:</b> 1) Unlock the service panel. 2) Check the temperature reading. 3) Check the weight using an external reference block. 4) Close the service panel.</p>
    <p class="note">Note from the manufacturer: opening the case lid itself is <b>NOT</b> needed for this type of calibration. A ‘LATCH OPEN’ event cannot be caused by a temperature adjustment.</p>'],
  'B-04' => ['kind' => 'report', 'title' => 'Workshop loans', 'meta' => 'Copy register: object REPLICA-R7', 'body' => '
    <p>18 October, planned school project: teaching copy <b>REPLICA-R7</b> of STARFALL reserved for the workshop.</p>
    <p>17 October, 19:52: a note on the workshop table, written in ballpoint pen:</p>
    <p class="handwriting">Borrowed R7 as reference at M-4. L / tech</p>
    <p>Selma Juhl: “I didn’t write that note. The copy was on my shelf at 19:30 and gone after 21:00.”</p>
    <p class="note">In the workshop there is an empty space for an equipment case, and a loose strip of orange tape. The case is missing.</p>'],
  'B-05' => ['kind' => 'lab', 'title' => 'Laboratory sheet', 'meta' => 'Preliminary comparison, 23:18', 'body' => '
    <dl class="rows"><dt>Real STARFALL</dt><dd>1.840 kg; natural minerals and iron-nickel; uneven surface (latest catalogue check).</dd>
    <dt>Object from M-4</dt><dd>1.840 kg; resin with a steel core; a smooth metal surface underneath, faintly engraved <b>‘R7’</b>.</dd></dl>
    '],
  'B-06' => ['kind' => 'log', 'title' => 'Tech room log', 'meta' => 'PLC and workstation', 'body' => '
    ' . gn_t([['20:26:12', 'LOGIN · Leo / L-17'], ['20:27:01', 'Ventilation profile opened'], ['20:28:50', 'Session set to idle'], ['20:40:33', 'SESSION RESUMED · Leo / L-17'], ['20:41:05', 'LOGOUT']], ['Time', 'Event']) . '
    <p>The system does not log whether anyone is physically in the tech room while a session is idle.</p>
    <p class="note">According to the local door sensor, the tech room door was not opened between 20:28 and 20:40. But there is a second exit through the staff corridor that this sensor does not cover.</p>'],
  'B-07' => ['kind' => 'report', 'title' => 'Power and building report', 'meta' => 'Building operations, 20:00–21:20', 'body' => '
    <p>No power cuts, voltage drops or restarts of the door controller. Camera K-2’s time error was caused by missing time synchronisation, not a power failure.</p>
    <p>Between 20:30 and 20:36 there is no general fault in the alarm system. The case recorded a normal weight after 20:34.</p>
    <p class="note">The operations manager stresses that a ‘digital tamper event’ can be triggered by a test signal without anything physically being opened.</p>'],
  'B-08' => ['kind' => 'note', 'aid' => true, 'title' => 'Questions before envelope C', 'meta' => 'Checkpoint: time and method', 'body' => '
    <div class="aid"><p><b>STOP and discuss:</b></p><ol><li>At what exact time could the original have been removed?</li><li>Which evidence shows that the person using technician access did more than the work order required?</li><li>What does the wrong time on camera K-2 mean for the technician’s story?</li></ol></div>
    <p>When your table has a theory, you may open envelope C. Use the online helper for a discreet hint if you need one.</p>'],
  'C-01' => ['kind' => 'report', 'title' => 'Service gate: collection slip', 'meta' => 'External bike courier, job 81164', 'body' => '
    <dl class="rows"><dt>20:47:06</dt><dd>Box collected at the service gate</dd><dt>Label</dt><dd>‘LIGHT CONTROLLER / RETURN’</dd><dt>Sender</dt><dd>Nordhavn Science House</dd><dt>Destination</dt><dd><b>Private storage box 14</b>, Kajgade 6</dd><dt>Gross weight</dt><dd><b>4.200 kg</b> (scanner)</dd><dt>Carrier</dt><dd>CityCycle Express</dd></dl>
    <p>The courier says a man in a dark technician’s jacket put the box on a trolley. Nobody opened the parcel.</p>'],
  'C-02' => ['kind' => 'audit', 'img' => ['file' => 'zero-point/h32-case.jpg', 'caption' => 'Transport case H-32 (stock photo)', 'prompt' => 'Product-style photo of an open black hard-shell transport case with grey foam insert, a fist-sized irregular cavity cut into the foam, a strip of orange tape wrapped around the handle, on a workshop bench, neutral lighting, no text'], 'title' => 'Equipment case and weights', 'meta' => 'Purchase slip and stock list', 'body' => '
    <p>A hard transport case of type <b>H-32</b> was lent out from the museum workshop that day. It is black, has <b>orange tape on the handle</b> and a custom-cut foam insert shaped to STARFALL’s dimensions.</p>
    <dl class="rows"><dt>Case + foam</dt><dd>2.360 kg</dd><dt>STARFALL</dt><dd>1.840 kg</dd><dt>Total</dt><dd><b>4.200 kg</b></dd></dl>
    <p class="note">A normal faulty light controller sent for return weighs 0.750 kg. The museum’s returned equipment had already been put in a different cage in the basement.</p>'],
  'C-03' => ['kind' => 'log', 'title' => 'Shipping terminal receipt', 'meta' => 'Operator record, local server', 'body' => '
    <p>Transaction log for shipment 81164, extracted at 21:03:</p>
    ' . gn_t([['20:42:51', 'Label created at the terminal by the service gate · operator <b>L-17 / Leo Strand</b> · return code ‘EV-LIGHT’'], ['', 'Destination changed by hand from the supplier’s warehouse to <b>storage box 14</b>'], ['20:43:04', 'Label printed']], ['Time', 'Event']) . '
    <p class="note">The terminal clock is synchronised with the museum’s door controller. Any employee with an active badge may create a label, but the operator’s badge ID is recorded.</p>'],
  'C-04' => ['kind' => 'log', 'title' => 'Alarm log: digital test', 'meta' => 'Documentation from the security supplier', 'body' => '
    ' . gn_t([['21:07:58', 'TEST CHANNEL · ARMAN-SH · CASE TAMPER simulation'], ['21:08:01', 'TEST DELIVERY · delivered to central monitoring'], ['21:09:02', 'CALL INITIATED · Felix Holm']], ['Time', 'Event']) . '
    <p>Arman had a signed test permit from the museum’s operations manager. The test could send a ‘tamper’ event, but could not change the case’s physical lock log or the weight sensor’s baseline.</p>
    <p class="note">The supplier’s technician has confirmed that the alarm at 21:07 was a simulation.</p>'],
  'C-05' => ['kind' => 'report', 'title' => 'Storage box 14', 'meta' => 'Customer card and delivery record', 'body' => '
    <p>The storage company’s card says: box 14 was rented the same week by a company registered as <b>‘LS Teknikservice’</b>. Contact person: <b>Leo Strand</b>.</p>
    ' . gn_t([['21:08:42', 'CityCycle Express delivers a parcel to night box 14']], ['Time', 'Event']) . '
    <p class="note">Nobody has opened box 14 since. The storage company has locked it for the police, but it has not been seized yet.</p>'],
  'C-06' => ['kind' => 'messages', 'title' => 'Financial background', 'meta' => 'Extract of messages handed over voluntarily', 'body' => '
    <div class="chat"><p class="msg in"><span>15 October · private lender → Leo</span>180,000 by Monday at the latest. No more excuses.</p>
    <p class="msg out"><span>17 October, 18:12 · Leo’s note to himself</span>Case – pickup – box 14 – cash on delivery</p></div>
    '],
  'C-07' => ['kind' => 'note', 'aid' => true, 'title' => 'Accusation form', 'meta' => 'Fill in before you reveal the solution', 'body' => '
    <div class="aid"><ol><li>Who removed STARFALL?</li><li>In which time window – ideally at what minute – did it happen?</li><li>How were the alarm and weight systems fooled?</li><li>How did the meteorite get out of the museum?</li><li>Name at least four independent pieces of evidence that support your explanation.</li><li>Which suspicious details were red herrings – and why?</li></ol></div>
    <p>When everyone agrees, enter your accusation with the online helper. This document does not reveal the solution.</p>'],
 ],
 'checkpoints' => [
  'A' => ['title' => 'The silent alarm', 'prompt' => 'The glass is intact and the weight never changed. So how could STARFALL disappear without a physical alarm?',
          'gate' => ['q' => 'What can the weight sensor in M-4 really tell you?', 'choices' => ['Which object is lying in the case', 'Only how much the object in the case weighs', 'Who opened the case'], 'answer' => 1,
                     'ok' => 'A sensor measures kilograms, not identity – an object with the same weight would fool it. Open envelope B.'],
          'hints' => ['A weight sensor records kilograms, not the identity of the object.', 'Who was allowed to open the case after closing time – and who has a copy of exactly the same weight?']],
  'B' => ['title' => 'Time and method', 'prompt' => 'When exactly was the case opened – and was opening it part of the job?',
          'gate' => ['q' => 'Camera K-2 shows the person with the equipment case at 20:26:42 and 20:29:46. What was the real time?', 'choices' => ['20:22 and 20:25', '20:26 and 20:29 – the camera is right', '20:30 and 20:33'], 'answer' => 2,
                     'ok' => 'K-2 runs four minutes slow – so the person with the taped case was in the hall exactly when the latch opened at 20:32. Open envelope C.'],
          'hints' => ['Camera K-2 shows a time that is four minutes too early. Add four minutes.', 'Compare the work order (B-03) with the actual LATCH OPEN event in B-01.']],
  'final' => ['title' => 'The accusation', 'prompt' => 'Who took STARFALL, when and how – and how did it leave the building?',
          'hints' => ['Add the empty transport case’s weight to the original’s weight, and compare with the courier’s scanner.', 'Which badge created the shipping label, and who rented the storage box?']],
 ],
 'accuse' => [
  'culprit_q' => 'Who stole STARFALL?',
  'wrong' => 'That’s not the person who took the meteorite.',
  'items' => ['when' => ['The time', 'When was the original taken?', 4], 'method' => ['The method', 'How were the alarm and the weight sensor fooled?', 4], 'route' => ['The getaway', 'How did STARFALL leave the building?', 3]],
 ],
 'choices' => [
  'when' => [
   'a' => 'At 21:07, when the tamper alarm went off.',
   'b' => 'At about 20:32, during the service access.',
   'c' => 'At 20:47, at the service gate.',
   'd' => 'Before 20:00, while visitors were still inside.',
  ],
  'method' => [
   'a' => 'A hacker opened the case remotely.',
   'b' => 'The original was swapped for the weight-identical replica R7 while the latch was open.',
   'c' => 'The lock was forced while the alarm test was running.',
   'd' => 'The curator opened the case with her service permit and took the meteorite.',
  ],
  'route' => [
   'a' => 'Carried out through the public entrance under a coat.',
   'b' => 'Hidden in the workshop until the next morning.',
   'c' => 'In the orange-taped H-32 case, sent by bike courier to storage box 14.',
   'd' => 'Packed in with Vera’s returned lighting equipment to the supplier.',
  ],
 ],
 'worksheet' => ['Who removed STARFALL?', 'When did it happen – to the minute?', 'How were the alarm and the weight sensor fooled?', 'How did STARFALL leave the building?', 'Which details were red herrings?'],
 'solution_title' => 'What really happened at Nordhavn Science House',
];
