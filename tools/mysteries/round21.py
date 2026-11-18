from lib import *  # evidence helpers

# Round 21 (18 Nov): 1 Rookie, 1 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- SCARECROW (L1)
scarecrow = {
 "slug": "the-scarecrow-festival", "level": 1, "crime": "VANDALISM", "who": "vandal", "added": ADDED,
 "caseno": "CASE NO. 146", "title_html": "THE SCARECROW<br>FESTIVAL", "title_plain": "The Scarecrow Festival",
 "teaser": "The favourite scarecrow in the village trail loses its head the night before judging. A trail of straw and a muddy bicycle point the way.",
 "intro": "In the village of <b>Little Haddow</b>, the scarecrow trail is judged on Sunday morning. Overnight, the favourite – 'Farmer Fred' outside the bakery – had its head pulled off and thrown in the pond. " + STD,
 "clues": [
  {"name": "Bella Croft", "role": "Baker, Fred's maker", "label": "DAMAGE REPORT",
   "quote": "Fred was perfect when I locked the bakery at nine on Saturday night. At six on Sunday morning his pumpkin head was floating in the pond.",
   "evidence": ev_rows("Festival committee – damage report", [
       ("Last seen whole", "Saturday 21:00"),
       ("Found", "Sunday 06:00, head in the village pond"),
       ("At the scene", "A trail of straw and narrow bicycle tyre tracks in the mud"),
       ("Prize", "Best Scarecrow: trophy and £75"),
     ])},
  {"name": "Roger Pinn", "role": "Rival scarecrow maker", "label": "ROGER'S STATEMENT",
   "quote": "My 'Space Scarecrow' was always going to win. I was home in bed by ten and didn't go out again – I don't even own a bicycle any more.",
   "evidence": ev_rows("Best Scarecrow – last two years", [
       ("2024", "1st Bella Croft · 2nd Roger Pinn"),
       ("2025", "1st Bella Croft · 2nd Roger Pinn"),
       ("Note", "Roger complained the judges 'always pick the bakery'"),
     ])},
  {"name": "Hal Morgan", "role": "Bike shop owner", "label": "BIKE REPAIR BOOK",
   "quote": "I only sell racing bikes with narrow tyres to a few people round here. One of them brought his in on Monday for a new chain.",
   "evidence": ev_table("Morgan's Cycles – repair book", ["Date", "Customer", "Bike", "Job"], [
       ("Thu", "J. Tate", "Mountain bike, wide tyres", "Puncture"),
       ("Mon", "R. Pinn", "Racing bike, narrow tyres", "New chain – mud and straw in the gears"),
     ])},
  {"name": "Jenny Tate", "role": "Pub landlady", "label": "PUB TILL",
   "quote": "I was serving at The Plough until gone midnight on Saturday. Bella came in for one drink after she locked up and stayed till closing.",
   "evidence": ev_table("The Plough – Saturday", ["Time", "Order", "Customer"], [
       ("21:15", "Half of cider", "B. Croft"),
       ("22:40", "Lemonade", "B. Croft"),
       ("23:55", "Last orders", "–"),
     ], mono_cols=(0,))},
  {"name": "Pip Lowe", "role": "Night-shift nurse", "label": "PIP'S NOTE",
   "quote": "I drive home from the hospital at about one in the morning. On Sunday I passed someone cycling away from the pond with no lights on.",
   "evidence": ev_note("PIP'S NOTE TO THE COMMITTEE", [
       "About 01:10, Pond Lane:",
       "man on a thin racing bike, no lights,",
       "wearing a silver 'Space Scarecrow'",
       "T-shirt. Cycled off towards Mill Row."],
     "– Pip")},
  {"name": "Mr Owen Shaw", "role": "Committee chair", "label": "ADDRESS LIST",
   "quote": "We printed T-shirts for each scarecrow team this year. Every maker got one with their scarecrow's name on it.",
   "evidence": ev_table("Scarecrow trail – makers", ["Scarecrow", "Maker", "Address"], [
       ("Farmer Fred", "Bella Croft", "The Bakery, High St"),
       ("Space Scarecrow", "Roger Pinn", "4 Mill Row"),
       ("Pirate Pete", "Jenny Tate", "The Plough"),
     ])},
 ],
 "solution": {"killer": "Roger Pinn",
   "motive": "Roger had come second to Bella two years running and wanted the trophy and £75 (clues 1, 2).",
   "proof": ["Fred was wrecked overnight, and narrow bicycle tracks were left in the mud (clue 1).",
             "Roger says he has no bicycle, but on Monday he brought in a narrow-tyred racing bike with mud and straw in the gears (clue 3).",
             "At 01:10 Pip saw a man on a thin racing bike in a 'Space Scarecrow' T-shirt riding towards Mill Row (clue 5) – Roger's scarecrow and Roger's street (clue 6)."],
   "cleared": ["<b>Bella</b> was in the pub until closing (clue 4).",
               "<b>Jenny</b> was serving at The Plough and rides a wide-tyred mountain bike (clues 3, 4).",
               "<b>Hal</b>, <b>Pip</b> and <b>Mr Shaw</b> only report what they know."]},
}

# ---------------------------------------------------------------- CYCLE SPORTIVE (L2)
sportive = {
 "slug": "the-cycle-race-sabotage", "level": 2, "crime": "SABOTAGE", "who": "saboteur", "added": ADDED,
 "caseno": "CASE NO. 147", "title_html": "THE CYCLE RACE<br>SABOTAGE", "title_plain": "The Cycle Race Sabotage",
 "teaser": "The race favourite's brake cable snaps on the first descent. Someone cut it in the team tent – and one rival's alibi is a little too well timed.",
 "intro": "At the <b>Dales Classic</b> amateur cycle race, favourite Tessa Hart crashed on the first descent when her front brake cable snapped. The mechanic found it had been cut almost through. " + STD,
 "clues": [
  {"name": "Tessa Hart", "role": "Cyclist", "label": "RACE REPORT",
   "quote": "My bike was checked at eight and then left in the team tent while I warmed up on the rollers outside. I started at nine and crashed at twenty past.",
   "evidence": ev_rows("Race report", [
       ("Bike checked", "08:00 by the team mechanic – brakes perfect"),
       ("In the tent alone", "08:05–08:50"),
       ("Crash", "09:20, first descent – front brake cable cut 9/10 through"),
       ("Tool", "Small cable cutters with blue handles found under the tent flap"),
     ])},
  {"name": "Mia Lund", "role": "Rival cyclist", "label": "MIA'S STATEMENT",
   "quote": "I was in the queue for the toilets and then at the sign-on desk from eight until half past. You can check – I signed on at twenty past eight.",
   "evidence": ev_rows("Series standings before the Dales Classic", [
       ("1", "T. Hart – 210 pts"),
       ("2", "M. Lund – 198 pts"),
       ("Prize", "Series winner: a pro team trial contract"),
     ])},
  {"name": "Gus Ward", "role": "Sign-on marshal", "label": "SIGN-ON SHEET",
   "quote": "Riders sign on and collect their race numbers at my desk. Some send a team-mate to collect for them – that's allowed if they bring the licence.",
   "evidence": ev_table("Sign-on desk", ["Time", "Rider", "Collected by"], [
       ("08:12", "T. Hart", "T. Hart"),
       ("08:20", "M. Lund", "S. Lund (sister) – with licence"),
       ("08:31", "R. Kaye", "R. Kaye"),
     ], mono_cols=(0,))},
  {"name": "Sara Lund", "role": "Mia's sister", "label": "SARA'S NOTE",
   "quote": "Mia asked me to collect her number because she was 'busy'. I didn't think anything of it.",
   "evidence": ev_note("SARA'S TEXT MESSAGES", [
       "08:06 Mia: Can you sign me on? Licence in",
       "my bag. I'm busy for a bit.",
       "08:44 Mia: Thanks sis. Did anyone see",
       "me near the Hart tent? lol jk"],
     "– Sara's phone")},
  {"name": "Ray Kaye", "role": "Team mechanic", "label": "TOOL LIST",
   "quote": "Those blue cutters aren't ours – our team's tools all have red handles. Every team's toolkit is a different colour so they don't get mixed up.",
   "evidence": ev_table("Team toolkits", ["Team", "Handle colour"], [
       ("Hart Racing", "Red"),
       ("Lund Cycling", "Blue"),
       ("Kaye Velo", "Yellow"),
     ])},
  {"name": "Olly Price", "role": "Photographer", "label": "WARM-UP PHOTO",
   "quote": "I photographed the riders warming up. Tessa was on her rollers outside her tent the whole time.",
   "evidence": ev_photos("Olly's camera", [
       ("DSC_2201", "08:25", "Tessa Hart on rollers outside the Hart Racing tent. Behind her, the tent flap is open – someone in a blue Lund Cycling jacket is inside, bent over a bike."),
     ])},
 ],
 "solution": {"killer": "Mia Lund",
   "motive": "Mia was second in the series, 12 points behind Tessa, with a pro team trial at stake (clue 2).",
   "proof": ["The cable was cut between 08:05 and 08:50 while the bike stood in the tent (clue 1).",
             "Mia says she signed on at 08:20, but her sister collected her number for her (clue 3) because Mia was 'busy' (clue 4).",
             "The blue cutters are Lund Cycling's colour (clue 5), and at 08:25 someone in a blue Lund Cycling jacket was inside the Hart tent bent over a bike (clue 6)."],
   "cleared": ["<b>Sara</b> was at the sign-on desk at 08:20 (clue 3).",
               "<b>Tessa</b> was warming up outside (clue 6), and <b>Ray</b> signed on at 08:31 and uses yellow tools (clues 3, 5).",
               "<b>Gus</b> and <b>Olly</b> were at the desk and behind the camera."]},
}

# ---------------------------------------------------------------- TRUFFLE HUNT (L3)
truffle = {
 "slug": "death-at-the-truffle-hunt", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 148", "title_html": "DEATH AT THE<br>TRUFFLE HUNT", "title_plain": "Death at the Truffle Hunt",
 "teaser": "A truffle dealer is found dead in an oak wood during a hunt. The dogs' GPS collars recorded every step – including the one handler who wasn't with his dog.",
 "intro": "In the hills above <b>Alba</b>, truffle dealer Marco Bellini was found dead in the Bosco Nero oak wood during a guided truffle hunt for wealthy guests. " + STD,
 "clues": [
  {"name": "Ispettore Lucia Ferri", "role": "Police", "label": "POLICE REPORT",
   "quote": "Signor Bellini was struck with a truffle spade near the old well. His phone shows he was sending a message at 10:31, so he died after that. He was found at 11:00.",
   "evidence": ev_rows("Police report – Bosco Nero", [
       ("Found", "11:00, by the old well"),
       ("Last message sent", "10:31, from his phone"),
       ("Weapon", "A truffle spade (vanghetto) – every hunter carries one"),
       ("Well", "Northern edge of the wood, 600 m from the clearing"),
     ])},
  {"name": "Paolo Conti", "role": "Truffle hunter", "label": "DOG GPS LOG",
   "quote": "I was with my dog Bianca the whole morning, on the southern slope. A truffle hunter never leaves his dog – it's the first rule.",
   "evidence": ev_table("GPS collars – 10:15 to 10:50", ["Dog", "Handler", "Location"], [
       ("Bianca", "P. Conti", "Tied to an oak in the clearing, 10:20–10:48 – no movement"),
       ("Tartufo", "G. Neri", "Southern slope, moving with handler"),
       ("Luna", "A. Ricci", "Eastern edge, moving with handler"),
     ])},
  {"name": "Giulia Neri", "role": "Truffle hunter", "label": "BELLINI'S MESSAGES",
   "quote": "I was on the southern slope with Tartufo and the guests the whole time. If Paolo had been there, I'd have seen him – he wasn't.",
   "evidence": ev_note("BELLINI'S LAST MESSAGES", [
       "10:29 to P. Conti: Meet me at the well.",
       "Bring the money you owe me or I go to",
       "the carabinieri about the fake truffles.",
       "10:31 to P. Conti: I'm waiting."],
     "– from Bellini's phone")},
  {"name": "Anna Ricci", "role": "Truffle hunter", "label": "TRUFFLE REPORT",
   "quote": "Marco was a hard man to deal with. He told me last week he'd found someone selling Chinese truffles as Alba white truffles.",
   "evidence": ev_rows("Laboratory test, ordered by Bellini", [
       ("Sample", "Truffles bought from P. Conti, October"),
       ("Result", "Tuber indicum (cheap Chinese truffle), not Alba white"),
       ("Value difference", "About €18,000"),
     ])},
  {"name": "Mr James Holt", "role": "Guest", "label": "GUEST PHOTOS",
   "quote": "I paid a fortune for this hunt and spent half of it watching other people dig. I took a lot of photos.",
   "evidence": ev_photos("James Holt's phone", [
       ("IMG_7701", "10:24", "The clearing: a white dog (Bianca) tied to an oak, nobody with her."),
       ("IMG_7712", "10:41", "Southern slope: Giulia Neri and her dog Tartufo digging with the guests."),
     ])},
  {"name": "Elena Bassi", "role": "Hunt organiser", "label": "PAOLO'S BOOTS",
   "quote": "When Paolo came back to the clearing at ten to eleven, his boots were covered in the red clay you only get up by the old well.",
   "evidence": ev_rows("Soil check – police lab", [
       ("Paolo Conti's boots", "Red iron-rich clay"),
       ("Clay found", "Only around the old well on the northern edge"),
       ("Southern slope", "Pale chalky soil"),
     ])},
 ],
 "solution": {"killer": "Paolo Conti",
   "motive": "Bellini had proved Paolo sold him cheap Chinese truffles as Alba whites – about €18,000 – and threatened to go to the carabinieri (clues 3, 4).",
   "proof": ["Bellini was alive at 10:31 and found by the well at 11:00 (clue 1). At 10:29 he told Paolo to meet him at the well (clue 3).",
             "Paolo says he never left his dog on the southern slope. But Bianca's GPS collar shows her tied in the clearing, not moving, from 10:20 to 10:48 (clue 2), and a photo at 10:24 shows her alone (clue 5).",
             "When Paolo returned at 10:50 his boots carried the red clay found only around the well (clue 6)."],
   "cleared": ["<b>Giulia</b> was on the southern slope with Tartufo and the guests (clues 2, 5).",
               "<b>Anna</b> was moving with Luna on the eastern edge (clue 2).",
               "<b>Mr Holt</b> was taking photos with the group, and <b>Elena</b> ran the hunt from the clearing."]},
}

# ---------------------------------------------------------------- FILM SET (L3)
filmset = {
 "slug": "murder-on-the-film-set", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 149", "title_html": "MURDER ON THE<br>FILM SET", "title_plain": "Murder on the Film Set",
 "teaser": "A film director dies in his trailer between takes. The continuity notes, the clapperboard and a costume change prove who wasn't where they said.",
 "intro": "On the set of the period drama <b>“The Winter Palace”</b>, director Simon Vale was found dead in his trailer during a break in filming. " + STD,
 "clues": [
  {"name": "DI Grace Obi", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Vale was poisoned – something in the coffee on his trailer table. Somebody slipped it in after the runner brought it.",
   "evidence": ev_rows("Police report – Stage 4 backlot", [
       ("Found", "15:05, director's trailer"),
       ("Cause", "Poison in a coffee cup on his table"),
       ("Coffee", "Delivered by a runner at 14:05; Vale was on the phone until 14:10 and let it cool"),
       ("Poison drunk", "Between 14:10 and 14:25 (pathologist)"),
     ])},
  {"name": "Lena Frost", "role": "Lead actress", "label": "LENA'S STATEMENT",
   "quote": "I was on set filming the ballroom scene from two o'clock until half past. You'll see me in every take – the gold ballgown is hard to miss.",
   "evidence": ev_rows("Lena Frost – contract", [
       ("Fee", "£400,000"),
       ("Clause 12", "Director may recast the lead within the first two weeks"),
       ("Vale's note, Monday", "“Recasting Lena. Will tell her Friday.”"),
     ])},
  {"name": "Max Cole", "role": "Clapper loader", "label": "CLAPPERBOARD LOG",
   "quote": "I mark every take with the clapperboard and note the time. The ballroom scene had a short break while they changed the lighting.",
   "evidence": ev_table("Camera log – Stage 4", ["Take", "Clap", "Scene"], [
       ("12", "14:01", "Ballroom – wide"),
       ("13", "14:03", "Ballroom – wide"),
       ("—", "14:04–14:18", "Lighting change, actors released"),
       ("14", "14:19", "Ballroom – close-ups"),
     ], mono_cols=(1,))},
  {"name": "Ruby Shah", "role": "Continuity supervisor", "label": "CONTINUITY NOTES",
   "quote": "My job is to make sure everything matches between takes. Something didn't, and I wrote it down.",
   "evidence": ev_note("CONTINUITY NOTES – BALLROOM", [
       "Take 14 (14:19): Lena's left glove",
       "is now on inside out, and there is mud",
       "on the hem of the gold gown. Neither",
       "in take 13. Fixed before take 15."],
     "– Ruby")},
  {"name": "Tom Reed", "role": "Runner", "label": "COFFEE DELIVERIES",
   "quote": "I took Mr Vale his coffee at five past two, like always. He was on the phone, so I put it on his table and left – he always lets it cool first. Then I went back for the next order.",
   "evidence": ev_table("Runner's deliveries", ["Time", "To", "Order"], [
       ("14:05", "S. Vale – trailer", "Black coffee, no sugar"),
       ("14:08", "Make-up truck", "3 teas"),
       ("14:12", "Lena Frost – trailer (next to Vale's)", "Hot water with lemon"),
     ], mono_cols=(0,))},
  {"name": "Kit Baron", "role": "Producer", "label": "TRAILER PARK CAMERA",
   "quote": "Simon and I argued about the budget all week, but I was in the production office on a call to Los Angeles from two until half past.",
   "evidence": ev_photos("Trailer park camera", [
       ("CAM-1", "14:07", "A woman in a long gold ballgown crosses the muddy trailer park to the director's trailer."),
       ("CAM-1", "14:10", "The same woman goes into the trailer next door."),
       ("CAM-1", "14:15", "Through the production office window: K. Baron on the phone."),
     ])},
 ],
 "solution": {"killer": "Lena Frost",
   "motive": "Vale was about to recast her and tell her on Friday – costing her a £400,000 role (clue 2).",
   "proof": ["The coffee was left on Vale's table at 14:05 and he drank it after 14:10, so the poison went in between 14:05 and 14:10 (clues 1, 5).",
             "Lena says she was filming from 14:00 to 14:30. But between 14:04 and 14:18 filming stopped for a lighting change and the actors were released (clue 3).",
             "At 14:07 a woman in a long gold ballgown crossed the muddy trailer park to Vale's trailer (clue 6). In take 14 Lena's glove was inside out and her gold gown had mud on the hem (clue 4)."],
   "cleared": ["<b>Kit</b> argued with Vale but is seen on the phone in the production office (clue 6).",
               "<b>Tom</b> delivered drinks to the make-up truck at 14:08 and Lena's trailer at 14:12 (clue 5); <b>Max</b> and <b>Ruby</b> stayed on set (clues 3, 4).",
               "<b>DI Obi</b> only investigated."]},
}

MYSTERIES = [scarecrow, sportive, truffle, filmset]
