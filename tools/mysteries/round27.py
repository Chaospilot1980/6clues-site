from lib import *  # evidence helpers

# Round 27 (18 Nov): 1 Rookie, 1 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- GUINEA PIG (L1)
guinea = {
 "slug": "the-missing-guinea-pig", "level": 1, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 170", "title_html": "THE MISSING<br>GUINEA PIG", "title_plain": "The Missing Guinea Pig",
 "teaser": "The class guinea pig vanishes from the school over the weekend. Carrot crumbs, a pet carrier and a sign-in sheet help find who took Biscuit home.",
 "intro": "At <b>Willowbank School</b>, Biscuit the class guinea pig was missing from her cage on Monday morning. Luckily she was safe and well – but who took her, and why didn't they say? " + STD,
 "clues": [
  {"name": "Miss Hannah Price", "role": "Class teacher", "label": "TEACHER'S REPORT",
   "quote": "Biscuit was in her cage when I locked the classroom at four on Friday. On Monday at eight, the cage was empty and there were carrot crumbs on the floor.",
   "evidence": ev_rows("Teacher's report", [
       ("Locked", "Friday 16:00"),
       ("Found empty", "Monday 08:00"),
       ("Clue", "Carrot crumbs leading to the classroom door"),
       ("Weekend", "School open on Saturday morning for the Pet Club only"),
     ])},
  {"name": "Mr Gary Ward", "role": "Pet Club leader", "label": "GARY'S STATEMENT",
   "quote": "Pet Club only cleans the rabbit hutches outside on Saturdays. I never went into Miss Price's classroom.",
   "evidence": ev_rows("Gary Ward – note to the head", [
       ("Last month", "“Biscuit should go home with someone at weekends – she gets lonely.”"),
       ("Head's reply", "“No – she stays at school.”"),
     ])},
  {"name": "Mrs Pat Dean", "role": "School office", "label": "SATURDAY SIGN-IN",
   "quote": "Everyone who comes in on Saturday signs the book and takes a key if they need one.",
   "evidence": ev_table("Saturday sign-in", ["Time", "Name", "Key taken"], [
       ("09:00", "G. Ward (Pet Club)", "Classroom 4 – 'to fetch the pet food'"),
       ("09:10", "Mrs P. Dean", "Office"),
       ("11:00", "G. Ward", "Key back"),
     ], mono_cols=(0,))},
  {"name": "Mr Sam Holt", "role": "Caretaker", "label": "CARETAKER'S NOTE",
   "quote": "On Saturday at about half ten I saw someone walk to the car park carrying a little blue pet carrier with straw sticking out.",
   "evidence": ev_note("CARETAKER'S NOTEBOOK", [
       "Sat 10:30 – man in a green Pet Club",
       "fleece carrying small blue pet carrier",
       "to the car park. Put it on the",
       "passenger seat of a silver car."],
     "– Sam")},
  {"name": "Mrs Rita Shah", "role": "Head teacher", "label": "CAR PARK LIST",
   "quote": "Only three people drove in on Saturday. We note every car.",
   "evidence": ev_table("Saturday car park", ["Car", "Driver"], [
       ("Silver hatchback", "G. Ward"),
       ("Red estate", "P. Dean"),
       ("White van", "S. Holt"),
     ])},
  {"name": "Mr Leo Fox", "role": "Pet shop owner", "label": "PET SHOP RECEIPT",
   "quote": "A man bought a little blue pet carrier and a bag of guinea-pig food on Friday evening. He said it was for 'a weekend guest'.",
   "evidence": ev_table("Fox's Pets – Friday", ["Time", "Item", "Customer"], [
       ("17:40", "Small pet carrier (blue)", "G. Ward (loyalty card)"),
       ("17:40", "Guinea pig food, 1 kg", "G. Ward (loyalty card)"),
     ], mono_cols=(0,))},
 ],
 "solution": {"killer": "Mr Gary Ward",
   "motive": "Gary thought Biscuit got lonely at weekends and wanted to take her home, but the head said no (clue 2).",
   "proof": ["Gary says he never went into Miss Price's classroom, but he signed out the classroom 4 key at 09:00 on Saturday (clue 3).",
             "On Friday evening he bought a blue pet carrier and guinea-pig food 'for a weekend guest' (clue 6).",
             "At 10:30 the caretaker saw a man in a Pet Club fleece put a blue pet carrier in a silver car (clue 4) – Gary's car (clue 5)."],
   "cleared": ["<b>Mrs Dean</b> only took the office key and drives a red estate; <b>Mr Holt</b> drives a white van (clues 3, 5).",
               "<b>Miss Price</b>, <b>Mrs Shah</b> and <b>Mr Fox</b> only report what they know."]},
}

# ---------------------------------------------------------------- ALLOTMENT (L2)
allotment = {
 "slug": "the-allotment-tomato-thief", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 171", "title_html": "THE ALLOTMENT<br>TOMATO THIEF", "title_plain": "The Allotment Tomato Thief",
 "teaser": "Prize tomatoes vanish from an allotment the night before the village show – and win first prize the next day on someone else's table.",
 "intro": "At <b>Meadow Lane Allotments</b>, Bill Turner's rare 'Black Krim' tomatoes were picked in the night. The next day, a plate of 'Black Krim' won first prize at the village show – entered by someone else. " + STD,
 "clues": [
  {"name": "Bill Turner", "role": "Allotment holder", "label": "BILL'S REPORT",
   "quote": "I'm the only one on the site who grows Black Krim – I brought the seeds back from Ukraine. On Friday evening they were perfect. On Saturday morning the vine was bare.",
   "evidence": ev_rows("Allotment committee report", [
       ("Plot", "No. 14 – B. Turner"),
       ("Picked", "Friday night"),
       ("Variety", "'Black Krim' – no other plot grows it (seed register)"),
       ("Site gate", "Combination lock – code changed weekly, sent to plot holders"),
     ])},
  {"name": "Sheila Bright", "role": "Allotment holder, plot 9", "label": "SHOW RESULTS",
   "quote": "My tomatoes are my own! I grew them from seed in my greenhouse at home. I wasn't even at the allotment on Friday night.",
   "evidence": ev_table("Village show – tomato class", ["Place", "Entrant", "Variety"], [
       ("1st", "S. Bright", "Black Krim"),
       ("2nd", "B. Turner", "Gardener's Delight (his back-up plate)"),
       ("3rd", "K. Ahmed", "Moneymaker"),
     ])},
  {"name": "Kamal Ahmed", "role": "Allotment holder, plot 2", "label": "SEED REGISTER",
   "quote": "I keep the seed swap register. Everyone writes down what they're growing so we don't double up.",
   "evidence": ev_table("Seed register – this year", ["Plot", "Holder", "Tomatoes"], [
       ("2", "K. Ahmed", "Moneymaker"),
       ("9", "S. Bright", "Gardener's Delight, Alicante"),
       ("14", "B. Turner", "Black Krim, Gardener's Delight"),
     ])},
  {"name": "Doug Price", "role": "Site warden", "label": "GATE CAMERA",
   "quote": "There's a little wildlife camera on the gate post – it was meant to catch badgers.",
   "evidence": ev_photos("Gate wildlife camera", [
       ("WILD_88", "Fri 21:47", "A woman with a head torch and a wicker trug walks in through the gate."),
       ("WILD_89", "Fri 22:05", "The same woman walks out; the trug is full of dark tomatoes."),
     ])},
  {"name": "Rose Tate", "role": "Show judge", "label": "JUDGE'S NOTE",
   "quote": "The winning tomatoes were wonderful – but they still had allotment soil on them, a red clay. Odd, for tomatoes grown in a greenhouse.",
   "evidence": ev_rows("Judge's notes", [
       ("Winning plate", "S. Bright – Black Krim"),
       ("Soil on tomatoes", "Red clay, as on Meadow Lane plots"),
       ("Greenhouse tomatoes", "Usually grown in clean compost"),
     ])},
  {"name": "Pam Hughes", "role": "Shop owner", "label": "HEAD TORCH SALE",
   "quote": "On Friday afternoon a lady from the allotments bought a head torch – said she had 'some late gardening' to do.",
   "evidence": ev_table("Hughes Hardware – Friday", ["Time", "Item", "Customer"], [
       ("15:20", "Head torch + batteries", "S. Bright (account)"),
       ("16:05", "Bird feeder", "K. Ahmed (account)"),
     ], mono_cols=(0,))},
 ],
 "solution": {"killer": "Sheila Bright",
   "motive": "Sheila wanted the first prize at the village show (clue 2).",
   "proof": ["Only Bill grows Black Krim – Sheila's register lists only Gardener's Delight and Alicante (clues 1, 3). Yet Sheila won with Black Krim (clue 2).",
             "Sheila says she wasn't at the allotment on Friday night, but at 21:47 a woman with a head torch and a trug came in and left at 22:05 with dark tomatoes (clue 4). Sheila bought a head torch on Friday afternoon (clue 6).",
             "Her 'greenhouse' tomatoes had red allotment clay on them (clue 5)."],
   "cleared": ["<b>Kamal</b> grows Moneymaker and bought a bird feeder, not a head torch (clues 3, 6); the camera shows a woman.",
               "<b>Doug</b>, <b>Rose</b> and <b>Pam</b> only report what they know, and <b>Bill</b> is the victim."]},
}

# ---------------------------------------------------------------- HUNTING LODGE (L3)
lodge = {
 "slug": "death-at-the-hunting-lodge", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 172", "title_html": "DEATH AT THE<br>HUNTING LODGE", "title_plain": "Death at the Hunting Lodge",
 "teaser": "A businessman is shot in the woods during a deer stalk. Everyone carried a rifle – but the GPS trackers, a spent cartridge and the wind tell who fired.",
 "intro": "On the <b>Glenmore estate</b> in the Highlands, property developer Malcolm Shaw was shot dead in the birch woods during a guided deer stalk. It was made to look like an accident. " + STD,
 "clues": [
  {"name": "Insp. Alan Fraser", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Shaw was shot from about 80 metres, uphill, at 10:42 – a stalker heard the shot. The bullet came from a .308 rifle.",
   "evidence": ev_rows("Police report – Glenmore", [
       ("Found", "10:55, Birch Hollow"),
       ("Shot", "10:42, from the ridge above Birch Hollow, about 80 m"),
       ("Bullet", ".308 calibre"),
       ("Cartridge case", "Found on the ridge by the old cairn"),
     ])},
  {"name": "Fiona Shaw", "role": "Malcolm's wife", "label": "FIONA'S STATEMENT",
   "quote": "I was with Ross, the head stalker, the whole morning in the east glen, watching a herd of hinds. I didn't even fire my rifle.",
   "evidence": ev_rows("Malcolm Shaw – will and insurance", [
       ("Life insurance", "£3m, paid to F. Shaw"),
       ("Divorce papers", "Drawn up by Malcolm, to be signed Monday – Fiona would get nothing"),
     ])},
  {"name": "Ross MacLeod", "role": "Head stalker", "label": "GPS TRACKERS",
   "quote": "Every guest wears a GPS tracker for safety on the hill. Fiona was with me until about twenty past ten, then she said she'd take a shortcut back to the lodge on her own.",
   "evidence": ev_table("Guest GPS trackers – 10:30 to 10:45", ["Guest", "Location"], [
       ("M. Shaw", "Birch Hollow"),
       ("F. Shaw", "Ridge above Birch Hollow, by the old cairn"),
       ("D. Lyle", "East glen, with R. MacLeod"),
       ("P. Grant", "Lodge – kitchen"),
     ])},
  {"name": "Duncan Lyle", "role": "Malcolm's business partner", "label": "RIFLE LIST",
   "quote": "Malcolm and I were about to fall out over money, I won't hide that. But I spent the morning in the east glen with Ross. I shoot a .243 – a smaller calibre entirely.",
   "evidence": ev_table("Estate rifle register", ["Guest", "Rifle", "Rounds issued", "Rounds returned"], [
       ("M. Shaw", ".270", "5", "–"),
       ("F. Shaw", ".308", "5", "4"),
       ("D. Lyle", ".243", "5", "5"),
     ])},
  {"name": "Peggy Grant", "role": "Lodge cook", "label": "KITCHEN NOTE",
   "quote": "I was in the kitchen making the lunch all morning. At about quarter to eleven I heard one shot from the direction of Birch Hollow – then nothing.",
   "evidence": ev_rows("Kitchen timer and radio log", [
       ("10:30", "Venison pie into the oven"),
       ("10:42", "Single shot heard from the west, Birch Hollow way"),
       ("11:15", "Pie out"),
     ])},
  {"name": "Dr Iain Munro", "role": "Forensic scientist", "label": "CARTRIDGE TEST",
   "quote": "The cartridge case from the cairn was fired from a .308 rifle. It carries the firing-pin mark of one particular gun.",
   "evidence": ev_rows("Firearms lab", [
       ("Cartridge case", ".308, fired"),
       ("Firing-pin mark", "Matches estate rifle No. 6"),
       ("Rifle No. 6", "Issued to F. Shaw"),
     ])},
 ],
 "solution": {"killer": "Fiona Shaw",
   "motive": "Malcolm was about to divorce Fiona, leaving her nothing – but if he died she would collect £3m in life insurance (clue 2).",
   "proof": ["Malcolm was shot at 10:42 from the ridge above Birch Hollow with a .308 (clue 1).",
             "Fiona says she was with Ross all morning, but Ross says she left him at about 10:20 (clue 3), and her GPS tracker puts her on the ridge by the old cairn from 10:30 to 10:45 (clue 3).",
             "She was issued a .308 and returned only 4 of her 5 rounds (clue 4), and the cartridge from the cairn was fired from her rifle (clue 6)."],
   "cleared": ["<b>Duncan</b> was in the east glen with Ross, shoots a .243 and returned all five rounds (clues 3, 4).",
               "<b>Peggy</b> was in the kitchen (clues 3, 5); <b>Ross</b> was in the east glen with Duncan, and <b>Dr Munro</b> only tested the evidence."]},
}

# ---------------------------------------------------------------- QUARRY (L3)
quarry = {
 "slug": "death-at-the-quarry", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 173", "title_html": "DEATH AT<br>THE QUARRY", "title_plain": "Death at the Quarry",
 "teaser": "A quarry manager falls from the cliff edge on blasting day. The siren, the weighbridge tickets and a missing hard hat show it was no accident.",
 "intro": "At <b>Penhallow Stone Quarry</b>, manager Grace Tremayne was found at the foot of the north face on a blasting day. Everyone was supposed to be behind the safety line. " + STD,
 "clues": [
  {"name": "DS Owen Pascoe", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mrs Tremayne fell from the top of the north face – but she was hit on the head first. Her radio recorded her last words at 11:52.",
   "evidence": ev_rows("Police report – Penhallow Quarry", [
       ("Found", "12:20, foot of the north face"),
       ("Last radio call", "11:52 – “Who's that up here? Get behind the line!”"),
       ("Injury", "Blow to the head before the fall"),
       ("Missing", "Her hard hat – found later in a lorry cab"),
     ])},
  {"name": "Jago Polglase", "role": "Lorry driver", "label": "JAGO'S STATEMENT",
   "quote": "I was on the weighbridge from half eleven till twelve, loading and weighing my lorry. Ask Morwenna in the office.",
   "evidence": ev_rows("Grace's notebook – last page", [
       ("Note", "Weighbridge tickets for J. Polglase's lorry don't match deliveries"),
       ("Amount", "About £40,000 of stone sold privately over a year"),
       ("Plan", "“Tell the owners on Monday. Police too.”"),
     ])},
  {"name": "Morwenna Hicks", "role": "Weighbridge clerk", "label": "WEIGHBRIDGE TICKETS",
   "quote": "Jago's lorry came over the bridge twice that morning. In between, it was parked by the north face track while he 'checked his tyres'.",
   "evidence": ev_table("Weighbridge – Thursday", ["Time", "Lorry", "Weight"], [
       ("11:31", "J. Polglase – empty", "14.2 t"),
       ("11:40–12:05", "J. Polglase – parked at north track", "–"),
       ("12:06", "J. Polglase – loaded", "32.8 t"),
     ], mono_cols=(0,))},
  {"name": "Bryn Teague", "role": "Shot-firer", "label": "BLAST LOG",
   "quote": "I sound the siren, everyone gets behind the line, and I count them on the radio. Only one person didn't answer the roll call before the blast.",
   "evidence": ev_table("Blast log – Thursday", ["Time", "Event"], [
       ("11:45", "Siren – everyone behind the safety line"),
       ("11:48", "Radio roll call: G. Tremayne (top of north face, checking), M. Hicks, B. Teague, T. Rowe – J. Polglase: no answer"),
       ("12:00", "Blast"),
     ], mono_cols=(0,))},
  {"name": "Tamsin Rowe", "role": "Digger driver", "label": "DIGGER CAMERA",
   "quote": "My digger has a reversing camera that records. I was parked behind the line facing the north track.",
   "evidence": ev_photos("Digger reversing camera", [
       ("CAM-R", "11:49", "A man in an orange high-vis jacket and no hard hat climbs the north track towards the top of the face."),
       ("CAM-R", "11:56", "The same man hurries back down, carrying a white hard hat."),
     ])},
  {"name": "Kitto Pearce", "role": "Quarry owner", "label": "HARD HAT LIST",
   "quote": "Hard hats are colour-coded by job. Managers wear white. Drivers wear yellow.",
   "evidence": ev_table("Hard hat colours", ["Job", "Colour"], [
       ("Manager – G. Tremayne", "White"),
       ("Drivers – J. Polglase, T. Rowe", "Yellow"),
       ("Shot-firer – B. Teague", "Blue"),
       ("Office – M. Hicks", "Red"),
     ])},
 ],
 "solution": {"killer": "Jago Polglase",
   "motive": "Grace had found that Jago sold about £40,000 of the quarry's stone privately and was going to tell the owners and the police (clue 2).",
   "proof": ["Grace was struck on the north face at about 11:52 and her white hard hat was later found in a lorry cab (clues 1, 6).",
             "Jago says he was on the weighbridge from 11:30 to 12:00, but his lorry was parked at the north track from 11:40 to 12:05 (clue 3), and he alone missed the radio roll call at 11:48 (clue 4).",
             "At 11:49 a man in high-vis climbed the north track and at 11:56 came back down carrying a white hard hat – the manager's colour (clues 5, 6)."],
   "cleared": ["<b>Morwenna</b> and <b>Bryn</b> answered the roll call behind the line (clue 4).",
               "<b>Tamsin</b> answered the roll call from her digger behind the line (clues 4, 5), and <b>Kitto</b> was not on site – he isn't on the roll call (clue 4)."]},
}

MYSTERIES = [guinea, allotment, lodge, quarry]
