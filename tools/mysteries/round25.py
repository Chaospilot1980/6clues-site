from lib import *  # evidence helpers

# Round 25 (18 Nov): 1 Rookie, 1 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- GOLDFISH (L1)
goldfish = {
 "slug": "the-funfair-goldfish", "level": 1, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 162", "title_html": "THE FUNFAIR<br>GOLDFISH", "title_plain": "The Funfair Goldfish",
 "teaser": "The prize goldfish tank at the funfair is found empty one morning. Wet footprints, a fishing net and a very full bath tell the tale.",
 "intro": "At the <b>Shoreham Summer Funfair</b>, all twelve prize goldfish vanished from the hook-a-duck stall overnight. Luckily, the fish turned up safe – but who took them? " + STD,
 "clues": [
  {"name": "Rosie Cole", "role": "Hook-a-duck stall owner", "label": "STALL REPORT",
   "quote": "I counted the goldfish at ten when the fair closed – twelve, all happy. At eight in the morning, the tank was empty and there were wet footprints leading out of the tent.",
   "evidence": ev_rows("Stall report", [
       ("Last counted", "22:00 – 12 goldfish"),
       ("Found empty", "08:00"),
       ("At the scene", "Wet footprints in wellington boots, size 9"),
       ("Missing", "Rosie's long-handled fishing net"),
     ])},
  {"name": "Nick Hart", "role": "Dodgems operator", "label": "NICK'S STATEMENT",
   "quote": "Goldfish? I don't even like goldfish. I was asleep in my caravan from half ten until seven. Never left.",
   "evidence": ev_rows("Fairground complaint book", [
       ("Complaint from N. Hart", "“Giving away goldfish as prizes is cruel. Somebody should rescue them.”"),
       ("Date", "Last Tuesday"),
     ])},
  {"name": "Pat Rowe", "role": "Night security", "label": "SECURITY ROUND",
   "quote": "I walk round the fair every hour. At about two in the morning I saw someone in wellies carrying a big bucket towards the caravans.",
   "evidence": ev_table("Security rounds", ["Time", "Note"], [
       ("00:00", "All quiet"),
       ("01:00", "All quiet"),
       ("02:05", "Person in green wellies with a heavy bucket and a net, heading to the caravan field"),
       ("03:00", "All quiet"),
     ], mono_cols=(0,))},
  {"name": "Mo Diaz", "role": "Candyfloss seller", "label": "WELLIES LIST",
   "quote": "It rained all week, so we all bought wellies from the same shop in town. I've got the receipt for the fair's bulk order.",
   "evidence": ev_table("Bulk wellies order", ["Name", "Colour", "Size"], [
       ("N. Hart", "Green", "9"),
       ("R. Cole", "Red", "5"),
       ("M. Diaz", "Yellow", "7"),
     ])},
  {"name": "Sal Grant", "role": "Fairground manager", "label": "CARAVAN CHECK",
   "quote": "When we searched the caravans at nine, one of them had a very full bath – and twelve goldfish swimming in it.",
   "evidence": ev_rows("Caravan search", [
       ("Caravan 3", "Bath full of water with 12 goldfish"),
       ("Also inside", "Rosie's fishing net, still wet"),
       ("Caravan 3 belongs to", "N. Hart"),
     ])},
  {"name": "Jo Lake", "role": "Ghost-train operator", "label": "JO'S NOTE",
   "quote": "I share the caravan field with Nick. I woke up about ten past two because someone was running a bath. At two in the morning!",
   "evidence": ev_note("JO'S NOTE FOR SAL", [
       "02:10 – woke up to taps running",
       "in the caravan next door (no. 3)",
       "for about ten minutes. Then quiet."],
     "– Jo, caravan 4")},
 ],
 "solution": {"killer": "Nick Hart",
   "motive": "Nick thought giving goldfish as prizes was cruel and wanted to 'rescue' them (clue 2).",
   "proof": ["The fish were taken between 22:00 and 08:00, leaving size-9 welly prints, and Rosie's net was missing (clue 1).",
             "Nick says he never left his caravan, but at 02:05 security saw someone in green wellies carrying a bucket and net to the caravans (clue 3). Nick's wellies are green, size 9 (clue 4).",
             "At 02:10 Jo heard a bath running in caravan 3 (clue 6), and the goldfish and Rosie's net were found in Nick's bath (clue 5)."],
   "cleared": ["<b>Rosie</b> and <b>Mo</b> have red and yellow wellies in smaller sizes (clue 4).",
               "<b>Pat</b>, <b>Sal</b> and <b>Jo</b> only report what they saw or found."]},
}

# ---------------------------------------------------------------- WEDDING DRESS (L2)
dress = {
 "slug": "the-ruined-wedding-dress", "level": 2, "crime": "SABOTAGE", "who": "saboteur", "added": ADDED,
 "caseno": "CASE NO. 163", "title_html": "THE RUINED<br>WEDDING DRESS", "title_plain": "The Ruined Wedding Dress",
 "teaser": "The night before the wedding, red wine is poured all over the bride's dress. The bridal suite was locked – but someone knew where the spare key lived.",
 "intro": "At the <b>Hollin Hall Hotel</b>, bride-to-be Amy Fenwick found her wedding dress soaked in red wine on the morning of her wedding. " + STD,
 "clues": [
  {"name": "Amy Fenwick", "role": "Bride", "label": "BRIDE'S REPORT",
   "quote": "The dress was hanging in the bridal suite when I locked it at eleven and went to the hen party in the bar. At midnight I came back and it was ruined.",
   "evidence": ev_rows("Hotel incident report", [
       ("Suite locked", "23:00 by Amy"),
       ("Found", "00:05"),
       ("Damage", "Dress soaked in red wine – a bottle of Rioja left on the floor"),
       ("Door", "Not forced – opened with a key"),
     ])},
  {"name": "Kirsty Fenwick", "role": "Bride's sister", "label": "KIRSTY'S STATEMENT",
   "quote": "I was at the hen party in the bar all evening – everyone saw me dancing. I'd never hurt Amy's big day.",
   "evidence": ev_rows("Family background", [
       ("Groom Tom", "Was engaged to Kirsty until two years ago"),
       ("Kirsty, last week", "“She stole him. I hope it rains.”"),
     ])},
  {"name": "Gail Price", "role": "Hotel receptionist", "label": "KEY DESK LOG",
   "quote": "The bridal suite has two keys. Amy had one; the spare lives behind my desk. Someone asked for it at half eleven, saying they were the bride's sister and needed the veil.",
   "evidence": ev_table("Reception key log", ["Time", "Key", "Given to"], [
       ("23:30", "Bridal suite (spare)", "Woman who said she was the bride's sister"),
       ("23:42", "Bridal suite (spare)", "Returned"),
     ], mono_cols=(0,))},
  {"name": "Jade Holt", "role": "Bridesmaid", "label": "HEN PARTY PHOTOS",
   "quote": "I took photos all night. I noticed one person disappeared for a while after the cake.",
   "evidence": ev_photos("Jade's phone", [
       ("IMG_501", "23:15", "Hen party in the bar: Amy, Kirsty, Jade and Aunt Sue cutting a cake."),
       ("IMG_514", "23:35", "Hen party dancing: Amy, Jade and Aunt Sue. Kirsty is not in the room."),
       ("IMG_522", "23:50", "Kirsty back, with a red wine stain on her white sleeve."),
     ])},
  {"name": "Aunt Sue", "role": "Groom's aunt", "label": "BAR TILL",
   "quote": "I bought the drinks all night. Only one person ordered a whole bottle of red – everyone else was on prosecco.",
   "evidence": ev_table("Hotel bar – Friday", ["Time", "Order", "Signed to"], [
       ("22:30", "Prosecco x 6", "Aunt Sue"),
       ("23:20", "Bottle of Rioja – 'to take upstairs'", "K. Fenwick"),
       ("23:55", "Prosecco x 4", "Aunt Sue"),
     ], mono_cols=(0,))},
  {"name": "Ben Ross", "role": "Night porter", "label": "PORTER'S NOTE",
   "quote": "I was on the first floor at twenty to midnight and saw someone come out of the bridal suite in a hurry. Long dark hair, sparkly 'Sister of the Bride' sash.",
   "evidence": ev_note("PORTER'S NIGHT LOG", [
       "23:40 – woman leaving bridal suite,",
       "pink sash: 'SISTER OF THE BRIDE'.",
       "Took the back stairs down to the bar."],
     "– Ben, night porter")},
 ],
 "solution": {"killer": "Kirsty Fenwick",
   "motive": "Kirsty had been engaged to the groom and said she hoped it would rain on Amy's wedding (clue 2).",
   "proof": ["The dress was ruined between 23:00 and 00:05 with a bottle of Rioja, using a key (clue 1).",
             "Kirsty says she never left the hen party, but she's missing from the 23:35 photo and comes back at 23:50 with red wine on her sleeve (clue 4).",
             "She ordered the only bottle of Rioja at 23:20 (clue 5). At 23:30 a woman claiming to be the bride's sister took the spare key (clue 3), and at 23:40 the porter saw a woman in a 'Sister of the Bride' sash leave the suite (clue 6)."],
   "cleared": ["<b>Amy</b>, <b>Jade</b> and <b>Aunt Sue</b> are all in the 23:35 photo at the party (clue 4).",
               "<b>Gail</b> was at the reception desk and <b>Ben</b> on his rounds."]},
}

# ---------------------------------------------------------------- GHOST WALK (L3)
ghostwalk = {
 "slug": "death-on-the-ghost-walk", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 164", "title_html": "DEATH ON THE<br>GHOST WALK", "title_plain": "Death on the Ghost Walk",
 "teaser": "A ghost-walk guide is found dead in a dark alley halfway through his tour. Twenty tourists swear nobody left the group – but the church clock disagrees.",
 "intro": "In the old city of <b>York</b>, ghost-walk guide Edgar Penn was found dead in Mad Alice Lane during his 'Midnight Spirits' tour. " + STD,
 "clues": [
  {"name": "DI Rachel Stone", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Penn was struck in the alley while his tour group waited in the square around the corner. He'd gone ahead 'to set up a surprise'. His pocket watch broke as he fell.",
   "evidence": ev_rows("Police report – Mad Alice Lane", [
       ("Found", "21:50, by a tourist"),
       ("Watch", "Stopped at 21:32"),
       ("Alley", "Two minutes' walk from St Helen's Square"),
       ("Note", "Penn left the group at 21:25 to 'set up the next ghost'"),
     ])},
  {"name": "Simon Crake", "role": "Rival ghost-walk guide", "label": "SIMON'S STATEMENT",
   "quote": "I was running my own tour on the other side of town. At half past nine I was at the Shambles telling my group about the headless butcher.",
   "evidence": ev_rows("York ghost tours – licence dispute", [
       ("Penn's complaint", "Accused Crake of copying his stories word for word"),
       ("Council hearing", "Monday – Crake could lose his tour licence"),
       ("Crake's reply", "“Penn won't be at any hearing.”"),
     ])},
  {"name": "Martha Lee", "role": "Penn's assistant", "label": "TOUR TIMETABLE",
   "quote": "I stayed with the tourists in St Helen's Square. Edgar's 'surprise' was always me jumping out in a sheet – but tonight he went ahead himself, which was strange.",
   "evidence": ev_programme("Midnight Spirits tour – stops", "Penn's tours", [
       ("21:00", "Start – Minster steps"),
       ("21:20", "St Helen's Square"),
       ("21:35", "Mad Alice Lane – 'the surprise'"),
       ("22:00", "Finish – Golden Fleece pub"),
     ], None)},
  {"name": "Hugo Lind", "role": "Tourist on Crake's tour", "label": "HUGO'S VIDEO",
   "quote": "I filmed the whole of Mr Crake's tour on my phone. At the Shambles he said, 'Wait here, I'll fetch the lantern', and was gone for ages.",
   "evidence": ev_table("Hugo's videos – Crake tour", ["File", "Time", "What it shows"], [
       ("VID_11", "21:15", "Crake at the Shambles, telling the butcher story"),
       ("VID_12", "21:24", "Crake: 'Wait here, I'll fetch the lantern' – walks off"),
       ("VID_13", "21:41", "Crake comes back, out of breath, no lantern"),
     ], mono_cols=(1,))},
  {"name": "Father Paul", "role": "Priest at St Helen's", "label": "CHURCH CAMERA",
   "quote": "Our church camera looks down the lane beside the square. I've given the footage to the police.",
   "evidence": ev_photos("St Helen's church camera", [
       ("CAM-1", "21:29", "A man in a long black cape and top hat – Crake's tour costume – hurries towards Mad Alice Lane."),
       ("CAM-1", "21:34", "The same man hurries back towards the Shambles."),
     ])},
  {"name": "Nell Fry", "role": "Penn's ex-wife", "label": "PUB TILL",
   "quote": "Edgar and I fought for years about the business, but I was behind the bar of the Golden Fleece all evening waiting for his tour to arrive.",
   "evidence": ev_table("Golden Fleece – till", ["Time", "Served by"], [
       ("21:18", "N. Fry"),
       ("21:31", "N. Fry"),
       ("21:44", "N. Fry"),
     ], mono_cols=(0,))},
 ],
 "solution": {"killer": "Simon Crake",
   "motive": "Penn's complaint could cost Crake his tour licence at Monday's hearing, and he said Penn 'won't be at any hearing' (clue 2).",
   "proof": ["Penn died at 21:32 in Mad Alice Lane (clue 1).",
             "Crake says he was at the Shambles with his group at half past nine. But Hugo's video shows him leaving at 21:24 'for a lantern' and returning at 21:41, out of breath and without one (clue 4).",
             "At 21:29 the church camera shows a man in Crake's cape and top hat hurrying to Mad Alice Lane, and at 21:34 hurrying back (clue 5)."],
   "cleared": ["<b>Martha</b> stayed with the tourists in St Helen's Square (clues 1, 3).",
               "<b>Nell</b> was serving at the Golden Fleece at 21:31 (clue 6); <b>Hugo</b> and <b>Father Paul</b> only supplied footage."]},
}

# ---------------------------------------------------------------- CRICKET PAVILION (L3)
cricket = {
 "slug": "murder-at-the-cricket-pavilion", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 165", "title_html": "MURDER AT THE<br>CRICKET PAVILION", "title_plain": "Murder at the Cricket Pavilion",
 "teaser": "The club treasurer dies in the pavilion during the village cricket final. The scorebook says one batsman never left the crease – the scorer knows better.",
 "intro": "At <b>Upper Wyfold Cricket Club</b>, treasurer Gerald Banks was found dead in the pavilion office during the final of the village cup. " + STD,
 "clues": [
  {"name": "DS Lucy Hart", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Banks was hit with a cricket bat in the office. He'd been on the phone to the bank, and the call cut off when he was struck.",
   "evidence": ev_rows("Police report – Upper Wyfold CC", [
       ("Found", "16:30, pavilion office"),
       ("Phone call to bank", "Cut off at 15:42"),
       ("Weapon", "A bat from the home team's kit bags in the changing room"),
       ("Note", "Banks had told the committee he'd 'found something rotten in the accounts'"),
     ])},
  {"name": "Rupert Hale", "role": "Club captain", "label": "RUPERT'S STATEMENT",
   "quote": "I was batting from twenty past three until we won at ten to five. I never left the crease – it's all in the scorebook.",
   "evidence": ev_rows("Club accounts – Banks's notes", [
       ("Missing", "£11,500 from the pavilion fund"),
       ("Payments to", "'R.H. Groundworks' – no such company"),
       ("Cheques signed by", "R. Hale (captain and co-signatory)"),
     ])},
  {"name": "Edie Clark", "role": "Club scorer", "label": "SCOREBOOK",
   "quote": "Rupert was batting, yes – but at the tea interval he went off. The scorebook shows the break.",
   "evidence": ev_table("Scorebook – home innings", ["Time", "Event"], [
       ("15:20", "R. Hale comes in to bat"),
       ("15:35", "Rain – players off, covers on"),
       ("15:55", "Play resumes – R. Hale and J. Moss batting"),
       ("16:50", "Upper Wyfold win by 2 wickets"),
     ], mono_cols=(0,))},
  {"name": "Jack Moss", "role": "Batsman", "label": "RAIN BREAK PHOTO",
   "quote": "When the rain came, most of us sat in the tea tent with a cuppa. Rupert said he needed the loo in the pavilion – he was ages.",
   "evidence": ev_photos("Club photographer", [
       ("IMG_330", "15:40", "Tea tent during the rain: Jack Moss, Edie Clark and the visiting team. Rupert Hale is not there."),
     ])},
  {"name": "Ted Grimes", "role": "Groundsman", "label": "MUDDY PRINTS",
   "quote": "I covered the pitch in the rain, then checked the pavilion. There were muddy spike marks from cricket boots all the way to the office door.",
   "evidence": ev_rows("Groundsman's note", [
       ("Prints", "Batting spikes, size 11, muddy – from the side door to the office"),
       ("Batsmen in spikes during the rain break", "R. Hale, J. Moss"),
       ("J. Moss's boots", "Size 8"),
     ])},
  {"name": "Vera Banks", "role": "Gerald's widow", "label": "BANK CALL",
   "quote": "Gerald rang me from the office at half three to say he'd found the proof and would phone the bank. He sounded frightened.",
   "evidence": ev_note("BANK'S CALL RECORDING – TRANSCRIPT", [
       "15:41 Banks: The payments to R.H. Groundworks –",
       "I believe someone at the club has been...",
       "Who's that? Why aren't you on the pitch –",
       "15:42 [call ends]"],
     "– Northern Bank")},
 ],
 "solution": {"killer": "Rupert Hale",
   "motive": "Gerald had found that £11,500 was paid to a fake company on cheques Rupert signed (clue 2).",
   "proof": ["Gerald was struck at 15:42 while on the phone to the bank (clue 1).",
             "Rupert says he never left the crease from 15:20. But play stopped for rain from 15:35 to 15:55 (clue 3), and he was missing from the tea tent at 15:40 (clue 4).",
             "Size-11 batting spikes left muddy prints to the office door; only Rupert and Jack wore spikes, and Jack's are size 8 (clue 5). On the bank recording Gerald asks his attacker why they aren't 'on the pitch' – a player (clue 6)."],
   "cleared": ["<b>Jack</b> and <b>Edie</b> were in the tea tent at 15:40, and Jack's boots are size 8 (clues 4, 5).",
               "<b>Ted</b> was covering the pitch, and <b>Vera</b> was at home on the phone (clues 5, 6)."]},
}

MYSTERIES = [goldfish, dress, ghostwalk, cricket]
