from lib import *  # evidence helpers

# Round 16 (18 Nov): 1 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- ICE RINK (L2)
rink = {
 "slug": "the-ice-rink-sabotage", "level": 2, "crime": "SABOTAGE", "who": "saboteur", "added": ADDED,
 "caseno": "CASE NO. 131", "title_html": "THE ICE RINK<br>SABOTAGE", "title_plain": "The Ice Rink Sabotage",
 "teaser": "The favourite's skate blade snaps loose mid-routine. Someone loosened the screws – and one rival swears she was in the stands all along.",
 "intro": "At the <b>Northern Figure Skating Championships</b>, favourite Lena Novak fell when the blade came off her right skate. Two of its four screws had been loosened. " + STD,
 "clues": [
  {"name": "Lena Novak", "role": "Skater", "label": "INCIDENT REPORT",
   "quote": "I checked my skates myself at four o'clock – every screw tight, as always. Then I left them in my locker and went to warm up off the ice.",
   "evidence": ev_rows("Incident report", [
       ("Fall", "18:42, during the free skate"),
       ("Damage", "Two blade screws loosened by several turns"),
       ("Skates", "In locker 6, changing room B, from 16:00 to 18:20"),
       ("Locker", "Not locked – changing room B is for competitors only"),
     ])},
  {"name": "Bianca Rossi", "role": "Rival skater", "label": "BIANCA'S STATEMENT",
   "quote": "I was in the stands watching the pairs from five until six. I never went into changing room B. Lena and I don't get on, but I'd never do something like that.",
   "evidence": ev_rows("Championship standings before the free skate", [
       ("1", "L. Novak – 74.20"),
       ("2", "B. Rossi – 71.85"),
       ("3", "M. Sato – 70.10"),
       ("Prize", "Place on the national team for the Europeans"),
     ])},
  {"name": "Joe Pike", "role": "Ice technician", "label": "ICE SCHEDULE",
   "quote": "The rink was closed for resurfacing between five and six – the pairs final was moved to tomorrow because the ice machine broke down.",
   "evidence": ev_table("Arena schedule – Saturday (as changed)", ["Time", "Event"], [
       ("16:00", "Junior men"),
       ("17:00–18:00", "Rink closed – ice resurfacing; stands empty"),
       ("17:00", "Pairs final – POSTPONED to Sunday"),
       ("18:30", "Ladies' free skate"),
     ], mono_cols=(0,))},
  {"name": "Mika Sato", "role": "Skater", "label": "PHYSIO LOG",
   "quote": "I was with the physio from five until nearly six – my ankle has been bad all season. Then I warmed up in the gym.",
   "evidence": ev_table("Physio room – Saturday", ["Time", "Patient"], [
       ("16:30", "J. Kerr"),
       ("17:00", "M. Sato"),
       ("17:50", "M. Sato leaves"),
       ("18:00", "L. Novak"),
     ], mono_cols=(0,))},
  {"name": "Ruth Hale", "role": "Changing room steward", "label": "STEWARD'S NOTES",
   "quote": "I sat by the door of room B. I can't watch the lockers, but I saw who came and went. And I found a little hex key on the floor afterwards.",
   "evidence": ev_table("Changing room B door", ["Time", "Who"], [
       ("16:05", "L. Novak out"),
       ("17:20", "B. Rossi in"),
       ("17:31", "B. Rossi out"),
       ("18:20", "L. Novak in"),
     ], mono_cols=(0,))},
  {"name": "Greg Novak", "role": "Lena's coach and father", "label": "HEX KEY",
   "quote": "That hex key isn't ours. Lena's blades take a 4 mm key and ours lives in my bag. Whoever did this brought their own.",
   "evidence": ev_rows("Hex key found in room B", [
       ("Size", "4 mm"),
       ("Marking", "Engraved “B.R.”"),
       ("Found", "Under the bench by locker 6, 18:50"),
     ])},
 ],
 "solution": {"killer": "Bianca Rossi",
   "motive": "Bianca was second, 2.35 points behind Lena, with a national-team place at stake (clue 2).",
   "proof": ["Bianca says she watched the pairs from the stands from five to six (clue 2). But the rink was closed for resurfacing, the stands were empty and the pairs final had been postponed (clue 3). Her alibi is invented.",
             "The steward saw her go into changing room B at 17:20 and leave at 17:31 (clue 5), and a 4 mm hex key engraved “B.R.” was found under the bench by Lena's locker (clue 6)."],
   "cleared": ["<b>Mika</b> was with the physio from 17:00 to 17:50 (clue 4).",
               "<b>Greg</b> keeps his own key in his bag (clue 6), and <b>Joe</b> was resurfacing the ice (clue 3).",
               "<b>Ruth</b> was at the door, and <b>Lena</b> checked her skates at four (clue 1)."]},
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

MYSTERIES = [rink, orchid]
