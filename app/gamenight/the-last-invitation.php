<?php
// Game Night case: The Last Invitation. Server-side only (app/ is not web-accessible). The answer key never reaches the browser before the reveal.
return [
 'slug' => 'the-last-invitation',
 'no' => '001',
 'title' => 'The Last Invitation',
 'tagline' => 'A host is dead. Six guests have something to hide.',
 'teaser' => 'Property investor Alexander Voss gathers six guests at his seaside villa and promises to expose them all in the morning. By 22:52 he is dead behind a locked door.',
 'minutes' => [90, 120],
 'players' => [2, 6],
 'revision' => '1.1',
 'level' => 3,
 'genre' => 'Murder',
 'caseref' => 'NV-2026-1017',
 'stamp' => 'REOPENED',
 'cover' => ['file' => 'the-last-invitation/cover.jpg', 'prompt' => 'Moody cinematic illustration of a modern Scandinavian villa on a dark coast at night, one lit study window, storm clouds, a single wine glass on a terrace railing in the foreground, deep navy and amber palette, film-noir mood, no people, no text, 4:3'],
 'solution_title' => 'What really happened at Villa Nordlys',
 'accuse' => [
  'culprit_q' => 'Who killed Alexander?',
  'wrong' => 'That\'s not the person who killed Alexander.',
  'items' => ['motive' => ['Motive', 'What was the motive?', 4], 'door' => ['The locked door', 'How was the door locked?', 4], 'power' => ['The power cut', 'Why did the power go out?', 3]],
 ],
 'worksheet' => ['Who is responsible for Alexander\'s death?', 'What was the motive?', 'What happened between 22:25 and 22:43?', 'Why was the door locked?', 'Why did the power go out?'],
 'intro' => [
  'On Saturday 17 October 2026, property investor <b>Alexander Voss</b> invites six people to dinner at Villa Nordlys, his remote house on the Danish coast. Over dinner he announces that tomorrow morning he will publish documents that could ruin several of their lives.',
  'At 22:43 the power goes out. Seven minutes later the backup supply starts. At 22:52 Alexander is found dead in his study. The door was locked. A window stood ajar. The police first call it an accident.',
  'Three weeks later, Alexander\'s sister hands you the original case file. She is certain her brother\'s death was no accident.',
 ],
 'mission' => [
  'Find out whether Alexander was murdered – and if so, by whom.',
  'Explain the locked door, the power cut and the strange details at the scene.',
  'Back up your accusation with at least four document numbers.',
 ],
 'questions' => [
  'When did Alexander most likely die?',
  'How could the door be locked if the killer had left?',
  'Who had a private meeting with Alexander?',
  'Which alibi does not match the independent timestamps?',
  'Who had a concrete reason to stop tomorrow\'s disclosure?',
  'Who did what, when – and why?',
 ],
 'suspects' => [
  ['id' => 'nora-vale', 'name' => 'Nora Vale', 'role' => 'Business partner, 46'],
  ['id' => 'mara-voss', 'name' => 'Mara Voss', 'role' => 'Ex-wife, 49'],
  ['id' => 'elias-lund', 'name' => 'Elias Lund', 'role' => 'Family lawyer, 58'],
  ['id' => 'viktor-holm', 'name' => 'Viktor Holm', 'role' => 'House manager, 39'],
  ['id' => 'emil-voss', 'name' => 'Emil Voss', 'role' => 'Younger brother, 42'],
  ['id' => 'liv-brandt', 'name' => 'Liv Brandt', 'role' => 'Personal assistant, 31'],
 ],
 'packets' => [
  'START' => ['label' => 'Start folder', 'docs' => ['P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P07', 'P08', 'P09', 'P10']],
  'B' => ['label' => 'Envelope B', 'when' => 'you can explain why a locked door doesn\'t prove Alexander was alone', 'docs' => ['P11', 'P12', 'P13', 'P14', 'P15']],
  'C' => ['label' => 'Envelope C', 'when' => 'you have found a statement that clashes with a technical record', 'docs' => ['P16', 'P17', 'P18', 'P19']],
 ],
 'docs' => [
  'P01' => ['kind' => 'report', 'title' => 'Police incident report', 'body' => '
    <dl class="rows"><dt>Case no.</dt><dd>NV-2026-1017</dd><dt>Address</dt><dd>Villa Nordlys, Kystvejen 18</dd><dt>Call received</dt><dd>22:55</dd><dt>Patrol on site</dt><dd>23:14</dd><dt>Deceased</dt><dd>Alexander Voss, 54</dd></dl>
    <p>Found at 22:52 by house manager Viktor Holm and guest Elias Lund. The study door was closed and locked. Viktor opened it with the house\'s mechanical emergency key. A window facing the garden was ajar. A heavy bronze sculpture lay on the floor by the desk.</p>
    <p>Based on the first medical assessment, the case was initially registered as a possible fall. Following the sister\'s request, it has been reopened as a suspicious death.</p>'],
  'P02' => ['kind' => 'plan', 'title' => 'Floor plan and access routes', 'body' => '
    {{FLOORPLAN}}
    <ul class="plain"><li><b>North:</b> Study – one door to the corridor, one window to the garden.</li>
    <li><b>East:</b> East corridor between dining room and study. Every pass is logged by card reader <b>K2</b>.</li>
    <li><b>South:</b> Dining room, kitchen and stairs to the bedrooms.</li>
    <li><b>West:</b> Conservatory with a door to the terrace. Card reader <b>K5</b> at the entrance from the hall.</li>
    <li><b>Plant room</b> next to the kitchen.</li></ul>
    <p class="note">There is no inside door between the study and the conservatory. The route between them runs through the east corridor and the hall.</p>'],
  'P03' => ['kind' => 'list', 'title' => 'The six guests', 'body' => '
    <table class="guests"><tr><td><b>Nora Vale</b>, 46</td><td>Business partner. Runs the property company with Alexander.</td></tr>
    <tr><td><b>Mara Voss</b>, 49</td><td>Ex-wife. In dispute over the prenuptial agreement and wills.</td></tr>
    <tr><td><b>Elias Lund</b>, 58</td><td>Family lawyer. Manages private company documents.</td></tr>
    <tr><td><b>Viktor Holm</b>, 39</td><td>House manager. Responsible for the house and its keys.</td></tr>
    <tr><td><b>Emil Voss</b>, 42</td><td>Alexander\'s younger brother. Owes Alexander money.</td></tr>
    <tr><td><b>Liv Brandt</b>, 31</td><td>Personal assistant. Has access to calendars and invitations.</td></tr></table>
    <p>All six were invited to dinner. The other staff left the property at 21:45.</p>'],
  'P04' => ['kind' => 'interview', 'title' => 'Interview: Nora Vale', 'meta' => 'Interviewed 18 October, 09:40', 'body' => '
    <p>“Alexander was angry about an audit question. We agreed to talk the next day. I went to the conservatory at about 22:25 to call my daughter, and I stayed there until after the power cut. I didn\'t go past the study.”</p>
    <p>“I can\'t remember exactly where my guest card was around 22:30. I think it was in my bag. Anyone could leave their card on the console table.”</p>
    <p>“I didn\'t hear anything unusual. If my card was logged near the study, someone must have borrowed it.”</p>'],
  'P05' => ['kind' => 'interview', 'title' => 'Interview: Mara Voss', 'meta' => 'Interviewed 18 October, 10:05', 'body' => '
    <p>“I was in the guest bedroom from 22:25 to 22:48. I wanted to find a letter from our lawyer, but that has nothing to do with Alexander\'s death.”</p>
    <p>“He was not a nice man. But I didn\'t kill him. When the lights went out, I stayed in my room.”</p>
    <p>“My relationship with Alexander was bad, but we had a written agreement about dividing the money.”</p>'],
  'P06' => ['kind' => 'interview', 'title' => 'Interview: Elias Lund', 'meta' => 'Interviewed 18 October, 10:25', 'body' => '
    <p>“From about 22:25 I sat in the dining room going through an appendix to a contract. I saw Emil walk towards the kitchen at around half past ten.”</p>
    <p>“Alexander used a timed privacy lock on his study. He often said he didn\'t want to be disturbed late in the evening.”</p>
    <p>“I helped Viktor find the mechanical emergency key after the power came back. I knew about his upcoming audit, but not what was in it.”</p>'],
  'P07' => ['kind' => 'interview', 'title' => 'Interview: Viktor Holm', 'meta' => 'Interviewed 18 October, 11:10', 'body' => '
    <p>“I was in the plant room from about 22:35 to 22:49. The backup power didn\'t start as fast as it should have.”</p>
    <p>“I know the study window has had trouble closing properly before. But nobody could get in through it without forcing it.”</p>
    <p>“I went to the study with Elias at 22:51, opened it with the emergency key and found Alexander.”</p>'],
  'P08' => ['kind' => 'interview', 'title' => 'Interviews: Emil Voss and Liv Brandt', 'meta' => 'Interviewed 18 October', 'body' => '
    <p><b>Emil Voss:</b> “I called a creditor from the kitchen at about 22:30. I didn\'t want Alexander to hear. I was back in the dining room before the lights went out. I was furious that he refused to lend me more money.”</p>
    <p><b>Liv Brandt:</b> “I tidied up after dinner and then sat in the library. At about 22:20 Alexander asked me to put a folder marked ORIGINALS on his desk. It held audit papers. I saw him alive at 22:24.”</p>'],
  'P09' => ['kind' => 'calendar', 'title' => 'Extract from Alexander\'s calendar', 'body' => '
    <p class="cal-day">17 October 2026</p>
    <table class="cal"><tr><td>21:00</td><td>Dinner continues.</td></tr><tr><td>22:25</td><td>Liv delivers ORIGINALS.</td></tr>
    <tr><td>22:30</td><td><b>N.V.:</b> ‘Go through appendix 417 with no one else present.’ Private meeting in the study.</td></tr>
    <tr><td>23:00</td><td>Call external auditor.</td></tr></table>
    <p class="cal-day">18 October</p><table class="cal"><tr><td>08:30</td><td>Send documents to the board and the auditor.</td></tr></table>
    <p class="note">NOTE added by Alexander at 18:52: ‘N.V. must get the chance to explain herself first.’</p>'],
  'P10' => ['kind' => 'medical', 'title' => 'Preliminary forensic assessment', 'meta' => 'Supplementary note dated 26 October', 'body' => '
    <dl class="rows"><dt>Cause of death</dt><dd>Severe injury from a blow to the back of the head. The injury is not typical of a simple fall from standing.</dd>
    <dt>Likely time of death</dt><dd><b>Between 22:33 and 22:40</b> on 17 October. The interval is uncertain.</dd></dl>
    <p>Under the nails of the right hand: traces of <b>dark blue textile</b> and a very small piece of <b>gold-coloured metal</b>. The material has been secured for later analysis.</p>
    <p>No signs that the deceased survived beyond the power cut at 22:43.</p>'],
  'P11' => ['kind' => 'log', 'title' => 'K2 / K5 access log', 'body' => '
    <p class="log-head">K2 · EAST CORRIDOR</p>
    <table class="log"><tr><td>22:21:14</td><td>LIV</td><td>entry</td></tr><tr><td>22:24:52</td><td>LIV</td><td>pass out</td></tr>
    <tr><td>22:30:51</td><td>NORA</td><td>entry</td></tr><tr><td>22:36:09</td><td>NORA</td><td>pass out</td></tr>
    <tr><td>22:51:38</td><td>VIKTOR</td><td>entry</td></tr><tr><td>22:51:41</td><td>ELIAS</td><td>pass</td></tr></table>
    <p class="log-head">K5 · CONSERVATORY</p>
    <table class="log"><tr><td>22:41:12</td><td>NORA</td><td>entry</td></tr><tr><td>22:47:36</td><td>MARA</td><td>pass out towards hall</td></tr></table>
    <p class="note">System note: a card record proves that the card was used – not who was holding it. K5 records passes through the door between the hall and the conservatory, not activity inside the room.</p>'],
  'P12' => ['kind' => 'log', 'title' => 'Smart lock / door status', 'meta' => 'Local lock log, study door D1', 'body' => '
    <table class="log"><tr><td>19:12:40</td><td>ALEXANDER – routine ‘Private work’ activated</td></tr><tr><td>22:30:55</td><td>door opened</td></tr>
    <tr><td>22:36:11</td><td>door closed</td></tr><tr><td>22:39:00</td><td>automatic lock activated by routine</td></tr>
    <tr><td>22:43:17</td><td>power failure (lock keeps mechanical bolt)</td></tr><tr><td>22:50:21</td><td>power restored</td></tr>
    <tr><td>22:52:04</td><td>door opened with mechanical emergency key</td></tr></table>
    <p class="note">The routine locks the door automatically at 22:39 every evening if it is closed. It does not need anyone to be in the room at that moment.</p>'],
  'P13' => ['kind' => 'report', 'title' => 'Internal technical fault report', 'meta' => 'Service company note, 18 October', 'body' => '
    <p>Mains supply interrupted at 22:43:17. Backup generator started at 22:50:21.</p>
    <p>The fault was caused by a neglected relay in the backup power control. No sign of sabotage or of anyone switching off the mains by hand.</p>
    <p>House manager Viktor had reported the relay fault internally on 11 October, but the repair was postponed.</p>
    <p class="note">The power cut happened after the likely time of death and does not explain it.</p>'],
  'P14' => ['kind' => 'messages', 'title' => 'Private messages, 17 October', 'body' => '
    <div class="chat"><p class="msg in"><span>22:18 · Alexander → Nora</span>I have the originals. 417 is not just a bookkeeping error. Come alone at 22:30.</p>
    <p class="msg out"><span>22:20 · Nora → Alexander</span>We\'ll talk. Let\'s avoid a scene in front of the others.</p>
    <p class="msg out"><span>22:26 · Nora → her daughter</span>Will call later. Busy.</p>
    <p class="msg out"><span>22:44 · Nora → her daughter</span>Sorry, the evening ran late. Will call tomorrow.</p></div>
    <p class="note">The phone record shows the times of the messages. It shows no call between Nora and her daughter between 22:25 and 22:43.</p>'],
  'P15' => ['kind' => 'photo', 'img' => ['file' => 'the-last-invitation/p15-dinner.jpg', 'caption' => 'Dinner at Villa Nordlys, 20:17', 'prompt' => 'Candid flash photo of an elegant dinner party in a Scandinavian seaside villa at night, six guests around a long table with candles and wine glasses; in focus a woman of about 46 in a dark navy woven jacket with small gold hexagonal cufflinks; warm tones, slightly grainy, documentary style, no text'], 'title' => 'Photo from the dinner / clothing', 'meta' => 'Caption of photo taken at 20:17 by Liv', 'body' => '
    {{IMG}}
    <p>Nora wears a dark blue jacket of clearly woven fabric and gold-coloured cufflinks shaped like a hexagon with three narrow grooves. Both cufflinks are visible in the photo.</p>
    <p>Elias wears a grey suit, Emil a black jumper, Viktor an olive-green shirt, Liv a white blouse and Mara a burgundy dress.</p>
    <p class="note">A later photo of Nora at 23:18 shows that the cufflink on her right sleeve is missing. Nora says it ‘must have fallen off earlier in the evening’.</p>'],
  'P16' => ['kind' => 'lab', 'title' => 'Forensic analysis of material', 'meta' => 'Laboratory report, 29 October', 'body' => '
    <p>The textile found under Alexander\'s nails is consistent with the dark blue fabric of Nora\'s jacket. On its own this is not a unique identification.</p>
    <p>The metal fragment is gold-coloured, with a particular alloy and groove profile that match the remaining cufflink on Nora\'s jacket.</p>
    <p class="note">The report cannot say when the contact between Alexander and Nora\'s clothing took place, but the find is consistent with a physical struggle shortly before death.</p>'],
  'P17' => ['kind' => 'audit', 'title' => 'Appendix 417 / accounting irregularity', 'meta' => 'Internal audit sheet – Voss & Vale Properties A/S', 'body' => '
    <dl class="rows"><dt>Invoice 417</dt><dd>‘Due diligence, Coast Project’</dd><dt>Payee</dt><dd>Helix Advisory</dd><dt>Amount</dt><dd><b>DKK 2,480,000</b></dd></dl>
    <p>Bank appendix: the receiving account is controlled by the company <b>Vale Invest Holding ApS</b>. Company register copy: Vale Invest Holding ApS is 100% owned by <b>Nora Vale</b>.</p>
    <p class="quote">Email draft from Alexander, 18:52: ‘This is misuse of company money. Tomorrow the auditor and the board get everything. Nora gets one last chance to explain tonight.’</p>
    <p class="note">The internal investigation shows a serious conflict of interest. On its own this is not proof of murder.</p>'],
  'P18' => ['kind' => 'note', 'title' => 'Note found on the desk', 'body' => '
    <p>On the back of the top sheet in the ORIGINALS folder: an unsent handwritten note in Alexander\'s distinctive writing.</p>
    <p class="handwriting">NV came 22.31. She says 417 was only temporary. The original shows otherwise. She wants it stopped. I have said no. I</p>
    <p>The last word is broken off. There are small blood marks on the edge of the sheet, and the note is believed to have been written shortly before the injury.</p>
    <p class="note">The police technical unit judges handwriting and paper to be genuine. The time ‘22.31’ comes from the note itself, not from a digital timestamp.</p>'],
  'P19' => ['kind' => 'interview', 'title' => 'Corrected statement: Mara Voss', 'meta' => 'Corrected on 30 October', 'body' => '
    <p>“I lied about staying in my room all evening. After the power cut I went to the library to fetch a letter about the will. At 22:47 I went through the conservatory because the hall was dark. I was afraid of being blamed for something if anyone saw me.”</p>
    <p>Lawyer Elias confirms that an unresolved letter about the will exists. The K5 record at 22:47 fits Mara\'s corrected route.</p>
    <p class="note">This lie does not explain who was in the study between 22:30 and 22:36.</p>'],
 ],
 'checkpoints' => [
  'A' => ['title' => 'The locked door', 'prompt' => 'The study was locked when Alexander was found. Does that prove he was alone when he died?',
          'unlock' => 'B', 'button' => 'We can explain it – open envelope B',
          'hints' => ['A locked door only tells you when it was locked – not who was inside at that moment.', 'Read what Elias says about the study lock in P06. A lock on a timer doesn\'t care whether anyone is in the room.'],
          'fallback' => 'Stuck? You may open envelope B after 25 minutes anyway.'],
  'B' => ['title' => 'The shaky alibi', 'prompt' => 'Whose statement conflicts with the independent timestamps? Find more than one document that shows it.',
          'unlock' => 'C', 'button' => 'We\'ve found it – open envelope C',
          'hints' => ['Put P04 next to the K2/K5 log in P11. Where does Nora say she was?', 'Nora says she was in the conservatory from about 22:25 – but her card passes K2 at 22:30 and only enters the conservatory (K5) at 22:41. P14 shows no call to her daughter either.'],
          'fallback' => 'Stuck? You may open envelope C after another 25 minutes.'],
  'final' => ['title' => 'The accusation', 'prompt' => 'Who killed Alexander, why, and how did the locked door fool everyone? Back it up with at least four documents.',
          'hints' => ['Combine the meeting, the alibi, the motive and the physical contact into one explanation.', 'P09, P11, P14 and P16–P18 form one chain of evidence.']],
 ],
 'choices' => [
  'motive' => [
   'a' => 'Alexander was about to expose that she had moved DKK 2.48 million out of the company through invoice 417.',
   'b' => 'She wanted to inherit Alexander\'s share of the company.',
   'c' => 'Alexander refused to lend her more money.',
   'd' => 'She was afraid of losing out under Alexander\'s new will.',
  ],
  'door' => [
   'a' => 'The killer locked the door from outside with the mechanical emergency key.',
   'b' => 'The killer left by the window, and the door had been locked from the inside all along.',
   'c' => 'The killer left at 22:36, and Alexander\'s privacy routine locked the empty doorway automatically at 22:39.',
   'd' => 'The power cut jammed the lock and made it look locked.',
  ],
  'power' => [
   'a' => 'The killer cut the power to escape in the dark.',
   'b' => 'A known relay fault in the backup power – it had nothing to do with the murder.',
   'c' => 'Viktor switched the power off to hide the time of death.',
   'd' => 'Mara caused it while looking for the letter about the will.',
  ],
 ],
];
