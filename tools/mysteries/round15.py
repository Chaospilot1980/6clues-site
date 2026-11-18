from lib import *  # evidence helpers

# Round 15 (18 Nov): 1 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- BEEHIVES (L2)
bees = {
 "slug": "the-poisoned-beehives", "level": 2, "crime": "SABOTAGE", "who": "saboteur", "added": ADDED,
 "caseno": "CASE NO. 128", "title_html": "THE POISONED<br>BEEHIVES", "title_plain": "The Poisoned Beehives",
 "teaser": "On the morning of the county honey show, the favourite's twelve hives are found dead. One neighbour says she spent the night of the storm in her garden.",
 "intro": "In the village of <b>Little Brockwell</b>, all twelve hives of beekeeper Ruth Ashby died overnight – two days before the county honey show she has won four years running. Poison was found in the feeders. " + STD,
 "clues": [
  {"name": "Ruth Ashby", "role": "Beekeeper", "label": "VET'S REPORT",
   "quote": "I filled the feeders with sugar syrup at six on Friday evening and the bees were fine. On Saturday at seven they were all dead. Someone came into my orchard in the night.",
   "evidence": ev_rows("Bee inspector's report", [
       ("Hives", "12 of 12 dead"),
       ("Cause", "Insecticide added to the syrup feeders"),
       ("Time", "Poison taken in between 22:00 and 02:00 (bees feed little after dark, many found inside)"),
       ("Access", "Orchard reached only through the lane gate, which has a combination padlock"),
     ])},
  {"name": "Carol Finch", "role": "Rival beekeeper", "label": "CAROL'S STATEMENT",
   "quote": "I was home all Friday night. I sat out in my garden until midnight because it was such a lovely clear, still evening – you could see every star. Then I went to bed.",
   "evidence": ev_rows("Honey show – previous results", [
       ("2023", "1st R. Ashby · 2nd C. Finch"),
       ("2024", "1st R. Ashby · 2nd C. Finch"),
       ("2025", "1st R. Ashby · 2nd C. Finch"),
       ("Prize 2026", "£500 and supply contract with Brockwell Farm Shop"),
     ])},
  {"name": "Tom Ashby", "role": "Ruth's nephew", "label": "WEATHER STATION",
   "quote": "Aunt Ruth's hives? I had nothing to do with it. I know the gate code, sure – the whole family does. On Friday night I was at the pub quiz until closing.",
   "evidence": ev_table("Little Brockwell weather station – Friday night", ["Time", "Rain", "Wind", "Sky"], [
       ("20:00", "0 mm", "12 mph", "Overcast"),
       ("22:00", "6 mm", "34 mph", "Thunderstorm"),
       ("23:00", "9 mm", "41 mph", "Thunderstorm"),
       ("00:00", "4 mm", "28 mph", "Heavy rain"),
       ("02:00", "0 mm", "10 mph", "Clearing"),
     ], mono_cols=(0,))},
  {"name": "Gwen Pryor", "role": "Landlady, The Plough", "label": "QUIZ SCORE SHEET",
   "quote": "Tom's team won the quiz on Friday – he was here from eight till we shut at half eleven. Then he and the others stayed for a lock-in until gone one.",
   "evidence": ev_table("The Plough – Friday quiz", ["Round", "Time", "Tom's team"], [
       ("1", "20:15", "8/10"),
       ("4", "21:40", "9/10"),
       ("8", "23:05", "10/10 – winners"),
     ], mono_cols=(1,))},
  {"name": "Sid Morley", "role": "Gardener", "label": "GARDEN SHED STOCK",
   "quote": "I do Ruth's orchard and Carol's garden too. Carol asked me last week whether that old insecticide in the shed was still any good. I said I'd throw it out.",
   "evidence": ev_table("Carol Finch's shed – police search", ["Item", "Found"], [
       ("Insecticide, 1 litre", "Bottle a third full – same product as in the feeders"),
       ("Wellington boots", "Caked in fresh mud"),
       ("Raincoat", "Still damp on Saturday at 10:00"),
     ])},
  {"name": "Dr Anil Shah", "role": "Show judge", "label": "GATE CODE NOTE",
   "quote": "I judge the honey show. I visited Ruth on Thursday to see her hives – she wrote the gate code on a note for me, and Carol was in her kitchen at the time.",
   "evidence": ev_rows("Note on Ruth's kitchen board", [
       ("Text", "Lane gate: 4-7-1-9"),
       ("Written", "Thursday, for Dr Shah's visit"),
       ("Seen by", "Dr Shah, Carol Finch (dropping off jam jars)"),
     ])},
 ],
 "solution": {"killer": "Carol Finch",
   "motive": "Carol had come second to Ruth three years running (clue 2), and this year the prize included a farm-shop supply contract.",
   "proof": ["The hives were poisoned between 22:00 and 02:00 (clue 1). Carol says she sat in her garden under a clear, still, starry sky until midnight (clue 2) – but from 22:00 to midnight a thunderstorm raged (clue 3). Her alibi is invented.",
             "Her shed holds the same insecticide, a damp raincoat and muddy boots (clue 5), and she saw the gate code on Ruth's kitchen board on Thursday (clue 6)."],
   "cleared": ["<b>Tom</b> knows the code but was at the pub quiz and the lock-in until after one (clue 4).",
               "<b>Dr Shah</b> also knew the code but judges the show and gains nothing; <b>Sid</b> tried to get rid of the insecticide (clue 5).",
               "<b>Gwen</b> was running the pub all night (clue 4), and <b>Ruth</b> lost everything (clue 1)."]},
}

# ---------------------------------------------------------------- PLANETARIUM (L3)
planet = {
 "slug": "murder-at-the-planetarium", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 129", "title_html": "MURDER AT THE<br>PLANETARIUM", "title_plain": "Murder at the Planetarium",
 "teaser": "The director dies in the projection booth while the stars wheel overhead for a full house. The killer's alibi was the show itself.",
 "intro": "At the <b>Northgate Planetarium</b>, director Prof. Edwin Lyle was found dead in the projection booth after the 19:00 show “Journey to Saturn”. " + STD,
 "clues": [
  {"name": "Sgt Paula Grey", "role": "Police", "label": "POLICE REPORT",
   "quote": "The booth door locks itself and opens only with a staff card. The professor was struck from behind. His smartwatch recorded his heart stopping during the show.",
   "evidence": ev_rows("Police report – Northgate Planetarium", [
       ("Found", "19:52, projection booth"),
       ("Death", "Blow to the back of the head"),
       ("Smartwatch", "Heart stopped at 19:24"),
       ("Booth door", "Opens only with a staff card; every swipe is logged"),
     ])},
  {"name": "Dr Hana Ito", "role": "Presenter", "label": "SHOW SCRIPT",
   "quote": "I presented the show live from the console in the middle of the dome, as always. Kieran in the booth runs the projector; I never left the audience's sight.",
   "evidence": ev_programme("Journey to Saturn – running order", "Live show, dome", [
       ("19:00", "Welcome – presenter at console"),
       ("19:10", "Sunset over Northgate (pre-recorded, 12 min)"),
       ("19:22", "Live: the night sky tonight"),
       ("19:35", "Saturn flyby (pre-recorded)"),
       ("19:45", "Questions"),
     ], None)},
  {"name": "Kieran Doyle", "role": "Projectionist", "label": "BOOTH DOOR LOG",
   "quote": "I left the booth at ten past seven to fetch a spare lamp from the store. When I came back at half past, the professor was in there – alive, sitting with his back to me. I didn't want to disturb him, so I went to the café.",
   "evidence": ev_table("Projection booth – card log", ["Time", "Card", "Name"], [
       ("18:50", "S-04", "K. Doyle"),
       ("19:08", "S-01", "E. Lyle"),
       ("19:11", "S-02", "H. Ito"),
       ("19:31", "S-04", "K. Doyle"),
     ], mono_cols=(0,))},
  {"name": "Sophie Marr", "role": "Café manager", "label": "CAFÉ CCTV",
   "quote": "Kieran came into the café at about twenty-five to eight looking as white as a sheet. He drank a coffee and didn't say a word.",
   "evidence": ev_photos("Café camera", [
       ("CAM-2", "19:34", "K. Doyle enters the café, sits alone near the door."),
       ("CAM-2", "19:50", "K. Doyle still at the table."),
     ])},
  {"name": "Bryn Owens", "role": "Trustee", "label": "BOARD MINUTES",
   "quote": "Edwin and I fought over money for years – he wanted a new projector, I wanted to sell the building. But I sat in row F for the whole show. Ask the people next to me.",
   "evidence": ev_rows("Board minutes – last Monday", [
       ("Item 4", "Director reports £14,000 missing from the education fund"),
       ("Action", "Director to name the person responsible to the police on Friday"),
       ("Fund signatories", "E. Lyle, H. Ito"),
     ])},
  {"name": "Lily Carter", "role": "Visitor, row F", "label": "TICKET SCANS",
   "quote": "I sat next to the trustee – he snored through the sunset bit. But the presenter's console was dark for a few minutes during the recording; I remember thinking she'd gone for a break.",
   "evidence": ev_table("Dome entry scans", ["Time", "Ticket", "Seat"], [
       ("18:52", "Adult", "F-11 (B. Owens)"),
       ("18:53", "Adult", "F-12 (L. Carter)"),
       ("19:16", "Staff side door", "S-02"),
     ], mono_cols=(0,))},
 ],
 "solution": {"killer": "Dr Hana Ito",
   "motive": "£14,000 was missing from the education fund, which only Lyle and Ito could sign for. Lyle was going to name the culprit to the police (clue 5).",
   "proof": ["Hana says she never left the console. But during the pre-recorded sunset (19:10–19:22, clue 2) her card S-02 opened the booth at 19:11 (clue 3), and she came back into the dome by the staff door at 19:16 (clue 6). Lily saw her console dark during the recording.",
             "The smartwatch time of 19:24 (clue 1) seems to clear her, as she was back at the console. But the 'alive' professor that Kieran saw at 19:31 sat with his back turned and never moved – Lyle was already dead. Hana struck him at 19:11–19:16; the watch only registered the end, after he lay unconscious."],
   "cleared": ["<b>Kieran</b> came back at 19:31 (clue 3) and fled to the café in shock at 19:34 (clue 4). His story of a silent man with his back turned fits a dead body.",
               "<b>Bryn</b> quarrelled with Lyle, but sat in F-11 throughout, next to Lily (clue 6).",
               "<b>Sophie</b> was in the café, and <b>Lily</b> was in her seat."]},
}

# ---------------------------------------------------------------- SURF SCHOOL (L3)
surf = {
 "slug": "the-surf-school-drowning", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 130", "title_html": "THE SURF SCHOOL<br>DROWNING", "title_plain": "The Surf School Drowning",
 "teaser": "An expert surfer drowns on a calm evening in his own bay. His business partner says she watched the whole thing from the beach – at low tide.",
 "intro": "In <b>Penhallow Bay</b>, surf-school owner Jake Rowan was found drowned on the rocks at the north end of the beach after an evening paddle. " + STD,
 "clues": [
  {"name": "PC Morgan Tate", "role": "Police", "label": "POLICE REPORT",
   "quote": "Jake had a head wound that the pathologist says came before he went in the water. His dive watch stopped when it flooded – the glass was cracked by a blow.",
   "evidence": ev_rows("Police report – Penhallow Bay", [
       ("Found", "Saturday 20:40, north rocks"),
       ("Injury", "Blow to the temple before drowning"),
       ("Dive watch", "Flooded and stopped at 19:52"),
       ("Board", "Washed up on the south beach"),
     ])},
  {"name": "Nina Cole", "role": "Business partner", "label": "NINA'S STATEMENT",
   "quote": "I was on the beach locking up the hut. I watched Jake paddle out to the north rocks at about quarter to eight, then he waved and paddled round the point. I walked straight out along the wet sand to the water's edge to wave back – it was nearly high tide, so it wasn't far.",
   "evidence": ev_rows("Penhallow Surf School – partnership", [
       ("Owners", "J. Rowan 50 %, N. Cole 50 %"),
       ("Clause 9", "If a partner dies, the other inherits the whole business"),
       ("Dispute", "Jake wanted to sell to a hotel group; Nina refused"),
     ])},
  {"name": "Ben Hosking", "role": "Harbour master", "label": "TIDE TABLE",
   "quote": "Jake knew this bay better than anyone. On Saturday evening the water was very calm – a good night for a paddle, as long as you knew the tides.",
   "evidence": ev_table("Penhallow – Saturday tides", ["Time", "Event", "Height"], [
       ("13:42", "High water", "5.6 m"),
       ("19:58", "Low water", "0.4 m"),
       ("02:14", "High water", "5.8 m"),
     ], mono_cols=(0,))},
  {"name": "Dan Price", "role": "Instructor", "label": "HUT CCTV",
   "quote": "I left the hut at half seven and went to the beach bar. Nina was still at the hut, and Jake's car was in the car park. I didn't see either of them again.",
   "evidence": ev_photos("Hut camera", [
       ("CAM-1", "19:30", "D. Price leaves with his board bag."),
       ("CAM-1", "19:38", "N. Cole leaves the hut and walks north along the beach."),
       ("CAM-1", "20:14", "N. Cole returns, wet to the knees, and locks up."),
     ])},
  {"name": "Mo Jansen", "role": "Beach bar owner", "label": "BAR TILL",
   "quote": "Dan was at my bar from twenty to eight until after nine. Jake was a regular too – he owed me a tab, but who doesn't.",
   "evidence": ev_table("Beach bar – Saturday", ["Time", "Order", "Customer"], [
       ("19:41", "Pint", "D. Price"),
       ("19:55", "Chips", "D. Price"),
       ("20:20", "Pint", "D. Price"),
     ], mono_cols=(0,))},
  {"name": "Elsie Trevan", "role": "Dog walker", "label": "FOOTPRINT PHOTO",
   "quote": "I walk the dog on the cliff path every evening. Around ten to eight I saw two people on the north rocks, one of them with a surfboard. It was too far to see faces.",
   "evidence": ev_photos("Police photo, Sunday 07:00", [
       ("PH-3", "07:00", "Rocks at the north end: at low water they can be reached on foot over the sand. At high water they are cut off."),
     ])},
 ],
 "solution": {"killer": "Nina Cole",
   "motive": "Under clause 9 Nina inherits the whole surf school if Jake dies – and Jake wanted to sell to a hotel group against her wishes (clue 2).",
   "proof": ["Jake was hit on the head and his watch stopped at 19:52 (clue 1). Nina says it was nearly high tide, but low water was at 19:58 (clue 3) – the sea was as far out as it gets.",
             "At low water the north rocks can be reached on foot (clue 6). The hut camera shows Nina walking north at 19:38 and coming back wet to the knees at 20:14 (clue 4), and Elsie saw two people on the rocks around 19:50."],
   "cleared": ["<b>Dan</b> left at 19:30 and was at the bar at 19:41 and 19:55 (clues 4, 5).",
               "<b>Mo</b> was serving at the bar (clue 5), and <b>Elsie</b> was up on the cliff path with her dog (clue 6).",
               "<b>Ben</b> and <b>PC Tate</b> only supply the facts; neither was on the beach."]},
}

MYSTERIES = [bees, planet, surf]
