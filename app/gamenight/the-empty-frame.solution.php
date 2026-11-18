<?php
// SPOILERS. Answer key and solution text for The Empty Frame.
return [
 'culprit' => 'lena-hartmann',
 'when' => 'b',
 'route' => 'c',
 'motive' => 'b',
 'evidence' => ['A02', 'A04', 'A05', 'A06', 'B01', 'B02', 'B03', 'B04', 'C01', 'C02', 'C03', 'C04'],
 'summary' => [
  'The thief is <b>Dr Lena Hartmann</b>, the museum’s paintings conservator. She had no alarm code of her own, but she kept Marcus Webb’s code 4471 on a sticky note on her lamp. At 17:58 – just after the press preview – she put the frame sensor in Gallery 4 into maintenance mode, cut the canvas from its stretcher and re-armed the sensor at 18:20. The empty frame stayed on the wall, so the alarm never sounded.',
  'Gallery 4 was roped off and dimmed during the party. The guard checked it from the rope every hour and saw only the gold frame shining. Nobody noticed the empty frame until the director’s tour at 22:40 – four and a half hours after the theft.',
  'At 19:31 a courier collected crate CS-12 from Lena’s studio, labelled “frame samples” for a restorer in Antwerp. It weighed 18 kg – earlier sample crates weighed 2–4 kg – and at 20:40 its address was changed to 14 Quay Lane. The restorer had ordered nothing. Lena owed money to a buyer called “Q”; her messages promised “she travels Saturday evening, before the party”.',
 ],
 'conclusions' => [
  ['The alarm watches the frame, and it was switched off 17:58–18:20 with code 4471.', 'A02, A06'],
  ['After 17:50 nobody saw the painting up close – only the frame from the rope.', 'A04, A05, B05'],
  ['Marcus was at the gym; his code was written on a note in the conservation studio.', 'B01, B02'],
  ['Lena was in the studio at 17:55 and 18:24, and the courier collected there at 19:31.', 'B03, C01'],
  ['Crate CS-12 weighed 18 kg instead of 2–4 kg, nobody had ordered it, and it was redirected.', 'C01, C02, C03'],
  ['Her messages show the debt and the plan.', 'C04'],
 ],
 'timeline' => [
  ['17:50', 'Press preview – painting still on the wall', 'A04'],
  ['17:55', 'Lena enters the conservation studio', 'B03'],
  ['17:58', 'Frame sensor G4-07 into maintenance mode, code 4471', 'A02'],
  ['18:20', 'Sensor re-armed – the frame is now empty', 'A02'],
  ['18:24', 'Lena back in the studio', 'B03'],
  ['19:31', 'Courier collects crate CS-12, 18 kg, signed L. Hartmann', 'B03, C01'],
  ['20:40', 'Crate redirected to 14 Quay Lane', 'C01'],
  ['22:05', '“Q”: “Arrived. Debt cleared.”', 'C04'],
  ['22:40', 'Director finds the empty frame', 'A01'],
 ],
 'others' => [
  '<b>Marcus</b>’s code was used, but he was at the gym from 17:52 to 18:58 (B01).',
  '<b>Tom</b>’s flat boxes held 48 empty trays and were searched (B06).',
  '<b>Isabel</b>’s insurance increase was demanded by the insurer, and she was with donors all evening (C05).',
  '<b>Sophie</b> wanted to buy the painting honestly and was beside the auctioneer all evening (C06).',
  '<b>Ravi</b> checked from the rope as usual and stayed at the Great Hall doors (A05, B05).',
 ],
 'fairness' => 'The famous “moment of the theft” at 22:40 is only the moment of discovery. The alarm printout, the dimmed and roped-off gallery and the guard’s rounds together show that the painting could have gone hours earlier – and the crate weights, the redirected address and the restorer’s answer show where it went.',
];
