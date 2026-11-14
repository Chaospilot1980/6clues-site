<?php
// SPOILERS. Answer key and solution text for False Signal. Only loaded server-side to score an accusation or after the reveal.
return [
 'culprit' => 'ida-kragh',
 'access' => 'b',
 'owner' => 'c',
 'motive' => 'b',
 'evidence' => ['A04', 'B01', 'B02', 'B03', 'B04', 'B05', 'C01', 'C02', 'C03', 'C05', 'C06'],
 'summary' => [
  'The person who put the fake QR code on air is <b>Ida Kragh</b>, the broadcast producer. At 19:36 she opened a remote session to STUDIO-02 from her own tablet, <b>PROD-TAB7</b>. At 19:41 she cloned the approved graphic V4 into V5 and changed only the QR target to the fake page, and at 19:48 she approved it. Auto-play then sent V5 out at its scheduled time, 20:12.',
  'Ida says the tablet lay on the table in the production room while she was at the stage. But between 19:35 and 19:52 nobody swiped into that room – and at 19:51 her task was ticked off <b>from PROD-TAB7</b>, a minute before she swiped back in. She had the tablet with her. Her unsent note at 19:44 states the plan: show the fake page live, expose Mikkel, remove V5 straight after.',
  'The fake page and its account belong to <b>Mikkel Roed</b>: Event Services Ltd was registered six weeks earlier with him as the only representative. That makes him responsible for a prepared fraud attempt – but he never touched the broadcast. Ida chose a reckless way to expose him, and real donors were sent to the fake page.',
 ],
 'conclusions' => [
  ['Nothing was hacked: the overlay changed from V4 to V5 while the video and the foundation’s systems ran normally.', 'A01, A03, A04'],
  ['V5 was made by hand on STUDIO-02 under a shared account; auto-play only played it.', 'B01, B02, C02'],
  ['The only remote session to STUDIO-02 came from PROD-TAB7, which is registered to Ida.', 'B03, B04'],
  ['Ida’s ‘tablet on the table’ story fails: no one else entered the room, and the tablet ticked off her task at 19:51 while she was outside.', 'B05, B06, C01'],
  ['Ida’s own note and chat show the plan to expose Mikkel live.', 'C05, C06'],
  ['Mikkel owns the fake page and account, but had no access to the broadcast.', 'C03, C04'],
 ],
 'timeline' => [
  ['18:20', 'Mikkel drafts (but never sends) ‘no live changes without approval’', 'C04'],
  ['18:33–18:37', 'Ida asks Mikkel about his page; he says it’s a test', 'C05'],
  ['19:31–19:35', 'Ida in the production room', 'B05'],
  ['19:36', 'Remote session from PROD-TAB7 to STUDIO-02 opens', 'B03'],
  ['19:41', 'V5 created with the fake QR target', 'B01, C02'],
  ['19:44', 'Note on the tablet: ‘Show the fake page live…’', 'C06'],
  ['19:48', 'V5 approved', 'B01'],
  ['19:50', 'Remote session closes', 'B03'],
  ['19:51', 'Ida’s task ticked off from PROD-TAB7 – she is still outside', 'C01, B05'],
  ['19:52', 'Ida swipes back into the production room', 'B05'],
  ['19:55', 'Ida to Mikkel: ‘I’ve made sure we’ll get proof tonight.’', 'C05'],
  ['20:12', 'Auto-play sends V5 live', 'A04, B01'],
  ['20:27–20:30', 'The foundation notices; the overlay is taken off air', 'A01'],
 ],
 'others' => [
  '<b>Mikkel</b> set up the fake page and its account (C03) – a serious matter – but he had no card swipe, no device on the production network and no part in sending V5 live.',
  '<b>Theo</b> has no STUDIO-02 access and only entered the tech room at 20:04, after the session had ended (B05, B06). The shared ‘graphics-service’ name is not evidence against him.',
  '<b>Sofie, Malik and Eva</b> have no access to the graphics system; Eva’s volunteer account was closed in March (B02).',
 ],
 'fairness' => 'The account name ‘graphics-service’ proves nothing on its own. The case rests on the remote session from PROD-TAB7, the tablet’s registration, the complete door log, the task ticked off from the tablet while Ida was outside, and her own note.',
];
