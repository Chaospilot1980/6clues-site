from lib import *  # evidence helpers

# Round 22 (18 Nov): 1 Rookie, 1 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- DOG SHOW (L1)
dogshow = {
 "slug": "the-dog-show-trophy", "level": 1, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 150", "title_html": "THE DOG SHOW<br>TROPHY", "title_plain": "The Dog Show Trophy",
 "teaser": "The silver Best in Show cup vanishes from the prize table just before the final. A trail of dog biscuits and a very guilty-looking spaniel help crack the case.",
 "intro": "At the <b>Meadowford Village Dog Show</b>, the silver Best in Show cup disappeared from the prize table in the marquee half an hour before the final judging. " + STD,
 "clues": [
  {"name": "Mrs Pam Hughes", "role": "Show secretary", "label": "SHOW REPORT",
   "quote": "I polished the cup and put it on the prize table at two. When I came back from the gate at half past, it was gone – and there were dog biscuits all over the grass behind the marquee.",
   "evidence": ev_rows("Show report", [
       ("Cup on table", "14:00"),
       ("Found missing", "14:30"),
       ("Clue", "A trail of bone-shaped biscuits from the back of the marquee to the car park"),
       ("Final judging", "15:00"),
     ])},
  {"name": "Colin Rudd", "role": "Exhibitor", "label": "COLIN'S STATEMENT",
   "quote": "I was in the ring with my spaniel Pepper the whole time between two and half past – we were in the Obedience class. I never went near the prize table.",
   "evidence": ev_rows("Colin Rudd – show history", [
       ("Best in Show", "Never won in 12 years of trying"),
       ("Quote to the judge last year", "“That cup should be on my mantelpiece.”"),
       ("Dog", "Pepper, spaniel – famous for her love of biscuits"),
     ])},
  {"name": "Sue Barker", "role": "Ring steward", "label": "OBEDIENCE CLASS LIST",
   "quote": "I run the Obedience ring. One dog was entered but scratched at the last minute – the owner said his dog had a sore paw.",
   "evidence": ev_table("Obedience class – 14:00", ["Ring no.", "Dog", "Owner", "Result"], [
       ("4", "Max", "S. Barker's nephew Tom", "3rd"),
       ("7", "Pepper", "C. Rudd", "Scratched – did not compete"),
       ("9", "Daisy", "J. Lane", "1st"),
     ])},
  {"name": "Jo Lane", "role": "Exhibitor", "label": "BISCUIT STALL",
   "quote": "I was in the Obedience ring with Daisy and we won! After that I bought treats at the stall.",
   "evidence": ev_table("Biscuit stall – sales", ["Time", "Item", "Buyer"], [
       ("13:50", "Bag of bone-shaped biscuits", "C. Rudd"),
       ("14:35", "Chew toy", "J. Lane"),
     ], mono_cols=(0,))},
  {"name": "Ben Ford", "role": "Car park attendant", "label": "CAR PARK NOTE",
   "quote": "At about quarter past two a man came out the back of the marquee with a spaniel and a lumpy coat over his arm. He put the coat in his car boot.",
   "evidence": ev_note("CAR PARK NOTEBOOK", [
       "14:15 – spaniel man, lumpy coat,",
       "green estate car, registration",
       "ending RUD 1. Dog eating biscuits",
       "off the grass the whole way."],
     "– Ben")},
  {"name": "Mr Neil Shah", "role": "Judge", "label": "REGISTRATION LIST",
   "quote": "Every exhibitor registers their car so we can find them if their dog needs them. It's very useful today.",
   "evidence": ev_table("Exhibitors' cars", ["Owner", "Car", "Registration"], [
       ("C. Rudd", "Green estate", "…RUD 1"),
       ("J. Lane", "Red hatchback", "…JL 22"),
       ("P. Hughes", "Blue van", "…PH 07"),
     ])},
 ],
 "solution": {"killer": "Colin Rudd",
   "motive": "Colin had never won Best in Show in 12 years and said the cup should be on his mantelpiece (clue 2).",
   "proof": ["The cup went between 14:00 and 14:30, and a trail of bone-shaped biscuits led from the marquee to the car park (clue 1).",
             "Colin says he was in the Obedience ring with Pepper, but Pepper was scratched and didn't compete (clue 3).",
             "Colin bought bone-shaped biscuits at 13:50 (clue 4). At 14:15 a man with a spaniel put a lumpy coat in a green estate car ending RUD 1 (clue 5) – Colin's car (clue 6)."],
   "cleared": ["<b>Jo</b> was competing and won the Obedience class (clue 3).",
               "<b>Mrs Hughes</b> was at the gate, <b>Sue</b> ran the ring, and <b>Ben</b> and <b>Mr Shah</b> only report what they know."]},
}

# ---------------------------------------------------------------- ICE-CREAM VAN (L2)
icecream = {
 "slug": "the-ice-cream-van-takings", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 151", "title_html": "THE ICE-CREAM<br>VAN TAKINGS", "title_plain": "The Ice-Cream Van Takings",
 "teaser": "A whole bank-holiday's takings vanish from an ice-cream van on the seafront. The van's chime, a sticky receipt and the tide timetable tell the real story.",
 "intro": "On <b>Saltby seafront</b>, ice-cream seller Gino Russo's bank-holiday takings – £1,840 in a cash bag – disappeared from his van while he was helping at a rescue on the beach. " + STD,
 "clues": [
  {"name": "Gino Russo", "role": "Ice-cream seller", "label": "THEFT REPORT",
   "quote": "At four o'clock a child got stuck on the groyne and I ran down to help. I left the van unlocked – stupid. When I came back at twenty past, the cash bag under the counter was gone.",
   "evidence": ev_rows("Theft report", [
       ("Van left", "16:00"),
       ("Back", "16:20 – cash bag missing"),
       ("Amount", "£1,840"),
       ("Only people who knew where the bag was kept", "Gino, his assistant Kelly, and his cousin Marco"),
     ])},
  {"name": "Marco Russo", "role": "Gino's cousin", "label": "MARCO'S STATEMENT",
   "quote": "I was out fishing on the end of the pier from three until five. Ask anyone on the pier – I caught two mackerel.",
   "evidence": ev_rows("Marco Russo – money", [
       ("Owes Gino", "£900, borrowed in March"),
       ("Note", "Gino asked for it back on Saturday – 'by Tuesday or I tell your mother'"),
     ])},
  {"name": "Kelly Moss", "role": "Gino's assistant", "label": "LIFEGUARD LOG",
   "quote": "I was on my break at the café. I heard the shout about the child and ran to the beach too – I was there with Gino the whole time.",
   "evidence": ev_table("Lifeguard log – Bank Holiday Monday", ["Time", "Event", "Helpers"], [
       ("16:01", "Child stuck on the groyne", "Lifeguard, G. Russo, K. Moss"),
       ("16:18", "Child safe", "–"),
     ], mono_cols=(0,))},
  {"name": "Eli Watts", "role": "Harbour master", "label": "PIER NOTICE",
   "quote": "The end of the pier closes when the sea gets rough. On Monday we had a strong onshore wind all afternoon.",
   "evidence": ev_note("NOTICE ON THE PIER GATE – MONDAY", [
       "END OF PIER CLOSED 14:00–18:00",
       "HIGH WINDS – NO FISHING",
       "By order of the Harbour Master"],
     "– E. Watts")},
  {"name": "Rita Dunn", "role": "Fish-and-chip shop owner", "label": "CHIP SHOP RECEIPT",
   "quote": "Marco came in just after four, all out of breath, and paid for his chips with a twenty-pound note that was covered in sticky raspberry sauce.",
   "evidence": ev_table("Rita's Fish Bar – till", ["Time", "Order", "Paid with"], [
       ("16:06", "Cod and chips", "£20 note – sticky with red sauce"),
       ("16:12", "Two portions of chips", "Card"),
     ], mono_cols=(0,))},
  {"name": "Paul Grant", "role": "Deckchair attendant", "label": "VAN SAUCE",
   "quote": "Gino's van sells the only raspberry sauce on the seafront. Kids drip it on everything – including his money.",
   "evidence": ev_rows("Seafront traders – what they sell", [
       ("Gino's van", "Ice cream with raspberry sauce"),
       ("Rita's Fish Bar", "Fish and chips"),
       ("Beach café", "Tea, cake, sandwiches"),
     ])},
 ],
 "solution": {"killer": "Marco Russo",
   "motive": "Marco owed Gino £900 and had to pay it back by Tuesday (clue 2).",
   "proof": ["The cash was taken between 16:00 and 16:20, and only Gino, Kelly and Marco knew where the bag was kept (clue 1).",
             "Marco says he was fishing at the end of the pier from three until five. But the end of the pier was closed from 14:00 to 18:00 because of high winds (clue 4).",
             "At 16:06 Marco paid for chips with a £20 note sticky with red sauce (clue 5) – and Gino's van sells the only raspberry sauce on the seafront (clue 6)."],
   "cleared": ["<b>Kelly</b> was helping at the rescue with Gino and the lifeguard (clue 3).",
               "<b>Gino</b> was at the rescue (clue 3); <b>Rita</b>, <b>Paul</b> and <b>Eli</b> only report what they know."]},
}

# ---------------------------------------------------------------- LIDO (L3)
lido = {
 "slug": "death-at-the-lido", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 152", "title_html": "DEATH AT<br>THE LIDO", "title_plain": "Death at the Lido",
 "teaser": "The lido's owner drowns in the deep end before opening time. The pool's chlorine log, a wet swimming cap and a turnstile tell a story the staff won't.",
 "intro": "At the <b>Brockley Art Deco Lido</b>, owner Raymond Pike was found drowned in the deep end at 06:45, fifteen minutes before the early swimmers arrived. " + STD,
 "clues": [
  {"name": "DS Amina Yusuf", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Pike had a blow to the back of the head before he went into the water. His waterproof watch logs his heart rate, so we know exactly when he died.",
   "evidence": ev_rows("Police report – Brockley Lido", [
       ("Found", "06:45, deep end, by the duty lifeguard"),
       ("Injury", "Blow to the head before drowning"),
       ("Watch", "Heart rate stopped 06:12"),
       ("Lido", "Staff enter through the turnstile with a card; the gates open to the public at 07:00"),
     ])},
  {"name": "Gary Pike", "role": "Raymond's son, manager", "label": "TURNSTILE LOG",
   "quote": "I arrived at half past six, opened the café and started the coffee machine. I didn't go near the pool until Sam shouted.",
   "evidence": ev_table("Staff turnstile – Monday", ["Time", "Card", "Name"], [
       ("05:55", "S-01", "R. Pike"),
       ("06:02", "S-04", "D. Shaw"),
       ("06:30", "S-02", "G. Pike"),
       ("06:40", "S-06", "S. Lee"),
     ], mono_cols=(0,))},
  {"name": "Donna Shaw", "role": "Pool technician", "label": "CHLORINE LOG",
   "quote": "I came in at six to test the water and dose the chlorine, like every morning. Mr Pike was alive and swimming lengths when I started. I was in the plant room the whole time after that.",
   "evidence": ev_table("Plant room – water treatment", ["Time", "Action", "By"], [
       ("06:05", "Water test – pool clear", "D. Shaw"),
       ("06:08", "Chlorine dosing started", "Automatic"),
       ("06:15", "Dosing finished", "Automatic"),
       ("06:35", "Water test", "D. Shaw"),
     ], mono_cols=(0,))},
  {"name": "Sam Lee", "role": "Lifeguard", "label": "SALE AGREEMENT",
   "quote": "I found him when I came on duty. Everyone knew Mr Pike was about to sell the lido to a hotel chain – the staff were furious, and so was Donna.",
   "evidence": ev_rows("Draft sale agreement – signed by R. Pike only", [
       ("Buyer", "Harbour Hotels plc"),
       ("Plan", "Fill in the pool and build a spa hotel"),
       ("Staff", "All contracts end on completion"),
       ("Signing date", "Monday 10:00"),
     ])},
  {"name": "Nora Pike", "role": "Raymond's ex-wife", "label": "PLANT ROOM CAMERA",
   "quote": "Raymond and I haven't spoken in years. The lido's camera system is still on my phone from when we ran it together – I saved what it recorded.",
   "evidence": ev_photos("Plant room door camera", [
       ("CAM-5", "06:06", "D. Shaw enters the plant room."),
       ("CAM-5", "06:09", "D. Shaw leaves the plant room, towards the pool, in her technician's overalls."),
       ("CAM-5", "06:16", "D. Shaw comes back into the plant room. Her overalls are soaked from the chest down."),
     ])},
  {"name": "Theo Grant", "role": "Bakery delivery driver", "label": "DELIVERY RECEIPTS",
   "quote": "I deliver to the lido café every morning. I never get past the café counter – you can't even see the pool from there, the changing rooms are in the way.",
   "evidence": ev_table("Café supplier – Monday delivery", ["Time", "Delivered to", "Signed by"], [
       ("06:31", "Lido café – pastries", "G. Pike"),
       ("06:33", "Lido café – milk", "G. Pike"),
     ], mono_cols=(0,))},
 ],
 "solution": {"killer": "Donna Shaw",
   "motive": "Raymond was signing a sale that day that would fill in the pool and end every staff contract, including Donna's (clue 4).",
   "proof": ["Raymond died at 06:12 (clue 1). Only Raymond (05:55) and Donna (06:02) had come in through the turnstile before then (clue 2).",
             "Donna says she stayed in the plant room after starting her work. But the chlorine dosing ran automatically, and the camera shows her leaving the plant room at 06:09 towards the pool and coming back at 06:16 soaked from the chest down (clues 3, 5)."],
   "cleared": ["<b>Gary</b> only came in at 06:30 and signed for café deliveries at 06:31 and 06:33 (clues 2, 6).",
               "<b>Sam</b> arrived at 06:40 (clue 2), <b>Theo</b> only reached the café at 06:31 (clue 6), and <b>Nora</b> was not at the lido at all – no card of hers is on the turnstile log (clue 2)."]},
}

# ---------------------------------------------------------------- CLIMBING WALL (L3)
climbing = {
 "slug": "death-at-the-climbing-wall", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 153", "title_html": "DEATH AT THE<br>CLIMBING WALL", "title_plain": "Death at the Climbing Wall",
 "teaser": "A climbing-gym owner falls from the top wall after closing. The rope was cut, the gym was locked – and the auto-belay log knows who was still climbing.",
 "intro": "At <b>Summit Climbing Centre</b>, owner Will Hartley was found dead at the foot of the 15-metre lead wall after the gym had closed for the night. His rope had been cut almost through. " + STD,
 "clues": [
  {"name": "DI Mark Osei", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Hartley fell when his rope snapped – it had been cut with a blade to a few strands. Someone did it while he was climbing, from the top platform.",
   "evidence": ev_rows("Police report – Summit Climbing Centre", [
       ("Found", "22:40, foot of the lead wall"),
       ("Fall", "22:12 – recorded by the wall's impact sensor"),
       ("Rope", "Cut almost through, about 2 m below the top anchor"),
       ("Top platform", "Reached only by the staff ladder behind the wall"),
     ])},
  {"name": "Josh Hartley", "role": "Will's brother, co-owner", "label": "DOOR LOG",
   "quote": "I locked up at ten and went straight home. Will said he wanted to test the new route alone. I wish I'd stayed.",
   "evidence": ev_table("Front door – card log", ["Time", "Card", "Event"], [
       ("21:58", "J. Hartley", "Locked – alarm set to 'partial' (staff inside)"),
       ("22:20", "K. Brand", "Out"),
       ("22:38", "J. Hartley", "In"),
     ], mono_cols=(0,))},
  {"name": "Kira Brand", "role": "Route setter", "label": "AUTO-BELAY LOG",
   "quote": "I was setting new routes on the bouldering wall at the other end of the gym until twenty past ten. I had headphones on – I didn't hear a thing.",
   "evidence": ev_table("Auto-belay devices – after closing", ["Time", "Wall", "Event"], [
       ("22:02", "Speed wall (next to the staff ladder)", "Clipped in"),
       ("22:05", "Speed wall", "Clipped out at top"),
       ("22:14", "Speed wall", "Clipped in – lowered to floor"),
     ], mono_cols=(0,))},
  {"name": "Leo Marsh", "role": "Bookkeeper", "label": "SHOP AUDIT",
   "quote": "I did the audit for Will and left at closing time. He told me he'd found out someone was stealing from the shop takings and was going to sort it out tomorrow.",
   "evidence": ev_rows("Summit Climbing Centre – shop audit, Monday", [
       ("Missing", "£6,200 over three months"),
       ("Till operator on all short days", "K. Brand"),
       ("Will's note", "“Talk to Kira tomorrow – then police.”"),
     ])},
  {"name": "Ana Silva", "role": "Cleaner", "label": "SHOE CHECK",
   "quote": "I clean the bouldering area every night at half past ten. Kira's brushes and holds were laid out, but the chalk on her crash mat was untouched – nobody had climbed there for a while.",
   "evidence": ev_rows("Bouldering area – 22:30", [
       ("Route-setting tools", "Laid out, not used since the evening session"),
       ("New holds", "Still in their box – none screwed on"),
       ("Climbing shoes by the speed wall", "Size 5, name inside: K. BRAND"),
     ])},
  {"name": "Sophie Hartley", "role": "Will's wife", "label": "PHONE CALL",
   "quote": "Will rang me at ten past ten from the top of the wall – he always calls before a hard route. He said, 'Kira's still here, she's coming up to watch.'",
   "evidence": ev_table("Sophie's phone", ["Time", "Call", "Length"], [
       ("22:09", "Incoming – Will", "1 min 40 s"),
     ], mono_cols=(0,))},
 ],
 "solution": {"killer": "Kira Brand",
   "motive": "Will had found that £6,200 was missing from the shop takings – always on Kira's shifts – and was going to confront her and call the police (clue 4).",
   "proof": ["Will fell at 22:12 after his rope was cut from the top platform (clue 1). Only Kira was still in the gym – Josh locked up at 21:58 and only returned at 22:38 (clue 2).",
             "Kira says she was setting routes on the bouldering wall until 22:20. But nothing there had been touched (clue 5), and the auto-belay on the speed wall – next to the staff ladder – was used at 22:02, 22:05 and 22:14 (clue 3). Her climbing shoes were found by the speed wall (clue 5).",
             "At 22:09 Will told his wife Kira was coming up to watch him (clue 6)."],
   "cleared": ["<b>Josh</b> had left at 21:58 and came back at 22:38 (clue 2).",
               "<b>Leo</b> left at closing time, <b>Ana</b> arrived at 22:30, and <b>Sophie</b> was at home on the phone (clues 4, 5, 6)."]},
}

MYSTERIES = [dogshow, icecream, lido, climbing]
