from lib import *  # evidence helpers

# Round 23 (18 Nov): 1 Rookie, 1 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- SPORTS DAY MEDALS (L1)
medals = {
 "slug": "the-sports-day-medals", "level": 1, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 154", "title_html": "THE SPORTS DAY<br>MEDALS", "title_plain": "The Sports Day Medals",
 "teaser": "The box of gold medals vanishes from the prize table during the egg-and-spoon race. A sticky handprint and a sun hat point to the culprit.",
 "intro": "At the <b>Oakfield Village Sports Day</b>, a box of 30 gold medals disappeared from the prize tent during the egg-and-spoon race. " + STD,
 "clues": [
  {"name": "Mrs Kate Doyle", "role": "Organiser", "label": "PRIZE TENT REPORT",
   "quote": "The medals were on the prize table at two. When I went to fetch them at quarter past for the first race winners, the box was gone. All I found was a big sticky handprint on the tablecloth.",
   "evidence": ev_rows("Prize tent report", [
       ("Medals on table", "14:00"),
       ("Missing", "14:15"),
       ("On the tablecloth", "A sticky, jammy handprint – an adult's size"),
       ("Also found", "A straw sun hat with a red ribbon, under the table"),
     ])},
  {"name": "Mr Barry Hope", "role": "Medal maker", "label": "BARRY'S STATEMENT",
   "quote": "Those are MY medals – I made them and the committee never paid my bill. But I was refereeing the egg-and-spoon race the whole time, I promise.",
   "evidence": ev_rows("Committee letter to Barry Hope", [
       ("Bill for medals", "£240"),
       ("Committee reply", "“We will pay after Sports Day.”"),
       ("Barry's reply", "“Pay now or I'll take them back.”"),
     ])},
  {"name": "Lucy Watts", "role": "Jam stall holder", "label": "JAM STALL SALES",
   "quote": "My jam doughnuts are very sticky! Only a few grown-ups bought them before the races started.",
   "evidence": ev_table("Jam stall – Saturday", ["Time", "Item", "Customer"], [
       ("13:40", "Jam doughnut", "Mrs K. Doyle"),
       ("13:55", "Jam doughnut", "Mr B. Hope"),
       ("14:20", "Lemonade", "Mr S. Grant"),
     ], mono_cols=(0,))},
  {"name": "Mr Sam Grant", "role": "Egg-and-spoon starter", "label": "RACE LIST",
   "quote": "I started the egg-and-spoon race and the referee was supposed to stand at the finish line. Nobody was there – I had to judge it myself!",
   "evidence": ev_table("Egg-and-spoon race – 14:05", ["Job", "Planned", "Who did it"], [
       ("Starter", "S. Grant", "S. Grant"),
       ("Referee at finish", "B. Hope", "S. Grant (referee missing)"),
     ])},
  {"name": "Gran Ivy Bell", "role": "Spectator", "label": "IVY'S PHOTO",
   "quote": "I was taking pictures of my grandson in the race. Look at the background of this one.",
   "evidence": ev_photos("Ivy's camera", [
       ("PIC_33", "14:08", "Grandson running with his egg. Behind him, a man without a hat comes out of the back of the prize tent carrying a box under his arm."),
     ])},
  {"name": "Mr Tom Fry", "role": "Hat stall holder", "label": "HAT STALL LIST",
   "quote": "I sold straw sun hats all morning – each one with a different coloured ribbon, so people don't mix them up.",
   "evidence": ev_table("Hat stall – sales", ["Ribbon", "Buyer"], [
       ("Blue", "Mrs K. Doyle"),
       ("Red", "Mr B. Hope"),
       ("Green", "Mr S. Grant"),
     ])},
 ],
 "solution": {"killer": "Mr Barry Hope",
   "motive": "Barry had never been paid for the medals and threatened to take them back (clue 2).",
   "proof": ["The medals went between 14:00 and 14:15, leaving an adult's jammy handprint and a straw hat with a red ribbon (clue 1).",
             "Barry says he refereed the egg-and-spoon race, but the referee never turned up (clue 4). At 14:08 a man with no hat carried a box out of the back of the prize tent (clue 5).",
             "Barry bought a jam doughnut at 13:55 (clue 3) and the red-ribbon hat is his (clue 6)."],
   "cleared": ["<b>Mrs Doyle</b> has the blue-ribbon hat, and <b>Mr Grant</b> the green one; Mr Grant was starting and judging the race (clues 4, 6).",
               "<b>Lucy</b>, <b>Gran Ivy</b> and <b>Mr Fry</b> only report what they saw or sold."]},
}

# ---------------------------------------------------------------- FARMERS' MARKET (L2)
market = {
 "slug": "the-farmers-market-scales", "level": 2, "crime": "FRAUD", "who": "cheat", "added": ADDED,
 "caseno": "CASE NO. 155", "title_html": "THE FARMERS'<br>MARKET SCALES", "title_plain": "The Farmers' Market Scales",
 "teaser": "Shoppers at a farmers' market are paying for honey they never got. Someone has fiddled the scales – and the numbers on the scales book tell on them.",
 "intro": "At the <b>Ashcombe Farmers' Market</b>, a customer complained that a 'one-pound' jar of honey weighed only 380 grams. Trading standards found that one stall's scales had been tampered with. " + STD,
 "clues": [
  {"name": "Officer Dev Patel", "role": "Trading standards officer", "label": "INSPECTION REPORT",
   "quote": "The market lends every stallholder a set of digital scales. One set had a small magnet glued under the plate – it made every weight read 15 percent heavy.",
   "evidence": ev_rows("Inspection report", [
       ("Scales tampered", "Set No. 6 – magnet under the plate"),
       ("Effect", "Reads 15% too heavy"),
       ("Lost to shoppers", "About £1,100 over two months"),
       ("Note", "Market scales are handed out by number each Saturday"),
     ])},
  {"name": "Holly Burns", "role": "Honey seller", "label": "HOLLY'S STATEMENT",
   "quote": "I always use scales No. 2 – it's my lucky number. Whoever had No. 6 is your cheat, not me.",
   "evidence": ev_rows("Holly Burns – honey stall", [
       ("Product", "Honey, sold by weight from big tubs into jars"),
       ("Complaint", "'One-pound' jar weighed 380 g instead of 454 g"),
       ("Sales this year", "Up 40% on last year"),
     ])},
  {"name": "Frank Moor", "role": "Market manager", "label": "SCALES BOOK",
   "quote": "Every stallholder signs for their scales when they arrive. I keep the book in the market hut.",
   "evidence": ev_table("Scales book – last eight Saturdays", ["Scales", "Signed out by"], [
       ("No. 2", "B. Lee (cheese) – every week"),
       ("No. 4", "A. Khan (spices)"),
       ("No. 6", "H. Burns (honey) – every week"),
     ])},
  {"name": "Bryn Lee", "role": "Cheese seller", "label": "CHEESE CHECK",
   "quote": "I've used No. 2 for years. I weighed a test cheese on my scales for the inspector – spot on.",
   "evidence": ev_table("Inspector's test weights", ["Scales", "Test weight", "Reading"], [
       ("No. 2", "500 g", "500 g"),
       ("No. 4", "500 g", "501 g"),
       ("No. 6", "500 g", "575 g"),
     ])},
  {"name": "Aisha Khan", "role": "Spice seller", "label": "GLUE RECEIPT",
   "quote": "Holly borrowed my glue gun last month – said a jar label kept coming off. She gave it back with a little magnet stuck to it.",
   "evidence": ev_note("HARDWARE SHOP RECEIPT IN HOLLY'S STALL BOX", [
       "Ashcombe Hardware – 12 Sept",
       "1 x neodymium magnet, 10 mm",
       "1 x superglue",
       "Paid: £6.40"],
     "– found by Officer Patel")},
  {"name": "Mrs Joy Elms", "role": "Shopper", "label": "JOY'S JAR",
   "quote": "I bought a 'one-pound' jar from the honey stall on Saturday and weighed it at home. Then I complained.",
   "evidence": ev_rows("Joy's kitchen scales", [
       ("Jar label", "1 lb (454 g)"),
       ("Actual honey", "380 g"),
       ("Bought from", "Honey stall, Saturday 10:15"),
     ])},
 ],
 "solution": {"killer": "Holly Burns",
   "motive": "Holly sold honey by weight – heavy-reading scales meant shoppers paid for honey they never got, worth about £1,100 (clues 1, 2).",
   "proof": ["Scales No. 6 had a magnet glued under the plate and read 15% too heavy (clues 1, 4).",
             "Holly says she always uses No. 2, but the scales book shows No. 2 always goes to Bryn and No. 6 to Holly every week (clue 3).",
             "A receipt for a magnet and superglue was in Holly's stall box, and she borrowed Aisha's glue gun (clue 5). Joy's 'one-pound' jar from her stall held only 380 g (clue 6)."],
   "cleared": ["<b>Bryn</b>'s scales No. 2 and <b>Aisha</b>'s No. 4 both weighed correctly (clue 4).",
               "<b>Frank</b> keeps the book, <b>Joy</b> is the shopper who complained, and <b>Officer Patel</b> investigated."]},
}

# ---------------------------------------------------------------- BREWERY (L3)
brewery = {
 "slug": "death-at-the-brewery", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 156", "title_html": "DEATH AT<br>THE BREWERY", "title_plain": "Death at the Brewery",
 "teaser": "A master brewer collapses in the fermenting room. The CO₂ alarm was switched off, the door was wedged – and the brewing log shows who was in the building.",
 "intro": "At <b>Old Mill Brewery</b>, master brewer Douglas Reid was found dead in the sealed fermenting room. The room had filled with carbon dioxide – and the gas alarm had been switched off. " + STD,
 "clues": [
  {"name": "DI Helen Marsh", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Reid was overcome by carbon dioxide from the fermenting tanks. Someone switched off the gas alarm and wedged the door shut from outside with a mash paddle.",
   "evidence": ev_rows("Police report – Old Mill Brewery", [
       ("Found", "07:30, fermenting room"),
       ("Cause", "Carbon dioxide poisoning"),
       ("Gas alarm", "Switched off at the panel at 05:52"),
       ("Door", "Wedged from outside with a wooden mash paddle"),
     ])},
  {"name": "Callum Reid", "role": "Douglas's nephew, assistant brewer", "label": "CALLUM'S STATEMENT",
   "quote": "I didn't get in until seven – I'd been at the gym from five until quarter to seven. My uncle always started the early brew on his own.",
   "evidence": ev_rows("Old Mill Brewery – ownership", [
       ("Douglas Reid", "60%"),
       ("Callum Reid", "40% – inherits the rest if Douglas dies"),
       ("Dispute", "Douglas refused to sell to a big beer company; Callum wanted the £2m"),
     ])},
  {"name": "Mairi Shaw", "role": "Brewery manager", "label": "DOOR LOG",
   "quote": "Every staff card is logged at the yard gate. I keep the system – it's never wrong.",
   "evidence": ev_table("Yard gate – Tuesday", ["Time", "Card", "Name"], [
       ("05:30", "B-01", "D. Reid"),
       ("05:47", "B-02", "C. Reid"),
       ("05:58", "B-02", "C. Reid (out)"),
       ("06:55", "B-02", "C. Reid"),
       ("07:20", "B-03", "M. Shaw"),
     ], mono_cols=(0,))},
  {"name": "Ollie Brandt", "role": "Gym receptionist", "label": "GYM SCANS",
   "quote": "Callum's a regular. He scanned in this morning – but not as early as he's saying.",
   "evidence": ev_table("FitHub gym – member scans", ["Time", "Member", "Event"], [
       ("06:10", "C. Reid", "In"),
       ("06:40", "C. Reid", "Out"),
     ], mono_cols=(0,))},
  {"name": "Gus Fraser", "role": "Delivery driver", "label": "DELIVERY NOTE",
   "quote": "I dropped the malt sacks in the yard at five to six. Callum's car was there, and he waved me off – said Douglas was busy.",
   "evidence": ev_rows("Malt delivery note", [
       ("Delivered", "05:55"),
       ("Signed by", "C. Reid"),
       ("Note", "Unloaded in yard; brewer 'busy in fermenting room'"),
     ])},
  {"name": "Rhona Kerr", "role": "Cleaner", "label": "CLEANER'S ROTA",
   "quote": "I only clean on Mondays and Thursdays, so I wasn't there on Tuesday. But I'll tell you this – the mash paddles are kept in the store, and only the brewers have a key.",
   "evidence": ev_table("Store key holders", ["Name", "Store key"], [
       ("D. Reid", "Yes"),
       ("C. Reid", "Yes"),
       ("M. Shaw", "No"),
       ("R. Kerr", "No"),
     ])},
 ],
 "solution": {"killer": "Callum Reid",
   "motive": "Callum would inherit his uncle's 60% and could sell to the big beer company for £2m (clue 2).",
   "proof": ["The gas alarm was switched off at 05:52 and the door wedged from outside with a mash paddle (clue 1).",
             "Callum says he was at the gym from five until 06:45. But his card entered the brewery at 05:47 and left at 05:58 (clue 3), he signed for a malt delivery at 05:55 (clue 5), and he only scanned into the gym at 06:10 (clue 4).",
             "Mash paddles are kept in the store, and only Douglas and Callum have a key (clue 6)."],
   "cleared": ["<b>Mairi</b> arrived at 07:20 and has no store key (clues 3, 6).",
               "<b>Rhona</b> doesn't work Tuesdays and has no store key (clue 6); <b>Gus</b> only delivered malt, and <b>Ollie</b> was at the gym."]},
}

# ---------------------------------------------------------------- HAUNTED HOTEL (L3)
haunted = {
 "slug": "murder-at-the-haunted-hotel", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 157", "title_html": "MURDER AT THE<br>HAUNTED HOTEL", "title_plain": "Murder at the Haunted Hotel",
 "teaser": "A ghost-hunting TV host dies during a live overnight broadcast. The 'ghost' on camera wore very real shoes – and the night-vision footage has a timestamp problem.",
 "intro": "At the <b>Blackmoor Hall Hotel</b>, famous for its ghost, TV presenter Rex Harlow was found dead on the main staircase during his live overnight show 'Spirit Hunters'. " + STD,
 "clues": [
  {"name": "DS Neil Ford", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Harlow was pushed down the stairs. He was wearing a heart monitor for the show's 'fear meter', so we know the exact second he died.",
   "evidence": ev_rows("Police report – Blackmoor Hall", [
       ("Found", "03:20, foot of the main staircase"),
       ("Heart monitor", "Spike of fear 02:47, stopped 02:48"),
       ("Show", "Live on air 00:00–04:00"),
       ("Staircase", "Lit only by the night-vision cameras"),
     ])},
  {"name": "Carla Vance", "role": "Co-presenter", "label": "LIVE RUNNING ORDER",
   "quote": "At quarter to three I was live on camera in the cellar, doing my séance segment. Millions of people saw me – you can't have a better alibi than that.",
   "evidence": ev_programme("Spirit Hunters – live running order", "Night of 31 October", [
       ("02:30", "Cellar séance – Carla Vance (pre-recorded, played as live)"),
       ("02:50", "Back to Rex on the staircase – live"),
       ("03:15", "Rex not answering – technical break"),
     ], None)},
  {"name": "Dan Pryce", "role": "Camera operator", "label": "NIGHT-VISION STILL",
   "quote": "Bella and I were in the outside broadcast truck all night, mixing the cameras. Carla insisted her séance was recorded at midnight 'so the candles look right'.",
   "evidence": ev_photos("Staircase camera 3 – night vision", [
       ("CAM-3", "02:47", "A pale figure in a long white sheet at the top of the stairs, beside Rex. Beneath the sheet: a pair of bright gold trainers."),
     ])},
  {"name": "Olive Grey", "role": "Hotel owner", "label": "HOTEL CONTRACT",
   "quote": "I let them film here because the show brings guests. But Rex was going to reveal on air that our ghost was a hoax – that would have ruined me. I was in the office with the TV on the whole night.",
   "evidence": ev_rows("Office phone log", [
       ("02:30–03:05", "O. Grey on a call to her sister – 35 minutes"),
       ("Note", "Office is in the east wing, far from the staircase"),
     ])},
  {"name": "Kai Lund", "role": "Runner", "label": "WARDROBE LIST",
   "quote": "I look after the costumes and kit. The ghost sheet for the show's 'reconstruction' went missing from the wardrobe at about half two.",
   "evidence": ev_table("Crew wardrobe – personal items", ["Name", "Shoes on set"], [
       ("Rex Harlow", "Black boots"),
       ("Carla Vance", "Gold trainers"),
       ("Dan Pryce", "Hiking boots"),
       ("Kai Lund", "White canvas shoes"),
     ])},
  {"name": "Bella Rhys", "role": "Producer", "label": "CONTRACT NOTE",
   "quote": "Rex and Carla were at war. He'd told the channel he wanted her fired after this episode – I had the email.",
   "evidence": ev_note("EMAIL FROM REX TO THE CHANNEL, 30 OCT", [
       "After Halloween I want Carla gone.",
       "Either she goes or I go to another",
       "channel – and I take the show",
       "with me."],
     "– printed by Bella Rhys")},
 ],
 "solution": {"killer": "Carla Vance",
   "motive": "Rex was trying to get Carla fired from the show after this episode (clue 6).",
   "proof": ["Rex was pushed at 02:47–02:48 (clue 1).",
             "Carla says she was live in the cellar at 02:45. But her séance was pre-recorded and only played as live (clues 2, 3) – she was free.",
             "At 02:47 a figure in a white sheet beside Rex was wearing bright gold trainers (clue 3) – Carla's shoes (clue 5). The ghost sheet went missing from the wardrobe at about 02:30 (clue 5)."],
   "cleared": ["<b>Olive</b> had a motive but was on the phone in the far east wing from 02:30 to 03:05 (clue 4).",
               "<b>Dan</b> was in the broadcast truck and wears hiking boots; <b>Kai</b> wears white shoes (clues 3, 5).",
               "<b>Bella</b> was in the broadcast truck with Dan all night (clue 3)."]},
}

MYSTERIES = [medals, market, brewery, haunted]
