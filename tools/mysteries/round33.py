from lib import *  # evidence helpers

# Round 33 (18 Nov): 2 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- HONEY (L2)
honey = {
 "slug": "the-honey-label-fraud", "level": 2, "crime": "FRAUD", "who": "fraudster", "added": ADDED,
 "caseno": "CASE NO. 194", "title_html": "THE HONEY<br>LABEL FRAUD", "title_plain": "The Honey Label Fraud",
 "teaser": "A prize-winning 'local' honey turns out to be cheap imported syrup in new jars. A lab test, a delivery note and a missing beehive count catch the fraudster.",
 "intro": "At the <b>Ashdown Honey Show</b>, the gold medal went to 'Heath Gold' local heather honey. Then a lab test showed the winning jar was cheap imported syrup. " + STD,
 "clues": [
  {"name": "Dr Fay Collins", "role": "Food scientist", "label": "LAB TEST",
   "quote": "There's no heather pollen in it at all – it's imported blended syrup with a bit of colouring. Real heather honey is thick and full of pollen.",
   "evidence": ev_rows("Lab report – jar 'Heath Gold' No. 31", [
       ("Heather pollen", "None found"),
       ("Sugar profile", "Matches imported rice syrup blend"),
       ("Colouring", "Caramel colour added"),
       ("Verdict", "Not honey"),
     ])},
  {"name": "Neil Barrow", "role": "Beekeeper, 'Heath Gold'", "label": "NEIL'S STATEMENT",
   "quote": "Every jar of Heath Gold comes from my own forty hives on the heath. I'd never buy in honey – I've won this show five years running.",
   "evidence": ev_rows("Beekeepers' association – hive count", [
       ("N. Barrow – hives registered", "40 (spring)"),
       ("Autumn inspection", "8 hives alive – 32 lost to disease in June"),
       ("Normal crop from 8 hives", "About 120 jars"),
     ])},
  {"name": "Kay Ellis", "role": "Shop owner", "label": "SALES FIGURES",
   "quote": "I sold Heath Gold in my farm shop. This year Neil delivered more jars than ever.",
   "evidence": ev_table("Heath Gold – jars delivered to Kay's shop", ["Year", "Jars"], [
       ("2024", "480"),
       ("2025", "500"),
       ("2026", "620"),
     ])},
  {"name": "Barry Cope", "role": "Wholesale driver", "label": "DELIVERY NOTE",
   "quote": "I deliver to farms all over the county. In July I dropped off six big drums of 'golden syrup blend' at a farm on the heath.",
   "evidence": ev_rows("Delivery note – Imperial Syrups Ltd", [
       ("Date", "12 July 2026"),
       ("Goods", "6 × 200 kg drums, 'golden blend'"),
       ("Deliver to", "Heath Farm (N. Barrow)"),
       ("Signed", "N. Barrow"),
     ])},
  {"name": "Mo Rahman", "role": "Rival beekeeper", "label": "MO'S STATEMENT",
   "quote": "I came second. I'll admit I was angry, but I only sell what my own bees make – you can test every jar.",
   "evidence": ev_rows("Lab report – Mo's 'Valley Blossom'", [
       ("Pollen", "Clover, blackberry, lime – local"),
       ("Verdict", "Genuine honey"),
     ])},
  {"name": "Janet Barrow", "role": "Neil's sister", "label": "JANET'S NOTE",
   "quote": "I help Neil with the jars every autumn. This year he did them alone, with the barn locked – he said it was a 'new method'.",
   "evidence": ev_note("JANET'S DIARY", [
       "Sept – Neil won't let me in the",
       "barn. Saw big blue drums behind",
       "the door, 'IMPERIAL' on the side.",
       "Jars everywhere."],
     "– Janet")},
 ],
 "solution": {"killer": "Neil Barrow",
   "motive": "Neil lost 32 of his 40 hives but wanted to keep winning and selling as many jars as ever (clues 2, 3).",
   "proof": ["The winning Heath Gold jar is imported syrup, not honey (clue 1).",
             "Neil says every jar comes from his forty hives, but only eight survived – enough for about 120 jars, yet he delivered 620 (clues 2, 3).",
             "Six drums of syrup blend were delivered to his farm and signed for by him (clue 4), and Janet saw 'Imperial' drums in his locked barn (clue 6)."],
   "cleared": ["<b>Mo</b>'s honey tested genuine (clue 5).",
               "<b>Kay</b>, <b>Barry</b>, <b>Janet</b> and <b>Dr Collins</b> only report what they found (clues 1, 3, 4, 6)."]},
}

# ---------------------------------------------------------------- KEY CARD (L2)
keycard = {
 "slug": "the-hotel-key-card-thief", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 195", "title_html": "THE HOTEL<br>KEY CARD THIEF", "title_plain": "The Hotel Key Card Thief",
 "teaser": "Jewellery vanishes from three rooms of a seaside hotel, but the doors were never forced. The key card system remembers more than the thief thought.",
 "intro": "At the <b>Grand Esplanade Hotel</b>, three guests on the second floor reported jewellery stolen from their rooms on the same evening. No doors were forced. " + STD,
 "clues": [
  {"name": "Mrs Clara Vane", "role": "Hotel manager", "label": "THEFT LIST",
   "quote": "Rooms 204, 207 and 211 – all robbed while the guests were at the gala dinner downstairs, from seven until ten.",
   "evidence": ev_table("Thefts – gala night", ["Room", "Missing"], [
       ("204", "Gold bracelet"),
       ("207", "Pearl earrings"),
       ("211", "Diamond ring"),
     ])},
  {"name": "Josh Patel", "role": "Night porter", "label": "JOSH'S STATEMENT",
   "quote": "My master card was in my pocket all evening. I never went to the second floor – I was at the front desk the whole time.",
   "evidence": ev_table("Master cards", ["Card", "Holder"], [
       ("M1", "C. Vane (manager)"),
       ("M2", "J. Patel (porter)"),
       ("M3", "Housekeeping trolley – returned at 18:00"),
     ])},
  {"name": "Ines Duarte", "role": "Housekeeper", "label": "TROLLEY LOG",
   "quote": "I put card M3 back in the office at six when my shift ended, like always. I went home on the bus.",
   "evidence": ev_rows("Office key cabinet", [
       ("M3", "Returned 18:00 – I. Duarte"),
       ("M3", "Taken out 22:30 – night housekeeping"),
     ])},
  {"name": "Ray Doyle", "role": "IT technician", "label": "DOOR LOCK LOG",
   "quote": "Every door lock records which card opened it. All three rooms were opened by the same card that night.",
   "evidence": ev_table("Door locks – gala night", ["Time", "Room", "Card"], [
       ("19:42", "204", "M2"),
       ("19:47", "207", "M2"),
       ("19:53", "211", "M2"),
     ], mono_cols=(0, 1, 2))},
  {"name": "Penny Shaw", "role": "Receptionist", "label": "DESK ROTA",
   "quote": "Josh asked me to cover the front desk for twenty minutes at about half past seven – he said he needed a break.",
   "evidence": ev_table("Front desk – gala night", ["Time", "At the desk"], [
       ("18:00–19:35", "J. Patel"),
       ("19:35–19:58", "P. Shaw (cover)"),
       ("19:58–23:00", "J. Patel"),
     ], mono_cols=(0,))},
  {"name": "Mr Hugo Lamb", "role": "Guest, room 209", "label": "HUGO'S NOTE",
   "quote": "I'd gone up early with a headache. About ten to eight I looked out of my door and saw a man in a porter's waistcoat walking quickly to the stairs, putting something in his pocket.",
   "evidence": ev_note("HUGO'S NOTE", [
       "About 19:50 – man in burgundy",
       "porter's waistcoat, name badge",
       "'JOSH', coming from 211 end of",
       "corridor, to the stairs."],
     "– Hugo")},
 ],
 "solution": {"killer": "Josh Patel",
   "motive": "Josh stole jewellery from guests at the gala dinner (clue 1).",
   "proof": ["All three rooms were opened with master card M2 between 19:42 and 19:53 (clue 4), and M2 is Josh's card (clue 2).",
             "Josh says he was at the front desk all evening, but Penny covered for him from 19:35 to 19:58 (clue 5).",
             "At about 19:50 Hugo saw a porter with a 'JOSH' badge on the second floor heading for the stairs (clue 6)."],
   "cleared": ["<b>Ines</b> returned card M3 at 18:00, and it wasn't used on these doors (clues 3, 4).",
               "<b>Mrs Vane</b>'s card M1 wasn't used; <b>Penny</b> was at the desk, and <b>Hugo</b> and <b>Ray</b> only report what they saw (clues 4, 5, 6)."]},
}

# ---------------------------------------------------------------- ROWING (L3)
rowing = {
 "slug": "death-at-the-rowing-club", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 196", "title_html": "DEATH AT THE<br>ROWING CLUB", "title_plain": "Death at the Rowing Club",
 "teaser": "A rowing coach is found drowned below the club pontoon at dawn. A boat log, a river tide table and a wet blazer prove it was no accident.",
 "intro": "At the <b>Kingsmere Rowing Club</b>, head coach Duncan Reeve was found drowned below the club's pontoon at dawn. A bruise on his head shows he was struck before he went into the water. " + STD,
 "clues": [
  {"name": "DS Leah Grant", "role": "Police", "label": "POLICE REPORT",
   "quote": "He was hit and pushed in. The river was at low tide when he went in – there's mud on his shoes from the bank, which is only uncovered at low tide.",
   "evidence": ev_rows("Police report – Kingsmere RC", [
       ("Found", "06:40, below the pontoon"),
       ("Head", "Struck with a blunt object – an oar handle?"),
       ("Shoes", "Thick river mud – from the bank below the pontoon"),
       ("Watch", "Waterproof, still working – no help"),
     ])},
  {"name": "Felix Hardy", "role": "Club captain", "label": "FELIX'S STATEMENT",
   "quote": "I left the club at nine last night and was home by half past. I didn't come back until the police called me.",
   "evidence": ev_rows("Club committee minutes", [
       ("Item 4", "Coach Reeve to drop Felix Hardy from the first crew for the national regatta"),
       ("Felix", "Walked out of the meeting"),
       ("Date", "Two days before"),
     ])},
  {"name": "Mags O'Neill", "role": "Boatman", "label": "TIDE TABLE",
   "quote": "The bank below the pontoon is under water except at low tide. Last night low tide was just before midnight.",
   "evidence": ev_table("River tide table – that night", ["Time", "Tide"], [
       ("21:00", "High – bank covered"),
       ("23:40", "Low – bank uncovered 23:10 to 00:20"),
       ("05:50", "High – bank covered"),
     ], mono_cols=(0,))},
  {"name": "Sean Pike", "role": "Night security", "label": "GATE LOG",
   "quote": "Members use their fob at the boathouse gate. Two people came in late last night.",
   "evidence": ev_table("Boathouse gate – fob log", ["Time", "Fob", "Member"], [
       ("22:55", "117", "D. Reeve"),
       ("23:20", "042", "F. Hardy"),
       ("23:58", "042", "F. Hardy (out)"),
     ], mono_cols=(0, 1))},
  {"name": "Ellen Reeve", "role": "Duncan's wife", "label": "ELLEN'S STATEMENT",
   "quote": "Duncan said he had to meet someone at the club about 'the crew'. I was at home with our neighbours playing bridge until one.",
   "evidence": ev_rows("Neighbour's statement", [
       ("Bridge game", "Ellen Reeve, Mr and Mrs Cole, Ann Dix"),
       ("Time", "21:00–01:10 at the Coles' house"),
     ])},
  {"name": "Tara Quinn", "role": "Rower", "label": "LOCKER PHOTO",
   "quote": "In the morning I found Felix's club blazer stuffed in the drying room – soaking wet, with river mud on the cuffs.",
   "evidence": ev_photos("Tara's phone", [
       ("IMG_1188", "07:05", "Drying room: a navy club blazer, sleeves soaked, mud on the cuffs. Name tape inside the collar: F. HARDY."),
       ("IMG_1189", "07:06", "Rack of oars – one oar handle missing its grip, a dark stain on the wood."),
     ])},
 ],
 "solution": {"killer": "Felix Hardy",
   "motive": "Duncan was dropping Felix from the first crew for the national regatta (clue 2).",
   "proof": ["Duncan was struck and pushed in while the bank was uncovered – between 23:10 and 00:20 (clues 1, 3).",
             "Felix says he never came back after 21:00, but his fob opened the boathouse gate at 23:20 and let him out at 23:58 (clue 4).",
             "His club blazer was found soaked, with river mud on the cuffs (clue 6)."],
   "cleared": ["<b>Ellen</b> was playing bridge with neighbours until 01:10 (clue 5).",
               "<b>Sean</b>, <b>Mags</b> and <b>Tara</b> only report what they found (clues 3, 4, 6)."]},
}

# ---------------------------------------------------------------- PERFUME (L3)
perfume = {
 "slug": "murder-at-the-perfume-house", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 197", "title_html": "MURDER AT THE<br>PERFUME HOUSE", "title_plain": "Murder at the Perfume House",
 "teaser": "A famous perfumer is poisoned on the night she launches her new scent. Only one person could have known which bottle she would test first.",
 "intro": "At <b>Maison Delacroix</b> in Paris, master perfumer Camille Delacroix collapsed and died at the launch of her new scent, 'Nuit Blanche'. She had sniffed and dabbed a test bottle laced with poison. " + STD,
 "clues": [
  {"name": "Inspector Luc Moreau", "role": "Police", "label": "POLICE REPORT",
   "quote": "The poison was only in one of twelve test bottles – the one marked 'N°7'. Whoever poisoned it knew she would test N°7 first.",
   "evidence": ev_rows("Police report – Maison Delacroix", [
       ("Died", "21:15, launch party"),
       ("Poison", "In test bottle N°7 only – other 11 bottles clean"),
       ("Bottles", "Set out on the tray at 20:30"),
       ("Glove print", "A latex glove print on N°7's cap"),
     ])},
  {"name": "Hélène Roux", "role": "Assistant perfumer", "label": "HÉLÈNE'S STATEMENT",
   "quote": "I only set out the tray – I had no idea which bottle Camille would choose. She decided on the night.",
   "evidence": ev_rows("Email from C. Delacroix", [
       ("To", "Hélène Roux only"),
       ("Sent", "Morning of the launch"),
       ("Text", "“Tonight I will open the show by testing N°7 – our secret. Then I'll announce that you are leaving.”"),
     ])},
  {"name": "Bruno Marchetti", "role": "Business partner", "label": "BRUNO'S STATEMENT",
   "quote": "Camille and I argued about money. But I was greeting guests at the door from eight until nine – fifty people saw me.",
   "evidence": ev_photos("Party photographer", [
       ("IMG_301", "20:25", "Bruno at the front door greeting guests."),
       ("IMG_318", "20:50", "Bruno at the front door with the mayor."),
     ])},
  {"name": "Sophie Lenoir", "role": "Lab technician", "label": "GLOVE LOG",
   "quote": "Latex gloves are kept in the lab. Everyone who takes a pair has to sign for them.",
   "evidence": ev_table("Lab glove log – launch day", ["Time", "Name", "Pairs"], [
       ("09:10", "S. Lenoir", "2"),
       ("14:30", "H. Roux", "1"),
       ("20:20", "H. Roux", "1"),
     ], mono_cols=(0,))},
  {"name": "Marc Delacroix", "role": "Camille's son", "label": "MARC'S STATEMENT",
   "quote": "My mother and I were close. I arrived late from the airport at nine, after the bottles were set out.",
   "evidence": ev_rows("Taxi receipt", [
       ("From", "Charles de Gaulle airport"),
       ("To", "Maison Delacroix"),
       ("Arrived", "20:58"),
     ])},
  {"name": "Nadia Benali", "role": "Waitress", "label": "NADIA'S NOTE",
   "quote": "I was passing the lab at about twenty-five past eight. A woman in a white lab coat was at the tray, wearing gloves, holding one bottle up to the light.",
   "evidence": ev_note("NADIA'S NOTE", [
       "About 20:25 – woman in lab coat",
       "and gloves at the perfume tray,",
       "hair in a red scarf. Held up one",
       "bottle, then put it back first in line."],
     "– Nadia")},
 ],
 "solution": {"killer": "Hélène Roux",
   "motive": "Camille was going to announce that Hélène was leaving (clue 2).",
   "proof": ["The poison was only in N°7, so the killer knew Camille would test N°7 first (clue 1).",
             "Hélène says she had no idea which bottle Camille would choose, but Camille emailed only her that morning: 'I will open by testing N°7' (clue 2).",
             "Hélène signed out gloves at 20:20 (clue 4), just before Nadia saw a gloved woman in a lab coat at the tray at 20:25 (clue 6). A glove print was on N°7's cap (clue 1)."],
   "cleared": ["<b>Bruno</b> was photographed at the door at 20:25 and 20:50 (clue 3), and <b>Marc</b> arrived at 20:58 (clue 5).",
               "<b>Sophie</b> only took gloves in the morning, and <b>Nadia</b> is a witness (clues 4, 6)."]},
}

MYSTERIES = [honey, keycard, rowing, perfume]
