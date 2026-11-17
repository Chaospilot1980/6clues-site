/* Six Clues escape room #5 – The Alchemist's Attic (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const SIGNS = ['♈ Aries', '♉ Taurus', '♊ Gemini', '♋ Cancer', '♌ Leo', '♍ Virgo', '♎ Libra', '♏ Scorpio', '♐ Sagittarius', '♑ Capricorn', '♒ Aquarius', '♓ Pisces'];
const KEY = [['♀', 'A'], ['♂', 'E'], ['☽', 'F'], ['♃', 'I'], ['☿', 'L'], ['☉', 'M'], ['♄', 'N'], ['♁', 'T']];
const room = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 9 }, (_, i) => `<rect x="${i * 190}" y="0" width="22" height="660" fill="${c2}"/>`).join('')}<rect y="660" width="1600" height="240" fill="#1a130c"/><ellipse cx="800" cy="0" rx="560" ry="360" fill="url(#lamp)"/>`;
const flask = (x, y, c) => `<path d="M${x - 14} ${y - 70} h28 v40 l40 70 a14 14 0 0 1 -12 22 h-84 a14 14 0 0 1 -12 -22 l40 -70z" fill="${c}" stroke="#ddd" stroke-width="3" opacity=".85"/>`;
const SEALS = ['earth', 'water', 'air', 'fire'];

return {
  start: 'attic', v: 1,
  items: {
    mirror: ['🪞', 'Hand mirror', 'A small silver hand mirror with a cracked handle.'],
    ring: ['⭕', 'Iron ring', 'A heavy iron ring with a screw thread – a handle for something.'],
    charcoal: ['⚫', 'Charcoal', 'A sack of good beech charcoal.'],
    hatchKey: ['🗝️', 'Hatch key', 'A small iron key stamped with a crescent moon.'],
    earth: ['🟫', 'Earth seal', 'A square seal of clay with the sign ▽ crossed.'],
    water: ['🟦', 'Water seal', 'A seal of blue glass with the sign ▽.'],
    air: ['⬜', 'Air seal', 'A seal of white alabaster with the sign △ crossed.'],
    fire: ['🟥', 'Fire seal', 'A seal of red enamel with the sign △.'],
  },
  rooms: {
    attic: {
      name: 'The laboratory in the attic',
      bg: () => room('#3a2a1c', '#2c2015'),
      spots: [
        { id: 'note', photo: [315, 80, 100, 110], x: 60, y: 120, w: 260, h: 260, art: () => `${E.paper(80, 140, 220, 200, 5)}${L(190, 380, 'Note on the beam')}`, act: () => openNote(),
          use: { mirror: () => { F().mirrored = 1; E.note('mirror', 'Master Kavka’s note, read in the mirror: “BODY, SOUL, SPIRIT – then the library will open. Trust nothing written in green.”'); E.say('In the mirror the scrawl turns into plain words: “Body, soul, spirit – then the library will open. Trust nothing written in green.”'); return true; } } },
        { id: 'table', photo: [260, 420, 240, 330], x: 360, y: 400, w: 260, h: 260, art: () => `<rect x="370" y="520" width="240" height="30" fill="#5b3c25"/><ellipse cx="490" cy="500" rx="40" ry="22" fill="${F().mirror ? '#3a2a1c' : '#c0c8d0'}"/>${L(490, 690, 'Washstand')}`,
          act: () => { if (F().mirror) return E.say('A cracked basin and a dry sponge.'); F().mirror = 1; E.give('mirror'); E.say('Beside the basin: the master’s silver hand mirror.'); } },
        { id: 'chart', photo: [645, 50, 340, 320], x: 660, y: 120, w: 280, h: 300, art: () => `${E.paper(670, 130, 260, 260, 5)}${L(800, 430, 'Chart of principles')}`, act: () => openPrinciples() },
        { id: 'desk', photo: [950, 400, 385, 350], x: 980, y: 420, w: 300, h: 240, art: () => `<rect x="990" y="470" width="280" height="40" fill="#5b3c25"/><rect x="1010" y="510" width="240" height="140" fill="#4a3020"/><rect x="1060" y="440" width="120" height="30" fill="#2f6a3a"/>${L(1130, 690, 'Writing desk')}`, act: () => openDesk() },
        { id: 'trapdoor', photo: [545, 700, 420, 120], x: 640, y: 680, w: 320, h: 180, art: () => `<rect x="660" y="700" width="280" height="140" fill="#2a1c10" stroke="#5b3c25" stroke-width="8"/>${F().trapOpen ? '' : '<circle cx="800" cy="770" r="10" fill="#555"/>'}${L(800, 870, F().trapOpen ? 'Trapdoor ↓ cellar' : 'Trapdoor')}`,
          act: () => F().trapOpen ? E.go('cellar') : E.say('A trapdoor in the floorboards. There is a threaded hole where a handle should be – no way to lift it.'),
          use: { ring: () => { F().trapOpen = 1; E.take('ring'); E.say('The iron ring screws into the hole. You heave the trapdoor up: steps lead down into warm darkness.'); return true; } } },
        { id: 'toLibrary', photo: [1390, 170, 200, 600], x: 1320, y: 120, w: 260, h: 480, art: () => E.door(1340, 160, 200, 420, F().libOpen, F().libOpen ? 'Library →' : 'Library door'), act: () => F().libOpen ? E.go('library') : openLibDoor() },
        { id: 'ladder', photo: [60, 110, 240, 740], x: 40, y: 420, w: 220, h: 440, art: () => `<line x1="90" y1="420" x2="90" y2="860" stroke="#6b4a2a" stroke-width="14"/><line x1="200" y1="420" x2="200" y2="860" stroke="#6b4a2a" stroke-width="14"/>${[0, 1, 2, 3, 4, 5].map(i => `<line x1="90" y1="${460 + i * 70}" x2="200" y2="${460 + i * 70}" stroke="#6b4a2a" stroke-width="10"/>`).join('')}${L(145, 405, F().hatchOpen ? 'Ladder ↑ roof' : 'Ladder to roof hatch')}`,
          act: () => F().hatchOpen ? E.go('roof') : E.say('A ladder up to a hatch in the roof. The hatch is locked – a small keyhole with a crescent moon.'),
          use: { hatchKey: () => { F().hatchOpen = 1; E.take('hatchKey'); E.say('The crescent key turns. Cold night air pours in through the hatch.'); return true; } } },
      ],
    },
    library: {
      name: 'The library',
      bg: () => room('#2c2418', '#3a2c1c'),
      spots: [
        { id: 'back', photo: [0, 700, 120, 200], x: 20, y: 740, w: 260, h: 130, art: () => E.exit('← Laboratory'), act: () => E.go('attic') },
        { id: 'portrait', photo: [30, 15, 295, 410], x: 60, y: 100, w: 260, h: 340, art: () => `<rect x="80" y="120" width="220" height="280" fill="#5a3a20" stroke="#c9a24a" stroke-width="10"/><circle cx="190" cy="230" r="60" fill="#c8a080"/>${L(190, 440, 'Portrait of the emperor')}`,
          act: () => { E.note('portrait', 'Brass plate under the portrait: “Rudolf II – King of Bohemia 1575, crowned Holy Roman Emperor 1576.”'); E.modal(`<h2>Portrait of the emperor</h2><p class="paper">Rudolf II<br>King of Bohemia 1575 · crowned Holy Roman Emperor <b>1576</b></p><p class="small">The court painter has given him a very long chin.</p>`); } },
        { id: 'globe', photo: [200, 365, 360, 460], x: 380, y: 380, w: 240, h: 280, art: () => `<circle cx="500" cy="480" r="90" fill="#6a8aa0" stroke="#c9a24a" stroke-width="8"/><rect x="480" y="570" width="40" height="80" fill="#5b3c25"/>${L(500, 690, 'Globe')}`, act: () => openGlobe() },
        { id: 'books', photo: [420, 0, 830, 420], x: 660, y: 100, w: 440, h: 360, art: () => `${Array.from({ length: 3 }, (_, r) => Array.from({ length: 12 }, (_, i) => `<rect x="${680 + i * 34}" y="${120 + r * 110}" width="28" height="94" fill="${['#5a2a20', '#2a4a3a', '#3a3a5a', '#6a5a2a'][(i + r) % 4]}"/>`).join('')).join('')}${L(880, 470, 'Books')}`, act: () => openBooks() },
        { id: 'lectern', photo: [905, 340, 460, 440], x: 1140, y: 360, w: 260, h: 300, art: () => `<path d="M1180 420 L1360 400 L1340 460 L1200 480z" fill="#6b4a2a"/><rect x="1260" y="470" width="20" height="180" fill="#5b3c25"/>${L(1270, 690, 'Lectern with horoscopes')}`, act: () => openHoroscopes() },
        { id: 'ledger', photo: [1260, 530, 340, 330], x: 1420, y: 420, w: 160, h: 240, art: () => `${E.paper(1430, 440, 140, 170, 5)}${L(1500, 650, 'Court ledger')}`, act: () => openLedger() },
      ],
    },
    cellar: {
      name: 'The furnace cellar',
      bg: () => `<rect width="1600" height="900" fill="#1e1610"/>${Array.from({ length: 10 }, (_, r) => Array.from({ length: 12 }, (_, c) => `<rect x="${c * 140 + (r % 2) * 70}" y="${r * 66}" width="132" height="60" fill="#2a1e14"/>`).join('')).join('')}<rect y="660" width="1600" height="240" fill="#140e0a"/>${F().fired ? '<ellipse cx="800" cy="480" rx="300" ry="200" fill="#ff7a2a" opacity=".25"/>' : ''}`,
      spots: [
        { id: 'up', photo: [0, 700, 220, 200], x: 20, y: 740, w: 260, h: 130, art: () => E.exit('↑ Laboratory'), act: () => E.go('attic') },
        { id: 'coal', photo: [110, 395, 320, 300], x: 60, y: 440, w: 220, h: 220, art: () => `<path d="M80 650 Q170 470 260 650z" fill="#111"/>${L(170, 690, 'Coal bin')}`,
          act: () => { if (E.has('charcoal') || F().charcoal) return E.say('Black dust. Nothing more.'); F().charcoal = 1; E.give('charcoal'); E.say('You drag out a sack of good beech charcoal.'); } },
        { id: 'furnace', photo: [410, 40, 465, 640], x: 620, y: 260, w: 360, h: 400, art: () => `<path d="M650 650 V380 Q800 260 950 380 V650z" fill="#5a3a2a" stroke="#2a1a10" stroke-width="8"/><rect x="740" y="480" width="120" height="100" rx="10" fill="${F().fired ? '#ff9a3a' : '#111'}"/><text x="800" y="420" text-anchor="middle" font-size="34" fill="#e9dcb8">☽ ☿ ♀ ☉ ♂</text>${L(800, 690, 'Athanor furnace')}`, act: () => openFurnace(),
          use: { charcoal: () => { if (!F().furnaceOpen) return false; F().fired = 1; E.take('charcoal'); E.say('You heap the charcoal and pump the bellows. The athanor roars – and in the heat, a red enamel seal drops from a niche above the fire door.'); E.give('fire'); return true; } } },
        { id: 'scale', photo: [885, 265, 205, 460], x: 1020, y: 380, w: 280, h: 280, art: () => `<line x1="1160" y1="420" x2="1160" y2="640" stroke="#c9a24a" stroke-width="10"/><line x1="1050" y1="440" x2="1270" y2="${F().balanced ? 440 : 470}" stroke="#c9a24a" stroke-width="8"/><ellipse cx="1060" cy="470" rx="40" ry="10" fill="#c9a24a"/><ellipse cx="1260" cy="${F().balanced ? 470 : 500}" rx="40" ry="10" fill="#c9a24a"/>${L(1160, 690, 'Apothecary’s scale')}`, act: () => openScale() },
        { id: 'flasks', photo: [1185, 330, 410, 500], x: 1320, y: 360, w: 260, h: 300, art: () => `${flask(1370, 560, '#111')}${flask(1440, 560, '#eee')}${flask(1510, 560, '#e8c21a')}${flask(1560, 560, '#b0202a')}${L(1460, 690, 'Four flasks & basin')}`, act: () => openFlasks() },
      ],
    },
    roof: {
      name: 'The roof observatory',
      bg: () => `<rect width="1600" height="900" fill="#0d1020"/>${Array.from({ length: 60 }, (_, i) => `<circle cx="${(i * 137) % 1600}" cy="${(i * 71) % 400}" r="${i % 7 ? 1.5 : 3}" fill="#fff8d8"/>`).join('')}<path d="M0 520 L200 430 L340 520 L520 380 L700 520 L1600 520 V660 H0z" fill="#141826"/><rect y="660" width="1600" height="240" fill="#22180f"/>`,
      spots: [
        { id: 'down', photo: [0, 500, 500, 380], x: 20, y: 740, w: 280, h: 130, art: () => E.exit('↓ Laboratory'), act: () => E.go('attic') },
        { id: 'wheel', photo: [260, 10, 600, 640], x: 380, y: 160, w: 460, h: 460, art: () => `<circle cx="610" cy="390" r="210" fill="#2a2418" stroke="#c9a24a" stroke-width="8"/><circle cx="610" cy="390" r="140" fill="none" stroke="#c9a24a" stroke-width="4"/><circle cx="610" cy="390" r="70" fill="none" stroke="#c9a24a" stroke-width="4"/>${SIGNS.map((s, i) => `<text x="${610 + Math.cos(i * Math.PI / 6) * 175}" y="${400 + Math.sin(i * Math.PI / 6) * 175}" text-anchor="middle" font-size="26" fill="#e9dcb8">${s[0]}</text>`).join('')}${L(610, 650, 'Astrological wheel')}`, act: () => openWheel() },
        { id: 'chest', photo: [965, 460, 465, 340], x: 960, y: 380, w: 420, h: 280, art: () => `<rect x="980" y="440" width="380" height="200" rx="12" fill="#4a3020" stroke="#c9a24a" stroke-width="6"/>${SEALS.map((k, i) => `<rect x="${1010 + i * 88}" y="470" width="60" height="60" fill="${F()['in_' + k] ? ['#7a5a3a', '#2a5ab0', '#ddd', '#b0202a'][i] : '#1a120c'}" stroke="#c9a24a" stroke-width="3"/>`).join('')}${L(1170, 690, F().chestOpen ? 'Chest (open)' : 'Chest of the four elements')}`, act: () => openChest(),
          use: Object.fromEntries(SEALS.map(k => [k, () => { F()['in_' + k] = 1; E.take(k); const all = SEALS.every(s => F()['in_' + s]); if (all) F().chestOpen = 1; E.say(all ? 'The fourth seal clicks into place. Somewhere inside the chest, bolts slide back one after another – the lid rises.' : `The ${k} seal fits its square socket.`); return true; }])) },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['mirror', () => F().mirrored, ['The note on the beam is written backwards.', 'Leonardo wrote that way too. Something on the washstand helps.', 'Take the hand mirror from the washstand and use it on the note.']],
    ['library', () => F().libOpen, ['The library door wants three symbols: body, soul, spirit.', 'The chart of principles names the three principles.', 'Salt (body) ⊖, Sulphur (soul) ▲, Mercury (spirit) ☿.']],
    ['globe', () => F().globe, ['The globe has a four-figure lock. The emperor is watching it.', 'Read the plate under the portrait.', 'He was crowned Emperor in 1576.']],
    ['cellar', () => F().trapOpen, ['The iron ring from the globe is a handle.', 'There is a threaded hole in the laboratory floor.', 'Use the iron ring on the trapdoor.']],
    ['furnace', () => F().furnaceOpen, ['The furnace door has five planetary signs and a five-letter lock.', 'The library books include a key from planet signs to letters.', '☽ ☿ ♀ ☉ ♂ = F L A M E. Enter FLAME.']],
    ['fire', () => E.has('fire') || F().in_fire, ['The furnace is cold. It needs fuel.', 'There is a coal bin in the cellar.', 'Take the charcoal and use it on the open furnace.']],
    ['scale', () => F().balanced, ['The lead weight is marked in drams and scruples; the dial counts grains.', 'The library has a table of apothecaries’ weights.', '20 grains = 1 scruple, 3 scruples = 1 dram: 2 drams 1 scruple = 140 grains.']],
    ['flasks', () => F().poured, ['Four coloured flasks, one basin. The order matters.', 'A book in the library describes the colours of the Great Work.', 'Black, white, yellow, red (nigredo, albedo, citrinitas, rubedo).']],
    ['roof', () => F().hatchOpen, ['The roof hatch has a crescent-moon keyhole.', 'A key was hidden with the earth seal in the scale.', 'Use the hatch key on the ladder.']],
    ['wheel', () => F().wheel, ['Set the wheel to the emperor’s horoscope. There are two horoscopes.', 'The master’s note: trust nothing written in green.', 'Brown-ink horoscope: Sun in Cancer, Moon in Sagittarius, Mars in Leo.']],
    ['chest', () => F().chestOpen, ['The chest has four sockets: earth, water, air, fire.', 'Each element came from a different puzzle: scale, flasks, wheel, furnace.', 'Use all four seals on the chest.']],
    ['name', () => F().won, ['The guards will want a name. Who wrote the poisoned recipe?', 'The recipe on the desk is in green ink. Who buys green ink?', 'The court ledger: green ink for Master Vellinus. Enter VELLINUS.']],
  ],
  intro: ['Prague Castle · 3 March 1610 · an hour before dawn', 'The Alchemist’s Attic',
    `<p>The emperor’s wine was poisoned at supper. By midnight your master, the alchemist Ondřej Kavka, had been dragged away – a recipe for the poison was found in his own hand.</p><p>You are his apprentice. At dawn the guards come back for you. Master Kavka hid his true work in a chest only the four elements can open – and somewhere in this attic is the proof of who really wrote that recipe.</p><p>Level 2: not everything here was written by your master.</p>`,
    'Candles gutter in the cold attic. Glass and brass everywhere. Look around.'],
  timesUp: ['Dawn.', 'Boots on the stairs. The captain of the guard has come for the apprentice.'],
  win: ['The captain of the guard reads it twice', 'Green ink, bought by the pot for one man only. At sunrise the guards march not to the attic but to the astrologer’s tower, and Master Vellinus is found burning papers. By noon Ondřej Kavka is free – and the emperor, who survived his bitter wine, asks to meet the apprentice who opened the chest of the four elements.'],
};

function openNote() {
  if (F().mirrored) return E.say('“Body, soul, spirit – then the library will open. Trust nothing written in green.”');
  E.modal(`<h2>A note nailed to the beam</h2><p class="paper" style="transform:scaleX(-1);font-size:1.3rem">Body, soul, spirit – then the library will open.<br>Trust nothing written in green.</p><p class="small">Master Kavka always wrote his private notes backwards.</p>`);
}
function openPrinciples() {
  E.note('principles', 'Chart of principles: ⊖ Salt – the body · ▲ Sulphur – the soul · ☿ Mercury – the spirit · ☉ Gold – the sun · ☽ Silver – the moon.');
  E.modal(`<h2>The three principles</h2><div class="paper"><table style="width:100%;font-size:1.2rem"><tr><td>⊖</td><td>Salt</td><td>the body</td></tr><tr><td>▲</td><td>Sulphur</td><td>the soul</td></tr><tr><td>☿</td><td>Mercury</td><td>the spirit</td></tr><tr><td>☉</td><td>Gold</td><td>the sun</td></tr><tr><td>☽</td><td>Silver</td><td>the moon</td></tr></table></div>`);
}
function openLibDoor() {
  E.cycler('Library door', 'Three brass dials, each engraved with signs.', [0, 1, 2].map(i => ({ name: String(i + 1), opts: ['☉', '⊖', '☽', '▲', '☿'] })), v => { if (v.join('') !== '⊖▲☿') return false; F().libOpen = 1; E.say('Something clicks deep in the door. The library is open.'); return true; }, 'The dials spin back.', 'Turn the handle');
}
function openDesk() {
  E.note('recipe', 'On the desk: the “poison recipe” the guards say is the master’s – but it is written in GREEN ink, and the hand is too neat.');
  E.modal(`<h2>The writing desk</h2><p class="paper" style="color:#2f6a3a">Take of the white arsenick two scruples, grind with sugar of lead, and give in sweet wine…</p><p class="small">Green ink. Master Kavka only ever used brown oak-gall ink – the pot on the desk is brown, and dry.</p>`);
}
function openGlobe() {
  if (F().globe) return E.say('The globe stands open at the equator – empty.');
  E.numLock('The globe', 'A brass ring around the equator holds four number dials. Engraved on the meridian: <i>“The year he took the crown of the Empire.”</i>', 4, c => { if (c !== '1576') return false; F().globe = 1; E.give('ring'); E.say('The globe splits at the equator. Inside lies a heavy iron ring with a screw thread.'); return true; });
}
function openBooks() {
  E.note('books', 'Library books: a planet-sign alphabet (' + KEY.map(k => k.join(' = ')).join(', ') + '); apothecaries’ weights (20 grains = 1 scruple, 3 scruples = 1 dram, 8 drams = 1 ounce); “The Great Work passes through four colours: black (nigredo), white (albedo), yellow (citrinitas), red (rubedo).”');
  E.modal(`<h2>The master’s books</h2><h3>A secret alphabet</h3><p class="paper" style="font-size:1.2rem">${KEY.map(k => `${k[0]} = ${k[1]}`).join(' · ')}</p><h3>Apothecaries’ weights</h3><p class="paper">20 grains = 1 scruple · 3 scruples = 1 dram · 8 drams = 1 ounce</p><h3>On the Great Work</h3><p class="paper">The work passes through four colours, and no other order: first black (nigredo), then white (albedo), then yellow (citrinitas), at last red (rubedo).</p>`);
}
function openHoroscopes() {
  E.note('horoscopes', 'Two horoscopes of the emperor. Brown ink (the master’s hand): Sun in Cancer, Moon in Sagittarius, Mars in Leo. Green ink (unknown hand): Sun in Cancer, Moon in Pisces, Mars in Aries.');
  E.modal(`<h2>Two horoscopes of the emperor</h2><p class="paper" style="color:#5a3a20">Sun in ♋ Cancer · Moon in ♐ Sagittarius · Mars in ♌ Leo<br><span class="small">– brown ink, the master’s hand</span></p><p class="paper" style="color:#2f6a3a">Sun in ♋ Cancer · Moon in ♓ Pisces · Mars in ♈ Aries<br><span class="small">– green ink, unsigned</span></p>`);
}
function openLedger() {
  E.note('ledger', 'Court ledger of purchases: “Brown oak-gall ink, 2 pots – Master Kavka. Green verdigris ink, 3 pots – Master Vellinus, astrologer. Red ink, 1 pot – Brother Ambrož, physician.”');
  E.modal(`<h2>Ledger of the imperial stores</h2><p class="paper">Brown oak-gall ink, 2 pots – Master Kavka, alchemist.<br>Green verdigris ink, 3 pots – Master Vellinus, astrologer.<br>Red ink, 1 pot – Brother Ambrož, physician.<br>Candles, 40 – the kitchens.</p>`);
}
function openFurnace() {
  if (F().fired) return E.say('The athanor glows steadily.');
  if (F().furnaceOpen) return E.say('The fire door stands open over a cold grate. It needs fuel.');
  E.wordLock('Furnace door', 'Five letter wheels under the five signs carved above the door: ☽ ☿ ♀ ☉ ♂.', 5, w => { if (w !== 'FLAME') return false; F().furnaceOpen = 1; E.say('FLAME. The iron fire door swings open on a cold grate.'); return true; });
}
function openScale() {
  if (F().balanced) return E.say('The scale hangs level. The drawer beneath it is empty.');
  E.numLock('Apothecary’s scale', 'A lead weight sits in the left pan, stamped <b>“2 drams, 1 scruple”</b>. The right pan is worked by a dial counting <b>grains</b>.', 3, c => { if (c !== '140') return false; F().balanced = 1; E.give('earth'); E.give('hatchKey'); E.say('The pans settle level and a drawer springs open: a clay earth seal and a small key stamped with a crescent moon.'); return true; }, 'The pans swing and settle crooked.');
}
function openFlasks() {
  if (F().poured) return E.say('The basin holds a clear red liquid. The water seal lies dry beside it.');
  E.orderer('Four flasks', 'One basin, four flasks of coloured tincture. Pour them in.', ['Black', 'White', 'Yellow', 'Red'], o => { if (o.join() !== 'Black,White,Yellow,Red') return false; F().poured = 1; E.give('water'); E.say('Black, white, yellow, red – the liquid clears to a deep ruby, and through it you see a blue glass seal at the bottom of the basin.'); return true; }, 'The mixture turns to brown sludge. You rinse the basin and start again.');
}
function openWheel() {
  if (F().wheel) return E.say('The wheel stays set to the true horoscope.');
  E.cycler('Astrological wheel', 'Three rings: the Sun, the Moon and Mars.', [{ name: '☉ Sun', opts: SIGNS }, { name: '☽ Moon', opts: SIGNS }, { name: '♂ Mars', opts: SIGNS }], v => {
    if (v[1] === '♓ Pisces' && v[2] === '♈ Aries') { E.say('The rings lock for a moment – then spring back. That is not the emperor’s sky.'); return false; }
    if (v.join() !== '♋ Cancer,♐ Sagittarius,♌ Leo') return false; F().wheel = 1; E.give('air'); E.say('The rings click into line and the hub opens: a white alabaster air seal.'); return true;
  }, 'The rings will not lock.', 'Lock the rings');
}
function openChest() {
  if (!F().chestOpen) return E.say('A heavy chest with four square sockets marked earth, water, air and fire.');
  E.note('journal', 'In the chest: Master Kavka’s journal and a letter to the captain of the guard, unfinished: “The man who wrote that recipe is …”');
  E.modal(`<h2>Master Kavka’s chest</h2><p class="paper">My dear apprentice – if you are reading this, I have been taken. The recipe they found is not mine; I never write in green. Give the captain the name of the man who does, and he will believe you.</p><button class="btn" id="name">Write the name for the captain</button>`, m => {
    m.querySelector('#name').addEventListener('click', () => E.wordLock('Letter to the captain', 'Eight letters.', 8, w => { if (w !== 'VELLINUS') return false; E.win(); return true; }, 'The captain would laugh at that.'));
  });
}
});
