from lib import *  # evidence helpers

# Round 12 (18 Nov night): 1 Detective, 1 Mastermind.
STD = "Find all 6 clues, compare the statements and the evidence, and work out who did it."
ADDED = "2026-11-18"

# ---------------------------------------------------------------- WEDDING (L2)
wedding = {
 "slug": "the-wedding-gift-box", "level": 2, "crime": "THEFT", "who": "thief", "added": ADDED,
 "caseno": "CASE NO. 120", "title_html": "THE WEDDING<br>GIFT BOX", "title_plain": "The Wedding Gift Box",
 "teaser": "£3,000 in cards and cash vanishes from the gift table during the speeches. One guest swears he was still on the bus.",
 "intro": "At <b>Ashby Barn</b>, the white card box holding the wedding guests' gifts – about £3,000 – disappeared from the gift table during the speeches at Lily and Sam's reception. " + STD,
 "clues": [
  {"name": "Mia Chen", "role": "Wedding photographer", "label": "MIA'S PHOTOS",
   "quote": "I photograph everything, including the gift table – brides love that. I was at the front for the speeches, but I kept glancing round with the long lens.",
   "evidence": ev_photos("Mia's camera – reception", [
       ("IMG_3301", "13:30", "The gift table: flowers, parcels and the white card box."),
       ("IMG_3318", "13:40", "Rob, the best man, bending over the gift table."),
       ("IMG_3342", "13:58", "The gift table without the box. At the side door, the back of a man in a grey suit."),
     ])},
  {"name": "Dean Hollis", "role": "Groom's cousin", "label": "DEAN'S INVITATION",
   "quote": "I missed the speeches – my car's off the road, so I came on the 14:10 bus from town. By the time I walked in, everyone was already shouting about the box.",
   "evidence": ev_note("YOU ARE INVITED", [
       "Lily Marsh &amp; Sam Hollis",
       "request the pleasure of your company",
       "Sunday 14 June · ceremony 12:00, St Anne's",
       "Reception from 13:00 at Ashby Barn",
       "Carriages at midnight"],
     "– RSVP to Lily")},
  {"name": "Rob Kerr", "role": "Best man", "label": "SPEECHES RUNNING ORDER",
   "quote": "I'd left my speech cards on the gift table, so I grabbed them at twenty to two – that's the photo. Then I was on the stage. Dean turned up in that awful grey suit afterwards, I suppose.",
   "evidence": ev_programme("Speeches", "Reception running order", [
       ("13:35", "Father of the bride"),
       ("13:45", "Best man – Rob Kerr"),
       ("13:55", "Maid of honour – Amy Marsh"),
       ("14:05", "Toast and cake"),
     ], None)},
  {"name": "Pat Hollis", "role": "Groom's aunt", "label": "KITCHEN SHEET",
   "quote": "Dean owes money to half the family, I'm sorry to say it. Me, I was in the kitchen with the caterers cutting the cake into two hundred pieces.",
   "evidence": ev_rows("Caterers' kitchen sheet", [
       ("13:20", "Cake cutting starts – Pat Hollis and two staff"),
       ("13:50", "Cake plated, 200 pieces"),
       ("14:02", "Pat carries the first tray out"),
     ])},
  {"name": "Laszlo Varga", "role": "Barn manager", "label": "BAR TILL",
   "quote": "I was behind the bar the whole time. During speeches people want a top-up before every toast.",
   "evidence": ev_table("Ashby Barn bar · till 1", ["Time", "Sale", "Server"], [
       ("13:33", "Prosecco × 4", "L. Varga"),
       ("13:41", "Pints × 2", "L. Varga"),
       ("13:49", "Gin and tonic", "L. Varga"),
       ("13:57", "Prosecco × 6", "L. Varga"),
     ], mono_cols=(0,))},
  {"name": "Amy Marsh", "role": "Bride's sister", "label": "BARN NOTICEBOARD",
   "quote": "I was at the front waiting for my speech, shaking with nerves. I took this photo of the noticeboard for the guests who don't drive.",
   "evidence": ev_table("Bus 22 · Town → Ashby Barn", ["Days", "Times"], [
       ("Monday–Saturday", "Every hour at :10, 07:10–19:10"),
       ("Sundays", "15:40 and 17:40 only"),
       ("Journey time", "25 minutes"),
     ])},
 ],
 "solution": {"killer": "Dean Hollis",
   "motive": "Dean owed money to half the family (clue 4).",
   "proof": ["The box vanished between 13:30 and 13:58, when a man in a grey suit was leaving by the side door (clue 1). Dean wore a grey suit (clue 3).",
             "Dean says he arrived on the 14:10 bus (clue 2). But the wedding was on a Sunday (clue 2), and on Sundays the first bus is at 15:40 (clue 6). There was no 14:10 bus – Dean was already at the barn."],
   "cleared": ["<b>Rob</b> was photographed at the gift table, but only fetching his speech cards; he was on stage from 13:45 (clue 3).",
               "<b>Pat</b> was cutting the cake in the kitchen until 14:02 (clue 4), and <b>Laszlo</b> was serving at the bar (clue 5).",
               "<b>Amy</b> was waiting to speak at 13:55 (clue 3), and <b>Mia</b> was taking the photos from the front (clue 1)."]},
}

# ---------------------------------------------------------------- SKI LODGE (L3)
ski = {
 "slug": "death-at-the-ski-lodge", "level": 3, "crime": "MURDER", "who": "killer", "added": ADDED,
 "caseno": "CASE NO. 121", "title_html": "DEATH AT THE<br>SKI LODGE", "title_plain": "Death at the Ski Lodge",
 "teaser": "The lodge owner is found dead at the top of the mountain, and the only way up is the chairlift. The lift remembers every pass – but not every face.",
 "intro": "In the Norwegian resort of <b>Fjellstua</b>, lodge owner Henrik Aas was found dead in the ski-wax room at the top station of the Summit chairlift. " + STD,
 "clues": [
  {"name": "Anders Fog", "role": "Ski patrol", "label": "POLICE REPORT",
   "quote": "Kari radioed me at ten past three and I went up on the lift. Before that I was at the first-aid hut at the bottom, strapping up an ankle. Henrik was a good man.",
   "evidence": ev_rows("Police report – Summit top station", [
       ("Found", "15:10, wax room at the top station, by A. Fog"),
       ("Death", "Between 14:20 and 14:50"),
       ("Top station", "Reachable only by the Summit chair – 9 minutes each way"),
       ("First-aid hut", "14:05–14:55: patient S. Berg, sprained ankle, treated by A. Fog"),
     ])},
  {"name": "Kari Lund", "role": "Top-station lift operator", "label": "TOP STATION LOG",
   "quote": "Henrik had found money missing from the books and was going through the accounts himself this weekend. I didn't see who went into the wax room – I can't leave the controls.",
   "evidence": ev_table("Summit chair – top station log", ["Time", "Entry"], [
       ("13:00", "Lift opened – K. Lund and P. Strand on duty"),
       ("14:00–15:00", "Both at the controls, unloading chairs"),
       ("14:30", "Wind check, 6 m/s, lift running"),
       ("15:08", "K. Lund radios patrol – Henrik found"),
     ], mono_cols=(0,))},
  {"name": "Ingrid Moe", "role": "Lodge manager", "label": "STAFF PASS LIST",
   "quote": "I was in the café office at the bottom doing the month's accounts from two until three. I didn't put my nose out of the door. Henrik and I ran this place together for ten years.",
   "evidence": ev_table("Fjellstua – staff lift passes", ["Pass", "Holder"], [
       ("4470", "H. Aas, owner"),
       ("4471", "Spare – hangs on the hook in the café office"),
       ("4472", "K. Lund"),
       ("4473", "S. Berg"),
       ("4474", "P. Strand"),
     ], mono_cols=(0,))},
  {"name": "Ola Dahl", "role": "Owner of a rival lodge", "label": "VETERANS' SLALOM",
   "quote": "Henrik blocked my new lift for three years, everyone knows we hated each other. But I was racing all afternoon, in front of a hundred people.",
   "evidence": ev_table("Veterans' slalom – results", ["Racer", "Run 1", "Run 2"], [
       ("T. Holm", "14:20", "14:39"),
       ("O. Dahl", "14:22", "14:41"),
       ("B. Sæther", "14:24", "14:43"),
       ("G. Lie", "14:26", "14:45"),
     ], mono_cols=(1, 2))},
  {"name": "Mette Rask", "role": "Guest, photographer", "label": "METTE'S PHOTOS",
   "quote": "I rode up to photograph the view from the top. I wear blue, by the way – everyone asks.",
   "evidence": ev_photos("Mette's camera – top station", [
       ("DSC_0611", "14:16", "Empty chairs swinging into the top station."),
       ("DSC_0619", "14:24", "A woman in a red Fjellstua jacket, a folder under her arm, going into the wax room. Face turned away."),
       ("DSC_0627", "14:38", "The wax-room door, shut. Nobody in sight."),
     ])},
  {"name": "Sven Berg", "role": "Ski instructor", "label": "BOTTOM GATE SCANNER",
   "quote": "Henrik sacked me last week, so I'm the obvious one. But I was teaching my two o'clock class until three. Instructors wear blue, lodge staff wear red – Henrik's idea.",
   "evidence": ev_table("Summit chair – pass scans", ["Time", "Gate", "Pass"], [
       ("14:03", "Bottom – up", "Day pass 3381"),
       ("14:12", "Bottom – up", "4471"),
       ("14:15", "Bottom – up", "Day pass 2290"),
       ("14:46", "Top – down", "4471"),
       ("14:51", "Top – down", "Day pass 2290"),
     ], mono_cols=(0,))},
 ],
 "solution": {"killer": "Ingrid Moe",
   "motive": "Money was missing from the books, and Henrik was going through the accounts himself that weekend (clue 2). Ingrid kept the accounts.",
   "proof": ["Pass 4471 rode up at 14:12 and came down at 14:46 (clue 6) – covering the time of death, 14:20–14:50 (clue 1). Pass 4471 is the spare that hangs in the café office (clue 3), where Ingrid says she sat all afternoon.",
             "At 14:24 a woman in a red Fjellstua jacket carried a folder into the wax room (clue 5). Red jackets are worn by lodge staff (clue 6).",
             "The only other woman on the staff, Kari, was at the top-station controls with a colleague the whole hour (clue 2). That leaves Ingrid – with her accounts folder."],
   "cleared": ["<b>Sven</b> lied about teaching – he was at the first-aid hut with a sprained ankle from 14:05 to 14:55 (clue 1) – and instructors wear blue.",
               "<b>Ola</b> hated Henrik, but he was racing at 14:22 and 14:41 (clue 4).",
               "<b>Anders</b> was treating Sven (clue 1), <b>Kari</b> was at the controls (clue 2) and <b>Mette</b> wears blue (clue 5)."]},
}

MYSTERIES = [wedding, ski]
