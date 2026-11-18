<?php
// SPOILERS. Answer key and solution text for The Dinosaur Egg.
return [
 'culprit' => 'pam-hill',
 'when' => 'b',
 'how' => 'b',
 'motive' => 'b',
 'evidence' => ['A02', 'A05', 'B01', 'B02', 'B04', 'C01', 'C02', 'C03'],
 'summary' => [
  'The thief is <b>Pam Hill</b>, the volunteer guide. The case was opened once in the night, at 02:14, with its key – the glass was never broken.',
  'At 02:11 the case key was taken from the key box with <b>code 4</b>, the volunteer guides’ code, and returned at 02:19. Pam was the only volunteer guide in the building. She says she slept right through, but at Grace’s 02:00 headcount her sleeping bag was empty.',
  'Pam’s father found the egg in 1961 and sold it to the museum for £50. She believed it should be hers, and a collector had offered her £8,000. The egg was in her overnight bag, wrapped in a gift-shop T-shirt.',
 ],
 'conclusions' => [
  ['The case was opened at 02:14 with the key.', 'A01, A02'],
  ['The key was taken with code 4 – the volunteer guides’ code.', 'B01, B02'],
  ['Pam was not in her sleeping bag, though she says she was.', 'B04, C01'],
  ['She had a buyer and a grudge.', 'A05, C02'],
  ['The egg was in her bag.', 'C03'],
 ],
 'timeline' => [
  ['Thursday', 'Pam tells the collector: “Saturday”', 'C02'],
  ['22:00', 'Lights out; the egg is in its case', 'A01'],
  ['02:00', 'Headcount: Pam’s sleeping bag empty', 'B04'],
  ['02:11', 'Case key taken with code 4', 'B01'],
  ['02:14–02:16', 'Case opened and closed', 'A02'],
  ['02:19', 'Key returned', 'B01'],
  ['06:30', 'Curator finds the case empty', 'A01'],
 ],
 'others' => [
  '<b>Dan</b> has code 2 and was in the boiler room at 02:12 (B03, C06).',
  '<b>Tom</b> walked past the hall at half past two – after the case was closed again (B05).',
  '<b>Zac</b> was online in the staff room (B06), and <b>Grace</b> doesn’t know the code (C04).',
  '<b>Dr Lane</b> was at home; the front door was not opened (C05). The fudge crumbs prove nothing – everyone had fudge (A06, C04).',
 ],
 'fairness' => 'The fudge crumbs, the dad with a torch and the gamer awake in the night are all red herrings. The case sensor, the key box code and the empty sleeping bag point to one person.',
];
