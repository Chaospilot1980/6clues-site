/* Six Clues escape room #29 – The Castle Under Siege (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const keep = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 12 }, (_, r) => Array.from({ length: 9 }, (_, c) => `<rect x="${c * 180 + (r % 2 ? 90 : 0)}" y="${r * 55}" width="176" height="51" fill="${c2}"/>`).join('')).join('')}<rect y="660" width="1600" height="240" fill="#2a241e"/><ellipse cx="800" cy="0" rx="520" ry="300" fill="url(#lamp)"/>`;
const TINCT = ['Gules', 'Azure', 'Or', 'Vert', 'Sable'];
const KNIGHTS = ['Sir Roland', 'Sir Hugh', 'Sir Edmund', 'Sir Walter'];

return {
  start: 'hall', v: 2,
  items: {
    flint: ['🪨', 'Flint and steel', 'For striking sparks.'],
    chapelKey: ['🗝️', 'Chapel key', 'A small key with a cross on it.'],
    towerKey: ['🗝️', 'Tower key', 'A huge iron key for the beacon tower.'],
    oil: ['🛢️', 'Pitch pot', 'A pot of sticky black pitch – it burns fiercely.'],
    seal: ['🔴', 'Wax seal', 'A broken wax seal showing a tower.'],
  },
  rooms: {
    hall: {
      name: 'The great hall',
      bg: () => keep('#3a3028', '#443a30'),
      spots: [
        { id: 'hearth', photo: [240, 190, 330, 400], x: 80, y: 300, w: 400, h: 340, art: () => `<rect x="100" y="320" width="360" height="300" fill="#2a1e14"/>${L(280, 650, 'Great hearth')}`,
          act: () => { if (F().flint) return E.say('Glowing embers.'); F().flint = 1; E.give('flint'); E.say('On the hearth stones: a flint and steel for lighting fires.'); } },
        { id: 'letter', photo: [800, 500, 140, 60], x: 560, y: 380, w: 380, h: 260, art: () => `<rect x="580" y="460" width="340" height="30" fill="#5a3a20"/>${E.paper(660, 410, 180, 60, 2)}${L(750, 640, 'Letter on the high table')}`,
          act: () => { if (!F().seal) { F().seal = 1; E.give('seal'); } E.note('letter', 'A letter dropped by the high table, to the enemy captain: “At midnight, when I take the gate watch, I will lift the bar. Have your men ready.” Sealed with a broken wax seal: a tower.'); E.say('A traitor’s letter: “At midnight, when I take the gate watch, I will lift the bar.” The broken seal shows a tower. You keep it.'); } },
        { id: 'banners', photo: [970, 40, 440, 280], x: 1000, y: 60, w: 520, h: 300, art: () => `${[0, 1, 2, 3].map(i => `<rect x="${1030 + i * 120}" y="80" width="90" height="220" fill="${['#a02a2a', '#2a4aa0', '#c9a24a', '#2a7a3a'][i]}"/>`).join('')}${L(1260, 340, 'Knights’ banners')}`,
          act: () => { E.note('banners', 'Knights’ banners: Sir Roland – a lion. Sir Hugh – a tower. Sir Edmund – a lily. Sir Walter – a stag.'); E.say('The knights’ banners: Sir Roland a lion, Sir Hugh a tower, Sir Edmund a lily, Sir Walter a stag.'); } },
        { id: 'rota', photo: [1450, 370, 150, 190], x: 1040, y: 400, w: 380, h: 240, art: () => `${E.paper(1060, 420, 340, 180, 5)}${L(1230, 640, 'Watch rota')}`,
          act: () => { E.note('rota', 'Watch rota tonight: Gate – Sir Walter until midnight, then Sir Hugh. Walls – Sir Roland. Keep – Sir Edmund.'); E.say('Tonight’s watch: the gate – Sir Walter until midnight, then Sir Hugh.'); } },
        { id: 'toArmoury', photo: [0, 270, 200, 350], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Armoury'), act: () => E.go('armoury') },
        { id: 'toChapel', photo: [870, 630, 280, 220], x: 620, y: 740, w: 340, h: 130, art: () => E.exit(F().chapel ? 'Chapel ↓' : 'Chapel (locked)', 640), act: () => F().chapel ? E.go('chapel') : E.say('The chapel door is locked.'),
          use: { chapelKey: () => { F().chapel = 1; E.take('chapelKey'); E.say('The chapel door opens. Candles flicker.'); return true; } } },
        { id: 'toTower', photo: [1300, 330, 170, 240], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit(F().tower ? 'Beacon tower ↑' : 'Beacon tower (locked)', 1240), act: () => F().tower ? E.go('tower') : E.say('The beacon tower door: oak and iron, locked.'),
          use: { towerKey: () => { F().tower = 1; E.take('towerKey'); E.say('The great key grinds round. Cold wind blows down the tower stair.'); return true; } } },
      ],
    },
    armoury: {
      name: 'The armoury',
      bg: () => keep('#2e2e2e', '#383838'),
      spots: [
        { id: 'back', photo: [1450, 160, 150, 420], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Great hall →', 1240), act: () => E.go('hall') },
        { id: 'book', photo: [20, 220, 370, 300], x: 100, y: 120, w: 360, h: 260, art: () => `${E.paper(120, 140, 320, 200, 6)}${L(280, 380, 'Book of heraldry')}`,
          act: () => { E.note('heraldry', 'Book of heraldry: “Gules is red. Azure is blue. Or is gold. Vert is green. Sable is black.” A marked page: “The armourer’s chest: our lord’s colours from top to bottom – Or, Azure, Gules.”'); E.say('Heraldry: Gules = red, Azure = blue, Or = gold, Vert = green, Sable = black. A marked page: “the armourer’s chest: our lord’s colours, top to bottom – Or, Azure, Gules.”'); } },
        { id: 'chest', photo: [500, 500, 520, 330], x: 520, y: 380, w: 420, h: 260, art: () => `<rect x="540" y="420" width="380" height="200" fill="#5a3a20"/>${[0, 1, 2].map(i => `<rect x="${600 + i * 100}" y="460" width="60" height="80" fill="#888"/>`).join('')}${L(730, 650, F().chest ? 'Armourer’s chest (open)' : 'Armourer’s chest – three shield plates')}`, act: () => openChest() },
        { id: 'rack', photo: [970, 80, 330, 560], x: 1000, y: 100, w: 500, h: 400, art: () => `${[0, 1, 2, 3, 4].map(i => `<rect x="${1040 + i * 90}" y="120" width="12" height="340" fill="#aaa"/>`).join('')}${L(1250, 500, 'Weapon rack')}`,
          act: () => { if (F().oil) return E.say('Swords, spears and crossbows.'); F().oil = 1; E.give('oil'); E.say('Behind the spears: a pot of pitch for the beacon.'); } },
      ],
    },
    chapel: {
      name: 'The chapel',
      bg: () => keep('#2a2438', '#342e44'),
      spots: [
        { id: 'up', photo: [0, 410, 250, 490], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('↑ Great hall'), act: () => E.go('hall') },
        { id: 'window', photo: [830, 20, 300, 380], x: 560, y: 60, w: 480, h: 360, art: () => `<path d="M600 400 V160 Q800 40 1000 160 V400z" fill="#4a3a8a"/>${L(800, 440, 'Stained glass window')}`,
          act: () => E.say('A stained glass window: Saint George and the dragon. Under it: “He who keeps the tower key keeps the kingdom.”') },
        { id: 'tomb', photo: [180, 450, 560, 350], x: 160, y: 400, w: 480, h: 240, art: () => `<rect x="180" y="460" width="440" height="140" fill="#6a6a6a"/>${L(400, 640, 'Tomb of the first lord')}`, act: () => openTomb() },
        { id: 'plaque', photo: [1405, 265, 180, 215], x: 1100, y: 120, w: 360, h: 260, art: () => `<rect x="1120" y="140" width="320" height="200" fill="#c9a24a"/>${L(1280, 380, 'Brass plaque')}`,
          act: () => { E.note('plaque', 'Brass plaque: “Here lies Lord Aldric, who built this castle in the year 1312. Speak his name to the stone and it will answer.”'); E.say('“Here lies Lord Aldric, who built this castle in 1312. Speak his name to the stone and it will answer.”'); } },
      ],
    },
    tower: {
      name: 'The beacon tower',
      bg: () => `<rect width="1600" height="900" fill="#141a2a"/>${Array.from({ length: 50 }, (_, i) => `<circle cx="${(i * 331) % 1600}" cy="${(i * 97) % 400}" r="2" fill="#fff"/>`).join('')}<rect y="560" width="1600" height="340" fill="#3a3a38"/>${[0, 1, 2, 3, 4, 5, 6, 7].map(i => `<rect x="${i * 200}" y="500" width="120" height="60" fill="#3a3a38"/>`).join('')}`,
      spots: [
        { id: 'down', photo: [0, 570, 240, 330], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('↓ Great hall'), act: () => E.go('hall') },
        { id: 'beacon', photo: [530, 80, 450, 560], x: 600, y: 240, w: 400, h: 360, art: () => `<path d="M680 560 L800 300 L920 560z" fill="#5a3a20"/>${L(800, 600, 'Beacon')}`, act: () => openBeacon(),
          use: { oil: () => { F().pitch = 1; E.take('oil'); E.say('You pour the pitch over the beacon wood.'); return true; }, flint: () => { if (!F().pitch) return false; F().lit = 1; E.take('flint'); E.say('Sparks – then WHOOSH! The beacon roars into flame. On the far hill, an answering fire flickers: the king’s army has seen it!'); return true; } } },
        { id: 'camp', photo: [1150, 350, 450, 180], x: 1100, y: 300, w: 440, h: 200, art: () => L(1320, 440, 'Enemy campfires'),
          act: () => E.say('Hundreds of enemy campfires below the walls. Some men are already creeping towards the main gate.') },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['chest', () => F().chest, ['The armourer’s chest has three shield plates.', 'The book of heraldry turns colour names into colours – and has a marked page.', 'Top to bottom: Or, Azure, Gules.']],
    ['chapel', () => F().chapel, ['The chest had a small key with a cross.', 'The chapel.', 'Use the chapel key on the chapel door.']],
    ['tomb', () => F().tomb, ['The tomb answers to a name.', 'The brass plaque says who lies here.', 'ALDRIC.']],
    ['tower', () => F().tower, ['The tomb held a huge iron key.', 'The beacon tower.', 'Use the tower key on the tower door.']],
    ['lit', () => F().lit, ['The beacon needs fuel and a spark.', 'Pitch from the armoury, flint from the hearth.', 'Use the pitch pot, then the flint, on the beacon.']],
    ['traitor', () => F().won, ['Now name the traitor before midnight.', 'The seal on the letter, the banners and the watch rota.', 'The tower seal, gate watch at midnight: Sir Hugh.']],
  ],
  intro: ['Castle Ravenmoor · 1450 · 23:00', 'The Castle Under Siege',
    `<p>You are a squire at Castle Ravenmoor. An enemy army camps below the walls – and you have just found out that one of the four knights is a traitor, planning to open the gate at midnight.</p><p>Light the beacon on the tower to call the king’s army, and name the traitor before the clock strikes twelve.</p><p>Level 2: four knights, four banners – and only one boar.</p>`,
    'Smoky torches, stone walls and the murmur of an army outside. Look around.'],
  timesUp: ['Midnight.', 'The gate creaks… you can still finish, but off the leaderboard.'],
  win: ['The gate holds!', 'You race down from the tower crying “Sir Hugh!” – and the guards seize him with his hand on the gate bar. By dawn the king’s banners crest the hill, and the enemy army melts away into the mist.'],
};

function openChest() {
  if (F().chest) return E.say('The armourer’s chest is open.');
  E.cycler('Armourer’s chest', 'Three shield-shaped plates, top to bottom. Each can be turned to a colour.', ['Top', 'Middle', 'Bottom'].map(n => ({ name: n, opts: TINCT.map(t => ({ Gules: 'Red', Azure: 'Blue', Or: 'Gold', Vert: 'Green', Sable: 'Black' }[t])) })), v => { if (v.join() !== 'Gold,Blue,Red') return false; F().chest = 1; E.give('chapelKey'); E.say('The chest opens: mail shirts, gauntlets – and a small key with a cross.'); return true; }, 'The plates clank and reset.', 'Set');
}
function openTomb() {
  if (F().tomb) return E.say('The tomb’s little door is open and empty.');
  E.wordLock('Tomb of the first lord', 'Six letter stones along the tomb’s edge.', 6, w => { if (w !== 'ALDRIC') return false; F().tomb = 1; E.give('towerKey'); E.say('The stones sink in. A little door in the tomb opens: a huge iron key!'); return true; });
}
function openBeacon() {
  if (!F().lit) return E.say(F().pitch ? 'The beacon is soaked in pitch. Now a spark.' : 'A great pile of dry wood, ready to burn. It needs pitch to catch in this wind.');
  E.cycler('Name the traitor', 'The beacon blazes. Now run to the gate guards and name the traitor!', [{ name: 'Traitor', opts: KNIGHTS }], v => { if (v[0] !== 'Sir Hugh') return false; E.win(); return true; }, 'The guards seize the wrong man – and the real traitor slips away. Think again!', 'Accuse');
}
});
