<?php
// SPOILERS. Answer key and solution text for The Blue Folder. Only loaded server-side to score an accusation or after the reveal.
return [
 'culprit' => 'rikke-falck',
 'version' => 'b',
 'route' => 'c',
 'decoy' => 'b',
 'evidence' => ['A02', 'A04', 'B01', 'B02', 'B04', 'B05', 'B06', 'B07', 'C01', 'C02', 'C03', 'C05'],
 'summary' => [
  'The leak is <b>Rikke Falck</b>, head of compliance. The rival’s PDF has 17 pages, the ‘Kestrel-7 test cell’ footnote and fingerprint 8D42 – that is the compliance copy <b>VC4-42-A</b>, not the engineers’ 16-page file. At 19:48 Rikke exported exactly that version under her own user, hidden inside a ‘quarterly audit export’ booked in her calendar weeks earlier.',
  'At 20:06 a 17-page file went into the upload queue at CopyPoint for <b>RFalck Consulting</b>, collected at 20:29 under code K7 by ‘R. Falck’. The day before, RFalck Consulting had received 185,000 kr. from <b>Northcap Advisory</b> – adviser to Helion’s investor group – and at 22:08 Northcap thanked her for ‘the PDF/A version including the Kestrel note’. She never declared the paid work.',
  'The download from Nadia’s account at 21:13 was a decoy. It used test token T-19, which Rikke had kept alive without MFA under change request CR-118 against IT’s warning, and it came from the test sandbox set up in Rikke’s own department – while Nadia was on a video call. It fetched the 16-page file, which is not what leaked.',
 ],
 'conclusions' => [
  ['The leaked file is not the engineers’ file: different fingerprint, 17 pages and an extra footnote.', 'A02, B01'],
  ['That 17-page compliance version was exported by RFALCK at 19:48.', 'B02, B03'],
  ['The 21:13 ‘Nadia’ login was a token refresh from Rikke’s department’s sandbox, using a token Rikke kept alive.', 'A04, B04, B05, B06'],
  ['A 17-page file was printed and collected at CopyPoint for RFalck Consulting.', 'B07, C03'],
  ['Northcap, Helion’s investor adviser, paid Rikke and confirmed receiving the Kestrel version.', 'C01, C02, C05'],
  ['Rikke never declared the paid work.', 'C06'],
 ],
 'timeline' => [
  ['2 Sept', 'Rikke keeps test token T-19 alive (‘My responsibility’)', 'B04, B05'],
  ['14 Sept', 'Compliance version VC4-42-A (17 pages, Kestrel-7 footnote) created', 'B01'],
  ['15 Sept', 'Northcap pays RFalck Consulting 185,000 kr.', 'C01, C02'],
  ['16 Sept, 19:48', 'RFALCK exports VC4-42-A', 'B02, B03'],
  ['20:06', '17-page file uploaded to CopyPoint for RFalck Consulting', 'B07'],
  ['20:29', 'Code K7 collected by ‘R. Falck’', 'C03'],
  ['20:48–21:31', 'Nadia leaves, takes the bus and is on a video call', 'A03'],
  ['21:13', 'Token refresh as NADIA.L from the sandbox fetches the 16-page file', 'A01, A04, B06'],
  ['22:08', 'Northcap thanks Rikke for the Kestrel version', 'C05'],
  ['17 Sept, 09:00', 'Helion shows the design', 'A01'],
 ],
 'others' => [
  '<b>Nadia</b> was framed: the 21:13 login was a token refresh from a sandbox while she was on a video call, it fetched the 16-page file, and she had no access to the 17-page version (A03, A04, B01, C07).',
  '<b>Henrik</b> can read compliance/audit, but the export was made under RFALCK, and the print job, the payment and Northcap’s email all lead to Rikke (B02, B07, C01, C05).',
  '<b>Oskar</b> made a security mistake by not killing T-19, but he warned against it and cannot read the encrypted audit archive (A05, B05, C04).',
  '<b>Lea</b>’s 12-minute chat at a public conference happened a week earlier, and sales has no access to engineering or compliance files (A05, A07).',
  '<b>Emil</b> only has access to the marketing/launch material (A05).',
 ],
 'fairness' => 'No account name proves who sat at a keyboard, and the CopyPoint camera shows no face. The case rests on the exact file version, the export journal, the print order and payment to Rikke’s own company, Northcap’s thank-you email and the token Rikke kept alive.',
];
