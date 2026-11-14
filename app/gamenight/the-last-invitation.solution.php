<?php
// SPOILERS. Answer key and solution text for The Last Invitation. Only loaded server-side after the group asks to reveal it, or to score an accusation.
return [
 'culprit' => 'nora-vale',
 'motive' => 'a',
 'door' => 'c',
 'power' => 'b',
 'evidence' => ['P09', 'P10', 'P11', 'P12', 'P14', 'P16', 'P17', 'P18'],
 'summary' => [
  'The killer is <b>Nora Vale</b>. She struck Alexander Voss in the study during their meeting about invoice 417, between 22:31 and 22:36, with the heavy bronze sculpture. In a short struggle, Alexander grabbed Nora\'s right sleeve and damaged her cufflink.',
  'Nora left the study at about 22:36. The door closed, and the automatic lock that Alexander himself had set at 19:12 locked it at 22:39. The locked door gave the false impression that no one could have left the room.',
  'At 22:41 Nora went into the conservatory and built her alibi around a phone call that the phone record does not confirm. The power only went at 22:43, because of a technical fault that was already known. The power cut was never part of the murder.',
 ],
 'conclusions' => [
  ['Alexander died between 22:33 and 22:40.', 'P10'],
  ['The door locked automatically at 22:39, after someone left at 22:36.', 'P12'],
  ['Alexander had a private meeting with Nora at 22:30.', 'P09, P14, P18'],
  ['Nora\'s alibi is contradicted by K2/K5 and by the missing phone call.', 'P04, P11, P14'],
  ['Nora risked the exposure of invoice 417 – money paid to her own company.', 'P17'],
  ['Meeting, access, the lie about her alibi, motive and physical contact together point to Nora.', 'P11, P15–P18'],
 ],
 'timeline' => [
  ['22:18–22:20', 'The private confrontation is arranged', 'P14'],
  ['22:25–22:30', 'Nora claims to be in the conservatory', 'P04'],
  ['22:30–22:31', 'Nora\'s card passes K2; meeting with Alexander begins', 'P09, P11, P18'],
  ['22:33–22:40', 'Forensic time of death', 'P10'],
  ['22:36', 'Nora\'s card passes out; the door closes', 'P11, P12'],
  ['22:39', 'The privacy routine locks the door', 'P12'],
  ['22:41', 'Nora\'s card enters the conservatory', 'P11'],
  ['22:43', 'Technical power cut', 'P13'],
  ['22:50–22:52', 'Power returns; Viktor opens the door', 'P01, P12'],
 ],
 'others' => [
  '<b>Mara</b> lied about her route to hide her search for a letter about the will, but her only logged movement is at K5 at 22:47 – after the death (P19).',
  '<b>Elias</b> knew about the lock, but P12 shows that Alexander himself activated the routine at 19:12.',
  '<b>Viktor</b> had neglected a known generator fault, which explains why he was evasive – but the power went after the likely murder (P13).',
  '<b>Emil</b> had a money motive, but no evidence places him in the study.',
  '<b>Liv</b> had access to the documents, but she delivered them earlier and was last logged at 22:24 (P08, P09, P11).',
 ],
 'fairness' => 'K2 alone only proves that Nora\'s card was used, not who held it. That is why the case rests on several independent pieces: the meeting, Alexander\'s note, the alibi that doesn\'t hold, the physical contact and the motive.',
];
