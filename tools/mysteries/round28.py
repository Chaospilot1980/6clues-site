from lib import *  # evidence helpers

# Round 28 (18 Nov): Christmas round – 1 Rookie, 1 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- NATIVITY STAR (L1)
nativity = {
 "slug": "the-nativity-play-star", "level": 1, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 174", "title_html": "THE NATIVITY<br>PLAY STAR", "title_plain": "The Nativity Play Star",
 "teaser": "The glittering star for the Christmas nativity play vanishes an hour before the show. A trail of gold glitter leads straight to the culprit.",
 "intro": "At <b>St Mary's Primary</b>, the big golden star that hangs over the stable in the Christmas nativity play disappeared from the school hall just before the show. " + STD,
 "clues": [
  {"name": "Mrs Helen Archer", "role": "Play director", "label": "HALL REPORT",
   "quote": "The star was on the stage at five. At quarter to six, when I came back with the costumes, it was gone – and there was gold glitter all over the floor.",
   "evidence": ev_rows("Hall report", [
       ("Star on stage", "17:00"),
       ("Gone", "17:45"),
       ("Clue", "Trail of gold glitter from the stage to the side door"),
       ("Show", "18:30"),
     ])},
  {"name": "Mr Dave Penn", "role": "Parent volunteer", "label": "DAVE'S STATEMENT",
   "quote": "I was in the car park the whole time helping parents park. I never went into the hall before six.",
   "evidence": ev_rows("Christmas fair committee notes", [
       ("Dave's idea", "Use the play's star on the top of the village Christmas tree instead"),
       ("Committee", "Voted no – the star stays with the school play"),
       ("Dave", "“We'll see about that.”"),
     ])},
  {"name": "Miss Ruby Fox", "role": "Car park helper", "label": "CAR PARK ROTA",
   "quote": "I did the car park on my own from five until half past. Dave was meant to help but he didn't turn up until twenty to six.",
   "evidence": ev_table("Car park rota", ["Time", "Planned", "Actually there"], [
       ("17:00–17:30", "R. Fox, D. Penn", "R. Fox only"),
       ("17:30–18:30", "R. Fox, D. Penn", "R. Fox; D. Penn from 17:40"),
     ], mono_cols=(0,))},
  {"name": "Mr Joe Clarke", "role": "Caretaker", "label": "VAN NOTE",
   "quote": "At about quarter past five I saw a man carrying something big and sparkly to a white van by the side door. Gold glitter everywhere.",
   "evidence": ev_note("CARETAKER'S NOTE", [
       "17:15 – man carrying a big gold",
       "star out of the side door into a",
       "white van, sign: 'PENN PLUMBING'.",
       "Glitter all over his jumper."],
     "– Joe")},
  {"name": "Mrs Asha Rao", "role": "Head teacher", "label": "TREE PHOTO",
   "quote": "The next morning, the star turned up – on top of the village Christmas tree on the green!",
   "evidence": ev_photos("Mrs Rao's phone", [
       ("IMG_7001", "Sat 08:10", "The village Christmas tree with the school's golden star on top. A ladder marked 'PENN PLUMBING' leans against it."),
     ])},
  {"name": "Mr Tom Lee", "role": "Lighting volunteer", "label": "LIGHTING LOG",
   "quote": "I was up the ladder in the hall rigging the stage lights from half four until six. Nobody touched the star while I was looking – but I had my back to it a lot.",
   "evidence": ev_table("Lighting rig – sign-off", ["Time", "Job", "By"], [
       ("16:30", "Stage lights rigged", "T. Lee"),
       ("17:10", "Spotlight on stable", "T. Lee"),
       ("17:50", "Final check", "T. Lee"),
     ], mono_cols=(0,))},
 ],
 "solution": {"killer": "Mr Dave Penn",
   "motive": "Dave wanted the star for the village Christmas tree, and the committee said no (clue 2).",
   "proof": ["The star went between 17:00 and 17:45, leaving a trail of gold glitter to the side door (clue 1).",
             "Dave says he was in the car park the whole time, but he only arrived there at 17:40 (clue 3).",
             "At 17:15 the caretaker saw a man carry the star to a 'Penn Plumbing' van (clue 4), and the next morning it was on the village tree with a Penn Plumbing ladder beside it (clue 5)."],
   "cleared": ["<b>Ruby</b> was in the car park from 17:00 (clue 3), and <b>Tom</b> was up his ladder rigging lights (clue 6).",
               "<b>Mrs Archer</b> was fetching costumes, and <b>Mr Clarke</b> and <b>Mrs Rao</b> only report what they saw."]},
}

# ---------------------------------------------------------------- HAMPER SWINDLE (L2)
hamper = {
 "slug": "the-christmas-hamper-swindle", "level": 2, "crime": "FRAUD", "who": "fraudster", "added": ADDED,
 "caseno": "CASE NO. 175", "title_html": "THE CHRISTMAS<br>HAMPER SWINDLE", "title_plain": "The Christmas Hamper Swindle",
 "teaser": "Fifty families paid for luxury Christmas hampers that never arrived. The money went somewhere – and a delivery van that never moved tells the story.",
 "intro": "In the town of <b>Holbrook</b>, fifty families paid £60 each into a community Christmas hamper scheme. On Christmas Eve, not one hamper arrived – and the £3,000 was gone. " + STD,
 "clues": [
  {"name": "Joan Webb", "role": "Scheme customer", "label": "COMPLAINT",
   "quote": "I paid my £60 in November like everyone else. The leaflet promised delivery on the twenty-third. Nothing came.",
   "evidence": ev_rows("Hamper scheme leaflet", [
       ("Price", "£60 – champagne, cheeses, Christmas pudding"),
       ("Pay to", "Holbrook Hampers – bank account ending 4417"),
       ("Delivery", "23 December, by the scheme's own van"),
       ("Organised by", "The Holbrook Traders' Club"),
     ])},
  {"name": "Rob Hale", "role": "Scheme treasurer", "label": "ROB'S STATEMENT",
   "quote": "The supplier let us down at the last minute. I paid him the full £3,000 on the first of December – I've got nothing to hide.",
   "evidence": ev_rows("Bank statement – account ending 4417", [
       ("Paid in", "£3,000 from 50 families"),
       ("1 Dec", "£3,000 transfer to 'Northern Gourmet Ltd'"),
       ("Account holder", "R. Hale, as treasurer"),
     ])},
  {"name": "Kay Moss", "role": "Traders' Club chair", "label": "COMPANY CHECK",
   "quote": "I'd never heard of 'Northern Gourmet', so I looked it up on the company register.",
   "evidence": ev_rows("Companies register – Northern Gourmet Ltd", [
       ("Registered", "28 November – three days before the payment"),
       ("Director", "Robert Hale"),
       ("Business", "None recorded – no food, no premises"),
     ])},
  {"name": "Sid Grant", "role": "Van driver", "label": "VAN MILEAGE",
   "quote": "I was hired to drive the hamper van. I turned up on the twenty-third ready to go and there was nothing to load. Rob said 'wait for a call' – it never came.",
   "evidence": ev_table("Hamper van – mileage log", ["Date", "Miles", "Note"], [
       ("20 Dec", "40,112", "Van hired"),
       ("23 Dec", "40,112", "No collection – van never left the yard"),
       ("24 Dec", "40,112", "Returned"),
     ])},
  {"name": "Priya Nair", "role": "Delicatessen owner", "label": "SUPPLIER QUOTE",
   "quote": "Rob asked me for a quote in October – fifty hampers for £2,400. He never placed the order. I never heard from any 'Northern Gourmet'.",
   "evidence": ev_note("EMAIL FROM PRIYA'S DELI", [
       "To R. Hale, 15 Oct:",
       "50 luxury hampers – £2,400 total.",
       "Order by 1 Dec for delivery 22 Dec.",
       "[No reply received]"],
     "– Priya's Deli")},
  {"name": "Mike Foley", "role": "Car dealer", "label": "SALES RECEIPT",
   "quote": "Rob bought a second-hand motorbike from me on the second of December. Paid in cash – nearly three grand.",
   "evidence": ev_table("Foley Motors – December sales", ["Date", "Vehicle", "Buyer", "Paid"], [
       ("2 Dec", "Motorbike, 2018", "R. Hale", "£2,950 cash"),
       ("9 Dec", "Hatchback, 2015", "K. Moss", "£4,200 card"),
     ])},
 ],
 "solution": {"killer": "Rob Hale",
   "motive": "Rob wanted the money – he spent nearly £3,000 cash on a motorbike the day after taking it (clue 6).",
   "proof": ["The £3,000 went from the scheme account to 'Northern Gourmet Ltd' on 1 December (clue 2).",
             "Rob says he paid the supplier, but 'Northern Gourmet' was set up three days earlier, has no business – and Rob is its director (clue 3). The real supplier quote was never ordered (clue 5).",
             "No hampers were ever collected – the van never moved (clue 4), and the next day Rob paid £2,950 cash for a motorbike (clue 6)."],
   "cleared": ["<b>Kay</b> exposed the fake company and paid for her car by card (clues 3, 6).",
               "<b>Sid</b> waited with an empty van, <b>Priya</b> was never paid, and <b>Joan</b> is one of the families cheated (clues 1, 4, 5)."]},
}

# ---------------------------------------------------------------- CAROL CONCERT (L3)
carol = {
 "slug": "death-at-the-carol-concert", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 176", "title_html": "DEATH AT THE<br>CAROL CONCERT", "title_plain": "Death at the Carol Concert",
 "teaser": "The choirmaster dies in the vestry during a candlelit carol concert. The order of service, a dropped candle and a solo that was never sung reveal the killer.",
 "intro": "At <b>St Barnabas' Church</b>, choirmaster Lionel Ashe was found dead in the vestry during the Christmas carol concert, struck with a heavy brass candlestick. " + STD,
 "clues": [
  {"name": "DS Martin Cole", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Ashe was struck in the vestry. A candle he was holding fell and burned a mark on the floor – the verger saw it still smoking at 19:47, and it burns at a known rate.",
   "evidence": ev_rows("Police report – St Barnabas'", [
       ("Found", "19:55, vestry"),
       ("Weapon", "Brass altar candlestick"),
       ("Dropped candle", "Burned 1.5 cm on the floor – about 15 minutes"),
       ("So he fell at", "About 19:32"),
     ])},
  {"name": "Celia Grant", "role": "Soprano soloist", "label": "CELIA'S STATEMENT",
   "quote": "I was in the choir stalls the whole concert. I sang the solo in 'Once in Royal David's City' at half past seven – the whole church heard me.",
   "evidence": ev_rows("Choir notes – Lionel Ashe", [
       ("Next year", "Celia Grant to be replaced as lead soprano"),
       ("Lionel's note", "“Tell Celia after the concert. She will not take it well.”"),
     ])},
  {"name": "Rev. Gareth Price", "role": "Vicar", "label": "ORDER OF SERVICE",
   "quote": "The order of service was printed weeks ago – but on the night, Lionel changed it. He was furious with someone.",
   "evidence": ev_programme("Carol concert – order of service (as performed)", "St Barnabas', 22 December", [
       ("19:00", "Once in Royal David's City – solo by C. Grant"),
       ("19:15", "First reading"),
       ("19:25", "Silent Night – full choir (solo dropped)"),
       ("19:40", "Second reading"),
     ], None)},
  {"name": "Alfie Shaw", "role": "Organist", "label": "ORGAN LOFT NOTE",
   "quote": "From the organ loft I can see the whole church. During the first reading, one of the sopranos slipped out of the stalls towards the vestry.",
   "evidence": ev_note("ALFIE'S NOTES ON HIS MUSIC", [
       "19:28 – soprano in a red robe and",
       "the gold soloist's sash leaves stalls",
       "towards vestry. 19:36 – back, out of",
       "breath, wax on her sleeve."],
     "– Alfie")},
  {"name": "Mrs Nora Lee", "role": "Choir wardrobe mistress", "label": "ROBE LIST",
   "quote": "Every chorister wears a red robe. Only the soloist wears the gold sash – and only one sash exists.",
   "evidence": ev_table("Choir robes – concert night", ["Singer", "Robe", "Sash"], [
       ("C. Grant", "Red", "Gold soloist's sash"),
       ("M. Dyer", "Red", "None"),
       ("Other sopranos", "Red", "None"),
     ])},
  {"name": "Mark Dyer", "role": "Tenor", "label": "VERGER'S NOTE",
   "quote": "I'm a tenor – I never left my seat. The verger told me he saw the candle still smoking when he looked in at quarter to eight, but thought Lionel had just stepped out.",
   "evidence": ev_rows("Verger's statement (given to M. Dyer)", [
       ("19:47", "Looked into vestry – candle smoking on the floor, nobody visible"),
       ("19:55", "Went back – found Mr Ashe behind the vestment cupboard"),
     ])},
 ],
 "solution": {"killer": "Celia Grant",
   "motive": "Lionel was about to replace Celia as lead soprano (clue 2).",
   "proof": ["Lionel fell at about 19:32, when his dropped candle started burning the floor (clue 1).",
             "Celia says she was in the stalls the whole time and sang at half past seven. But her solo was at 19:00 – and at 19:25 Lionel dropped her solo from 'Silent Night' (clue 3).",
             "At 19:28 a soprano in the gold soloist's sash went towards the vestry and came back at 19:36 with wax on her sleeve (clue 4). Only Celia wears that sash (clue 5)."],
   "cleared": ["<b>Mark</b> is a tenor without a sash and stayed in his seat; the other sopranos wear no sash (clues 5, 6).",
               "<b>Alfie</b> was playing in the organ loft, <b>Rev. Price</b> led the service, and <b>Mrs Lee</b> kept the robes (clues 3, 4, 5)."]},
}

# ---------------------------------------------------------------- MINCE PIE FACTORY (L3)
mince = {
 "slug": "murder-at-the-mince-pie-factory", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 177", "title_html": "MURDER AT THE<br>MINCE PIE FACTORY", "title_plain": "Murder at the Mince Pie Factory",
 "teaser": "The factory owner is found dead in the cold store on the busiest night before Christmas. A line counter, an oven log and floury boot prints catch the killer.",
 "intro": "At <b>Hartley's Bakery</b>, which makes two million mince pies every December, owner George Hartley was found dead in the walk-in cold store during the night shift. " + STD,
 "clues": [
  {"name": "DI Lena Brooks", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Hartley was struck with a rolling pin and locked in the cold store. The store's door sensor shows exactly when it was opened and shut.",
   "evidence": ev_rows("Police report – Hartley's Bakery", [
       ("Found", "03:40, cold store"),
       ("Cold store door", "Opened 02:14 · closed and bolted from outside 02:19"),
       ("Weapon", "A large wooden rolling pin from Line 2"),
       ("On the floor", "Floury boot prints, size 10"),
     ])},
  {"name": "Steve Rourke", "role": "Night-shift supervisor, Line 2", "label": "STEVE'S STATEMENT",
   "quote": "I was on Line 2 the whole shift. If I'd left, the line would have stopped – and it didn't stop once. Check the counter.",
   "evidence": ev_rows("George Hartley's notes", [
       ("Found", "Steve Rourke selling bakery stock to a cash-and-carry"),
       ("Value", "About £20,000 since September"),
       ("Plan", "“Sack Steve tonight, police in the morning.”"),
     ])},
  {"name": "Bina Patel", "role": "Line 2 operator", "label": "LINE 2 COUNTER",
   "quote": "The line can run on its own for a few minutes if somebody fills the hopper first. Steve filled it right up at two – I thought it was odd.",
   "evidence": ev_table("Line 2 – pie counter", ["Time", "Pies per minute", "Note"], [
       ("02:00", "1,200", "Hopper filled – 'full' sensor"),
       ("02:10", "1,200", "Supervisor badge logged out of Line 2 panel"),
       ("02:22", "1,180", "Supervisor badge logged back in"),
     ], mono_cols=(0,))},
  {"name": "Kev Holt", "role": "Oven operator", "label": "OVEN LOG",
   "quote": "I was at the ovens all night – they need watching every minute. I saw Steve walk past towards the cold store about ten past two, wiping his hands.",
   "evidence": ev_table("Oven log – night shift", ["Time", "Temperature check", "By"], [
       ("02:05", "200 °C", "K. Holt"),
       ("02:15", "201 °C", "K. Holt"),
       ("02:25", "199 °C", "K. Holt"),
     ], mono_cols=(0,))},
  {"name": "Mags Ellis", "role": "Hygiene manager", "label": "BOOT LIST",
   "quote": "Every worker gets white safety boots in their own size. I've got the list.",
   "evidence": ev_table("Safety boots issued", ["Worker", "Size"], [
       ("S. Rourke", "10"),
       ("K. Holt", "8"),
       ("B. Patel", "5"),
       ("M. Ellis", "6"),
     ])},
  {"name": "Joe Hartley", "role": "George's son", "label": "GATE LOG",
   "quote": "Dad and I argued about the business, but I wasn't even there – I left at ten and got home by half past.",
   "evidence": ev_table("Factory gate – night", ["Time", "Badge", "Event"], [
       ("22:02", "J. Hartley", "Out"),
       ("03:45", "Police", "In"),
     ], mono_cols=(0,))},
 ],
 "solution": {"killer": "Steve Rourke",
   "motive": "George had found Steve selling £20,000 of stock and was going to sack him that night and call the police (clue 2).",
   "proof": ["George was struck and bolted in the cold store between 02:14 and 02:19, leaving size-10 floury boot prints (clue 1).",
             "Steve says Line 2 never stopped, so he couldn't have left. But he filled the hopper at 02:00 so it would run on its own, and his badge was logged out of the Line 2 panel from 02:10 to 02:22 (clue 3).",
             "Kev saw Steve walk towards the cold store at about 02:10 (clue 4), and Steve's safety boots are size 10 (clue 5)."],
   "cleared": ["<b>Kev</b> was checking the ovens at 02:15 and wears size 8 (clues 4, 5); <b>Bina</b> and <b>Mags</b> wear sizes 5 and 6 (clue 5).",
               "<b>Joe</b> left the factory at 22:02 and didn't return (clue 6)."]},
}

MYSTERIES = [nativity, hamper, carol, mince]
