from lib import *  # evidence helpers

# Round 24 (18 Nov): 1 Rookie, 1 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- PANCAKE RACE (L1)
pancake = {
 "slug": "the-pancake-race-cheat", "level": 1, "crime": "CHEATING", "who": "cheat", "added": ADDED,
 "caseno": "CASE NO. 158", "title_html": "THE PANCAKE<br>RACE CHEAT", "title_plain": "The Pancake Race Cheat",
 "teaser": "The winner of the village pancake race crosses the line without a crumb out of place. But was the pancake glued to the pan?",
 "intro": "In <b>Little Fenwick</b>, runners in the Shrove Tuesday pancake race must flip their pancake three times on the way. This year's winner's pancake looked suspiciously perfect. " + STD,
 "clues": [
  {"name": "Rev. Alan Moss", "role": "Race judge", "label": "RACE RULES",
   "quote": "Every runner gets a pan and a pancake from the church hall at the start. They must flip it three times, at the three flags. The winner was Gloria Pratt, by a mile.",
   "evidence": ev_rows("Pancake race rules", [
       ("Pans", "Handed out at the start – all identical, numbered 1 to 6"),
       ("Pancakes", "Cooked by the WI in the church hall"),
       ("Flips", "Three, one at each flag"),
       ("Prize", "Golden Frying Pan trophy and a year's free bread"),
     ])},
  {"name": "Gloria Pratt", "role": "Winner", "label": "GLORIA'S STATEMENT",
   "quote": "I flipped my pancake at every flag, fair and square. I've been practising in my kitchen for weeks!",
   "evidence": ev_rows("Pancake race – last two years", [
       ("2024", "1st Peggy Lane · 2nd Gloria Pratt (dropped pancake)"),
       ("2025", "1st Peggy Lane · 2nd Gloria Pratt (dropped pancake)"),
     ])},
  {"name": "Peggy Lane", "role": "Runner-up", "label": "PEGGY'S PHOTO",
   "quote": "I was right behind Gloria at the second flag. She waved her pan about but the pancake never left it.",
   "evidence": ev_photos("Photo by Peggy's husband", [
       ("IMG_101", "Flag 2", "Gloria 'flipping': the pan is tipped upside down, and the pancake is still stuck flat to it."),
     ])},
  {"name": "Mrs June Cole", "role": "WI pancake cook", "label": "PAN CHECK",
   "quote": "After the race we washed the pans. Pan number 4 had a sticky, shiny layer on the bottom that wouldn't come off.",
   "evidence": ev_table("Pans after the race", ["Pan", "Runner", "State"], [
       ("2", "Peggy Lane", "Normal – a little butter"),
       ("4", "Gloria Pratt", "Thick layer of clear, sticky syrup glue"),
       ("5", "Tom Kerr", "Normal"),
     ])},
  {"name": "Tom Kerr", "role": "Runner", "label": "SHOP RECEIPT",
   "quote": "I dropped my pancake at the first flag, so I came last. I did see Gloria fiddling with her pan behind the hall before the start.",
   "evidence": ev_note("VILLAGE SHOP – TILL ROLL", [
       "Tuesday 09:12",
       "1 x Golden syrup, extra thick",
       "1 x Pancake mix",
       "Customer: G. Pratt (loyalty card)"],
     "– Village Shop")},
  {"name": "Sid Park", "role": "Shopkeeper", "label": "START LIST",
   "quote": "I helped hand out the pans at the start. Everybody got the pan with their own number on it.",
   "evidence": ev_table("Start list", ["Runner", "Pan"], [
       ("Peggy Lane", "2"),
       ("Gloria Pratt", "4"),
       ("Tom Kerr", "5"),
     ])},
 ],
 "solution": {"killer": "Gloria Pratt",
   "motive": "Gloria had come second to Peggy two years running after dropping her pancake (clue 2).",
   "proof": ["Gloria says she flipped her pancake at every flag, but Peggy's photo shows it stuck flat to her upside-down pan (clue 3).",
             "Gloria had pan 4 (clue 6), and pan 4 had a sticky layer of syrup glue on it (clue 4).",
             "On race morning Gloria bought extra-thick golden syrup (clue 5), and Tom saw her fiddling with her pan before the start."],
   "cleared": ["<b>Peggy</b> and <b>Tom</b> had normal pans (clue 4).",
               "<b>Rev. Moss</b>, <b>Mrs Cole</b> and <b>Sid</b> organised the race – they didn't run in it (clues 1, 4, 6)."]},
}

# ---------------------------------------------------------------- BETTING SLIP (L2)
betting = {
 "slug": "the-winning-betting-slip", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 159", "title_html": "THE WINNING<br>BETTING SLIP", "title_plain": "The Winning Betting Slip",
 "teaser": "An old man's winning horse-racing slip worth £8,000 vanishes from his pub table. The thief cashed it fast – but the bookmaker's camera never blinks.",
 "intro": "In the <b>Red Lion</b> pub, pensioner Arthur Bell's betting slip – a 100-to-1 winner worth £8,000 – was stolen from his table while he went to the bar. " + STD,
 "clues": [
  {"name": "Arthur Bell", "role": "Pensioner", "label": "ARTHUR'S REPORT",
   "quote": "My horse came in at ten past three! I put the slip on my table under my pint and went to buy a round. When I got back at quarter past, it was gone.",
   "evidence": ev_rows("Theft report", [
       ("Race finished", "15:10 – 'Lucky Clover' wins at 100 to 1"),
       ("Slip left on table", "15:11"),
       ("Missing", "15:15"),
       ("Slip number", "BK-40719, £80 to win – payout £8,080"),
     ])},
  {"name": "Dave Ryder", "role": "Pub regular", "label": "DAVE'S STATEMENT",
   "quote": "I never left the darts board all afternoon. I was playing a match against Les from three till four.",
   "evidence": ev_rows("Dave Ryder – money", [
       ("Owes the pub", "£310 bar tab"),
       ("Note", "Landlady told him on Friday: 'Pay up or you're barred.'"),
     ])},
  {"name": "Les Grant", "role": "Darts player", "label": "DARTS SCORECARD",
   "quote": "Dave? He was my opponent – but he stopped halfway through. Said he had 'an errand' and was back twenty minutes later grinning like a cat.",
   "evidence": ev_table("Darts match – Saturday", ["Leg", "Ended", "Winner"], [
       ("1", "15:05", "D. Ryder"),
       ("2", "15:12", "L. Grant"),
       ("—", "15:13–15:34", "Match paused – D. Ryder 'popped out'"),
       ("3", "15:45", "L. Grant"),
     ], mono_cols=(1,))},
  {"name": "Mrs Rose Dean", "role": "Landlady", "label": "BAR TILL",
   "quote": "Arthur bought a round for the whole bar to celebrate – that's why he was so long at the counter. Then he paid off Dave's tab for him, bless him, not knowing.",
   "evidence": ev_table("Red Lion – bar till", ["Time", "Order", "Customer"], [
       ("15:11", "Round of drinks for the bar", "A. Bell"),
       ("15:40", "Bar tab paid in cash – £310", "D. Ryder"),
     ], mono_cols=(0,))},
  {"name": "Mo Akhtar", "role": "Bookmaker's clerk", "label": "BOOKMAKER'S RECORD",
   "quote": "Somebody cashed slip BK-40719 at our shop across the road at twenty past three. We pay big wins in cash. Our counter camera records everyone.",
   "evidence": ev_photos("Bookmaker's counter camera", [
       ("CAM-1", "15:20", "Slip BK-40719 paid out – £8,080 in cash. Customer: man in a red darts shirt with 'RYDER' on the back."),
     ])},
  {"name": "Jill Hart", "role": "Barmaid", "label": "STAFF NOTE",
   "quote": "I was collecting glasses all afternoon. I saw Dave lean over Arthur's table on his way to the door, but I thought he was just saying hello.",
   "evidence": ev_note("JILL'S NOTE FOR THE POLICE", [
       "About 15:13: Dave Ryder walked past",
       "Arthur's empty table, picked something up",
       "from under the pint glass and went out",
       "of the front door."],
     "– Jill")},
 ],
 "solution": {"killer": "Dave Ryder",
   "motive": "Dave owed the pub £310 and had been told to pay up or be barred (clue 2).",
   "proof": ["The slip disappeared from Arthur's table between 15:11 and 15:15 (clue 1).",
             "Dave says he never left the darts board, but the match paused from 15:13 to 15:34 while he 'popped out' (clue 3). At 15:13 Jill saw him take something from under Arthur's pint (clue 6).",
             "At 15:20 a man in a red 'RYDER' darts shirt cashed slip BK-40719 across the road (clue 5), and at 15:40 Dave suddenly paid his £310 tab in cash (clue 4)."],
   "cleared": ["<b>Les</b> was at the darts board throughout (clue 3), and <b>Arthur</b> was at the bar buying a round (clue 4).",
               "<b>Mrs Dean</b> was serving, <b>Jill</b> was collecting glasses, and <b>Mo</b> was behind the bookmaker's counter."]},
}

# ---------------------------------------------------------------- WIND FARM (L3)
windfarm = {
 "slug": "death-at-the-wind-farm", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 160", "title_html": "DEATH AT THE<br>WIND FARM", "title_plain": "Death at the Wind Farm",
 "teaser": "An engineer falls inside a wind turbine tower on a storm-free day. The turbine's own computer logged every door, ladder lock and stop – and one lie.",
 "intro": "At the <b>Carrig Moor wind farm</b>, maintenance engineer Fiona Doyle was found dead at the foot of the ladder inside turbine T7. Her safety harness had been unclipped from the rail. " + STD,
 "clues": [
  {"name": "DI Seán Walsh", "role": "Police", "label": "POLICE REPORT",
   "quote": "Ms Doyle fell from about 40 metres up the tower ladder. Her fall-arrest clip was found open, and there's a bruise on her hand where someone prised it off.",
   "evidence": ev_rows("Police report – turbine T7", [
       ("Found", "13:10, foot of the ladder inside T7"),
       ("Fall", "12:31 – recorded by the tower's motion sensor"),
       ("Harness", "Clip opened by force"),
       ("Access", "Tower door opens only with an engineer's card"),
     ])},
  {"name": "Rory Burke", "role": "Senior engineer", "label": "RORY'S STATEMENT",
   "quote": "I was in turbine T3 all morning, two kilometres away, changing a gearbox filter. I had my radio on – I'd have heard if Fiona called for help.",
   "evidence": ev_rows("Safety report – drafted by F. Doyle", [
       ("Subject", "Faked inspection records on turbines T3–T9"),
       ("Signed off by", "R. Burke"),
       ("Consequence", "Dismissal and prosecution"),
       ("Due to be sent", "Monday 09:00"),
     ])},
  {"name": "Aoife Nolan", "role": "Control-room operator", "label": "TOWER DOOR LOG",
   "quote": "From the control room I see every turbine's door and status. T7 was stopped for maintenance from eleven.",
   "evidence": ev_table("Turbine door cards – Thursday", ["Time", "Turbine", "Card"], [
       ("11:05", "T7", "F. Doyle – in"),
       ("11:40", "T3", "R. Burke – in"),
       ("12:10", "T3", "R. Burke – out"),
       ("12:18", "T7", "R. Burke – in"),
       ("12:40", "T7", "R. Burke – out"),
       ("12:55", "T3", "R. Burke – in"),
     ], mono_cols=(0,))},
  {"name": "Conor Fahy", "role": "Apprentice", "label": "VAN TRACKER",
   "quote": "I was with Rory in T3 until about ten past twelve, then he sent me back to the depot for parts. I took the small van.",
   "evidence": ev_table("Vehicle trackers", ["Time", "Vehicle", "Location"], [
       ("12:12", "Small van (C. Fahy)", "Leaves T3 for depot"),
       ("12:14", "Pick-up (R. Burke)", "Leaves T3"),
       ("12:17", "Pick-up (R. Burke)", "Parked at T7"),
       ("12:42", "Pick-up (R. Burke)", "Leaves T7"),
       ("12:52", "Pick-up (R. Burke)", "Back at T3"),
     ], mono_cols=(0,))},
  {"name": "Niamh Byrne", "role": "Site manager", "label": "LADDER LOCK LOG",
   "quote": "The ladder has a climb-assist motor that logs who uses it by their card. Only one person rode it up T7 after Fiona.",
   "evidence": ev_table("T7 climb-assist", ["Time", "Card", "Direction"], [
       ("11:08", "F. Doyle", "Up"),
       ("12:21", "R. Burke", "Up"),
       ("12:34", "R. Burke", "Down"),
     ], mono_cols=(0,))},
  {"name": "Paddy Quinn", "role": "Farmer, landowner", "label": "PADDY'S PHOTO",
   "quote": "I was fixing a fence by T7 and saw a white pick-up parked at the tower at lunchtime. I took a photo because I thought it was the meter man.",
   "evidence": ev_photos("Paddy's phone", [
       ("IMG_2210", "12:25", "White pick-up at the foot of turbine T7, door marked 'CARRIG MOOR – R. BURKE'."),
     ])},
 ],
 "solution": {"killer": "Rory Burke",
   "motive": "Fiona's safety report exposed the faked inspection records Rory had signed – he faced dismissal and prosecution (clue 2).",
   "proof": ["Fiona fell at 12:31 when her clip was forced open (clue 1).",
             "Rory says he was in T3 all morning. But his card left T3 at 12:10, entered T7 at 12:18 and left at 12:40 (clue 3), and his pick-up was parked at T7 from 12:17 to 12:42 (clue 4).",
             "He rode the climb-assist up T7 at 12:21 and down at 12:34 (clue 5), and Paddy photographed his pick-up at T7 at 12:25 (clue 6)."],
   "cleared": ["<b>Conor</b> was driving the small van to the depot from 12:12 (clue 4).",
               "<b>Aoife</b> was in the control room, <b>Niamh</b> keeps the logs, and <b>Paddy</b> was mending his fence outside – none have tower cards (clues 3, 5)."]},
}

# ---------------------------------------------------------------- MARINA (L3)
marina = {
 "slug": "murder-at-the-marina", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 161", "title_html": "MURDER AT<br>THE MARINA", "title_plain": "Murder at the Marina",
 "teaser": "A yacht broker is found dead on a luxury boat in the marina. The tide, a fuel receipt and a mooring rope tied the wrong way reveal who was aboard.",
 "intro": "At <b>Port Solent Marina</b>, yacht broker Julian Cross was found dead in the saloon of the motor yacht 'Serenity' on a Sunday evening. " + STD,
 "clues": [
  {"name": "DS Kim Lowe", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Cross was struck with a winch handle. The pathologist puts death between six and half past six. Serenity had been out at sea that afternoon and came back in at five to six.",
   "evidence": ev_rows("Police report – Port Solent", [
       ("Found", "19:40, saloon of 'Serenity', berth C14"),
       ("Death", "Between 18:00 and 18:30"),
       ("Weapon", "Winch handle from the cockpit"),
       ("Serenity", "Left berth 14:00, returned 17:55 (marina lock log)"),
     ])},
  {"name": "Victor Hale", "role": "Serenity's owner", "label": "VICTOR'S STATEMENT",
   "quote": "I took Julian out to show him the engines, brought her back at five to six and left him aboard doing paperwork. I was in the yacht club bar from six until eight.",
   "evidence": ev_rows("Broker's file on 'Serenity'", [
       ("For sale", "£1.9m – Victor in serious debt"),
       ("Julian's survey", "Hull damage hidden under new paint"),
       ("Julian's note", "“Must tell the buyer on Monday – sale off.”"),
     ])},
  {"name": "Mel Archer", "role": "Yacht club barman", "label": "CLUB BAR TILL",
   "quote": "Victor came in for a gin, yes – but not at six. He rushed in at about twenty to seven, ordered a large one and said, 'I've been here since six, haven't I?' with a wink.",
   "evidence": ev_table("Yacht club bar – Sunday", ["Time", "Order", "Member"], [
       ("18:05", "2 x beer", "S. Ford"),
       ("18:41", "Large gin and tonic", "V. Hale"),
       ("19:15", "White wine", "L. Grey"),
     ], mono_cols=(0,))},
  {"name": "Sam Ford", "role": "Marina hand", "label": "FUEL RECEIPT",
   "quote": "I was on the fuel pontoon until six, then in the club bar. Serenity didn't refuel – Mr Hale said the tanks were fine.",
   "evidence": ev_table("Fuel pontoon – Sunday", ["Time", "Boat", "Litres"], [
       ("17:40", "'Kittiwake'", "120"),
       ("17:52", "'Seahorse'", "80"),
       ("18:00", "Pontoon closed", "–"),
     ], mono_cols=(0,))},
  {"name": "Lily Grey", "role": "Neighbour on berth C15", "label": "LILY'S PHOTO",
   "quote": "I was varnishing my deck all evening next to Serenity. I heard a shout about quarter past six and took a picture when someone hurried off.",
   "evidence": ev_photos("Lily's phone", [
       ("IMG_4421", "18:16", "A man in a navy blazer with the yacht club badge jumps from Serenity's stern onto the pontoon, carrying a briefcase."),
     ])},
  {"name": "Tom Reyes", "role": "Buyer's surveyor", "label": "MOORING NOTE",
   "quote": "I came to meet Julian at half seven and found him. Funny thing – the mooring lines were tied in Victor's special knot, the one he always boasts about. Julian couldn't tie it.",
   "evidence": ev_rows("Surveyor's notes, 19:35", [
       ("Mooring lines", "Tied with a 'Hale hitch' – Victor's own knot, retied after the boat came in"),
       ("Briefcase", "Julian's briefcase missing"),
       ("Navy blazer with club badge", "Worn by yacht club members such as V. Hale"),
       ("Marina staff", "Wear green fleeces – S. Ford, M. Archer"),
     ])},
 ],
 "solution": {"killer": "Victor Hale",
   "motive": "Julian had found hidden hull damage and was going to call off Victor's £1.9m sale on Monday – and Victor was deep in debt (clue 2).",
   "proof": ["Julian died between 18:00 and 18:30, after Serenity returned at 17:55 (clue 1).",
             "Victor says he was in the club bar from six, but his first drink was at 18:41, and he asked the barman to say he'd been there since six (clue 3).",
             "At 18:16 a man in a navy club blazer jumped off Serenity carrying a briefcase (clue 5) – Julian's briefcase was missing, and only members like Victor wear that blazer (clue 6). The mooring lines were retied in Victor's own knot (clue 6)."],
   "cleared": ["<b>Sam</b> worked the fuel pontoon until 18:00, then bought drinks in the club bar at 18:05; staff wear green fleeces, not blazers (clues 3, 4, 6).",
               "<b>Lily</b> was varnishing her own deck, <b>Mel</b> was serving, and <b>Tom</b> only arrived at 19:30 (clues 5, 6)."]},
}

MYSTERIES = [pancake, betting, windfarm, marina]
