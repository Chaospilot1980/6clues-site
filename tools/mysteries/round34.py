from lib import *  # evidence helpers

# Round 34 (18 Nov): 2 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- POTTERY (L2)
pottery = {
 "slug": "the-pottery-kiln-sabotage", "level": 2, "crime": "SABOTAGE", "who": "saboteur", "added": ADDED,
 "caseno": "CASE NO. 198", "title_html": "THE POTTERY<br>KILN SABOTAGE", "title_plain": "The Pottery Kiln Sabotage",
 "teaser": "A potter's whole exhibition cracks in the kiln the night before opening. The kiln controller remembers who turned the heat up – and when.",
 "intro": "At the <b>Saltmarsh Pottery Studio</b>, Iris Penn's thirty vases for her first exhibition all cracked in the kiln overnight. Someone had changed the firing programme. " + STD,
 "clues": [
  {"name": "Iris Penn", "role": "Potter", "label": "IRIS'S REPORT",
   "quote": "I set the kiln to my usual slow firing at six and went home. In the morning every piece was cracked – fired far too fast and too hot.",
   "evidence": ev_rows("Iris's report", [
       ("Kiln loaded", "18:00"),
       ("Programme set", "'Slow bisque' – 100 °C per hour"),
       ("Morning", "All 30 vases cracked"),
       ("Exhibition", "Opening the next day"),
     ])},
  {"name": "Derek Holt", "role": "Studio member", "label": "DEREK'S STATEMENT",
   "quote": "I left before Iris that evening – about half five. I wasn't even in the building when she loaded the kiln.",
   "evidence": ev_rows("Gallery email to studio members", [
       ("Subject", "Spring exhibition"),
       ("Text", "“We have chosen Iris Penn's work for the spring show instead of Derek Holt's.”"),
       ("Date", "One month before"),
     ])},
  {"name": "Kim Sato", "role": "Studio manager", "label": "KILN LOG",
   "quote": "The kiln's controller records every change, and every member has their own PIN to change a programme.",
   "evidence": ev_table("Kiln controller log", ["Time", "PIN", "Change"], [
       ("18:02", "1104 (I. Penn)", "Slow bisque – 100 °C/h"),
       ("19:47", "2290 (D. Holt)", "Fast glaze – 400 °C/h, max 1,280 °C"),
     ], mono_cols=(0,))},
  {"name": "Lou Grant", "role": "Studio member", "label": "LOU'S STATEMENT",
   "quote": "I was at a pottery class in town from seven until nine – I teach it. Twenty students saw me.",
   "evidence": ev_rows("Evening class register", [
       ("Class", "Beginners' wheel – Community Hall"),
       ("Time", "19:00–21:00"),
       ("Teacher", "L. Grant – signed in 18:50"),
     ])},
  {"name": "Mr Ted Fowler", "role": "Neighbour, café owner", "label": "TED'S NOTE",
   "quote": "I was closing my café across the road. Just before eight I saw the studio lights come on and a man go in with a key.",
   "evidence": ev_note("TED'S NOTE", [
       "About 19:45 – studio lights on.",
       "Tall man, grey beard, green apron",
       "under his coat, let himself in.",
       "Lights off at 19:55."],
     "– Ted")},
  {"name": "Anya Fox", "role": "Studio member", "label": "MEMBER LIST",
   "quote": "There are only four of us with keys: Iris, Derek, Lou and me. I was in Edinburgh visiting my sister all week.",
   "evidence": ev_table("Studio members", ["Member", "Looks", "Studio apron"], [
       ("I. Penn", "Short, dark hair", "Blue"),
       ("D. Holt", "Tall, grey beard", "Green"),
       ("L. Grant", "Short, bald", "Red"),
       ("A. Fox", "Tall, red hair", "Yellow"),
     ])},
 ],
 "solution": {"killer": "Derek Holt",
   "motive": "The gallery chose Iris's work instead of Derek's (clue 2).",
   "proof": ["Iris set a slow firing at 18:02, but at 19:47 the programme was changed to a fast, very hot glaze firing with Derek's PIN (clue 3).",
             "Derek says he left at 17:30 and never came back, but at about 19:45 Ted saw a tall man with a grey beard and a green apron let himself into the studio (clue 5).",
             "Derek is the only member who is tall with a grey beard and wears a green apron (clue 6)."],
   "cleared": ["<b>Lou</b> was teaching a class from 19:00 to 21:00 (clue 4), and <b>Anya</b> was in Edinburgh (clue 6).",
               "<b>Iris</b> set the safe firing, and <b>Kim</b> and <b>Ted</b> only report what they saw (clues 3, 5)."]},
}

# ---------------------------------------------------------------- VET (L2)
vet = {
 "slug": "the-vet-clinic-drug-theft", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 199", "title_html": "THE VET CLINIC<br>DRUG THEFT", "title_plain": "The Vet Clinic Drug Theft",
 "teaser": "Medicines keep vanishing from a vet clinic's locked cupboard. A stock book, a dog that never existed and a swipe card reveal the thief.",
 "intro": "At <b>Brookside Vets</b>, head vet Dr Amira Saleh noticed that boxes of expensive animal medicine were vanishing from the locked drug cupboard every week. " + STD,
 "clues": [
  {"name": "Dr Amira Saleh", "role": "Head vet", "label": "STOCK COUNT",
   "quote": "Every box taken out has to be written down against a patient. The book looks perfect – but the patients in it don't add up.",
   "evidence": ev_table("Drug cupboard book – November", ["Date", "Medicine", "Patient", "Signed"], [
       ("3 Nov", "Pain relief ×2", "'Biscuit' (dog)", "G. Lane"),
       ("10 Nov", "Pain relief ×3", "'Biscuit' (dog)", "G. Lane"),
       ("17 Nov", "Pain relief ×3", "'Biscuit' (dog)", "G. Lane"),
       ("12 Nov", "Antibiotic ×1", "'Luna' (cat)", "P. Ray"),
     ])},
  {"name": "Gina Lane", "role": "Veterinary nurse", "label": "GINA'S STATEMENT",
   "quote": "Biscuit is a real dog with bad hips – he needs a lot of pain relief. I've done nothing wrong.",
   "evidence": ev_rows("Patient records search", [
       ("Search", "'Biscuit' – dog"),
       ("Result", "No patient record, no owner, no visits"),
       ("Note", "No bills ever paid for 'Biscuit'"),
     ])},
  {"name": "Pete Ray", "role": "Veterinary nurse", "label": "PETE'S STATEMENT",
   "quote": "I signed out one antibiotic for Luna, a cat who had an operation on the twelfth. Check her file – it's all there.",
   "evidence": ev_rows("Patient record – 'Luna'", [
       ("Owner", "Mrs J. Holt"),
       ("12 Nov", "Operation – antibiotic given"),
       ("Bill", "Paid by card"),
     ])},
  {"name": "Sid Moran", "role": "Practice manager", "label": "SWIPE CARD LOG",
   "quote": "The drug cupboard opens with a swipe card. Each nurse has their own card.",
   "evidence": ev_table("Drug cupboard – swipe log", ["Date", "Time", "Card"], [
       ("3 Nov", "19:10", "G. Lane"),
       ("10 Nov", "19:05", "G. Lane"),
       ("12 Nov", "11:30", "P. Ray"),
       ("17 Nov", "19:12", "G. Lane"),
     ], note="The clinic closes at 18:30.")},
  {"name": "Rosa Kemp", "role": "Receptionist", "label": "ROSA'S NOTE",
   "quote": "Gina often stays late on Mondays to 'tidy up'. Last week I saw her put a box in her handbag on the way out.",
   "evidence": ev_note("ROSA'S NOTE", [
       "Mon 17 Nov, about 19:15 – Gina",
       "leaving by back door. Small white",
       "boxes in her open handbag. She",
       "zipped it up when she saw me."],
     "– Rosa")},
  {"name": "Dan Hollis", "role": "Online seller", "label": "MARKETPLACE",
   "quote": "I run a pet supplies website. Someone was selling the same pain relief cheap on a second-hand site – too cheap. I reported it.",
   "evidence": ev_rows("Second-hand site listing", [
       ("Item", "Dog pain relief – 8 boxes, 'unwanted'"),
       ("Seller", "gina.l.petcare"),
       ("Posted", "18 Nov"),
     ])},
 ],
 "solution": {"killer": "Gina Lane",
   "motive": "Gina was selling the stolen medicine online (clue 6).",
   "proof": ["Eight boxes of pain relief were signed out for a dog called 'Biscuit', all by Gina (clue 1).",
             "Gina says Biscuit is a real dog, but the clinic has no record, owner, visit or bill for any 'Biscuit' (clue 2).",
             "Gina's card opened the cupboard after closing on each of those days (clue 4), Rosa saw her leave with boxes on 17 Nov (clue 5), and 'gina.l.petcare' listed 8 boxes the next day (clue 6)."],
   "cleared": ["<b>Pete</b>'s one antibiotic was for a real cat with a paid bill, during opening hours (clues 3, 4).",
               "<b>Dr Saleh</b>, <b>Sid</b>, <b>Rosa</b> and <b>Dan</b> only report what they found."]},
}

# ---------------------------------------------------------------- CAROUSEL (L3)
carousel = {
 "slug": "death-on-the-carousel", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 200", "title_html": "DEATH ON<br>THE CAROUSEL", "title_plain": "Death on the Carousel",
 "teaser": "A fairground owner is found dead on his antique carousel after the Christmas fair closes. An organ music roll and a toffee-apple stick trap the killer.",
 "intro": "At the <b>Winter Wonderfair</b> on the seafront, owner Reg Fairweather was found dead on his antique carousel after closing time, struck with a heavy brass starting handle. " + STD,
 "clues": [
  {"name": "DS Pat Morgan", "role": "Police", "label": "POLICE REPORT",
   "quote": "The carousel's organ plays one paper music roll per ride. The roll stopped halfway through 'The Skaters' Waltz' – the killer switched it off when Reg fell.",
   "evidence": ev_rows("Police report – Winter Wonderfair", [
       ("Found", "22:40, on the carousel platform"),
       ("Weapon", "Brass starting handle – kept on a hook by the organ"),
       ("Organ", "Stopped 4 minutes into 'The Skaters' Waltz'"),
       ("By the body", "A sticky toffee-apple stick"),
     ])},
  {"name": "Lenny Fairweather", "role": "Reg's nephew", "label": "LENNY'S STATEMENT",
   "quote": "I ran the dodgems until the fair closed at ten, then I counted the takings in the office. I never went near the carousel.",
   "evidence": ev_rows("Reg's will (draft)", [
       ("Old will", "Fair left to nephew Lenny"),
       ("New will", "Fair to be sold – money to charity"),
       ("Signing", "Booked with the lawyer for the next morning"),
     ])},
  {"name": "Dot Hughes", "role": "Organ keeper", "label": "MUSIC ROLL LOG",
   "quote": "I keep the list of which roll goes on and when. Reg asked me to put 'The Skaters' Waltz' on at quarter past ten for one last private ride – then I went home.",
   "evidence": ev_table("Organ roll log", ["Time", "Roll", "Length"], [
       ("21:45", "Jingle Bells (last public ride)", "5 min"),
       ("22:15", "The Skaters' Waltz (Reg's private ride)", "8 min"),
     ], mono_cols=(0,), note="So the music stopped at about 22:19.")},
  {"name": "Kyle Brennan", "role": "Dodgems attendant", "label": "DODGEM LOG",
   "quote": "Lenny gave me the dodgems to close at ten past ten. He said he was going to the office – but the office is the other way from where he went.",
   "evidence": ev_table("Dodgems – staff on duty", ["Time", "Attendant"], [
       ("18:00–22:10", "L. Fairweather, K. Brennan"),
       ("22:10–22:35", "K. Brennan only"),
     ], mono_cols=(0,))},
  {"name": "Marge Tilly", "role": "Toffee-apple stall", "label": "STALL NOTE",
   "quote": "I sold my last toffee apple at quarter past ten to Lenny – he always buys one on his break. I saw him walk off towards the carousel eating it.",
   "evidence": ev_note("MARGE'S TILL ROLL", [
       "22:14 – 1 toffee apple, £2,",
       "staff price – Lenny F.",
       "LAST ONE SOLD TONIGHT.",
       "Closed stall 22:16."],
     "– Marge")},
  {"name": "Beth Fairweather", "role": "Reg's daughter", "label": "BETH'S STATEMENT",
   "quote": "Dad and I fell out years ago, but I came to make peace. I was waiting in my car in the car park from ten until he didn't come.",
   "evidence": ev_rows("Car park camera", [
       ("Car", "B. Fairweather"),
       ("In", "21:58"),
       ("Driver", "Seen in car 21:58–22:45 – never got out"),
     ])},
 ],
 "solution": {"killer": "Lenny Fairweather",
   "motive": "Reg was signing a new will the next morning that would cut Lenny out (clue 2).",
   "proof": ["Reg was struck at about 22:19, when the organ stopped 4 minutes into 'The Skaters' Waltz' (clues 1, 3).",
             "Lenny says he went from the dodgems to the office, but he left the dodgems at 22:10 and walked the other way (clue 4).",
             "Marge sold the last toffee apple of the night to Lenny at 22:14 and saw him walk to the carousel (clue 5) – and a toffee-apple stick lay by the body (clue 1)."],
   "cleared": ["<b>Beth</b> sat in her car from 21:58 to 22:45 (clue 6).",
               "<b>Kyle</b> ran the dodgems alone, <b>Dot</b> went home after starting the roll, and <b>Marge</b> closed her stall at 22:16 (clues 3, 4, 5)."]},
}

# ---------------------------------------------------------------- THEATRE ORGAN / CINEMA (L3)
cinema = {
 "slug": "murder-at-the-picture-palace", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 201", "title_html": "MURDER AT THE<br>PICTURE PALACE", "title_plain": "Murder at the Picture Palace",
 "teaser": "A cinema owner dies in the projection booth during the Christmas classic. A reel change, a usher's torch and a popcorn receipt show who left their seat.",
 "intro": "At the old <b>Regal Picture Palace</b>, owner Victor Ames was found dead in the projection booth during a sold-out Christmas screening. He had been hit with a film canister. " + STD,
 "clues": [
  {"name": "DI Sunita Bose", "role": "Police", "label": "POLICE REPORT",
   "quote": "The film is shown on old reels. Victor changed reel two to reel three himself – then reel three ran out and nobody changed it. That tells us when he died.",
   "evidence": ev_rows("Police report – Regal Picture Palace", [
       ("Found", "21:20, projection booth"),
       ("Reels", "Reel 3 put on at 20:20 by Victor; reel 4 never loaded"),
       ("Reel 3 ends", "20:40 – screen went white"),
       ("So he died", "Between 20:20 and 20:40"),
     ])},
  {"name": "Gemma Ames", "role": "Victor's wife", "label": "GEMMA'S STATEMENT",
   "quote": "I sat in the front row of the balcony through the whole film. I never moved until the screen went white.",
   "evidence": ev_rows("Victor's notes", [
       ("To his lawyer", "“Start the divorce. Gemma gets nothing – the prenup is clear.”"),
       ("Date", "That morning"),
     ])},
  {"name": "Liam Ward", "role": "Usher", "label": "USHER'S TORCH LOG",
   "quote": "I patrol with a torch and note anyone who leaves their seat during the film. The balcony door to the booth stairs is right by the front row.",
   "evidence": ev_table("Usher's notes – balcony", ["Time", "Note"], [
       ("20:05", "Man, seat B4, to toilets – back 20:09"),
       ("20:22", "Woman, front row seat A1, through booth stairs door"),
       ("20:36", "Woman back to A1, breathing hard"),
     ], mono_cols=(0,))},
  {"name": "Rita Cole", "role": "Box office", "label": "SEAT LIST",
   "quote": "Every seat is booked by name. Here's the balcony front row.",
   "evidence": ev_table("Balcony front row bookings", ["Seat", "Name"], [
       ("A1", "G. Ames"),
       ("A2", "N. Ames"),
       ("A3", "M. Reid"),
     ])},
  {"name": "Noah Ames", "role": "Victor's son", "label": "POPCORN RECEIPT",
   "quote": "I went down to buy popcorn just before eight and stayed in the bar downstairs for the rest of the film. Mum was still in her seat when I left.",
   "evidence": ev_table("Bar till – downstairs", ["Time", "Item", "Paid by"], [
       ("19:58", "Large popcorn", "N. Ames"),
       ("20:25", "Pint of beer", "N. Ames"),
       ("20:38", "Pint of beer", "N. Ames"),
     ], mono_cols=(0,))},
  {"name": "Martin Reid", "role": "Projectionist's assistant", "label": "MARTIN'S STATEMENT",
   "quote": "Victor sent me home at eight – he wanted to run the Christmas film himself, like in the old days. I was on the bus by ten past.",
   "evidence": ev_rows("Bus pass log", [
       ("Card", "M. Reid"),
       ("Boarded", "20:11, Regal stop"),
       ("Got off", "20:42, Elm Park"),
     ])},
 ],
 "solution": {"killer": "Gemma Ames",
   "motive": "Victor was divorcing Gemma, and she would get nothing (clue 2).",
   "proof": ["Victor died between 20:20 and 20:40, after he loaded reel three (clue 1).",
             "Gemma says she never left her seat, but at 20:22 the woman in seat A1 went through the booth stairs door and came back breathing hard at 20:36 (clue 3).",
             "Seat A1 is booked to G. Ames – Gemma (clue 4)."],
   "cleared": ["<b>Noah</b> was buying drinks in the bar downstairs at 20:25 and 20:38 (clue 5).",
               "<b>Martin</b> was on the bus from 20:11 to 20:42 (clue 6); <b>Liam</b> and <b>Rita</b> only report what they saw (clues 3, 4)."]},
}

MYSTERIES = [pottery, vet, carousel, cinema]
