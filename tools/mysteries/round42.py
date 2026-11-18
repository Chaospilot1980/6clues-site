from lib import *  # evidence helpers

# Round 42 (18 Nov): 4 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- COURTROOM
court = {
 "slug": "death-in-the-courthouse", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 230", "title_html": "DEATH IN THE<br>COURTHOUSE", "title_plain": "Death in the Courthouse",
 "teaser": "A star witness is found dead in a courthouse waiting room before he can testify. The court clerk's list, a security scan and a juror's note show who got to him.",
 "intro": "At <b>Crown Court, Ashbury</b>, star witness Terry Doyle was found dead in the witness waiting room minutes before he was due to give evidence in a big fraud trial. He had been poisoned through his water. " + STD,
 "clues": [
  {"name": "DI Rosa Quinn", "role": "Police", "label": "POLICE REPORT",
   "quote": "The poison was in Mr Doyle's water bottle. He drank from it at 10:50 and collapsed at 11:00. The bottle was left on the waiting-room table while he went to the toilet from 10:35 to 10:42.",
   "evidence": ev_rows("Police report – Ashbury Crown Court", [
       ("Bottle unattended", "10:35–10:42"),
       ("Drank", "10:50 · collapsed 11:00"),
       ("Waiting room", "Only witnesses, ushers and lawyers allowed"),
       ("Poison", "Clear liquid – tasteless"),
     ])},
  {"name": "Ms Victoria Lane", "role": "Defence lawyer", "label": "VICTORIA'S STATEMENT",
   "quote": "I was in Courtroom 2 from ten until eleven, arguing a legal point before the judge. I never left.",
   "evidence": ev_rows("Defence notes (seized)", [
       ("Client", "Gerald Moss – charged with £4m fraud"),
       ("Note in V. Lane's hand", "“If Doyle testifies, Moss goes to prison. Doyle must NOT testify.”"),
     ])},
  {"name": "Ben Price", "role": "Court usher", "label": "COURT LOG",
   "quote": "The judge called a short break from 10:30 to 10:45 while the jury came in. Ms Lane left the courtroom then – she said she needed to 'speak to a witness'.",
   "evidence": ev_table("Courtroom 2 – log", ["Time", "Event"], [
       ("10:00", "Legal argument – V. Lane"),
       ("10:30", "Short break – courtroom empties"),
       ("10:45", "Court resumes"),
       ("10:58", "Witness T. Doyle called – does not appear"),
     ], mono_cols=(0,))},
  {"name": "Asha Mills", "role": "Court security", "label": "DOOR SCAN",
   "quote": "The witness waiting room has a card reader. Lawyers use their court pass. Only one lawyer's pass opened it that morning.",
   "evidence": ev_table("Witness room door – scans", ["Time", "Pass"], [
       ("09:45", "T. Doyle (witness pass)"),
       ("10:36", "V. Lane (counsel pass)"),
       ("10:40", "Exit – V. Lane"),
       ("10:42", "T. Doyle (witness pass)"),
     ], mono_cols=(0,))},
  {"name": "Mr Gerald Moss", "role": "Defendant", "label": "GERALD'S STATEMENT",
   "quote": "I'm on bail, but I was in the dock the whole time with a guard beside me. I couldn't go anywhere.",
   "evidence": ev_rows("Dock officer's note", [
       ("10:00–11:15", "G. Moss in the dock or in the cells – never alone"),
     ])},
  {"name": "Kate Wells", "role": "Juror", "label": "JUROR'S NOTE",
   "quote": "In the break I went to the toilet. Through the waiting-room glass I saw a lawyer in a wig and gown bending over a table, with a small brown bottle in her hand.",
   "evidence": ev_note("JUROR'S NOTE TO THE JUDGE", [
       "About 10:37 – woman in wig and",
       "gown in witness room, alone. Small",
       "brown bottle over a water bottle.",
       "Red lipstick, gold earrings."],
     "– Juror 7")},
 ],
 "solution": {"killer": "Ms Victoria Lane",
   "motive": "If Terry testified, her client would go to prison: 'Doyle must NOT testify' (clue 2).",
   "proof": ["The water bottle was poisoned while Terry was away from 10:35 to 10:42 (clue 1).",
             "Victoria says she never left Courtroom 2, but there was a break from 10:30 to 10:45 and she left to 'speak to a witness' (clue 3).",
             "Her pass opened the witness room at 10:36 and she left at 10:40 (clue 4), and a juror saw a woman lawyer with a small brown bottle over the water at 10:37 (clue 6)."],
   "cleared": ["<b>Gerald</b> was guarded in the dock or cells the whole time (clue 5).",
               "<b>Ben</b>, <b>Asha</b> and <b>Kate</b> only report what they saw."]},
}

# ---------------------------------------------------------------- REGATTA
regatta = {
 "slug": "murder-at-the-winter-regatta", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 231", "title_html": "MURDER AT THE<br>WINTER REGATTA", "title_plain": "Murder at the Winter Regatta",
 "teaser": "A sailing club commodore is found dead in the committee boat during the winter regatta. Race start signals and a lifejacket number reveal who left their dinghy.",
 "intro": "At the <b>Fenmouth Sailing Club</b> Winter Regatta, Commodore Hugh Brennan was found dead on the committee boat, struck with a flag pole. " + STD,
 "clues": [
  {"name": "DS Kate Ellis", "role": "Police", "label": "POLICE REPORT",
   "quote": "The commodore was alone on the committee boat running the race. He sounded the start horn at 11:00 and the next signal was never given. He died soon after 11:00.",
   "evidence": ev_rows("Police report – Fenmouth SC", [
       ("Start horn", "11:00 – sounded"),
       ("5-minute signal", "11:05 – never sounded"),
       ("Found", "11:40, committee boat"),
       ("On deck", "Wet bootprints and a broken lifejacket buckle, No. 17"),
     ])},
  {"name": "Rachel Brennan", "role": "Commodore's daughter, sailor", "label": "RACHEL'S STATEMENT",
   "quote": "I was racing in my dinghy the whole time. I was out at the far mark when Dad was killed.",
   "evidence": ev_rows("Club committee letter", [
       ("To", "Rachel Brennan"),
       ("Text", "“The commodore has banned you from racing for one year for cheating at the autumn series.”"),
       ("Date", "Last week"),
     ])},
  {"name": "Paul Webb", "role": "Shore race officer", "label": "RACE TRACKER",
   "quote": "Every dinghy has a GPS tracker. One boat didn't go round the course at the start.",
   "evidence": ev_table("Dinghy trackers – 11:00 to 11:15", ["Boat", "Sailor", "Position"], [
       ("Dinghy 12", "T. Hall", "Racing to mark 1"),
       ("Dinghy 17", "R. Brennan", "Alongside committee boat 11:01–11:09"),
       ("Dinghy 21", "S. Adams", "Racing to mark 1"),
     ])},
  {"name": "Tim Hall", "role": "Sailor", "label": "TIM'S NOTE",
   "quote": "At the start I looked back and saw a dinghy tied up next to the committee boat. Its sail number was 17.",
   "evidence": ev_note("TIM'S RACE NOTES", [
       "11:02 – dinghy 17 tied alongside",
       "the committee boat. Sailor in a red",
       "spray top climbing aboard. Strange",
       "– she should be racing."],
     "– Tim")},
  {"name": "Sue Adams", "role": "Sailor", "label": "SUE'S STATEMENT",
   "quote": "I had an argument with Hugh about the club fees, yes. But I was racing all morning – you can check my tracker.",
   "evidence": ev_rows("Tracker – Dinghy 21", [
       ("11:00–11:40", "On the race course – never near the committee boat"),
     ])},
  {"name": "Mick Grey", "role": "Club bosun", "label": "LIFEJACKET LIST",
   "quote": "Club lifejackets are numbered to match the dinghy. Number 17 goes with dinghy 17.",
   "evidence": ev_table("Lifejackets issued – regatta", ["No.", "Sailor"], [
       ("12", "T. Hall"),
       ("17", "R. Brennan"),
       ("21", "S. Adams"),
     ])},
 ],
 "solution": {"killer": "Rachel Brennan",
   "motive": "Her father had banned her from racing for a year for cheating (clue 2).",
   "proof": ["The commodore died soon after 11:00; a broken lifejacket buckle No. 17 was on deck (clue 1).",
             "Rachel says she was racing at the far mark, but her dinghy 17 was alongside the committee boat from 11:01 to 11:09 (clue 3), and Tim saw a sailor climb aboard from dinghy 17 at 11:02 (clue 4).",
             "Lifejacket 17 belongs to Rachel (clue 6)."],
   "cleared": ["<b>Tim</b> and <b>Sue</b> were racing to mark 1 the whole time (clues 3, 5).",
               "<b>Paul</b> and <b>Mick</b> only report what they found."]},
}

# ---------------------------------------------------------------- HOSPITAL
hospital = {
 "slug": "death-on-the-night-ward", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 232", "title_html": "DEATH ON THE<br>NIGHT WARD", "title_plain": "Death on the Night Ward",
 "teaser": "A rich patient dies on a quiet hospital ward over Christmas. A drip pump log, a staff badge and a visitor's coffee cup show who changed his medicine.",
 "intro": "At <b>St Hilda's Hospital</b>, businessman Arthur Graves was recovering well from an operation when he died in the night. Someone had changed the speed of his medicine drip. " + STD,
 "clues": [
  {"name": "Dr Maya Singh", "role": "Ward doctor", "label": "DOCTOR'S REPORT",
   "quote": "His drip pump was changed from 5 ml an hour to 50. It was done by hand on the pump keypad – and it needs a staff badge to unlock.",
   "evidence": ev_rows("Doctor's report", [
       ("Died", "About 03:00"),
       ("Drip pump", "Changed 5 → 50 ml/h at 01:12"),
       ("Pump unlock", "Staff badge needed"),
       ("Visitors", "Not allowed after 21:00"),
     ])},
  {"name": "Owen Ford", "role": "Night nurse", "label": "OWEN'S STATEMENT",
   "quote": "I checked Mr Graves at midnight. He was sleeping. I lost my staff badge somewhere that evening – I reported it at 23:00.",
   "evidence": ev_rows("Security – lost badge report", [
       ("Badge", "O. Ford"),
       ("Reported lost", "23:00"),
       ("Last used before loss", "22:40, staff room door"),
     ])},
  {"name": "Sam Lee", "role": "Equipment technician", "label": "PUMP LOG",
   "quote": "The pump records which badge unlocked it. It was Owen's – the one he'd reported lost two hours before.",
   "evidence": ev_table("Drip pump – bed 4", ["Time", "Badge", "Change"], [
       ("00:00", "O. Ford", "Check – no change"),
       ("01:12", "O. Ford (reported lost)", "5 → 50 ml/h"),
     ], mono_cols=(0,))},
  {"name": "Celia Graves", "role": "Arthur's daughter", "label": "CELIA'S STATEMENT",
   "quote": "I visited Dad in the evening and left at nine like everyone else. I spent the night at my hotel.",
   "evidence": ev_rows("Arthur's new will (unsigned)", [
       ("Old will", "Everything to Celia"),
       ("New will", "Everything to the hospital's cancer fund"),
       ("Signing", "Booked for 10:00 the next morning"),
     ])},
  {"name": "Dave Okafor", "role": "Night porter", "label": "PORTER'S NOTE",
   "quote": "At about ten past one I saw a woman in a nurse's tunic I didn't recognise, with a staff badge on, coming out of the ward. She had an expensive handbag – no nurse brings that on shift.",
   "evidence": ev_note("PORTER'S NOTE", [
       "About 01:15 – woman in blue tunic,",
       "staff badge, designer handbag, came",
       "out of Ward 7 to the stairs. Not one",
       "of ours. Long blonde hair."],
     "– Dave")},
  {"name": "Lily Tan", "role": "Riverside Hotel", "label": "HOTEL LOG",
   "quote": "Ms Graves had room 12. Our key cards show when a room door is opened.",
   "evidence": ev_table("Room 12 – key card", ["Time", "Event"], [
       ("21:30", "Door opened – guest in"),
       ("00:40", "Door opened – guest out"),
       ("01:55", "Door opened – guest in"),
     ], mono_cols=(0,), note="The hotel is a 10-minute walk from St Hilda's.")},
 ],
 "solution": {"killer": "Celia Graves",
   "motive": "Arthur was about to sign a new will leaving everything to charity instead of Celia (clue 4).",
   "proof": ["The drip was changed at 01:12 with Owen's badge – the one he lost in the evening (clues 1, 2, 3).",
             "Celia says she spent the night at her hotel, but she left her room at 00:40 and only came back at 01:55, and the hotel is ten minutes from the hospital (clue 6).",
             "At 01:15 the porter saw a woman who wasn't a nurse, with long blonde hair, a staff badge and a designer handbag, leaving the ward (clue 5)."],
   "cleared": ["<b>Owen</b> reported his badge lost at 23:00, before it was used (clues 2, 3).",
               "<b>Dr Singh</b>, <b>Sam</b>, <b>Dave</b> and <b>Lily</b> only report what they found."]},
}

# ---------------------------------------------------------------- EMBASSY
embassy = {
 "slug": "murder-at-the-embassy-ball", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 233", "title_html": "MURDER AT THE<br>EMBASSY BALL", "title_plain": "Murder at the Embassy Ball",
 "teaser": "An ambassador's aide is found dead in the embassy library during the New Year ball. The band's set list and a cufflink catch the killer.",
 "intro": "At the <b>Embassy of Valoria</b> in London, aide Lukas Varga was found dead in the library during the New Year ball, struck with a heavy crystal paperweight. " + STD,
 "clues": [
  {"name": "Inspector James Holt", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Varga died in the library during the waltz – the band played it from 22:10 to 22:25. A gold cufflink with the letter 'R' was under the desk.",
   "evidence": ev_rows("Police report – Valorian Embassy", [
       ("Found", "22:40, library"),
       ("Time of death", "22:10–22:25"),
       ("Weapon", "Crystal paperweight"),
       ("Under the desk", "Gold cufflink, engraved 'R'"),
     ])},
  {"name": "Count Rafael Orsini", "role": "Guest, businessman", "label": "RAFAEL'S STATEMENT",
   "quote": "I was dancing the waltz with the ambassador's wife. Everyone in the ballroom saw us.",
   "evidence": ev_rows("Lukas Varga's notes", [
       ("File", "Count Orsini – bribes to embassy staff for oil contracts"),
       ("Note", "“Hand to the ambassador after the ball.”"),
     ])},
  {"name": "Madame Elena Kova", "role": "Ambassador's wife", "label": "DANCE CARD",
   "quote": "The Count was on my dance card for the waltz. But he said he had to take a call, and left me after the first few bars. I danced with the Ambassador instead.",
   "evidence": ev_table("Madame Kova's dance card", ["Time", "Dance", "Partner"], [
       ("22:00", "Polka", "Ambassador Kova"),
       ("22:10", "Waltz", "Count Orsini – left at 22:11"),
       ("22:12", "Waltz (cont.)", "Ambassador Kova"),
     ], mono_cols=(0,))},
  {"name": "Simon Reece", "role": "Embassy butler", "label": "CORRIDOR NOTE",
   "quote": "The library is at the end of the east corridor. At about twenty past ten a gentleman in a white tie came down it, holding his left shirt cuff closed.",
   "evidence": ev_note("BUTLER'S NOTE", [
       "About 22:20 – gentleman, white tie,",
       "grey moustache, from library, holding",
       "his left cuff. Walked fast back to the",
       "ballroom."],
     "– Reece")},
  {"name": "Mr Robert Lowe", "role": "Guest, journalist", "label": "ROBERT'S STATEMENT",
   "quote": "My initial is R too – I know how that looks. But I was in the smoking room with three other guests from ten till eleven.",
   "evidence": ev_photos("Smoking room photo", [
       ("IMG_501", "22:15", "Robert Lowe and three guests playing cards in the smoking room. Robert is clean-shaven and wearing silver cufflinks."),
     ])},
  {"name": "Nina Bose", "role": "Cloakroom", "label": "GUEST LIST",
   "quote": "I check every guest in. Only one wore gold 'R' cufflinks – I remember because he made me polish them.",
   "evidence": ev_table("Guests – white tie", ["Guest", "Notes"], [
       ("Count R. Orsini", "Grey moustache, gold 'R' cufflinks"),
       ("Mr R. Lowe", "Clean-shaven, silver cufflinks"),
       ("Ambassador Kova", "Beard, no cufflinks – studs"),
     ])},
 ],
 "solution": {"killer": "Count Rafael Orsini",
   "motive": "Lukas was going to hand the ambassador proof of the Count's bribes (clue 2).",
   "proof": ["Lukas died between 22:10 and 22:25; a gold 'R' cufflink was under the desk (clue 1).",
             "The Count says he danced the waltz with Madame Kova, but he left her at 22:11 (clue 3).",
             "At 22:20 the butler saw a man with a grey moustache coming from the library holding his left cuff (clue 4). Only the Count has a grey moustache and gold 'R' cufflinks (clue 6)."],
   "cleared": ["<b>Robert</b> was playing cards at 22:15, clean-shaven with silver cufflinks (clues 5, 6).",
               "<b>Madame Kova</b> danced with the Ambassador (clue 3); <b>Simon</b> and <b>Nina</b> only report what they saw."]},
}

MYSTERIES = [court, regatta, hospital, embassy]
