from lib import *  # evidence helpers

# Round 38 (18 Nov): 2 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- LOTTERY (L2)
lottery = {
 "slug": "the-office-lottery-ticket", "level": 2, "crime": "FRAUD", "who": "fraudster", "added": ADDED,
 "caseno": "CASE NO. 214", "title_html": "THE OFFICE<br>LOTTERY TICKET", "title_plain": "The Office Lottery Ticket",
 "teaser": "An office lottery syndicate wins £60,000 – but the organiser says their ticket lost. A shop till receipt, a group chat and a new car tell the true story.",
 "intro": "At <b>Penrose Insurance</b>, eight colleagues pay £2 a week into a lottery syndicate. On Saturday their numbers came up for £60,000. On Monday the organiser said she had 'forgotten to buy the ticket'. " + STD,
 "clues": [
  {"name": "Gary Mills", "role": "Syndicate member", "label": "SYNDICATE NUMBERS",
   "quote": "We've played the same numbers for six years. Saturday's draw was ours – every single one.",
   "evidence": ev_rows("Syndicate card", [
       ("Numbers", "4 – 11 – 19 – 23 – 37 – 42"),
       ("Saturday draw", "4 – 11 – 19 – 23 – 37 – 42"),
       ("Prize", "£60,000 (5 + bonus)"),
       ("Organiser", "Debbie Shaw – buys the ticket every Friday"),
     ])},
  {"name": "Debbie Shaw", "role": "Syndicate organiser", "label": "DEBBIE'S STATEMENT",
   "quote": "I'm so sorry – I was ill on Friday and forgot to buy the ticket. I've paid everyone's £2 back.",
   "evidence": ev_rows("Office sign-in sheet – Friday", [
       ("D. Shaw", "In 08:55 · Out 17:30"),
       ("Note", "No sick day recorded"),
     ])},
  {"name": "Mr Arjun Patel", "role": "Newsagent", "label": "TILL RECEIPT",
   "quote": "Debbie buys the office ticket from me every Friday lunchtime. Same numbers, every week.",
   "evidence": ev_table("Lottery sales – Friday", ["Time", "Numbers", "Paid"], [
       ("12:42", "4-11-19-23-37-42", "£2 – card ending 3391"),
       ("12:44", "Lucky dip", "£2 – cash"),
     ], mono_cols=(0,))},
  {"name": "Lisa Grant", "role": "Syndicate member", "label": "GROUP CHAT",
   "quote": "On Friday afternoon Debbie posted in the group chat like always. Then on Sunday she deleted the message – but I'd already screenshotted it.",
   "evidence": ev_note("SCREENSHOT – 'LOTTO GANG' CHAT", [
       "Fri 12:50 – Debbie: 'Ticket bought!",
       "Fingers crossed for the big one 🤞'",
       "[Sun 09:14 – message deleted by",
       "Debbie]"],
     "– Lisa's phone")},
  {"name": "Tom Rees", "role": "Bank fraud officer", "label": "BANK CHECK",
   "quote": "The police asked us whose card ends in 3391. And whether that person received a large payment this week.",
   "evidence": ev_rows("Bank reply to police", [
       ("Card ending 3391", "Debbie Shaw"),
       ("Monday", "Lottery prize £60,000 paid in"),
       ("Tuesday", "£24,000 to Grove Car Sales"),
     ])},
  {"name": "Nadia Cole", "role": "Syndicate member", "label": "NADIA'S STATEMENT",
   "quote": "I don't play the numbers – I just pay my £2. I was on holiday in Spain all last week, so I couldn't have bought anything.",
   "evidence": ev_rows("Holiday booking", [
       ("Passenger", "N. Cole"),
       ("Away", "Saturday to Saturday, Málaga"),
     ])},
 ],
 "solution": {"killer": "Debbie Shaw",
   "motive": "Debbie wanted to keep the whole £60,000 instead of sharing it eight ways (clue 5).",
   "proof": ["The syndicate's numbers won £60,000 (clue 1).",
             "Debbie says she was ill and forgot the ticket, but she was at work all Friday (clue 2), and the newsagent sold the syndicate numbers at 12:42 on a card ending 3391 (clue 3) – Debbie's card (clue 5).",
             "At 12:50 she posted 'Ticket bought!' and then deleted it on Sunday (clue 4). On Monday £60,000 was paid to her account (clue 5)."],
   "cleared": ["<b>Nadia</b> was in Spain all week (clue 6).",
               "<b>Gary</b>, <b>Lisa</b>, <b>Mr Patel</b> and <b>Tom</b> only report what they found."]},
}

# ---------------------------------------------------------------- SCOUT CAMP (L2)
scout = {
 "slug": "the-scout-camp-cash-box", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 215", "title_html": "THE SCOUT CAMP<br>CASH BOX", "title_plain": "The Scout Camp Cash Box",
 "teaser": "The tuck shop money disappears from a locked tent on the last night of scout camp. A campfire rota, a muddy footprint and a torch battery point to the thief.",
 "intro": "At the <b>Pinewood Scout Camp</b>, £340 of tuck shop money vanished from the cash box in the leaders' tent on the last night. The tent was zipped and padlocked. " + STD,
 "clues": [
  {"name": "Mrs Hilary Doyle", "role": "Camp leader", "label": "LEADER'S REPORT",
   "quote": "I counted the money at eight and locked it in the leaders' tent. At ten it was gone. The padlock was open – not broken.",
   "evidence": ev_rows("Leader's report", [
       ("Money counted", "20:00 – £340"),
       ("Missing", "22:00"),
       ("Padlock", "Opened with the code – 4 digits"),
       ("Code known by", "The four leaders only"),
     ])},
  {"name": "Craig Fenton", "role": "Assistant leader", "label": "CRAIG'S STATEMENT",
   "quote": "I was at the campfire from eight till ten leading the songs. Forty scouts can tell you that.",
   "evidence": ev_rows("Message on Craig's phone (shown to police)", [
       ("From", "Car garage"),
       ("Text", "“Your car repair is £320. Please pay by Monday or we keep the car.”"),
       ("Date", "That afternoon"),
     ])},
  {"name": "Jo Park", "role": "Assistant leader", "label": "CAMPFIRE ROTA",
   "quote": "We took turns leading the campfire songs. Craig did the first half hour, then went off 'to fetch more marshmallows'. He was gone a long time.",
   "evidence": ev_table("Campfire rota", ["Time", "Leading songs"], [
       ("20:00–20:30", "C. Fenton"),
       ("20:30–21:00", "J. Park"),
       ("21:00–21:30", "R. Bhatt"),
       ("21:30–22:00", "C. Fenton"),
     ], mono_cols=(0,))},
  {"name": "Ravi Bhatt", "role": "Assistant leader", "label": "RAVI'S STATEMENT",
   "quote": "I was with the campfire all night apart from my turn. Craig came back at about twenty past nine with marshmallows – and mud up to his knees.",
   "evidence": ev_rows("Camp map", [
       ("Campfire to leaders' tent", "5 minutes, along the stream (muddy)"),
       ("Campfire to food store", "2 minutes, on the path (dry)"),
     ])},
  {"name": "Scout Ellie Ward", "role": "Patrol leader, aged 14", "label": "ELLIE'S NOTE",
   "quote": "I went back to my tent for a jumper at about nine. I saw a leader's torch – a big red one – going into the leaders' tent.",
   "evidence": ev_note("ELLIE'S NOTE", [
       "About 21:00 – big red torch going",
       "into the leaders' tent. Someone",
       "tall, in a leader's green neckerchief.",
       "Came out 5 minutes later."],
     "– Ellie")},
  {"name": "Mr Bob Clay", "role": "Campsite warden", "label": "TORCH LIST",
   "quote": "Every leader was given a camp torch. Only one asked for the big red one.",
   "evidence": ev_table("Torches issued to leaders", ["Leader", "Torch"], [
       ("H. Doyle", "Small yellow"),
       ("C. Fenton", "Big red"),
       ("J. Park", "Small yellow"),
       ("R. Bhatt", "Head torch"),
     ])},
 ],
 "solution": {"killer": "Craig Fenton",
   "motive": "Craig needed £320 for his car repair by Monday (clue 2).",
   "proof": ["The money was taken between 20:00 and 22:00, by someone who knew the padlock code – a leader (clue 1).",
             "Craig says he led the songs from eight to ten, but he only led 20:00–20:30 and 21:30–22:00 and was away 'fetching marshmallows' (clue 3). He came back with mud to his knees – the muddy route goes to the leaders' tent, not the food store (clue 4).",
             "At about 21:00 Ellie saw a leader with a big red torch go into the leaders' tent (clue 5) – Craig has the only big red torch (clue 6)."],
   "cleared": ["<b>Jo</b> and <b>Ravi</b> were at the campfire and have yellow and head torches (clues 3, 6).",
               "<b>Mrs Doyle</b> has a small yellow torch and found the theft (clues 1, 6); <b>Ellie</b> and <b>Bob</b> are witnesses."]},
}

# ---------------------------------------------------------------- CASTLE (L3)
castle = {
 "slug": "death-at-the-castle-banquet", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 216", "title_html": "DEATH AT THE<br>CASTLE BANQUET", "title_plain": "Death at the Castle Banquet",
 "teaser": "A laird dies at his own medieval banquet after drinking from a silver goblet. The seating plan, a toast schedule and a lute player's song reveal the poisoner.",
 "intro": "At <b>Castle Dunmorrow</b>, Laird Angus Mackie collapsed at his Christmas medieval banquet just after the second toast. His silver goblet had been poisoned. " + STD,
 "clues": [
  {"name": "DI Fraser Moir", "role": "Police", "label": "POLICE REPORT",
   "quote": "The poison was in the laird's goblet only. It acts in minutes, and he drank from it twice – fine after the first toast, dead after the second.",
   "evidence": ev_rows("Police report – Castle Dunmorrow", [
       ("First toast", "20:00 – laird drank, no harm"),
       ("Second toast", "20:30 – laird drank, collapsed 20:35"),
       ("So poisoned", "Between 20:00 and 20:30"),
       ("Goblet", "Refilled once, at 20:15, from the wine jug"),
     ])},
  {"name": "Lady Fiona Mackie", "role": "Laird's niece", "label": "FIONA'S STATEMENT",
   "quote": "I sat at the far end of the long table all evening. I couldn't have reached my uncle's goblet even if I'd wanted to.",
   "evidence": ev_rows("Lawyer's letter to Lady Fiona", [
       ("Subject", "Your uncle's estate"),
       ("Text", "“The laird is changing his will on Monday to leave the castle to the National Trust.”"),
       ("Date", "Last week"),
     ])},
  {"name": "Hamish Reid", "role": "Butler", "label": "SEATING PLAN",
   "quote": "I made the seating plan. But during the dancing between the toasts, some guests swapped places to talk.",
   "evidence": ev_table("High table seating", ["Seat", "Guest"], [
       ("1 (head)", "Laird Angus Mackie"),
       ("2 (right)", "Rev. Ian Small"),
       ("3 (left)", "Mrs Moira Gunn"),
       ("12 (far end)", "Lady Fiona Mackie"),
     ])},
  {"name": "Rory Bell", "role": "Lute player", "label": "MINSTREL'S NOTE",
   "quote": "From the minstrel gallery I could see everything. While I played the dance at quarter past eight, a lady in a green velvet gown sat in the empty chair next to the laird and leaned over his goblet.",
   "evidence": ev_note("RORY'S SET LIST", [
       "20:15 – 'Dance of the Thistle'.",
       "Lady in green velvet, tartan sash,",
       "sat in seat 2 while Rev. Small",
       "danced. Hand over the laird's cup."],
     "– Rory")},
  {"name": "Mrs Moira Gunn", "role": "Guest, old friend", "label": "COSTUME LIST",
   "quote": "Everyone had a medieval costume from the castle wardrobe. I wore blue. Only one guest wore green velvet.",
   "evidence": ev_table("Banquet costumes", ["Guest", "Costume"], [
       ("Lady F. Mackie", "Green velvet gown, tartan sash"),
       ("Mrs M. Gunn", "Blue gown"),
       ("Rev. I. Small", "Brown monk's robe"),
       ("Hamish Reid (staff)", "Black livery"),
     ])},
  {"name": "Rev. Ian Small", "role": "Local minister", "label": "MINISTER'S STATEMENT",
   "quote": "I left my seat to dance the Thistle reel at quarter past eight. When I came back, my chair had been moved a little – and Fiona was walking back to the far end.",
   "evidence": ev_rows("Dance card", [
       ("20:15 reel", "Rev. Small with Mrs Gunn"),
       ("Laird", "Stayed seated – bad knee"),
     ])},
 ],
 "solution": {"killer": "Lady Fiona Mackie",
   "motive": "The laird was changing his will to leave the castle to the National Trust instead of Fiona (clue 2).",
   "proof": ["The goblet was poisoned between the toasts, 20:00–20:30 (clue 1).",
             "Fiona says she sat at the far end all evening (clues 2, 3). But at 20:15, while Rev. Small and Mrs Gunn danced, a lady in green velvet with a tartan sash sat in seat 2 and leaned over the laird's goblet (clues 4, 6).",
             "Only Fiona wore green velvet (clue 5), and Rev. Small saw her walk back to the far end (clue 6)."],
   "cleared": ["<b>Mrs Gunn</b> wore blue and was dancing; <b>Rev. Small</b> was dancing too (clues 5, 6).",
               "<b>Hamish</b> wore black livery, and <b>Rory</b> was playing in the gallery (clues 4, 5)."]},
}

# ---------------------------------------------------------------- ARCHIVE (L3)
archive = {
 "slug": "murder-in-the-city-archive", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 217", "title_html": "MURDER IN THE<br>CITY ARCHIVE", "title_plain": "Murder in the City Archive",
 "teaser": "An archivist is found dead in the vault after finding a document that could ruin a powerful family. A lift log and a pencil catch the killer.",
 "intro": "At the <b>Redbridge City Archive</b>, archivist Dr Ruth Okoye was found dead in the basement vault, crushed by a moving shelf. She had just found a 1952 land deed that proved the Harrington family's estate was stolen. " + STD,
 "clues": [
  {"name": "DS Kofi Mensah", "role": "Police", "label": "POLICE REPORT",
   "quote": "The shelves in the vault move on rails, turned by a hand wheel. Someone turned the wheel and closed the gap while she was inside.",
   "evidence": ev_rows("Police report – City Archive", [
       ("Found", "17:30, basement vault"),
       ("Time of death", "Between 15:40 and 16:10"),
       ("Shelf wheel", "Turned by hand – needs strength"),
       ("Missing", "The 1952 land deed"),
     ])},
  {"name": "Lord Edward Harrington", "role": "Archive visitor", "label": "EDWARD'S STATEMENT",
   "quote": "I was in the reading room upstairs all afternoon studying my family's letters. I never went down to the vault – visitors aren't allowed.",
   "evidence": ev_rows("Dr Okoye's email to a journalist", [
       ("Sent", "That morning"),
       ("Text", "“I have found proof that the Harrington estate was taken illegally in 1952. Lord Harrington knows – he's coming in today.”"),
     ])},
  {"name": "Gemma Fox", "role": "Reading room supervisor", "label": "READING ROOM SLIPS",
   "quote": "Every visitor fills in a slip when they leave their desk, even for the toilet. Lord Harrington left his desk once.",
   "evidence": ev_table("Reading room – desk slips", ["Time out", "Time back", "Visitor", "Reason"], [
       ("14:20", "14:25", "Ms P. Lowe", "Toilet"),
       ("15:45", "16:08", "Lord E. Harrington", "'Phone call'"),
     ], mono_cols=(0, 1))},
  {"name": "Kenny Dunn", "role": "Caretaker", "label": "LIFT LOG",
   "quote": "The staff lift to the basement needs a key card. Dr Okoye went down with her own card. Her spare card hangs on a hook by the reading room door – and it was used a few minutes later.",
   "evidence": ev_table("Staff lift – key card log", ["Time", "Card", "To"], [
       ("15:35", "R. Okoye – own card", "Basement"),
       ("15:48", "R. Okoye – spare card", "Basement"),
       ("16:04", "R. Okoye – spare card", "Ground floor"),
     ], mono_cols=(0,))},
  {"name": "Ms Priya Lowe", "role": "Archive visitor", "label": "PRIYA'S NOTE",
   "quote": "I sat next to Lord Harrington. When he came back he had dust on his sleeves and a pencil in his pocket – but he'd been using a fountain pen all day.",
   "evidence": ev_note("PRIYA'S NOTEBOOK", [
       "16:08 – Lord H back. Dust on both",
       "sleeves, breathing hard. Pencil in",
       "his top pocket – he'd been using",
       "a fountain pen all afternoon."],
     "– Priya")},
  {"name": "Dr Alan Shore", "role": "Head archivist", "label": "VAULT RULES",
   "quote": "In the vault, staff must use archive pencils only – grey ones stamped 'RCA'. They're kept in a pot by the vault door, nowhere else.",
   "evidence": ev_photos("Police photos", [
       ("IMG_51", "18:10", "Pot of grey pencils stamped 'RCA' by the vault door – one missing."),
       ("IMG_52", "18:30", "A grey 'RCA' pencil taken from Lord Harrington's jacket pocket."),
     ])},
 ],
 "solution": {"killer": "Lord Edward Harrington",
   "motive": "Dr Okoye had found proof that the Harrington estate was stolen, and was telling a journalist (clue 2).",
   "proof": ["Dr Okoye was killed in the vault between 15:40 and 16:10, and the 1952 deed was taken (clue 1).",
             "Lord Harrington says he never left the reading room for the vault, but he left his desk from 15:45 to 16:08 (clue 3) – and Dr Okoye's spare key card took the lift to the basement at 15:48 and back up at 16:04 (clue 4).",
             "He came back dusty with a pencil in his pocket (clue 5) – a grey 'RCA' vault pencil, which is kept only by the vault door (clue 6)."],
   "cleared": ["<b>Priya</b> was in the reading room, back at her desk by 14:25 (clue 3).",
               "<b>Gemma</b>, <b>Kenny</b> and <b>Dr Shore</b> only report what they found."]},
}

MYSTERIES = [lottery, scout, castle, archive]
