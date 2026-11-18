from lib import *  # evidence helpers

# Round 35 (18 Nov): 2 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- HOCKEY (L2)
hockey = {
 "slug": "the-ice-hockey-trophy-theft", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 202", "title_html": "THE ICE HOCKEY<br>TROPHY THEFT", "title_plain": "The Ice Hockey Trophy Theft",
 "teaser": "The league trophy vanishes from the rink's glass cabinet during the Christmas derby. A Zamboni schedule, a dropped puck and a sports bag give the thief away.",
 "intro": "At the <b>Northfield Ice Arena</b>, the silver league trophy was taken from its locked glass cabinet in the lobby during the Christmas derby against the Harbour Hawks. " + STD,
 "clues": [
  {"name": "Mr Gordon Fisk", "role": "Club chairman", "label": "CHAIRMAN'S REPORT",
   "quote": "The trophy was in the cabinet when the game started at seven. At the second break, at twenty past eight, the cabinet was empty – unlocked, not smashed.",
   "evidence": ev_rows("Chairman's report", [
       ("Trophy seen", "19:00"),
       ("Missing", "20:20"),
       ("Cabinet", "Unlocked with a key – no damage"),
       ("On the floor", "A puck with 'HAWKS' printed on it"),
     ])},
  {"name": "Jess Doran", "role": "Ice technician", "label": "KEY RING",
   "quote": "Lobby cabinet keys are on the staff key ring in the ice room. I drive the ice machine – the Zamboni – during the breaks, so I'm on the ice then.",
   "evidence": ev_table("Staff key ring – sign-out", ["Time", "Name"], [
       ("19:30", "Signed out – S. Hart"),
       ("19:52", "Returned – S. Hart"),
     ], mono_cols=(0,))},
  {"name": "Sam Hart", "role": "Harbour Hawks kit manager", "label": "SAM'S STATEMENT",
   "quote": "I was in the away bench for the whole first period sorting sticks. I never touched any keys – I don't even work here.",
   "evidence": ev_rows("Harbour Hawks forum post", [
       ("Posted by", "SamHart_HawksKit"),
       ("Date", "One week before"),
       ("Text", "“That trophy belongs in Harbour. Maybe we'll just bring it home ourselves.”"),
     ])},
  {"name": "Tony Webb", "role": "Lobby steward", "label": "STEWARD'S NOTE",
   "quote": "During the first period the lobby is empty – everyone's watching the game. At about quarter to eight a man in a Hawks tracksuit came through with a big kit bag.",
   "evidence": ev_note("STEWARD'S LOG", [
       "19:44 – man in red Hawks tracksuit,",
       "large kit bag, near trophy cabinet.",
       "Said he was 'looking for the toilets'.",
       "Left towards away changing room."],
     "– Tony")},
  {"name": "Kerry Lowe", "role": "Northfield player", "label": "KERRY'S STATEMENT",
   "quote": "I was on the ice for the whole first period – I scored twice! Then I was in our changing room at the break.",
   "evidence": ev_table("Match sheet – first period", ["Time", "Event"], [
       ("19:12", "Goal – K. Lowe (Northfield)"),
       ("19:41", "Goal – K. Lowe (Northfield)"),
       ("19:50", "End of first period"),
     ], mono_cols=(0,))},
  {"name": "Officer Dee Marsh", "role": "Police", "label": "BAG SEARCH",
   "quote": "We searched the away team's kit at the end of the game. The trophy was wrapped in towels in one bag.",
   "evidence": ev_photos("Police photo", [
       ("IMG_884", "21:40", "Away changing room: a large Hawks kit bag labelled 'KIT MANAGER – S. HART', unzipped, showing the silver trophy wrapped in towels."),
     ])},
 ],
 "solution": {"killer": "Sam Hart",
   "motive": "Sam wanted to 'bring the trophy home' to Harbour (clue 3).",
   "proof": ["The trophy went between 19:00 and 20:20, taken with a key (clue 1).",
             "Sam says he never touched any keys, but he signed out the staff key ring from 19:30 to 19:52 (clue 2).",
             "At 19:44 a man in a Hawks tracksuit with a big kit bag was at the cabinet (clue 4), and the trophy was found in the kit manager's bag – S. Hart (clue 6)."],
   "cleared": ["<b>Kerry</b> was on the ice scoring at 19:41 (clue 5), and <b>Jess</b> drives the ice machine in the breaks (clue 2).",
               "<b>Gordon</b>, <b>Tony</b> and <b>Officer Marsh</b> only report what they found."]},
}

# ---------------------------------------------------------------- FORGED PAINTING (L2)
forgery = {
 "slug": "the-gallery-forgery-swap", "level": 2, "crime": "FRAUD", "who": "fraudster", "added": ADDED,
 "caseno": "CASE NO. 203", "title_html": "THE GALLERY<br>FORGERY SWAP", "title_plain": "The Gallery Forgery Swap",
 "teaser": "A small gallery's prize seascape turns out to be a fresh fake. Wet paint under UV light, a restorer's diary and an art-supply receipt reveal the forger.",
 "intro": "At the <b>Harbour Light Gallery</b>, the painting 'Storm off Fowey' (valued at £40,000) was sent for insurance checks. The expert found it was a modern copy – painted in the last few weeks. " + STD,
 "clues": [
  {"name": "Dr Ruth Fenn", "role": "Art expert", "label": "UV REPORT",
   "quote": "Under UV light, the paint glows like new. Some of it is still soft. And the canvas has a supplier's stamp from this year.",
   "evidence": ev_rows("Expert's report", [
       ("Paint", "Modern acrylic – some still soft"),
       ("Canvas stamp", "'Kemp's Art Supplies – 2026'"),
       ("Painted", "Within the last 4–6 weeks"),
       ("Original", "Oil, 1902 – missing"),
     ])},
  {"name": "Alan Pryce", "role": "Picture restorer", "label": "ALAN'S STATEMENT",
   "quote": "I had the painting in my workshop for cleaning in October, yes. But I gave back the real one. Someone must have swapped it after.",
   "evidence": ev_rows("Restorer's job sheet", [
       ("Job", "Clean 'Storm off Fowey'"),
       ("In", "1 October"),
       ("Out", "29 October – returned to gallery"),
       ("Signed", "A. Pryce"),
     ])},
  {"name": "Mrs Edie Kemp", "role": "Art supply shop owner", "label": "SHOP RECEIPT",
   "quote": "Only one person bought a canvas that exact size this autumn – it's an unusual size, so I ordered it in specially.",
   "evidence": ev_rows("Kemp's Art Supplies – special order", [
       ("Item", "Linen canvas 61 × 46 cm + Prussian blue, white, grey acrylics"),
       ("Ordered", "28 September"),
       ("Collected", "3 October"),
       ("Customer", "A. Pryce"),
     ])},
  {"name": "Nina Holt", "role": "Gallery owner", "label": "NINA'S STATEMENT",
   "quote": "The painting has hung in the main room since it came back on the twenty-ninth. Nobody has taken it down since.",
   "evidence": ev_table("Gallery camera – main room", ["Date", "Note"], [
       ("29 Oct", "Painting rehung by N. Holt"),
       ("30 Oct – 15 Nov", "Painting on the wall, never touched"),
       ("16 Nov", "Taken down for the insurance expert"),
     ])},
  {"name": "Joe Sutton", "role": "Gallery assistant", "label": "JOE'S STATEMENT",
   "quote": "I visited Alan's workshop in mid-October to drop off a frame. There were two paintings of the same storm on two easels side by side.",
   "evidence": ev_note("JOE'S TEXT TO NINA", [
       "15 Oct – at Alan's. Funny – he's",
       "got TWO Fowey storms side by side.",
       "Said one is 'a study for practice'.",
       "Smelled of fresh paint."],
     "– Joe")},
  {"name": "Clive Barr", "role": "Private collector", "label": "COLLECTOR'S LETTER",
   "quote": "In November a restorer offered me an original 'Storm off Fowey', 1902, for £15,000 cash. I said it was hanging in Harbour Light – he said 'not any more'.",
   "evidence": ev_rows("Letter to Clive Barr", [
       ("Date", "5 November"),
       ("Offer", "'Storm off Fowey', oil, 1902 – £15,000 cash, quick sale"),
       ("Signed", "A.P."),
     ])},
 ],
 "solution": {"killer": "Alan Pryce",
   "motive": "Alan wanted to sell the real painting for £15,000 cash (clue 6).",
   "proof": ["The painting in the gallery is a copy on a 2026 canvas from Kemp's, painted in the last few weeks (clue 1).",
             "Alan says he returned the real painting, but he bought that unusual canvas size and the matching paints on 3 October, while he had the original (clues 2, 3), and Joe saw two copies of the storm in his workshop on 15 October (clue 5).",
             "The painting hasn't been touched at the gallery since it came back from Alan (clue 4), and 'A.P.' then offered the original to a collector (clue 6)."],
   "cleared": ["<b>Nina</b> only rehung it and the camera shows nobody touched it (clue 4).",
               "<b>Joe</b>, <b>Mrs Kemp</b>, <b>Clive</b> and <b>Dr Fenn</b> only report what they saw."]},
}

# ---------------------------------------------------------------- MOUNTAIN HUT (L3)
hut = {
 "slug": "death-at-the-mountain-hut", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 204", "title_html": "DEATH AT THE<br>MOUNTAIN HUT", "title_plain": "Death at the Mountain Hut",
 "teaser": "A guide dies at a snowed-in mountain hut. Four climbers swear they never left the room – but fresh footprints, a stove log and a crampon say otherwise.",
 "intro": "At the <b>Rifugio Stella</b>, 2,800 metres up, mountain guide Paolo Neri was found dead in the snow behind the hut's woodshed. He had been struck with an ice axe. A storm had snowed everyone in. " + STD,
 "clues": [
  {"name": "Marco Bassi", "role": "Hut warden", "label": "WARDEN'S REPORT",
   "quote": "It stopped snowing at ten. When I found Paolo at eleven, there were two sets of footprints in the fresh snow from the back door to the woodshed – his, and one other set that came back.",
   "evidence": ev_rows("Warden's report", [
       ("Snow stopped", "22:00"),
       ("Found", "23:00, behind the woodshed"),
       ("Footprints", "Two sets out – only one set back. Fresh, after 22:00"),
       ("Returning prints", "Crampon spikes – 12 points"),
     ])},
  {"name": "Elsa Brandt", "role": "Climber", "label": "ELSA'S STATEMENT",
   "quote": "All four of us sat in the common room playing cards from nine until the warden came in shouting. Nobody went out in that cold.",
   "evidence": ev_rows("Guide's notebook – P. Neri", [
       ("Note", "Elsa Brandt lied about her summit last year – she never reached the top"),
       ("Plan", "“Tell the climbing magazine when I get down. Her sponsor will drop her.”"),
     ])},
  {"name": "Karl Weiss", "role": "Climber", "label": "STOVE LOG",
   "quote": "I was on wood duty – I had to fill the stove every twenty minutes, so I wrote down who fetched wood. Elsa offered to go once.",
   "evidence": ev_table("Stove log", ["Time", "Wood fetched by"], [
       ("21:40", "K. Weiss"),
       ("22:00", "K. Weiss"),
       ("22:20", "E. Brandt – 'my turn'"),
       ("22:40", "K. Weiss"),
     ], mono_cols=(0,))},
  {"name": "Anna Rossi", "role": "Climber", "label": "ANNA'S NOTE",
   "quote": "When Elsa came back from the woodshed she had snow up to her knees and no wood. She said the pile was frozen. She was gone a long time for one trip.",
   "evidence": ev_note("ANNA'S DIARY", [
       "Elsa went for wood at 22:20 –",
       "back 22:38, no wood, crampons on,",
       "breathing hard. Said 'frozen pile'.",
       "Karl went at 22:40 – back in 4 min."],
     "– Anna")},
  {"name": "Tom Hale", "role": "Climber", "label": "KIT LIST",
   "quote": "Everyone's crampons are different. Only one of us brought the heavy twelve-point ones – the rest of us have ten-point walking crampons.",
   "evidence": ev_table("Climbers' kit", ["Climber", "Crampons"], [
       ("E. Brandt", "12-point"),
       ("K. Weiss", "10-point"),
       ("A. Rossi", "10-point"),
       ("T. Hale", "10-point"),
     ])},
  {"name": "Dr Lia Conti", "role": "Mountain rescue doctor", "label": "DOCTOR'S NOTE",
   "quote": "Paolo died between ten and eleven. From the snow on him and his body temperature, I'd say around half past ten.",
   "evidence": ev_rows("Rescue doctor's notes", [
       ("Time of death", "About 22:30 (22:15–22:45)"),
       ("Wound", "Ice axe – pick end"),
       ("Snow on body", "Light – after the storm stopped"),
     ])},
 ],
 "solution": {"killer": "Elsa Brandt",
   "motive": "Paolo was going to reveal that Elsa lied about reaching a summit, and her sponsor would drop her (clue 2).",
   "proof": ["Paolo died at about 22:30, after the snow stopped (clues 1, 6). Someone walked out with him and came back in 12-point crampons (clue 1).",
             "Elsa says nobody left the common room, but she went out 'for wood' from 22:20 to 22:38 and came back with no wood, out of breath (clues 3, 4).",
             "Elsa is the only climber with 12-point crampons (clue 5)."],
   "cleared": ["<b>Karl</b>'s trips were short and he wears 10-point crampons (clues 3, 4, 5).",
               "<b>Anna</b> and <b>Tom</b> stayed inside and wear 10-point crampons; <b>Marco</b> and <b>Dr Conti</b> only report what they found (clues 1, 5, 6)."]},
}

# ---------------------------------------------------------------- TEA PLANTATION (L3)
tea = {
 "slug": "murder-at-the-tea-estate", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 205", "title_html": "MURDER AT<br>THE TEA ESTATE", "title_plain": "Murder at the Tea Estate",
 "teaser": "A tea estate owner is poisoned at his own tasting. Only one cup was poisoned – and the tasting order, a kettle log and a sugar bowl show who knew which one.",
 "intro": "At the <b>Glenmara Tea Estate</b> in the hills, owner Charles Ashworth died at the annual tea tasting after drinking from cup number 5. He had been poisoned. " + STD,
 "clues": [
  {"name": "Inspector Priya Das", "role": "Police", "label": "POLICE REPORT",
   "quote": "Only cup 5 was poisoned. The poison was in the sugar that went into that cup – the other cups had no sugar at all.",
   "evidence": ev_rows("Police report – Glenmara Estate", [
       ("Died", "16:20, tasting room"),
       ("Poison", "In cup 5 only – mixed with sugar"),
       ("Other cups", "1–4 and 6: no sugar, no poison"),
       ("Sugar bowl", "Clean – poison added to one spoonful only"),
     ])},
  {"name": "Rajan Pillai", "role": "Head taster", "label": "RAJAN'S STATEMENT",
   "quote": "I poured all six cups, but I don't add sugar – tasters never do. I didn't even know Charles liked sugar.",
   "evidence": ev_rows("Estate letter to R. Pillai", [
       ("From", "Charles Ashworth"),
       ("Text", "“After thirty years, your contract will not be renewed. The new owners want their own taster.”"),
       ("Date", "One week before"),
     ])},
  {"name": "Mrs Edith Ashworth", "role": "Charles's wife", "label": "TASTING ORDER",
   "quote": "Charles always tasted in the same order, one to six. And he always took one sugar in cup 5 – the Darjeeling. Only someone who'd tasted with him for years would know.",
   "evidence": ev_table("Tasting card – Charles's order", ["Cup", "Tea", "Sugar?"], [
       ("1", "Assam", "No"),
       ("2", "Ceylon", "No"),
       ("3", "Nilgiri", "No"),
       ("4", "Green", "No"),
       ("5", "Darjeeling", "One spoon – always"),
       ("6", "Glenmara Gold", "No"),
     ])},
  {"name": "Sita Menon", "role": "Kitchen assistant", "label": "KITCHEN NOTE",
   "quote": "I filled the kettle and brought the tray. Mr Rajan put the sugar in cup 5 himself – I saw him do it while Mr Ashworth was on the phone.",
   "evidence": ev_note("SITA'S NOTE", [
       "16:05 – Mr Rajan poured six cups.",
       "16:08 – took a small paper twist from",
       "his pocket, then a spoon of sugar,",
       "into cup 5. Stirred it."],
     "– Sita")},
  {"name": "Henry Ashworth", "role": "Charles's son", "label": "HENRY'S STATEMENT",
   "quote": "I wanted Father to sell the estate, yes – and he was going to. I arrived from the airport at quarter past four, just before he drank.",
   "evidence": ev_rows("Gate log", [
       ("Car", "H. Ashworth"),
       ("In", "16:14"),
       ("Note", "Went straight to the veranda, not the tasting room"),
     ])},
  {"name": "Dr Ken Bose", "role": "Estate doctor", "label": "DOCTOR'S NOTE",
   "quote": "I've known Rajan for years. He doesn't take sugar – but he always knew exactly how Charles liked his tea.",
   "evidence": ev_rows("Doctor's notes", [
       ("Poison", "Fast – acts in 5–10 minutes"),
       ("Drank cup 5", "About 16:12"),
       ("Collapsed", "16:20"),
     ])},
 ],
 "solution": {"killer": "Rajan Pillai",
   "motive": "Charles was ending Rajan's contract after thirty years (clue 2).",
   "proof": ["Only cup 5 was poisoned, through one spoonful of sugar (clue 1). Charles always took one sugar in cup 5 – something only a long-time tasting partner would know (clue 3).",
             "Rajan says he doesn't add sugar and didn't know Charles took it, but Sita saw him tip a paper twist and a spoon of sugar into cup 5 at 16:08 (clue 4).",
             "Charles drank cup 5 at about 16:12 and collapsed at 16:20 (clue 6)."],
   "cleared": ["<b>Henry</b> only arrived at 16:14, after the cup was poisoned, and went to the veranda (clue 5).",
               "<b>Edith</b>, <b>Sita</b> and <b>Dr Bose</b> only report what they know (clues 3, 4, 6)."]},
}

MYSTERIES = [hockey, forgery, hut, tea]
