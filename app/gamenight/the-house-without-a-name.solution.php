<?php
// SPOILERS. Answer key and solution text for The House Without a Name.
return [
 'culprit' => 'niels-vang',
 'lookup' => 'b',
 'card' => 'c',
 'motive' => 'b',
 'evidence' => ['S01', 'S05', 'B01', 'B02', 'B03', 'B04', 'B06', 'C01', 'C02', 'C04'],
 'summary' => [
  'The man behind the postcard is <b>Niels Vang</b>, the family’s former security contact. He still had access to service account <b>KV-14</b> until the end of February, and on 6 February at 14:11 he used his firm’s laptop <b>NV-04</b> to open the family’s historic case file and see their new address.',
  'On 5 February an anonymous account registered with his firm’s email domain had been created; on 7 February it wrote to Freja. On 8 February his firm ordered and paid for postcard <b>614</b> with a picture of the family’s old house, posted through Aalborg on 9 February. That same evening, at 18:50, he wrote a 145,000 kr. ‘security package after suspicious incidents’ – before the family had even received the card.',
  'His firm was short of money and he had promised the bank an ‘expected large private client’. His own draft says it plainly: if the family believed Jorgen Sahl had found them, Thomas would pay for protection. When Thomas refused, the invoice was cancelled and the anonymous messages stopped.',
 ],
 'conclusions' => [
  ['Only the contact function may link old and new identities.', 'S05'],
  ['The protected address was opened on KV-14 from NV-04 – Niels’s account and his firm’s laptop.', 'B01, B02, B03'],
  ['The card’s control number 614 is a print order paid by NV Beredskab.', 'S01, B04'],
  ['The account that wrote to Freja was registered with NV Beredskab’s domain.', 'B06'],
  ['The sales offer was written before the card was even posted.', 'C01'],
  ['Niels needed money and planned to use the family’s fear of Sahl.', 'C02, C04'],
 ],
 'timeline' => [
  ['1 Feb', 'Niels applies for credit: ‘expected large private client’', 'C02'],
  ['5 Feb', 'Anonymous account created with an NV Beredskab email', 'B06'],
  ['6 Feb, 14:11', 'KV-14 opens the family’s file from NV-04', 'B01, B03'],
  ['6 Feb, 14:18', 'Draft email: ‘Thomas will pay for the protection’', 'C04'],
  ['7 Feb', 'Message to Freja: ‘What were you called before?’', 'S03, B06'],
  ['8 Feb, 18:32', 'Postcard 614 ordered, paid by NV Beredskab', 'B04'],
  ['8 Feb, 18:50', 'Niels writes the 145,000 kr. offer', 'C01'],
  ['9 Feb', 'Card postmarked in Aalborg', 'S01, B04'],
  ['10 Feb', 'Thomas phones Niels: ‘Don’t overreact’; the offer is sent', 'S06, C01'],
  ['12 Feb', 'Thomas refuses; invoice cancelled; messages stop', 'C05'],
 ],
 'others' => [
  '<b>Jorgen Sahl</b> is a believable threat from the past, but he was abroad and nothing links him to the order or the lookup (C03).',
  '<b>Camilla</b> found the current house through a public sale, never the old names – and her photo is from 11 February, after the card (S04, B07).',
  '<b>Freja</b> was the target of the messages, not their sender (S03, B06).',
  '<b>Maja and Thomas</b> are the people being frightened; the lookup, the laptop and the payment all lead to Niels’s firm (B01–B04).',
 ],
 'fairness' => 'A photo of an old house proves nothing on its own. The case is built on small, boring numbers – the KV-14 lookup, terminal NV-04, control number 614 – plus a sales offer dated before the threat arrived.',
];
