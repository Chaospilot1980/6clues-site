<?php
// SPOILERS. Answer key and solution text for The Other Name. Only loaded server-side to score an accusation or after the reveal.
return [
 'culprit' => 'martin-holm',
 'sender' => 'b',
 'past' => 'c',
 'next' => 'd',
 'evidence' => ['S-03', 'S-04', 'B-01', 'B-03', 'B-05', 'B-07', 'C-02', 'C-04', 'C-05', 'C-06'],
 'summary' => [
  'Liv is <b>Anna Holm</b>. In February she went to the Havblik crisis centre with her son Elias to get away from a controlling and threatening marriage. On 2 March, at her own request, Elias was placed safely with an approved carer. That evening she locked her red raincoat, Elias’s drawing and a USB stick with her evidence in locker 218 at Linde bus terminal, and took the 21:40 bus towards Sundby. She was found on the quay the next morning with a concussion and no memory.',
  'Martin hired private investigator <b>Mikkel Gade</b> on 5 March to find her. Mikkel tried locker 218 on 10 March without success and called Havblik, but was told nothing. In October Martin gave Mikkel a photo from Anna’s old cloud album – taken at the crisis centre’s yellow gate on 1 March – and told him to “make her unsure” and “remind her of the boy”. Mikkel ordered the print with the words YOU PROMISED TO COME BACK and posted it from Linde. Martin approved the invoice.',
  'A marriage certificate gives Martin no right to take Anna anywhere. The right ending is not to hand her back, but to contact Ada and the social worker, keep her address secret and let Anna choose for herself – as she writes in her own note.',
 ],
 'conclusions' => [
  ['The bus ticket and key 218 tie Liv to Linde and a locker she locked herself on 2 March.', 'S-03, S-04, B-01'],
  ['The locker, the admission note and her own text file show that Anna planned to leave Martin and made Elias safe.', 'B-02, B-03, B-05'],
  ['The yellow gate is at the crisis centre, not at Martin’s home – the photo was taken on 1 March.', 'C-02'],
  ['Mikkel ordered and posted the photo, and billed Martin for it.', 'B-07, C-05'],
  ['Martin told Mikkel to frighten her into coming home.', 'C-06'],
  ['Anna is an adult; any contact goes through the social worker, and she has said what she wants.', 'C-04, C-07'],
 ],
 'timeline' => [
  ['21–27 Feb', 'Anna records three conversations as evidence', 'C-01'],
  ['27 Feb', 'Anna and Elias arrive at Havblik', 'B-03'],
  ['1 Mar', 'Visiting day: photo at the yellow gate; Elias’s drawing', 'C-02, B-04'],
  ['2 Mar · 19:12', 'Anna writes the text file on the USB stick', 'B-05'],
  ['2 Mar · 20:14', 'Last call between Ada and Anna', 'B-06'],
  ['2 Mar · 20:56', 'Locker 218 locked by a woman in a red raincoat', 'B-01'],
  ['2 Mar · 21:18–21:40', 'Bus ticket bought; bus leaves Linde towards Sundby', 'S-03'],
  ['3 Mar · 05:42', 'Found on the ferry quay in Sundby with no memory', 'S-01, S-02'],
  ['5 Mar', 'Martin hires Mikkel to “locate his spouse”', 'B-07'],
  ['10 Mar · 10:49–11:19', 'Mikkel parks at Linde terminal, fails to open locker 218, calls Havblik', 'B-01, B-06, B-07'],
  ['18 Oct', 'Martin: “Make her unsure.” Mikkel orders the print', 'C-05, C-06'],
  ['19–20 Oct', 'Envelope posted from Linde; it reaches the guesthouse', 'S-05, S-06'],
 ],
 'others' => [
  '<b>Jonas</b> is suspicious of Liv, but nothing links him to the photo – the print was ordered and paid for by Mikkel (C-05).',
  '<b>Signe</b> took Liv in and only received the envelope (S-06).',
  '<b>Ada</b> helped Anna escape and tried to find her; she never knew where Anna was (B-06, C-03).',
  '<b>Liv</b> is Anna – the person the photo was meant to frighten, not its sender (C-05, C-07).',
  '<b>Mikkel</b> ordered and posted the photo, but he did it on Martin’s instructions and for Martin’s money (B-07, C-06). That is why Martin is the one behind it.',
 ],
 'fairness' => 'Memory loss proves nothing on its own, and the camera never shows a face. The case rests on the paper trail: the ticket and key, the locker contents in Anna’s own words, the invoice and print order, and Martin’s messages.',
];
