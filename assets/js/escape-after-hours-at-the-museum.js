/* Six Clues escape room #4 – After Hours at the Museum (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const star = (x, y, r = 4) => `<circle cx="${x}" cy="${y}" r="${r}" fill="#fff8d8"/>`;
const PATTERNS = {
  LYRA: [[200, 60, 9], [170, 120], [215, 125], [160, 185], [205, 190]],
  ORION: [[120, 50, 7], [260, 60], [165, 130], [190, 135], [215, 140], [130, 230], [270, 220, 7]],
  CYGNUS: [[190, 40, 8], [190, 110], [190, 180], [190, 250], [110, 120], [270, 100]],
  CASSIOPEIA: [[80, 120], [130, 70], [190, 120], [250, 60], [310, 110]],
};
const pattern = (k, x, y, s = 1) => `<g transform="translate(${x} ${y}) scale(${s})">${PATTERNS[k].map(p => star(p[0], p[1], p[2] || 4)).join('')}</g>`;
const DRAWERS = [['Melolontha', 6], ['Carabus', 3], ['Lucanus', 1], ['Dytiscus', 8]];
const JARS = [['Anglerfish', '1,500 m'], ['Herring', '50 m'], ['Tripod fish', '4,700 m'], ['Lanternfish', '600 m']];
const FISH = { red: 3, blue: 5, yellow: 2, green: 7 };
const fishSvg = () => { let o = '', i = 0; for (const [c, n] of Object.entries(FISH)) for (let k = 0; k < n; k++, i++) { const x = 40 + (i * 97) % 520, y = 40 + ((i * 53) % 230); o += `<g transform="translate(${x} ${y})"><ellipse rx="22" ry="11" fill="${c === 'yellow' ? '#e8c21a' : c === 'red' ? '#c4232b' : c === 'blue' ? '#2a5ab0' : '#2f8a3a'}"/><path d="M20 0 l16 -10 v20z" fill="${c === 'yellow' ? '#e8c21a' : c === 'red' ? '#c4232b' : c === 'blue' ? '#2a5ab0' : '#2f8a3a'}"/><circle cx="-12" cy="-3" r="2.5" fill="#111"/></g>`; } return o; };
const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
const hallBg = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 7 }, (_, i) => `<rect x="${60 + i * 230}" y="0" width="40" height="660" fill="${c2}"/>`).join('')}<path d="M0 0 H1600 V90 Q800 170 0 90z" fill="${c2}"/><rect y="660" width="1600" height="240" fill="#1a1612"/><ellipse cx="800" cy="0" rx="620" ry="380" fill="url(#lamp)"/>`;

return {
  start: 'hall', v: 1,
  items: {
    uv: ['🔦', 'UV lamp', 'A mineralogist’s ultraviolet lamp. Things glow under it that are invisible in daylight.'],
    earth: ['🗝️', 'Earth key', 'A brass key with a little ammonite on the bow.'],
    sky: ['🗝️', 'Sky key', 'A brass key with a star on the bow.'],
    sea: ['🗝️', 'Sea key', 'A brass key with a shell on the bow.'],
    magnet: ['🧲', 'Horseshoe magnet', 'A strong horseshoe magnet from the navigation display. Iron meteorites cling to it.'],
    staffKey: ['🔑', 'Staff-door key', 'A Yale key on a ring tagged “Curator – private”. It was hidden under the fake meteorite.'],
    stone: ['☄️', 'Kensington meteorite', 'The real meteorite: heavy, cold, pitted iron. The magnet bites into it.'],
  },
  rooms: {
    hall: {
      name: 'The Earth Hall',
      bg: () => hallBg('#3a3128', '#2e271f'),
      spots: [
        { id: 'leaflet', photo: [0, 490, 155, 175], x: 60, y: 480, w: 200, h: 170, art: () => `${E.paper(80, 500, 160, 120, 4)}${L(160, 660, 'Gift-shop leaflet')}`,
          act: () => { E.note('leaflet', 'Gift-shop leaflet: “Spot our famous plaster bone! Old No. 11 was replaced after the war. Replicas of the Kensington meteorite – 7s 6d.”'); E.modal(`<h2>Museum shop leaflet</h2><p class="paper">Can you spot the plaster bone? Our Iguanodon lost <b>No. 11</b> in the Blitz – the replacement was cast in plaster in 1947!<br><br>New this season: hand-painted replicas of the <b>Kensington meteorite</b>, only 7s 6d. Ask at the shop.</p><p class="small">Printed 1951.</p>`); } },
        { id: 'drawers', photo: [335, 340, 205, 270], x: 300, y: 380, w: 300, h: 280, art: () => `<rect x="310" y="390" width="280" height="260" fill="#5b3c25" stroke="#2a1a10" stroke-width="6"/>${[0, 1, 2, 3].map(i => `<rect x="330" y="${410 + i * 58}" width="240" height="46" fill="#6b4a2a" stroke="#2a1a10" stroke-width="3"/><circle cx="450" cy="${433 + i * 58}" r="6" fill="#c9a24a"/>`).join('')}${L(450, 690, 'Beetle drawers')}`, act: () => openDrawers() },
        { id: 'minerals', photo: [555, 260, 280, 340], x: 640, y: 300, w: 260, h: 360, art: () => `<rect x="650" y="310" width="240" height="340" fill="#2a3a3a" stroke="#c9a24a" stroke-width="6"/>${[0, 1, 2].map(i => `<rect x="670" y="${330 + i * 100}" width="200" height="80" fill="#9fc3d8" opacity=".25"/>`).join('')}${L(770, 690, F().mineral ? 'Mineral cabinet (open)' : 'Mineral cabinet (locked)')}`, act: () => openMinerals() },
        { id: 'dino', photo: [820, 110, 480, 490], x: 940, y: 60, w: 460, h: 600, art: () => `<path d="M960 560 Q1050 300 1200 260 Q1330 230 1380 120" stroke="#d8ccb0" stroke-width="22" fill="none"/>${Array.from({ length: 9 }, (_, i) => `<line x1="${1040 + i * 30}" y1="${330 - i * 6}" x2="${1040 + i * 30}" y2="${450 - i * 6}" stroke="#d8ccb0" stroke-width="10"/>`).join('')}<line x1="1100" y1="420" x2="1080" y2="640" stroke="#d8ccb0" stroke-width="18"/><line x1="1250" y1="380" x2="1270" y2="640" stroke="#d8ccb0" stroke-width="18"/>${L(1170, 690, 'Iguanodon skeleton')}`, act: () => openDino() },
        { id: 'panel', photo: [1310, 405, 105, 235], x: 1420, y: 360, w: 160, h: 220, art: () => `${E.paper(1430, 380, 140, 170, 5)}${L(1500, 600, 'Info panel')}`, act: () => openPanel(),
          use: { uv: () => { F().uvPanel = 1; E.note('uv', 'Under UV, the Iguanodon info panel shows writing in invisible ink: “Plaster bone now No. 17 – the old one went to the shop. – H.M.”'); E.say('The UV lamp makes violet letters bloom across the panel: “Plaster bone now No. 17 – the old one went to the shop. – H.M.”'); return true; } } },
        { id: 'toSky', photo: [70, 40, 200, 480], x: 20, y: 60, w: 220, h: 360, art: () => E.door(40, 120, 180, 280, true, '← Meteorite gallery'), act: () => E.go('sky') },
        { id: 'toSea', photo: [200, 640, 400, 260], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('↓ Ocean Hall'), act: () => E.go('sea') },
        { id: 'toOffice', photo: [1480, 300, 115, 310], x: 1300, y: 720, w: 290, h: 150, art: () => E.exit(F().officeOpen ? 'Curator’s office →' : 'Staff door (locked) →', 1320), act: () => F().officeOpen ? E.go('office') : E.say('A door marked PRIVATE – STAFF ONLY. A Yale lock, no keyhole for anything but its own key.'),
          use: { staffKey: () => { F().officeOpen = 1; E.take('staffKey'); E.say('The Yale key turns. The curator’s office smells of pipe smoke and floor polish.'); return true; } } },
      ],
    },
    sky: {
      name: 'The meteorite gallery',
      bg: () => `<rect width="1600" height="900" fill="#141824"/><ellipse cx="800" cy="120" rx="700" ry="260" fill="#0b0e18"/>${F().dome ? pattern(F().dome, 640, 20, 1) : Array.from({ length: 40 }, (_, i) => star((i * 151) % 1400 + 100, (i * 67) % 260 + 20, 2)).join('')}<rect y="660" width="1600" height="240" fill="#10131c"/>`,
      spots: [
        { id: 'back', photo: [1480, 300, 120, 500], x: 1340, y: 740, w: 250, h: 130, art: () => E.exit('Earth Hall →', 1360), act: () => E.go('hall') },
        { id: 'plinth', photo: [10, 380, 360, 470], x: 120, y: 360, w: 300, h: 300, art: () => `<rect x="170" y="520" width="200" height="130" fill="#5b4a3a"/><ellipse cx="270" cy="490" rx="${F().lifted ? 0 : 80}" ry="${F().lifted ? 0 : 45}" fill="#4a4440"/>${E.paper(190, 540, 160, 50, 2)}${L(270, 690, 'The Kensington meteorite')}`, act: () => openPlinth(),
          use: { magnet: () => { if (F().lifted) return false; F().lifted = 1; E.give('staffKey'); E.note('fake', 'The meteorite on the plinth will not take the magnet – it is painted plaster, a gift-shop replica. Under it: a Yale key tagged “Curator – private”.'); E.say('The magnet slides off. You lift the “meteorite” – it weighs nothing. Painted plaster. Underneath lies a Yale key: “Curator – private”.'); return true; } } },
        { id: 'projector', photo: [480, 190, 330, 590], x: 560, y: 380, w: 360, h: 280, art: () => `<rect x="640" y="520" width="200" height="130" fill="#333"/><circle cx="740" cy="470" r="70" fill="#555" stroke="#c9a24a" stroke-width="6"/>${L(740, 690, 'Star projector')}`, act: () => openProjector() },
        { id: 'chart', photo: [845, 310, 295, 285], x: 980, y: 300, w: 300, h: 300, art: () => `<rect x="990" y="310" width="280" height="280" fill="#0b0e18" stroke="#c9a24a" stroke-width="6"/>${Object.keys(PATTERNS).map((k, i) => pattern(k, 1000 + (i % 2) * 135, 320 + Math.floor(i / 2) * 135, .38)).join('')}${L(1130, 630, 'Star chart')}`, act: () => openChart() },
        { id: 'skycase', photo: [1170, 275, 250, 490], x: 1300, y: 340, w: 200, h: 320, art: () => `<rect x="1310" y="360" width="180" height="280" fill="#1e2a40" stroke="#c9a24a" stroke-width="6"/><text x="1400" y="420" text-anchor="middle" font-size="46" fill="#e9dcb8">★</text>${L(1400, 690, F().skyKey ? 'Sky case (empty)' : 'Sky case')}`, act: () => openSkyCase() },
      ],
    },
    sea: {
      name: 'The Ocean Hall',
      bg: () => `<rect width="1600" height="900" fill="#14262e"/><path d="M200 140 Q800 40 1400 160 Q900 230 200 140z" fill="#3a4a52"/><rect y="660" width="1600" height="240" fill="#0e1a20"/><ellipse cx="800" cy="0" rx="600" ry="320" fill="url(#lamp)"/>`,
      spots: [
        { id: 'back', photo: [0, 600, 400, 300], x: 20, y: 740, w: 260, h: 130, art: () => E.exit('↑ Earth Hall'), act: () => E.go('hall') },
        { id: 'jars', photo: [100, 290, 210, 270], x: 80, y: 360, w: 420, h: 300, art: () => `<rect x="90" y="560" width="400" height="30" fill="#5b3c25"/>${[0, 1, 2, 3].map(i => `<rect x="${110 + i * 95}" y="420" width="70" height="140" rx="12" fill="#c9d89f" opacity=".5" stroke="#ddd" stroke-width="3"/>`).join('')}${L(290, 690, 'Specimen jars')}`, act: () => openJars() },
        { id: 'nav', photo: [350, 400, 380, 330], x: 540, y: 360, w: 300, h: 300, art: () => `<rect x="550" y="380" width="280" height="260" fill="#2a3a3a" stroke="#c9a24a" stroke-width="6"/><circle cx="690" cy="500" r="60" fill="#e9dcb8"/><path d="M690 450 L700 500 L690 550 L680 500z" fill="#a33"/>${L(690, 690, F().navOpen ? 'Navigation case (open)' : 'Navigation case')}`, act: () => openNav() },
        { id: 'reef', photo: [805, 290, 495, 270], x: 880, y: 300, w: 360, h: 330, art: () => `<rect x="890" y="310" width="340" height="300" fill="#1f5f7a" stroke="#c9a24a" stroke-width="6"/><g transform="translate(900 320) scale(.55)">${fishSvg()}</g>${L(1060, 650, 'Coral reef diorama')}`, act: () => openReef() },
        { id: 'seacase', photo: [1310, 230, 265, 540], x: 1280, y: 340, w: 220, h: 320, art: () => `<rect x="1290" y="360" width="200" height="280" fill="#1e3a40" stroke="#c9a24a" stroke-width="6"/><text x="1390" y="420" text-anchor="middle" font-size="46" fill="#e9dcb8">🐚</text>${L(1390, 690, F().seaKey ? 'Sea case (empty)' : 'Sea case')}`, act: () => openSeaCase() },
      ],
    },
    office: {
      name: 'The curator’s office',
      bg: () => `<rect width="1600" height="900" fill="#2e2a24"/>${Array.from({ length: 6 }, (_, i) => `<rect x="${100 + i * 70}" y="120" width="56" height="${360 - (i % 3) * 30}" fill="${['#5a2a20', '#2a4a3a', '#3a3a5a'][i % 3]}"/>`).join('')}<rect y="660" width="1600" height="240" fill="#1e1a14"/><ellipse cx="900" cy="0" rx="560" ry="340" fill="url(#lamp)"/>`,
      spots: [
        { id: 'back', photo: [0, 560, 210, 340], x: 20, y: 740, w: 260, h: 130, art: () => E.exit('← Earth Hall'), act: () => E.go('hall') },
        { id: 'register', photo: [0, 0, 520, 560], x: 80, y: 120, w: 440, h: 380, art: () => L(300, 530, 'Accession registers'), act: () => openRegister() },
        { id: 'desk', photo: [330, 440, 870, 460], x: 560, y: 420, w: 480, h: 240, art: () => `<rect x="560" y="470" width="480" height="40" fill="#5b3c25"/><rect x="580" y="510" width="440" height="140" fill="#4a3020"/><rect x="620" y="440" width="70" height="40" rx="8" fill="#111"/><circle cx="655" cy="460" r="16" fill="#333" stroke="#c9a24a" stroke-width="3"/>${E.paper(780, 430, 160, 50, 2)}${L(800, 690, 'Desk, telephone & papers')}`, act: () => openDesk() },
        { id: 'safe', photo: [1200, 80, 375, 600], x: 1120, y: 300, w: 380, h: 360, art: () => `<rect x="1140" y="320" width="340" height="320" rx="10" fill="#3a3c40" stroke="#222" stroke-width="8"/>${['earth', 'sky', 'sea'].map((k, i) => `<circle cx="${1210 + i * 100}" cy="400" r="22" fill="${F()['in_' + k] ? '#c9a24a' : '#111'}"/>`).join('')}<circle cx="1310" cy="520" r="60" fill="#555" stroke="#c9a24a" stroke-width="5"/>${L(1310, 690, F().safeOpen ? 'Safe (open)' : 'Curator’s safe')}`, act: () => openSafe(),
          use: Object.assign(Object.fromEntries(['earth', 'sky', 'sea'].map(k => [k, () => { F()['in_' + k] = 1; E.take(k); E.say(`The ${k} key slides into its keyhole and turns a quarter.` + (F().in_earth && F().in_sky && F().in_sea ? ' All three keys are in. Now the dial.' : '')); return true; }])),
            { magnet: () => { if (!F().safeOpen || E.has('stone')) return false; E.give('stone'); E.note('real', 'The magnet snaps onto the left-hand stone: iron. That is the real Kensington meteorite. The other is plaster.'); E.say('The magnet slides off one stone and snaps hard onto the other. That one is iron – the real meteorite. You lift it out: heavy and cold.'); return true; } }) },
      ],
    },
  },
  combine: (a, b) => false,
  stages: [
    ['minerals', () => F().mineral, ['The mineral cabinet has a four-digit lock. The beetle drawers have numbers.', 'A card on the drawers says how to read them: by the alphabet.', 'Carabus 3, Dytiscus 8, Lucanus 1, Melolontha 6 → 3816.']],
    ['bone', () => F().earthKey, ['The UV lamp shows what ordinary light hides. Try it on the Iguanodon’s info panel.', 'The shop leaflet says No. 11 – but it was printed in 1951. The invisible note is newer.', 'Bone No. 17 is the plaster one: open it for the Earth key.']],
    ['magnet', () => F().navOpen, ['The navigation case wants the jars in order. The brass plate says “from the light to the dark”.', 'Light fades with depth. Read each jar’s depth.', 'Herring, Lanternfish, Anglerfish, Tripod fish.']],
    ['fake', () => F().lifted, ['The meteorite is meant to be iron.', 'Iron sticks to a magnet. Test the meteorite with the horseshoe magnet.', 'Use the magnet on the plinth: it’s plaster, and a key is hidden underneath.']],
    ['office', () => F().officeOpen, ['The Yale key from under the fake fits a door in the Earth Hall.', 'The staff door at the far end of the Earth Hall.', 'Use the staff-door key on the staff door.']],
    ['sky', () => F().skyKey, ['The projector shows the sky of a chosen night. Which night matters here?', 'The plinth label’s glue is fresh – trust the curator’s register instead: the meteorite fell on 21 June. Set the projector, then compare the dome with the star chart.', 'The dome shows Lyra. Enter LYRA on the Sky case.']],
    ['sea', () => F().seaKey, ['The Sea case’s dials are coloured. Something in the Ocean Hall has those colours.', 'Count the fish of each colour in the reef diorama, then read them in the dials’ colour order.', 'Yellow 2, red 3, green 7, blue 5 → 2375.']],
    ['safe', () => F().safeOpen, ['The safe needs three keys and a three-figure dial.', 'The register gives the meteorite an accession number.', 'Earth, Sky and Sea keys in the keyholes, then dial 621 (BM 1904,621).']],
    ['real', () => E.has('stone'), ['Two stones in the safe. Only one is the real meteorite.', 'You already know how to test for iron.', 'Use the magnet on the stones: the one it grips is real.']],
    ['phone', () => F().won, ['Time to call for help. The curator kept a card by the phone.', 'Old London numbers start with letters. On a dial, each letter shares a hole with a number.', 'WHItehall 1212: W=9, H=4, I=4 → dial 9441212.']],
  ],
  intro: ['London · Friday 14 November 1958 · 22:00', 'After Hours at the Museum',
    `<p>You are a junior reporter for the <i>Evening Courier</i>. A tip-off said the museum’s famous Kensington meteorite has been swapped for a fake – so you hid in a cloakroom at closing time.</p><p>The lights are down. At 23:00 the night guard starts his round, and the thief will come back for the real stone. You have one hour to find it and raise the alarm.</p><p>Level 2: not every label in this museum is true.</p>`,
    'The great hall is silent. A dinosaur looms in the dark. Look around.'],
  timesUp: ['23:00.', 'A key turns in the staff door. Footsteps – and the stone leaves the building in a shopping bag.'],
  win: ['Whitehall 1212', 'Within ten minutes a police car pulls up on Cromwell Road. At 23:02 Hugo Marsh, assistant curator, lets himself in by the staff door with a gift-shop bag – and finds a constable waiting. The Kensington meteorite is back on its plinth by Monday, and your story makes the front page.'],
};

function openDrawers() {
  E.note('drawers', 'Beetle drawers (number on each): ' + DRAWERS.map(d => `${d[0]} ${d[1]}`).join(' · ') + '. Card: “Specimens are filed alphabetically.”');
  E.modal(`<h2>Beetle drawers</h2><div class="paper"><table style="width:100%">${DRAWERS.map(d => `<tr><td><i>${d[0]}</i></td><td style="text-align:right"><b>${d[1]}</b></td></tr>`).join('')}</table></div><p class="small">A typed card pinned to the cabinet: “Specimens are filed alphabetically. Please return drawers in order.”</p>`);
}
function openMinerals() {
  if (F().mineral) return E.say(E.has('uv') ? 'Empty shelves where the UV lamp was.' : 'Quartz, galena, a lump of sulphur.');
  E.numLock('Mineral cabinet', 'A brass combination lock with four wheels.', 4, c => { if (c !== '3816') return false; F().mineral = 1; E.give('uv'); E.say('The cabinet opens. Among the crystals: a mineralogist’s UV lamp.'); return true; });
}
function openPanel() {
  if (F().uvPanel) return E.say('“Plaster bone now No. 17 – the old one went to the shop. – H.M.”');
  E.modal(`<h2>Iguanodon bernissartensis</h2><p class="paper">Found in a Belgian coal mine in 1878. Our skeleton is a cast of the Brussels original, with real bones where the war left gaps. Each bone carries a small number.</p><p class="small">The panel’s white border looks oddly smudged, as if someone wrote on it with a dry pen.</p>`);
}
function openDino() {
  if (F().earthKey) return E.say('Bone No. 17 hangs open on its hinge – empty now.');
  E.numLock('Iguanodon skeleton', 'Every bone has a tiny number. Which one do you prise open?', 2, c => {
    if (c === '11') { E.say('Bone No. 11 is solid fossil – heavy and real. The leaflet was out of date.'); return false; }
    if (c !== '17') return false; F().earthKey = 1; E.give('earth'); E.say('Bone No. 17 is hollow plaster. Inside, wrapped in cotton wool: a brass key with an ammonite on the bow.'); return true;
  }, 'Solid fossil. That isn’t the plaster one.');
}
function openPlinth() {
  if (F().lifted) return E.say('An empty plinth and a painted plaster lump. The real stone is somewhere else.');
  E.note('plinth', 'Plinth label: “Kensington meteorite – iron. Fell 12 March 1904.” The glue on the label is still tacky.');
  E.modal(`<h2>The Kensington meteorite</h2><p class="paper">Iron meteorite, 31 kg.<br>Fell at Kensington Gardens, <b>12 March 1904</b>.</p><p class="small">The label looks brand new, and the glue under its corner is still tacky. The stone has a faint smell of paint.</p>`);
}
function openProjector() {
  E.cycler('Star projector', 'Set the date and the dome shows the sky over London on that night.', [{ name: 'Month', opts: MONTHS }, { name: 'Day ×10', opts: ['0', '1', '2', '3'] }, { name: 'Day ×1', opts: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] }], v => {
    const d = v[0] + ' ' + (+v[1] * 10 + +v[2]);
    F().dome = d === 'Jun 21' ? 'LYRA' : d === 'Mar 12' ? 'ORION' : null;
    E.say(F().dome ? 'The projector hums and a constellation blooms on the dome overhead.' : 'A blur of stars sweeps across the dome. Nothing stands out.');
    return true;
  }, '', 'Project');
}
function openChart() {
  E.note('chart', 'Star chart: Lyra (bright Vega above a small parallelogram), Orion, Cygnus (a cross), Cassiopeia (a W).');
  E.modal(`<h2>Star chart</h2><svg viewBox="0 0 760 640" class="close" style="background:#0b0e18">${Object.keys(PATTERNS).map((k, i) => pattern(k, 20 + (i % 2) * 370, 10 + Math.floor(i / 2) * 310, .9) + `<text x="${190 + (i % 2) * 370}" y="${300 + Math.floor(i / 2) * 310}" text-anchor="middle" fill="#e9dcb8" font-family="Georgia" font-size="24">${k[0] + k.slice(1).toLowerCase()}</text>`).join('')}</svg>`);
}
function openSkyCase() {
  if (F().skyKey) return E.say('The Sky case stands open and empty.');
  E.wordLock('Sky case', 'A star-shaped brass lock with four letter wheels. Engraved: “Name the stars that fell with it.”', 4, w => { if (w !== 'LYRA') return false; F().skyKey = 1; E.give('sky'); E.say('The Sky case clicks open: a brass key with a star on the bow.'); return true; });
}
function openJars() {
  E.note('jars', 'Specimen jars (depth caught): ' + JARS.map(j => `${j[0]} ${j[1]}`).join(' · ') + '.');
  E.modal(`<h2>Specimen jars</h2><div class="paper"><table style="width:100%">${JARS.map(j => `<tr><td>${j[0]}</td><td style="text-align:right">caught at ${j[1]}</td></tr>`).join('')}</table></div>`);
}
function openNav() {
  if (F().navOpen) return E.say(E.has('magnet') || F().lifted ? 'A ship’s compass and an empty hook where the magnet hung.' : 'The case is open. A horseshoe magnet hangs inside.');
  E.orderer('Navigation case', 'Four buttons, one per specimen. A brass plate: <i>“From the light to the dark.”</i>', JARS.map(j => j[0]), o => { if (o.join() !== 'Herring,Lanternfish,Anglerfish,Tripod fish') return false; F().navOpen = 1; E.give('magnet'); E.say('The navigation case swings open. You take the horseshoe magnet from its hook.'); return true; });
}
function openReef() {
  E.note('reef', 'Coral reef diorama – count the fish by colour.');
  E.modal(`<h2>Coral reef diorama</h2><svg viewBox="0 0 600 320" class="close" style="background:#1f5f7a">${fishSvg()}</svg>`);
}
function openSeaCase() {
  if (F().seaKey) return E.say('The Sea case stands open and empty.');
  E.numLock('Sea case', 'Four number dials, painted <b style="color:#e8c21a">yellow</b>, <b style="color:#e05050">red</b>, <b style="color:#3fa34d">green</b> and <b style="color:#5a8ae0">blue</b>, left to right.', 4, c => { if (c !== '2375') return false; F().seaKey = 1; E.give('sea'); E.say('The Sea case opens: a brass key with a shell on the bow.'); return true; });
}
function openRegister() {
  E.note('register', 'Accession register, 1904: “BM 1904,621 – Kensington meteorite, iron, 31 kg. Fell Kensington Gardens 21 June 1904 (midsummer night).”');
  E.modal(`<h2>Accession register – 1904</h2><p class="paper">BM 1904,620 – fossil sponge, Wiltshire.<br><b>BM 1904,621</b> – Kensington meteorite, iron, 31 kg. Fell Kensington Gardens on the night of <b>21 June 1904</b> (midsummer). Witnessed by a park keeper.<br>BM 1904,622 – Hawksbill turtle shell.</p><p class="small">The curator’s own handwriting, faded brown ink.</p>`);
}
function openDesk() {
  E.note('desk', 'Desk: guard’s round sheet (round starts 23:00 at the staff door). Card by the telephone: “Emergency – Scotland Yard: WHItehall 1212. Dial the first three letters of the exchange, then the number.”');
  E.modal(`<h2>The curator’s desk</h2><h3>Card by the telephone</h3><p class="paper">Emergency – Scotland Yard: <b>WHItehall 1212</b><br><span class="small">Dial the first three letters of the exchange, then the number.</span></p><h3>Telephone dial</h3><p class="paper">1 · 2 ABC · 3 DEF · 4 GHI · 5 JKL · 6 MNO · 7 PRS · 8 TUV · 9 WXY · 0 OPER</p><h3>Night guard’s round</h3><p class="paper">23:00 staff door · 23:07 Earth Hall · 23:15 Ocean Hall · 23:24 meteorite gallery</p>${E.has('stone') ? '<button class="btn" id="dial">Pick up the telephone</button>' : '<p class="small">You won’t get anyone to believe you without the real meteorite in your hands.</p>'}`, m => {
    const b = m.querySelector('#dial'); b && b.addEventListener('click', () => E.numLock('Telephone', 'Dial seven digits.', 7, c => { if (c !== '9441212') return false; E.say('“Scotland Yard.” You talk fast.'); E.win(); return true; }, 'A wrong number – a sleepy voice in Fulham.'));
  });
}
function openSafe() {
  if (F().safeOpen) {
    if (E.has('stone')) return E.say('Only the second stone is left in the safe – a light, painted replica.');
    return E.modal(`<h2>The safe</h2><p>Two stones on a velvet cloth, almost identical. A note in the same hand as the panel: <i>“Collect 23:00. – H.M.”</i></p><p class="small">One is the real iron meteorite. The other is another shop replica.</p>`);
  }
  if (!(F().in_earth && F().in_sky && F().in_sea)) return E.say('A heavy safe with three keyholes – marked with an ammonite, a star and a shell – and a three-figure dial.');
  E.numLock('Safe dial', 'Three figures.', 3, c => { if (c !== '621') return false; F().safeOpen = 1; E.note('safe', 'In the safe: two near-identical stones and a note: “Collect 23:00. – H.M.”'); E.say('The bolts draw back. Inside: two stones on velvet, and a note.'); return true; });
}
});
