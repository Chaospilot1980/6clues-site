from lib import *  # evidence helpers

# Round 43 (18 Nov): final 6 Mastermind cases → 200.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- OIL RIG
rig = {
 "slug": "death-on-the-oil-rig", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 234", "title_html": "DEATH ON<br>THE OIL RIG", "title_plain": "Death on the Oil Rig",
 "teaser": "A safety inspector falls from a North Sea oil rig in a storm. The shift board, a helicopter manifest and a hard hat number reveal who was out on deck with him.",
 "intro": "On the <b>Brenna Alpha</b> oil rig in the North Sea, safety inspector Callum Ross fell from the cellar deck into the sea during a storm. A struggle had taken place on the deck. " + STD,
 "clues": [
  {"name": "DI Fiona Strachan", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Ross went over the rail on the cellar deck between 02:00 and 02:20. A hard hat was found jammed under the rail – number 31.",
   "evidence": ev_rows("Police report – Brenna Alpha", [
       ("Fell", "02:00–02:20, cellar deck"),
       ("Rail", "Struggle marks"),
       ("Found", "Hard hat No. 31 under the rail"),
       ("Weather", "Storm – deck closed to all but the night crew"),
     ])},
  {"name": "Gordon Bain", "role": "Rig manager", "label": "GORDON'S STATEMENT",
   "quote": "I was asleep in my cabin from midnight. I only heard about it at breakfast.",
   "evidence": ev_rows("Callum Ross's draft report", [
       ("Finding", "Rig manager G. Bain switched off gas alarms to save money"),
       ("Action", "“Rig to be shut down. Bain to be reported to the safety authority.”"),
       ("Due", "Next morning"),
     ])},
  {"name": "Shona Kerr", "role": "Night shift supervisor", "label": "SHIFT BOARD",
   "quote": "Everyone on deck signs the shift board. The night crew was three people – and at about two o'clock a fourth name went on it.",
   "evidence": ev_table("Cellar deck – sign-in board", ["Time", "Name", "Hard hat"], [
       ("00:00", "S. Kerr", "12"),
       ("00:00", "D. Watt", "14"),
       ("00:00", "C. Ross (inspection)", "22"),
       ("01:58", "G. Bain – 'checking valves'", "31"),
     ], mono_cols=(0, 2))},
  {"name": "Dougie Watt", "role": "Roustabout", "label": "DOUGIE'S NOTE",
   "quote": "I was at the pump room with Shona from two until half past – the pump was leaking. When I came out the inspector was gone, and the manager was heading back inside soaking wet.",
   "evidence": ev_note("DOUGIE'S NOTE", [
       "02:25 – manager Bain coming in from",
       "the cellar deck, soaked, no hard hat,",
       "cut on his hand. Said 'Go back to",
       "work, Dougie.'"],
     "– Dougie")},
  {"name": "Ali Hassan", "role": "Rig medic", "label": "MEDIC'S LOG",
   "quote": "At half past two Mr Bain came to me with a cut hand. He said he'd caught it on his cabin door.",
   "evidence": ev_rows("Medical log", [
       ("02:30", "G. Bain – deep cut, right palm, rust in wound"),
       ("Note", "Rust – like the deck rail, not a cabin door"),
     ])},
  {"name": "Erin Hale", "role": "Helicopter pilot", "label": "FLIGHT MANIFEST",
   "quote": "No helicopter flew that night – the storm grounded us. Nobody came or left the rig.",
   "evidence": ev_rows("Helicopter manifest", [
       ("Last flight", "18:00 – landed"),
       ("Night", "No flights – storm"),
       ("On board", "64 crew, all accounted for"),
     ])},
 ],
 "solution": {"killer": "Gordon Bain",
   "motive": "Callum was going to report Gordon for switching off the gas alarms and shut the rig down (clue 2).",
   "proof": ["Callum went over the rail between 02:00 and 02:20; hard hat No. 31 was under the rail (clue 1).",
             "Gordon says he was asleep from midnight, but he signed onto the cellar deck at 01:58 with hard hat 31 (clue 3).",
             "At 02:25 Dougie saw him come in soaked, without a hat and with a cut hand (clue 4), and the medic found rust in the cut like the deck rail (clue 5)."],
   "cleared": ["<b>Shona</b> and <b>Dougie</b> were in the pump room from 02:00 to 02:30 (clue 4).",
               "Nobody arrived or left the rig (clue 6); <b>Ali</b> and <b>Erin</b> only report what they found."]},
}

# ---------------------------------------------------------------- WAXWORKS
wax = {
 "slug": "murder-at-the-waxworks", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 235", "title_html": "MURDER AT<br>THE WAXWORKS", "title_plain": "Murder at the Waxworks",
 "teaser": "The waxworks owner is found dead among his own figures after a late-night unveiling. One 'wax figure' moved – and the motion sensor proves who was posing.",
 "intro": "At <b>Madame Fontaine's Waxworks</b>, owner Felix Fontaine was found dead in the Hall of Villains after the unveiling of a new figure. He had been struck with a wax candlestick weighted with lead. " + STD,
 "clues": [
  {"name": "DS Leo Grant", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Fontaine died in the Hall of Villains between 22:00 and 22:20, after the guests had left. The doors were locked at 22:00 – the killer was already inside.",
   "evidence": ev_rows("Police report – Fontaine's Waxworks", [
       ("Doors locked", "22:00"),
       ("Time of death", "22:00–22:20"),
       ("Weapon", "Lead-weighted candlestick from the display"),
       ("Strange", "One empty plinth in the hall – figure missing"),
     ])},
  {"name": "Margot Fontaine", "role": "Felix's wife, sculptor", "label": "MARGOT'S STATEMENT",
   "quote": "I left with the last guests at ten and drove home. I was in bed by half past.",
   "evidence": ev_rows("Felix's notes", [
       ("To", "His lawyer"),
       ("Text", "“I'm divorcing Margot and taking back the waxworks. She gets nothing.”"),
       ("Date", "That morning"),
     ])},
  {"name": "Tom Pike", "role": "Night guard", "label": "MOTION SENSOR",
   "quote": "The hall has motion sensors. After 22:00 nothing should move but Mr Fontaine – but one sensor fired by plinth 7, where a wax figure is supposed to stand still.",
   "evidence": ev_table("Hall of Villains – sensors", ["Time", "Sensor", "Note"], [
       ("22:02", "Door", "Mr Fontaine enters"),
       ("22:09", "Plinth 7", "Movement – figure 'Lady Macbeth'"),
       ("22:14", "Fire exit", "Opened from inside, closed"),
     ], mono_cols=(0,))},
  {"name": "Rosie Dunn", "role": "Wax artist", "label": "ROSIE'S NOTE",
   "quote": "The Lady Macbeth figure was moved to the store room that afternoon for repairs. Margot told me to leave the costume on the plinth stand.",
   "evidence": ev_note("ROSIE'S WORKSHOP NOTE", [
       "15:00 – Lady Macbeth figure to store",
       "for repair. Margot said: 'Leave the",
       "dress and wig on the stand.' Odd –",
       "we never do that."],
     "– Rosie")},
  {"name": "Mr Ken Lowe", "role": "Guest", "label": "GUEST PHOTO",
   "quote": "I took a photo of Lady Macbeth at quarter to ten. I swear her eyes blinked.",
   "evidence": ev_photos("Ken's phone", [
       ("IMG_9001", "21:45", "Lady Macbeth on plinth 7 – in the green dress and red wig. Visible under the hem: modern black trainers with a white stripe."),
     ])},
  {"name": "Jo Ellis", "role": "Car park", "label": "CAR PARK LOG",
   "quote": "Mrs Fontaine's car didn't leave at ten. It left at twenty past – from the back gate by the fire exit.",
   "evidence": ev_table("Car park barrier", ["Time", "Car", "Gate"], [
       ("22:01", "Last guest cars", "Front"),
       ("22:18", "M. Fontaine", "Back gate"),
     ], mono_cols=(0,))},
 ],
 "solution": {"killer": "Margot Fontaine",
   "motive": "Felix was divorcing Margot and taking the waxworks from her (clue 2).",
   "proof": ["Felix was killed after the doors locked at 22:00, so the killer was hiding inside (clue 1).",
             "Margot had the Lady Macbeth figure removed and its costume left on the stand (clue 4). At 21:45 a guest photographed 'Lady Macbeth' wearing modern trainers (clue 5), and at 22:09 plinth 7 moved (clue 3).",
             "Margot says she left at ten, but her car left by the back gate at 22:18, right after the fire exit opened at 22:14 (clues 3, 6)."],
   "cleared": ["<b>Tom</b> watched the sensors, <b>Rosie</b> only moved the figure as asked, and <b>Ken</b> and <b>Jo</b> only report what they saw."]},
}

# ---------------------------------------------------------------- TOY FACTORY
toyf = {
 "slug": "death-at-the-toy-factory", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 236", "title_html": "DEATH AT THE<br>TOY FACTORY", "title_plain": "Death at the Toy Factory",
 "teaser": "The toy factory owner is found dead on the night of the big Christmas order. The conveyor belt counter and a teddy bear's stuffing reveal who stopped the line.",
 "intro": "At <b>Jolly Jack Toys</b>, owner Jack Holloway was found dead under the teddy bear conveyor belt on the night shift before the big Christmas delivery. He had been struck with a spanner. " + STD,
 "clues": [
  {"name": "DI Sam Rowe", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Holloway was killed beside conveyor 3 between 23:00 and 23:30. Teddy stuffing was caught in his hand – pink stuffing.",
   "evidence": ev_rows("Police report – Jolly Jack Toys", [
       ("Found", "00:10, under conveyor 3"),
       ("Time of death", "23:00–23:30"),
       ("Weapon", "Spanner from line 3 toolbox"),
       ("In his hand", "Pink teddy stuffing"),
     ])},
  {"name": "Nick Dyer", "role": "Line 3 supervisor", "label": "NICK'S STATEMENT",
   "quote": "I was running line 2 all night – the blue teddies. I never went to line 3.",
   "evidence": ev_rows("Jack's email to HR", [
       ("Subject", "Nick Dyer"),
       ("Text", "“Nick has been selling our toy designs to a rival company. Dismiss him tomorrow.”"),
     ])},
  {"name": "Penny Moss", "role": "Line 2 worker", "label": "LINE 2 COUNTER",
   "quote": "Line 2 counts every teddy that comes off the belt. Between eleven and half past, it stopped completely – the supervisor wasn't there to restart it.",
   "evidence": ev_table("Line 2 counter – blue teddies", ["Time", "Teddies made"], [
       ("22:30–23:00", "180"),
       ("23:00–23:30", "0 – line stopped, supervisor absent"),
       ("23:30–00:00", "175"),
     ], mono_cols=(0,))},
  {"name": "Ray Collins", "role": "Line 3 worker", "label": "RAY'S STATEMENT",
   "quote": "I was on my break in the canteen from eleven till half past. Line 3 was empty – only the boss was checking it.",
   "evidence": ev_rows("Canteen till", [
       ("23:02", "Tea and pie – R. Collins"),
       ("23:28", "Second tea – R. Collins"),
     ])},
  {"name": "Gail Fox", "role": "Quality checker", "label": "STUFFING LIST",
   "quote": "Each line uses a different colour stuffing so we can trace faults. Pink is only used on line 3.",
   "evidence": ev_table("Stuffing colours", ["Line", "Teddies", "Stuffing"], [
       ("Line 1", "Brown", "White"),
       ("Line 2", "Blue", "Grey"),
       ("Line 3", "Pink", "Pink"),
     ])},
  {"name": "Lou Ames", "role": "Night security", "label": "CAMERA NOTE",
   "quote": "The camera on line 3 was switched off at 22:58. But the corridor camera caught someone walking from line 2 to line 3.",
   "evidence": ev_photos("Corridor camera", [
       ("CAM4_2301", "23:01", "Man in a blue supervisor's tabard walking from line 2 to line 3, carrying a spanner. Grey stuffing on his sleeve."),
       ("CAM4_2326", "23:26", "Same man walking back to line 2, pink fluff on his tabard."),
     ])},
 ],
 "solution": {"killer": "Nick Dyer",
   "motive": "Jack had found out Nick was selling toy designs and was firing him (clue 2).",
   "proof": ["Jack was killed beside line 3 between 23:00 and 23:30, with pink stuffing in his hand (clue 1). Pink stuffing is only used on line 3 (clue 5).",
             "Nick says he ran line 2 all night, but line 2 stopped from 23:00 to 23:30 because the supervisor was absent (clue 3).",
             "The corridor camera shows a man in a blue supervisor's tabard walking to line 3 with a spanner at 23:01 and back at 23:26 with pink fluff on him (clue 6)."],
   "cleared": ["<b>Ray</b> was in the canteen at 23:02 and 23:28 (clue 4).",
               "<b>Penny</b>, <b>Gail</b> and <b>Lou</b> only report what they found."]},
}

# ---------------------------------------------------------------- LAKE HOUSE
lake = {
 "slug": "murder-at-the-lake-house", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 237", "title_html": "MURDER AT THE<br>LAKE HOUSE", "title_plain": "Murder at the Lake House",
 "teaser": "A famous author is found dead in her boathouse study on a frozen lake. The thin ice, a skate mark and a wet scarf show who crossed the lake that night.",
 "intro": "At <b>Loch Ellen House</b>, crime author Dame Agnes Hale was found dead in her boathouse study across the frozen lake. She had been struck with a heavy typewriter. " + STD,
 "clues": [
  {"name": "DS Moira Kane", "role": "Police", "label": "POLICE REPORT",
   "quote": "The boathouse is across the lake. The road round takes twenty minutes by car – but the ice was thick enough to skate across in five.",
   "evidence": ev_rows("Police report – Loch Ellen", [
       ("Found", "23:30, boathouse study"),
       ("Time of death", "21:30–22:00"),
       ("Road", "Gate log – no car on the lake road all evening"),
       ("Ice", "Fresh skate marks from the house jetty to the boathouse and back"),
     ])},
  {"name": "Oliver Hale", "role": "Agnes's nephew", "label": "OLIVER'S STATEMENT",
   "quote": "I was in the library reading all evening. I can't even skate – ask anyone.",
   "evidence": ev_rows("Agnes's letter to her publisher", [
       ("Text", "“My nephew Oliver has been writing my last three books and I've been paying him to keep quiet. I'm going to tell the world – and stop paying.”"),
       ("Date", "That afternoon"),
     ])},
  {"name": "Mrs Jean Lyle", "role": "Housekeeper", "label": "HOUSE NOTE",
   "quote": "I took cocoa to the library at half past nine. Oliver wasn't there – his chair was empty and his book was face down. When I went back at ten he was there, red-faced and puffing.",
   "evidence": ev_note("HOUSEKEEPER'S NOTE", [
       "21:30 – library empty, cocoa left.",
       "22:00 – Oliver back, red face, wet",
       "scarf on the radiator, snow on his",
       "trousers."],
     "– Mrs Lyle")},
  {"name": "Hamish Lyle", "role": "Gardener", "label": "SKATE RACK",
   "quote": "The skates hang by the jetty door. In the morning one pair was wet and put back on the wrong hook.",
   "evidence": ev_table("Jetty skate rack", ["Hook", "Owner", "Morning"], [
       ("1", "Dame Agnes", "Dry"),
       ("2", "O. Hale (won skating cup 2019)", "Wet – on hook 3"),
       ("3", "Guests", "Dry"),
     ])},
  {"name": "Dr Ruth Kerr", "role": "Guest, Agnes's friend", "label": "RUTH'S STATEMENT",
   "quote": "I was on the phone to my husband in my room from nine till ten. He'll tell you – and the phone bill will too.",
   "evidence": ev_rows("Phone bill", [
       ("Call", "R. Kerr to home"),
       ("Time", "21:02–21:58"),
     ])},
  {"name": "Nina Hale", "role": "Oliver's sister", "label": "NINA'S NOTE",
   "quote": "From my window I saw someone skating fast across the lake in the moonlight – with a long striped scarf flying behind them.",
   "evidence": ev_photos("Nina's phone", [
       ("IMG_402", "21:41", "Moonlit frozen lake: a skater halfway to the boathouse, long red-and-white striped scarf. The same scarf Oliver wore at dinner (photo 20:00)."),
     ])},
 ],
 "solution": {"killer": "Oliver Hale",
   "motive": "Agnes was going to reveal that Oliver wrote her books and stop paying him (clue 2).",
   "proof": ["Agnes died between 21:30 and 22:00. No car used the road, but fresh skate marks crossed the lake (clue 1).",
             "Oliver says he was in the library and can't skate, but his chair was empty at 21:30 and he came back at 22:00 out of breath with a wet scarf (clue 3) – and he won a skating cup in 2019 (clue 4).",
             "His skates were wet in the morning (clue 4), and Nina photographed a skater in his striped scarf crossing the lake at 21:41 (clue 6)."],
   "cleared": ["<b>Ruth</b> was on the phone from 21:02 to 21:58 (clue 5).",
               "<b>Mrs Lyle</b>, <b>Hamish</b> and <b>Nina</b> only report what they saw."]},
}

# ---------------------------------------------------------------- DAM
dam = {
 "slug": "death-at-the-dam", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 238", "title_html": "DEATH AT<br>THE DAM", "title_plain": "Death at the Dam",
 "teaser": "An engineer is found dead in the control tunnel of a mountain dam. The tunnel door log, a flood-gate test and a muddy boot catch the killer.",
 "intro": "At the <b>Carrick Valley Dam</b>, engineer Dr Mark Ellery was found dead deep in the inspection tunnel, struck with a heavy torch. He had found cracks in the dam wall. " + STD,
 "clues": [
  {"name": "DI Ann Price", "role": "Police", "label": "POLICE REPORT",
   "quote": "Dr Ellery died in the inspection tunnel between 14:00 and 14:30. The only way in is through the steel door at the top, which logs every key card.",
   "evidence": ev_rows("Police report – Carrick Dam", [
       ("Found", "16:00, inspection tunnel"),
       ("Time of death", "14:00–14:30"),
       ("Tunnel door", "Key card log"),
       ("Floor", "Wet clay – boot prints, size 11"),
     ])},
  {"name": "Rob Kinnear", "role": "Dam manager", "label": "ROB'S STATEMENT",
   "quote": "I was in the control room running the flood-gate test from two till three. You can't leave the control panel during a test.",
   "evidence": ev_rows("Dr Ellery's report (draft)", [
       ("Finding", "Cracks in the wall – hidden by the manager for two years"),
       ("Action", "“Report R. Kinnear and close the dam.”"),
     ])},
  {"name": "Liz Moffat", "role": "Control room operator", "label": "TEST LOG",
   "quote": "The flood-gate test runs on a timer once it's started. Rob started it at two and said 'watch it for me' – then left.",
   "evidence": ev_table("Flood-gate test – control room", ["Time", "Event", "At panel"], [
       ("14:00", "Test started", "R. Kinnear"),
       ("14:05", "Gates opening – automatic", "L. Moffat"),
       ("14:40", "Gates closing – automatic", "L. Moffat, R. Kinnear"),
     ], mono_cols=(0,))},
  {"name": "Tam Reid", "role": "Security", "label": "DOOR LOG",
   "quote": "The tunnel door logs every card in and out.",
   "evidence": ev_table("Inspection tunnel door", ["Time", "Card", "In/Out"], [
       ("13:40", "M. Ellery", "In"),
       ("14:08", "R. Kinnear", "In"),
       ("14:31", "R. Kinnear", "Out"),
     ], mono_cols=(0,))},
  {"name": "Gill Stewart", "role": "Visiting inspector", "label": "GILL'S STATEMENT",
   "quote": "I arrived at the dam at half past two and waited in the visitors' centre for Dr Ellery. He never came.",
   "evidence": ev_rows("Visitor centre sign-in", [
       ("G. Stewart", "In 14:32"),
     ])},
  {"name": "Davey Shaw", "role": "Maintenance worker", "label": "BOOT FIND",
   "quote": "When I went to the control room at quarter to three, I saw muddy boots by the door – with wet clay on them. Size 11.",
   "evidence": ev_photos("Davey's phone", [
       ("IMG_77", "14:45", "Pair of work boots, size 11, caked in wet grey clay, outside the control room door. Name written inside: 'R.K.'"),
     ])},
 ],
 "solution": {"killer": "Rob Kinnear",
   "motive": "Dr Ellery was going to report Rob for hiding cracks in the dam for two years (clue 2).",
   "proof": ["Dr Ellery died in the tunnel between 14:00 and 14:30; there were size-11 clay boot prints (clue 1).",
             "Rob says he couldn't leave the control panel, but the test ran on a timer and he left Liz to watch it (clue 3). His card opened the tunnel door at 14:08 and left at 14:31 (clue 4).",
             "His size-11 boots, marked 'R.K.', were covered in wet clay at 14:45 (clue 6)."],
   "cleared": ["<b>Liz</b> stayed at the panel (clue 3), and <b>Gill</b> arrived at 14:32 (clue 5).",
               "<b>Tam</b> and <b>Davey</b> only report what they saw."]},
}

# ---------------------------------------------------------------- CHOCOLATIER
choc = {
 "slug": "murder-at-the-chocolatier", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 239", "title_html": "MURDER AT THE<br>CHOCOLATIER", "title_plain": "Murder at the Chocolatier",
 "teaser": "A master chocolatier is poisoned by one of his own Christmas truffles. Only one was poisoned – and only his inner team knew which he'd taste first.",
 "intro": "At <b>Maison Leclerc</b>, master chocolatier Henri Leclerc died after tasting a truffle from the new Christmas collection. One truffle on the tasting tray had been injected with poison. " + STD,
 "clues": [
  {"name": "Inspector Claire Dubois", "role": "Police", "label": "POLICE REPORT",
   "quote": "Only the truffle in the top-left corner of the tray was poisoned. Henri always tasted the top-left first. Whoever did it knew his habit.",
   "evidence": ev_rows("Police report – Maison Leclerc", [
       ("Died", "17:20"),
       ("Poisoned", "Top-left truffle only – injected through the base"),
       ("Tray", "Prepared 16:00–16:30 in the cold room"),
       ("Habit", "Henri always tasted top-left first – known to his inner team"),
       ("Catalogue photo", "16:18 – tray perfect, no needle hole in any truffle"),
     ])},
  {"name": "Sophie Leclerc", "role": "Henri's daughter, pastry chef", "label": "SOPHIE'S STATEMENT",
   "quote": "I was decorating the window display out front from four until five. I never went into the cold room.",
   "evidence": ev_rows("Henri's notes", [
       ("Plan", "Hand the business to his head chocolatier, Marc – not to Sophie"),
       ("Telling the family", "That evening"),
     ])},
  {"name": "Marc Duval", "role": "Head chocolatier", "label": "COLD ROOM LOG",
   "quote": "The cold room door logs every time it opens. I made the truffles but left the tray at 16:15 to cool.",
   "evidence": ev_table("Cold room door", ["Time", "Who"], [
       ("16:00", "M. Duval – in"),
       ("16:15", "M. Duval – out"),
       ("16:22", "S. Leclerc – in"),
       ("16:27", "S. Leclerc – out"),
     ], mono_cols=(0,))},
  {"name": "Amélie Roux", "role": "Shop assistant", "label": "WINDOW NOTE",
   "quote": "Sophie started the window display, but about twenty past four she went to the back. The display was half done for a while.",
   "evidence": ev_note("AMÉLIE'S NOTE", [
       "16:20 – Sophie to the back,",
       "'need more ribbon'. 16:30 – back,",
       "no ribbon, wiping her hands on her",
       "apron. Smelled of almonds."],
     "– Amélie")},
  {"name": "Dr Paul Martin", "role": "Pharmacist next door", "label": "PHARMACY SALE",
   "quote": "Sophie bought a small syringe from me last week – she said it was for filling éclairs.",
   "evidence": ev_rows("Pharmacy sales", [
       ("Item", "Small syringe with fine needle"),
       ("Customer", "S. Leclerc"),
       ("Date", "Last Thursday"),
     ])},
  {"name": "Luc Petit", "role": "Delivery driver", "label": "LUC'S STATEMENT",
   "quote": "I collected the Christmas boxes at four and was driving all afternoon. I never saw the tasting tray.",
   "evidence": ev_rows("Van tracker", [
       ("16:05", "Left Maison Leclerc"),
       ("16:05–18:00", "Deliveries across the city"),
     ])},
 ],
 "solution": {"killer": "Sophie Leclerc",
   "motive": "Henri was handing the business to Marc instead of Sophie (clue 2).",
   "proof": ["Only the top-left truffle was poisoned – the one Henri always tasted first, which only his inner team knew (clue 1).",
             "Sophie says she never went into the cold room, but the door log shows her inside from 16:22 to 16:27, after Marc left (clue 3), and Amélie saw her leave the window display at 16:20 (clue 4).",
             "Sophie bought a fine-needle syringe the week before (clue 5)."],
   "cleared": ["<b>Marc</b> left the cold room at 16:15, and the tray was still untouched at 16:18 (clues 1, 3). <b>Luc</b> left at 16:05 (clue 6).",
               "<b>Amélie</b> and <b>Dr Martin</b> only report what they saw."]},
}

MYSTERIES = [rig, wax, toyf, lake, dam, choc]
