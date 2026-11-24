# Billedcyklus – driftsnote

Genererer de manglende mysteriebilleder (portrætter, bevisfotos, covers) med Dennis' ChatGPT Plus i Chrome på laptoppen (DNH-LAPTOP) og lægger dem i `assets/img/m/<case>/<name>.jpg`.

## Dele

| Fil | Hvad |
|---|---|
| `tools/m_images.py` | Skriver `tools/mystery_images.md` med alle billeder, der stadig mangler (køres også af `export.py`). |
| `tools/img_driver.js` | Driveren, der kører i en chatgpt.com-fane: ét billede ad gangen, ny chat pr. billede, beskærer til sidens format og gemmer som JPG. |
| `tools/img_install.py` | Lægger hentede billeder ind i `assets/img/m/` (beskærer/komprimerer igen for en sikkerheds skyld) og kører `export.py`. |

## Fanen

- Én fast chatgpt.com-fane i Chrome, titel **"🤖 RØR IKKE DENNE FANE – 6c"**. Hold den gerne i sit eget vindue, så den ikke ligger i baggrunden (Chrome bremser timere i skjulte faner).
- Første gang skal Chrome have lov til "flere downloads" fra chatgpt.com (klik **Tillad**, når Chrome spørger).
- Hvert billede downloades som `6c__<case>__<name>.jpg` til Chromes download-mappe og gemmes også i fanens IndexedDB (`6c` / `img`).
- localStorage i fanen:
  - `__q_backup` – den fulde kø: `[key, "P"|"E", prompt]`
  - `__6c_missing` – manglende nøgler, kompakt (`case:navn,navn;case:navn`)
  - `__6cSaved` – nøgler der allerede er downloadet (`case__navn`)
  - `__q` – den aktuelle restkø
  - `__6c_driver` – en kopi af driveren

## Status i fanen

```js
__6cStatus()        // running, current, left, failed, sidste log-linjer
__6cStop()          // stopper efter det aktuelle billede
__6cRequeue()       // sætter fejlede billeder i kø igen
__6cGrab('case/navn') // gemmer billedet, der står på siden, under den nøgle
```

Rate limit fra ChatGPT: driveren pauser selv 45 min og fortsætter.

## Genstart efter reboot / genindlæst fane

1. Åbn chatgpt.com (logget ind) i en fane.
2. Kør i fanen (javascript-værktøjet eller konsollen):
   ```js
   (0, eval)(localStorage.__6c_driver); __6cStart(null, {skipSaved: true})
   ```
3. Mangler `__6c_driver` (ny browserprofil): indsæt hele `tools/img_driver.js`, og kør derefter `__6cStart(null, {skipSaved: true})`.
4. Er `__6c_missing` forældet (efter mange installerede billeder), opdatér den først:
   `python3 tools/img_install.py --missing-compact` → `localStorage.__6c_missing = "<output>"`.

## Installér, commit, push

På en maskine med repoet og adgang til download-mappen:

```bash
git pull --rebase
python3 tools/img_install.py ~/Downloads          # finder 6c__*.jpg (og ZIP'er), kører export.py
git add assets/img/m tools/mystery_images.md app/mysteries.php VERSION
git commit -m "Images: <antal> nye mysteriebilleder" && git push
```

Flyt de installerede filer ud af download-mappen bagefter (fx til `~/Downloads/6c-done/`), så de ikke tælles to gange. Sitet henter selv ændringer fra GitHub via `/cron/deploy` (hver time, minut 07, eller `fetch('/cron/deploy?force=1')` fra en 6clues.com-fane).

Den planlagte opgave **"6clues image cycle"** (bundet til DNH-LAPTOP) gør dette hver ~2. time: tjekker fanen, genstarter driveren hvis nødvendigt, installerer nye billeder, committer, pusher og deployer.
