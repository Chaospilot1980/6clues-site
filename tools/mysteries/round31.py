from lib import *  # evidence helpers

# Round 31 (18 Nov): 2 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- SNOW GLOBE (L2)
globe = {
 "slug": "the-snow-globe-swap", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 186", "title_html": "THE SNOW<br>GLOBE SWAP", "title_plain": "The Snow Globe Swap",
 "teaser": "A rare Victorian snow globe in a town museum has been swapped for a cheap copy. A visitor book, a gift shop receipt and a ticket stamp unmask the thief.",
 "intro": "At the <b>Fairhaven Town Museum</b>, curator Agnes Ward discovered that the star of the Christmas display – a Victorian snow globe worth £12,000 – had been replaced with a gift-shop copy. " + STD,
 "clues": [
  {"name": "Agnes Ward", "role": "Curator", "label": "CURATOR'S REPORT",
   "quote": "The copy is from our own gift shop – there's a 'Made in 2026' sticker on the base. The real globe was checked on Monday evening. On Thursday morning I found the fake.",
   "evidence": ev_rows("Curator's report", [
       ("Last checked", "Monday 17:00 – real globe"),
       ("Fake found", "Thursday 09:30"),
       ("The copy", "Gift-shop snow globe, £14.99, sticker on base"),
       ("Display case", "Opened with a small key – no damage"),
     ])},
  {"name": "Rob Kelly", "role": "Volunteer guide", "label": "ROB'S STATEMENT",
   "quote": "I haven't been in since the weekend. I've got nothing to do with the Christmas display – Agnes does all of that.",
   "evidence": ev_table("Display case keys", ["Key", "Kept by"], [
       ("Key 1", "Agnes Ward"),
       ("Key 2", "Volunteer key box – signed out in the book"),
     ])},
  {"name": "Mina Lowe", "role": "Gift shop manager", "label": "SHOP RECEIPT",
   "quote": "We only sold one of those copy globes this week. The buyer paid by card.",
   "evidence": ev_rows("Gift shop receipt", [
       ("Item", "Victorian-style snow globe (copy)"),
       ("Price", "£14.99"),
       ("Date", "Tuesday 11:42"),
       ("Card", "R. KELLY"),
     ])},
  {"name": "Joan Price", "role": "Front desk", "label": "KEY BOOK",
   "quote": "Volunteers sign the key box book when they borrow a key. Someone took key 2 on Wednesday.",
   "evidence": ev_table("Key box book", ["Day", "Key", "Out", "In", "Signed"], [
       ("Tuesday", "Key 2", "–", "–", "–"),
       ("Wednesday", "Key 2", "16:10", "16:35", "R.K."),
     ])},
  {"name": "Ollie Shaw", "role": "Visitor", "label": "VISITOR PHOTO",
   "quote": "I visited on Wednesday afternoon. I took a photo of the snow globe – and a man in a guide's lanyard was leaning into the open case.",
   "evidence": ev_photos("Ollie's phone", [
       ("IMG_5512", "Wed 16:20", "The Christmas display with its case open. A man in a red 'GUIDE' lanyard holds a snow globe; a gift-shop bag sits at his feet."),
     ])},
  {"name": "Dr Leon Abbott", "role": "Antiques dealer", "label": "DEALER'S EMAIL",
   "quote": "A man emailed me on Thursday offering a 'Victorian snow globe, no questions asked'. I said no and told the police.",
   "evidence": ev_note("EMAIL TO L. ABBOTT", [
       "From: robk.collector@mail.com",
       "Thu 08:02 – Victorian snow globe,",
       "perfect, £6,000 cash. No paperwork,",
       "no questions."],
     "– forwarded to police")},
 ],
 "solution": {"killer": "Rob Kelly",
   "motive": "Rob tried to sell the real globe for £6,000 cash (clue 6).",
   "proof": ["The real globe was swapped between Monday and Thursday for a £14.99 gift-shop copy, using a key (clue 1).",
             "Rob says he hasn't been in since the weekend, but he bought the only copy on Tuesday (clue 3) and signed out key 2 on Wednesday from 16:10 to 16:35 (clues 2, 4).",
             "At 16:20 Ollie photographed a guide with the case open and a gift-shop bag at his feet (clue 5), and the next morning 'robk' offered the globe to a dealer (clue 6)."],
   "cleared": ["<b>Agnes</b> found the fake and reported it, and <b>Mina</b> and <b>Joan</b> only keep the records (clues 1, 3, 4).",
               "<b>Ollie</b> was a visitor, and <b>Leon</b> refused the deal and went to the police (clues 5, 6)."]},
}

# ---------------------------------------------------------------- CHALET (L2)
chalet = {
 "slug": "the-chalet-safe-robbery", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 187", "title_html": "THE CHALET<br>SAFE ROBBERY", "title_plain": "The Chalet Safe Robbery",
 "teaser": "A luxury ski chalet's safe is emptied while the guests are on the slopes. A lift pass, a safe code log and wet ski boots reveal the thief.",
 "intro": "At <b>Chalet Edelweiss</b> in the Alps, the safe in the main bedroom was emptied of €8,000 and a diamond watch while the guests were out skiing. " + STD,
 "clues": [
  {"name": "Mr James Rhodes", "role": "Guest, owner of the watch", "label": "JAMES'S REPORT",
   "quote": "We all went up the mountain at nine. When we came back at four, the safe was open and empty.",
   "evidence": ev_rows("Safe log", [
       ("Opened", "11:48 with the correct code"),
       ("Code", "Set by the chalet host – only staff know the master code"),
       ("Missing", "€8,000 cash, diamond watch"),
     ])},
  {"name": "Lena Brandt", "role": "Chalet host", "label": "LENA'S STATEMENT",
   "quote": "I was in the village doing the food shopping from ten until one. I couldn't have been here at midday.",
   "evidence": ev_table("Chalet staff – master code", ["Staff", "Knows code?"], [
       ("L. Brandt (host)", "Yes"),
       ("T. Weiss (chef)", "Yes"),
       ("M. Novak (cleaner)", "No"),
     ])},
  {"name": "Tomas Weiss", "role": "Chalet chef", "label": "LIFT PASS",
   "quote": "It was my day off. I was skiing all day – my lift pass shows it.",
   "evidence": ev_table("Lift pass scans – T. Weiss", ["Time", "Lift"], [
       ("09:15", "Gondola, valley"),
       ("10:40", "Chair 4"),
       ("12:05", "Chair 6"),
       ("13:30", "Gondola, top"),
     ], mono_cols=(0,), note="Chair 6 is 25 minutes from the chalet.")},
  {"name": "Marta Novak", "role": "Cleaner", "label": "MARTA'S NOTE",
   "quote": "I cleaned the upstairs from eleven to twelve. I heard someone come in the back door just before quarter to twelve, then leave ten minutes later. I thought it was Lena back early.",
   "evidence": ev_note("MARTA'S NOTE", [
       "About 11:43 – back door opens.",
       "Boots on the stairs, someone goes",
       "into the main bedroom. 11:53 –",
       "back door again. Car leaves."],
     "– Marta")},
  {"name": "Herr Paul Gruber", "role": "Village shopkeeper", "label": "SHOP RECEIPTS",
   "quote": "Lena shops with me every day. On that day she came in twice – early, and then again after lunch.",
   "evidence": ev_table("Gruber's shop – chalet account", ["Time", "Items"], [
       ("10:12", "Bread, milk, eggs"),
       ("12:40", "Cheese, wine"),
     ], note="The chalet is 15 minutes by car from the village.")},
  {"name": "Sophie Rhodes", "role": "James's daughter", "label": "SOPHIE'S STATEMENT",
   "quote": "I skied with Dad and the group all day. We had lunch together in the mountain hut from twelve to one.",
   "evidence": ev_rows("Mountain hut receipt", [
       ("Table", "Rhodes party – 5 people"),
       ("Time", "12:02–13:05"),
     ])},
 ],
 "solution": {"killer": "Lena Brandt",
   "motive": "Lena took €8,000 and a diamond watch from the guests' safe (clue 1).",
   "proof": ["The safe was opened at 11:48 with the master code, which only Lena and Tomas know (clues 1, 2).",
             "Lena says she was in the village from 10:00 to 13:00. But she shopped at 10:12 and then not again until 12:40 – and the chalet is only 15 minutes away by car (clue 5).",
             "Marta heard someone come in the back door at 11:43, go into the main bedroom and drive off at 11:53 (clue 4)."],
   "cleared": ["<b>Tomas</b> was scanned at Chair 6 at 12:05, 25 minutes from the chalet – he could not have left the chalet at 11:53 by car and be there (clue 3).",
               "<b>Marta</b> doesn't know the code (clue 2), and <b>James</b> and <b>Sophie</b> were on the mountain (clue 6)."]},
}

# ---------------------------------------------------------------- SLEEPER TRAIN (L3)
sleeper = {
 "slug": "death-on-the-sleeper-train", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 188", "title_html": "DEATH ON THE<br>SLEEPER TRAIN", "title_plain": "Death on the Sleeper Train",
 "teaser": "A publisher is found dead in his cabin on the night sleeper to the Highlands. Station stops, a tea order and a door-lock log catch the killer.",
 "intro": "On the <b>Highland Night Sleeper</b>, publisher Edmund Crane was found dead in cabin 12 when the attendant brought his morning tea. He had been smothered with a pillow. " + STD,
 "clues": [
  {"name": "DS Callum Reid", "role": "Transport police", "label": "POLICE REPORT",
   "quote": "Mr Crane died while the train was stopped at Crewe – his cabin's door log shows it was opened then, and he was alive at the stop before.",
   "evidence": ev_rows("Police report – cabin 12", [
       ("Found", "06:30, by the attendant"),
       ("Door log", "Opened with a staff master card at 01:42"),
       ("Alive", "Ordered tea by phone at 00:55"),
       ("Pillow", "A long red hair caught in the pillowcase"),
     ])},
  {"name": "Fiona Marsh", "role": "Author, cabin 14", "label": "FIONA'S STATEMENT",
   "quote": "I was asleep from midnight. I take a sleeping pill on trains – I didn't wake until Inverness.",
   "evidence": ev_rows("Letter from E. Crane to F. Marsh", [
       ("Subject", "Your contract"),
       ("Text", "“I am cancelling your book deal. You copied whole chapters from another writer.”"),
       ("Date", "Delivered the day before the trip"),
     ])},
  {"name": "Gordon Fyfe", "role": "Train attendant", "label": "MASTER CARD LOG",
   "quote": "My master card opens every cabin. I lent it to a passenger who said she was locked out of her cabin – about half past one. She gave it back ten minutes later.",
   "evidence": ev_table("Master card 2 – use log", ["Time", "Door"], [
       ("01:31", "Cabin 14"),
       ("01:42", "Cabin 12"),
       ("01:49", "Returned to attendant"),
     ], mono_cols=(0,))},
  {"name": "Kirsty Allan", "role": "Passenger, cabin 10", "label": "KIRSTY'S NOTE",
   "quote": "The train stopped at Crewe and I couldn't sleep. Through my door I saw a woman with long red hair in a dressing gown go into cabin 12.",
   "evidence": ev_note("KIRSTY'S NOTE", [
       "Crewe stop, about 01:40 –",
       "woman, long red hair, green dressing",
       "gown, went into cabin 12. Came out",
       "a few minutes later, very quickly."],
     "– Kirsty")},
  {"name": "Dr Ian Moss", "role": "Passenger, cabin 11", "label": "PASSENGER LIST",
   "quote": "I'm a doctor – I was asked to look at the body. I also saw the passenger list on the attendant's clipboard.",
   "evidence": ev_table("Coach B passengers", ["Cabin", "Passenger", "Hair"], [
       ("10", "K. Allan", "Short, grey"),
       ("11", "I. Moss", "Bald"),
       ("12", "E. Crane", "–"),
       ("14", "F. Marsh", "Long, red"),
       ("15", "R. Crane", "Short, blonde"),
     ])},
  {"name": "Rachel Crane", "role": "Edmund's wife, cabin 15", "label": "RACHEL'S STATEMENT",
   "quote": "Edmund and I had separate cabins because he snored. I was in the dining car playing cards with the guard until two.",
   "evidence": ev_rows("Guard's note", [
       ("Dining car", "Cards with Mrs R. Crane, 00:30–02:05"),
       ("Guard", "Never left the dining car"),
     ])},
 ],
 "solution": {"killer": "Fiona Marsh",
   "motive": "Edmund was cancelling Fiona's book deal for copying (clue 2).",
   "proof": ["Edmund died after 00:55; his door was opened with a master card at 01:42 (clue 1).",
             "Fiona says she was asleep from midnight, but the borrowed master card first opened her own cabin 14 at 01:31 and then cabin 12 (clue 3).",
             "Kirsty saw a woman with long red hair go into cabin 12 at about 01:40 (clue 4), a long red hair was in the pillow (clue 1), and Fiona is the only passenger with long red hair (clue 5)."],
   "cleared": ["<b>Rachel</b> played cards with the guard until 02:05 and has short blonde hair (clues 5, 6).",
               "<b>Kirsty</b> and <b>Dr Moss</b> have short and no hair (clue 5); <b>Gordon</b> lent the card and stayed at his post (clue 3)."]},
}

# ---------------------------------------------------------------- CABLE CAR (L3)
cable = {
 "slug": "murder-on-the-cable-car", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 189", "title_html": "MURDER ON THE<br>CABLE CAR", "title_plain": "Murder on the Cable Car",
 "teaser": "A ski resort owner is found dead alone in a cable car cabin at the summit. A middle-station log, a ski locker and a class register reveal the killer.",
 "intro": "At the <b>Alpenkrone ski resort</b>, owner Anton Weber was found dead in cabin 23 of the cable car when it arrived at the summit. He had been hit with a ski pole handle. " + STD,
 "clues": [
  {"name": "Inspector Eva Lang", "role": "Police", "label": "POLICE REPORT",
   "quote": "The cable car takes twelve minutes from bottom to top. Cabin 23 left the valley at 15:30 and reached the summit at 15:42 with only the body inside.",
   "evidence": ev_rows("Police report – Alpenkrone", [
       ("Cabin 23", "Left valley 15:30 · reached summit 15:42"),
       ("Found", "15:42, Anton Weber, dead"),
       ("Weapon", "Heavy ski pole with a broken basket – pole missing"),
       ("Middle station", "Cabins stop for 1 minute at 15:36"),
     ])},
  {"name": "Kurt Brenner", "role": "Ski school director", "label": "KURT'S STATEMENT",
   "quote": "I was teaching a class on the nursery slope at the bottom all afternoon. I never got on the cable car.",
   "evidence": ev_rows("Resort board minutes", [
       ("Anton's plan", "Close the Brenner Ski School and run lessons himself"),
       ("Kurt's reply", "“Over my dead body – or his.”"),
       ("Date", "One week before"),
     ])},
  {"name": "Nina Fuchs", "role": "Ski instructor", "label": "CLASS REGISTER",
   "quote": "Kurt's class that afternoon was handed over to me at quarter past three. He said he had 'a meeting'.",
   "evidence": ev_table("Nursery slope – class register", ["Time", "Instructor"], [
       ("14:00–15:15", "K. Brenner"),
       ("15:15–16:30", "N. Fuchs (cover)"),
     ], mono_cols=(0,))},
  {"name": "Felix Moser", "role": "Lift operator, middle station", "label": "MIDDLE STATION LOG",
   "quote": "At the middle station I saw a man in a red ski school jacket step out of cabin 23 holding one ski pole. He went straight down the black run.",
   "evidence": ev_table("Middle station – cabin log", ["Time", "Cabin", "Off"], [
       ("15:35", "22", "2 skiers"),
       ("15:36", "23", "1 man, red ski school jacket, one pole"),
       ("15:37", "24", "Empty"),
     ], mono_cols=(0,))},
  {"name": "Ursula Weber", "role": "Anton's sister", "label": "URSULA'S STATEMENT",
   "quote": "My brother and I fought about the will, yes. But I was in the spa at the summit hotel from three until five.",
   "evidence": ev_rows("Summit spa booking", [
       ("Guest", "U. Weber"),
       ("Treatment", "Massage, 15:00–16:00"),
       ("Therapist", "With her the whole hour"),
     ])},
  {"name": "Max Huber", "role": "Ski hire shop", "label": "LOCKER FIND",
   "quote": "That evening we found a single ski pole in the ski school staff locker – the basket broken off and blood on the grip.",
   "evidence": ev_photos("Ski hire shop photos", [
       ("IMG_7711", "18:20", "Staff locker 1 labelled 'K. BRENNER – DIRECTOR'. Inside: one ski pole with a broken basket and a dark stain on the grip."),
     ])},
 ],
 "solution": {"killer": "Kurt Brenner",
   "motive": "Anton was going to close Kurt's ski school (clue 2).",
   "proof": ["Anton was killed in cabin 23 between 15:30 and 15:42, and the cabin stopped at the middle station at 15:36 (clue 1).",
             "Kurt says he taught on the nursery slope all afternoon, but he handed his class to Nina at 15:15 for 'a meeting' (clue 3).",
             "At 15:36 a man in a red ski school jacket with one pole left cabin 23 (clue 4), and the bloody pole with the broken basket was in Kurt's locker (clue 6)."],
   "cleared": ["<b>Ursula</b> was having a massage at the summit from 15:00 to 16:00 (clue 5).",
               "<b>Nina</b> was teaching from 15:15, and <b>Felix</b> and <b>Max</b> were at work (clues 3, 4, 6)."]},
}

MYSTERIES = [globe, chalet, sleeper, cable]
