<?php
// Game Night case 012: The Locked Terrace. Server-side only. Adapted from the 6CLUES premium beta set (2026).
return [
  "slug" => 'the-locked-terrace',
  "no" => '012',
  "title" => 'The Locked Terrace',
  "tagline" => 'A wife vanishes after a row. The terrace tells a story – but whose?',
  "teaser" => 'After a loud argument, Elena Ruiz disappears from her Seville apartment. Her husband shows the police a broken phone and a toppled planter on the terrace.',
  "genre" => 'Disappearance',
  "level" => 1,
  "minutes" => [60, 90],
  "players" => [2, 6],
  "revision" => '1.0',
  "caseref" => 'SEV-0424',
  "stamp" => 'MISSING',
  "envelope" => '#E3C9A8',
  "flap" => '#C9A57E',
  "cover" => [
   "file" => 'the-locked-terrace/cover.jpg',
   "prompt" => 'Night view of a Seville apartment terrace with wrought-iron railing, an overturned terracotta planter and spilled soil, warm street light below, orange trees, tense noir mood, no people, no text, 4:3',
  ],
  "intro" => ['On the evening of 24 April, neighbours in a Seville apartment block hear a loud argument. Soon after, <b>Mateo Ruiz</b> calls for help: his wife <b>Elena</b> has vanished. On the terrace he shows the police a cracked phone and an overturned planter.', 'A neighbour heard a metal door on the other side of the courtyard. And bank records suggest the argument was about much more than jealousy.', 'Did Elena leave of her own free will? Who staged the terrace – and what was the real money behind it all?'],
  "mission" => ['Find out what happened to Elena.', 'Explain who arranged the scene on the terrace, and when.', 'Uncover the real financial motive.', 'Back up your accusation with at least three document numbers.'],
  "questions" => ['What does the terrace really show?', 'Which door did someone use at 21:56 and 22:07?', 'Whose phone was lying on the terrace?', 'Where was Elena at 22:19?', 'Who tried to move 180,000 euros – and to whom?', 'Why does Elena not want her address shared?'],
  "suspects" => [[
    "id" => 'elena-ruiz',
    "name" => 'Elena Ruiz',
    "role" => 'Missing business owner',
   ], [
    "id" => 'mateo-ruiz',
    "name" => 'Mateo Ruiz',
    "role" => 'Husband',
   ], [
    "id" => 'carmen-salas',
    "name" => 'Carmen Salas',
    "role" => 'Elena’s sister',
   ], [
    "id" => 'rosa-ortega',
    "name" => 'Rosa Ortega',
    "role" => 'Neighbour',
   ], [
    "id" => 'lucia-vega',
    "name" => 'Officer Lucía Vega',
    "role" => 'First responder',
   ]],
  "packets" => [
   "START" => [
    "label" => 'Envelope A',
    "docs" => ['E01', 'E02', 'E03', 'E04', 'E05'],
   ],
   "B" => [
    "label" => 'Envelope B',
    "when" => 'you have found a contradiction between Mateo’s story and the neighbour’s',
    "docs" => ['E06', 'E07', 'E08', 'E09', 'E10'],
   ],
   "C" => [
    "label" => 'Envelope C',
    "when" => 'you know where Elena went',
    "docs" => ['E11', 'E12', 'E13', 'E14', 'E15'],
   ],
  ],
  "docs" => [
   "E01" => [
    "kind" => 'report',
    "title" => 'First-response report',
    "meta" => 'Seville · 24 April, 22:19',
    "body" => '<p>Officer Vega attended a report of a missing adult. Mateo Ruiz showed a cracked phone and a toppled planter on the terrace. The terrace door was closed but could be opened from inside.</p><p class="note">No blood and no signs of a fall were found.</p>',
   ],
   "E02" => [
    "kind" => 'photo',
    "title" => 'Terrace photo register',
    "meta" => 'Photo sheet · 22:25',
    "body" => '<table class="log"><tr><td>E1</td><td>Terrace door</td></tr><tr><td>E2</td><td>Black phone with cracked glass</td></tr><tr><td>E3</td><td>Overturned planter and loose soil</td></tr><tr><td>E4</td><td>Small smear of black paint on the inside threshold</td></tr></table><p class="note">The phone was not confirmed to belong to Elena.</p>',
    "img" => [
     "file" => 'the-locked-terrace/terrace.jpg',
     "caption" => 'Terrace, photo E3',
     "prompt" => 'Night photo of a tiled Seville terrace, an overturned terracotta planter with spilled soil and a cracked black phone lying on top of the soil, police evidence-photo style, no text',
    ],
   ],
   "E03" => [
    "kind" => 'interview',
    "title" => 'Statement: Mateo Ruiz',
    "meta" => '25 April, 00:10',
    "body" => '<p>“Elena shouted that she would take everything. She ran onto the terrace. When I came back at 22:05 she was gone.”</p><p>“I think she climbed over, or ran off to a lover. She took money from our company.”</p>',
   ],
   "E04" => [
    "kind" => 'interview',
    "title" => 'Statement: Rosa Ortega',
    "meta" => 'Neighbour · 25 April',
    "body" => '<p>“At 21:43 I heard arguing. Around 21:58 I heard the metal door of the service stairs on the other side of the courtyard.”</p><p>“At 22:09 someone dragged something heavy across the tiles. Mateo called for help after that.”</p>',
   ],
   "E05" => [
    "kind" => 'note',
    "title" => 'Elena’s safety plan',
    "meta" => 'Drafted 19 April',
    "body" => '<p class="handwriting">If I leave: use the rear service stairs, travel with Carmen, and do not tell Mateo where I am. I have told my lawyer the account access is restricted.</p>',
   ],
   "E06" => [
    "kind" => 'log',
    "title" => 'Key-card audit',
    "meta" => 'Building manager · 24 April',
    "body" => '<table class="log"><tr><td>21:56</td><td>Rear service stairs opened with resident code <b>ER-02</b> (Elena)</td></tr><tr><td>22:07</td><td>Same door opened with master code <b>MR-01</b> (Mateo)</td></tr></table><p class="note">Both events were logged locally on the door, not through an app.</p>',
   ],
   "E07" => [
    "kind" => 'report',
    "title" => 'Taxi receipt',
    "meta" => 'Licensed driver · 24 April',
    "body" => '<p>A taxi picked up Elena and Carmen in the rear street at <b>22:01</b> and dropped them at a private clinic at <b>22:19</b>.</p><p class="note">The driver’s licence record and a road-toll time confirm the journey.</p>',
   ],
   "E08" => [
    "kind" => 'medical',
    "title" => 'Clinic admission',
    "meta" => '24 April, 22:22',
    "body" => '<p>Elena attended with Carmen. She asked that her address not be given to her husband and that her visit be documented.</p><p class="note">The clinician noted that she was alert and fully able to choose where to stay.</p>',
   ],
   "E09" => [
    "kind" => 'lab',
    "title" => 'Phone ownership check',
    "meta" => 'Device serial reference',
    "body" => '<p>The phone found on the terrace was bought and registered by <b>Mateo Ruiz</b>. Elena’s own phone was later handed in by her lawyer.</p><p class="note">Mateo told the police the terrace phone was Elena’s.</p>',
    "img" => [
     "file" => 'the-locked-terrace/terrace-phone.jpg',
     "caption" => 'The phone found on the terrace',
     "prompt" => 'Illustration: The phone found on the terrace, film-noir evidence photo, no text',
    ],
   ],
   "E10" => [
    "kind" => 'audit',
    "title" => 'Bank security alert',
    "meta" => '23 April, 17:34',
    "body" => '<p>Elena’s company account reported a beneficiary change: <b>EUR 180,000</b> to a company called <b>SOLARIS OPERATIONS SL</b>. The change used Mateo’s administrator login MR-FIN.</p><p class="note">The transfer was held until the owner confirms it by phone.</p>',
   ],
   "E11" => [
    "kind" => 'messages',
    "title" => 'Email from Elena’s lawyer',
    "meta" => '24 April, 12:16',
    "body" => '<div class="chat"><p class="msg in"><span>Lawyer → Elena</span>Your audit has found a proposed unauthorised beneficiary change. Keep the records and avoid confronting anyone alone. The funds remain frozen. You may use the safety arrangements we discussed.</p></div>',
   ],
   "E12" => [
    "kind" => 'audit',
    "title" => 'Business ledger extract',
    "meta" => 'April · audit',
    "body" => '<p>SOLARIS OPERATIONS SL was set up recently, with <b>Mateo</b> as its only registered manager. It had no service contract with Elena’s company.</p><p class="note">The proposed payment was coded “consulting” with no matching invoice.</p>',
   ],
   "E13" => [
    "kind" => 'report',
    "title" => 'Police scene reconstruction',
    "meta" => '25 April, 11:00',
    "body" => '<p>Glass from the phone lay on top of the fresh soil – so the planter fell first. The phone’s last motion event was at <b>22:11</b>, after the taxi had left.</p><p class="note">The police cannot say who tipped the planter, but rule out that the phone fell while Elena was leaving.</p>',
   ],
   "E14" => [
    "kind" => 'interview',
    "title" => 'Statement: Carmen Salas',
    "meta" => '25 April',
    "body" => '<p>“I picked Elena up at the back door. She was frightened, but she knew exactly where she wanted to go. She did not take company money.”</p><p>“Mateo had threatened to report her missing if she exposed the transfer. We agreed not to share her new address.”</p>',
   ],
   "E15" => [
    "kind" => 'report',
    "title" => 'Welfare confirmation',
    "meta" => '27 April',
    "body" => '<p>Through an independent lawyer, Elena gave a signed statement that she is safe, does not wish to return to the apartment and does not consent to her location being shared with Mateo. The lawyer checked the signature against earlier documents.</p><p class="note">The statement does not say who disturbed the terrace.</p>',
   ],
  ],
  "checkpoints" => [
   "A" => [
    "title" => 'The terrace',
    "prompt" => 'Mateo says Elena ran onto the terrace and vanished. Does the evidence fit his story?',
    "gate" => [
     "q" => 'What did the neighbour hear at 21:58?',
     "choices" => ['Someone falling from the terrace', 'The metal door of the service stairs', 'Mateo calling for help'],
     "answer" => 1,
     "ok" => 'Exactly – a door on the other side of the courtyard, not the terrace. Open envelope B.',
    ],
    "hints" => ['Rebuild the timeline from 21:43 to 22:19 using only independent records.', 'Elena wrote a plan for leaving five days earlier. Which way out did she plan to use?'],
   ],
   "B" => [
    "title" => 'Where did Elena go?',
    "prompt" => 'Two key cards opened the service stairs that night. What happened between 21:56 and 22:19?',
    "gate" => [
     "q" => 'Whose phone was lying on the terrace?',
     "choices" => ['Elena’s', 'Mateo’s', 'Carmen’s'],
     "answer" => 1,
     "ok" => 'Yes – the “evidence” phone belongs to Mateo. Open envelope C.',
    ],
    "hints" => ['Check who owned the phone on the terrace.', 'Taxi, door log and clinic tell one story. Mateo tells another.'],
   ],
   "final" => [
    "title" => 'The accusation',
    "prompt" => 'What happened to Elena, who staged the terrace – and why?',
    "hints" => ['Compare the company that would receive the money with the company register.', 'E09 + E13 show when the terrace was arranged; E10 + E12 show why.'],
   ],
  ],
  "accuse" => [
   "culprit_q" => 'Who staged the terrace scene?',
   "wrong" => 'That’s not the person who arranged the terrace.',
   "items" => [
    "fate" => ['What happened to Elena', 'Where is Elena?', 4],
    "staging" => ['The staging', 'How was the terrace arranged?', 4],
    "motive" => ['The motive', 'What was the scene meant to hide?', 3],
   ],
  ],
  "choices" => [
   "fate" => [
    "a" => 'She fell from the terrace.',
    "b" => 'She was kidnapped by a stranger.',
    "c" => 'She left of her own free will with Carmen, by the service stairs, as she had planned.',
    "d" => 'She ran off with company money.',
   ],
   "staging" => [
    "a" => 'Elena dropped her phone as she climbed over the railing.',
    "b" => 'After Elena had left, Mateo tipped the planter and dropped his own phone on the soil.',
    "c" => 'Carmen arranged it to cover Elena’s escape.',
    "d" => 'The wind knocked the planter over.',
   ],
   "motive" => [
    "a" => 'Mateo’s attempt to move EUR 180,000 to his own company, SOLARIS.',
    "b" => 'Elena’s theft of company cash.',
    "c" => 'An insurance claim.',
    "d" => 'A dispute with the neighbour.',
   ],
  ],
  "worksheet" => ['What happened?', 'Who was responsible – and what was the motive?', 'Which documents prove it? Name at least three.', 'Which misleading explanation did you rule out, and why?', 'What should happen now?'],
  "solution_title" => 'What really happened on the terrace',
 ];
