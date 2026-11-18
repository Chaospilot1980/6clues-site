from lib import *  # evidence helpers

# Round 40 (18 Nov): 4 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- HEDGE MAZE
maze = {
 "slug": "death-in-the-hedge-maze", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 222", "title_html": "DEATH IN THE<br>HEDGE MAZE", "title_plain": "Death in the Hedge Maze",
 "teaser": "A stately home's owner is found dead at the centre of his hedge maze during a winter lantern trail. Lantern numbers and a frosty footprint lead to the killer.",
 "intro": "At <b>Ashcombe Hall</b>, Sir Rupert Vane was found dead at the centre of his famous hedge maze during the winter lantern trail. He had been struck with a heavy garden lantern. " + STD,
 "clues": [
  {"name": "DS Holly Ward", "role": "Police", "label": "POLICE REPORT",
   "quote": "Sir Rupert died at the maze centre between 19:00 and 19:20. The weapon is lantern number 9 – every visitor carries a numbered lantern.",
   "evidence": ev_rows("Police report – Ashcombe Hall", [
       ("Found", "19:40, maze centre"),
       ("Time of death", "19:00–19:20"),
       ("Weapon", "Iron lantern No. 9 – glass broken"),
       ("Frost", "Fresh footprints with a ridged welly sole"),
     ])},
  {"name": "Cecily Vane", "role": "Sir Rupert's daughter", "label": "CECILY'S STATEMENT",
   "quote": "I was serving mulled wine at the entrance hut all evening. I never set foot in the maze.",
   "evidence": ev_rows("Letter from Sir Rupert", [
       ("To", "Cecily Vane"),
       ("Text", "“I am selling Ashcombe to a hotel group. You will not inherit the house.”"),
       ("Date", "Two days before"),
     ])},
  {"name": "Mrs Pam Hood", "role": "Lantern hire", "label": "LANTERN LIST",
   "quote": "Every lantern is signed out with a name. Number 9 went to a member of the family.",
   "evidence": ev_table("Lantern sign-out", ["No.", "Name", "Time"], [
       ("7", "Mr G. Ellis (guest)", "18:30"),
       ("8", "Mrs J. Lamb (guest)", "18:35"),
       ("9", "C. Vane", "18:55"),
     ], mono_cols=(0, 2))},
  {"name": "Josh Hart", "role": "Mulled wine helper", "label": "WINE HUT ROTA",
   "quote": "Cecily and I ran the wine hut. At five to seven she said she'd 'check the lanterns in the maze' and left me alone for about twenty-five minutes.",
   "evidence": ev_table("Wine hut – staff", ["Time", "Serving"], [
       ("18:00–18:55", "C. Vane, J. Hart"),
       ("18:55–19:22", "J. Hart only"),
       ("19:22–21:00", "C. Vane, J. Hart"),
     ], mono_cols=(0,))},
  {"name": "Mr George Ellis", "role": "Guest", "label": "GUEST'S NOTE",
   "quote": "Deep in the maze I passed a woman in a red coat carrying a lantern, walking fast towards the centre. Her lantern said 9.",
   "evidence": ev_note("GEORGE'S DIARY", [
       "About 19:05 – woman in red coat,",
       "green wellies, lantern '9', going",
       "fast towards the centre. Didn't",
       "say hello."],
     "– George")},
  {"name": "Ned Barlow", "role": "Head gardener", "label": "BOOT CHECK",
   "quote": "The police asked about the ridged welly prints. Family and staff all keep their wellies in the boot room.",
   "evidence": ev_table("Boot room", ["Owner", "Wellies", "Sole"], [
       ("C. Vane", "Green", "Ridged"),
       ("N. Barlow", "Black", "Flat"),
       ("J. Hart", "Trainers today", "–"),
     ])},
 ],
 "solution": {"killer": "Cecily Vane",
   "motive": "Sir Rupert was selling Ashcombe, so Cecily would not inherit it (clue 2).",
   "proof": ["Sir Rupert was killed with lantern No. 9 between 19:00 and 19:20 (clue 1). Lantern 9 was signed out to Cecily at 18:55 (clue 3).",
             "Cecily says she never left the wine hut, but she was away from 18:55 to 19:22 (clue 4).",
             "At 19:05 George saw a woman in green wellies with lantern 9 heading for the centre (clue 5), and the ridged welly prints match Cecily's green wellies (clues 1, 6)."],
   "cleared": ["<b>Josh</b> served alone at the hut and wore trainers (clues 4, 6). <b>Ned</b>'s wellies have flat soles (clue 6).",
               "<b>George</b> and <b>Mrs Hood</b> only report what they saw."]},
}

# ---------------------------------------------------------------- AIRPORT LOUNGE
airport = {
 "slug": "murder-in-the-airport-lounge", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 223", "title_html": "MURDER IN THE<br>AIRPORT LOUNGE", "title_plain": "Murder in the Airport Lounge",
 "teaser": "A tech boss is poisoned in a first-class airport lounge before a Christmas flight. Boarding scans and a coffee order prove one passenger lied.",
 "intro": "In the <b>Skyline First Lounge</b> at Heathfield Airport, tech founder Martin Kale collapsed and died after drinking an espresso. It had been poisoned. " + STD,
 "clues": [
  {"name": "DI Sara Kemp", "role": "Police", "label": "POLICE REPORT",
   "quote": "The poison was added to his espresso while he took a phone call in the quiet booth. The coffee sat unattended on his table from 14:10 to 14:18.",
   "evidence": ev_rows("Police report – Skyline Lounge", [
       ("Coffee served", "14:08"),
       ("Martin in phone booth", "14:10–14:18"),
       ("Drank coffee", "14:19 · collapsed 14:30"),
       ("Poison", "Fast-acting – in the espresso"),
     ])},
  {"name": "Olivia Shaw", "role": "Co-founder", "label": "OLIVIA'S STATEMENT",
   "quote": "I left the lounge at two o'clock to board my flight to Geneva. I was on the plane when he died.",
   "evidence": ev_rows("Board meeting minutes", [
       ("Item 1", "Martin Kale proposes removing Olivia Shaw as co-founder"),
       ("Vote", "Next Monday"),
     ])},
  {"name": "Tom Bell", "role": "Gate agent, gate 22", "label": "BOARDING SCANS",
   "quote": "The Geneva flight boards at gate 22. Every boarding pass is scanned. One passenger was very late.",
   "evidence": ev_table("Gate 22 – Geneva flight", ["Passenger", "Scanned"], [
       ("Mr A. Grant", "13:55"),
       ("Ms O. Shaw", "14:24 – last to board, running"),
     ], mono_cols=(1,))},
  {"name": "Lena Park", "role": "Lounge barista", "label": "COFFEE ORDERS",
   "quote": "Olivia ordered a hot chocolate at five past two and drank it at the table next to Mr Kale's.",
   "evidence": ev_table("Lounge orders", ["Time", "Order", "Guest"], [
       ("14:05", "Hot chocolate", "O. Shaw"),
       ("14:08", "Espresso", "M. Kale"),
       ("14:16", "Bill closed", "O. Shaw – 'in a hurry'"),
     ], mono_cols=(0,))},
  {"name": "Andy Grant", "role": "Martin's assistant", "label": "ANDY'S STATEMENT",
   "quote": "I'm on the same Geneva flight. I boarded early and was in seat 3A from five to two – the crew will tell you.",
   "evidence": ev_rows("Cabin crew note", [
       ("Seat 3A", "Mr A. Grant – seated 13:57, did not leave"),
     ])},
  {"name": "Jade Moss", "role": "Lounge cleaner", "label": "BIN FIND",
   "quote": "When I emptied the bin by the table next to Mr Kale's, I found a tiny empty glass bottle wrapped in a napkin with lipstick on it.",
   "evidence": ev_photos("Police photo", [
       ("IMG_102", "15:00", "Empty 5 ml glass vial in a napkin, coral lipstick mark. From the bin beside table 6 – O. Shaw's table."),
     ])},
 ],
 "solution": {"killer": "Olivia Shaw",
   "motive": "Martin was going to remove Olivia as co-founder (clue 2).",
   "proof": ["The espresso was poisoned while Martin was in the phone booth, 14:10–14:18 (clue 1).",
             "Olivia says she left at 14:00 and was on the plane, but she was at the next table until she closed her bill at 14:16 (clue 4) and boarded last at 14:24 (clue 3).",
             "An empty vial in a lipstick-marked napkin was in the bin beside her table (clue 6)."],
   "cleared": ["<b>Andy</b> was in seat 3A from 13:57 (clues 3, 5).",
               "<b>Lena</b>, <b>Tom</b> and <b>Jade</b> only report what they saw."]},
}

# ---------------------------------------------------------------- YACHT
yacht = {
 "slug": "death-aboard-the-yacht", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 224", "title_html": "DEATH ABOARD<br>THE YACHT", "title_plain": "Death Aboard the Yacht",
 "teaser": "A shipping tycoon goes overboard from his yacht on a calm night. The anchor watch, a wet towel and the ship's tender reveal who was on deck with him.",
 "intro": "Aboard the yacht <b>Aurora</b>, anchored off Monaco, shipping tycoon Stavros Leandros went overboard on a calm night. He had been struck before he fell. " + STD,
 "clues": [
  {"name": "Capitaine Luc Marin", "role": "Harbour police", "label": "POLICE REPORT",
   "quote": "Mr Leandros was hit on the head on the aft deck and fell into the sea between 23:30 and 23:50.",
   "evidence": ev_rows("Police report – yacht Aurora", [
       ("Fell", "23:30–23:50, from the aft deck"),
       ("Head wound", "Struck with a winch handle"),
       ("Aft deck", "Wet bare footprints leading to the swim platform"),
     ])},
  {"name": "Nikos Leandros", "role": "Stavros's son", "label": "NIKOS'S STATEMENT",
   "quote": "I took the tender ashore at eleven to go to the casino. I didn't come back until one.",
   "evidence": ev_rows("Stavros's email", [
       ("To", "Board of Leandros Shipping"),
       ("Text", "“My son Nikos is stealing from the company. He leaves the board tomorrow.”"),
       ("Sent", "That evening, 21:00"),
     ])},
  {"name": "Mate Erik Holm", "role": "First mate", "label": "ANCHOR WATCH",
   "quote": "I keep the anchor watch log. The tender went ashore at 23:00 – but it came back at 23:25 and went out again at 23:55.",
   "evidence": ev_table("Anchor watch – tender", ["Time", "Tender"], [
       ("23:00", "Out – N. Leandros to shore"),
       ("23:25", "Back alongside – swim platform"),
       ("23:55", "Out again to shore"),
     ], mono_cols=(0,))},
  {"name": "Mrs Helena Leandros", "role": "Stavros's wife", "label": "HELENA'S STATEMENT",
   "quote": "I went to bed at eleven with a headache. I didn't hear anything – our cabin is at the front.",
   "evidence": ev_rows("Stewardess's note", [
       ("23:00", "Mrs Leandros to bed – tea delivered 23:15"),
       ("23:45", "Checked on her – asleep"),
     ])},
  {"name": "Marc Lebrun", "role": "Casino doorman", "label": "CASINO ENTRY",
   "quote": "Mr Nikos Leandros signed in at the casino. Not at eleven – later.",
   "evidence": ev_rows("Casino entry log", [
       ("Guest", "N. Leandros"),
       ("Entered", "00:10"),
       ("Note", "Wet trouser cuffs, no socks"),
     ])},
  {"name": "Rosa Diaz", "role": "Stewardess", "label": "TOWEL FIND",
   "quote": "In the morning I found a wet beach towel in the tender, and a winch handle missing from the aft deck.",
   "evidence": ev_photos("Rosa's phone", [
       ("IMG_331", "07:10", "Inside the tender: a wet towel with the monogram 'NL', and a pair of soaked deck shoes."),
     ])},
 ],
 "solution": {"killer": "Nikos Leandros",
   "motive": "Stavros had found out Nikos was stealing and was removing him from the board (clue 2).",
   "proof": ["Stavros was struck and fell from the aft deck between 23:30 and 23:50 (clue 1).",
             "Nikos says he went ashore at 23:00 and stayed there, but the tender came back to the swim platform at 23:25 and left again at 23:55 (clue 3), and he only entered the casino at 00:10 with wet cuffs (clue 5).",
             "A wet towel monogrammed 'NL' and soaked deck shoes were in the tender (clue 6)."],
   "cleared": ["<b>Helena</b> was in bed, checked by the stewardess at 23:15 and 23:45 (clue 4).",
               "<b>Erik</b>, <b>Rosa</b> and <b>Marc</b> only report what they saw."]},
}

# ---------------------------------------------------------------- BANK VAULT
bank = {
 "slug": "murder-in-the-bank-vault", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 225", "title_html": "MURDER IN THE<br>BANK VAULT", "title_plain": "Murder in the Bank Vault",
 "teaser": "A bank manager is found dead inside the time-locked vault on Christmas Eve. The time lock, two keys and a coffee cup reveal who was inside with him.",
 "intro": "At <b>Whitmore Private Bank</b>, manager Desmond Clarke was found dead inside the vault on Christmas Eve morning. The vault needs two keys held by two different people. " + STD,
 "clues": [
  {"name": "DI Grace Hill", "role": "Police", "label": "POLICE REPORT",
   "quote": "The vault has a time lock: it can only be opened between 08:00 and 08:30. Mr Clarke was killed inside it during that window.",
   "evidence": ev_rows("Police report – Whitmore Bank", [
       ("Vault opened", "08:02"),
       ("Vault closed", "08:26 (time lock)"),
       ("Found", "10:00, when the vault reopened"),
       ("Weapon", "Heavy deposit box lid"),
     ])},
  {"name": "Julia Frost", "role": "Deputy manager", "label": "JULIA'S STATEMENT",
   "quote": "I opened the vault with Desmond at eight, turned my key and went straight back upstairs. He stayed inside alone.",
   "evidence": ev_rows("Audit email", [
       ("To", "Desmond Clarke"),
       ("Text", "“Three customer boxes are short of gold coins. Only the deputy manager has signed for them.”"),
       ("Date", "23 December"),
     ])},
  {"name": "Kevin Moss", "role": "Security guard", "label": "VAULT CAMERA",
   "quote": "The camera outside the vault door records who comes and goes. Two went in. Only one came out before the time lock closed.",
   "evidence": ev_table("Vault door camera", ["Time", "Event"], [
       ("08:02", "D. Clarke and J. Frost enter"),
       ("08:24", "J. Frost leaves, alone"),
       ("08:26", "Door closes – time lock"),
     ], mono_cols=(0,))},
  {"name": "Paula Reyes", "role": "Cashier", "label": "COFFEE NOTE",
   "quote": "Julia came up to the counter at about twenty-five past eight, very pale, and asked for a coffee. There was dust on her suit.",
   "evidence": ev_note("PAULA'S NOTE", [
       "08:25 – Julia at the counter, white",
       "as a sheet. Grey dust on her navy",
       "jacket. Spilled her coffee. Said",
       "'Long morning.'"],
     "– Paula")},
  {"name": "Mr Arthur Penn", "role": "Customer", "label": "CUSTOMER'S STATEMENT",
   "quote": "I had an appointment to see my deposit box at 08:15, but they told me the vault was 'busy'. I waited in the lobby until nine.",
   "evidence": ev_rows("Lobby visitor book", [
       ("A. Penn", "In 08:10 – waited in lobby until 09:00"),
     ])},
  {"name": "Tom Gale", "role": "IT technician", "label": "KEY LOG",
   "quote": "The two vault keys log every turn. Desmond's key and Julia's key both turned at 08:02. No one else has a key.",
   "evidence": ev_table("Vault key log", ["Time", "Key"], [
       ("08:02", "Key A – D. Clarke"),
       ("08:02", "Key B – J. Frost"),
     ], mono_cols=(0,))},
 ],
 "solution": {"killer": "Julia Frost",
   "motive": "An audit was about to show Julia had stolen gold coins from customer boxes (clue 2).",
   "proof": ["Desmond was killed inside the vault between 08:02 and 08:26 (clue 1).",
             "Julia says she turned her key and went straight back upstairs, but the camera shows she stayed inside until 08:24 (clue 3).",
             "She arrived at the counter at 08:25 pale and covered in dust (clue 4), and only she and Desmond had keys (clue 6)."],
   "cleared": ["<b>Mr Penn</b> waited in the lobby from 08:10 to 09:00 (clue 5).",
               "<b>Kevin</b>, <b>Paula</b> and <b>Tom</b> only report what they saw (clues 3, 4, 6)."]},
}

MYSTERIES = [maze, airport, yacht, bank]
