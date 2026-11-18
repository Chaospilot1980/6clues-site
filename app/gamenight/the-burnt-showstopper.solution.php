<?php
// SPOILERS. Answer key and solution text for The Burnt Showstopper.
return [
 'culprit' => 'neil-harte',
 'what' => 'b',
 'where' => 'b',
 'motive' => 'b',
 'evidence' => ['A02', 'A04', 'B01', 'B02', 'B03', 'B04', 'B05', 'C01', 'C02', 'C05', 'C06'],
 'summary' => [
  'The saboteur is <b>Neil Harte</b>, the producer. Oven 3 was not faulty: at 14:12 its setting was changed from 160 °C to 250 °C by the studio app on tablet <b>TECH-2</b>.',
  'TECH-2 belongs to technician Dev Iyer, who left it charging on the gallery desk while he was in the canteen from 14:02 to 14:26. Its PIN was written on the back. The gallery Wi-Fi reaches only the control room – and the door log shows Neil alone in the gallery from 14:04 to 14:21. Saskia confirms he was talking to her from the gallery the whole time, not standing beside her on the floor as he claims.',
  'His reason: the channel would only renew the series – and his contract – if the final reached 8 million viewers. The night before he promised “tears and smoke – a proper disaster moment”. The burnt cake went viral and the final reached 10.4 million.',
 ],
 'conclusions' => [
  ['The oven worked; its setting was raised to 250 °C at 14:12.', 'A02, A04'],
  ['The change came from tablet TECH-2, which was charging in the gallery.', 'B01, B02, C05'],
  ['Dev was in the canteen; Neil was alone in the gallery 14:04–14:21.', 'B03, B04'],
  ['Neil lies about being on the floor – Saskia had him in her ear from the gallery.', 'B05, C06'],
  ['He needed a viral disaster to save the series and his contract.', 'C01, C02'],
 ],
 'timeline' => [
  ['Fri 18:24', 'Neil promises “a proper disaster moment”', 'C01'],
  ['14:02', 'Dev leaves TECH-2 on the gallery desk and goes to the canteen', 'B02, B03'],
  ['14:03', 'Kofi sets oven 3 to 160 °C', 'A02, B01'],
  ['14:04', 'Neil enters the gallery', 'B04'],
  ['14:10', 'Gemma takes icing sugar from the shelf – the dial does not move', 'A03, B06'],
  ['14:12', 'TECH-2 sets oven 3 to 250 °C', 'B01'],
  ['14:21', 'Neil steps out of the gallery for a minute', 'B04'],
  ['14:40', 'The burnt showstopper goes out live', 'A01'],
 ],
 'others' => [
  '<b>Gemma</b> stood next to oven 3 at 14:10, but camera 4 shows the dial untouched (B06).',
  '<b>Ollie</b> argued with Kofi at 14:30 – long after the change – and was on camera at his bench throughout (C04).',
  '<b>Marjorie</b> had a grudge but sat at the judges’ table in view of three cameras (C03).',
  '<b>Saskia</b> was on the studio floor on talkback (B05), and <b>Dev</b> was in the canteen (B03).',
 ],
 'fairness' => 'The tablet’s owner is a natural suspect, but the canteen till puts Dev elsewhere. The device, the Wi-Fi range and the gallery door log put the change in one room, at one time, with one person in it.',
];
