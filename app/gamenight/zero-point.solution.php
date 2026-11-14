<?php
// SPOILERS. Answer key and solution text for Zero Point. Only loaded server-side to score an accusation or after the reveal.
return [
 'culprit' => 'leo-strand',
 'when' => 'b',
 'method' => 'b',
 'route' => 'c',
 'evidence' => ['B-01', 'B-02', 'B-03', 'B-04', 'B-05', 'B-06', 'C-01', 'C-02', 'C-03', 'C-05', 'C-06'],
 'summary' => [
  'The thief is <b>Leo Strand</b>, the external technician. Earlier in the evening he took the teaching copy <b>REPLICA-R7</b> – which weighs exactly the same as STARFALL – from the workshop and left a note signed ‘L / tech’. He packed it in the orange-taped transport case H-32.',
  'Nora’s service permit was genuine. Leo used it and his badge L-17 to activate the service panel at 20:30:54, but the work order never required the lid to be opened. At <b>20:32:08 the latch opened</b>. He lifted out the real meteorite, put R7 in its place and closed the latch at 20:33:42. The weight sensor saw 1.840 kg before and after, so no alarm sounded. Camera K-2 seemed to put him there at 20:26 and 20:29 – but it runs four minutes slow.',
  'His tech-room session was left idle from 20:28 to 20:40 as an alibi; the second exit through the staff corridor isn’t covered by the door sensor. At 20:42 he created the courier label with his own badge and changed the destination to <b>storage box 14</b>, rented by his own firm. At 20:47 the courier collected a box weighing 4.200 kg – exactly case (2.360 kg) plus STARFALL (1.840 kg). The tamper alarm at 21:07 was only Arman’s announced test.',
 ],
 'conclusions' => [
  ['The object in the case is the weight-identical replica R7, so the weight sensor could not notice the swap.', 'B-05, B-01'],
  ['The only opening of M-4 was LATCH OPEN at 20:32:08 – and the work order did not need it.', 'B-01, B-03'],
  ['Corrected by four minutes, camera K-2 shows the person with the taped case in the hall at 20:30–20:33.', 'B-02'],
  ['Leo’s ‘tech room’ alibi is only an idle session, and there is an uncovered exit.', 'B-06, S-07'],
  ['The courier box weighed exactly case plus meteorite and went to a box rented by Leo’s firm, with a label made on his badge.', 'C-01, C-02, C-03, C-05'],
  ['Leo owed a lender 180,000 by Monday and planned ‘case – pickup – box 14’.', 'C-06'],
 ],
 'timeline' => [
  ['19:52', 'Note in the workshop: ‘Borrowed R7 as reference at M-4. L / tech’', 'B-04'],
  ['20:25', 'Nora issues a 12-minute service permit', 'B-01'],
  ['20:26–20:28', 'Leo logs into the tech room and leaves the session idle', 'B-06'],
  ['20:30:42', 'K-2 (shows 20:26:42): person with taped case heads into the hall', 'B-02'],
  ['20:30:54', 'Badge L-17 activates the service panel', 'B-01'],
  ['20:32:08', 'LATCH OPEN – the swap', 'B-01, B-03'],
  ['20:33:42–20:33:46', 'Latch closed; K-2 (shows 20:29:46): person leaves with the case', 'B-01, B-02'],
  ['20:34', 'Weight baseline 1.840 kg – the replica', 'B-01, B-05'],
  ['20:42:51', 'L-17 creates the courier label to storage box 14', 'C-03'],
  ['20:47', 'Courier collects a 4.200 kg box', 'C-01, C-02'],
  ['21:07:58', 'Arman’s simulated tamper alarm', 'C-04'],
  ['21:08:42', 'Parcel delivered to box 14', 'C-05'],
 ],
 'others' => [
  '<b>Nora</b> gave a genuine, time-limited permit – but the permit alone can’t open the case without a technician badge (S-02, B-01).',
  '<b>Selma</b> made the replica, but the note isn’t hers, and the case with the orange tape left her workshop without her (B-04).',
  '<b>Arman</b>’s alarm at 21:07 was an announced simulation that could not touch the lock or the weight (C-04).',
  '<b>Felix</b> called in the alarm and saw Leo near the staff corridor at about 20:30 – exactly when the camera, corrected, shows the case (S-08, B-02).',
  '<b>Vera</b> booked a courier for one box, but the label was made on Leo’s badge, not hers (S-11, C-03).',
 ],
 'fairness' => 'No single document convicts Leo: the badge proves the card was used and the box isn’t opened yet. The case rests on the corrected camera time, the unnecessary latch opening, the matching weights, the label made on his badge and the storage box rented by his firm.',
];
