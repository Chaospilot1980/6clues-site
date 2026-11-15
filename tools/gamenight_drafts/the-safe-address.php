<?php
// Game Night case 015: The Safe Address. Server-side only. Adapted from the 6CLUES premium beta set (2026).
return [
  "slug" => 'the-safe-address',
  "no" => '015',
  "title" => 'The Safe Address',
  "tagline" => '“I know who you are.” A family in hiding is told to run. Should they?',
  "teaser" => 'A family has lived under protected names on a Swedish island for eight years. Then a postcard arrives – and their protection officer orders them onto a boat at once.',
  "genre" => 'Betrayal',
  "level" => 1,
  "minutes" => [60, 90],
  "players" => [2, 6],
  "revision" => '1.0',
  "caseref" => 'VIK-0914',
  "stamp" => 'EXPOSED',
  "envelope" => '#D8C7B2',
  "flap" => '#BCA68C',
  "cover" => [
   "file" => 'the-safe-address/cover.jpg',
   "prompt" => 'Red wooden Swedish cottage on a rocky island at dusk, warm light in two windows, a Swedish flag on a pole, calm grey sea and pine trees, quiet tension, no people, no text, 4:3',
  ],
  "intro" => ['For eight years Eva, Jonas and Klara Lind have lived under protected names on the fictional island of <b>Vikskär</b> in the Swedish archipelago, after Jonas testified against a fraud network.', 'On 14 September a postcard arrives: <i>“So it is true. I know who you are.”</i> Hours later their protection officer, <b>Henrik Nordin</b>, orders an emergency move – a private boat from the west pier at 18:00, phones off, no calls to head office.', 'Klara notices the instructions don’t match the rules they were taught. Who exposed the safe address, why was the family told to run – and who can they trust?'],
  "mission" => ['Find out who sent the postcard.', 'Explain why the family was ordered onto the boat.', 'Decide who can be trusted.', 'Back up your accusation with at least three document numbers.'],
  "questions" => ['What do the relocation rules say?', 'Did head office order the move?', 'Who paid to deliver the postcard?', 'Where was the boat really going?', 'Where do the words on the postcard come from?', 'Who stood to gain from moving the family?'],
  "suspects" => [[
    "id" => 'eva-lind',
    "name" => 'Eva Lind',
    "role" => 'Mother (protected identity)',
   ], [
    "id" => 'jonas-lind',
    "name" => 'Jonas Lind',
    "role" => 'Father (protected identity)',
   ], [
    "id" => 'klara-lind',
    "name" => 'Klara Lind',
    "role" => 'Daughter',
   ], [
    "id" => 'henrik-nordin',
    "name" => 'Henrik Nordin',
    "role" => 'Protection officer',
   ], [
    "id" => 'sofia-berg',
    "name" => 'Sofia Berg',
    "role" => 'Neighbour',
   ]],
  "packets" => [
   "START" => [
    "label" => 'Envelope A',
    "docs" => ['E01', 'E02', 'E03', 'E04', 'E05'],
   ],
   "B" => [
    "label" => 'Envelope B',
    "when" => 'you have found where Henrik’s orders break the rules',
    "docs" => ['E06', 'E07', 'E08', 'E09', 'E10'],
   ],
   "C" => [
    "label" => 'Envelope C',
    "when" => 'you know who paid for the postcard',
    "docs" => ['E11', 'E12', 'E13', 'E14', 'E15'],
   ],
  ],
  "docs" => [
   "E01" => [
    "kind" => 'report',
    "title" => 'Protected residence brief',
    "meta" => 'Restricted · 12 September',
    "body" => '<p>Eva, Jonas and Klara Lind live on Vikskär under protected names. They were moved there after Jonas testified against an organised fraud network eight years ago.</p><p class="note">Two-person verification is mandatory for any emergency relocation.</p>',
   ],
   "E02" => [
    "kind" => 'photo',
    "title" => 'Anonymous postcard',
    "meta" => 'Delivered 14 September',
    "body" => '<p>“So it is true. I know who you are.” No signature. Postmark from a sorting centre on the mainland.</p><p class="note">On the back: a smear of violet ink near the stamp.</p>',
    "img" => [
     "file" => 'the-safe-address/postcard.jpg',
     "caption" => 'The postcard, front',
     "prompt" => 'Vintage-style postcard on a wooden table, handwritten message in black ink, a smear of violet ink near the stamp, soft window light, no readable text',
    ],
   ],
   "E03" => [
    "kind" => 'report',
    "title" => 'Standing relocation protocol',
    "meta" => 'Issued 2 January',
    "body" => '<ol><li>Call the published duty line.</li><li>Get confirmation from the case officer.</li><li>Confirm a separate phrase with a <b>second officer</b>.</li></ol><p class="note">Families must never board a vehicle arranged only through one officer’s personal phone.</p>',
   ],
   "E04" => [
    "kind" => 'messages',
    "title" => 'Henrik’s text',
    "meta" => '14 September, 15:08',
    "body" => '<div class="chat"><p class="msg in"><span>Henrik → Lind family</span>Your location is burned. Take the 18:00 private launch from the west pier. No time for two-person verification. Do not call central; the network is compromised. Keep phones off.</p></div>',
   ],
   "E05" => [
    "kind" => 'log',
    "title" => 'Official duty desk record',
    "meta" => '14 September, 15:12',
    "body" => '<ul class="plain"><li>No emergency move authorised for the Lind family.</li><li>No compromise of the central network reported.</li><li>No information about an 18:00 boat.</li><li>Henrik Nordin has not logged a verified incident.</li></ul>',
   ],
   "E06" => [
    "kind" => 'interview',
    "title" => 'Interview: Eva Lind',
    "meta" => '14 September',
    "body" => '<p>“We were told never to move on a single message. Henrik got angry when I asked for the second officer.”</p><p>“Jonas said Henrik had always kept us safe, but Klara said the whole thing was wrong.”</p>',
   ],
   "E07" => [
    "kind" => 'photo',
    "title" => 'Neighbour’s delivery photo',
    "meta" => 'Sofia Berg · 14 September, 10:44',
    "body" => '<p>The shared security camera shows a uniformed courier putting the postcard in the family’s postbox. The courier’s ID code belongs to a commercial delivery service.</p><p class="note">There is no sign of anyone entering the house.</p>',
   ],
   "E08" => [
    "kind" => 'audit',
    "title" => 'Postage purchase trace',
    "meta" => 'Commercial courier · 13 September',
    "body" => '<p>A delivery order for one postcard was billed to <b>NORDIN FIELD SERVICES</b> – Henrik’s registered consultancy – under reference NFS-220.</p><p class="note">Paid with a company card.</p>',
   ],
   "E09" => [
    "kind" => 'log',
    "title" => 'Private boat booking',
    "meta" => 'Harbour master · 14 September',
    "body" => '<p>The 18:00 boat from the west pier was booked by “Nordin Field Services” to take three passengers to an <b>industrial quay on the mainland</b> – not the official reception station.</p><p class="note">The boat operator has no contract with the protection service.</p>',
   ],
   "E10" => [
    "kind" => 'note',
    "title" => 'Klara’s journal',
    "meta" => 'Recovered · 8 September',
    "body" => '<p>The line “I know who you are” appears in a story Klara drafted for school.</p><p class="note">Henrik saw that exact line on a page left open during a safety inspection on 9 September. The wording may have been copied to frighten the family.</p>',
   ],
   "E11" => [
    "kind" => 'audit',
    "title" => 'Collection notice',
    "meta" => '11 September',
    "body" => '<p>Henrik Nordin’s consultancy had unpaid debts – and a promised six-figure payment from a company linked to a former associate of the fraud network.</p><p class="note">Condition for payment: “successful transfer of dependents”.</p>',
   ],
   "E12" => [
    "kind" => 'interview',
    "title" => 'Interview: Henrik Nordin',
    "meta" => '14 September',
    "body" => '<p>“I used my consultancy because the normal booking system was slow. Central was compromised.”</p><p>“The postcard came from the criminal network. I can’t give you the second officer’s name.”</p>',
   ],
   "E13" => [
    "kind" => 'note',
    "title" => 'Jonas’s hidden letter',
    "meta" => 'Found in a lockbox',
    "body" => '<p>Jonas kept an unopened apology letter from an old associate, never shown to the family. It contains no current address and no link to the postcard.</p><p class="note">Jonas hid it because he was afraid of bringing old loyalties into the home.</p>',
    "img" => [
     "file" => 'the-safe-address/lockbox.jpg',
     "caption" => 'Jonas’s lockbox',
     "prompt" => 'Illustration: Jonas’s lockbox, film-noir evidence photo, no text',
    ],
   ],
   "E14" => [
    "kind" => 'log',
    "title" => 'Secure duty callback',
    "meta" => '14 September, 16:21',
    "body" => '<p>A second officer independently confirms the authorised plan: stay where you are until vetted transport at 09:00 tomorrow, from the north pier, only after two-person verification.</p><p class="note">Henrik’s 18:00 boat must not be used.</p>',
   ],
   "E15" => [
    "kind" => 'report',
    "title" => 'Transaction freeze notice',
    "meta" => '15 September',
    "body" => '<p>Nordin Field Services’ boat booking and the related payment have been frozen pending investigation.</p><p class="note">The family stayed at their safe address until a verified transfer. Nobody boarded Henrik’s boat.</p>',
   ],
  ],
  "checkpoints" => [
   "A" => [
    "title" => 'How did the postcard arrive?',
    "prompt" => 'Henrik says the address is burned and the family must leave now. Do his orders follow the rules?',
    "gate" => [
     "q" => 'What does the protocol demand before any emergency move?',
     "choices" => ['Only the case officer’s order', 'A duty-line call and confirmation by a second officer', 'Leaving within one hour'],
     "answer" => 1,
     "ok" => 'Exactly – and Henrik refused both. The duty desk knows nothing. Open envelope B.',
    ],
    "hints" => ['Compare Henrik’s text with the written relocation protocol.', 'What did the duty desk say four minutes after the text?'],
   ],
   "B" => [
    "title" => 'Who sent the postcard?',
    "prompt" => 'The postcard came by courier. Who paid for it – and where was the boat going?',
    "gate" => [
     "q" => 'Who paid for the postcard delivery?',
     "choices" => ['The criminal network', 'Nordin Field Services – Henrik’s own company', 'Klara, as a prank'],
     "answer" => 1,
     "ok" => 'Yes – reference NFS-220, paid with his company card. Open envelope C.',
    ],
    "hints" => ['Who paid to deliver the anonymous postcard?', 'Where would the 18:00 boat have landed?'],
   ],
   "final" => [
    "title" => 'The accusation',
    "prompt" => 'Who exposed the family, why were they told to run – and who can they trust?',
    "hints" => ['Follow the boat’s destination and the consultancy payment.', 'E08 + E09 + E11 show plan and motive; E10 explains the words.'],
   ],
  ],
  "accuse" => [
   "culprit_q" => 'Who betrayed the family?',
   "wrong" => 'That’s not the person who betrayed the Linds.',
   "items" => [
    "postcard" => ['The postcard', 'Where did the postcard come from?', 4],
    "boat" => ['The boat', 'What was the 18:00 boat for?', 4],
    "trust" => ['Trust', 'What should the family do?', 3],
   ],
  ],
  "choices" => [
   "postcard" => [
    "a" => 'From the old fraud network, which had found them.',
    "b" => 'Henrik arranged it through his own company, copying a line he had seen in Klara’s journal.',
    "c" => 'Klara sent it as a joke.',
    "d" => 'From Jonas’s old associate.',
   ],
   "boat" => [
    "a" => 'An official, approved emergency move.',
    "b" => 'To take the family to an unofficial quay, for money promised by a former associate of the fraud network.',
    "c" => 'A holiday trip Henrik had planned.',
    "d" => 'To bring the second officer to the island.',
   ],
   "trust" => [
    "a" => 'Follow Henrik’s instructions at once.',
    "b" => 'Follow the official protocol with two-person verification – and stay put until then.',
    "c" => 'Flee on their own without telling anyone.',
    "d" => 'Contact the fraud network to negotiate.',
   ],
  ],
  "worksheet" => ['What happened?', 'Who was responsible – and what was the motive?', 'Which documents prove it? Name at least three.', 'Which misleading explanation did you rule out, and why?', 'What should happen now?'],
  "solution_title" => 'Who really knew the safe address',
 ];
