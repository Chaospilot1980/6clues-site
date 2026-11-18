from lib import *  # evidence helpers

# Round 39 (18 Nov): 2 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- PARCEL (L2)
parcel = {
 "slug": "the-missing-christmas-parcels", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 218", "title_html": "THE MISSING<br>CHRISTMAS PARCELS", "title_plain": "The Missing Christmas Parcels",
 "teaser": "Christmas parcels keep vanishing from one village delivery round. A van's GPS, a doorbell camera and an online shop unmask the thief.",
 "intro": "In <b>Little Haddon</b>, twelve families reported Christmas parcels marked 'delivered' that never arrived. All were on the same delivery round. " + STD,
 "clues": [
  {"name": "Mrs Jan Booth", "role": "Village resident", "label": "COMPLAINTS",
   "quote": "My parcel said 'delivered at 10:42, left in porch'. I was home all day – nobody came to my door.",
   "evidence": ev_table("Missing parcels – December", ["House", "Marked delivered", "Item"], [
       ("Mrs Booth, No. 3", "10:42", "Headphones"),
       ("Mr Ali, No. 9", "10:51", "Smartwatch"),
       ("The Kemps, No. 14", "11:03", "Games console"),
     ], note="All on Round 7.")},
  {"name": "Darren Cole", "role": "Delivery driver, Round 7", "label": "DARREN'S STATEMENT",
   "quote": "I delivered every parcel – someone must be stealing them from porches. I'm in and out of the van all morning.",
   "evidence": ev_table("Van GPS – Round 7, 4 Dec", ["Time", "Van location"], [
       ("10:30", "Little Haddon village centre"),
       ("10:40–11:10", "Parked in Mill Lane lay-by, 1 km outside village"),
       ("11:15", "Back in village"),
     ], mono_cols=(0,))},
  {"name": "Mr Omar Ali", "role": "Village resident", "label": "DOORBELL CAMERA",
   "quote": "My doorbell camera records everything. No van came to my house at ten to eleven – nothing at all.",
   "evidence": ev_photos("Doorbell camera – No. 9", [
       ("CLIP_1", "4 Dec 10:30–11:15", "Empty doorstep. No van, no driver, no parcel."),
     ])},
  {"name": "Kerry Ward", "role": "Depot manager", "label": "ROUND LIST",
   "quote": "Each round has one driver. Round 7 is Darren's – every day this month.",
   "evidence": ev_table("Driver rounds – December", ["Round", "Driver"], [
       ("Round 6", "S. Morris"),
       ("Round 7", "D. Cole"),
       ("Round 8", "P. Lang"),
     ])},
  {"name": "Steve Morris", "role": "Delivery driver, Round 6", "label": "STEVE'S STATEMENT",
   "quote": "I do the next village over. I saw Darren's van parked in the Mill Lane lay-by every morning – back doors open, him on his phone taking photos.",
   "evidence": ev_note("STEVE'S NOTE", [
       "Mill Lane lay-by, most mornings",
       "about 10:45 – Darren's van, back",
       "open, him photographing boxes on",
       "the floor. Thought it was odd."],
     "– Steve")},
  {"name": "PC Hannah Grey", "role": "Police", "label": "ONLINE SHOP",
   "quote": "We found an online seller listing brand-new headphones, smartwatches and a games console as 'unwanted gifts' – photographed on the floor of a van.",
   "evidence": ev_rows("Online listing", [
       ("Seller", "dazzadeals77"),
       ("Items", "Headphones, smartwatch, games console – 'new, unwanted gifts'"),
       ("Photo background", "Grey van floor with a courier logo"),
       ("Bank account", "D. Cole"),
     ])},
 ],
 "solution": {"killer": "Darren Cole",
   "motive": "Darren was selling the parcels online (clue 6).",
   "proof": ["The missing parcels were marked delivered on Round 7 between 10:42 and 11:03 (clue 1). Round 7 is Darren's (clue 4).",
             "Darren says he delivered every parcel, but his van was parked outside the village from 10:40 to 11:10 (clue 2), and Mr Ali's camera shows no delivery at all (clue 3).",
             "Steve saw him photographing boxes in his van in the lay-by (clue 5), and the same items were sold online by a seller paid into D. Cole's account (clue 6)."],
   "cleared": ["<b>Steve</b> drives Round 6 in the next village (clues 4, 5).",
               "<b>Mrs Booth</b>, <b>Mr Ali</b>, <b>Kerry</b> and <b>PC Grey</b> only report what they found."]},
}

# ---------------------------------------------------------------- BALLET (L2)
ballet = {
 "slug": "the-ballet-shoe-sabotage", "level": 2, "crime": "SABOTAGE", "who": "saboteur", "added": ADDED,
 "caseno": "CASE NO. 219", "title_html": "THE BALLET SHOE<br>SABOTAGE", "title_plain": "The Ballet Shoe Sabotage",
 "teaser": "The star of The Nutcracker falls on opening night when her shoe ribbon snaps – it was cut. A gold thread and a warm-up register catch the saboteur.",
 "intro": "At the <b>Northern City Ballet</b>, lead dancer Sofia Reyes fell during the opening night of The Nutcracker when the ribbon on her pointe shoe snapped. It had been cut almost through. " + STD,
 "clues": [
  {"name": "Sofia Reyes", "role": "Lead dancer", "label": "SOFIA'S REPORT",
   "quote": "I sewed fresh ribbons on at four. I left the shoes in my dressing room and went to warm up at six. At seven I put them on and didn't check.",
   "evidence": ev_rows("Shoe check", [
       ("Ribbons sewn", "16:00"),
       ("Shoes left", "Dressing room 1, 18:00–19:00"),
       ("Ribbon", "Cut neatly with small scissors – three-quarters through"),
       ("On the floor", "A tiny gold thread"),
     ])},
  {"name": "Bella Grant", "role": "Understudy", "label": "BELLA'S STATEMENT",
   "quote": "I was at the barre warming up with everyone from six to seven. I never left the studio.",
   "evidence": ev_rows("Casting note", [
       ("Role", "The Sugar Plum Fairy"),
       ("First cast", "S. Reyes"),
       ("If injured", "B. Grant takes over for the whole run"),
     ])},
  {"name": "Mr Leo Park", "role": "Ballet master", "label": "WARM-UP REGISTER",
   "quote": "I take the register at warm-up. Everyone was there – except one dancer who said she needed to 'fix her costume' and left for fifteen minutes.",
   "evidence": ev_table("Warm-up – opening night", ["Time", "Note"], [
       ("18:00", "All 24 dancers present"),
       ("18:25", "B. Grant – out, 'costume problem'"),
       ("18:41", "B. Grant – back"),
     ], mono_cols=(0,))},
  {"name": "Meg Hollis", "role": "Wardrobe mistress", "label": "COSTUME LIST",
   "quote": "Bella didn't come to me about any costume problem. And only the Sugar Plum costumes have gold thread – Sofia's and Bella's spare.",
   "evidence": ev_table("Costumes with gold thread", ["Costume", "Dancer"], [
       ("Sugar Plum – first", "S. Reyes (in wardrobe until 18:50)"),
       ("Sugar Plum – spare", "B. Grant (worn at warm-up)"),
     ])},
  {"name": "Tom Fry", "role": "Stage door keeper", "label": "CORRIDOR NOTE",
   "quote": "The dressing rooms are on my corridor. At about half six a dancer in a gold-trimmed tutu went into dressing room 1 – Sofia's – and came out a few minutes later.",
   "evidence": ev_note("STAGE DOOR LOG", [
       "18:30 – dancer, gold tutu, into DR1.",
       "18:35 – out again, fast, towards",
       "the studio. Carrying small sewing",
       "scissors?"],
     "– Tom")},
  {"name": "Ana Lowe", "role": "Dancer", "label": "ANA'S STATEMENT",
   "quote": "Sofia and I share a flat, and we've argued about the rent. But I was at warm-up the whole hour – Mr Park can tell you.",
   "evidence": ev_rows("Warm-up partner list", [
       ("A. Lowe", "Partnered with J. Kent 18:00–19:00, never apart"),
     ])},
 ],
 "solution": {"killer": "Bella Grant",
   "motive": "If Sofia was hurt, Bella would dance the Sugar Plum Fairy for the whole run (clue 2).",
   "proof": ["The ribbon was cut while the shoes were in dressing room 1, between 18:00 and 19:00, and a gold thread was left behind (clue 1).",
             "Bella says she never left the studio, but she was out from 18:25 to 18:41 – not for any costume problem (clues 3, 4).",
             "At 18:30 a dancer in a gold-trimmed tutu went into Sofia's room (clue 5). The only other gold costume was Bella's spare, worn at warm-up (clue 4)."],
   "cleared": ["<b>Ana</b> was partnered at warm-up the whole hour (clue 6).",
               "<b>Mr Park</b>, <b>Meg</b> and <b>Tom</b> only report what they saw (clues 3, 4, 5)."]},
}

# ---------------------------------------------------------------- LIGHTHOUSE HOTEL (L3)
light = {
 "slug": "death-at-the-lighthouse-hotel", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 220", "title_html": "DEATH AT THE<br>LIGHTHOUSE HOTEL", "title_plain": "Death at the Lighthouse Hotel",
 "teaser": "A hotel owner falls from the gallery of his lighthouse hotel on a stormy night. A guest's long-exposure photo and a yellow oilskin expose the killer.",
 "intro": "At the <b>Lighthouse Hotel</b> on Skerra Point, owner Neil Burke fell from the lantern gallery on a stormy night. Someone was up there with him. " + STD,
 "clues": [
  {"name": "DS Morag Allan", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Burke went over the gallery rail – he was pushed. The only way up is the spiral staircase: 112 steps from the hotel lobby.",
   "evidence": ev_rows("Police report – Skerra Point", [
       ("Fell", "Between 22:00 and 22:30"),
       ("Gallery", "Reached only by the 112-step staircase from the lobby"),
       ("Gallery rail", "Fresh scuff marks – a struggle"),
       ("On the rail", "A torn thread of yellow oilskin"),
     ])},
  {"name": "Ellen Burke", "role": "Neil's sister, co-owner", "label": "ELLEN'S STATEMENT",
   "quote": "I was in the hotel kitchen from ten until half past, making the breakfast bread. I never went up the tower.",
   "evidence": ev_rows("Solicitor's letter", [
       ("To", "Ellen Burke"),
       ("Subject", "Sale of the Lighthouse Hotel"),
       ("Text", "“Your brother has agreed to sell the hotel against your wishes. Contracts are signed on Friday.”"),
     ])},
  {"name": "Mr Kit Lowry", "role": "Guest, photographer", "label": "LONG-EXPOSURE PHOTO",
   "quote": "I was on the beach taking a long-exposure photo of the beam. When I looked at it later, there were two people on the gallery.",
   "evidence": ev_photos("Kit's camera", [
       ("DSC_2214", "22:14 (30-second exposure)", "The lighthouse at night, beam sweeping. On the gallery, lit by the beam: two figures – one in a dark jumper, one in a long yellow oilskin coat with the hood up."),
     ])},
  {"name": "Dougie Ross", "role": "Night porter", "label": "LOBBY LOG",
   "quote": "The staircase door is in the lobby, beside my desk. I left my desk once – to fetch towels at ten past ten – for about fifteen minutes.",
   "evidence": ev_table("Porter's lobby log", ["Time", "Note"], [
       ("22:00", "Mr Burke up the tower – 'checking the lamp'"),
       ("22:10", "Porter away – towels"),
       ("22:25", "Porter back – yellow oilskin dripping on the coat hook"),
     ], mono_cols=(0,))},
  {"name": "Mrs Jean Craig", "role": "Cook", "label": "KITCHEN NOTE",
   "quote": "Ellen came into the kitchen at ten and started the dough. But she went out to 'check the generator' at about ten past, and when she came back her hair was soaking wet.",
   "evidence": ev_note("JEAN'S NOTE", [
       "22:00 – Ellen starts bread dough.",
       "22:09 – Ellen out, 'generator'.",
       "22:24 – back, hair soaking wet,",
       "hands shaking. Dough over-proved."],
     "– Jean")},
  {"name": "Sam Duffy", "role": "Handyman", "label": "OILSKIN LIST",
   "quote": "The yellow oilskins hang in the lobby for staff. There are only two – mine was in my van all night.",
   "evidence": ev_table("Staff oilskins", ["Coat", "Used by"], [
       ("Yellow, long, with hood", "E. Burke"),
       ("Yellow, short jacket", "S. Duffy – in his van all night"),
     ])},
 ],
 "solution": {"killer": "Ellen Burke",
   "motive": "Neil was selling the hotel against Ellen's wishes (clue 2).",
   "proof": ["Neil went up the tower at 22:00 and was pushed from the gallery; a yellow oilskin thread was on the rail (clues 1, 4).",
             "Ellen says she was in the kitchen from 22:00 to 22:30, but she left from 22:09 to 22:24 and came back soaked (clue 5), while the porter was away from the staircase door (clue 4).",
             "At 22:14 a figure in a long yellow oilskin with a hood was on the gallery with Neil (clue 3). The long hooded oilskin is Ellen's (clue 6), and it was hanging up dripping at 22:25 (clue 4)."],
   "cleared": ["<b>Sam</b>'s short jacket was in his van all night (clue 6).",
               "<b>Kit</b> was on the beach, <b>Dougie</b> was fetching towels, and <b>Mrs Craig</b> stayed in the kitchen (clues 3, 4, 5)."]},
}

# ---------------------------------------------------------------- FASHION SHOW (L3)
fashion = {
 "slug": "murder-at-the-fashion-show", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 221", "title_html": "MURDER AT THE<br>FASHION SHOW", "title_plain": "Murder at the Fashion Show",
 "teaser": "A designer is found dead backstage during her own winter show. The running order and a missing silver shoe reveal which model left the catwalk.",
 "intro": "At <b>London Winter Fashion Week</b>, designer Margot Vell was found dead in the backstage fitting room during her own show, strangled with a silk scarf from the collection. " + STD,
 "clues": [
  {"name": "DI Rachel Shaw", "role": "Police", "label": "POLICE REPORT",
   "quote": "Ms Vell was killed in the fitting room between 19:20 and 19:35. A single silver stiletto was left under the table – size 4.",
   "evidence": ev_rows("Police report – Fashion Week", [
       ("Found", "19:50, fitting room"),
       ("Time of death", "19:20–19:35"),
       ("Weapon", "Silk scarf, look 14"),
       ("Under the table", "One silver stiletto, size 4"),
     ])},
  {"name": "Kira Dahl", "role": "Model", "label": "KIRA'S STATEMENT",
   "quote": "I was on the catwalk or in the changing line the whole show. You don't get a free minute at a fashion show.",
   "evidence": ev_rows("Margot's message to the agency", [
       ("Sent", "That afternoon"),
       ("Text", "“Kira Dahl will not be the face of our new perfume. Tell her after the show.”"),
     ])},
  {"name": "Luca Ferri", "role": "Show producer", "label": "RUNNING ORDER",
   "quote": "Each model walks three looks. Between looks they have a gap while the others walk. Kira had the longest gap – fifteen minutes between look 6 and look 18.",
   "evidence": ev_table("Running order – Kira Dahl", ["Look", "Time on catwalk"], [
       ("Look 1", "19:00"),
       ("Look 6", "19:18"),
       ("Look 18", "19:38"),
     ], mono_cols=(1,))},
  {"name": "Bea Morley", "role": "Dresser", "label": "DRESSER'S NOTE",
   "quote": "When Kira came back for look 18, she was wearing only one silver shoe. I had to grab another pair, and the hem of her dress was pinned wrong – it had been half undone.",
   "evidence": ev_note("DRESSER'S SHEET", [
       "19:36 – Kira back for look 18.",
       "Only ONE silver stiletto (size 4).",
       "Hem pins out, scarf missing from",
       "her look 6 outfit."],
     "– Bea")},
  {"name": "Nina Holt", "role": "Model", "label": "SHOE SIZES",
   "quote": "Each model has her own shoes for the show. Silver stilettos were only in Kira's looks.",
   "evidence": ev_table("Show shoes", ["Model", "Shoes", "Size"], [
       ("K. Dahl", "Silver stilettos", "4"),
       ("N. Holt", "Black boots", "6"),
       ("P. Ade", "Gold sandals", "5"),
     ])},
  {"name": "Paul Vell", "role": "Margot's husband", "label": "PAUL'S STATEMENT",
   "quote": "Margot and I argued about money that morning. But I sat in the front row the whole show – the photographers have me in every shot.",
   "evidence": ev_photos("Press photos", [
       ("PRESS_19:22", "19:22", "Front row: Paul Vell clapping."),
       ("PRESS_19:31", "19:31", "Front row: Paul Vell on his phone."),
     ])},
 ],
 "solution": {"killer": "Kira Dahl",
   "motive": "Margot was dropping Kira as the face of the new perfume (clue 2).",
   "proof": ["Margot was killed between 19:20 and 19:35, and a size-4 silver stiletto was left under the table (clue 1).",
             "Kira says she had no free minute, but between look 6 at 19:18 and look 18 at 19:38 she had a long gap (clue 3).",
             "She came back at 19:36 with only one silver stiletto, size 4, and her scarf missing (clue 4). Only Kira wore silver stilettos (clue 5)."],
   "cleared": ["<b>Paul</b> was photographed in the front row at 19:22 and 19:31 (clue 6).",
               "<b>Nina</b> wore size-6 boots (clue 5); <b>Luca</b> and <b>Bea</b> only report what they saw."]},
}

MYSTERIES = [parcel, ballet, light, fashion]
