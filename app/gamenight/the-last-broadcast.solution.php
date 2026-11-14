<?php
// SPOILERS. Answer key and solution text for The Last Broadcast. Only loaded server-side to score an accusation or after the reveal.
return [
 'culprit' => 'kasper-berg',
 'voice' => 'c',
 'where' => 'a',
 'what' => 'd',
 'evidence' => ['S-03', 'B-01', 'B-02', 'B-05', 'B-06', 'B-07', 'C-01', 'C-02', 'C-03', 'C-04'],
 'summary' => [
  'Vera Skov was never kidnapped. She recorded the message herself in edit suite 2 at 18:14, finished it at 22:39 and scheduled it at 22:42 to play automatically at 00:17. At 23:11 she left with a small suitcase, switched her phone off, took a taxi to the ferry quay and bought a ticket on the 00:35 overnight ferry with booking code <b>N-730</b>. The “meeting N. 07:30” was Nora, who flew over with the original documents.',
  'Her careless wording made the whole country fear the worst – but the real scandal was the one she was chasing. On 19 May, with <b>Kasper Berg</b>’s approval, an external communications firm replaced the foundation’s annual report online. The new version calls the 1.4 million kroner “advisory services”; the original said it went to Brask Holding ApS, a company owned by a board member.',
  'That is a documented manipulation of a public report that hid a possible conflict of interest. Whether it is also a crime is for the authorities to decide – but the person responsible for the cover-up is Kasper Berg.',
 ],
 'conclusions' => [
  ['Nobody entered the building at 00:17; the file was scheduled by Vera’s own user and played automatically.', 'S-03, B-01'],
  ['Vera recorded and edited the message herself before she left.', 'B-02, B-03'],
  ['N-730 is Vera’s ferry booking and her 07:30 meeting with Nora.', 'S-05, B-05, B-06, C-04'],
  ['Vera planned to disappear for a while and said so to Nora in advance.', 'C-03, C-06'],
  ['The web version of the annual report was changed to hide the payment to a board member’s company.', 'B-07, C-01'],
  ['The change was approved by Kasper Berg.', 'C-02'],
 ],
 'timeline' => [
  ['19 May · 15:32', 'Annual report replaced online, approved by Kasper Berg', 'C-02'],
  ['20 May · 18:14', 'Vera records the message in edit suite 2', 'B-02'],
  ['20 May · 19:04–19:12', 'Vera and Nora agree the plan and booking N-730', 'C-03, C-04'],
  ['20 May · 22:39–22:42', 'Vera finishes the file and schedules it for 00:17', 'B-01, B-02'],
  ['20 May · 23:11', 'Vera leaves by the main door with a suitcase', 'S-01, S-03'],
  ['20 May · 23:16', 'Her phone goes offline', 'S-06'],
  ['20 May · 23:24', 'Taxi to the ferry quay', 'B-04'],
  ['20 May · 23:29–23:58', 'Selma loads the night playlist – no changes to scheduled items', 'B-01, C-07'],
  ['20 May · 23:52', 'Ferry ticket bought, booking N-730', 'B-05'],
  ['21 May · 00:17', 'The message plays automatically', 'B-01, S-02'],
  ['21 May · 00:21', 'Vera photographed at the ferry kiosk', 'C-05'],
  ['21 May · 00:35', 'Ferry leaves for Osterby', 'B-05'],
 ],
 'others' => [
  '<b>Vera</b> staged a dramatic message, which was careless – but she covered nothing up; she was exposing the cover-up (C-03, C-06).',
  '<b>Nora</b> deleted a calendar entry to keep the meeting secret, not to hide a crime (B-06, C-04).',
  '<b>Selma</b> was in the building 23:29–23:58, but the playout log shows no changes to scheduled items, and the file was made on Vera’s profile (B-01, B-02).',
  '<b>Anton</b> wanted to avoid a legal fight, but has no access to the playout schedule (S-04, C-07).',
  '<b>Lukas</b> only saw Vera leave alone with her suitcase (S-01).',
 ],
 'fairness' => 'A voice on air proves nothing about where someone is, and the taxi driver and kiosk photo can’t identify a face. The answer rests on the playout log and metadata, the code N-730 across four documents, and the archive log that shows who approved changing the report.',
];
