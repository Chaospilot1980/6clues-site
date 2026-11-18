from lib import *  # evidence helpers

# Round 20 (18 Nov): 1 Rookie, 1 Detective, 2 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- MASCOT (L1)
mascot = {
 "slug": "the-missing-mascot-costume", "level": 1, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 142", "title_html": "THE MISSING<br>MASCOT COSTUME", "title_plain": "The Missing Mascot Costume",
 "teaser": "The night before sports day, the school's lucky badger costume vanishes from a locked store. The key book knows who borrowed the key.",
 "intro": "At <b>Elmwood Primary</b>, Bertie the Badger – the giant mascot costume that cheers the team on every sports day – disappeared from the PE store the day before the big match against Hilltop School. " + STD,
 "clues": [
  {"name": "Mrs Ruth Okoro", "role": "Head teacher", "label": "SCHOOL REPORT",
   "quote": "Bertie was hanging in the PE store when Mr Hale locked it at half past three on Thursday. On Friday morning at eight, the hook was empty. Nothing was broken.",
   "evidence": ev_rows("School report", [
       ("Locked", "Thursday 15:30, by Mr Hale"),
       ("Found missing", "Friday 08:00"),
       ("Damage", "None – the store was opened with the key"),
       ("Key", "Kept in the school office; borrowers must sign the key book"),
     ])},
  {"name": "Mr Kyle Banks", "role": "Hilltop School PE teacher", "label": "KYLE'S STATEMENT",
   "quote": "I brought the Hilltop team over for practice on Thursday and we left at three o'clock sharp. I never set foot in the Elmwood PE store.",
   "evidence": ev_rows("Sports day – last three years", [
       ("2024", "Elmwood won · Bertie on the touchline"),
       ("2025", "Elmwood won · Bertie on the touchline"),
       ("Note", "Mr Banks joked in the staff room: “One day I'll kidnap that badger.”"),
     ])},
  {"name": "Mrs Joan Pell", "role": "School secretary", "label": "KEY BOOK",
   "quote": "Everyone who borrows a key has to sign for it. Thursday afternoon was busy – lots of visitors for the practice match.",
   "evidence": ev_table("Office key book – Thursday", ["Time", "Key", "Signed", "Back"], [
       ("15:30", "PE store", "D. Hale", "15:32"),
       ("15:40", "PE store", "K. Banks (to return Hilltop's balls)", "15:50"),
       ("16:10", "Hall", "R. Okoro", "16:30"),
     ], mono_cols=(0, 3))},
  {"name": "Stan Price", "role": "Caretaker", "label": "CARETAKER'S NOTE",
   "quote": "I keep a notebook of anything unusual on the school grounds. Thursday afternoon there was one thing.",
   "evidence": ev_note("CARETAKER'S NOTEBOOK", [
       "Thursday 15:45 –",
       "man in a red Hilltop tracksuit carrying a",
       "big black kit bag, very full, out to the",
       "car park. Looked in a hurry."],
     "– Stan, caretaker")},
  {"name": "Mr Dan Hale", "role": "Elmwood PE teacher", "label": "CAR PARK LOG",
   "quote": "I locked the store at half three with Bertie on his hook. Walking to the staff meeting I noticed the Hilltop minibus was still in the car park – the barrier log shows when it left.",
   "evidence": ev_table("Car park barrier – Thursday", ["Time", "Vehicle"], [
       ("15:02", "Parents' cars"),
       ("16:05", "Hilltop School minibus – driver K. Banks"),
       ("16:40", "Staff cars"),
     ], mono_cols=(0,))},
  {"name": "Miss Leah Ford", "role": "Elmwood teaching assistant", "label": "STAFF MEETING",
   "quote": "All the Elmwood teachers were in the staff meeting from quarter to four until half past four. Nobody left early – it was about sports day!",
   "evidence": ev_table("Staff meeting – attendance", ["Name", "From", "To"], [
       ("D. Hale", "15:40", "16:30"),
       ("L. Ford", "15:40", "16:30"),
       ("R. Okoro", "15:40", "16:05"),
     ], mono_cols=(1, 2))},
 ],
 "solution": {"killer": "Mr Kyle Banks",
   "motive": "Kyle's school had lost sports day to Elmwood two years running with Bertie cheering, and he had joked about kidnapping the badger (clue 2).",
   "proof": ["The store was opened with the key, not broken into (clue 1).",
             "Kyle says he left at three and never went to the store. But he signed out the PE store key at 15:40 and returned it at 15:50 (clue 3).",
             "At 15:45 the caretaker saw a man in a red Hilltop tracksuit carrying a big, full kit bag to the car park (clue 4), and the Hilltop minibus driven by Kyle only left at 16:05 (clue 5)."],
   "cleared": ["<b>Mr Hale</b> returned the key at 15:32 and was in the staff meeting (clues 3, 6).",
               "<b>Miss Ford</b> and <b>Mrs Okoro</b> were in the staff meeting when the store was opened (clue 6).",
               "<b>Mrs Pell</b> and <b>Stan</b> only kept the records (clues 3, 4)."]},
}

# ---------------------------------------------------------------- CAMERA FAIR (L2)
camera = {
 "slug": "the-camera-fair-leica", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 143", "title_html": "THE CAMERA<br>FAIR LEICA", "title_plain": "The Camera Fair Leica",
 "teaser": "A rare 1930s camera vanishes from a dealer's stand during the raffle draw. One collector's alibi is a photo – but cameras remember more than you think.",
 "intro": "At the <b>Northbridge Camera Fair</b>, a 1933 Leica worth £15,000 disappeared from dealer Frank Wiley's stand while everyone was watching the raffle draw. " + STD,
 "clues": [
  {"name": "Frank Wiley", "role": "Camera dealer", "label": "DEALER'S REPORT",
   "quote": "I left my stand for ten minutes to draw the raffle on the stage – I'm the fair's treasurer. When I got back, the Leica was gone from the cabinet.",
   "evidence": ev_rows("Theft report", [
       ("Stand left", "14:58"),
       ("Back", "15:08 – Leica missing"),
       ("Cabinet", "Unlocked – Frank had shown the camera to a buyer at 14:50"),
       ("Value", "£15,000"),
     ])},
  {"name": "Gordon Bell", "role": "Collector", "label": "GORDON'S STATEMENT",
   "quote": "I was in the lecture hall from quarter to three until half past. Look – here's the photo I took of the speaker at five past three.",
   "evidence": ev_rows("Gordon Bell – dealings with Frank", [
       ("October", "Offered £9,000 for the Leica – refused"),
       ("This morning", "Offered £11,000 – refused again"),
       ("Note", "Told another dealer he would 'have that camera one way or another'"),
     ])},
  {"name": "Asha Kumar", "role": "Fair organiser", "label": "LECTURE PROGRAMME",
   "quote": "We had two talks in the lecture hall this afternoon. Both were packed.",
   "evidence": ev_programme("Lecture hall – Saturday", "Northbridge Camera Fair", [
       ("14:00–14:45", "“A History of the Leica” – slides of classic cameras"),
       ("15:00–15:45", "“Darkroom Basics” – live demonstration, lights dimmed"),
     ], None)},
  {"name": "Tim Rhodes", "role": "Photo technician", "label": "PHOTO DATA",
   "quote": "Every digital photo stores the time it was taken. I checked the one Mr Bell showed the police.",
   "evidence": ev_rows("Gordon's photo – file information", [
       ("Taken", "Saturday 14:21"),
       ("Shows", "Speaker beside a slide titled “A History of the Leica”"),
       ("Camera clock", "Checked – correct to the minute"),
     ])},
  {"name": "Rosa Hill", "role": "Raffle helper", "label": "RAFFLE LIST",
   "quote": "Frank drew the tickets and I read out the names. One winner never came up to collect his prize.",
   "evidence": ev_table("Raffle draw – stage", ["Time", "Ticket", "Name", "Collected?"], [
       ("15:00", "042", "P. Shah", "Yes"),
       ("15:02", "118", "G. Bell", "No – not in the hall"),
       ("15:04", "203", "R. Hill", "Yes"),
     ], mono_cols=(0, 1))},
  {"name": "Len Fox", "role": "Security guard", "label": "CAR PARK CAMERA",
   "quote": "I watch the car park camera from my booth. One visitor nipped out halfway through the afternoon and came straight back in.",
   "evidence": ev_photos("Car park camera", [
       ("CAM-2", "15:06", "G. Bell puts a small padded camera bag into the boot of his car."),
       ("CAM-2", "15:09", "G. Bell walks back into the fair."),
     ])},
 ],
 "solution": {"killer": "Gordon Bell",
   "motive": "Gordon had twice tried to buy the Leica and been refused, and said he'd have it 'one way or another' (clue 2).",
   "proof": ["The Leica was taken from the unlocked cabinet between 14:58 and 15:08 (clue 1).",
             "Gordon says he was in the lecture and took a photo of the speaker at 15:05. But the photo was taken at 14:21, during the first talk – it shows the Leica history slide (clues 3, 4).",
             "His raffle ticket was drawn at 15:02 and he wasn't in the hall to collect (clue 5). At 15:06 he put a small camera bag into his car boot (clue 6)."],
   "cleared": ["<b>Frank</b> and <b>Rosa</b> were on stage drawing the raffle (clues 1, 5).",
               "<b>Asha</b> ran the programme, <b>Tim</b> checked the photo, and <b>Len</b> was in his booth watching the camera."]},
}

# ---------------------------------------------------------------- SHEEPDOG TRIALS (L3)
sheepdog = {
 "slug": "death-at-the-sheepdog-trials", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 144", "title_html": "DEATH AT THE<br>SHEEPDOG TRIALS", "title_plain": "Death at the Sheepdog Trials",
 "teaser": "A judge is found dead in his caravan at a Highland sheepdog trial. A shepherd swears he was out on the course – but his dog was somewhere else.",
 "intro": "At the <b>Glen Lyon Sheepdog Trials</b>, senior judge Hamish Reid was found dead in the judges' caravan on the afternoon of the open final. " + STD,
 "clues": [
  {"name": "Sgt Fiona Gray", "role": "Police", "label": "POLICE REPORT",
   "quote": "Mr Reid was struck on the head in the judges' caravan. He bought a tea at two o'clock, so we know he was alive then. He was found at three.",
   "evidence": ev_rows("Police report – Glen Lyon", [
       ("Found", "15:00, judges' caravan beside the course"),
       ("Last seen alive", "14:02, buying tea at the catering van"),
       ("Death", "Between 14:05 and 14:20 (pathologist)"),
       ("Note", "Mr Reid left the judges' box at 14:00 for his tea break"),
     ])},
  {"name": "Alasdair Munro", "role": "Shepherd", "label": "SOCIETY LETTER",
   "quote": "I was out on the course with Bess from five past two till twenty past – the whole field was watching us work the sheep. Ask anyone.",
   "evidence": ev_note("DRAFT LETTER IN HAMISH'S BRIEFCASE", [
       "To the Sheepdog Society:",
       "I have proof that A. Munro falsified the",
       "pedigree papers of his dog Bess. I will",
       "hand them in after the final on Saturday."],
     "– H. Reid")},
  {"name": "Morag Lennox", "role": "Commentator", "label": "REVISED RUNNING ORDER",
   "quote": "After the rain delay we had to shuffle the running order for the final. I read the new order out over the loudspeaker.",
   "evidence": ev_table("Open final – running order (revised)", ["Start", "Handler", "Dog"], [
       ("13:30", "A. Munro", "Bess"),
       ("13:50", "D. Doyle", "Nell"),
       ("14:05", "E. Kerr", "Fly"),
       ("14:25", "I. Grant", "Moss"),
     ], mono_cols=(0,))},
  {"name": "Ewan Kerr", "role": "Shepherd", "label": "SCORE SHEET",
   "quote": "I ran Fly at five past two, right on time. Best run of my life, if I'm honest – shame it was overshadowed.",
   "evidence": ev_table("Judges' score sheet", ["Handler", "Start", "Finish", "Judge"], [
       ("A. Munro / Bess", "13:31", "13:46", "H. Reid, S. Grant"),
       ("D. Doyle / Nell", "13:51", "13:59", "H. Reid, S. Grant"),
       ("E. Kerr / Fly", "14:06", "14:19", "S. Grant only"),
     ], mono_cols=(1, 2))},
  {"name": "Shona Grant", "role": "Co-judge", "label": "JUDGES' BOX PHOTO",
   "quote": "I judged Ewan's run alone while Hamish had his tea. I took a photo from the judges' box to send to the newspaper.",
   "evidence": ev_photos("Shona's phone", [
       ("IMG_0412", "14:12", "View from the judges' box: Ewan Kerr and his black-and-white dog Fly at the pen. Far left: a red quad bike parked right beside the judges' caravan, its back box labelled 'MUNRO'."),
     ])},
  {"name": "Dr Iain Lewis", "role": "Vet on duty", "label": "VET TENT LOG",
   "quote": "Bess came to my tent straight after her run with a sore paw. She stayed with my nurse until twenty to three while her owner went off somewhere.",
   "evidence": ev_table("Vet tent – Saturday", ["Time", "Dog", "Owner", "Note"], [
       ("13:55", "Bess (collie)", "A. Munro", "Left on the bench for observation – owner leaves"),
       ("14:40", "Bess (collie)", "A. Munro", "Collected by owner"),
     ], mono_cols=(0,))},
 ],
 "solution": {"killer": "Alasdair Munro",
   "motive": "Hamish had proof that Alasdair had falsified Bess's pedigree papers and was about to report him to the Sheepdog Society (clue 2).",
   "proof": ["Hamish died between 14:05 and 14:20 in the judges' caravan (clue 1).",
             "Alasdair says he was on the course with Bess from 14:05 to 14:20. But after the rain delay his run was moved to 13:30 (clue 3), it finished at 13:46, and the 14:05 run was Ewan and Fly (clue 4).",
             "From 13:55 to 14:40 Bess was in the vet tent while Alasdair 'went off somewhere' (clue 6), and at 14:12 his red quad bike was parked right beside the judges' caravan (clue 5)."],
   "cleared": ["<b>Ewan</b> was running Fly on the course from 14:06 to 14:19 (clues 4, 5).",
               "<b>Shona</b> was judging alone in the judges' box (clues 4, 5), and <b>Morag</b> was commentating (clue 3).",
               "<b>Dr Lewis</b> was in the vet tent, and <b>Sgt Gray</b> only investigated."]},
}

# ---------------------------------------------------------------- FENCING CLUB (L3)
fencing = {
 "slug": "murder-at-the-fencing-club", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 145", "title_html": "MURDER AT THE<br>FENCING CLUB", "title_plain": "Murder at the Fencing Club",
 "teaser": "A fencing coach is killed in the armoury during club night. The scoring machine says his star pupil was on the piste – but behind a mask, who can tell?",
 "intro": "At the <b>Riverside Fencing Club</b>, head coach Viktor Lenz was found dead in the armoury during Tuesday club night, struck with a heavy trophy. " + STD,
 "clues": [
  {"name": "DS Paul Okafor", "role": "Police", "label": "POLICE REPORT",
   "quote": "The coach was hit from behind with one of the club's own trophies. His fitness watch shows exactly when his heart stopped.",
   "evidence": ev_rows("Police report – Riverside Fencing Club", [
       ("Found", "19:40, armoury, by the armourer"),
       ("Weapon", "County Cup trophy, from the armoury shelf"),
       ("Fitness watch", "Heart stopped 19:18"),
       ("Armoury", "End of the corridor behind the main hall"),
     ])},
  {"name": "Clara Duval", "role": "Club fencer", "label": "SELECTION LETTER",
   "quote": "I was on piste 2 fencing Jo Moss from ten past seven until nearly half past. It's all on the scoring machine – look it up.",
   "evidence": ev_note("DRAFT ON VIKTOR'S LAPTOP", [
       "To the National Squad panel:",
       "I cannot recommend Clara Duval for",
       "selection this season. Sending",
       "on Wednesday morning. – V. Lenz"],
     "– found by DS Okafor")},
  {"name": "Jo Moss", "role": "Club fencer", "label": "SCORING MACHINE",
   "quote": "I fenced whoever was in Clara's jacket – with the mask down, you can't see a face. But she fenced left-handed tonight, which she never does. I lost 15–11.",
   "evidence": ev_table("Piste 2 – electronic scoring", ["Start", "End", "Fencer A (jacket)", "Fencer B (jacket)", "Score"], [
       ("18:40", "18:55", "J. Moss (#9)", "P. Vance (#4)", "15–9"),
       ("19:12", "19:24", "C. Duval (#14)", "J. Moss (#9)", "15–11"),
     ], mono_cols=(0, 1))},
  {"name": "Nina Ortiz", "role": "Club fencer", "label": "CLUB REGISTER",
   "quote": "I'm so sorry – Clara asked me to fence Jo in her jacket so the bout would count for her ranking. She said she had to ring her agent. My own jacket was being repaired anyway.",
   "evidence": ev_table("Club register", ["Fencer", "Hand", "Own jacket"], [
       ("Clara Duval", "Right", "#14"),
       ("Nina Ortiz", "Left", "#22"),
       ("Jo Moss", "Right", "#9"),
       ("Pete Vance", "Right", "#4"),
     ])},
  {"name": "Pete Vance", "role": "Armourer", "label": "REPAIR LOG",
   "quote": "I was upstairs in the repair room all evening, mending jackets. I only went down to the armoury at twenty to eight to put one back – and found Viktor.",
   "evidence": ev_table("Repair room – Tuesday", ["Time", "Item", "By"], [
       ("18:50", "Jacket #22 (N. Ortiz) – broken wire, in for repair", "P. Vance"),
       ("19:05", "Mask #3 – new bib", "P. Vance"),
       ("19:35", "Jacket #22 – repaired", "P. Vance"),
     ], mono_cols=(0,))},
  {"name": "Lily Shaw", "role": "Receptionist", "label": "CORRIDOR CAMERA",
   "quote": "The corridor camera covers the way to the changing rooms and the armoury. I didn't see anything odd at the time.",
   "evidence": ev_photos("Corridor camera", [
       ("CAM-3", "19:14", "C. Duval, in club tracksuit, no fencing kit, walks towards the armoury."),
       ("CAM-3", "19:22", "C. Duval walks back towards the changing rooms."),
     ])},
 ],
 "solution": {"killer": "Clara Duval",
   "motive": "Viktor was about to tell the national panel not to select Clara for the squad (clue 2).",
   "proof": ["Viktor died at 19:18 in the armoury (clue 1).",
             "Clara says the scoring machine proves she was fencing Jo from 19:12 to 19:24 (clues 2, 3). But Jo noticed the fencer in Clara's jacket was left-handed (clue 3) – Clara is right-handed, Nina is left-handed (clue 4), and Nina admits she fenced in Clara's jacket because her own was being repaired (clues 4, 5).",
             "At 19:14 the corridor camera shows Clara walking to the armoury, and at 19:22 coming back (clue 6)."],
   "cleared": ["<b>Jo</b> and <b>Nina</b> were fencing on piste 2 from 19:12 to 19:24 (clues 3, 4).",
               "<b>Pete</b> was repairing equipment upstairs (clue 5), and <b>Lily</b> was at reception.",
               "<b>DS Okafor</b> only investigated."]},
}

MYSTERIES = [mascot, camera, sheepdog, fencing]
