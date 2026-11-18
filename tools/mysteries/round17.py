from lib import *  # evidence helpers

# Round 17 (18 Nov): 1 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- CARAVAN (L2)
caravan = {
 "slug": "the-caravan-park-jewels", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 133", "title_html": "THE CARAVAN<br>PARK JEWELS", "title_plain": "The Caravan Park Jewels",
 "teaser": "A widow's jewellery roll vanishes from her caravan during the park's talent show. One neighbour says he was on stage – but the running order says otherwise.",
 "intro": "At <b>Sandpiper Bay Holiday Park</b>, Mrs Iris Bell's jewellery roll – her late husband's gifts, worth £9,000 – was taken from caravan 14 during Friday's talent show. " + STD,
 "clues": [
  {"name": "Iris Bell", "role": "Holidaymaker", "label": "THEFT REPORT",
   "quote": "I locked the caravan at half seven and went to the clubhouse for the talent show. At ten past nine the door was unlocked and the roll was gone from under my pillow.",
   "evidence": ev_rows("Theft report – caravan 14", [
       ("Left", "19:30, door locked"),
       ("Returned", "21:10, door unlocked, not forced"),
       ("Missing", "Jewellery roll, under the pillow"),
       ("Spare keys", "One with reception, one lent to neighbour in no. 15 last week to feed the cat"),
     ])},
  {"name": "Barry Cole", "role": "Neighbour, caravan 15", "label": "BARRY'S STATEMENT",
   "quote": "I gave the key back days ago. On Friday I was in the talent show – I sang “My Way” at about half eight and stayed in the clubhouse all night. Everyone saw me.",
   "evidence": ev_rows("Barry Cole – park records", [
       ("Booking", "Caravan 15, two weeks"),
       ("Account", "£640 site fees overdue"),
       ("Note", "Asked reception twice whether Mrs Bell “has anything valuable”"),
     ])},
  {"name": "Donna Pike", "role": "Entertainments host", "label": "RUNNING ORDER",
   "quote": "The show started at eight. One act pulled out at the last minute, so we moved everyone up – I've got the final running order here.",
   "evidence": ev_table("Talent show – final running order", ["Time", "Act"], [
       ("20:00", "Twins on ukulele"),
       ("20:12", "Magic Mick"),
       ("20:25", "Barry Cole – “My Way” (WITHDRAWN, did not arrive)"),
       ("20:25", "Line dancers (moved up)"),
       ("20:45", "Interval"),
       ("21:00", "Winner announced"),
     ], mono_cols=(0,))},
  {"name": "Kev Shaw", "role": "Reception", "label": "SPARE KEY BOOK",
   "quote": "Our spare key for 14 was on the board all night. Barry did borrow Mrs Bell's own spare – did he give it back? She'd know better than me.",
   "evidence": ev_table("Reception key book", ["Date", "Key", "Out", "Back"], [
       ("Mon", "No. 14 (park spare)", "—", "On board"),
       ("Fri 21:30", "No. 14 (park spare)", "Police", "—"),
     ])},
  {"name": "Tasha Moore", "role": "Caravan 16", "label": "TASHA'S PHOTO",
   "quote": "I stayed in with the baby. Just after half eight I took a picture of the sunset from my step – there's someone going into number 14 in the corner of it.",
   "evidence": ev_photos("Tasha's phone", [
       ("IMG_7731", "20:34", "Sunset over the dunes. Bottom left: a man in a Hawaiian shirt opening the door of caravan 14."),
     ])},
  {"name": "Mick Dunn", "role": "Magician", "label": "COSTUME LIST",
   "quote": "I did my act at quarter past eight and stayed for the rest. Barry told me in the bar on Thursday he'd be singing in his lucky Hawaiian shirt.",
   "evidence": ev_rows("Search of caravan 15", [
       ("Found", "Hawaiian shirt with sand on the hem"),
       ("Found", "A key tagged “14 – Iris”"),
       ("Not found", "The jewellery roll"),
     ])},
 ],
 "solution": {"killer": "Barry Cole",
   "motive": "Barry owed £640 in site fees and had asked reception whether Mrs Bell owned anything valuable (clue 2).",
   "proof": ["Barry says he sang “My Way” at half eight in front of everyone (clue 2). But the running order shows he was withdrawn and never arrived (clue 3).",
             "At 20:34 Tasha photographed a man in a Hawaiian shirt opening caravan 14 (clue 5). Barry's Hawaiian shirt and Iris's own spare key, which he claimed to have returned, were in his caravan (clues 1, 6)."],
   "cleared": ["<b>Kev</b>'s park spare never left the board (clue 4).",
               "<b>Mick</b> performed and stayed in the clubhouse (clues 3, 6), and <b>Donna</b> was hosting the show (clue 3).",
               "<b>Tasha</b> stayed home with the baby and reported what she saw (clue 5); <b>Iris</b> was at the show (clue 1)."]},
}

# ---------------------------------------------------------------- AUCTION (L3)
auction = {
 "slug": "death-at-the-auction-house", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 134", "title_html": "DEATH AT THE<br>AUCTION HOUSE", "title_plain": "Death at the Auction House",
 "teaser": "The auctioneer dies in the strongroom on sale day. The porter says he was taking a phone bid at the time. The phone lines say otherwise.",
 "intro": "At <b>Ferris &amp; Gold</b> auctioneers, senior valuer Martin Gold was found dead in the basement strongroom during the Thursday sale of fine silver. " + STD,
 "clues": [
  {"name": "DI Helen Shaw", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Gold was struck with a silver candlestick taken from the sale. The strongroom has a time lock and a door log; whoever killed him was logged in.",
   "evidence": ev_rows("Police report – Ferris &amp; Gold", [
       ("Found", "15:20, basement strongroom"),
       ("Death", "Between 14:30 and 14:50 (pathologist)"),
       ("Weapon", "Lot 52, Georgian candlestick"),
       ("Strongroom", "Staff cards only; every entry logged"),
     ])},
  {"name": "Clive Ferris", "role": "Partner", "label": "STRONGROOM LOG",
   "quote": "I was on the rostrum taking bids all afternoon – two hundred people watched me. Martin and I disagreed about the business, but I'd never hurt him.",
   "evidence": ev_table("Strongroom door log", ["Time", "Card", "Name"], [
       ("14:05", "S-02", "M. Gold"),
       ("14:31", "S-06", "J. Reid"),
       ("14:46", "S-06", "J. Reid (exit)"),
       ("15:20", "S-03", "P. Lam"),
     ], mono_cols=(0,))},
  {"name": "Josh Reid", "role": "Porter", "label": "JOSH'S STATEMENT",
   "quote": "I took lot 52 back down at half two, after it sold, and left it on the bench. Mr Gold was fine. I wasn't down there long – then I manned the phone bank. I took Mrs Albright's bid on lot 47 at twenty to three.",
   "evidence": ev_table("Sale record", ["Lot", "Time", "Item", "Sold to"], [
       ("47", "14:40", "Tea service", "Phone bid – Mrs Albright"),
       ("52", "14:22", "Pair of candlesticks", "Room – paddle 118"),
       ("60", "14:58", "Salver", "Online"),
     ], mono_cols=(1,))},
  {"name": "Priya Lam", "role": "Cataloguer", "label": "PHONE BANK LOG",
   "quote": "I found him when I went down for lot 61. I'd been in the office cataloguing all afternoon with the door open – I saw Clive on the CCTV monitor the whole time.",
   "evidence": ev_table("Phone bank – line records", ["Line", "Porter", "Call"], [
       ("Line 1", "A. Okoro", "14:36–14:41, Mrs Albright, lot 47"),
       ("Line 2", "J. Reid", "No calls 14:00–15:00"),
       ("Line 3", "S. Wren", "14:55–14:59, lot 60 enquiry"),
     ])},
  {"name": "Ade Okoro", "role": "Porter", "label": "MANAGER'S MEMO",
   "quote": "I took Mrs Albright's call myself on line 1 – I always do, she likes me. Josh wasn't at the phones at all until about ten to three, now I think of it.",
   "evidence": ev_rows("Martin Gold's desk – memo, Wednesday", [
       ("To", "J. Reid"),
       ("Re", "Missing lot 33 (silver vinaigrette) from last month's sale"),
       ("Text", "“Bring it back by Friday or I go to the police.”"),
     ])},
  {"name": "Sarah Wren", "role": "Porter", "label": "ROSTRUM CCTV",
   "quote": "Clive never left the rostrum. Josh came up the basement stairs just before quarter to three looking pale and went to wash his hands.",
   "evidence": ev_photos("Saleroom camera", [
       ("CAM-1", "14:30–15:00", "C. Ferris on the rostrum throughout, gavel in hand."),
       ("CAM-3", "14:47", "J. Reid coming up from the basement, sleeves pushed up."),
     ])},
 ],
 "solution": {"killer": "Josh Reid",
   "motive": "Martin had caught Josh stealing a silver vinaigrette and was going to the police on Friday (clue 5).",
   "proof": ["Martin died between 14:30 and 14:50 (clue 1). Josh's card was the only one to enter the strongroom then: in at 14:31 and out at 14:46 (clue 2).",
             "Josh says he was back at the phone bank taking Mrs Albright's bid at 14:40 (clue 3). But the line records show Ade took that call on line 1 and Josh's line had no calls at all (clues 4, 5). CCTV shows him coming up from the basement only at 14:47 (clue 6)."],
   "cleared": ["<b>Clive</b> argued with Martin but was on the rostrum throughout (clue 6).",
               "<b>Priya</b> found the body at 15:20, long after the death (clues 1, 2).",
               "<b>Ade</b> and <b>Sarah</b> were on the phone bank (clue 4)."]},
}

MYSTERIES = [caravan, auction]
