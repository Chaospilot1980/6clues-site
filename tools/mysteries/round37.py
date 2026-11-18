from lib import *  # evidence helpers

# Round 37 (18 Nov): 2 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- NEWSPAPER LEAK (L2)
leak = {
 "slug": "the-newspaper-scoop-leak", "level": 2, "crime": "SABOTAGE", "who": "saboteur", "added": ADDED,
 "caseno": "CASE NO. 210", "title_html": "THE NEWSPAPER<br>SCOOP LEAK", "title_plain": "The Newspaper Scoop Leak",
 "teaser": "A local paper's front-page scoop appears on a rival's website an hour before printing. A deliberate typo, a printer log and a phone call catch the leaker.",
 "intro": "At the <b>Westbury Gazette</b>, editor Moira Kerr's big story about the town council was posted by the rival <i>Westbury Echo</i> one hour before the Gazette went to print. Someone inside leaked it. " + STD,
 "clues": [
  {"name": "Moira Kerr", "role": "Editor", "label": "EDITOR'S NOTE",
   "quote": "Only four of us saw the story before printing. I always put a tiny different mistake in each person's copy – so I know exactly whose copy leaked.",
   "evidence": ev_table("Editor's secret typos", ["Copy for", "Hidden mistake"], [
       ("Sports desk – Ian", "'councilor' (one L)"),
       ("Subeditor – Tess", "'Thurdsay'"),
       ("Photo desk – Leon", "'£2.4 milion'"),
       ("Night editor – Alex", "'recieved'"),
     ])},
  {"name": "Tess Brook", "role": "Subeditor", "label": "TESS'S STATEMENT",
   "quote": "I've been here twelve years. I'd never leak to the Echo – I worked late that night checking every page right here at my desk.",
   "evidence": ev_rows("The Echo's website – posted 21:02", [
       ("Headline", "Council's secret £2.4 million deal"),
       ("Text", "“...the deal was signed on Thurdsay in a private meeting...”"),
       ("Byline", "Echo staff"),
     ])},
  {"name": "Ian Doyle", "role": "Sports editor", "label": "IAN'S STATEMENT",
   "quote": "I only glanced at the story – I was busy with the football results all evening. I left at eight.",
   "evidence": ev_rows("Building door log", [
       ("I. Doyle", "Out 20:04"),
       ("T. Brook", "Out 21:40"),
       ("L. Ward", "Out 19:30"),
       ("A. Fry", "Out 22:30"),
     ])},
  {"name": "Sid Mallon", "role": "IT manager", "label": "PRINTER LOG",
   "quote": "Somebody printed a copy of the story at 20:30 on the subeditors' printer and then emailed a scan. The email was deleted, but the scan record stays.",
   "evidence": ev_table("Printer and scan log", ["Time", "Job", "User"], [
       ("20:30", "Print – 'council_story_v4'", "tbrook"),
       ("20:34", "Scan to email – 2 pages", "tbrook"),
     ], mono_cols=(0,))},
  {"name": "Leon Ward", "role": "Photographer", "label": "LEON'S STATEMENT",
   "quote": "I left at half seven to photograph a fire. I never even read the full story – I just needed the headline for the picture.",
   "evidence": ev_rows("Echo job advert", [
       ("Job", "Chief subeditor – Westbury Echo"),
       ("Starts", "January"),
       ("Note on Tess's desk", "“Interview Monday – Echo – don't tell Moira.”"),
     ])},
  {"name": "Alex Fry", "role": "Night editor", "label": "PHONE LOG",
   "quote": "I stayed till the paper went to print. At about twenty to nine I heard Tess on her mobile saying 'it's on its way to you now'.",
   "evidence": ev_note("ALEX'S NOTE", [
       "About 20:40 – Tess on mobile, quiet:",
       "'It's on its way to you now. You",
       "owe me.' Hung up when she saw me.",
       "Strange."],
     "– Alex")},
 ],
 "solution": {"killer": "Tess Brook",
   "motive": "Tess had a job interview at the Echo (clue 5).",
   "proof": ["Each copy had its own secret mistake (clue 1). The Echo's story says 'Thurdsay' – the mistake only in Tess's copy (clues 1, 2).",
             "Tess says she'd never leak, but her login printed and scanned the story to email at 20:30–20:34 (clue 4).",
             "At about 20:40 Alex heard her say on the phone: 'It's on its way to you now' (clue 6)."],
   "cleared": ["<b>Ian</b> left at 20:04 and <b>Leon</b> at 19:30, before the scan (clue 3). Their copies had different mistakes (clue 1).",
               "<b>Alex</b>'s copy said 'recieved', not 'Thurdsay' (clue 1); <b>Moira</b> and <b>Sid</b> found the leak."]},
}

# ---------------------------------------------------------------- RACEHORSE (L2)
horse = {
 "slug": "the-racehorse-doping", "level": 2, "crime": "SABOTAGE", "who": "saboteur", "added": ADDED,
 "caseno": "CASE NO. 211", "title_html": "THE RACEHORSE<br>DOPING", "title_plain": "The Racehorse Doping",
 "teaser": "The favourite in the Boxing Day race runs like a carthorse – and a test finds a sleeping drug. A stable log, a carrot bag and a betting slip expose who did it.",
 "intro": "At <b>Kempfield Racecourse</b>, the favourite, Silver Comet, finished last in the Boxing Day Chase. A test showed he had been given a sleeping drug that morning. " + STD,
 "clues": [
  {"name": "Dr Fiona Hart", "role": "Racecourse vet", "label": "VET REPORT",
   "quote": "The drug works in two to three hours. Silver Comet ran at two o'clock, so he was given it between eleven and twelve – mixed into food.",
   "evidence": ev_rows("Vet report – Silver Comet", [
       ("Drug", "Sedative – crushed tablets"),
       ("Given", "Between 11:00 and 12:00, in food"),
       ("Stomach", "Carrot pieces with white powder"),
       ("Race", "14:00"),
     ])},
  {"name": "Jake Turner", "role": "Stable lad", "label": "JAKE'S STATEMENT",
   "quote": "I look after Silver Comet, but I love that horse. I was walking the other horses from eleven till twelve – I never went into his box.",
   "evidence": ev_rows("Bookmaker's betting slip", [
       ("Bet", "£500 – Silver Comet to LOSE (lay bet)"),
       ("Placed", "Boxing Day, 09:15"),
       ("Account", "J. Turner"),
     ])},
  {"name": "Mags Pell", "role": "Head groom", "label": "STABLE LOG",
   "quote": "Everyone signs in and out of the stable block. The horses are walked from eleven – Jake took three of them out, but he was back much earlier than the others.",
   "evidence": ev_table("Stable block log – Boxing Day", ["Time", "Name", "In/Out"], [
       ("11:00", "J. Turner", "Out – walking 3 horses"),
       ("11:20", "J. Turner", "In – 'forgot his gloves'"),
       ("11:28", "J. Turner", "Out"),
       ("12:05", "J. Turner", "In – horses back"),
     ], mono_cols=(0,))},
  {"name": "Owen Price", "role": "Jockey", "label": "OWEN'S STATEMENT",
   "quote": "I didn't go near the stables in the morning – I was in the weighing room with the other jockeys from ten.",
   "evidence": ev_rows("Weighing room register", [
       ("O. Price", "In 10:02, stayed until 13:40"),
       ("Clerk", "Saw him the whole time"),
     ])},
  {"name": "Gail Hunt", "role": "Feed store manager", "label": "CARROT BAG",
   "quote": "The carrots for the horses are kept in the feed store. Somebody took a bag of carrots and left it in Silver Comet's box – with a stable lad's glove inside.",
   "evidence": ev_photos("Feed store photos", [
       ("IMG_330", "15:00", "Paper carrot bag in Silver Comet's box, white powder in the bottom, and a green work glove with 'J.T.' written on the cuff."),
     ])},
  {"name": "Rory Blythe", "role": "Owner of a rival horse", "label": "RORY'S STATEMENT",
   "quote": "My horse won, so of course people suspect me. But I arrived at the course at half past twelve – my car park ticket shows it.",
   "evidence": ev_rows("Owners' car park ticket", [
       ("Car", "R. Blythe"),
       ("In", "12:31"),
     ])},
 ],
 "solution": {"killer": "Jake Turner",
   "motive": "Jake bet £500 that Silver Comet would lose (clue 2).",
   "proof": ["Silver Comet was given crushed tablets in carrots between 11:00 and 12:00 (clue 1).",
             "Jake says he was walking horses the whole time, but he came back to the stable block from 11:20 to 11:28 to 'fetch his gloves' (clue 3).",
             "A carrot bag with powder and a glove marked 'J.T.' was found in Silver Comet's box (clue 5)."],
   "cleared": ["<b>Owen</b> was in the weighing room from 10:02 (clue 4), and <b>Rory</b> arrived at 12:31 (clue 6).",
               "<b>Mags</b>, <b>Gail</b> and <b>Dr Hart</b> only report what they found."]},
}

# ---------------------------------------------------------------- SPACE CAMP (L3)
space = {
 "slug": "death-at-the-space-camp", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 212", "title_html": "DEATH AT THE<br>SPACE CAMP", "title_plain": "Death at the Space Camp",
 "teaser": "The director of a space training camp dies inside the spinning centrifuge. Mission control logs, a spacesuit badge and a timed countdown prove it was murder.",
 "intro": "At the <b>Polaris Space Training Camp</b>, director Dr Hugo Brandt was found dead inside the training centrifuge after it had been run at dangerous speed with the safety lock removed. " + STD,
 "clues": [
  {"name": "DI Nora Pike", "role": "Police", "label": "POLICE REPORT",
   "quote": "Somebody locked Dr Brandt inside the centrifuge capsule and started it from the control room at full speed. It needs a personal access badge to start.",
   "evidence": ev_rows("Police report – Polaris Camp", [
       ("Found", "21:50, centrifuge capsule"),
       ("Centrifuge run", "21:05 to 21:20 at maximum speed"),
       ("Safety lock", "Removed by hand"),
       ("Control panel", "Starts only with a staff badge"),
     ])},
  {"name": "Kai Moreno", "role": "Senior trainer", "label": "KAI'S STATEMENT",
   "quote": "I was in the planetarium giving the evening star talk to the cadets from nine until ten. Sixty kids saw me.",
   "evidence": ev_rows("Email from Dr Brandt to the board", [
       ("Subject", "Kai Moreno"),
       ("Text", "“Kai faked his training records. I'm firing him tomorrow morning.”"),
       ("Sent", "That afternoon"),
     ])},
  {"name": "Tara Lin", "role": "Planetarium technician", "label": "SHOW LOG",
   "quote": "Kai started the star talk, but at five to nine he switched to the pre-recorded 'Journey to Mars' film – 30 minutes – and slipped out. He came back for the questions.",
   "evidence": ev_table("Planetarium – evening show", ["Time", "Part", "Presenter"], [
       ("20:45–20:55", "Live star talk", "K. Moreno"),
       ("20:55–21:25", "Film: Journey to Mars", "Recorded"),
       ("21:25–22:00", "Live questions", "K. Moreno"),
     ], mono_cols=(0,))},
  {"name": "Sam Okafor", "role": "IT and security", "label": "BADGE LOG",
   "quote": "Every badge swipe is recorded. The centrifuge was started with one badge only.",
   "evidence": ev_table("Badge log – centrifuge hall", ["Time", "Door / panel", "Badge"], [
       ("20:58", "Centrifuge hall door", "K. Moreno"),
       ("21:04", "Control panel – START", "K. Moreno"),
       ("21:21", "Centrifuge hall door – exit", "K. Moreno"),
     ], mono_cols=(0,))},
  {"name": "Dr Ellen Wu", "role": "Camp doctor", "label": "ELLEN'S STATEMENT",
   "quote": "Hugo and I argued about the budget, but I was in the medical bay all evening treating a cadet with a twisted ankle.",
   "evidence": ev_rows("Medical bay log", [
       ("Patient", "Cadet J. Bell – twisted ankle"),
       ("Treated by", "Dr E. Wu, 20:40–21:45"),
     ])},
  {"name": "Cadet Mia Ross", "role": "Trainee, aged 16", "label": "MIA'S NOTE",
   "quote": "I needed the toilet during the Mars film. In the corridor I saw Mr Moreno running back from the centrifuge hall, straightening his flight jacket.",
   "evidence": ev_note("MIA'S JOURNAL", [
       "Mars film – went to the loo at",
       "about 21:22. Saw Mr Moreno coming",
       "from the centrifuge hall, out of",
       "breath. He said 'Back to your seat!'"],
     "– Mia")},
 ],
 "solution": {"killer": "Kai Moreno",
   "motive": "Dr Brandt was going to fire Kai for faking training records (clue 2).",
   "proof": ["The centrifuge was started with a staff badge and ran from 21:05 to 21:20 (clue 1).",
             "Kai says he was giving the star talk from nine to ten, but from 20:55 to 21:25 a recorded film played and he slipped out (clue 3).",
             "His badge opened the centrifuge hall at 20:58, started the machine at 21:04 and left at 21:21 (clue 4), and Mia saw him running back from the hall at about 21:22 (clue 6)."],
   "cleared": ["<b>Dr Wu</b> was treating a cadet from 20:40 to 21:45 (clue 5).",
               "<b>Tara</b> ran the planetarium, and <b>Sam</b> and <b>Mia</b> only report what they saw (clues 3, 4, 6)."]},
}

# ---------------------------------------------------------------- ORCHESTRA (L3)
orchestra = {
 "slug": "murder-at-the-new-year-concert", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 213", "title_html": "MURDER AT THE<br>NEW YEAR CONCERT", "title_plain": "Murder at the New Year Concert",
 "teaser": "A conductor is found dead in his dressing room during the interval of the New Year concert. The musical score itself shows which player was not playing.",
 "intro": "At the <b>Royal Albion Hall</b>, conductor Sir Julian Frost was found dead in his dressing room during the New Year's Eve concert. He had been hit with a heavy metronome. " + STD,
 "clues": [
  {"name": "DS Alice Vane", "role": "Police", "label": "POLICE REPORT",
   "quote": "Sir Julian was killed during the second half – while the orchestra played the Waltz Suite without a conductor, led by the first violin. He'd gone to his room with a headache.",
   "evidence": ev_rows("Police report – Royal Albion Hall", [
       ("Sir Julian left stage", "21:10 – 'headache'"),
       ("Found", "21:50, dressing room 1"),
       ("Time of death", "21:15–21:35"),
       ("Weapon", "Brass metronome – from the instrument store"),
     ])},
  {"name": "Clara Novak", "role": "First flute", "label": "CLARA'S STATEMENT",
   "quote": "I played every note of the Waltz Suite. Ask anyone in the woodwind section – I was in my chair the whole time.",
   "evidence": ev_rows("Letter from Sir Julian to C. Novak", [
       ("Subject", "Your position"),
       ("Text", "“After tonight, you will no longer be first flute. I have found someone better.”"),
       ("Date", "Handed to her at the interval"),
     ])},
  {"name": "Felix Gray", "role": "Orchestra librarian", "label": "SCORE",
   "quote": "In the Waltz Suite, the flutes have a long rest – twenty minutes without a single note in movements two and three. Players often slip out.",
   "evidence": ev_table("Waltz Suite – flute part", ["Time", "Movement", "Flute"], [
       ("21:10", "1. Grand Waltz", "Playing"),
       ("21:14", "2. Night Waltz", "Rest – 11 min"),
       ("21:25", "3. Snow Waltz", "Rest – 9 min"),
       ("21:34", "4. Finale", "Playing – solo"),
     ], mono_cols=(0,))},
  {"name": "Mo Akhtar", "role": "Stage manager", "label": "BACKSTAGE NOTE",
   "quote": "The stage door to the dressing room corridor is right behind the woodwind section. At about quarter past nine it opened and closed – I saw a woman in black with a silver hairclip go through.",
   "evidence": ev_note("STAGE MANAGER'S SHEET", [
       "21:15 – woodwind player, black",
       "dress, silver hairclip, through",
       "stage door. 21:32 – back in.",
       "Played the flute solo at 21:34."],
     "– Mo")},
  {"name": "Ruth Hale", "role": "Second flute", "label": "RUTH'S STATEMENT",
   "quote": "I sat next to Clara. At the start of the Night Waltz she whispered 'back in a minute' and left. I stayed in my chair.",
   "evidence": ev_photos("Audience member's photo (no flash)", [
       ("IMG_7742", "21:20", "Woodwind section during the Night Waltz: the first flute chair empty, flute resting on the seat. Second flute Ruth Hale in her chair, red hairband."),
     ])},
  {"name": "Peter Lang", "role": "First violin, leader", "label": "PETER'S STATEMENT",
   "quote": "I led the orchestra from my chair after Sir Julian left. I couldn't stop playing for a second – violins never rest in the waltzes.",
   "evidence": ev_table("Waltz Suite – first violin part", ["Movement", "Violin"], [
       ("1–4", "Playing throughout – no rests"),
     ])},
 ],
 "solution": {"killer": "Clara Novak",
   "motive": "Sir Julian was removing Clara as first flute (clue 2).",
   "proof": ["Sir Julian was killed between 21:15 and 21:35 (clue 1).",
             "Clara says she played every note, but the flutes rest from 21:14 to 21:34 (clue 3), and a photo at 21:20 shows the first flute chair empty (clue 5).",
             "At 21:15 Mo saw a woodwind player with a silver hairclip go through the stage door and come back at 21:32 – then play the flute solo at 21:34, which is Clara's part (clues 3, 4)."],
   "cleared": ["<b>Ruth</b> is in the photo in her chair at 21:20 (clue 5), and <b>Peter</b> led the orchestra with no rests (clue 6).",
               "<b>Felix</b> and <b>Mo</b> only report what they know (clues 3, 4)."]},
}

MYSTERIES = [leak, horse, space, orchestra]
