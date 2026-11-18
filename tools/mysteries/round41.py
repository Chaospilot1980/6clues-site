from lib import *  # evidence helpers

# Round 41 (18 Nov): 4 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- POLAR STATION
polar = {
 "slug": "death-at-the-polar-station", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 226", "title_html": "DEATH AT THE<br>POLAR STATION", "title_plain": "Death at the Polar Station",
 "teaser": "A scientist freezes to death outside an Antarctic research station after someone locks the airlock. The airlock log and a frosted glove reveal who did it.",
 "intro": "At <b>Halvorsen Research Station</b> in Antarctica, glaciologist Dr Pieter Smit was found frozen outside the station. The airlock door had been locked from inside while he was checking the weather mast. " + STD,
 "clues": [
  {"name": "Ingrid Dahl", "role": "Station leader", "label": "CHIEF'S REPORT",
   "quote": "Pieter went out to the weather mast at 21:00. Ten minutes later someone locked the airlock from the inside. At minus forty, he had no chance.",
   "evidence": ev_rows("Station chief's report", [
       ("Out", "21:00 – P. Smit to weather mast"),
       ("Airlock locked", "21:10, from inside, by hand"),
       ("Found", "22:15, frozen at the airlock door"),
       ("Radio", "His radio battery had been removed"),
     ])},
  {"name": "Dr Hugo Brandt", "role": "Fellow scientist", "label": "HUGO'S STATEMENT",
   "quote": "I was in the lab running ice core samples all evening. The machine logs every sample – I was there the whole time.",
   "evidence": ev_rows("Pieter's email draft (unsent)", [
       ("To", "Polar Science Journal"),
       ("Text", "“Dr Brandt's ice core results were faked. I have the proof.”"),
       ("Saved", "That afternoon"),
     ])},
  {"name": "Kim Larsen", "role": "Lab technician", "label": "LAB MACHINE LOG",
   "quote": "The ice core machine runs a sample every twenty minutes, but it doesn't need anyone there. You load it and walk away.",
   "evidence": ev_table("Ice core machine – samples", ["Time", "Sample", "Loaded by"], [
       ("20:40", "Core 14", "H. Brandt"),
       ("21:00", "Core 15", "Auto – from rack"),
       ("21:20", "Core 16", "Auto – from rack"),
       ("21:40", "Core 17", "H. Brandt"),
     ], mono_cols=(0,))},
  {"name": "Sam Osei", "role": "Mechanic", "label": "CORRIDOR NOTE",
   "quote": "I was fixing a heater by the airlock corridor. At about ten past nine someone in a red lab coat walked past towards the airlock with his hood up. I thought nothing of it.",
   "evidence": ev_note("SAM'S REPAIR SHEET", [
       "21:08 – person in red lab coat to",
       "airlock. 21:12 – back past me,",
       "something small in his hand. Frost",
       "on his left glove."],
     "– Sam")},
  {"name": "Dr Lucy Fenn", "role": "Station doctor", "label": "LAB COATS",
   "quote": "Each of us has a coloured lab coat so we can tell who's who in the cold rooms. Only one person wears red.",
   "evidence": ev_table("Lab coat colours", ["Person", "Coat"], [
       ("H. Brandt", "Red"),
       ("K. Larsen", "Blue"),
       ("L. Fenn", "White"),
       ("S. Osei", "Orange overalls"),
     ])},
  {"name": "Joe Park", "role": "Communications", "label": "RADIO FIND",
   "quote": "In the morning I found a radio battery hidden in the lab's sample freezer – it had Pieter's radio number on it.",
   "evidence": ev_photos("Joe's photo", [
       ("IMG_14", "07:30", "Lab sample freezer, behind Core 16: a radio battery labelled 'R-4 – SMIT'."),
     ])},
 ],
 "solution": {"killer": "Dr Hugo Brandt",
   "motive": "Pieter was about to reveal that Hugo had faked his ice core results (clue 2).",
   "proof": ["The airlock was locked from inside at 21:10 while Pieter was outside, and his radio battery was gone (clue 1).",
             "Hugo says he was in the lab all evening, but the machine ran on its own from 20:40 to 21:40 – he wasn't needed (clue 3).",
             "At 21:08 a person in a red lab coat went to the airlock (clue 4); only Hugo wears red (clue 5). Pieter's radio battery was hidden in Hugo's lab freezer (clue 6)."],
   "cleared": ["<b>Kim</b> wears blue and <b>Dr Fenn</b> white (clue 5). <b>Sam</b> was fixing the heater in orange overalls (clues 4, 5).",
               "<b>Ingrid</b> and <b>Joe</b> only report what they found."]},
}

# ---------------------------------------------------------------- TOMB EXHIBITION
tomb = {
 "slug": "murder-at-the-pharaoh-exhibition", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 227", "title_html": "MURDER AT THE<br>PHARAOH EXHIBITION", "title_plain": "Murder at the Pharaoh Exhibition",
 "teaser": "A museum curator is found dead inside the replica tomb on the opening night of a pharaoh exhibition. Audio guide numbers and a sand trail expose the killer.",
 "intro": "At the <b>Kingsgate Museum</b>, Egyptologist Dr Leonard Wise was found dead inside the replica tomb on the opening night of 'Gold of the Pharaohs'. He had been struck with a stone statue. " + STD,
 "clues": [
  {"name": "DI Neha Joshi", "role": "Police", "label": "POLICE REPORT",
   "quote": "Dr Wise died in the tomb between 20:15 and 20:35. The tomb floor is covered in fine golden sand – the killer would have carried some out on their shoes.",
   "evidence": ev_rows("Police report – Kingsgate Museum", [
       ("Found", "21:00, replica tomb"),
       ("Time of death", "20:15–20:35"),
       ("Weapon", "Small stone cat statue from the gift display"),
       ("Floor", "Fine golden sand"),
     ])},
  {"name": "Prof. Diane Marsh", "role": "Rival Egyptologist", "label": "DIANE'S STATEMENT",
   "quote": "I was in the main hall giving interviews to journalists from eight until nine. I never went near the tomb.",
   "evidence": ev_rows("Dr Wise's speech notes", [
       ("Line", "“Tonight I will reveal that the 'Golden Mask' Professor Marsh found in 2019 is a fake.”"),
       ("Planned for", "21:00 speech"),
     ])},
  {"name": "Rob Hayes", "role": "Audio guide manager", "label": "AUDIO GUIDE LOG",
   "quote": "Every guest has an audio guide. It logs each room they enter. Guide 12 went into the tomb at 20:18.",
   "evidence": ev_table("Audio guide – entries to tomb room", ["Time", "Guide", "Holder"], [
       ("20:05", "Guide 4", "Mr P. Lowe (guest)"),
       ("20:18", "Guide 12", "Prof. D. Marsh"),
       ("20:31", "Guide 12 – leaves tomb", "Prof. D. Marsh"),
     ], mono_cols=(0, 1))},
  {"name": "Jenny Cole", "role": "Journalist", "label": "INTERVIEW TIMES",
   "quote": "I had an interview booked with Professor Marsh at quarter past eight. She said 'give me ten minutes' and disappeared. She came back at twenty-five to nine, a bit flustered.",
   "evidence": ev_table("Press interviews – Prof. Marsh", ["Time", "Journalist", "Done?"], [
       ("20:00", "BBC Arts", "Yes"),
       ("20:15", "J. Cole – Daily Post", "Delayed to 20:35"),
       ("20:40", "History Today", "Yes"),
     ], mono_cols=(0,))},
  {"name": "Mr Peter Lowe", "role": "Guest", "label": "PETER'S STATEMENT",
   "quote": "I visited the tomb at five past eight. Dr Wise was in there, alive and cheerful. I left after five minutes.",
   "evidence": ev_rows("Audio guide 4", [
       ("Tomb", "20:05 – 20:10"),
       ("Then", "Gift shop 20:12–20:50"),
     ])},
  {"name": "Mo Rahim", "role": "Cleaner", "label": "SAND TRAIL",
   "quote": "After the police came, I noticed a trail of golden sand going from the tomb – not to the exit, but to the ladies' cloakroom by the main hall.",
   "evidence": ev_photos("Mo's photo", [
       ("IMG_88", "21:30", "Golden sand footprints from the tomb exit to the ladies' cloakroom. Inside: a pair of black heels with sand in the soles, a name tag 'D. MARSH' on the coat hook above them."),
     ])},
 ],
 "solution": {"killer": "Prof. Diane Marsh",
   "motive": "Dr Wise was going to reveal that Diane's famous 'Golden Mask' was a fake (clue 2).",
   "proof": ["Dr Wise died in the tomb between 20:15 and 20:35 (clue 1).",
             "Diane says she gave interviews all evening, but she delayed her 20:15 interview and was gone until 20:35 (clue 4). Her audio guide entered the tomb at 20:18 and left at 20:31 (clue 3).",
             "A trail of tomb sand led to her shoes in the cloakroom (clue 6)."],
   "cleared": ["<b>Peter</b> left the tomb at 20:10, before Dr Wise died, and was in the gift shop (clue 5).",
               "<b>Jenny</b>, <b>Rob</b> and <b>Mo</b> only report what they saw."]},
}

# ---------------------------------------------------------------- STEAM RAILWAY
steam = {
 "slug": "death-on-the-santa-steam-train", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 228", "title_html": "DEATH ON THE<br>SANTA STEAM TRAIN", "title_plain": "Death on the Santa Steam Train",
 "teaser": "The railway chairman is found dead in the guard's van of the Santa Special. The tunnel timing and a soot handprint show who left Santa's grotto.",
 "intro": "On the <b>Moorvale Steam Railway</b>'s Santa Special, chairman Clive Hargreaves was found dead in the guard's van, struck with a coal shovel. The train had just come out of Hollow Hill Tunnel. " + STD,
 "clues": [
  {"name": "DS Ian Booth", "role": "Transport police", "label": "POLICE REPORT",
   "quote": "Mr Hargreaves was alive when the train entered Hollow Hill Tunnel. He was found dead when it came out. The killer used the darkness.",
   "evidence": ev_rows("Police report – Santa Special", [
       ("Entered tunnel", "15:20"),
       ("Left tunnel", "15:24"),
       ("Found", "15:25, guard's van"),
       ("On the van door", "A sooty handprint – coal dust and glitter"),
     ])},
  {"name": "Barry Pike", "role": "Volunteer playing Santa", "label": "BARRY'S STATEMENT",
   "quote": "I was in Santa's grotto in carriage C the whole trip, handing out presents. A hundred children saw me.",
   "evidence": ev_rows("Railway committee minutes", [
       ("Item", "Barry Pike to be removed from the board for selling railway coal"),
       ("Proposed by", "C. Hargreaves"),
       ("Vote", "Next week"),
     ])},
  {"name": "Megan Ross", "role": "Volunteer elf", "label": "GROTTO LOG",
   "quote": "In the tunnel the lights go out, so we pause the queue. Santa said he needed some air and went out the back of the grotto. He came back just as we came out of the tunnel.",
   "evidence": ev_table("Grotto queue – carriage C", ["Time", "Note"], [
       ("15:18", "Family 41 with Santa"),
       ("15:20", "Tunnel – queue paused, Santa out back door"),
       ("15:24", "Santa back, out of breath"),
       ("15:25", "Family 42 with Santa"),
     ], mono_cols=(0,))},
  {"name": "Fred Wilde", "role": "Fireman (stoker)", "label": "FOOTPLATE LOG",
   "quote": "I was shovelling coal on the engine the whole way. The coal shovel in the guard's van is the spare – it's always black with soot.",
   "evidence": ev_rows("Engine crew note", [
       ("Driver", "R. Moss – on footplate the whole trip"),
       ("Fireman", "F. Wilde – on footplate the whole trip"),
       ("Note", "Engine is 5 carriages from the guard's van"),
     ])},
  {"name": "Mrs Lorna Kay", "role": "Passenger", "label": "PASSENGER NOTE",
   "quote": "My carriage is D, between the grotto and the guard's van. In the tunnel someone squeezed past me in the dark – he had a big soft belly and smelled of mince pies. Glitter on my sleeve afterwards.",
   "evidence": ev_note("LORNA'S NOTE", [
       "Tunnel – someone big pushed past",
       "towards the guard's van, then back",
       "again a minute or two later.",
       "Gold glitter on my sleeve."],
     "– Lorna")},
  {"name": "Pat Ellis", "role": "Wardrobe", "label": "COSTUME LIST",
   "quote": "Only Santa's costume has gold glitter on it – the elves are green and red, no glitter.",
   "evidence": ev_table("Santa Special costumes", ["Role", "Volunteer", "Glitter?"], [
       ("Santa", "B. Pike", "Gold glitter on coat"),
       ("Elf", "M. Ross", "No"),
       ("Guard", "C. Hargreaves", "No"),
     ])},
 ],
 "solution": {"killer": "Barry Pike",
   "motive": "Clive was getting Barry removed from the board for selling railway coal (clue 2).",
   "proof": ["Clive was killed in the tunnel between 15:20 and 15:24, and a sooty, glittery handprint was on the van door (clue 1).",
             "Barry says he was in the grotto the whole trip, but he left by the back door at 15:20 and came back out of breath at 15:24 (clue 3).",
             "Lorna felt a big figure push to the guard's van and back in the tunnel, leaving gold glitter (clue 5). Only the Santa costume has gold glitter (clue 6)."],
   "cleared": ["<b>Fred</b> was on the engine, five carriages away (clue 4). <b>Megan</b> stayed in the grotto with no glitter (clues 3, 6).",
               "<b>Lorna</b> and <b>Pat</b> only report what they know."]},
}

# ---------------------------------------------------------------- SAFARI LODGE
safari = {
 "slug": "murder-at-the-safari-lodge", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 229", "title_html": "MURDER AT THE<br>SAFARI LODGE", "title_plain": "Murder at the Safari Lodge",
 "teaser": "A lodge owner is found dead by the waterhole during a night game drive. The vehicle GPS, a camera trap and a ranger's spotlight log show who slipped away.",
 "intro": "At <b>Kingfisher Safari Lodge</b>, owner Alistair Burke was found dead by the waterhole, struck with a heavy torch. Everyone else was out on the night game drive – or said they were. " + STD,
 "clues": [
  {"name": "Inspector Grace Ndlovu", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Burke died by the waterhole between 21:00 and 21:30. The waterhole is 2 km from the lodge – you need a vehicle to get there and back quickly.",
   "evidence": ev_rows("Police report – Kingfisher Lodge", [
       ("Found", "22:15, waterhole hide"),
       ("Time of death", "21:00–21:30"),
       ("Weapon", "Heavy spotlight torch"),
       ("Tyre marks", "One vehicle stopped by the hide"),
     ])},
  {"name": "Jake Mbeki", "role": "Head ranger", "label": "JAKE'S STATEMENT",
   "quote": "I drove guests on the night drive the whole evening in Land Cruiser 2. We never went near the waterhole.",
   "evidence": ev_rows("Alistair's note", [
       ("To", "Lodge accountant"),
       ("Text", "“Jake has been selling rhino-tracking information to poachers. Police tomorrow.”"),
       ("Date", "That afternoon"),
     ])},
  {"name": "Clara Holt", "role": "Guest on night drive", "label": "CLARA'S NOTE",
   "quote": "Our ranger stopped the truck at nine and said 'stay quiet, watch the lions' – then he walked off with his radio. He was gone ages. Another ranger turned up to sit with us.",
   "evidence": ev_note("CLARA'S SAFARI DIARY", [
       "21:00 – Jake parks by lion pride,",
       "takes the spare truck, drives off.",
       "Ranger Thandi sits with us.",
       "21:35 – Jake back, dusty."],
     "– Clara")},
  {"name": "Thandi Khumalo", "role": "Ranger", "label": "VEHICLE GPS",
   "quote": "Jake radioed me to sit with his guests. The spare truck, Land Cruiser 5, has a GPS tracker.",
   "evidence": ev_table("GPS – Land Cruiser 5", ["Time", "Location"], [
       ("21:02", "Lion pride viewpoint"),
       ("21:10", "Waterhole hide"),
       ("21:25", "Leaves waterhole"),
       ("21:34", "Lion pride viewpoint"),
     ], mono_cols=(0,))},
  {"name": "Dr Sam Ade", "role": "Wildlife vet", "label": "CAMERA TRAP",
   "quote": "I have camera traps at the waterhole for my research. One caught a person at 21:14.",
   "evidence": ev_photos("Camera trap 3 – waterhole", [
       ("TRAP3_2114", "21:14", "Infrared: a man in a ranger's khaki uniform with a wide-brimmed hat, holding a big spotlight torch, walking towards the hide. Name badge glinting: 'JAKE'."),
     ])},
  {"name": "Mrs Fiona Burke", "role": "Alistair's wife", "label": "FIONA'S STATEMENT",
   "quote": "I stayed at the lodge doing the accounts. The kitchen staff brought me dinner at nine.",
   "evidence": ev_rows("Kitchen note", [
       ("21:00", "Dinner to Mrs Burke in the office"),
       ("21:30", "Plates collected – Mrs Burke still at desk"),
     ])},
 ],
 "solution": {"killer": "Jake Mbeki",
   "motive": "Alistair had found out Jake was selling rhino-tracking information to poachers (clue 2).",
   "proof": ["Alistair died at the waterhole between 21:00 and 21:30, and one vehicle had stopped there (clue 1).",
             "Jake says he drove the guests all evening and never went near the waterhole, but at 21:00 he left them and took the spare truck (clue 3). Its GPS shows it at the waterhole from 21:10 to 21:25 (clue 4).",
             "A camera trap caught a ranger with a 'JAKE' badge and a spotlight torch walking to the hide at 21:14 (clue 5)."],
   "cleared": ["<b>Fiona</b> was in the office at 21:00 and 21:30 (clue 6). <b>Thandi</b> was sitting with the guests (clues 3, 4).",
               "<b>Clara</b> and <b>Dr Ade</b> only report what they saw."]},
}

MYSTERIES = [polar, tomb, steam, safari]
