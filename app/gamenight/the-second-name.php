<?php
// Game Night case 014: The Second Name. Server-side only. Adapted from the 6CLUES premium beta set (2026).
return [
  "slug" => 'the-second-name',
  "no" => '014',
  "title" => 'The Second Name',
  "tagline" => 'A woman with two names. One of them is a hiding place.',
  "teaser" => 'A confused woman with a head injury is found at Howrah Station in Kolkata. A kind couple calls her Mira Sen. The hospital calls her Anamika Roy. Someone wants to take her home.',
  "genre" => 'Identity',
  "level" => 1,
  "minutes" => [60, 90],
  "players" => [2, 6],
  "revision" => '1.0',
  "caseref" => 'KOL-0317',
  "stamp" => 'UNKNOWN',
  "envelope" => '#E6D0B8',
  "flap" => '#CDB08F',
  "cover" => [
   "file" => 'the-second-name/cover.jpg',
   "prompt" => 'Early-morning platform of a grand old railway station in Kolkata, mist, a lone brown handbag on a bench, warm amber light and deep shadows, a red stairwell in the background, mystery mood, no people, no text, 4:3',
  ],
  "intro" => ['At 06:15 on 17 March a confused woman with a head injury is found near platform 8 at Howrah Station in Kolkata. In her handbag: a brass key and a folded paper marked “Mira S.”', 'A kind couple, Harish and Lakshmi Sen, say they know her as <b>Mira Sen</b>. At the hospital she gives another name: <b>Anamika Roy</b>. A day later a notice appears claiming the Sens have kidnapped her.', 'Who is she, why did she leave – and who is trying to take control of her again?'],
  "mission" => ['Find out who the woman really is.', 'Explain what happened at the station.', 'Uncover who is trying to get her back – and how.', 'Back up your accusation with at least three document numbers.'],
  "questions" => ['Which name is her legal name?', 'Which papers were written before anyone reported a kidnapping?', 'Did she board the train?', 'Who followed her at the station?', 'Whose phone number is on the “missing” notice?', 'What does she want now?'],
  "suspects" => [[
    "id" => 'mira-sen',
    "name" => 'Mira Sen',
    "role" => 'Name used by the missing woman',
   ], [
    "id" => 'harish-sen',
    "name" => 'Harish Sen',
    "role" => 'School principal',
   ], [
    "id" => 'lakshmi-sen',
    "name" => 'Lakshmi Sen',
    "role" => 'Harish’s wife',
   ], [
    "id" => 'dev-mallick',
    "name" => 'Inspector Dev Mallick',
    "role" => 'Missing-persons investigator',
   ], [
    "id" => 'rhea-dutta',
    "name" => 'Dr Rhea Dutta',
    "role" => 'Neurologist',
   ], [
    "id" => 'kabir-roy',
    "name" => 'Kabir Roy',
    "role" => 'Anamika’s husband',
   ]],
  "packets" => [
   "START" => [
    "label" => 'Envelope A',
    "docs" => ['E01', 'E02', 'E03', 'E04', 'E05'],
   ],
   "B" => [
    "label" => 'Envelope B',
    "when" => 'you can separate her legal name from the name her helpers used',
    "docs" => ['E06', 'E07', 'E08', 'E09', 'E10'],
   ],
   "C" => [
    "label" => 'Envelope C',
    "when" => 'you know why she was at the station – and who followed her',
    "docs" => ['E11', 'E12', 'E13', 'E14', 'E15'],
   ],
  ],
  "docs" => [
   "E01" => [
    "kind" => 'report',
    "title" => 'Station discovery report',
    "meta" => 'Howrah · 17 March, 06:15',
    "body" => '<p>An adult woman was found confused near platform 8. She carried a brown handbag, a brass key and a folded paper marked “Mira S.” She had a minor head injury and no phone.</p><p class="note">A station employee called the hospital, not the police.</p>',
   ],
   "E02" => [
    "kind" => 'medical',
    "title" => 'Hospital intake',
    "meta" => '17 March, 07:25',
    "body" => '<p>Patient gives the name <b>Anamika Roy</b>, age 28. Staff note disorientation after a head injury. She keeps saying: “Do not contact Kabir.”</p><p class="note">Second entry: “Patient asks for a private room and an independent advocate.”</p>',
   ],
   "E03" => [
    "kind" => 'medical',
    "title" => 'Medical assessment',
    "meta" => 'Dr Rhea Dutta · 18 March',
    "body" => '<p>Symptoms fit a concussion with patchy memory. There is no reason to claim permanent memory loss, or that she cannot make her own choices.</p><p class="note">She understands a safety plan correctly when given simple options.</p>',
   ],
   "E04" => [
    "kind" => 'photo',
    "title" => 'Back of a photograph',
    "meta" => 'Found in the handbag',
    "body" => '<p>The photo shows Anamika next to a man at a family event. A crease hides part of his face.</p><p class="handwriting">Kabir and me, 2023. I was not smiling.</p>',
    "img" => [
     "file" => 'the-second-name/photograph.jpg',
     "caption" => 'Photograph from the handbag',
     "prompt" => 'Old creased family-event photograph lying on a wooden table: a young woman in a sari standing stiffly next to a man whose face is hidden by a deep crease in the print, warm faded colours, no text',
    ],
   ],
   "E05" => [
    "kind" => 'report',
    "title" => 'Legal aid complaint',
    "meta" => 'Legal aid clinic · 8 March',
    "body" => '<p>Case LAC-44: Anamika Roy reported threats, being kept from going out, and her husband taking her identity papers. An independent advocate set up a safe way to contact her.</p><p class="note">The note does not claim any court verdict.</p>',
   ],
   "E06" => [
    "kind" => 'log',
    "title" => 'Train reservation',
    "meta" => 'Booking record · 16 March',
    "body" => '<dl class="rows"><dt>Seat</dt><dd>S6-36, Howrah → Bardhaman</dd><dt>Passenger</dt><dd>“A. Roy”</dd><dt>Departure</dt><dd>05:45, 17 March</dd></dl><p class="note">Ticket cancelled at 05:32 with the passenger’s own booking code. She never travelled on that train.</p>',
   ],
   "E07" => [
    "kind" => 'interview',
    "title" => 'Interview: Harish Sen',
    "meta" => 'Recorded 19 March',
    "body" => '<p>“Rhea called to ask if my wife and I could give someone a quiet room for a few days. We agreed. She used the name Mira, not Anamika.”</p><p>“We didn’t know the whole story, and we never claimed to be her parents.”</p>',
   ],
   "E08" => [
    "kind" => 'note',
    "title" => 'Safety-plan envelope',
    "meta" => 'Prepared 15 March',
    "body" => '<p>Envelope addressed to “Mira Sen”, care of Harish and Lakshmi Sen. Inside: an appointment card for Dr Dutta and a note:</p><p class="handwriting">If you are followed, do not board the train. Go to the station information desk and ask for the nurse.</p>',
   ],
   "E09" => [
    "kind" => 'interview',
    "title" => 'Taxi driver’s account',
    "meta" => '17 March',
    "body" => '<p>“I brought a woman to the station at 05:21. A man in a pale blue shirt followed her from the taxi stand.”</p><p>“She ran towards the east stairs, stumbled and hit her head. The man didn’t help her.”</p>',
   ],
   "E10" => [
    "kind" => 'messages',
    "title" => 'Message archive',
    "meta" => 'Recovered from a cloud backup',
    "body" => '<div class="chat"><p class="msg in"><span>16 March · Kabir Roy → Anamika</span>You cannot leave this marriage. I have your documents. Whoever is helping you will regret it.</p><p class="msg in"><span>17 March, 05:04 · Kabir Roy → Anamika</span>I know about the train.</p></div>',
   ],
   "E11" => [
    "kind" => 'photo',
    "title" => 'CCTV review',
    "meta" => 'Station cameras',
    "body" => '<p>At 05:26 a person in a pale blue shirt enters the east stairwell 17 seconds after the woman. A street camera later shows the same man getting into a car registered to <b>Kabir Roy’s office</b>.</p><p class="note">The face cannot be identified with certainty.</p>',
    "img" => [
     "file" => 'the-second-name/stairwell.jpg',
     "caption" => 'East stairwell, 05:26',
     "prompt" => 'Grainy CCTV still of a red-painted station stairwell in Kolkata at dawn, a woman hurrying down the stairs and a man in a pale blue shirt following a few steps behind, faces not visible, security-camera look, no readable text',
    ],
   ],
   "E12" => [
    "kind" => 'interview',
    "title" => 'Interview: Lakshmi Sen',
    "meta" => 'Recorded 19 March',
    "body" => '<p>“She asked me not to put her name on the door. She remembered some things perfectly. She said Kabir would pretend she had been kidnapped.”</p><p>“She was frightened, but she was clear that she wanted to stay here.”</p>',
   ],
   "E13" => [
    "kind" => 'report',
    "title" => 'The “missing person” notice',
    "meta" => 'Submitted 18 March',
    "body" => '<p>A printed notice calls the woman “Mira Sen” and claims the Sen couple kidnapped her. Its contact number belongs to a <b>private investigator hired by Kabir Roy</b>.</p><p class="note">The notice appeared one day before the official missing-person investigation.</p>',
   ],
   "E14" => [
    "kind" => 'report',
    "title" => 'Memo: Inspector Mallick',
    "meta" => '20 March',
    "body" => '<p>The woman has asked that her location be kept from Kabir Roy. Police have confirmed Anamika Roy’s identity from independently held registration records.</p><p class="note">Nothing supports an abduction by the Sen household.</p>',
   ],
   "E15" => [
    "kind" => 'lab',
    "title" => 'Identity check',
    "meta" => 'Official registration cross-check · 20 March',
    "body" => '<p>A protected comparison of birth-registration and biometric records matches the patient to <b>Anamika Roy</b>. There is no registered “Mira Sen” matching her.</p><p class="note">The identity data is restricted and has not been given to Kabir Roy.</p>',
   ],
  ],
  "checkpoints" => [
   "A" => [
    "title" => 'Which name is real?',
    "prompt" => 'The paper in her bag says “Mira S.” The hospital says Anamika Roy. Which is her real name – and where does the other come from?',
    "gate" => [
     "q" => 'Which records came before anyone said “kidnapping”?',
     "choices" => ['Only the missing-person notice', 'The hospital intake and the legal aid complaint', 'Only Inspector Mallick’s memo'],
     "answer" => 1,
     "ok" => 'Yes – those were made before any kidnapping story. Open envelope B.',
    ],
    "hints" => ['Separate her legal identity from the name her helpers used.', 'Who is Kabir – and why does she keep saying “do not contact Kabir”?'],
   ],
   "B" => [
    "title" => 'The station',
    "prompt" => 'She had a train ticket and a safety plan. What really happened at the station?',
    "gate" => [
     "q" => 'Did she board the 05:45 train?',
     "choices" => ['Yes, and she got off at the next stop', 'No – the ticket was cancelled at 05:32, as the plan said if she was followed', 'Nobody can tell'],
     "answer" => 1,
     "ok" => 'Right – she followed the plan when she knew she was followed. Open envelope C.',
    ],
    "hints" => ['Compare the 05:04 message with the 05:32 cancellation.', 'Who followed her from the taxi stand?'],
   ],
   "final" => [
    "title" => 'The accusation',
    "prompt" => 'Who is she, why did she leave – and who is trying to take control of her again?',
    "hints" => ['Trace the phone number on the “missing” notice and compare it with the station timeline.', 'E10 + E11 + E13 lead to one person.'],
   ],
  ],
  "accuse" => [
   "culprit_q" => 'Who is trying to take control of her again?',
   "wrong" => 'That’s not the person behind the pressure campaign.',
   "items" => [
    "identity" => ['Who she is', 'Who is the woman?', 4],
    "station" => ['The station', 'What happened at Howrah?', 4],
    "notice" => ['The notice', 'What was the “missing” notice?', 3],
   ],
  ],
  "choices" => [
   "identity" => [
    "a" => 'Mira Sen, the Sens’ long-lost daughter.',
    "b" => 'Anamika Roy – “Mira Sen” is the safe-house name her helpers gave her.',
    "c" => 'A woman who has lost her memory for good.',
    "d" => 'An unknown woman with no records.',
   ],
   "station" => [
    "a" => 'She was pushed down the stairs by Harish.',
    "b" => 'She was escaping as planned, saw she was followed, skipped the train, ran for the stairs and fell.',
    "c" => 'She got lost on her way to visit family.',
    "d" => 'She fainted while boarding the train.',
   ],
   "notice" => [
    "a" => 'A genuine police appeal.',
    "b" => 'A false accusation by Kabir’s hired investigator, to make the Sens look like kidnappers.',
    "c" => 'The Sens’ own request for help.',
    "d" => 'A mistake by the hospital.',
   ],
  ],
  "worksheet" => ['What happened?', 'Who was responsible – and what was the motive?', 'Which documents prove it? Name at least three.', 'Which misleading explanation did you rule out, and why?', 'What should happen now?'],
  "solution_title" => 'The truth about the second name',
 ];
