from lib import *  # evidence helpers

# Round 30 (18 Nov): 1 Rookie, 1 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- GINGERBREAD (L1)
ginger = {
 "slug": "the-gingerbread-house-wrecker", "level": 1, "crime": "SABOTAGE", "who": "saboteur", "added": ADDED,
 "caseno": "CASE NO. 182", "title_html": "THE GINGERBREAD<br>HOUSE WRECKER", "title_plain": "The Gingerbread House Wrecker",
 "teaser": "The best gingerbread house at the Christmas bake show is found crushed before judging. A sticky handprint and a sugar trail lead to the wrecker.",
 "intro": "At the <b>Fernley Christmas Bake Show</b>, Nora Bell's tall gingerbread house was found crushed on its table half an hour before the judges arrived. " + STD,
 "clues": [
  {"name": "Nora Bell", "role": "Baker", "label": "NORA'S REPORT",
   "quote": "My house was fine at two o'clock. When I came back from the café at half past, the roof was smashed and there was a sticky green handprint on the table.",
   "evidence": ev_rows("Nora's report", [
       ("House fine", "14:00"),
       ("Found crushed", "14:30"),
       ("On the table", "Sticky handprint in green icing"),
       ("Judging", "15:00"),
     ])},
  {"name": "Gail Turner", "role": "Rival baker", "label": "GAIL'S STATEMENT",
   "quote": "I was at the front door selling raffle tickets the whole afternoon. I never went near the tables.",
   "evidence": ev_table("Bake show – last year's results", ["Place", "Baker"], [
       ("1st", "Nora Bell"),
       ("2nd", "Gail Turner"),
     ], note="Gail told the newspaper: “Next year that trophy is mine.”")},
  {"name": "Mr Ken Shaw", "role": "Raffle organiser", "label": "RAFFLE ROTA",
   "quote": "Gail was meant to sell raffle tickets with me, but she left the door at ten past two and came back at twenty-five past.",
   "evidence": ev_table("Raffle rota", ["Time", "At the door"], [
       ("13:30–14:10", "K. Shaw, G. Turner"),
       ("14:10–14:25", "K. Shaw only"),
       ("14:25–16:00", "K. Shaw, G. Turner"),
     ], mono_cols=(0,))},
  {"name": "Poppy Lane", "role": "Bake show helper", "label": "ICING LIST",
   "quote": "Each baker brought their own icing colours. Only one baker used green icing this year.",
   "evidence": ev_table("Icing colours by baker", ["Baker", "Colours"], [
       ("N. Bell", "White, red"),
       ("G. Turner", "White, green"),
       ("A. Moss", "White, blue"),
     ])},
  {"name": "Arthur Moss", "role": "Baker", "label": "ARTHUR'S NOTE",
   "quote": "I was at my table all afternoon fixing my chimney. At about quarter past two I saw a woman with green icing on her fingers hurry out of the hall.",
   "evidence": ev_note("ARTHUR'S NOTE", [
       "About 14:15 – woman with green",
       "icing on her fingers left the bake",
       "hall towards the front door.",
       "Wearing a raffle sash."],
     "– Arthur")},
  {"name": "Mrs Ruth Okafor", "role": "Head judge", "label": "JUDGE'S NOTE",
   "quote": "I arrived at quarter to three, after the house was already crushed. I only judge – I don't see the tables before.",
   "evidence": ev_rows("Car park ticket", [
       ("Car", "R. Okafor"),
       ("In", "14:45"),
     ])},
 ],
 "solution": {"killer": "Gail Turner",
   "motive": "Gail wanted to beat Nora, who won last year (clue 2).",
   "proof": ["The house was crushed between 14:00 and 14:30, leaving a green icing handprint (clue 1).",
             "Gail says she never left the raffle door, but she was away from 14:10 to 14:25 (clue 3).",
             "Only Gail used green icing (clue 4), and Arthur saw a woman in a raffle sash with green icing on her fingers at 14:15 (clue 5)."],
   "cleared": ["<b>Arthur</b> used blue icing and stayed at his table (clues 4, 5); <b>Ruth</b> arrived at 14:45 (clue 6).",
               "<b>Ken</b> was at the door the whole time, and <b>Poppy</b> only kept the list (clues 3, 4)."]},
}

# ---------------------------------------------------------------- TOY SHOP (L2)
toy = {
 "slug": "the-toy-shop-till-fraud", "level": 2, "crime": "FRAUD", "who": "fraudster", "added": ADDED,
 "caseno": "CASE NO. 183", "title_html": "THE TOY SHOP<br>TILL FRAUD", "title_plain": "The Toy Shop Till Fraud",
 "teaser": "A busy toy shop is losing money every December day. Refunds that nobody asked for and a login that should not exist point to the fraudster.",
 "intro": "At <b>Pickle &amp; Pip Toys</b>, owner Martha Pickle noticed that the till is £200–£300 short almost every day in December. " + STD,
 "clues": [
  {"name": "Martha Pickle", "role": "Shop owner", "label": "TILL REPORT",
   "quote": "The card takings are fine, but the cash drawer is short every evening – and the till shows lots of cash refunds I never approved.",
   "evidence": ev_table("Cash refunds – 1 to 6 Dec", ["Date", "Refunds", "Total"], [
       ("1 Dec", "4", "£212"),
       ("3 Dec", "5", "£276"),
       ("5 Dec", "4", "£238"),
       ("6 Dec", "5", "£291"),
     ], note="No cash refunds on 2 and 4 December.")},
  {"name": "Leo Grant", "role": "Shop assistant", "label": "LEO'S STATEMENT",
   "quote": "Refunds are done on the manager login, not mine. I can't even do a refund on my own code – ask anyone.",
   "evidence": ev_table("Staff rota – December", ["Date", "Leo", "Amy", "Joe"], [
       ("1 Dec", "Yes", "Yes", "–"),
       ("2 Dec", "–", "Yes", "Yes"),
       ("3 Dec", "Yes", "–", "Yes"),
       ("4 Dec", "–", "Yes", "Yes"),
       ("5 Dec", "Yes", "Yes", "–"),
       ("6 Dec", "Yes", "–", "Yes"),
     ])},
  {"name": "Amy Kerr", "role": "Shop assistant", "label": "TILL LOGINS",
   "quote": "The till keeps a list of every login code. I noticed a code I've never seen before – 'MGR2'.",
   "evidence": ev_table("Till login codes", ["Code", "Belongs to", "Can refund?"], [
       ("MGR1", "M. Pickle", "Yes"),
       ("MGR2", "Created 30 Nov from code LG01", "Yes"),
       ("LG01", "L. Grant", "No"),
       ("AK01", "A. Kerr", "No"),
       ("JB01", "J. Bloom", "No"),
     ])},
  {"name": "Joe Bloom", "role": "Weekend assistant", "label": "JOE'S STATEMENT",
   "quote": "I only work some days. On the twenty-ninth Leo asked me how the manager screen works – said Martha wanted him to help.",
   "evidence": ev_rows("Martha's diary, 30 Nov", [
       ("Note", "Leo locked up alone – I left at 16:00 for the dentist"),
       ("Martha's rule", "Only Martha can set up new till codes"),
     ])},
  {"name": "Sam Ruiz", "role": "Till engineer", "label": "REFUND RECORD",
   "quote": "All the cash refunds were made on code MGR2. None of them has a receipt number from a real sale.",
   "evidence": ev_table("Refund record – 6 Dec", ["Time", "Code", "Amount", "Sale receipt"], [
       ("10:14", "MGR2", "£58", "None"),
       ("12:40", "MGR2", "£64", "None"),
       ("15:02", "MGR2", "£55", "None"),
       ("16:48", "MGR2", "£61", "None"),
       ("17:20", "MGR2", "£53", "None"),
     ])},
  {"name": "Ivy Pickle", "role": "Martha's sister", "label": "IVY'S STATEMENT",
   "quote": "I helped out on the second and the fourth. I never touched the till – I only wrapped presents in the back.",
   "evidence": ev_rows("Wrapping service list", [
       ("2 Dec", "Ivy – 40 parcels wrapped"),
       ("4 Dec", "Ivy – 35 parcels wrapped"),
     ])},
 ],
 "solution": {"killer": "Leo Grant",
   "motive": "Leo kept the cash from fake refunds – about £250 a day (clue 1).",
   "proof": ["Every cash refund was made on code MGR2, with no real sale behind it (clue 5).",
             "Leo says he can't do refunds, but MGR2 was created on 30 November from his code LG01 (clue 3) – the day he locked up alone, after asking Joe how the manager screen works (clue 4).",
             "Refunds happened only on 1, 3, 5 and 6 December – exactly the days Leo worked. On 2 and 4 December, when he was off, there were none (clues 1, 2)."],
   "cleared": ["<b>Amy</b> worked on 2 and 4 December when there were no refunds, and missed 3 and 6 (clue 2). <b>Joe</b> was off on 1 and 5 December (clue 2).",
               "<b>Ivy</b> only wrapped presents on days without refunds, and <b>Sam</b> found the trick (clues 5, 6)."]},
}

# ---------------------------------------------------------------- BELL TOWER (L3)
bell = {
 "slug": "death-in-the-bell-tower", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 184", "title_html": "DEATH IN THE<br>BELL TOWER", "title_plain": "Death in the Bell Tower",
 "teaser": "The tower captain falls to his death during New Year bell practice. A peal sheet, a missed bell and a dusty ladder show who was really in the tower.",
 "intro": "At <b>St Aldhelm's Church</b>, tower captain Walter Penrose fell through the trapdoor of the bell chamber during practice for the New Year peal. He did not fall by accident. " + STD,
 "clues": [
  {"name": "DS Holly Grey", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Penrose fell from the bell chamber to the ringing room floor. The trapdoor bolt had been drawn back, and there was a scuffle in the dust up there.",
   "evidence": ev_rows("Police report – St Aldhelm's", [
       ("Fall", "During the practice – exact time from the peal sheet"),
       ("Bell chamber", "Trapdoor bolt drawn back; scuffle marks in thick dust"),
       ("Dust", "Grey belfry dust on the ladder rungs"),
       ("Bells", "Six bells, each rung by one ringer"),
     ])},
  {"name": "Martin Hale", "role": "Ringer, bell 4", "label": "MARTIN'S STATEMENT",
   "quote": "I rang bell four for the whole practice. If I'd stopped, everyone would have heard – the change would have fallen apart.",
   "evidence": ev_rows("Tower accounts – note from W. Penrose", [
       ("Found", "£1,800 missing from the bell restoration fund"),
       ("Treasurer", "Martin Hale"),
       ("Walter's note", "“Tell the vicar after practice. Martin must explain.”"),
     ])},
  {"name": "Eileen Shaw", "role": "Conductor, bell 1", "label": "PEAL SHEET",
   "quote": "I conduct from bell one. I write down every change and anything that goes wrong.",
   "evidence": ev_table("Practice sheet – 28 Dec", ["Time", "Change", "Note"], [
       ("19:00", "Rounds", "All six bells"),
       ("19:20", "Plain Bob", "All six bells"),
       ("19:40", "Plain Bob", "Bell 4 missing – rang on five bells"),
       ("19:52", "Crash from above – stopped", "Bell 4 back at 19:51"),
     ], mono_cols=(0,))},
  {"name": "Tom Akers", "role": "Ringer, bell 6", "label": "TOM'S NOTE",
   "quote": "At about twenty to eight Martin said he'd tie off his rope for a minute and go up to check a 'rattle' in the bell chamber. Walter had gone up a few minutes earlier for the same reason.",
   "evidence": ev_note("TOM'S NOTE", [
       "19:36 – Walter goes up the ladder",
       "to look at a rattle.",
       "19:39 – Martin ties his rope, goes up.",
       "19:51 – Martin back, dust on knees."],
     "– Tom")},
  {"name": "Jean Penrose", "role": "Walter's wife, bell 2", "label": "JEAN'S STATEMENT",
   "quote": "Walter and I hadn't been happy, I won't lie. But I never left my bell – Eileen would have written it down.",
   "evidence": ev_photos("Choir member's phone (outside church)", [
       ("IMG_3301", "19:45", "Through the ringing room window: five ringers at their ropes, Jean Penrose at bell 2."),
     ])},
  {"name": "Rev. Alan Moss", "role": "Vicar", "label": "VICAR'S NOTE",
   "quote": "I was in the vestry writing my sermon. The only way up to the bell chamber is the ladder from the ringing room.",
   "evidence": ev_rows("Tower access", [
       ("Bell chamber", "Reached only by the ladder from the ringing room"),
       ("Outside door", "Locked at 18:45 by the vicar"),
       ("Vestry", "Rev. Moss, 18:30–20:00 – seen by the organist"),
     ])},
 ],
 "solution": {"killer": "Martin Hale",
   "motive": "Walter had found £1,800 missing from the fund Martin looked after and was going to tell the vicar (clue 2).",
   "proof": ["Walter fell from the bell chamber, which you can only reach by the ladder from the ringing room (clues 1, 6). The crash came at 19:52 (clue 3).",
             "Martin says he rang the whole time, but bell 4 – his bell – was missing from 19:40 until 19:51 (clue 3).",
             "Tom saw Martin follow Walter up the ladder at 19:39 and come back at 19:51 with dust on his knees (clue 4)."],
   "cleared": ["<b>Jean</b> was photographed ringing bell 2 at 19:45 (clue 5), and <b>Eileen</b> and <b>Tom</b> were ringing.",
               "<b>Rev. Moss</b> was in the vestry with the outside door locked (clue 6)."]},
}

# ---------------------------------------------------------------- SKATING GALA (L3)
skate = {
 "slug": "murder-at-the-skating-gala", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 185", "title_html": "MURDER AT THE<br>SKATING GALA", "title_plain": "Murder at the Skating Gala",
 "teaser": "A famous skating coach is found dead in the rink's plant room during the winter gala. Music cues, a skate-blade cut and a guard's log expose the killer.",
 "intro": "At the <b>Crystal Ice Arena</b>, coach Viktor Hale was found dead in the ice plant room during the winter skating gala, struck with a heavy wrench. " + STD,
 "clues": [
  {"name": "DI Ruth Kemp", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Hale was killed in the plant room. On the rubber floor there's a fresh cut – the kind only a skate blade makes. The killer came in with skates on.",
   "evidence": ev_rows("Police report – Crystal Ice Arena", [
       ("Found", "21:10, ice plant room"),
       ("Time of death", "Between 20:30 and 20:45"),
       ("Weapon", "Wrench from the plant room wall"),
       ("Floor", "Fresh blade cut in the rubber – skater wearing skates"),
     ])},
  {"name": "Lara Quinn", "role": "Skater", "label": "LARA'S STATEMENT",
   "quote": "I was on the ice performing my solo at half past eight. Three minutes of music, then I bowed and went straight to the dressing room.",
   "evidence": ev_rows("Viktor Hale's email to the federation", [
       ("Subject", "Lara Quinn – team selection"),
       ("Text", "“I will not pick Lara for the championship team. I'll tell her after the gala.”"),
     ])},
  {"name": "Ben Ortiz", "role": "Sound technician", "label": "MUSIC CUES",
   "quote": "I play every skater's music. Lara's solo didn't start at half eight – it was swapped, and she went on later.",
   "evidence": ev_table("Gala music cues (as played)", ["Time", "Skater", "Music"], [
       ("20:25", "Kim Lowe", "Swan Lake (3 min)"),
       ("20:30", "Kim Lowe", "Extra encore medley (10 min) – order swapped"),
       ("20:48", "Lara Quinn", "Solo (3 min)"),
       ("20:55", "Finale", "All skaters"),
     ], mono_cols=(0,))},
  {"name": "Dave Pike", "role": "Security guard", "label": "CORRIDOR LOG",
   "quote": "I sat by the corridor that goes from the rink side to the plant room. One skater went down there in costume – with her skates still on, clacking on the floor.",
   "evidence": ev_note("SECURITY LOG – PLANT CORRIDOR", [
       "20:31 – skater in silver costume,",
       "skates on, guards off, went down",
       "to plant room. 20:41 – back, fast.",
       "Number on back: 7."],
     "– Dave")},
  {"name": "Kim Lowe", "role": "Skater", "label": "KIM'S STATEMENT",
   "quote": "I was on the ice from twenty-five past eight to twenty to nine – I did my piece and an extra encore because Lara wasn't ready.",
   "evidence": ev_table("Gala programme – skater numbers", ["No.", "Skater", "Costume"], [
       ("3", "Kim Lowe", "Blue"),
       ("7", "Lara Quinn", "Silver"),
       ("9", "Ellie Hart", "Green"),
     ])},
  {"name": "Ellie Hart", "role": "Skater", "label": "ELLIE'S STATEMENT",
   "quote": "I hurt my ankle in warm-up, so I sat in the first-aid room with skates off and ice on my foot from eight o'clock.",
   "evidence": ev_rows("First-aid room sheet", [
       ("Patient", "Ellie Hart – sprained ankle"),
       ("In", "20:00"),
       ("Out", "21:30 – sent home, skates off"),
       ("Nurse", "With her the whole time"),
     ])},
 ],
 "solution": {"killer": "Lara Quinn",
   "motive": "Viktor was going to leave Lara out of the championship team (clue 2).",
   "proof": ["Viktor died between 20:30 and 20:45 in the plant room, killed by someone wearing skates (clue 1).",
             "Lara says she was skating her solo at 20:30, but the order was swapped: Kim did an encore at 20:30 and Lara only skated at 20:48 (clue 3).",
             "At 20:31 a skater in a silver costume with number 7, skates on, went to the plant room and came back at 20:41 (clue 4). Number 7 in silver is Lara (clue 5)."],
   "cleared": ["<b>Kim</b> was on the ice from 20:25 to 20:40 and wears blue number 3 (clues 3, 5).",
               "<b>Ellie</b> was in first aid with a nurse, skates off (clue 6). <b>Ben</b> was playing music and <b>Dave</b> was at his post (clues 3, 4)."]},
}

MYSTERIES = [ginger, toy, bell, skate]
