from lib import *  # evidence helpers

# Round 26 (18 Nov): 1 Rookie, 1 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- EASTER EGG HUNT (L1)
easter = {
 "slug": "the-easter-egg-hunt", "level": 1, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 166", "title_html": "THE EASTER<br>EGG HUNT", "title_plain": "The Easter Egg Hunt",
 "teaser": "The giant golden egg for the village Easter hunt disappears from the vicarage the night before. Chocolate fingerprints and a bunny costume point the way.",
 "intro": "In <b>Brambleford</b>, the star prize of the Easter egg hunt – a giant golden chocolate egg – vanished from the vicarage kitchen on Saturday evening. " + STD,
 "clues": [
  {"name": "Rev. Clare Webb", "role": "Vicar", "label": "VICARAGE REPORT",
   "quote": "The golden egg was on my kitchen table at six. When I came back from evensong at half seven, the box was empty and there was white fluff on the floor.",
   "evidence": ev_rows("Vicarage report", [
       ("Egg on table", "18:00"),
       ("Gone", "19:30"),
       ("On the floor", "Tufts of white fake fur"),
       ("Back door", "Left unlocked – the vicar always does on Saturdays"),
     ])},
  {"name": "Barney Hale", "role": "Easter Bunny volunteer", "label": "BARNEY'S STATEMENT",
   "quote": "I was at evensong in the front pew, singing my heart out. I haven't even put my bunny suit on since last Easter.",
   "evidence": ev_rows("Barney Hale – the hunt", [
       ("Job", "Plays the Easter Bunny who hides the eggs"),
       ("Last year", "Complained he never gets a chocolate egg himself"),
     ])},
  {"name": "Mrs Edna Pike", "role": "Church warden", "label": "EVENSONG REGISTER",
   "quote": "I count everyone who comes to evensong. Barney signed in – but he slipped out during the first hymn and came back for the blessing.",
   "evidence": ev_table("Evensong – Saturday", ["Time", "Note"], [
       ("18:30", "Service starts – 14 people incl. B. Hale"),
       ("18:35", "B. Hale leaves during first hymn"),
       ("19:15", "B. Hale returns for the blessing"),
     ], mono_cols=(0,))},
  {"name": "Tilly Moss", "role": "Village shopkeeper", "label": "COSTUME BOX",
   "quote": "The bunny costume lives in a box in the church hall. When I went to get the Easter bonnets out, the costume was damp and had chocolate on the paws.",
   "evidence": ev_rows("Church hall costume box – Sunday morning", [
       ("Bunny costume", "Damp, chocolate smears on both paws"),
       ("Fur", "White fake fur, shedding"),
       ("Size label", "Made to fit B. Hale"),
     ])},
  {"name": "Mr Ken Rhodes", "role": "Neighbour", "label": "KEN'S NOTE",
   "quote": "I was walking my dog at about quarter to seven and saw a big white rabbit hopping out of the vicarage gate with a box. I thought I was dreaming.",
   "evidence": ev_note("KEN'S NOTE", [
       "About 18:45 – a person in a",
       "white bunny suit came out of the",
       "vicarage back gate carrying a box.",
       "Went towards the church hall."],
     "– Ken, dog-walker")},
  {"name": "Gemma Lyle", "role": "Hunt organiser", "label": "HALL KEY BOOK",
   "quote": "Only two people have a key to the church hall this week: me and the Easter Bunny, so he can get his costume.",
   "evidence": ev_table("Church hall keys", ["Key", "Holder"], [
       ("1", "G. Lyle"),
       ("2", "B. Hale (Easter Bunny)"),
     ])},
 ],
 "solution": {"killer": "Barney Hale",
   "motive": "Barney complained that he never gets a chocolate egg himself (clue 2).",
   "proof": ["The egg went between 18:00 and 19:30, leaving white fake fur on the floor (clue 1).",
             "Barney says he sang through evensong, but he left at 18:35 and came back at 19:15 (clue 3).",
             "At 18:45 Ken saw someone in a white bunny suit carry a box towards the church hall (clue 5). The bunny costume – made to fit Barney – was damp with chocolate on the paws (clue 4), and only Barney and Gemma have hall keys (clue 6)."],
   "cleared": ["<b>Rev. Webb</b> and <b>Mrs Pike</b> were at evensong the whole time (clues 1, 3).",
               "<b>Gemma</b>'s key was with her, and the costume doesn't fit her; <b>Tilly</b> and <b>Ken</b> only report what they found and saw (clues 4, 5, 6)."]},
}

# ---------------------------------------------------------------- VINYL RECORDS (L2)
vinyl = {
 "slug": "the-vanishing-vinyl", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 167", "title_html": "THE VANISHING<br>VINYL", "title_plain": "The Vanishing Vinyl",
 "teaser": "A rare signed record worth £12,000 disappears from a record shop during an in-store gig. The playlist, a power cut and a guitar case hide the truth.",
 "intro": "At <b>Groove Records</b>, a signed first pressing of a famous 1960s album, worth £12,000, vanished from its locked display case during a busy in-store gig. " + STD,
 "clues": [
  {"name": "Della King", "role": "Shop owner", "label": "THEFT REPORT",
   "quote": "The record was in its case at seven when the band started. During the song where all the lights went out for effect, someone opened the case. When the lights came back, it was empty.",
   "evidence": ev_rows("Theft report", [
       ("Gig", "19:00–20:00, 80 people in the shop"),
       ("Lights out", "One song only – a 'blackout' effect"),
       ("Display case", "Opened with its key – not forced"),
       ("Case keys", "Della (on her belt) and a spare on a hook behind the counter"),
     ])},
  {"name": "Rich Stone", "role": "Band's guitarist", "label": "SET LIST",
   "quote": "I was on stage playing the whole gig. I never stopped playing, not for a second. Ask anyone in the crowd.",
   "evidence": ev_programme("Set list – The Night Owls", "Groove Records gig", [
       ("19:00", "Song 1–4"),
       ("19:22", "'Midnight Hour' – blackout effect, 4 minutes, backing track only, band off stage"),
       ("19:26", "Song 6–10"),
     ], None)},
  {"name": "Kofi Mensah", "role": "Sound engineer", "label": "SOUND DESK NOTE",
   "quote": "During 'Midnight Hour' the band leaves the stage and I play a recording in the dark. It's a trick to make the crowd scream when they come back.",
   "evidence": ev_note("SOUND DESK LOG", [
       "19:22 Lights off, backing track on.",
       "Band off – Rich went behind the counter",
       "'to get a plectrum', not the side door.",
       "19:26 Lights on, band back."],
     "– Kofi")},
  {"name": "Ivy Jones", "role": "Shop assistant", "label": "SPARE KEY",
   "quote": "I was at the till by the door all night selling T-shirts. After the gig I noticed the spare key wasn't on its hook any more.",
   "evidence": ev_rows("Behind the counter – after the gig", [
       ("Spare case key", "Missing from its hook"),
       ("Found later", "In the lining of a guitar case, with the record"),
       ("Guitar case", "Belongs to R. Stone"),
     ])},
  {"name": "Sean Cole", "role": "Collector", "label": "MESSAGES",
   "quote": "I've wanted that record for years. A guitarist messaged me last week asking what I'd pay for a signed first pressing, 'no questions asked'.",
   "evidence": ev_note("MESSAGES ON SEAN'S PHONE", [
       "Rich S: What would you pay for a signed",
       "first pressing? No paperwork.",
       "Sean: £8k cash if it's real.",
       "Rich S: Saturday."],
     "– from Sean's phone")},
  {"name": "Maya King", "role": "Della's daughter, ticket desk", "label": "TICKET DESK",
   "quote": "I was on the ticket desk at the door all evening. Nobody left the shop during the blackout – the door has a loud bell.",
   "evidence": ev_rows("Door bell log", [
       ("19:20–19:30", "No door openings"),
       ("Note", "So the thief was someone already inside"),
     ])},
 ],
 "solution": {"killer": "Rich Stone",
   "motive": "Rich had arranged to sell a signed first pressing to a collector for £8,000 cash, 'no paperwork' (clue 5).",
   "proof": ["The case was opened with a key during the blackout song (clue 1). Nobody left the shop then (clue 6).",
             "Rich says he never stopped playing, but during 'Midnight Hour' the band left the stage for 4 minutes (clue 2), and Rich went behind the counter – where the spare key hangs (clues 1, 3).",
             "The spare key and the record were found in the lining of Rich's guitar case (clue 4)."],
   "cleared": ["<b>Della</b> kept her key on her belt, <b>Ivy</b> was at the till, and <b>Maya</b> was on the ticket desk (clues 1, 4, 6).",
               "<b>Kofi</b> was at the sound desk running the blackout (clue 3), and <b>Sean</b> was only offered the record (clue 5)."]},
}

# ---------------------------------------------------------------- SAUNA (L3)
sauna = {
 "slug": "death-in-the-sauna", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 168", "title_html": "DEATH IN<br>THE SAUNA", "title_plain": "Death in the Sauna",
 "teaser": "A tech millionaire is found dead in a hotel sauna that someone locked from outside. The thermostat log, a towel and a wristband reveal who was there.",
 "intro": "At the <b>Nordlys Spa Hotel</b> in Bergen, tech investor Henrik Vold was found dead in the private sauna. The door had been jammed shut and the heat turned to maximum. " + STD,
 "clues": [
  {"name": "Insp. Kari Berg", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Vold was trapped. The handle was jammed from outside with a towel rail, and the thermostat was turned up from the control panel outside the door.",
   "evidence": ev_rows("Police report – Nordlys Spa", [
       ("Found", "21:45, private sauna"),
       ("Door", "Jammed from outside with a towel rail"),
       ("Thermostat", "Changed at the outside panel – see spa log"),
       ("Access", "Spa doors open only with guest wristbands"),
     ])},
  {"name": "Mona Lie", "role": "Business partner", "label": "MONA'S STATEMENT",
   "quote": "I left the spa at eight and went straight to my room to prepare for tomorrow's board meeting. I didn't go back down at all.",
   "evidence": ev_rows("Board meeting agenda – tomorrow", [
       ("Item 1", "Henrik Vold proposes to remove M. Lie as CEO"),
       ("Item 2", "Vote: Henrik holds 51% of the shares"),
       ("If Vold dies", "His shares pass to the company trust – Mona chairs it"),
     ])},
  {"name": "Erik Dahl", "role": "Spa attendant", "label": "SAUNA LOG",
   "quote": "The sauna panel logs every change, and the wristband reader logs who opens the spa door. I was in the towel room at the back most of the evening.",
   "evidence": ev_table("Sauna control panel", ["Time", "Change"], [
       ("20:30", "Private sauna on – 80 °C (H. Vold)"),
       ("21:02", "Temperature → 110 °C (outside panel)"),
       ("21:03", "Safety cut-out disabled (outside panel)"),
     ], mono_cols=(0,))},
  {"name": "Lars Moen", "role": "Henrik's assistant", "label": "WRISTBAND LOG",
   "quote": "I was in the hotel bar until ten waiting for Henrik to call me. He never did.",
   "evidence": ev_table("Spa door – wristbands", ["Time", "Wristband", "Guest"], [
       ("20:25", "Room 501", "H. Vold"),
       ("20:58", "Room 412", "M. Lie"),
       ("21:06", "Room 412", "M. Lie – out"),
       ("21:45", "Staff", "E. Dahl"),
     ], mono_cols=(0,))},
  {"name": "Siri Holm", "role": "Bar manager", "label": "BAR TILL",
   "quote": "Lars sat at the end of the bar all evening on his laptop. He ordered coffee after coffee.",
   "evidence": ev_table("Hotel bar – till", ["Time", "Order", "Room"], [
       ("20:40", "Espresso", "Room 318 – L. Moen"),
       ("21:05", "Espresso", "Room 318 – L. Moen"),
       ("21:30", "Espresso", "Room 318 – L. Moen"),
     ], mono_cols=(0,))},
  {"name": "Anna Strand", "role": "Housekeeper", "label": "TOWEL NOTE",
   "quote": "When I turned down Room 412 at quarter past nine, there was a damp spa towel on the floor and a pair of spa slippers by the door, still wet.",
   "evidence": ev_note("HOUSEKEEPING NOTE – ROOM 412", [
       "21:15 – turndown:",
       "1 damp Nordlys spa towel on floor,",
       "1 pair spa slippers, wet soles.",
       "Guest not in room – shower running."],
     "– Anna")},
 ],
 "solution": {"killer": "Mona Lie",
   "motive": "Henrik was about to remove Mona as CEO at tomorrow's board meeting – and if he died, his shares would pass to a trust she chairs (clue 2).",
   "proof": ["Henrik was trapped in the sauna, and the heat was raised and the safety cut-out disabled at the outside panel at 21:02–21:03 (clues 1, 3).",
             "Mona says she never went back down after eight. But her wristband opened the spa door at 20:58 and she left at 21:06 (clue 4).",
             "At 21:15 her room held a damp spa towel and wet spa slippers (clue 6)."],
   "cleared": ["<b>Lars</b> was in the bar buying espressos at 20:40, 21:05 and 21:30 (clue 5).",
               "<b>Erik</b> was in the towel room and only entered at 21:45 when he found Henrik (clue 4); <b>Siri</b> and <b>Anna</b> were working in the bar and the rooms."]},
}

# ---------------------------------------------------------------- MODEL VILLAGE (L3)
modelv = {
 "slug": "murder-at-the-model-village", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 169", "title_html": "MURDER AT THE<br>MODEL VILLAGE", "title_plain": "Murder at the Model Village",
 "teaser": "The owner of a seaside model village is found dead among the tiny houses. The miniature railway's timetable and a tiny clock tower hold the clues.",
 "intro": "At <b>Bayview Model Village</b>, owner Cyril Moss was found dead behind the miniature church, struck on the head, shortly after closing time. " + STD,
 "clues": [
  {"name": "DS Joanna Price", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Moss was struck behind the miniature church. When he fell, he knocked the tiny clock tower off its base – its little working clock stopped when it hit the ground.",
   "evidence": ev_rows("Police report – Bayview Model Village", [
       ("Found", "17:40, behind the miniature church"),
       ("Model clock tower", "Knocked over, stopped at 17:12"),
       ("Gate", "Locked at 17:00 – only staff with keys inside"),
       ("Weapon", "A model-railway track spanner"),
     ])},
  {"name": "Dennis Kerr", "role": "Model railway engineer", "label": "DENNIS'S STATEMENT",
   "quote": "I was in the railway shed the whole time from five, oiling the engines. The trains run on their own schedule – you'd have heard me if I'd stopped them.",
   "evidence": ev_rows("Model village – partnership", [
       ("Owners", "C. Moss 70%, D. Kerr 30%"),
       ("Moss's plan", "Sell the land to a hotel group – the railway would be scrapped"),
       ("Kerr, to a friend", "“Over my dead body – or his.”"),
     ])},
  {"name": "Pearl Jones", "role": "Café manager", "label": "TRAIN TIMETABLE",
   "quote": "After closing the little trains keep running round the village on a timer while Dennis services them. You can hear them from my café.",
   "evidence": ev_table("Miniature railway controller – after closing", ["Time", "Event"], [
       ("17:00", "Timetable mode – trains run automatically"),
       ("17:08", "Manual stop – controller in the shed left unattended"),
       ("17:20", "Manual restart"),
     ], mono_cols=(0,))},
  {"name": "Gary Lomas", "role": "Gardener", "label": "SHED KEY",
   "quote": "I was trimming the tiny hedges near the harbour model until ten past five, then I went home. I saw Dennis carrying a spanner past the church at about ten past.",
   "evidence": ev_table("Staff gate – after closing", ["Time", "Key", "Name"], [
       ("17:00", "Gate locked", "C. Moss"),
       ("17:11", "Out", "G. Lomas"),
       ("17:45", "In", "Police"),
     ], mono_cols=(0,))},
  {"name": "Rita Moss", "role": "Cyril's daughter", "label": "PHONE CALL",
   "quote": "Dad rang me at five past five to say he was 'going to have it out with Dennis' about the sale. I was at home in Exeter, two hours away.",
   "evidence": ev_table("Rita's phone – incoming", ["Time", "Caller", "Length"], [
       ("17:05", "Dad", "3 min"),
     ], mono_cols=(0,))},
  {"name": "Owen Tate", "role": "Security firm operator", "label": "CAFÉ CAMERA",
   "quote": "I watch the model village cameras remotely after closing. The café camera points out over the village – you can just see the church from it.",
   "evidence": ev_photos("Café camera", [
       ("CAM-1", "17:10", "A man in blue overalls with an oily rag in his pocket walks towards the miniature church."),
       ("CAM-1", "17:12", "In the corner of the frame: Pearl Jones behind the café counter, cashing up."),
       ("CAM-1", "17:14", "The same man hurries back towards the railway shed."),
     ])},
 ],
 "solution": {"killer": "Dennis Kerr",
   "motive": "Cyril planned to sell the land and scrap the railway; Dennis said it would be 'over my dead body – or his' (clue 2).",
   "proof": ["Cyril was struck at 17:12, when the model clock tower fell (clue 1). The gate was locked at 17:00, so only staff were inside (clues 1, 4).",
             "Dennis says he never left the shed, but the trains were stopped by hand at 17:08 and only restarted at 17:20 (clue 3).",
             "At 17:10 Gary saw Dennis carrying a spanner past the church, and the café camera shows a man in oily overalls going to the church at 17:10 and hurrying back to the railway shed at 17:14 (clues 4, 6)."],
   "cleared": ["<b>Gary</b> left through the gate at 17:11, before Cyril was struck (clue 4).",
               "<b>Rita</b> was in Exeter (clue 5), <b>Pearl</b> was cashing up in her café at 17:12 (clue 6), and <b>Owen</b> watches the cameras remotely."]},
}

MYSTERIES = [easter, vinyl, sauna, modelv]
