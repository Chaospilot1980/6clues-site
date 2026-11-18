from lib import *  # evidence helpers

# Round 18 (18 Nov): 3 Rookie (level 1).
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- TOMBOLA (L1)
tombola = {
 "slug": "the-school-fair-tombola", "level": 1, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 135", "title_html": "THE SCHOOL FAIR<br>TOMBOLA", "title_plain": "The School Fair Tombola",
 "teaser": "The tombola's star prize – a brand-new games console – disappears from under the table. One helper says she never left the cake stall.",
 "intro": "At the <b>Elmwood Primary Christmas Fair</b>, the tombola's top prize, a £300 games console, vanished from its box under the tombola table during the afternoon. " + STD,
 "clues": [
  {"name": "Mrs Jenny Clarke", "role": "Fair organiser", "label": "FAIR REPORT",
   "quote": "The console was under the tombola table in its box all afternoon. At four o'clock the box was there – but empty. Whoever took it must have been at the tombola table.",
   "evidence": ev_rows("Fair report – Elmwood Primary", [
       ("Fair", "13:00–16:00, school hall"),
       ("Prize", "Games console, £300, under the tombola table"),
       ("Last seen", "14:30 – Mr Dale showed it to a family"),
       ("Found empty", "16:00"),
       ("Tombola rota", "Helpers take turns, 30 minutes each"),
     ])},
  {"name": "Mr Owen Dale", "role": "Tombola helper", "label": "TOMBOLA ROTA",
   "quote": "I did the first shift and showed the console to the Patel family at half two, just before I handed over. It was definitely in the box then.",
   "evidence": ev_table("Tombola rota", ["Time", "Helper"], [
       ("14:00–14:30", "Owen Dale"),
       ("14:30–15:00", "Sandra Hughes"),
       ("15:00–15:30", "Kerry Lamb"),
       ("15:30–16:00", "Owen Dale"),
     ], mono_cols=(0,))},
  {"name": "Sandra Hughes", "role": "Parent helper", "label": "SANDRA'S STATEMENT",
   "quote": "I wasn't on the tombola at all! I spent the whole afternoon helping on the cake stall. Ask anyone.",
   "evidence": ev_table("Cake stall rota", ["Time", "Helper"], [
       ("13:00–15:00", "Kerry Lamb"),
       ("15:00–16:00", "Mr Ford's wife, Ellen"),
     ], mono_cols=(0,))},
  {"name": "Kerry Lamb", "role": "Parent helper", "label": "CAKE STALL TILL",
   "quote": "I did the cake stall until three, then the tombola. The console box was already closed when I got there – I never looked inside.",
   "evidence": ev_table("Cake stall – card machine", ["Time", "Sale", "Served by"], [
       ("14:38", "Chocolate cake", "K. Lamb"),
       ("14:46", "4 cupcakes", "K. Lamb"),
       ("14:55", "Flapjacks", "K. Lamb"),
     ], mono_cols=(0,))},
  {"name": "Raj Patel", "role": "Parent", "label": "RAJ'S PHOTO",
   "quote": "My son wanted a photo with the console – he was desperate to win it. We took one just after half past two.",
   "evidence": ev_photos("Raj's phone", [
       ("IMG_330", "14:28", "Raj's son next to the tombola table. Mr Dale holds up the console."),
       ("IMG_335", "14:41", "Raj's son with a tombola prize. Behind the table: Sandra Hughes, bending down to the box under the table."),
     ])},
  {"name": "Mr Tim Ford", "role": "Caretaker", "label": "CAR PARK",
   "quote": "At about quarter to three I saw a parent carrying a big shopping bag out to the car park and putting it in her car boot, then coming straight back in.",
   "evidence": ev_rows("Car park camera – 14:47", [
       ("Person", "Woman in a red Christmas jumper"),
       ("Car", "Blue estate, registration ending 'SH'"),
       ("Car owner", "Sandra Hughes"),
     ])},
 ],
 "solution": {"killer": "Sandra Hughes",
   "motive": "Sandra wanted the £300 console for herself (clues 5, 6).",
   "proof": ["The console was there at 14:28 and the box was empty at 16:00 (clues 1, 5).",
             "Sandra says she was on the cake stall all afternoon (clue 3). But she is not on the cake stall rota (clue 3), the tombola rota puts her on the tombola from 14:30 to 15:00 (clue 2), and Raj's photo shows her behind the tombola table at 14:41, bending down to the box (clue 5).",
             "Kerry was serving cakes from 14:38 to 14:55 (clue 4), so Sandra was alone at the tombola.",
             "At 14:47 the caretaker's camera shows Sandra putting a big bag in the boot of her car (clue 6)."],
   "cleared": ["<b>Kerry</b> was selling cakes at 14:38, 14:46 and 14:55 (clue 4).",
               "<b>Owen</b> showed the console at 14:28 and handed over (clues 2, 5).",
               "<b>Raj</b>, <b>Mr Ford</b> and <b>Mrs Clarke</b> only report what they saw."]},
}

# ---------------------------------------------------------------- LIBRARY (L1)
library = {
 "slug": "the-library-first-edition", "level": 1, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 136", "title_html": "THE LIBRARY<br>FIRST EDITION", "title_plain": "The Library First Edition",
 "teaser": "A signed first edition vanishes from a locked library cabinet. Three people had a key – and one forgot which day the library is closed.",
 "intro": "At <b>Kingsford Library</b>, a signed first edition worth £4,000 has gone from the locked Local History cabinet. " + STD,
 "clues": [
  {"name": "Mrs Ada Lowe", "role": "Head librarian", "label": "LIBRARY REPORT",
   "quote": "I checked the cabinet on Saturday at closing time – the book was there. On Tuesday morning it was gone, and the cabinet was locked again.",
   "evidence": ev_rows("Library report", [
       ("Last seen", "Saturday, 17:00 (closing)"),
       ("Missing", "Tuesday, 09:00"),
       ("Cabinet", "Not damaged – opened with a key"),
       ("Keys", "Mrs Lowe, Mr Nash (deputy), Ms Vega (archive volunteer)"),
     ])},
  {"name": "Mr Colin Nash", "role": "Deputy librarian", "label": "OPENING HOURS",
   "quote": "I was on holiday in Cornwall from Saturday night until Tuesday. I left my keys in my desk drawer, as always.",
   "evidence": ev_table("Kingsford Library – opening hours", ["Day", "Open"], [
       ("Saturday", "09:00–17:00"),
       ("Sunday", "Closed"),
       ("Monday", "Closed"),
       ("Tuesday", "09:00–19:00"),
     ])},
  {"name": "Rosa Vega", "role": "Archive volunteer", "label": "ROSA'S STATEMENT",
   "quote": "I came in on Monday morning to do my usual archive work. There were lots of people in the reading room – it was busy. I didn't touch the cabinet.",
   "evidence": ev_rows("Rosa Vega – volunteer record", [
       ("Volunteer since", "Last year"),
       ("Has", "Front door key and cabinet key"),
       ("Note", "Asked twice if the first edition was “insured for a lot”"),
     ])},
  {"name": "Jack Bright", "role": "Cleaner", "label": "ALARM LOG",
   "quote": "I clean on Saturday evenings after closing. I don't have a cabinet key – only the front door.",
   "evidence": ev_table("Library alarm", ["Day", "Time", "Event", "Code"], [
       ("Saturday", "17:30", "Alarm off", "Cleaner"),
       ("Saturday", "19:00", "Alarm on", "Cleaner"),
       ("Monday", "10:12", "Alarm off", "Volunteer – R. Vega"),
       ("Monday", "10:40", "Alarm on", "Volunteer – R. Vega"),
     ], mono_cols=(1,))},
  {"name": "Mr Lee Shaw", "role": "Bookseller", "label": "BOOKSELLER'S NOTE",
   "quote": "On Monday afternoon a woman phoned asking what I'd pay for a signed first edition of that very book. She wouldn't give her name.",
   "evidence": ev_note("SHAW'S BOOKS – PHONE MESSAGE", [
       "Monday 15:20.",
       "Woman asking about selling a signed first edition.",
       "Called from mobile number ending 4471.",
       "Said she would 'bring it in on Thursday'."],
     "– L. Shaw")},
  {"name": "Mrs Pat Moore", "role": "Library friend", "label": "PHONE LIST",
   "quote": "I keep the volunteers' phone list for the Friends of the Library. I hope nobody I know did this.",
   "evidence": ev_table("Friends of the Library – phone list", ["Name", "Mobile ends"], [
       ("Ada Lowe", "2210"),
       ("Colin Nash", "8803"),
       ("Rosa Vega", "4471"),
       ("Jack Bright", "1590"),
     ])},
 ],
 "solution": {"killer": "Rosa Vega",
   "motive": "Rosa wanted to sell the book – she had asked how much it was insured for (clue 3) and phoned a bookseller (clue 5).",
   "proof": ["Rosa says the reading room was busy on Monday (clue 3). But the library is closed on Mondays (clue 2) – nobody else was there.",
             "The alarm log shows Rosa alone in the building on Monday from 10:12 to 10:40 (clue 4), and she has a cabinet key (clue 3).",
             "That afternoon a woman phoned the bookseller from a number ending 4471 (clue 5) – Rosa's number (clue 6)."],
   "cleared": ["<b>Colin</b> was on holiday and the alarm shows no visit from him (clues 2, 4).",
               "<b>Jack</b> has no cabinet key and was there on Saturday, before the book was checked (clues 1, 4).",
               "<b>Ada</b> reported the theft; <b>Lee</b> and <b>Pat</b> only supply the facts."]},
}

# ---------------------------------------------------------------- SNOWMAN (L1)
snowman = {
 "slug": "the-snowman-contest", "level": 1, "crime": "VANDALISM", "who": "vandal", "added": ADDED,
 "caseno": "CASE NO. 137", "title_html": "THE SNOWMAN<br>CONTEST", "title_plain": "The Snowman Contest",
 "teaser": "The night before judging, the best snowman in the village is knocked flat. The footprints in the fresh snow lead straight to the culprit.",
 "intro": "In the village of <b>Fernley</b>, the snowman contest is judged at nine on Sunday morning. Overnight, the favourite – a giant snow-owl built by the Grant family – was smashed. " + STD,
 "clues": [
  {"name": "Molly Grant", "role": "Snow-owl builder", "label": "DAMAGE REPORT",
   "quote": "We finished our snow-owl at eight on Saturday evening. At seven in the morning it was smashed to pieces. And there was a big footprint trail across our lawn.",
   "evidence": ev_rows("Village green warden – report", [
       ("Snow-owl finished", "Saturday 20:00"),
       ("Found smashed", "Sunday 07:00"),
       ("Footprints", "One set, size 11 wellies with a star pattern on the sole"),
       ("Snow", "Fresh snow fell from 23:00 to 01:00"),
     ])},
  {"name": "Gus Rowley", "role": "Rival builder", "label": "GUS'S STATEMENT",
   "quote": "My snow-dragon was going to win anyway. I went to bed at ten and didn't go out again till morning.",
   "evidence": ev_rows("Snowman contest – last year", [
       ("1st", "The Grant family – snow-castle"),
       ("2nd", "Gus Rowley – snow-car"),
       ("Prize", "£100 and a trophy"),
     ])},
  {"name": "Warden Pete", "role": "Village green warden", "label": "WEATHER NOTE",
   "quote": "The footprints were sharp and clear on top of the new snow – not covered at all. So whoever made them walked there after the snow stopped.",
   "evidence": ev_note("FERNLEY WEATHER BOOK", [
       "Saturday night:",
       "Snow started 23:00.",
       "Snow stopped 01:00.",
       "Clear and frosty after that."],
     "– Pete, warden")},
  {"name": "Nina Patel", "role": "Neighbour", "label": "WELLIES",
   "quote": "I sell wellies at the village shop. Only two people in Fernley bought the size 11 Star-Grip wellies this winter.",
   "evidence": ev_table("Village shop – Star-Grip wellies, size 11", ["Date", "Buyer"], [
       ("2 Nov", "Gus Rowley"),
       ("9 Nov", "Ben Hart"),
     ])},
  {"name": "Ben Hart", "role": "Farmer", "label": "LAMBING LOG",
   "quote": "I did buy those wellies. But on Saturday night I was in the lambing shed at my farm, five miles away, until six in the morning.",
   "evidence": ev_table("Hart Farm – lambing shed", ["Time", "Note", "By"], [
       ("22:30", "Ewe 14 in labour", "B. Hart"),
       ("01:15", "Twin lambs born", "B. Hart"),
       ("03:40", "All well – checked", "B. Hart, vet"),
       ("06:00", "Left shed", "B. Hart"),
     ], mono_cols=(0,))},
  {"name": "Jill Rowley", "role": "Gus's wife", "label": "JILL'S STATEMENT",
   "quote": "Gus says he was in bed all night? He got up at about two – I heard the back door bang. He said he was checking on the car.",
   "evidence": ev_photos("Rowleys' doorbell camera", [
       ("CAM", "02:05", "A man in a big coat and wellies leaving the Rowleys' back gate towards the green."),
       ("CAM", "02:20", "The same man coming back in, brushing snow off his sleeves."),
     ])},
 ],
 "solution": {"killer": "Gus Rowley",
   "motive": "Gus came second to the Grants last year and wanted the £100 prize and trophy (clue 2).",
   "proof": ["The footprints were made after the snow stopped at 01:00 (clue 3), by size 11 Star-Grip wellies (clue 1).",
             "Only Gus and Ben bought those wellies (clue 4). Ben was in his lambing shed all night (clue 5).",
             "Gus says he stayed in bed, but his wife heard him go out at about two (clue 6), and the doorbell camera shows him leaving at 02:05 and coming back at 02:20 (clue 6)."],
   "cleared": ["<b>Ben</b> was in the lambing shed until 06:00 (clue 5).",
               "<b>Molly</b> built the snow-owl; <b>Nina</b>, <b>Pete</b> and <b>Jill</b> only report what they know."]},
}

MYSTERIES = [tombola, library, snowman]
