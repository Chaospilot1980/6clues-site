<?php
// SPOILERS. Answer key and solution text for The Silent Stradivarius.
return [
 'culprit' => 'oskar-dahl',
 'when' => 'b',
 'how' => 'b',
 'motive' => 'b',
 'evidence' => ['A02', 'A03', 'A04', 'B01', 'B02', 'B03', 'B04', 'C01', 'C02', 'C03', 'C04', 'C05'],
 'summary' => [
  'The thief is <b>Oskar Dahl</b>, Ana’s agent. The real Aurora has a small chip on its scroll; it is there in the photo at 20:03 and gone at 20:41. The swap happened during the interval.',
  'At 20:11 dressing room 4 was opened with <b>artist pass 2</b>, signed out by Oskar, while Ana was live on radio upstairs. Only Ana and Oskar knew the case combination. Oskar claims he lent his pass to Felix Brandt – but Felix was paying at the bar at 20:10 and stood beside Clara Voss until 20:24.',
  'The copy came from Felix’s workshop: Oskar ordered an “exact copy” and collected it the day before the concert. A collector in Geneva had offered him €1.5 million, “no questions”, knowing about his problems with the bank.',
 ],
 'conclusions' => [
  ['The Aurora was genuine until the interval; the copy lacks the chip.', 'A02, A03, A04'],
  ['Room 4 was opened with Oskar’s pass while Ana was on air.', 'B01, B02, B03'],
  ['Only Ana and Oskar knew the case combination.', 'B04'],
  ['Oskar’s story about lending his pass collapses at the bar.', 'C01, C02, C03'],
  ['He ordered the copy and had a buyer waiting.', 'C04, C05'],
 ],
 'timeline' => [
  ['October', 'Oskar orders an exact copy from Felix Brandt', 'C04'],
  ['Thursday', 'Oskar collects the copy', 'C04'],
  ['18:30', 'Curator checks the genuine Aurora – chip present', 'A02'],
  ['20:03', 'Photo: chip on the scroll', 'A03'],
  ['20:08', 'Ana goes on air in the green room', 'B03'],
  ['20:11–20:14', 'Artist pass 2 opens room 4', 'B01'],
  ['20:19', 'Oskar orders champagne at the bar', 'C02'],
  ['20:41', 'Photo: no chip – the copy is on stage', 'A03'],
 ],
 'others' => [
  '<b>Mei Lin</b> was in corridor B, but her pass opened only room 5 (B01, B05).',
  '<b>Jonas</b> had the master key, but it was never used (B01, B06).',
  '<b>Felix</b> made the copy, but in good faith, and was at the bar with Clara during the swap (C03).',
  '<b>Clara</b> gains nothing from a theft (C06), and <b>Ana</b> was live on radio (B03).',
 ],
 'fairness' => 'The violin maker looks guilty because he made the copy, but the bar till and Clara give him an alibi for 20:11. The chip dates the swap, the door log names the pass, and the bar till breaks the only story that could explain it away.',
];
