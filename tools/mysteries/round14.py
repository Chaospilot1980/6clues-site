from lib import *  # evidence helpers

# Round 14 (18 Nov): 1 Detective, 1 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- HARBOUR (L2)
harbour = {
 "slug": "the-harbour-office-safe", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 126", "title_html": "THE HARBOUR<br>OFFICE SAFE", "title_plain": "The Harbour Office Safe",
 "teaser": "The mooring fees vanish from the harbour safe before dawn. One fisherman says he was out on the pier watching the sun come up.",
 "intro": "In the little fishing port of <b>Polcarrow</b>, a year's mooring fees – £6,400 – were taken from the harbour office safe early on a January morning. " + STD,
 "clues": [
  {"name": "Morwen Tregear", "role": "Harbour master", "label": "THEFT REPORT",
   "quote": "I locked the safe at six on Tuesday evening and opened the office at quarter to eight on Wednesday. The safe was open and empty. Only three of us know the combination.",
   "evidence": ev_rows("Theft report – harbour office", [
       ("Date", "Wednesday 12 January"),
       ("Last locked", "Tuesday 18:00, by M. Tregear"),
       ("Found open", "Wednesday 07:45"),
       ("Alarm", "Office motion sensor: 05:20–05:35"),
       ("Combination", "M. Tregear, J. Penrose (deputy), D. Hocking (former deputy)"),
     ])},
  {"name": "Davey Hocking", "role": "Fisherman, former deputy", "label": "DAVEY'S STATEMENT",
   "quote": "I wasn't anywhere near the office. At half past five I was out at the end of the pier, mending a net and watching the sun come up over the bay. Beautiful, it was.",
   "evidence": ev_rows("Davey Hocking – background", [
       ("Job", "Deputy harbour master until October"),
       ("Left", "Asked to resign over unpaid mooring fees"),
       ("Now", "Fishes from his own boat, the Kittiwake"),
       ("Debts", "Owes the harbour £1,900 in back fees"),
     ])},
  {"name": "Jenna Penrose", "role": "Deputy harbour master", "label": "HOSPITAL WRISTBAND",
   "quote": "I know the combination, yes. But on Tuesday night I was in Truro with my mum – she had a fall. I didn't get home until nine on Wednesday.",
   "evidence": ev_rows("Royal Cornwall Hospital – visitor record", [
       ("Visitor", "J. Penrose (daughter)"),
       ("Arrived", "Tuesday 22:40, A&amp;E"),
       ("Ward", "Wednesday 03:10, ward 6"),
       ("Left", "Wednesday 08:20"),
     ])},
  {"name": "Kit Rowe", "role": "Harbour café owner", "label": "TIDE &amp; SUN TABLE",
   "quote": "I open the café at six for the early boats. Funny thing – I saw a light in the harbour office through the window as I came down the hill, but I thought it was Morwen.",
   "evidence": ev_table("Polcarrow tide &amp; sun table – January", ["Date", "High water", "Sunrise", "Sunset"], [
       ("11 Jan", "05:52", "08:16", "16:32"),
       ("12 Jan", "06:40", "08:15", "16:33"),
       ("13 Jan", "07:31", "08:15", "16:35"),
     ])},
  {"name": "Ned Pascoe", "role": "Fish merchant", "label": "FISH MARKET SHEET",
   "quote": "The market opens at five. I was buying the whole time – you can't step away when the auctioneer's going. Davey still owes me money too, as it happens.",
   "evidence": ev_table("Fish market – Wednesday", ["Time", "Lot", "Buyer"], [
       ("05:05", "Pollock, 40 kg", "N. Pascoe"),
       ("05:18", "Crab, 3 boxes", "N. Pascoe"),
       ("05:31", "Mackerel, 60 kg", "N. Pascoe"),
       ("05:44", "Lobster, 6", "N. Pascoe"),
     ], mono_cols=(0,))},
  {"name": "Lowenna Kemp", "role": "Lifeboat mechanic", "label": "LIFEBOAT STATION LOG",
   "quote": "There was a shout at five – a yacht dragging its anchor off the point. I was on the slipway with the crew until it was all over.",
   "evidence": ev_table("Lifeboat station – Wednesday", ["Time", "Entry"], [
       ("04:58", "Pagers – yacht dragging anchor"),
       ("05:09", "Launch: crew of 5, mechanic L. Kemp ashore on slipway"),
       ("05:52", "Lifeboat back, recovered by L. Kemp"),
       ("06:15", "Station stood down"),
     ], mono_cols=(0,))},
 ],
 "solution": {"killer": "Davey Hocking",
   "motive": "Davey had been made to resign over unpaid fees and still owed the harbour £1,900 (clue 2).",
   "proof": ["The office was entered between 05:20 and 05:35 and the safe opened with the combination (clue 1), which Davey, as former deputy, still knew.",
             "Davey says that at 05:30 he was on the pier watching the sun come up (clue 2). But on 12 January the sun rose at 08:15 (clue 4) – at half past five it was still pitch dark. His alibi is invented."],
   "cleared": ["<b>Jenna</b> knows the combination but was at the hospital in Truro until 08:20 (clue 3).",
               "<b>Ned</b> was bidding at the fish market at 05:18 and 05:31 (clue 5), and <b>Lowenna</b> was on the lifeboat slipway (clue 6).",
               "<b>Kit</b> saw the light but only came down the hill to open at six (clue 4), and <b>Morwen</b> found the theft at 07:45 (clue 1)."]},
}

# ---------------------------------------------------------------- SIGNAL BOX (L3)
signal = {
 "slug": "death-in-the-signal-box", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 127", "title_html": "DEATH IN THE<br>SIGNAL BOX", "title_plain": "Death in the Signal Box",
 "teaser": "The old signalman dies in his box on a busy steam-railway Sunday. Every train left on time – and that is exactly what gives somebody away.",
 "intro": "On the <b>Hollow Vale Steam Railway</b>, volunteer signalman Harold Brock was found dead in Hollow Lane signal box during a busy Sunday timetable. " + STD,
 "clues": [
  {"name": "Colin Hart", "role": "Guard", "label": "POLICE REPORT",
   "quote": "When nobody answered the bell for the 15:10, I walked up the line to the box and found Harold on the floor. Before that I was in my van on train 3, checking tickets.",
   "evidence": ev_rows("Police report – Hollow Lane signal box", [
       ("Found", "14:52, by guard C. Hart"),
       ("Death", "Blow to the head; his watch smashed in the fall, stopped at 14:22"),
       ("Signal box", "Six minutes' walk from Hollow Vale station platform"),
       ("Token", "Single-line tokens are issued only from the instrument in the box"),
     ])},
  {"name": "Tom Ames", "role": "Driver, engine 3", "label": "TOKEN INSTRUMENT LOG",
   "quote": "I never left my footplate. Harold handed the token up to me at the platform as he always did, and we left on time. He'd reported me over a speeding complaint, but we'd made our peace.",
   "evidence": ev_table("Hollow Lane – token instrument", ["Time", "Token", "Event"], [
       ("13:42", "No. 2", "Out – for train 2"),
       ("14:05", "No. 2", "In – train 2 arrived"),
       ("14:29", "No. 3", "Out – for train 3"),
       ("15:02", "No. 3", "Not yet returned"),
     ], mono_cols=(0,))},
  {"name": "Lucy Bright", "role": "Fireman, engine 3", "label": "MIRA'S PLATFORM PHOTO",
   "quote": "I stayed on the footplate keeping the fire up – an engine doesn't look after itself. Tom always walks up for the token himself before a run. He says it's tradition.",
   "evidence": ev_photos("Platform photo by Mira Shah", [
       ("IMG_5520", "14:25", "Engine 3 at the platform, steam up. On the footplate: the fireman alone, shovel in hand."),
     ])},
  {"name": "Gordon Pike", "role": "Station master", "label": "TIMETABLE",
   "quote": "Harold and I had a blazing row about the rota last week, I admit it. But I didn't leave the booking office all afternoon – queues to the door.",
   "evidence": ev_programme("Hollow Vale – Sunday timetable", "Hollow Vale → Moor End", [
       ("13:45", "Train 2 – engine 2"),
       ("14:30", "Train 3 – engine 3 (driver T. Ames)"),
       ("15:10", "Train 4 – engine 2"),
     ], None)},
  {"name": "Edna Ross", "role": "Tea-room volunteer", "label": "BOOKING OFFICE TILL",
   "quote": "I took Harold his flask at two, like every Sunday, and came straight back. I told the police I never went up there at all – I panicked. He was fine and grumbling about the heat.",
   "evidence": ev_table("Booking office till", ["Time", "Sale", "Clerk"], [
       ("14:12", "4 × return, Moor End", "G. Pike"),
       ("14:18", "Family ticket", "G. Pike"),
       ("14:24", "2 × single", "G. Pike"),
       ("14:31", "Dog ticket", "G. Pike"),
     ], mono_cols=(0,))},
  {"name": "Mira Shah", "role": "Railway photographer", "label": "TEA-ROOM RECEIPTS",
   "quote": "I take pictures every Sunday. After my platform shots I went into the tea room to warm up. Edna served me – she was there the whole time I was.",
   "evidence": ev_table("Tea room – Sunday", ["Time", "Order", "Served by"], [
       ("14:08", "Pot of tea", "E. Ross"),
       ("14:19", "Bacon roll", "E. Ross"),
       ("14:27", "2 × scones", "E. Ross"),
       ("14:36", "Hot chocolate", "E. Ross"),
     ], mono_cols=(0,))},
 ],
 "solution": {"killer": "Tom Ames",
   "motive": "Harold had reported Tom over a speeding complaint (clue 2) – enough to cost him his driver's badge.",
   "proof": ["Harold's watch stopped at 14:22 when he fell (clue 1). Yet token No. 3 for Tom's train was taken out of the box instrument at 14:29 (clue 2) – and tokens can only be issued from inside the box (clue 1). Somebody else was in the box after Harold died.",
             "Tom says Harold handed the token up at the platform, as usual. But at 14:25 the platform photo shows only the fireman on the footplate (clue 3) – and Lucy says Tom always walks up to the box for the token himself.",
             "The box is six minutes from the platform (clue 1). Tom had time to reach it by 14:22, take the token at 14:29 and be back for the 14:30 departure – a few minutes late, but nobody counted."],
   "cleared": ["<b>Gordon</b> rowed with Harold, but he was selling tickets at 14:18 and 14:24 (clue 5).",
               "<b>Edna</b> lied about not going to the box – she took the flask at two – but she was serving in the tea room from 14:08 to 14:36 (clue 6).",
               "<b>Lucy</b> was on the footplate in the photo (clue 3), <b>Mira</b> was in the tea room (clue 6) and <b>Colin</b> was on the train."]},
}

MYSTERIES = [harbour, signal]
