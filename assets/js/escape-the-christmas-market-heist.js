/* Six Clues escape room #33 – The Christmas Market Heist (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const night = () => `<rect width="1600" height="900" fill="#141c34"/>${Array.from({ length: 40 }, (_, i) => `<circle cx="${(i * 389) % 1600}" cy="${(i * 173) % 600}" r="4" fill="#fff" opacity=".7"/>`).join('')}<rect y="640" width="1600" height="260" fill="#e8eef4"/>${Array.from({ length: 12 }, (_, i) => `<circle cx="${70 + i * 135}" cy="70" r="12" fill="${['#ffcf7a', '#d33', '#3a3'][i % 3]}"/>`).join('')}`;
const HORSE = ['Red', 'Gold', 'White', 'Green'];

return {
  start: 'square', v: 1,
  items: {
    towerKey: ['🗝️', 'Tower key', 'A heavy iron key from the carousel cabinet. There is sawdust on it.'],
    star: ['⭐', 'The market star', 'The great golden star from the top of the market tree.'],
  },
  rooms: {
    square: {
      name: 'The market square',
      bg: night,
      spots: [
        { id: 'tree', x: 80, y: 100, w: 380, h: 540, art: () => `<path d="M270 ${F().won ? 130 : 160} L100 620 H440z" fill="#1e5a2e"/>${L(270, 650, 'The market tree')}`,
          act: () => { E.note('tree', 'The market tree: the golden star vanished between 18:00 and 18:30, says the night watchman. The lighting ceremony is at 20:00.'); E.say('The great market tree – with no star on top! The night watchman says it vanished between six and half past six. The lighting ceremony is at eight.'); },
          use: { star: () => { E.take('star'); E.win(); return true; } } },
        { id: 'watch', x: 520, y: 340, w: 300, h: 300, art: () => `<circle cx="670" cy="420" r="40" fill="#e8c0a0"/><rect x="620" y="460" width="100" height="160" fill="#2a3a6a"/>${L(670, 650, 'Night watchman’s notebook')}`,
          act: () => { E.note('watch', 'Statements, 18:00–18:30 – Greta (mulled wine): “I was at my stall serving all evening.” Otto (toymaker): “I was riding the carousel, testing my new music box.” Hans (organ grinder): “I played carols by the tree the whole time.”'); E.say('The watchman shows you his notebook. Three stallholders were near the tree. Greta: “I was at my stall serving all evening.” Otto: “I was riding the carousel, testing my new music box.” Hans: “I played carols by the tree the whole time.” One of them is lying.'); } },
        { id: 'flag', x: 880, y: 80, w: 300, h: 300, art: () => `<rect x="960" y="100" width="12" height="260" fill="#555"/>${['#fff', '#c33', '#d4a92a'].map((c, i) => `<rect x="972" y="${110 + i * 40}" width="160" height="40" fill="${c}"/>`).join('')}${L(1030, 390, 'Flag on the clock tower')}`,
          act: () => { E.note('flag', 'Flag on the clock tower, three stripes from top to bottom: white, red, gold.'); E.say('The town flag flies from the clock tower: three stripes – white at the top, red in the middle, gold at the bottom.'); } },
        { id: 'toTower', x: 880, y: 420, w: 300, h: 220, art: () => `<rect x="920" y="440" width="220" height="200" fill="#5a4a3a"/>${L(1030, 660, F().tower ? 'Clock tower (open)' : 'Clock tower door (locked)')}`,
          act: () => F().tower ? E.go('tower') : E.say('The clock tower door is locked tight. There is fresh sawdust on the step.'),
          use: { towerKey: () => { F().tower = 1; E.take('towerKey'); E.say('The key turns with a groan. The clock tower door opens.'); return true; } } },
        { id: 'toStall', x: 20, y: 740, w: 360, h: 130, art: () => E.exit('← Mulled-wine stall'), act: () => E.go('stall') },
        { id: 'toCarousel', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Carousel →', 1240), act: () => E.go('carousel') },
      ],
    },
    stall: {
      name: 'Greta’s mulled-wine stall',
      bg: () => `<rect width="1600" height="900" fill="#5a2a1a"/><path d="M0 0 H1600 V120 Q1400 180 1200 120 Q1000 180 800 120 Q600 180 400 120 Q200 180 0 120z" fill="#c33"/><rect y="560" width="1600" height="340" fill="#7a4a2a"/><ellipse cx="800" cy="200" rx="520" ry="300" fill="url(#lamp)"/>`,
      spots: [
        { id: 'back', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Market square →', 1240), act: () => E.go('square') },
        { id: 'prices', x: 80, y: 180, w: 420, h: 300, art: () => `<rect x="100" y="200" width="380" height="240" fill="#2a2a2a" stroke="#8a5a3a" stroke-width="10"/>${L(290, 480, 'Price board')}`,
          act: () => { E.note('prices', 'Price board: mulled wine 3 €, hot chocolate 2 €, apple punch 4 €.'); E.say('Mulled wine 3 €, hot chocolate 2 €, apple punch 4 €.'); } },
        { id: 'cashbox', x: 600, y: 380, w: 360, h: 180, art: () => `<rect x="620" y="420" width="320" height="120" fill="#6a6a7a" stroke="#333" stroke-width="6"/>${L(780, 580, F().cash ? 'Cash box (open)' : 'Cash box (3 numbers)')}`, act: () => openCash() },
        { id: 'photo', x: 1060, y: 160, w: 400, h: 320, art: () => `<rect x="1100" y="180" width="320" height="240" fill="#e8e0d0" stroke="#fff" stroke-width="12"/>${L(1260, 460, 'Snapshot on the wall')}`,
          act: () => { E.note('photo', 'Snapshot, printed with the time 18:15: Hans the organ grinder playing by the tree, a crowd singing around him.'); E.say('A snapshot a tourist pinned up, stamped 18:15: Hans the organ grinder playing by the tree, a crowd singing around him.'); } },
      ],
    },
    carousel: {
      name: 'The carousel',
      bg: () => `${night()}<ellipse cx="800" cy="600" rx="600" ry="80" fill="#8a2a2a"/><path d="M200 300 L800 140 L1400 300z" fill="#c9a24a"/>`,
      spots: [
        { id: 'back', x: 20, y: 740, w: 340, h: 130, art: () => E.exit('← Market square'), act: () => E.go('square') },
        { id: 'sign', x: 120, y: 340, w: 360, h: 220, art: () => `${E.paper(140, 360, 320, 160, 3)}${L(300, 560, 'Sign on the rope')}`,
          act: () => { E.note('sign', 'Carousel sign: “CLOSED for repairs 17:30–19:00 – nobody rides!”'); E.say('A sign hangs on a rope across the entrance: “CLOSED for repairs 17:30–19:00 – nobody rides!”'); } },
        { id: 'sheet', x: 600, y: 320, w: 360, h: 240, art: () => `${E.paper(620, 340, 320, 180, 5)}${L(780, 560, 'Sheet on the organ')}`,
          act: () => { E.note('sheet', 'Sheet on the carousel organ: “To restart: light the three horses in the colours of the town flag, from the top down.”'); E.say('“To restart: light the three horses in the colours of the town flag, from the top down.”'); } },
        { id: 'cabinet', x: 1080, y: 320, w: 380, h: 300, art: () => `<rect x="1120" y="340" width="300" height="240" fill="#3a5a8a" stroke="#c9a24a" stroke-width="8"/>${L(1270, 610, F().key ? 'Horse switches (done)' : 'Cabinet – 3 horse switches')}`, act: () => openCabinet() },
      ],
    },
    tower: {
      name: 'The clock tower',
      bg: () => `<rect width="1600" height="900" fill="#3a3028"/><circle cx="800" cy="200" r="160" fill="#e8dcc0" stroke="#5a4a3a" stroke-width="20"/><rect y="640" width="1600" height="260" fill="#2a2018"/><ellipse cx="800" cy="0" rx="520" ry="300" fill="url(#lamp)"/>`,
      spots: [
        { id: 'back', x: 20, y: 740, w: 340, h: 130, art: () => E.exit('← Market square'), act: () => E.go('square') },
        { id: 'sacks', x: 420, y: 380, w: 760, h: 260, art: () => `${['Greta', 'Hans', 'Otto'].map((n, i) => `<ellipse cx="${540 + i * 260}" cy="540" rx="100" ry="90" fill="#a08050"/>${L(540 + i * 260, 650, n)}`).join('')}`, act: () => openSacks() },
        { id: 'saw', x: 1240, y: 420, w: 300, h: 220, art: () => `<rect x="1260" y="560" width="260" height="20" fill="#8a6a3a"/>${L(1390, 640, 'Sawdust and a saw')}`,
          act: () => E.say('A little saw and a pile of fresh sawdust. Somebody has been making something – or taking something apart.') },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['cash', () => F().cash, ['Greta’s cash box has three number wheels.', 'The price board – and the label on the cash box.', 'Cheapest to dearest: 2, 3, 4 – 234.']],
    ['key', () => F().key, ['The carousel has three horse switches.', 'The organ sheet talks about the town flag. Look up at the clock tower.', 'White, Red, Gold.']],
    ['tower', () => F().tower, ['You have a key with sawdust on it.', 'Where else did you see sawdust?', 'Use the tower key on the clock tower door.']],
    ['star', () => F().star, ['One stallholder lied about where they were.', 'Greta’s till roll and Hans’s photo both check out. What about the carousel?', 'The carousel was closed – Otto lied. Open Otto’s sack.']],
    ['won', () => F().won, ['You have the star.', 'Where does a star belong?', 'Use the star on the market tree.']],
  ],
  intro: ['Christmas market · 24 December · 19:15', 'The Christmas Market Heist',
    `<p>The old Christmas market glows with lanterns, mulled wine and gingerbread – but someone has stolen the great golden star from the top of the market tree!</p><p>The lighting ceremony is at eight o’clock. Three stallholders were near the tree when the star vanished, and one of them is lying. Find out who, and get the star back on top.</p><p>Level 2: for players with a few escape rooms behind them.</p>`,
    'The crowd is starting to gather. The night watchman waves you over. Look around.'],
  timesUp: ['Eight o’clock!', 'The mayor is stalling with a long speech… you still have a moment!'],
  win: ['Star of the market!', 'The golden star goes back on top just as the mayor flicks the switch. Ten thousand lights blaze on, the brass band plays – and Otto the toymaker, red-faced, admits he only wanted to copy the star for his new music box.'],
};

function openCash() {
  if (F().cash) return E.say('The till roll is still in the cash box: sales every few minutes, all evening.');
  E.numLock('Cash box', 'Greta’s label: “My code is my three drinks, from cheapest to dearest.”', 3, c => { if (c !== '234') return false; F().cash = 1; E.note('till', 'Till roll from Greta’s cash box: sales at 18:02, 18:09, 18:15, 18:21 and 18:28 – all served by Greta.'); E.say('The cash box opens. The till roll shows sales at 18:02, 18:09, 18:15, 18:21 and 18:28 – all served by Greta herself.'); return true; });
}
function openCabinet() {
  if (F().key) return E.say('The horses glow and the music plays. The cabinet is empty.');
  E.cycler('Horse switches', 'Three switches for the three lead horses. Each can light up in a different colour.', ['1st horse', '2nd horse', '3rd horse'].map(n => ({ name: n, opts: HORSE })), v => { if (v.join() !== 'White,Red,Gold') return false; F().key = 1; E.give('towerKey'); E.say('The horses light up and the carousel jingles into life. A panel drops open: an iron key, covered in sawdust!'); return true; }, 'The lights flicker and go dark.', 'Switch on');
}
function openSacks() {
  if (F().star) return E.say('You already found the star.');
  E.cycler('Three sacks', 'Three sacks, each with a name tag. You only have time to search one before someone comes up the stairs.', [{ name: 'Search the sack of…', opts: ['Greta', 'Hans', 'Otto'] }], v => { if (v[0] !== 'Otto') return false; F().star = 1; E.give('star'); E.say('Under a pile of wood shavings in Otto’s sack: the great golden star!'); return true; }, 'Just cups and spare organ handles. Wrong sack!', 'Search');
}
});
