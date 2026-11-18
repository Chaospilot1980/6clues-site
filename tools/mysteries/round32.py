from lib import *  # evidence helpers

# Round 32 (18 Nov): 2 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- FUN RUN (L2)
funrun = {
 "slug": "the-charity-fun-run-cheat", "level": 2, "crime": "FRAUD", "who": "fraudster", "added": ADDED,
 "caseno": "CASE NO. 190", "title_html": "THE CHARITY<br>FUN RUN CHEAT", "title_plain": "The Charity Fun Run Cheat",
 "teaser": "The winner of a Santa charity fun run claims a record time and a £500 prize. Checkpoint chips, a bus ticket and a photo of the beard prove it was a cheat.",
 "intro": "At the <b>Bridgeford Santa Fun Run</b>, 300 runners in Santa suits raced 10 km for charity. The winner set a course record and claimed the £500 prize – but the organisers are not convinced. " + STD,
 "clues": [
  {"name": "Helen Price", "role": "Race organiser", "label": "RESULTS",
   "quote": "The winning time was 31 minutes – four minutes faster than any time ever run on this course. Every runner wears a chip that beeps at three checkpoints.",
   "evidence": ev_table("Top three – official results", ["Place", "Runner", "Bib", "Time"], [
       ("1", "Craig Dunn", "117", "31:02"),
       ("2", "Asha Rai", "54", "35:40"),
       ("3", "Will Ford", "208", "36:15"),
     ])},
  {"name": "Craig Dunn", "role": "Winning runner", "label": "CRAIG'S STATEMENT",
   "quote": "I've trained all year. I ran every step of the course – check the chip, it beeped at every checkpoint.",
   "evidence": ev_table("Chip times – bib 117", ["Checkpoint", "Distance", "Time"], [
       ("Start", "0 km", "10:00:00"),
       ("CP1", "3 km", "10:10:30"),
       ("CP2", "7 km", "–  no beep"),
       ("CP3", "9 km", "10:28:10"),
       ("Finish", "10 km", "10:31:02"),
     ])},
  {"name": "Ray Lowe", "role": "Timing engineer", "label": "CHIP CHECK",
   "quote": "A missed beep can happen, but look at the times: from CP1 to CP3 is six kilometres. Bib 117 did it in under eighteen minutes – that's faster than a world-class runner.",
   "evidence": ev_rows("Chip system note", [
       ("CP2 beeps", "All other 299 runners recorded at CP2"),
       ("CP1 → CP3", "6 km in 17 min 40 s for bib 117"),
       ("World record pace", "About 16 min for 6 km"),
     ])},
  {"name": "Bev Shah", "role": "Bus driver", "label": "BUS TICKET",
   "quote": "A man in a Santa suit got on my bus at the Mill Road stop just after quarter past ten and got off at the Riverside stop. He paid by card.",
   "evidence": ev_rows("Bus ticket – route 6", [
       ("Boarded", "Mill Road, 10:16 (next to CP1)"),
       ("Got off", "Riverside, 10:24 (next to CP3)"),
       ("Card", "C. DUNN"),
     ])},
  {"name": "Asha Rai", "role": "Second-place runner", "label": "ASHA'S STATEMENT",
   "quote": "Nobody passed me after the first kilometre – and I was in front of everyone after CP1. Then at the finish, Craig was already there.",
   "evidence": ev_photos("Race photographer", [
       ("IMG_2201", "10:12", "CP1 to CP2 stretch: Asha Rai (bib 54) leading. No other runner in sight."),
       ("IMG_2207", "10:25", "Riverside bus stop: a Santa with bib 117 stepping off a route 6 bus."),
     ])},
  {"name": "Will Ford", "role": "Third-place runner", "label": "WILL'S STATEMENT",
   "quote": "I'm happy with third. I had a twisted ankle at 5 km and walked a bit, so my time was slow.",
   "evidence": ev_table("Chip times – bib 208", ["Checkpoint", "Time"], [
       ("CP1", "10:11:50"),
       ("CP2", "10:25:10"),
       ("CP3", "10:32:40"),
       ("Finish", "10:36:15"),
     ])},
 ],
 "solution": {"killer": "Craig Dunn",
   "motive": "Craig wanted the £500 prize and the course record (clue 1).",
   "proof": ["Craig's chip has no beep at CP2, the only runner of 300 to miss it, and his CP1 to CP3 time is faster than world-record pace (clues 2, 3).",
             "Craig says he ran every step, but a card in his name rode the route 6 bus from Mill Road (by CP1) at 10:16 to Riverside (by CP3) at 10:24 (clue 4).",
             "A photo shows a Santa with bib 117 getting off the bus at Riverside at 10:25 (clue 5)."],
   "cleared": ["<b>Asha</b> was photographed leading on the course, and <b>Will</b>'s chip beeped at every checkpoint (clues 5, 6).",
               "<b>Helen</b>, <b>Ray</b> and <b>Bev</b> only report what they found (clues 1, 3, 4)."]},
}

# ---------------------------------------------------------------- AQUARIUM (L2)
aquarium = {
 "slug": "the-aquarium-pearl-theft", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 191", "title_html": "THE AQUARIUM<br>PEARL THEFT", "title_plain": "The Aquarium Pearl Theft",
 "teaser": "A giant black pearl vanishes from the aquarium's shipwreck tank during feeding time. A wet suit, a feeding rota and a door code lead to the thief.",
 "intro": "At the <b>Seacliff Aquarium</b>, the famous Black Moon pearl was displayed inside a treasure chest in the shipwreck tank. During the 15:00 shark feeding show, it disappeared. " + STD,
 "clues": [
  {"name": "Dr Ann Moore", "role": "Aquarium director", "label": "DIRECTOR'S REPORT",
   "quote": "The pearl was in the chest at the start of the feeding show. At the end, the chest was empty – and you can only reach it by diving into the tank from the service room above.",
   "evidence": ev_rows("Director's report", [
       ("Pearl seen", "15:00, start of feeding show"),
       ("Missing", "15:30"),
       ("Access", "Only by diving from the service room above the tank"),
       ("Service room door", "Keypad – every keeper has a personal code"),
     ])},
  {"name": "Jake Marsh", "role": "Aquarist", "label": "JAKE'S STATEMENT",
   "quote": "I was on the stage doing the shark show with Pia the whole time. I never went up to the service room.",
   "evidence": ev_rows("Jake's bank letter", [
       ("Subject", "Final warning – overdue loan"),
       ("Owed", "£9,400"),
       ("Date", "One week before"),
     ])},
  {"name": "Pia Lund", "role": "Show presenter", "label": "SHOW SCRIPT",
   "quote": "Jake did the first part with me, then he said he had to fetch more fish. I did the rest on my own – the audience didn't mind.",
   "evidence": ev_table("Feeding show – as it happened", ["Time", "On stage"], [
       ("15:00–15:08", "P. Lund, J. Marsh"),
       ("15:08–15:24", "P. Lund only – 'Jake fetching fish'"),
       ("15:24–15:30", "P. Lund, J. Marsh"),
     ], mono_cols=(0,))},
  {"name": "Omar Haddad", "role": "Security", "label": "DOOR LOG",
   "quote": "The service room keypad records every code. Only one keeper went in during the show.",
   "evidence": ev_table("Service room – keypad log", ["Time", "Code", "Keeper"], [
       ("14:30", "2201", "O. Kerr"),
       ("15:10", "4417", "J. Marsh"),
       ("15:21", "Exit", "–"),
     ], mono_cols=(0, 1))},
  {"name": "Olive Kerr", "role": "Keeper", "label": "OLIVE'S STATEMENT",
   "quote": "I checked the filters in the service room at half past two and left at twenty to three. After that I was in the café on my break – the café till has my staff discount at five past three.",
   "evidence": ev_rows("Café till", [
       ("15:05", "Staff discount – O. Kerr – tea and scone"),
       ("15:40", "Staff discount – O. Kerr – second tea"),
     ])},
  {"name": "Ben Clay", "role": "Cleaner", "label": "CLEANER'S NOTE",
   "quote": "When I went into the staff changing room at half past three, there was a wet wetsuit hanging in a locker that had been dry this morning.",
   "evidence": ev_photos("Ben's phone", [
       ("IMG_6090", "15:32", "Staff locker 6 open: a dripping wetsuit and a small velvet pouch on the shelf. Name tag on the locker: J. MARSH."),
     ])},
 ],
 "solution": {"killer": "Jake Marsh",
   "motive": "Jake owed £9,400 and had a final warning from the bank (clue 2).",
   "proof": ["The pearl went during the show and could only be reached by diving from the service room (clue 1).",
             "Jake says he never left the stage, but he was away from 15:08 to 15:24 'fetching fish' (clue 3), and his code opened the service room at 15:10 (clue 4).",
             "At 15:32 his locker held a dripping wetsuit and a velvet pouch (clue 6)."],
   "cleared": ["<b>Olive</b> left the service room before the show and was in the café at 15:05 (clues 4, 5).",
               "<b>Pia</b> was on stage the whole time; <b>Omar</b>, <b>Ben</b> and <b>Dr Moore</b> only report what they saw (clues 3, 4, 6)."]},
}

# ---------------------------------------------------------------- CHEESE CAVES (L3)
cheese = {
 "slug": "death-in-the-cheese-caves", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 192", "title_html": "DEATH IN THE<br>CHEESE CAVES", "title_plain": "Death in the Cheese Caves",
 "teaser": "A cheese maker is found dead deep in the caves where his famous cheddar ripens. A tour timetable, a turning log and chalk dust on a sleeve reveal the killer.",
 "intro": "At the <b>Gorge Cheese Caves</b>, master cheese maker Harold Pike was found dead in the deepest chamber, struck with a heavy cheese iron. " + STD,
 "clues": [
  {"name": "DS Rhiannon Bell", "role": "Police", "label": "POLICE REPORT",
   "quote": "Harold had been turning the cheeses – he writes the time on each shelf in chalk. The last mark is 14:20. The shelf after that was never turned.",
   "evidence": ev_rows("Police report – deepest chamber", [
       ("Found", "16:05"),
       ("Turning log", "Last chalk mark 14:20, shelf 12 – shelf 13 not turned"),
       ("So he died", "Soon after 14:20 (he turns a shelf every 5 minutes)"),
       ("Weapon", "Cheese iron – long steel tester"),
     ])},
  {"name": "Simon Pike", "role": "Harold's son", "label": "SIMON'S STATEMENT",
   "quote": "I was guiding the two o'clock cave tour. Forty people saw me – it lasts an hour and I never leave the group.",
   "evidence": ev_rows("Harold's letter to his lawyer", [
       ("Subject", "The cheese business"),
       ("Text", "“Leave the caves to my daughter Kate, not Simon – he wants to sell to a factory.”"),
       ("Date", "Posted the day before"),
     ])},
  {"name": "Tilly Moss", "role": "Tour shop manager", "label": "TOUR TIMETABLE",
   "quote": "The two o'clock tour was run by a recorded audio guide for the middle part. Guides often slip out then for a break.",
   "evidence": ev_table("Cave tour – 14:00", ["Time", "Part", "Guide needed?"], [
       ("14:00–14:10", "Welcome and history", "Yes"),
       ("14:10–14:35", "Audio guide walk – the river chamber", "No"),
       ("14:35–15:00", "Cheese tasting", "Yes"),
     ], mono_cols=(0,))},
  {"name": "Gareth Lloyd", "role": "Tour visitor", "label": "VISITOR NOTE",
   "quote": "During the audio part, our guide said 'enjoy the river, back soon' and went off into a side tunnel marked 'Staff only'. He came back just before the tasting, out of breath.",
   "evidence": ev_note("GARETH'S HOLIDAY DIARY", [
       "Cave tour, 2pm. Guide left us at",
       "about 14:12 down the 'Staff only'",
       "tunnel. Back at 14:33 with white",
       "chalk dust on his sleeve."],
     "– Gareth")},
  {"name": "Kate Pike", "role": "Harold's daughter", "label": "KATE'S STATEMENT",
   "quote": "I was in the dairy on the farm making the next batch all afternoon. The milk tanks log every time someone opens them.",
   "evidence": ev_table("Dairy tank log", ["Time", "Tank", "Opened by"], [
       ("14:05", "Tank 1", "K. Pike"),
       ("14:25", "Tank 2", "K. Pike"),
       ("14:45", "Tank 1", "K. Pike"),
     ], note="The dairy is a 20-minute drive from the caves.")},
  {"name": "Dai Evans", "role": "Cave maintenance", "label": "TUNNEL MAP",
   "quote": "The 'Staff only' tunnel from the river chamber leads straight to the deepest chamber – five minutes' walk. Nobody else uses it.",
   "evidence": ev_rows("Cave map – staff routes", [
       ("River chamber → deepest chamber", "Staff tunnel, 5 minutes"),
       ("Main entrance → deepest chamber", "15 minutes, past the shop"),
       ("Dai's afternoon", "Fixing lights in the shop tunnel 13:30–15:00 – nobody passed"),
     ])},
 ],
 "solution": {"killer": "Simon Pike",
   "motive": "Harold was leaving the caves to Kate instead of Simon (clue 2).",
   "proof": ["Harold died soon after 14:20 in the deepest chamber (clue 1).",
             "Simon says he never left his tour group, but the middle of the tour ran on an audio guide from 14:10 to 14:35 (clue 3), and he went down the 'Staff only' tunnel from 14:12 to 14:33 (clue 4).",
             "That tunnel leads to the deepest chamber in five minutes (clue 6), and Simon came back with chalk dust on his sleeve – the chalk Harold used to mark the shelves (clues 1, 4)."],
   "cleared": ["<b>Kate</b> was opening dairy tanks at 14:25, 20 minutes' drive away (clue 5).",
               "Nobody passed <b>Dai</b> in the shop tunnel (clue 6); <b>Tilly</b> and <b>Gareth</b> only report what they know."]},
}

# ---------------------------------------------------------------- RECORDING STUDIO (L3)
studio = {
 "slug": "murder-at-the-recording-studio", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 193", "title_html": "MURDER AT THE<br>RECORDING STUDIO", "title_plain": "Murder at the Recording Studio",
 "teaser": "A record producer is found dead in the tape store during a band's Christmas single session. The recording itself holds the clue that breaks one alibi.",
 "intro": "At <b>Echo Lane Studios</b>, producer Miles Garner was found dead in the tape store while the band Glass Harbour recorded their Christmas single. He had been strangled with a guitar cable. " + STD,
 "clues": [
  {"name": "DI Grace Obi", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Garner was killed between 22:10 and 22:30. He was last heard on the studio talkback at 22:10 saying he'd 'fetch the old master tapes'.",
   "evidence": ev_rows("Police report – Echo Lane Studios", [
       ("Last heard", "22:10 on talkback"),
       ("Found", "22:50, tape store"),
       ("Time of death", "Between 22:10 and 22:30"),
       ("Weapon", "Guitar cable – yellow, 6 m"),
     ])},
  {"name": "Rory Blake", "role": "Guitarist", "label": "RORY'S STATEMENT",
   "quote": "I was in the live room recording my guitar solo the whole time. It's on the tape – take after take, you can hear me.",
   "evidence": ev_rows("Glass Harbour contract", [
       ("Clause 9", "Producer M. Garner owns the rights to all songs written in the studio"),
       ("Rory's note", "“He stole my song. I'll never let him have it.”"),
     ])},
  {"name": "Jas Kaur", "role": "Sound engineer", "label": "TAKE SHEET",
   "quote": "Rory recorded six takes. But takes 4 and 5 are the same recording – the same tiny mistake at the same second. Someone copied take 3 twice.",
   "evidence": ev_table("Guitar solo – take sheet", ["Take", "Time", "Note"], [
       ("1", "21:50", "Live"),
       ("2", "22:00", "Live"),
       ("3", "22:08", "Live"),
       ("4", "22:15", "Copy of take 3 – same mistake at 0:41"),
       ("5", "22:22", "Copy of take 3 – same mistake at 0:41"),
       ("6", "22:31", "Live – out of breath at the start"),
     ], mono_cols=(0, 1))},
  {"name": "Lou Hart", "role": "Singer", "label": "LOU'S STATEMENT",
   "quote": "I was in the vocal booth the whole evening. It's soundproof and locked from inside. I didn't hear a thing.",
   "evidence": ev_table("Vocal booth door log", ["Time", "Event"], [
       ("21:30", "Locked from inside"),
       ("22:55", "Opened (police knock)"),
     ], mono_cols=(0,))},
  {"name": "Theo Grant", "role": "Drummer", "label": "THEO'S NOTE",
   "quote": "I was having a smoke out the back. At about quarter past ten I saw Rory come out of the live room carrying a coiled yellow cable, heading for the tape store corridor.",
   "evidence": ev_note("THEO'S NOTE", [
       "About 22:13 – Rory out of live",
       "room with yellow cable. Didn't",
       "come back past me until 22:29.",
       "Smoked 3 cigarettes – bored."],
     "– Theo")},
  {"name": "Nell Fox", "role": "Studio manager", "label": "CABLE LIST",
   "quote": "Every cable is colour-coded by room. The yellow six-metre cables belong to the live room only.",
   "evidence": ev_table("Cable colours", ["Colour", "Room"], [
       ("Yellow", "Live room (guitars)"),
       ("Red", "Vocal booth"),
       ("Blue", "Drum room"),
     ])},
 ],
 "solution": {"killer": "Rory Blake",
   "motive": "Miles owned the rights to Rory's song (clue 2).",
   "proof": ["Miles was killed between 22:10 and 22:30 with a yellow guitar cable (clue 1), and yellow cables belong only to the live room, where Rory was (clue 6).",
             "Rory says the tape proves he was playing, but takes 4 and 5 at 22:15 and 22:22 are copies of take 3 – no live playing between 22:08 and 22:31, when he came back out of breath (clue 3).",
             "Theo saw Rory leave the live room with a yellow cable at 22:13 and not come back until 22:29 (clue 5)."],
   "cleared": ["<b>Lou</b> was locked in the vocal booth from 21:30 to 22:55 (clue 4).",
               "<b>Theo</b> was smoking out the back, and <b>Jas</b> and <b>Nell</b> only report what they found (clues 3, 5, 6)."]},
}

MYSTERIES = [funrun, aquarium, cheese, studio]
