<?php
// SPOILERS. Answer key and solution text for The Glass Wall.
return [
 'culprit' => 'sara-munk',
 'where' => 'b',
 'trace' => 'b',
 'hide' => 'c',
 'evidence' => ['A02', 'A03', 'A05', 'B01', 'B02', 'B03', 'B04', 'B05', 'C01', 'C02', 'C03', 'C06'],
 'summary' => [
  'The thief is <b>Sara Munk</b>, the conservator. She received box T12 with the original at 13:54 and was alone in the workshop until 15:33. There she swapped the sculpture for the approved copy, which weighs only 1,005 g.',
  'To hide the swap she signed a false condition report at 15:21 (‘blue thread verified’) with a photo from the week before. T12 left with the copy, and Lena unknowingly put the copy into case M4 at 16:12. Jonas’s photo at 16:24 already shows the matt scratch – so the reception and the alarm were never part of it.',
  'The original left the workshop on the same trolley at 15:39, in an extra box marked <b>RETURN FILTER</b>. Sara then had it moved to depot D2 with an email saying it must not be opened before Monday. The box weighed 2,790 g – exactly 950 g of box and filter plus the original’s 1,840 g – and that is where the police found it.',
 ],
 'conclusions' => [
  ['The copy was already in the case at 16:24, and the case was not opened again.', 'A03, A05'],
  ['T12 left the workshop with 1,005 g inside – the copy.', 'B01, B02'],
  ['Only Sara had the box, a key and the workshop between 13:54 and 15:33.', 'B03, B04'],
  ['Sara’s condition report was false and used an old photo.', 'B05'],
  ['RETURN FILTER held exactly 1,840 g extra and was sent and hidden on Sara’s instructions.', 'C01, C02, C03'],
  ['The original was found in RETURN FILTER.', 'C06'],
 ],
 'timeline' => [
  ['09:05', 'Original weighed in T12: 7,440 g', 'B01'],
  ['13:54', 'Sara receives T12 in the workshop', 'B04'],
  ['15:21', 'Sara signs a false condition report', 'B05'],
  ['15:33', 'T12 leaves with the copy', 'B04'],
  ['15:39', 'Extra box RETURN FILTER leaves with the original', 'C01'],
  ['15:46', 'T12 weighed: 6,605 g (copy)', 'B01'],
  ['16:12–16:28', 'Lena puts the copy in case M4', 'A03'],
  ['16:24', 'Jonas photographs the copy', 'A05'],
  ['18:31', 'RETURN FILTER moved to depot D2 on Sara’s email', 'C02'],
  ['20:17', 'The copy is discovered', 'A01'],
 ],
 'others' => [
  '<b>Lena</b> opened the case legitimately at 16:12 – but T12 already held the copy at 15:46 (A03, B01).',
  '<b>Emil</b>’s key was sealed from 11:10 to 17:20, and he was not let into the workshop (B03, B04).',
  '<b>Bo</b> broke the seal at 17:20, long after the swap (B03).',
  '<b>Nadia</b> wanted a private viewing, but her phone first appears in reception at 19:22 (B06).',
  '<b>Jonas</b> only photographed the object at 16:24 – his photo is what proves the copy was already there (A05).',
 ],
 'fairness' => 'Nobody saw the swap. The case rests on simple arithmetic – the box weights – combined with the key and workshop logs, the false report and the extra box that held exactly the missing 1,840 g.',
];
