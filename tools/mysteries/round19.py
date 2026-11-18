from lib import *  # evidence helpers

# Round 19 (18 Nov): 1 Rookie, 1 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- PET SHOW (L1)
petshow = {
 "slug": "the-pet-show-rosette", "level": 1, "crime": "SABOTAGE", "who": "saboteur", "added": ADDED,
 "caseno": "CASE NO. 138", "title_html": "THE PET SHOW<br>ROSETTE", "title_plain": "The Pet Show Rosette",
 "teaser": "The favourite rabbit at the village pet show is found with its fur dyed green an hour before judging. Somebody's sticky fingers give them away.",
 "intro": "At the <b>Hollybrook Village Pet Show</b>, champion rabbit Biscuit was found with green dye all over her white fur just before the 'Best in Show' judging. " + STD,
 "clues": [
  {"name": "Ellie Moss", "role": "Biscuit's owner", "label": "SHOW REPORT",
   "quote": "I left Biscuit in her hutch in the rabbit tent at half past one and went to get a cup of tea. When I came back at two, she was green!",
   "evidence": ev_rows("Show report – rabbit tent", [
       ("Biscuit alone", "13:30–14:00"),
       ("Dye", "Green food colouring, poured over her back"),
       ("Found by hutch", "An empty bottle of 'Leafy Green' food colouring"),
       ("Best in Show", "Judging at 15:00, prize: silver rosette and £50"),
     ])},
  {"name": "Gary Pike", "role": "Rival rabbit owner", "label": "GARY'S STATEMENT",
   "quote": "I was in the cake tent the whole time, judging the sponges. I never went near the rabbit tent after lunch.",
   "evidence": ev_rows("Best in Show – last year", [
       ("1st", "Biscuit (Ellie Moss)"),
       ("2nd", "Thumper (Gary Pike)"),
       ("Note", "Gary complained the judges 'always pick the white one'"),
     ])},
  {"name": "Mrs June Hart", "role": "Cake tent organiser", "label": "CAKE JUDGING LIST",
   "quote": "Gary was supposed to judge the sponges with me, but he didn't turn up until ten past two. I did them all myself.",
   "evidence": ev_table("Cake tent – judging", ["Time", "Class", "Judges"], [
       ("13:30", "Victoria sponge", "J. Hart"),
       ("13:45", "Lemon drizzle", "J. Hart"),
       ("14:10", "Chocolate cake", "J. Hart, G. Pike"),
     ], mono_cols=(0,))},
  {"name": "Sam Lee", "role": "Cake stall", "label": "CAKE STALL SALES",
   "quote": "I sold green-iced cupcakes all day – I made them with 'Leafy Green' colouring. Only one person bought a whole bottle of it from me, to 'make his own'.",
   "evidence": ev_table("Sam's stall – Saturday", ["Time", "Item", "Buyer"], [
       ("12:15", "Bottle of 'Leafy Green' colouring", "G. Pike"),
       ("13:05", "6 cupcakes", "J. Hart"),
       ("13:50", "Tea and flapjack", "E. Moss"),
     ], mono_cols=(0,))},
  {"name": "Kayla Brown", "role": "Rabbit tent helper", "label": "KAYLA'S NOTE",
   "quote": "I was on my break from half one. When I came back just before two, I saw a man hurrying out of the rabbit tent wiping his hands on a tissue.",
   "evidence": ev_note("FOUND IN THE BIN BY THE RABBIT TENT", [
       "One paper tissue, stained bright green.",
       "Printed on the corner: 'Hollybrook Show – Judge'.",
       "Judges' tissues are only handed out in the judges' pack."],
     "– Kayla")},
  {"name": "Mr Tom Reed", "role": "Show secretary", "label": "JUDGES' PACKS",
   "quote": "Every judge gets a pack with a badge, a pen and a packet of tissues. This year there were only two judges.",
   "evidence": ev_table("Judges' packs handed out", ["Judge", "Event"], [
       ("June Hart", "Cakes"),
       ("Gary Pike", "Cakes"),
     ])},
 ],
 "solution": {"killer": "Gary Pike",
   "motive": "Gary's rabbit Thumper came second to Biscuit last year (clue 2) and he wanted the silver rosette and £50 (clue 1).",
   "proof": ["Biscuit was dyed between 13:30 and 14:00 with 'Leafy Green' colouring (clue 1). Gary bought a whole bottle of it at 12:15 (clue 4).",
             "Gary says he was judging cakes, but June judged alone until 14:10 (clue 3).",
             "A green-stained judge's tissue was found by the rabbit tent (clue 5). Only two judges had them – June and Gary (clue 6) – and June was in the cake tent."],
   "cleared": ["<b>June</b> was judging cakes all the time (clue 3).",
               "<b>Sam</b> was at the stall; <b>Ellie</b> was buying tea at 13:50 (clue 4).",
               "<b>Kayla</b> was on her break, and <b>Tom</b> only handed out the packs."]},
}

# ---------------------------------------------------------------- PANTO (L2)
panto = {
 "slug": "the-pantomime-takings", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 139", "title_html": "THE PANTOMIME<br>TAKINGS", "title_plain": "The Pantomime Takings",
 "teaser": "The panto's box-office cash vanishes during the interval. The dame says he never left the stage – but his costume tells another story.",
 "intro": "At the <b>Little Dorrit Theatre</b>, £3,400 in ticket money disappeared from the box-office safe during the interval of the Saturday matinee of “Cinderella”. " + STD,
 "clues": [
  {"name": "Fiona Crane", "role": "Theatre manager", "label": "MANAGER'S REPORT",
   "quote": "I counted the takings at the start of the interval and locked them in the safe. When I opened it at the end of the show, the cash bag was gone. Only the cast and crew can get backstage.",
   "evidence": ev_rows("Manager's report", [
       ("Interval", "15:10–15:30"),
       ("Counted", "15:12 – £3,400, safe locked"),
       ("Discovered", "16:45 – cash bag missing"),
       ("Safe code", "Known to the manager and the company's two senior actors"),
     ])},
  {"name": "Barry Stokes", "role": "The Dame", "label": "BARRY'S STATEMENT",
   "quote": "I spent the whole interval on stage behind the curtain, getting into my second costume – the giant cupcake dress. Getting that thing on takes twenty minutes and two people.",
   "evidence": ev_rows("Barry Stokes – company file", [
       ("Role", "Dame Trott (senior actor – knows the safe code)"),
       ("Note", "Asked for an advance on his wages twice this month"),
       ("Costume 2", "Cupcake dress – put on in the wings with two dressers"),
     ])},
  {"name": "Lily Okoye", "role": "Dresser", "label": "DRESSER'S LOG",
   "quote": "Barry's cupcake dress? He didn't put it on in the interval. He told us he'd change at the start of act two instead, during the ballroom scene, when he isn't on.",
   "evidence": ev_table("Wardrobe log – Saturday matinee", ["Time", "Actor", "Change"], [
       ("15:12", "Cinderella", "Ballgown, in the wings"),
       ("15:20", "Prince", "Jacket"),
       ("15:41", "Dame Trott", "Cupcake dress (moved from interval)"),
     ], mono_cols=(0,))},
  {"name": "Ravi Sen", "role": "Stage manager", "label": "BACKSTAGE CAMERA",
   "quote": "The camera in the corridor to the office covers the safe door. It's grainy, but you can see enough.",
   "evidence": ev_photos("Corridor camera", [
       ("CAM-2", "15:18", "A figure in a long frilly apron and a huge curly wig walks into the office."),
       ("CAM-2", "15:21", "Same figure leaves, holding something under the apron."),
     ])},
  {"name": "Holly Grant", "role": "Cinderella", "label": "COSTUME LIST",
   "quote": "I was in the wings changing into my ballgown with Lily the whole interval. The Ugly Sisters were out front signing autographs for the children.",
   "evidence": ev_table("Act one costumes", ["Character", "Costume"], [
       ("Dame Trott", "Frilly apron, huge curly orange wig"),
       ("Ugly Sisters", "Pink dresses, tall beehive wigs"),
       ("Buttons", "Red page-boy suit"),
       ("Cinderella", "Rags, then ballgown"),
     ])},
  {"name": "Dan Marsh", "role": "Buttons", "label": "FOYER PHOTO",
   "quote": "I'm the other senior actor, so I know the code too. But I spent the interval in the foyer with the Ugly Sisters – there's a photo on the theatre's page.",
   "evidence": ev_photos("Theatre social media", [
       ("POST", "15:19", "Buttons and the Ugly Sisters signing autographs in the foyer."),
     ])},
 ],
 "solution": {"killer": "Barry Stokes",
   "motive": "Barry was short of money – he had asked for an advance on his wages twice this month (clue 2).",
   "proof": ["The cash was taken from the safe between 15:12 and 16:45 (clue 1); the camera shows the thief entering the office at 15:18 (clue 4). Only the manager, Barry and Dan know the code (clues 1, 2, 6).",
             "Barry says he spent the interval changing into the cupcake dress, but the dresser moved that change to 15:41 at his own request (clue 3).",
             "The figure on camera wears a frilly apron and a huge curly wig (clue 4) – Dame Trott's act-one costume (clue 5)."],
   "cleared": ["<b>Dan</b> knows the code but was photographed in the foyer at 15:19 (clue 6).",
               "<b>Holly</b> was changing in the wings with Lily (clues 3, 5), and the Ugly Sisters wear beehive wigs, not a curly one (clue 5).",
               "<b>Fiona</b> reported the theft, and <b>Ravi</b> supplied the camera footage."]},
}

# ---------------------------------------------------------------- CANAL LOCK (L3)
canal = {
 "slug": "death-at-the-canal-lock", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 140", "title_html": "DEATH AT THE<br>CANAL LOCK", "title_plain": "Death at the Canal Lock",
 "teaser": "A narrowboat owner drowns in a canal lock at dusk. The lock-keeper's log, a boat's water tank and a two-minute gap reveal who closed the gates.",
 "intro": "On the <b>Ashby Canal</b>, retired engineer Victor Hale was found drowned in Burbage Lock after his narrowboat came through on a winter evening. " + STD,
 "clues": [
  {"name": "PC Ruth Ambler", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Hale had a bruise on the back of his head and was found in the lock chamber. His waterproof watch was still running, but the GPS tracker on his boat tells us exactly when it stopped moving.",
   "evidence": ev_rows("Police report – Burbage Lock", [
       ("Found", "17:40, in the lock chamber"),
       ("Injury", "Blow to the back of the head before he went in"),
       ("Boat GPS", "Entered the lock 16:52 · stationary from 16:54"),
       ("Sunset", "16:05 – dark by 16:45"),
     ])},
  {"name": "Colin Hale", "role": "Victim's son", "label": "COLIN'S STATEMENT",
   "quote": "Dad and I argued about money, yes. But I was on my own boat two locks down, filling my water tank, from half four until after six. The water point log will prove it.",
   "evidence": ev_table("Water point, Lock 27 – card log", ["Card", "Start", "Stop", "Litres"], [
       ("Boat 'Kestrel' (C. Hale)", "16:31", "16:38", "160"),
       ("Boat 'Wren'", "17:05", "17:12", "150"),
     ], mono_cols=(1, 2))},
  {"name": "Pat Doyle", "role": "Lock-keeper", "label": "LOCK LOG",
   "quote": "I log every boat through Burbage. Mr Hale's 'Heron' came in at about ten to five. I'd gone home for my tea by then – the lock's self-service after half four.",
   "evidence": ev_table("Burbage Lock – sensor log", ["Time", "Event"], [
       ("16:52", "Top gates opened – 'Heron' enters"),
       ("16:54", "Top gates closed"),
       ("16:58", "Bottom paddles raised – lock emptying (operated from towpath)"),
       ("17:20", "Bottom gates opened – no boat leaves"),
     ], mono_cols=(0,))},
  {"name": "Marina Shaw", "role": "Victim's partner in a boatyard", "label": "BOATYARD ACCOUNTS",
   "quote": "Victor wanted to sell his half of our boatyard to a developer. I'd lose everything. But I was in the boatyard office doing the books until seven – the alarm system shows it.",
   "evidence": ev_rows("Hale & Shaw Boatyard", [
       ("Owners", "V. Hale 50 %, M. Shaw 50 %"),
       ("Victor's plan", "Sell his half to a housing developer"),
       ("Office alarm", "Unset 16:20 by M. Shaw · set 19:05"),
       ("Distance", "Boatyard to Burbage Lock: 3 miles by road"),
     ])},
  {"name": "Ned Foster", "role": "Walker", "label": "TOWPATH PHOTO",
   "quote": "I walked the towpath at about five. There was a man on the lock beam winding the paddles with a windlass – and a boat called Kestrel tied up just below the lock with its lights off.",
   "evidence": ev_photos("Ned's phone", [
       ("IMG_9012", "16:59", "Burbage Lock in the dark: a man in a yellow jacket on the bottom beam, windlass in hand. Below the lock: narrowboat 'Kestrel', unlit."),
     ])},
  {"name": "Gail Price", "role": "Boater on 'Wren'", "label": "WATER TANK GAUGE",
   "quote": "When I got to the water point at five past five, the Kestrel wasn't there – and the tap was still dripping from someone before me. Colin wears a yellow jacket, doesn't he?",
   "evidence": ev_note("KESTREL – POLICE CHECK, 18:30", [
       "Water tank capacity: 400 litres.",
       "Gauge reads: 40 % full.",
       "Owner says tank was 'nearly empty' before filling.",
       "Yellow waterproof jacket in cabin – wet."],
     "– PC Ambler")},
 ],
 "solution": {"killer": "Colin Hale",
   "motive": "Colin and his father had argued about money (clue 2) – Colin stood to inherit Victor's half of the boatyard before it could be sold (clue 4).",
   "proof": ["Victor's boat stopped at 16:54 when the top gates closed, and somebody emptied the lock from the towpath at 16:58 (clues 1, 3).",
             "Colin says he was filling his water tank from half four until after six. But the card log shows he filled for only seven minutes, 16:31–16:38 (clue 2) – 160 litres, which matches a 400-litre tank reading 40 % (clue 6). Gail found no Kestrel there at 17:05 (clue 6).",
             "At 16:59 Ned photographed a man in a yellow jacket on the lock beam and the Kestrel tied up just below Burbage Lock (clue 5). Colin's yellow jacket was wet (clue 6)."],
   "cleared": ["<b>Marina</b> had a motive but was in the boatyard office three miles away from 16:20 to 19:05 (clue 4).",
               "<b>Pat</b> had gone home before Victor arrived (clue 3).",
               "<b>Ned</b> and <b>Gail</b> only passed by (clues 5, 6), and <b>PC Ambler</b> investigated."]},
}

# ---------------------------------------------------------------- COFFEE ROASTERY (L3)
coffee = {
 "slug": "death-at-the-coffee-roastery", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 141", "title_html": "DEATH AT THE<br>COFFEE ROASTERY", "title_plain": "Death at the Coffee Roastery",
 "teaser": "A star coffee roaster collapses at a tasting of her prize-winning blend. Only one cup was poisoned – and only one person knew which cup she'd pick.",
 "intro": "At <b>Bean &amp; Ember</b>, champion roaster Nadia Brook collapsed during a private cupping of her new competition blend and died in hospital. " + STD,
 "clues": [
  {"name": "Dr Simon Reeve", "role": "Toxicologist", "label": "TOXICOLOGY REPORT",
   "quote": "The poison was in one of the six tasting bowls only. It was added after the hot water went in – the heat would have destroyed it otherwise.",
   "evidence": ev_rows("Toxicology report", [
       ("Poison", "Found in bowl 4 only"),
       ("Added", "After the water was poured at 10:05"),
       ("Effect", "Within minutes"),
       ("Bowls 1–3, 5–6", "Clean"),
     ])},
  {"name": "Leo Grant", "role": "Head barista", "label": "CUPPING ORDER",
   "quote": "I poured the water into all six bowls at five past ten, then went to answer the phone. Nadia always tasted the blends in the same order – but she kept the order on a card nobody else saw.",
   "evidence": ev_table("Cupping table, 10:00", ["Bowl", "Blend", "Set out by"], [
       ("1", "House espresso", "L. Grant"),
       ("2", "Kenya AA", "L. Grant"),
       ("3", "Old competition blend", "L. Grant"),
       ("4", "NEW competition blend", "L. Grant"),
       ("5", "Decaf", "L. Grant"),
       ("6", "Brazil", "L. Grant"),
     ])},
  {"name": "Anya Kim", "role": "Business partner", "label": "PHONE RECORDS",
   "quote": "I was upstairs in the office all morning on calls. I didn't go near the cupping room after Leo set it up.",
   "evidence": ev_table("Phones and van – that morning", ["Time", "Record"], [
       ("10:06", "Shop phone: 40-second call from A. Kim's mobile – “fetch the green bean invoices from the van, please”"),
       ("10:07", "Delivery van (yard): back door opened"),
       ("10:12", "Delivery van: back door closed"),
       ("10:13", "Office line: A. Kim calls a supplier"),
     ], mono_cols=(0,))},
  {"name": "Tom Fisher", "role": "Rival roaster", "label": "COMPETITION RULES",
   "quote": "I'd have loved to beat Nadia, but not like that. I was on my own stand at the trade fair across town until noon – check the fair's badge scanner.",
   "evidence": ev_rows("National Roasting Championship", [
       ("Entries", "One blend per roastery"),
       ("Bean & Ember entry", "Nadia's new blend – registered to N. Brook personally"),
       ("If entrant withdraws", "Roastery may enter its previous blend, registered by the co-owner"),
       ("Badge scans", "T. Fisher – trade fair, 09:00–12:00"),
     ])},
  {"name": "Rosie Lane", "role": "Cleaner", "label": "CORRIDOR CAMERA",
   "quote": "I was mopping the corridor. Someone went in and out of the cupping room while Leo was on the phone – I didn't see who, I was facing the other way.",
   "evidence": ev_photos("Corridor camera", [
       ("CAM-1", "10:07", "A person in a black apron with a gold 'B&E' logo enters the cupping room."),
       ("CAM-1", "10:09", "The same person leaves and walks to the stairs up to the office."),
     ])},
  {"name": "Mia Ortiz", "role": "Junior roaster", "label": "STAFF UNIFORMS",
   "quote": "Our aprons are colour-coded. I was in the roasting room the whole time – the roaster logs every batch.",
   "evidence": ev_table("Bean & Ember – aprons", ["Colour", "Worn by"], [
       ("Black with gold logo", "Owners only – N. Brook, A. Kim"),
       ("Brown", "Baristas – L. Grant"),
       ("Green", "Roasters – M. Ortiz"),
       ("Grey", "Cleaning staff"),
     ])},
 ],
 "solution": {"killer": "Anya Kim",
   "motive": "With Nadia gone, the roastery could enter the old blend, registered by the co-owner – Anya would be the champion entrant (clue 4).",
   "proof": ["Bowl 4 – Nadia's new blend – was poisoned after 10:05 (clues 1, 2). At 10:06 Anya phoned Leo and sent him out to the van, where he stayed from 10:07 to 10:12 (clue 3) – leaving the cupping room empty.",
             "At 10:07 a person in a black apron with the gold logo entered the cupping room and at 10:09 went back up to the office (clue 5). Only the two owners wear that apron (clue 6), and the other owner, Nadia, was the victim.",
             "Anya said she never went near the cupping room."],
   "cleared": ["<b>Leo</b> was out at the van 10:07–10:12 (clue 3) and wears a brown apron (clue 6).",
               "<b>Tom</b> was at the trade fair across town (clue 4).",
               "<b>Mia</b> wears green and was roasting; <b>Rosie</b> wears grey (clue 6)."]},
}

MYSTERIES = [petshow, panto, canal, coffee]
