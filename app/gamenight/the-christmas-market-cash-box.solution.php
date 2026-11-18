<?php
// SPOILERS. Answer key and solution text for The Christmas Market Cash Box.
return [
 'culprit' => 'harry-knight',
 'when' => 'b',
 'how' => 'b',
 'motive' => 'b',
 'evidence' => ['A01', 'A02', 'A05', 'B01', 'B02', 'B03', 'B04', 'B05', 'C01', 'C02', 'C03', 'C05', 'C06'],
 'summary' => [
  'The thief is <b>Harry Knight</b>, the market’s Santa. The cash box was counted at 18:30, and the cabin opened only once before 19:15 – from 18:42 to 18:45, with the code.',
  'Four people knew the code. Maggie was on stage with the microphone, Noah was selling tickets at the gate and Raj was moving a van in the car park. Harry claims he never left the grotto, but he put up a “feeding the reindeer” sign from 18:35 to 18:52, and Elsa saw Santa heading for the cabins with his sack at about 18:40.',
  'Charity money bands – which exist only inside the cash box – were found in Santa’s sack. Harry was £2,900 behind with his rent and faced eviction on Monday.',
 ],
 'conclusions' => [
  ['The cabin opened only at 18:42–18:45.', 'A01, A02'],
  ['Only four people knew the code.', 'A05'],
  ['Maggie, Noah and Raj have alibis at 18:42.', 'B01, B02, B03'],
  ['Santa left the grotto at that exact time and lied about it.', 'B04, B05, C01, C06'],
  ['The charity bands were in his sack; his rent was due.', 'C02, C03, C05'],
 ],
 'timeline' => [
  ['18:30', 'Maggie counts £8,200 and locks the cabin', 'A01'],
  ['18:30', 'Carols begin; Maggie on stage', 'B01'],
  ['18:35', 'Santa puts up the reindeer sign', 'B04, C06'],
  ['18:40', 'Elsa sees Santa heading for the cabins', 'B05'],
  ['18:42–18:45', 'Cabin opened with the code', 'A02'],
  ['18:52', 'Santa back in the grotto', 'B04'],
  ['19:15', 'Maggie finds the box gone', 'A01'],
 ],
 'others' => [
  '<b>Noah</b> is short of money, but sold tickets at 18:41 and 18:44 (B02, C04).',
  '<b>Raj</b> was in the car park, confirmed by camera (B03).',
  '<b>Lucy</b> has an old rumour against her but was conducting in front of the town – and never had the code (B06, A05).',
  '<b>Elsa</b> was serving at her stall all evening (B05), and <b>Maggie</b> was on stage (B01).',
 ],
 'fairness' => 'The student assistant with no money looks like the obvious suspect. The gate till clears him, and the grotto booking list shows a gap in Santa’s alibi exactly when the cabin opened.',
];
