# Writing new Six Clues mysteries

Every mystery lives in `tools/mysteries/roundN.py` as a Python dict, and each round file ends with
`MYSTERIES = [...]`. The site data (`app/mysteries.php`) and `VERSION` are generated, so never edit them by hand.

## Workflow
1. Create the next `tools/mysteries/roundN.py`. Copy the import line from `round3.py`.
2. Write the mysteries. Each one has a unique `slug`, `level` 1–3, `crime` (UPPERCASE, e.g. THEFT, MURDER,
   SABOTAGE, FORGERY, DISAPPEARANCE, CAR THEFT, HACKING, BLACKMAIL, SMUGGLING, ARSON, FRAUD, KIDNAPPING),
   `who` (killer / thief / saboteur / forger / culprit / hacker …), `caseno`, `title_html` (with `<br>`),
   `title_plain`, `teaser` (≤160 chars), `intro`, `clues` (exactly 6), `solution`, and `added` (YYYY-MM-DD).
3. Run `python3 tools/export.py`. It validates the mysteries and refuses to export if anything is wrong.
4. Run `python3 tools/check_layout.py <slugs>`. Every poster must fit; shorten any text that overflows.
5. Commit and push to `main`, including `tools/schedule.json`. Simply's hourly cron (`/cron/deploy`) installs the new version on 6clues.com.

## Daily cases
The first 30 mysteries form the free library (public at once, no daily date). Every mystery after that is the site's daily case on one date (`tools/schedule.json`, written by `export.py`): level 3 at weekends, level 1/2 on weekdays. A daily case stays hidden until its date, then joins the library. Never edit `schedule.json` by hand, or dates already announced could move.
On screen the clues are opened in order, and fewer clues = more points (100/85/70/55/40/25). So clue 1 must not give the answer away, and the decisive evidence should be spread over clues 2–6.

## Rules for a fair, fun mystery
- **Six suspects, one per poster.** Each poster has the suspect's statement plus one piece of evidence.
- **Exactly one culprit.** That person is the only one the evidence can't clear. Every other suspect is cleared by
  something concrete: an alibi backed by evidence, a physical detail, or not having the access needed.
- **The culprit lies.** Their own statement must contradict at least one piece of evidence.
- **Level 1 – Rookie (5–10 min):** 2–3 direct links. The culprit's lie is exposed by one piece of evidence. Highlighting a key row is allowed.
- **Level 2 – Detective (10–20 min):** at least one trick that must be worked out (wrong clock, time zone, tide, a changed programme, a weight, a route that takes longer than claimed). At least one false lead that points at an innocent suspect. No highlighted rows (`highlight=` is ignored for level 2+). The proof needs at least 3 clues.
- **Level 3 – Mastermind (20–40 min):** real head-scratching. Rules:
  - The proof needs **at least 4 clues combined**; no single poster points at the culprit.
  - The culprit's lie is **never contradicted directly** – the contradiction only appears when two or more documents are combined (time arithmetic, a route, an object that couldn't be where it was, two logs in different time formats).
  - **At least two strong red herrings**: an innocent suspect with motive and a suspicious detail, and an innocent who lies about something else (embarrassing but harmless).
  - **No nudges**: no notes, sticky notes, captions or “NB” lines that state or hint at the conclusion (“The phone was not hers”, “He shared a toast with someone he knew”). Notes may only state neutral facts.
  - **No emphasis**: don't use `<b>` or `highlight=` – export strips them anyway. Put the decisive fact in an ordinary row among 4–6 ordinary rows, so it must be found.
  - Plausible noise: tables and logs contain several rows that don't matter.
- Times are written 24h (`21:43`). Every time must be consistent across all six posters, so check them all.
- The solution's `proof` and `cleared` lists name the clue numbers that prove each point.
- Family-friendly: no gore, no sexual content, no real people or brands. Keep "flasher" or prowler cases tame.
- Fresh settings every time. Check the existing slugs and settings so nothing repeats.

## Evidence helpers (from `tools/lib.py`)
`ev_rows(title, [(label, value), …], note)` · `ev_table(title, headers, rows, highlight=lambda r: …, note, mono_cols)` ·
`ev_programme(heading, sub, [(time, item), …], sticky)` · `ev_phone(title, caption, [(to, time, text), …])` ·
`ev_note(title, [lines], sign, side)` · `ev_receipt([(kind, text), …])` (kinds: h, s, hr, b, "") ·
`ev_photos(title, [(file, time, caption), …])` (exactly 3 photos).
Keep tables to 6 rows or fewer, and quotes to 300 characters or fewer.

## Images
Each case can have a cover (`assets/img/m/<case>/cover.jpg`, 1600×1200) and six suspect portraits (`assets/img/m/<case>/<person-slug>.jpg`, 1024×1024). Until a file exists the site shows a grey silhouette. `export.py` rewrites `tools/mystery_images.md` – the list of missing images with prompts – every time it runs; commit it together with the round.

## Culprit position
Don't worry about which clue number the culprit gets. `export.py` (`spread_culprit`) moves the culprit's poster to a pseudo-random clue 2–6 and renumbers every “clue N” reference, and all answer lists are shown alphabetically. So always write references as “clue N” / “clues N and M”, never “the last clue”.
