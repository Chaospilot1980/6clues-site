from lib import *  # evidence helpers

# Round 44 (19 Nov): Black Friday round – 1 Rookie, 1 Detective, 1 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-19"

# ---------------------------------------------------------------- GOLDEN TEDDY (L1)
teddy = {
 "slug": "the-black-friday-teddy", "level": 1, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 240", "title_html": "THE BLACK<br>FRIDAY TEDDY", "title_plain": "The Black Friday Teddy",
 "teaser": "The only Golden Teddy in town vanishes from the toy shop window before the Black Friday doors open. A price tag and a sale online give the thief away.",
 "intro": "At <b>Pip's Toy Shop</b>, a queue formed all night for the one-and-only Golden Teddy, on sale for Black Friday. At 07:00, ten minutes before the doors opened, the teddy was gone from the window. " + STD,
 "clues": [
  {"name": "Mrs Pippa Grant", "role": "Shop owner", "label": "SHOP REPORT",
   "quote": "I checked the window at quarter to seven – the teddy was there. At seven it was gone, and only staff were inside the shop.",
   "evidence": ev_rows("Shop report", [
       ("Golden Teddy seen", "06:45"),
       ("Gone", "07:00"),
       ("Doors open", "07:10"),
       ("Inside the shop", "Pippa, Sam, Lily, Owen – staff only"),
       ("Clue", "The teddy's gold price tag torn off and left on the floor"),
     ])},
  {"name": "Sam Ford", "role": "Shop assistant", "label": "SAM'S STATEMENT",
   "quote": "I was in the stockroom the whole time, unpacking boxes of board games. I never went near the window.",
   "evidence": ev_table("Stockroom door log", ["Time", "Door", "Who"], [
       ("06:30", "In", "S. Ford"),
       ("06:48", "Out", "S. Ford"),
       ("06:58", "In", "S. Ford"),
       ("07:20", "Out", "S. Ford"),
     ], mono_cols=(0,))},
  {"name": "Lily Shaw", "role": "Shop assistant", "label": "LILY'S STATEMENT",
   "quote": "I was at the till counting the float from half six until the doors opened. You can see the till roll.",
   "evidence": ev_table("Till 1 – float count", ["Time", "Action", "By"], [
       ("06:35", "Float opened", "L. Shaw"),
       ("06:50", "Coins counted", "L. Shaw"),
       ("07:05", "Float checked", "L. Shaw"),
     ], mono_cols=(0,))},
  {"name": "Owen Price", "role": "Window dresser", "label": "OWEN'S NOTE",
   "quote": "I was outside handing out hot chocolate to the queue from half six. Through the glass I saw Sam at the window at about ten to seven, holding something gold.",
   "evidence": ev_note("OWEN'S NOTE", [
       "Outside with the queue 06:30–07:10.",
       "06:50 – Sam at the window, reaching",
       "in. Something gold in his arms.",
       "Thought he was tidying the display."],
     "– Owen")},
  {"name": "Mia Clark", "role": "First in the queue", "label": "ONLINE LISTING",
   "quote": "I'd queued since midnight. Then at eight o'clock my brother showed me the teddy for sale online – for ten times the price!",
   "evidence": ev_rows("Online listing (screenshot, 08:02)", [
       ("Item", "GOLDEN TEDDY – brand new, sold out everywhere!"),
       ("Price", "£400 (shop price £40)"),
       ("Seller", "samf_deals"),
       ("Photo", "The teddy on a pile of board-game boxes"),
     ])},
  {"name": "Mr Dev Shah", "role": "Shopping centre guard", "label": "GUARD'S LOG",
   "quote": "Nobody came in or out of the shop's back door before half seven. I was sitting right by it.",
   "evidence": ev_table("Back door – guard's log", ["Time", "Event"], [
       ("06:00–07:30", "Back door closed – no one in or out"),
       ("07:35", "S. Ford leaves with a big rucksack"),
     ], mono_cols=(0,))},
 ],
 "solution": {"killer": "Sam Ford",
   "motive": "Sam wanted to sell the rare teddy online for ten times its price (clue 5).",
   "proof": ["The teddy vanished between 06:45 and 07:00, when only staff were inside (clue 1).",
             "Sam says he never left the stockroom, but the door log shows him out from 06:48 to 06:58 (clue 2) – and Owen saw him at the window at 06:50 holding something gold (clue 4).",
             "At 08:02 the teddy was for sale by 'samf_deals', photographed on the board-game boxes Sam was unpacking (clue 5), and Sam left with a big rucksack at 07:35 (clue 6)."],
   "cleared": ["<b>Lily</b> was counting the float at the till all morning (clue 3), and <b>Owen</b> was outside with the queue (clue 4).",
               "<b>Pippa</b>, <b>Mia</b> and <b>Mr Shah</b> only report what they saw."]},
}

# ---------------------------------------------------------------- DOORBUSTER (L2)
door = {
 "slug": "the-doorbuster-deception", "level": 2, "crime": "FRAUD", "who": "fraudster", "added": ADDED,
 "caseno": "CASE NO. 241", "title_html": "THE DOORBUSTER<br>DECEPTION", "title_plain": "The Doorbuster Deception",
 "teaser": "Ten half-price TVs were the big Black Friday deal – and they sold out online in one second flat. Somebody inside the store bought them first.",
 "intro": "At <b>Brightway Electronics</b>, the Black Friday doorbuster was ten big TVs at half price, on sale online from exactly 00:00. All ten were gone at 00:00:01 – to orders that turned out to be fake. " + STD,
 "clues": [
  {"name": "Grace Lin", "role": "Store manager", "label": "SALES REPORT",
   "quote": "Ten TVs, gone in one second. No real shopper is that fast. All ten went to different names – but every one of them used the same delivery address.",
   "evidence": ev_table("Doorbuster orders – 00:00:01", ["Order", "Name", "Deliver to"], [
       ("#5501", "A. Smith", "Unit 7, Mill Lane"),
       ("#5502", "B. Jones", "Unit 7, Mill Lane"),
       ("#5503–5510", "8 more names", "Unit 7, Mill Lane"),
     ], mono_cols=(0,))},
  {"name": "Kevin Marsh", "role": "Deputy manager", "label": "KEVIN'S STATEMENT",
   "quote": "I've no idea who did it. I was home asleep at midnight – I had the opening shift at six.",
   "evidence": ev_rows("Staff file – Kevin Marsh", [
       ("Job", "Deputy manager, online shop admin"),
       ("System access", "Can set sale start time and see stock before launch"),
       ("Side business", "Marsh Resale Ltd – 'brand-new TVs at great prices'"),
     ])},
  {"name": "Tara Webb", "role": "Web admin", "label": "SYSTEM LOG",
   "quote": "Someone logged into the shop system from inside the store at 23:52 and changed the sale start time for one minute only. That let their orders in first.",
   "evidence": ev_table("Shop admin log", ["Time", "User", "Action"], [
       ("23:52", "k.marsh", "Login – store network"),
       ("23:53", "k.marsh", "TV sale start set to 23:59"),
       ("23:59", "–", "10 orders placed"),
       ("00:00", "k.marsh", "TV sale start reset to 00:00"),
     ], mono_cols=(0,))},
  {"name": "Bill Carter", "role": "Night cleaner", "label": "BILL'S STATEMENT",
   "quote": "I clean the store from ten till two. Just before midnight I saw the light on in the back office. Someone was at the computer – I didn't see who.",
   "evidence": ev_note("CLEANING SHEET", [
       "23:45 – back office light ON.",
       "Car park: one car – silver estate,",
       "plate ending '... KM1'.",
       "23:55 – sales floor done."],
     "– Bill")},
  {"name": "Nina Ross", "role": "Landlord, Mill Lane", "label": "TENANCY RECORD",
   "quote": "Unit 7 on Mill Lane? I rent that out. It's a little storage unit for a resale business.",
   "evidence": ev_rows("Mill Lane units – tenants", [
       ("Unit 6", "Bright Bakes (cake supplies)"),
       ("Unit 7", "Marsh Resale Ltd – K. Marsh"),
       ("Unit 8", "Empty"),
     ])},
  {"name": "Paul Day", "role": "Sales assistant", "label": "PAUL'S STATEMENT",
   "quote": "I did set my alarm for midnight to try for one of the TVs myself! By the time the page loaded they were all gone.",
   "evidence": ev_phone("Paul's phone", "Texts to his sister, just after midnight", [
       ("Jess", "00:00", "Opening the app NOW for that TV!!"),
       ("Jess", "00:01", "SOLD OUT. At 00:00:04. How?!"),
     ])},
 ],
 "solution": {"killer": "Kevin Marsh",
   "motive": "Kevin runs a resale business and wanted the cheap TVs to sell on at full price (clue 2).",
   "proof": ["All ten TVs went to fake names at one address – Unit 7, Mill Lane (clue 1), which is rented by Marsh Resale Ltd (clue 5).",
             "The sale start was secretly moved to 23:59 by user 'k.marsh' from inside the store (clue 3).",
             "Kevin says he was home asleep, but the cleaner saw the back office lit and a car ending 'KM1' in the car park just before midnight (clue 4)."],
   "cleared": ["<b>Paul</b> tried to buy a TV himself and was too late (clue 6). <b>Tara</b> found the log, and <b>Bill</b> was cleaning.",
               "<b>Grace</b> and <b>Nina</b> only report what they know."]},
}

# ---------------------------------------------------------------- MIDNIGHT SALE (L3)
midnight = {
 "slug": "death-at-the-midnight-sale", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 242", "title_html": "DEATH AT THE<br>MIDNIGHT SALE", "title_plain": "Death at the Midnight Sale",
 "teaser": "Black Friday at Harrow & Vane: the doors open at midnight – and the owner is found dead in the locked stockroom. One alibi is a minute too long.",
 "intro": "At <b>Harrow &amp; Vane</b>, the grand old department store, owner <b>Edmund Vane</b> planned to announce the sale of the store at the stroke of midnight on Black Friday. At 00:20 he was found dead in the fourth-floor stockroom, struck with a brass display weight. " + STD,
 "clues": [
  {"name": "Dr Ann Hollis", "role": "Police surgeon", "label": "MEDICAL REPORT",
   "quote": "He died between 23:40 and 23:50. One blow to the head with the brass weight from the clock display. Whoever did it had to be in the stockroom in that window.",
   "evidence": ev_rows("Medical report – E. Vane", [
       ("Time of death", "23:40–23:50"),
       ("Cause", "Blow to the head – brass display weight"),
       ("Found", "00:20, fourth-floor stockroom"),
       ("Note", "Stockroom door opens only with a staff key card"),
     ])},
  {"name": "Clara Vane", "role": "Edmund's daughter, buyer", "label": "CLARA'S STATEMENT",
   "quote": "Father was going to sell the store my grandfather built. I begged him not to. But I was on the ground floor all evening, opening the doors with the crowd.",
   "evidence": ev_table("Key card log – 4th floor stockroom", ["Time", "Card", "Holder"], [
       ("23:31", "IN", "R. Doyle"),
       ("23:36", "OUT", "R. Doyle"),
       ("23:42", "IN", "M. Pike"),
       ("23:44", "OUT", "M. Pike"),
       ("23:58", "IN", "C. Vane"),
       ("23:59", "OUT", "C. Vane"),
     ], mono_cols=(0,), note="Door cannot be opened without a card. Cards are personal.")},
  {"name": "Martin Pike", "role": "Floor manager, 4th floor", "label": "MARTIN'S STATEMENT",
   "quote": "I popped into the stockroom at 23:42 for more gift bags – two minutes, in and out. Mr Vane was on the phone. Then I went down to my till on the second floor and stayed there for the midnight rush – check the receipts.",
   "evidence": ev_table("Till 2F-3 – receipts", ["Time", "Item", "Operator"], [
       ("23:45", "Gift bag × 2", "M. Pike"),
       ("23:47", "Scarf", "M. Pike"),
       ("23:52", "Gloves", "M. Pike"),
       ("00:02", "Perfume", "M. Pike"),
     ], mono_cols=(0,))},
  {"name": "Rachel Doyle", "role": "Personal assistant", "label": "PHONE RECORD",
   "quote": "I brought Mr Vane his speech at 23:31 and left at 23:36. He then rang his lawyer – I heard him say 'the sale goes through at midnight'.",
   "evidence": ev_table("Office phone – E. Vane extension", ["Start", "End", "Number"], [
       ("23:37", "23:46", "Ellison & Co (lawyer)"),
       ("23:49", "23:49", "Missed call – C. Vane mobile"),
     ], mono_cols=(0, 1))},
  {"name": "George Ellison", "role": "Edmund's lawyer", "label": "LAWYER'S NOTE",
   "quote": "Edmund was on the phone with me until 23:46 and very much alive. He told me one of his staff had just overheard him confirm the sale – and had not taken it well.",
   "evidence": ev_note("ELLISON & CO – CALL NOTE", [
       "23:37–23:46. E. Vane confirms sale.",
       "23:43 – EV: 'Martin just came in for",
       "gift bags and heard everything. He's",
       "furious – thirty years, he says.'"],
     "– G.E.")},
  {"name": "Jonah Reed", "role": "Security guard", "label": "STAIRWELL CAMERA",
   "quote": "The back stairs camera covers the only stairs between the second and fourth floors that skip the shop floor. I logged everyone on it.",
   "evidence": ev_table("Back stairs camera – log", ["Time", "Direction", "Person"], [
       ("23:44", "Down 4F → 2F", "M. Pike"),
       ("23:47", "Up 2F → 4F", "M. Pike (no gift bags)"),
       ("23:51", "Down 4F → 2F", "M. Pike"),
       ("23:57", "Up GF → 4F", "C. Vane"),
       ("23:44–23:51", "Alarm", "Stockroom door HELD OPEN (no card used)"),
     ], mono_cols=(0,), note="Till receipts carry the operator's code – not the person standing at the till.")},
 ],
 "solution": {"killer": "Martin Pike",
   "motive": "Martin overheard Edmund confirm the sale of the store he had worked in for thirty years, and was furious (clue 5).",
   "proof": ["Edmund died between 23:40 and 23:50 (clue 1). Edmund was alive on the phone until 23:46 (clues 4 and 5).",
             "Martin's 23:47 till receipt seems to clear him – but receipts only show the operator's code (clue 6). The camera shows him going back up to the fourth floor at 23:47 and down again at 23:51 (clue 6).",
             "The stockroom needs a key card, and Martin's card shows no return – but the door alarm shows it was held open from 23:44, when Martin left, until 23:51, when he went back down (clues 2 and 6). He propped it so he could slip back in without a trace."],
   "cleared": ["<b>Clara</b> only reached the fourth floor at 23:57 (clues 2 and 6) – after Edmund was dead; her call at 23:49 went unanswered (clue 4).",
               "<b>Rachel</b> left at 23:36 while Edmund was still alive (clues 2 and 4). <b>Dr Hollis</b>, <b>Mr Ellison</b> and <b>Jonah</b> only report what they found."]},
}

MYSTERIES = [teddy, door, midnight]
