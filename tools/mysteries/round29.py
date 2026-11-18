from lib import *  # evidence helpers

# Round 29 (18 Nov): winter round – 1 Rookie, 1 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- SNOWMAN (L1)
snowman = {
 "slug": "the-snowman-contest-sabotage", "level": 1, "crime": "SABOTAGE", "who": "saboteur", "added": ADDED,
 "caseno": "CASE NO. 178", "title_html": "THE SNOWMAN<br>CONTEST SABOTAGE", "title_plain": "The Snowman Contest Sabotage",
 "teaser": "The favourite snowman in the village contest is knocked flat the night before judging. Boot prints in fresh snow show who did it.",
 "intro": "In the village of <b>Elmbury</b>, the Hill family's giant snowman was the favourite to win the winter snowman contest. On the morning of judging it lay smashed on the green. " + STD,
 "clues": [
  {"name": "Mrs Jenny Hill", "role": "Snowman builder", "label": "JENNY'S REPORT",
   "quote": "Our snowman was perfect at ten last night. At seven this morning it was smashed – and there were fresh boot prints all round it.",
   "evidence": ev_rows("Jenny's report", [
       ("Snowman fine", "22:00"),
       ("Found smashed", "07:00"),
       ("Snow", "Fresh snow fell until midnight, then stopped"),
       ("Boot prints", "One set, size 9, with a star pattern on the sole – on top of the fresh snow"),
     ])},
  {"name": "Mr Colin Barr", "role": "Rival snowman builder", "label": "COLIN'S STATEMENT",
   "quote": "I went to bed at half past nine and didn't go out again. Why would I knock over their snowman? Mine is just as good.",
   "evidence": ev_table("Snowman contest – last year's results", ["Place", "Builder"], [
       ("1st", "The Hill family"),
       ("2nd", "Colin Barr"),
       ("3rd", "The Patel twins"),
     ], note="Colin has come second three years in a row.")},
  {"name": "Mrs Gwen Ash", "role": "Neighbour", "label": "GWEN'S NOTE",
   "quote": "My dog woke me at about one in the morning. I looked out and saw someone in a bobble hat walking back from the green to Colin's house.",
   "evidence": ev_note("GWEN'S NOTE", [
       "About 01:00 – person in a red bobble",
       "hat walking from the green into",
       "Colin Barr's front gate. Carrying",
       "a shovel?"],
     "– Gwen")},
  {"name": "Sam Hill", "role": "Jenny's son, aged 10", "label": "BOOT PHOTO",
   "quote": "I followed the boot prints in the snow like a real detective. They went straight to a front door – and the boots were sitting on the step!",
   "evidence": ev_photos("Sam's tablet", [
       ("IMG_0451", "07:20", "Boot prints leading from the green to No. 4 – Colin Barr's house."),
       ("IMG_0452", "07:21", "A pair of wet size-9 boots with a star-pattern sole on Colin's step, next to a snowy shovel."),
     ])},
  {"name": "Mr Raj Patel", "role": "Contest judge", "label": "JUDGE'S LIST",
   "quote": "I have the list of entries. The Patel twins are my nieces, so I let another judge score theirs.",
   "evidence": ev_table("Contest entries", ["Entry", "Builder", "Address"], [
       ("Snow King", "The Hill family", "No. 2"),
       ("Frosty Fred", "Colin Barr", "No. 4"),
       ("Twin Towers", "The Patel twins", "No. 9"),
     ])},
  {"name": "Miss Lily Patel", "role": "Contest entrant", "label": "LILY'S STATEMENT",
   "quote": "My sister and I were at our gran's in the next town all night. We only got back at nine this morning.",
   "evidence": ev_rows("Bus ticket", [
       ("Route", "Hollin Cross → Elmbury"),
       ("Date", "Contest morning"),
       ("Time", "08:35"),
       ("Passengers", "2 children"),
     ])},
 ],
 "solution": {"killer": "Mr Colin Barr",
   "motive": "Colin always comes second behind the Hill family (clue 2).",
   "proof": ["The prints were made after midnight, on top of the fresh snow (clue 1).",
             "Colin says he never went out after 21:30, but at about 01:00 Gwen saw someone walk from the green into his gate with a shovel (clue 3).",
             "The prints lead to No. 4, Colin's house (clue 5), where Sam found wet size-9 star-sole boots and a snowy shovel (clue 4)."],
   "cleared": ["<b>Lily</b> and her sister were away and only came back by bus at 08:35 (clue 6).",
               "<b>Jenny</b> and <b>Sam</b> built the snowman, and <b>Raj</b> and <b>Gwen</b> only report what they know."]},
}

# ---------------------------------------------------------------- ADVENT CALENDAR (L2)
advent = {
 "slug": "the-advent-calendar-thief", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 179", "title_html": "THE ADVENT<br>CALENDAR THIEF", "title_plain": "The Advent Calendar Thief",
 "teaser": "Someone is stealing the gold coins from a jeweller's luxury advent calendar, one door at a time. A shop camera with a wrong clock points to the thief.",
 "intro": "At <b>Marlow &amp; Finch Jewellers</b>, the shop window holds a giant advent calendar with a real gold coin behind each door. Each morning a new door is found already open – and empty. " + STD,
 "clues": [
  {"name": "Mr Owen Finch", "role": "Jeweller", "label": "STOCK LOG",
   "quote": "Every morning when I open up, another coin is gone. The calendar is behind the counter glass – you need a key for the window cabinet.",
   "evidence": ev_table("Advent coins – stock log", ["Morning", "Door", "Coin"], [
       ("2 Dec", "2", "Missing"),
       ("3 Dec", "3", "Missing"),
       ("4 Dec", "4", "Missing"),
     ], note="Doors are opened and the coins taken between 17:30 closing and 09:00 opening.")},
  {"name": "Tess Marlow", "role": "Shop assistant", "label": "KEY LIST",
   "quote": "Only three people have a key to the window cabinet: Mr Finch, me and the cleaner, Dora. I always hand mine back at closing.",
   "evidence": ev_table("Window cabinet keys", ["Holder", "Key kept"], [
       ("O. Finch", "On his key ring, at all times"),
       ("T. Marlow", "In the shop safe after closing (signed in)"),
       ("D. Cole", "Takes it home – cleans 18:00–19:00"),
     ])},
  {"name": "Dora Cole", "role": "Cleaner", "label": "DORA'S STATEMENT",
   "quote": "I clean from six to seven every evening and I never touch the calendar. The camera will show I left at seven on the dot.",
   "evidence": ev_rows("Pawn shop receipt – Barker's Pawnbrokers", [
       ("Date", "4 Dec"),
       ("Item", "3 small gold coins, star stamp"),
       ("Seller", "D. Cole"),
       ("Paid", "£540"),
     ])},
  {"name": "Ben Quinn", "role": "Security engineer", "label": "CAMERA NOTE",
   "quote": "I checked the shop camera. Its clock was never changed for winter time – it runs one hour ahead of the real time.",
   "evidence": ev_table("Shop camera – 3 Dec (camera clock)", ["Camera time", "Event"], [
       ("19:02", "Cleaner arrives, starts mopping"),
       ("19:41", "Cleaner opens window cabinet with key, reaches into calendar"),
       ("20:05", "Cleaner leaves by back door"),
     ], note="Camera clock is 1 hour fast.")},
  {"name": "Rita Shah", "role": "Pawnbroker", "label": "RITA'S NOTE",
   "quote": "A woman sold me three small gold coins with a star stamp. I keep a copy of every seller's ID.",
   "evidence": ev_note("BARKER'S – SELLER NOTE", [
       "4 Dec, 12:10 – three 1g gold coins,",
       "star stamp. Seller showed library",
       "card: Dora Cole. Said they were",
       "'from my nan'."],
     "– Rita")},
  {"name": "Marcus Finch", "role": "Owen's nephew", "label": "MARCUS'S STATEMENT",
   "quote": "Uncle Owen thinks it's me because I borrowed money once. But I've been in Edinburgh since the first of December.",
   "evidence": ev_rows("Train booking", [
       ("Passenger", "Marcus Finch"),
       ("Out", "1 Dec, London → Edinburgh"),
       ("Return", "10 Dec"),
     ])},
 ],
 "solution": {"killer": "Dora Cole",
   "motive": "Dora sold the coins to a pawnbroker for £540 (clues 3, 5).",
   "proof": ["The coins vanish between closing and opening, and you need a cabinet key (clues 1, 2). Dora is the only key holder who takes her key home (clue 2).",
             "Dora says the camera shows her leaving at 19:00 and never touching the calendar. But the camera runs one hour fast: she really arrived at 18:02, opened the cabinet at 18:41 and left at 19:05 (clue 4).",
             "The next day she sold three star-stamped gold coins at Barker's (clues 3, 5)."],
   "cleared": ["<b>Tess</b>'s key is locked in the safe overnight, and <b>Owen</b> owns the coins (clue 2).",
               "<b>Marcus</b> was in Edinburgh, and <b>Ben</b> and <b>Rita</b> only report what they found (clues 4, 5, 6)."]},
}

# ---------------------------------------------------------------- TRAM DEPOT (L3)
tram = {
 "slug": "death-at-the-tram-depot", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 180", "title_html": "DEATH AT THE<br>TRAM DEPOT", "title_plain": "Death at the Tram Depot",
 "teaser": "A depot manager is found dead in the inspection pit on a snowy night. Tram running times, a radio log and a missing glove reveal the killer.",
 "intro": "At the <b>Northgate Tram Depot</b>, night manager Frank Doyle was found dead in the inspection pit under tram 14. He had been struck on the head with a heavy spanner. " + STD,
 "clues": [
  {"name": "DS Amy Ward", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Doyle's smashed watch stopped at 23:18. A leather driver's glove was found under his body – the left one, size L.",
   "evidence": ev_rows("Police report – Northgate Depot", [
       ("Found", "00:05, inspection pit, tram 14"),
       ("Watch", "Stopped at 23:18"),
       ("Weapon", "Heavy spanner from the pit tool rack"),
       ("Under the body", "Left driver's glove, size L, initials scratched off"),
     ])},
  {"name": "Gary Price", "role": "Tram driver, route 3", "label": "GARY'S STATEMENT",
   "quote": "I was out on route 3 until midnight. You can't stop a tram in the middle of a route – the radio log will show I was driving.",
   "evidence": ev_rows("Frank Doyle's desk diary", [
       ("Last week", "Gary Price failed a breath test before his shift – sent home"),
       ("Frank's note", "“Report Gary to head office tomorrow. He'll lose his licence.”"),
     ])},
  {"name": "Nell Hughes", "role": "Radio controller", "label": "RADIO LOG",
   "quote": "Every tram radios in at the end of each loop. Route 3 is a 40-minute loop that starts and ends at the depot gate.",
   "evidence": ev_table("Radio log – route 3, tram 9 (G. Price)", ["Time", "Message"], [
       ("22:30", "Leaving depot gate, loop 1"),
       ("23:10", "Back at depot gate – snow on track, short stop"),
       ("23:25", "Leaving depot gate, loop 2"),
       ("00:05", "Back at depot gate"),
     ], mono_cols=(0,))},
  {"name": "Dev Malik", "role": "Track cleaner", "label": "DEV'S NOTE",
   "quote": "I was gritting the gate points in the snow. Around quarter past eleven a driver jumped off tram 9 and ran into the shed. He came back ten minutes later with only one glove on.",
   "evidence": ev_note("DEV'S GRITTING SHEET", [
       "23:12 – driver off tram 9, into shed",
       "23:24 – back, running. Only ONE",
       "glove (right). Pulled out at 23:25.",
       "Gate points gritted 23:00–23:40."],
     "– Dev")},
  {"name": "Rosa Grant", "role": "Uniform store", "label": "GLOVE ISSUE",
   "quote": "Every driver gets one pair of leather gloves in their size. Here's the list.",
   "evidence": ev_table("Driver gloves issued", ["Driver", "Size"], [
       ("G. Price", "L"),
       ("T. Byrne", "M"),
       ("N. Hughes", "S"),
     ])},
  {"name": "Tom Byrne", "role": "Tram driver, route 5", "label": "TOM'S STATEMENT",
   "quote": "Frank and I argued about the overtime rota, it's true. But I was on route 5 across town all evening.",
   "evidence": ev_table("Radio log – route 5, tram 11 (T. Byrne)", ["Time", "Message"], [
       ("22:45", "Docks terminus"),
       ("23:15", "City Square"),
       ("23:45", "Docks terminus"),
     ], mono_cols=(0,))},
 ],
 "solution": {"killer": "Gary Price",
   "motive": "Frank was going to report Gary for failing a breath test, and Gary would lose his licence (clue 2).",
   "proof": ["Frank died at 23:18, and a size-L left driver's glove was under his body (clue 1).",
             "Gary says he was driving the whole time, but his tram stopped at the depot gate from 23:10 to 23:25 (clue 3).",
             "Dev saw a driver jump off tram 9 at 23:12 and return at 23:24 with only his right glove (clue 4). Gary drives tram 9 and wears size L (clues 3, 5)."],
   "cleared": ["<b>Tom</b> was at City Square at 23:15 and wears size M (clues 5, 6).",
               "<b>Nell</b> was on the radio and wears size S; <b>Dev</b> was gritting outside, and <b>Rosa</b> runs the store (clues 3, 4, 5)."]},
}

# ---------------------------------------------------------------- FROST FAIR (L3)
frost = {
 "slug": "murder-at-the-frost-fair", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 181", "title_html": "MURDER AT THE<br>FROST FAIR", "title_plain": "Murder at the Frost Fair",
 "teaser": "The organiser of a winter frost fair is found dead behind the mulled wine stall. Fireworks timing, a card machine and a glove print point to the killer.",
 "intro": "At the <b>Riverside Frost Fair</b>, organiser Hugh Mercer was found dead behind the mulled wine stall during the fireworks. He had been pushed and hit his head on the iron brazier. " + STD,
 "clues": [
  {"name": "DI Kate Marsh", "role": "Police", "label": "POLICE REPORT",
   "quote": "Witnesses heard a scream behind the stalls just as the first firework went up. The fireworks started exactly at 20:00.",
   "evidence": ev_rows("Police report – Riverside Frost Fair", [
       ("Found", "20:20, behind the mulled wine stall"),
       ("Scream heard", "As the first firework went up – 20:00"),
       ("Cause", "Pushed – head struck the iron brazier"),
       ("On his coat", "Cinnamon-red mulled wine stain, still wet"),
     ])},
  {"name": "Jill Rowe", "role": "Mulled wine stall holder", "label": "JILL'S STATEMENT",
   "quote": "I was serving at the front of my stall the whole time. The card machine proves it – I was taking payments all through the fireworks.",
   "evidence": ev_rows("Fair committee letter to J. Rowe", [
       ("Subject", "Your stall licence"),
       ("Text", "“After the hygiene complaints, H. Mercer will not renew your pitch next year.”"),
       ("Date", "Sent the morning of the fair"),
     ])},
  {"name": "Paul Rowe", "role": "Jill's husband", "label": "CARD MACHINE",
   "quote": "I helped Jill on the stall. We have two card readers – one on the counter and a spare one on my belt.",
   "evidence": ev_table("Card payments – mulled wine stall", ["Time", "Reader", "Taken by"], [
       ("19:52", "Counter", "J. Rowe"),
       ("19:57", "Spare (belt)", "P. Rowe"),
       ("20:03", "Spare (belt)", "P. Rowe"),
       ("20:06", "Counter", "J. Rowe"),
     ], note="The counter reader logs the staff code of whoever uses it. No counter payments between 19:52 and 20:06.")},
  {"name": "Eddie Lamb", "role": "Fireworks technician", "label": "FIREWORKS LOG",
   "quote": "I set off the first firework at eight on the dot from the barge. From there I could see the back of the stalls lit up by the brazier.",
   "evidence": ev_note("EDDIE'S FIRING SHEET", [
       "20:00:00 – first rocket fired.",
       "Lit by flash: woman in a stall apron",
       "behind mulled wine stall, arguing",
       "with a man in a top hat."],
     "– Eddie")},
  {"name": "Clara Mercer", "role": "Hugh's daughter", "label": "CLARA'S STATEMENT",
   "quote": "Dad always wore his top hat at the fair. I was with my friends at the ice rink watching the fireworks when it happened.",
   "evidence": ev_photos("Clara's phone", [
       ("IMG_9920", "20:00", "Clara and three friends on the ice rink, fireworks overhead – rink clock reads 20:00."),
     ])},
  {"name": "Simon Fry", "role": "Chestnut seller", "label": "SIMON'S NOTE",
   "quote": "Jill's stall is next to mine. Just before the fireworks she left the counter, went round the back, and came back a few minutes later with her apron soaked in mulled wine.",
   "evidence": ev_rows("Simon's statement", [
       ("19:55", "Jill goes round the back of her stall – Paul serves alone"),
       ("20:04", "Jill back at the counter, apron soaked red, out of breath"),
       ("Simon's stall", "Sold chestnuts the whole time – queue of ten people"),
     ])},
 ],
 "solution": {"killer": "Jill Rowe",
   "motive": "Hugh was not going to renew Jill's stall licence (clue 2).",
   "proof": ["Hugh was pushed at 20:00, and wet mulled wine was on his coat (clue 1).",
             "Jill says the card machine proves she was serving. But the counter reader took no payments from 19:52 to 20:06 – only Paul's spare reader was used (clue 3).",
             "At 20:00 Eddie saw a woman in a stall apron arguing with Hugh behind the mulled wine stall (clues 4, 5). Simon saw Jill go round the back at 19:55 and come back at 20:04 with her apron soaked (clue 6)."],
   "cleared": ["<b>Paul</b> was taking payments on his reader at 19:57 and 20:03 (clue 3), and <b>Clara</b> was on the ice rink at 20:00 (clue 5).",
               "<b>Eddie</b> was firing rockets from the barge, and <b>Simon</b> was serving a queue (clues 4, 6)."]},
}

MYSTERIES = [snowman, advent, tram, frost]
