from lib import *  # evidence helpers

# Round 16 (18 Nov): 1 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- MARATHON (L2)
marathon = {
 "slug": "the-marathon-shortcut", "level": 2, "crime": "FRAUD", "who": "cheat", "added": ADDED,
 "caseno": "CASE NO. 131", "title_html": "THE MARATHON<br>SHORTCUT", "title_plain": "The Marathon Shortcut",
 "teaser": "An amateur wins the city marathon in a record time – and the timing chips say something impossible happened between 25 and 30 kilometres.",
 "intro": "At the <b>Riverside City Marathon</b>, a surprise winner set a course record in the women's race. The runner-up has lodged a complaint: someone took a shortcut. " + STD,
 "clues": [
  {"name": "Paula Kerr", "role": "Race referee", "label": "COMPLAINT",
   "quote": "The runner-up says she never saw the winner pass her. We have timing mats every five kilometres, so the chips will tell us who ran the whole course.",
   "evidence": ev_rows("Official complaint", [
       ("From", "Joanna Wilde, 2nd place"),
       ("Claim", "“The winner was behind me at 20 km and I was never overtaken.”"),
       ("Course", "Out along the river to 25 km, back through the park to 30 km"),
       ("Short cut", "The footbridge links 25 km and 30 km directly: 600 m instead of 5 km"),
     ])},
  {"name": "Danny Holt", "role": "Timing manager", "label": "WINNER'S SPLITS",
   "quote": "The chip data are clean – no faults on any mat. I've pulled the splits for the top three women.",
   "evidence": ev_table("Chip splits – women's race", ["Runner", "20 km", "25 km", "30 km", "Finish"], [
       ("Rachel Moss", "1:12:40", "1:31:05", "1:33:58", "2:22:10"),
       ("Joanna Wilde", "1:12:31", "1:30:50", "1:48:55", "2:37:30"),
       ("Kate Ferris", "1:14:02", "1:32:44", "1:51:10", "2:40:02"),
     ], mono_cols=(1, 2, 3, 4))},
  {"name": "Rachel Moss", "role": "Winner", "label": "RACHEL'S STATEMENT",
   "quote": "I just felt amazing after 25 km – I had a gel, found a second wind and flew. I've trained for two years for this. Joanna is a bad loser.",
   "evidence": ev_rows("Rachel Moss – race record", [
       ("Best marathon before", "3:05:12 (last spring)"),
       ("This race", "2:22:10 – course record"),
       ("Prize", "£5,000 and a sponsored place at Boston"),
     ])},
  {"name": "Kate Ferris", "role": "Third place", "label": "MARSHAL'S PHOTO",
   "quote": "I ran my own race – I didn't see anyone go over the bridge. But I did hear a marshal shouting at somebody near the park.",
   "evidence": ev_photos("Marshal photo, footbridge", [
       ("IMG_0451", "1:31:40 race time", "A runner in a yellow vest crossing the footbridge towards the park. The marshal is waving her back."),
     ])},
  {"name": "Sam Ortiz", "role": "Kit sponsor", "label": "VEST LIST",
   "quote": "We supplied coloured vests to the top seeds so the TV cameras could pick them out. Every colour was different.",
   "evidence": ev_table("Seeded vests – women", ["Runner", "Vest"], [
       ("Joanna Wilde", "Blue"),
       ("Kate Ferris", "Green"),
       ("Rachel Moss", "Yellow"),
       ("Ama Boateng (dropped out at 12 km)", "Red"),
     ])},
  {"name": "Joanna Wilde", "role": "Runner-up", "label": "TV GRAPHICS",
   "quote": "I've been running for fifteen years. I know when somebody passes me – and nobody did.",
   "evidence": ev_rows("TV leaderboard at 27 km", [
       ("1", "J. Wilde (blue)"),
       ("2", "K. Ferris (green)"),
       ("Note", "No yellow vest seen on the river section after 25 km"),
     ])},
 ],
 "solution": {"killer": "Rachel Moss",
   "motive": "A course record brought £5,000 and a sponsored place at Boston (clue 3) – far beyond her previous best of 3:05.",
   "proof": ["Rachel ran 25 km to 30 km in 2 minutes 53 seconds (clue 2) – faster than any human can run 5 km. The footbridge links the two mats in just 600 m (clue 1).",
             "The marshal photographed a yellow-vested runner crossing the footbridge at 1:31:40 race time (clue 4), just after Rachel's 25 km split. Yellow was Rachel's vest (clue 5), and the TV saw no yellow vest on the river section (clue 6)."],
   "cleared": ["<b>Joanna</b> and <b>Kate</b> have normal 25–30 km splits of about 18 minutes (clue 2).",
               "<b>Ama</b>, the only other seed, dropped out at 12 km (clue 5).",
               "<b>Paula</b>, <b>Danny</b> and <b>Sam</b> are officials and a sponsor, not runners."]},
}

# ---------------------------------------------------------------- ORCHID (L3)
orchid = {
 "slug": "the-orchid-house-murder", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 132", "title_html": "THE ORCHID<br>HOUSE MURDER", "title_plain": "The Orchid House Murder",
 "teaser": "A famous orchid collector dies among his flowers. The heating log, the misting system and one very rare bloom tell the story his guests will not.",
 "intro": "At <b>Thornfield Manor</b>, orchid collector Sir Roland Hythe was found dead in his heated glasshouse on the night of a small dinner party. " + STD,
 "clues": [
  {"name": "Dr Eva Marsh", "role": "Police surgeon", "label": "POST-MORTEM",
   "quote": "Sir Roland was struck on the head and fell among the benches. In that heat the body tells me little – but his wristwatch stopped when it hit the iron edge of the bench.",
   "evidence": ev_rows("Post-mortem notes", [
       ("Found", "23:45, glasshouse, by the butler"),
       ("Cause", "Blow to the head"),
       ("Watch", "Stopped at 22:20, glass cracked"),
       ("Glasshouse", "Kept at 28 °C; misting runs every 10 minutes"),
     ])},
  {"name": "Hugo Hythe", "role": "Nephew", "label": "GLASSHOUSE SYSTEM LOG",
   "quote": "I was in the billiard room with Felicity all evening after dinner. Uncle Roland went to check his orchids at about ten. That's the last I saw of him.",
   "evidence": ev_table("Glasshouse controller", ["Time", "Event"], [
       ("22:10", "Misting cycle"),
       ("22:12", "Door opened"),
       ("22:18", "Door opened"),
       ("22:20", "Misting cycle"),
       ("22:22", "Door opened"),
       ("22:30", "Misting cycle"),
       ("22:41", "Door opened"),
       ("23:45", "Door opened"),
     ], mono_cols=(0,))},
  {"name": "Felicity Crane", "role": "Rival collector", "label": "BILLIARD SCORES",
   "quote": "Roland and I competed for twenty years. But Hugo and I played billiards from half nine until the butler raised the alarm. I never set foot in that glasshouse.",
   "evidence": ev_table("Billiard room – score pad", ["Frame", "Hugo", "Felicity", "Ended"], [
       ("1", "41", "56", "21:58"),
       ("2", "62", "38", "22:24"),
       ("3", "30", "71", "22:55"),
       ("4", "48", "45", "23:40"),
     ], mono_cols=(3,))},
  {"name": "Mrs Agnes Doyle", "role": "Housekeeper", "label": "WET CLOTHES",
   "quote": "Mr Pryce came into the kitchen at about twenty-five past ten asking for a towel – his jacket was soaked through on the shoulders. He said he'd been out for some air and got caught in the rain.",
   "evidence": ev_rows("Met Office – Thornfield, that night", [
       ("Rain", "None from 18:00 to 06:00"),
       ("Sky", "Clear, light frost"),
       ("Temperature at 22:00", "1 °C"),
     ])},
  {"name": "Gerald Pryce", "role": "Business partner", "label": "CATALOGUE NOTE",
   "quote": "I was out in the garden for some air between ten and half past – the house was stuffy. I never went into the glasshouse. Why would I? I hate the heat.",
   "evidence": ev_rows("Sir Roland's catalogue, last entry", [
       ("Plant", "Ghost orchid, the only one in England"),
       ("Valued", "£80,000"),
       ("Note", "“Gerald wants to sell it to the Dutch buyer behind my back. Over my dead body.”"),
     ])},
  {"name": "Simon Ward", "role": "Butler", "label": "BUTLER'S ROUNDS",
   "quote": "I took Sir Roland a cup of cocoa at twenty to eleven. He didn't answer, and I assumed he'd gone up. At quarter to midnight I found him.",
   "evidence": ev_rows("Butler's notes", [
       ("22:41", "Cocoa to the glasshouse – lights on, no answer, cup left by the door"),
       ("23:45", "Glasshouse – found Sir Roland"),
       ("Note", "Ghost orchid missing from its bench; found in a box in the boot of G. Pryce's car"),
     ])},
 ],
 "solution": {"killer": "Gerald Pryce",
   "motive": "Gerald wanted to sell the £80,000 ghost orchid to a Dutch buyer, and Sir Roland had refused (clue 5).",
   "proof": ["Sir Roland's watch stopped at 22:20 (clue 1). The glasshouse door opened at 22:12 (Roland) and again at 22:18 (clue 2) – the killer.",
             "Gerald says he was in the garden and was soaked by rain, but there was no rain that night (clue 4). The only wet place was the glasshouse, where the misting system sprayed at 22:20 (clues 1, 2). He came in at 22:18, struck at 22:20 and left at 22:22 – his wet shoulders put him inside – and the stolen orchid was in his car (clue 6)."],
   "cleared": ["<b>Hugo</b> and <b>Felicity</b> were playing billiards, with frames ending at 22:24 and 22:55 (clue 3).",
               "<b>Simon</b> opened the door at 22:41 with the cocoa (clues 2, 6) – after the death.",
               "<b>Mrs Doyle</b> was in the kitchen, where Gerald came for a towel (clue 4)."]},
}

MYSTERIES = [marathon, orchid]
