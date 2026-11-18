from lib import *  # evidence helpers

# Round 36 (18 Nov): 2 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- GARDEN SHOW (L2)
garden = {
 "slug": "the-prize-pumpkin-poisoning", "level": 2, "crime": "SABOTAGE", "who": "saboteur", "added": ADDED,
 "caseno": "CASE NO. 206", "title_html": "THE PRIZE PUMPKIN<br>POISONING", "title_plain": "The Prize Pumpkin Poisoning",
 "teaser": "The record-breaking pumpkin at the county show rots overnight. A needle hole, a weed killer receipt and a squeaky wheelbarrow lead to the saboteur.",
 "intro": "At the <b>Lowfield County Show</b>, Bert Gibbs's giant pumpkin was on course to break the county record. The night before weighing, it turned black and soft. " + STD,
 "clues": [
  {"name": "Bert Gibbs", "role": "Pumpkin grower", "label": "BERT'S REPORT",
   "quote": "It was perfect at ten last night. At six this morning it was rotting from the inside. There's a tiny hole near the stalk – like a needle.",
   "evidence": ev_rows("Bert's report", [
       ("Pumpkin fine", "22:00"),
       ("Found rotting", "06:00"),
       ("Damage", "Needle hole by the stalk – something injected"),
       ("Weighing", "10:00, county record attempt"),
     ])},
  {"name": "Vince Hardy", "role": "Rival grower", "label": "VINCE'S STATEMENT",
   "quote": "I went home at nine and slept like a log. I don't need to cheat – my pumpkin's nearly as big as Bert's.",
   "evidence": ev_table("County record – heaviest pumpkin", ["Year", "Grower", "Weight"], [
       ("2024", "V. Hardy", "612 kg (record)"),
       ("2025", "V. Hardy", "598 kg"),
       ("2026", "B. Gibbs – expected", "about 650 kg"),
     ])},
  {"name": "Dr Ana Ruiz", "role": "Plant scientist", "label": "LAB RESULT",
   "quote": "The pumpkin was injected with strong weed killer – a brand called 'Rootout'. It's only sold to farmers with a licence.",
   "evidence": ev_rows("Lab result – pumpkin flesh", [
       ("Found", "'Rootout' concentrated weed killer"),
       ("Injected", "Through a needle, near the stalk"),
       ("Who can buy", "Licensed farmers only"),
     ])},
  {"name": "Mrs Pat Crane", "role": "Farm shop owner", "label": "SALES LOG",
   "quote": "I sell Rootout from behind the counter – customers must show their licence, and I write it down.",
   "evidence": ev_table("Rootout sales – October/November", ["Date", "Customer", "Licence"], [
       ("4 Oct", "J. Moss (farmer)", "FL-2231"),
       ("2 Nov", "V. Hardy (farmer)", "FL-1187"),
     ])},
  {"name": "Gwen Moss", "role": "Night steward", "label": "STEWARD'S NOTE",
   "quote": "I walked round the show tents at midnight and two. At about one I heard a squeaky wheelbarrow near the giant veg tent – and saw a torch.",
   "evidence": ev_note("STEWARD'S ROUND", [
       "About 01:10 – squeaky wheelbarrow,",
       "torch near giant veg tent. Man in",
       "a flat cap and wax jacket. Went to",
       "the growers' car park – blue pickup."],
     "– Gwen")},
  {"name": "Jim Moss", "role": "Farmer, Gwen's husband", "label": "CAR PARK LIST",
   "quote": "I bought Rootout for my thistles in October. But I never went to the show at night – I was in bed. Gwen took the car to work.",
   "evidence": ev_table("Growers' car park – overnight", ["Vehicle", "Owner"], [
       ("Blue pickup", "V. Hardy"),
       ("Red tractor", "B. Gibbs"),
       ("Silver car", "G. Moss (steward)"),
     ])},
 ],
 "solution": {"killer": "Vince Hardy",
   "motive": "Vince held the county record, and Bert's pumpkin was about to beat it (clue 2).",
   "proof": ["The pumpkin was injected with 'Rootout' weed killer overnight (clues 1, 3).",
             "Vince says he went home at nine, but at about 01:10 Gwen saw a man with a wheelbarrow near the veg tent walk to a blue pickup in the growers' car park (clue 5) – the blue pickup is Vince's (clue 6).",
             "Vince bought Rootout on 2 November (clue 4)."],
   "cleared": ["<b>Jim</b> bought Rootout in October for thistles, but stayed home – Gwen had the car (clues 4, 6).",
               "<b>Gwen</b> was on duty, and <b>Bert</b>, <b>Pat</b> and <b>Dr Ruiz</b> only report what they know."]},
}

# ---------------------------------------------------------------- CHARITY SHOP (L2)
charity = {
 "slug": "the-charity-shop-necklace", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 207", "title_html": "THE CHARITY<br>SHOP NECKLACE", "title_plain": "The Charity Shop Necklace",
 "teaser": "A donated necklace turns out to be worth thousands – then vanishes from the charity shop's back room. A till roll and an auction listing reveal the thief.",
 "intro": "At the <b>Hope Lane Charity Shop</b>, a donated necklace was valued at £4,500 by a visiting jeweller. Before it could be sent to auction for the charity, it disappeared from the back room. " + STD,
 "clues": [
  {"name": "Mrs Sue Price", "role": "Shop manager", "label": "MANAGER'S REPORT",
   "quote": "The jeweller valued it on Tuesday morning. I locked it in the back-room drawer. On Thursday it was gone, and the drawer was locked again.",
   "evidence": ev_rows("Manager's report", [
       ("Valued", "Tuesday 10:00 – £4,500"),
       ("Locked away", "Tuesday 10:15, back-room drawer"),
       ("Missing", "Thursday 09:00"),
       ("Drawer key", "Hangs on a hook by the till"),
     ])},
  {"name": "Kevin Shaw", "role": "Volunteer", "label": "KEVIN'S STATEMENT",
   "quote": "I didn't even know it was valuable – I was sorting books in the corner when the jeweller came. I just price the books.",
   "evidence": ev_note("SUE'S NOTE ON TUESDAY", [
       "10:00 – jeweller here. Kevin came",
       "over and asked 'How much did you",
       "say it's worth?' twice. Very",
       "interested for a book man!"],
     "– Sue")},
  {"name": "Bea Holt", "role": "Volunteer", "label": "ROTA",
   "quote": "The shop is open ten till four. Two volunteers are on each day. The manager is only in on Tuesdays and Thursdays.",
   "evidence": ev_table("Volunteer rota", ["Day", "Volunteers"], [
       ("Tuesday", "K. Shaw, B. Holt (+ Sue)"),
       ("Wednesday", "K. Shaw, R. Ali"),
       ("Thursday", "B. Holt, R. Ali (+ Sue)"),
     ])},
  {"name": "Raj Ali", "role": "Volunteer", "label": "TILL ROLL",
   "quote": "On Wednesday Kevin sent me to the post office for stamps – said the shop was quiet. I was gone about half an hour.",
   "evidence": ev_table("Till roll – Wednesday", ["Time", "Sale", "Staff code"], [
       ("13:40", "2 books – £3", "R. Ali"),
       ("14:05", "Coat – £8", "K. Shaw"),
       ("14:20", "Post office stamps – petty cash £12", "R. Ali"),
       ("14:48", "Vase – £4", "R. Ali"),
     ], mono_cols=(0,))},
  {"name": "Mr Dennis Wren", "role": "Auction house clerk", "label": "AUCTION LISTING",
   "quote": "On Friday a man brought in a necklace to sell. It matched the description the police sent round.",
   "evidence": ev_rows("Auction intake form", [
       ("Item", "Gold and garnet necklace, Victorian"),
       ("Seller", "K. Shaw"),
       ("Said", "“It was my late aunt's.”"),
       ("Reserve", "£3,000"),
     ])},
  {"name": "Mrs Lily Grant", "role": "Donor", "label": "DONOR'S LETTER",
   "quote": "It was my mother's. I gave it to the shop hoping it would raise money for the hospice. I'd recognise it anywhere – it has a tiny 'L' engraved on the clasp.",
   "evidence": ev_rows("Donation slip", [
       ("Donor", "Mrs L. Grant"),
       ("Item", "Gold and garnet necklace – 'L' on clasp"),
       ("Date", "Monday"),
     ])},
 ],
 "solution": {"killer": "Kevin Shaw",
   "motive": "Kevin wanted the £4,500 necklace for himself – he took it to auction as his 'aunt's' (clue 5).",
   "proof": ["The necklace was taken from the back-room drawer between Tuesday 10:15 and Thursday 09:00 (clue 1).",
             "Kevin says he didn't know it was valuable, but Sue saw him ask twice how much it was worth (clue 2).",
             "On Wednesday Kevin sent Raj to the post office from about 14:20, leaving himself alone in the shop (clue 4), and on Friday he tried to sell the necklace at auction (clues 5, 6)."],
   "cleared": ["<b>Raj</b> was at the post office, and <b>Bea</b> wasn't working on Wednesday (clues 3, 4).",
               "<b>Sue</b> reported the theft, and <b>Lily</b> and <b>Dennis</b> only report what they know."]},
}

# ---------------------------------------------------------------- MONASTERY (L3)
abbey = {
 "slug": "death-at-the-monastery", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 208", "title_html": "DEATH AT<br>THE MONASTERY", "title_plain": "Death at the Monastery",
 "teaser": "The monastery's book restorer is found dead in the library during the night prayers. The bell schedule, a candle stub and a vow of silence break one alibi.",
 "intro": "At <b>St Columba's Monastery</b>, Brother Anselm, who restored the old books, was found dead in the library at dawn. He had been struck with a heavy brass bookend. A rare manuscript was missing. " + STD,
 "clues": [
  {"name": "Abbot Gregory", "role": "Head of the monastery", "label": "ABBOT'S REPORT",
   "quote": "Brother Anselm stayed in the library after supper to finish his work. The 'Book of Hours' – worth half a million – is gone from his desk.",
   "evidence": ev_rows("Abbot's report", [
       ("Found", "06:00, library"),
       ("Missing", "15th-century 'Book of Hours'"),
       ("Library door", "Only the abbot and three brothers have keys"),
     ])},
  {"name": "Brother Felix", "role": "Monk, librarian's assistant", "label": "FELIX'S STATEMENT",
   "quote": "I was at Compline, the night prayer, from ten until eleven. Every brother is there – we sing every psalm together. Then I went to bed.",
   "evidence": ev_rows("Letter in Felix's cell", [
       ("From", "A rare book dealer in Geneva"),
       ("Text", "“If you can deliver the Book of Hours, we will pay €200,000. No questions.”"),
       ("Date", "Two weeks before"),
     ])},
  {"name": "Brother Martin", "role": "Monk, bell ringer", "label": "COMPLINE REGISTER",
   "quote": "At Compline each brother lights his own candle on the rack when he arrives. On that night there was one candle unlit until well after ten.",
   "evidence": ev_table("Compline – candle rack", ["Brother", "Candle lit"], [
       ("Abbot Gregory", "22:00"),
       ("Br. Martin", "22:00"),
       ("Br. Thomas", "22:00"),
       ("Br. Felix", "22:40 – arrived late, 'from the infirmary'"),
     ], mono_cols=(1,))},
  {"name": "Dr Hannah Reed", "role": "Pathologist", "label": "PATHOLOGIST'S NOTE",
   "quote": "His watch cracked when he fell. Together with the body, I'd say he was struck at about quarter past ten.",
   "evidence": ev_rows("Pathologist's notes", [
       ("Watch", "Cracked in the fall – stopped at 22:17"),
       ("Time of death", "About 22:15"),
       ("Wound", "Heavy brass bookend"),
     ])},
  {"name": "Brother Thomas", "role": "Monk, infirmarian", "label": "INFIRMARY LOG",
   "quote": "I run the infirmary. Nobody came to see me that night – I was at Compline from ten, and the infirmary was locked.",
   "evidence": ev_table("Infirmary visitors log", ["Date", "Visitor", "Time"], [
       ("Night before", "Br. Martin – headache", "19:30"),
       ("That night", "None – locked 21:50", "–"),
     ])},
  {"name": "Sister Clare", "role": "Visiting nun, guest house", "label": "CLARE'S NOTE",
   "quote": "My window looks onto the cloister. Just after ten I saw a monk with a lantern go into the library and come out ten minutes later with something wrapped in a cloth.",
   "evidence": ev_note("CLARE'S JOURNAL", [
       "About 22:10 – monk with lantern",
       "into library. 22:22 – out again,",
       "parcel under his arm, towards the",
       "chapel. Very fast."],
     "– Sister Clare")},
 ],
 "solution": {"killer": "Brother Felix",
   "motive": "A dealer had offered Felix €200,000 for the Book of Hours (clue 2).",
   "proof": ["Brother Anselm was struck at about 22:15 – his watch stopped at 22:17 (clue 4).",
             "Felix says he was at Compline from 22:00, but his candle wasn't lit until 22:40 (clue 3). He said he came 'from the infirmary', but the infirmary was locked and had no visitors (clue 5).",
             "At 22:10 Sister Clare saw a monk go into the library and leave at 22:22 with a wrapped parcel (clue 6)."],
   "cleared": ["<b>Abbot Gregory</b>, <b>Martin</b> and <b>Thomas</b> lit their candles at 22:00 at Compline (clue 3).",
               "<b>Sister Clare</b> and <b>Dr Reed</b> only report what they found (clues 4, 6)."]},
}

# ---------------------------------------------------------------- SUBMARINE MUSEUM (L3)
sub = {
 "slug": "murder-aboard-the-museum-submarine", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 209", "title_html": "MURDER ABOARD THE<br>MUSEUM SUBMARINE", "title_plain": "Murder Aboard the Museum Submarine",
 "teaser": "A museum curator is found dead inside a historic submarine after a late-night tour. Hatch counters, a torch battery and a tour headcount show who stayed behind.",
 "intro": "At the <b>Portwell Naval Museum</b>, curator Dr Simon Lake was found dead in the torpedo room of the old submarine HMS Thresher after a late-night ghost tour. " + STD,
 "clues": [
  {"name": "DI Ben Okoro", "role": "Police", "label": "POLICE REPORT",
   "quote": "Dr Lake was struck with a heavy brass valve wheel. He was still alive when the ghost tour began – he gave the welcome speech.",
   "evidence": ev_rows("Police report – HMS Thresher", [
       ("Found", "23:40, torpedo room"),
       ("Last seen", "21:30, welcome speech on deck"),
       ("Weapon", "Brass valve wheel, removed from a pipe"),
       ("Torch", "A tour torch lying by the body, still on"),
     ])},
  {"name": "Ava Kent", "role": "Tour guide", "label": "AVA'S STATEMENT",
   "quote": "I led the group through the sub from 21:35 to 22:15 and counted everyone out at the end. Twelve went in, twelve came out.",
   "evidence": ev_rows("Museum board letter", [
       ("To", "Ava Kent"),
       ("From", "Dr S. Lake"),
       ("Text", "“The ghost tours end this month. Your job ends with them.”"),
     ])},
  {"name": "Dan Fry", "role": "Security", "label": "HATCH COUNTER",
   "quote": "The sub has an electronic counter on each hatch for safety – it counts people in and out. Twelve visitors and one guide went in.",
   "evidence": ev_table("Hatch counter – tour night", ["Time", "In", "Out", "Inside"], [
       ("21:35", "13", "0", "13 (12 visitors + guide)"),
       ("21:40", "1", "0", "14 (Dr Lake goes in)"),
       ("22:15", "0", "12", "2"),
       ("22:31", "0", "1", "1"),
     ], mono_cols=(0,))},
  {"name": "Rosie Parks", "role": "Visitor", "label": "VISITOR'S PHOTO",
   "quote": "I took a selfie as we left the sub. I think the guide was still inside – she waved us off from the hatch and said she'd 'lock up'.",
   "evidence": ev_photos("Rosie's phone", [
       ("IMG_4501", "22:15", "Visitors climbing out of the hatch; the guide in a red tour jacket waving from below with a torch."),
     ])},
  {"name": "Gary Hood", "role": "Museum shop", "label": "TORCH LOG",
   "quote": "Each tour torch is numbered. The guide always has torch 1. Visitors get 2 to 13.",
   "evidence": ev_table("Torch sign-out – tour night", ["Torch", "Signed out to", "Returned"], [
       ("1", "A. Kent (guide)", "No – found by the body"),
       ("2–13", "Visitors", "All returned 22:20"),
     ])},
  {"name": "Prof. Iris Bell", "role": "Museum trustee", "label": "IRIS'S STATEMENT",
   "quote": "I argued with Simon about the museum budget that afternoon. But I spent the evening at the trustees' dinner across town – speech and all.",
   "evidence": ev_rows("Trustees' dinner programme", [
       ("Venue", "Harbour Hotel, across town"),
       ("21:00–22:30", "Dinner – Prof. I. Bell, guest speaker at 22:00"),
     ])},
 ],
 "solution": {"killer": "Ava Kent",
   "motive": "Dr Lake was ending the ghost tours and Ava's job (clue 2).",
   "proof": ["Dr Lake went into the sub at 21:40. At 22:15 twelve visitors left, leaving two people inside – the guide and Dr Lake (clue 3).",
             "Ava says everyone came out at 22:15, but Rosie's photo shows her still inside, waving from below (clue 4). One person came out at 22:31, and Dr Lake never did (clue 3).",
             "The guide's own torch, number 1, was found by the body (clues 1, 5)."],
   "cleared": ["<b>Prof. Bell</b> was giving a speech across town at 22:00 (clue 6).",
               "All visitors left at 22:15 and returned their torches (clues 3, 5); <b>Dan</b>, <b>Rosie</b> and <b>Gary</b> only report what they saw."]},
}

MYSTERIES = [garden, charity, abbey, sub]
