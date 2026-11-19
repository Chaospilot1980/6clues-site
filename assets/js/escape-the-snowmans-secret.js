/* Six Clues escape room #23 – The Snowman's Secret (level 1, family). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const snow = c => `<rect width="1600" height="900" fill="${c}"/>${Array.from({ length: 40 }, (_, i) => `<circle cx="${(i * 389) % 1600}" cy="${(i * 173) % 640}" r="5" fill="#fff" opacity=".8"/>`).join('')}<rect y="640" width="1600" height="260" fill="#f0f4f8"/>`;
const STOPS = ['Hill', 'Mill', 'Pond', 'Church'];

return {
  start: 'square', v: 2,
  items: {
    carrot: ['🥕', 'Carrot', 'A fine orange carrot – perfect for a nose.'],
    shopKey: ['🗝️', 'Toy shop key', 'A little key with a jingle bell on the ring.'],
    lightKey: ['🔑', 'Lights key', 'The big golden key for the town’s Christmas lights.'],
  },
  rooms: {
    square: {
      name: 'The town square',
      bg: () => snow('#2a3a5a'),
      spots: [
        { id: 'snowman', photo: [205, 250, 300, 550], x: 100, y: 240, w: 360, h: 420, art: () => `<circle cx="280" cy="560" r="100" fill="#fff"/><circle cx="280" cy="400" r="70" fill="#fff"/><circle cx="280" cy="300" r="50" fill="#fff"/><rect x="240" y="230" width="80" height="40" fill="#111"/>${L(280, 680, 'Mayor’s snowman')}`,
          act: () => F().nose ? E.say('The snowman has a fine carrot nose now. He looks very pleased with himself.') : E.say('A big snowman in a black top hat – with no nose. A sign at his feet: “Give me back my nose, and I’ll give you my secret.”'),
          use: { carrot: () => { F().nose = 1; E.take('carrot'); E.give('shopKey'); E.say('You push the carrot in. The snowman’s hat tips forward… and a little key with a jingle bell falls into the snow!'); return true; } } },
        { id: 'notice', photo: [465, 245, 265, 330], x: 540, y: 120, w: 340, h: 260, art: () => `${E.paper(560, 140, 300, 200, 5)}${L(710, 380, 'Notice board')}`,
          act: () => { E.note('notice', 'Notice board: “Christmas lights switch-on – 6 o’clock tonight! The golden lights key is kept safe in the toy shop.”'); E.say('“Christmas lights switch-on – 6 o’clock tonight! The golden lights key is kept safe in the toy shop.”'); } },
        { id: 'map', photo: [885, 240, 300, 330], x: 920, y: 120, w: 300, h: 260, art: () => `${E.paper(940, 140, 260, 200, 3)}${L(1070, 380, 'Village map')}`,
          act: () => { E.note('map', 'Village map with the little railway: the train goes from the Station to the Hill, then the Pond, then the Mill – and home again.'); E.say('The little village railway: Station → Hill → Pond → Mill → home.'); } },
        { id: 'switch', photo: [1220, 320, 140, 375], x: 1260, y: 300, w: 300, h: 340, art: () => `<rect x="1280" y="320" width="260" height="280" fill="#5a3a20"/>${L(1410, 640, 'Lights switch box')}`,
          act: () => E.say('A wooden box with a big golden keyhole: “Christmas lights – switch on here.”'), use: { lightKey: () => { E.take('lightKey'); E.win(); return true; } } },
        { id: 'toBakery', photo: [0, 25, 245, 670], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Bakery'), act: () => E.go('bakery') },
        { id: 'toShop', photo: [1380, 200, 220, 545], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit(F().shop ? 'Toy shop →' : 'Toy shop (locked)', 1240), act: () => F().shop ? E.go('shop') : E.say('The toy shop door is locked. Through the window you can see a toy train.'),
          use: { shopKey: () => { F().shop = 1; E.take('shopKey'); E.say('Jingle! The toy shop door opens.'); return true; } } },
      ],
    },
    bakery: {
      name: 'The bakery',
      bg: () => `<rect width="1600" height="900" fill="#e8c890"/><rect y="640" width="1600" height="260" fill="#8a5a3a"/><ellipse cx="800" cy="0" rx="520" ry="300" fill="url(#lamp)"/>`,
      spots: [
        { id: 'back', photo: [1410, 65, 190, 750], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Town square →', 1240), act: () => E.go('square') },
        { id: 'board', photo: [20, 20, 480, 325], x: 100, y: 120, w: 380, h: 280, art: () => `<rect x="120" y="140" width="340" height="220" fill="#2a2a2a"/>${L(290, 400, 'Recipe chalkboard')}`,
          act: () => { E.note('recipe', 'Chalkboard: “Today’s carrot cake – 3 carrots, 2 eggs, 7 spoons of sugar. (Spare carrots locked in the cake case!)”'); E.say('“Carrot cake – 3 carrots, 2 eggs, 7 spoons of sugar. (Spare carrots locked in the cake case!)”'); } },
        { id: 'case', photo: [420, 420, 815, 380], x: 540, y: 380, w: 500, h: 260, art: () => `<rect x="560" y="420" width="460" height="200" fill="#c8e0e8" opacity=".7" stroke="#8a5a3a" stroke-width="8"/>${L(790, 660, F().case ? 'Cake case (open)' : 'Cake case (3 numbers)')}`, act: () => openCase() },
        { id: 'gingerbread', photo: [1020, 150, 315, 105], x: 1100, y: 160, w: 400, h: 300, art: () => `${[0, 1, 2, 3].map(i => `<circle cx="${1160 + i * 90}" cy="300" r="30" fill="#a0602a"/>`).join('')}${L(1300, 470, 'Gingerbread men')}`,
          act: () => E.say('A tray of gingerbread men with icing smiles. One has a bite missing. Not you!') },
      ],
    },
    shop: {
      name: 'The toy shop',
      bg: () => `<rect width="1600" height="900" fill="#5a2a2a"/>${Array.from({ length: 3 }, (_, i) => `<rect x="0" y="${180 + i * 160}" width="1600" height="14" fill="#3a1a1a"/>`).join('')}<rect y="640" width="1600" height="260" fill="#3a2414"/><ellipse cx="800" cy="0" rx="520" ry="300" fill="url(#lamp)"/>`,
      spots: [
        { id: 'back', photo: [0, 65, 200, 815], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Town square'), act: () => E.go('square') },
        { id: 'train', photo: [215, 450, 980, 350], x: 200, y: 380, w: 760, h: 260, art: () => `<ellipse cx="580" cy="520" rx="340" ry="90" fill="none" stroke="#888" stroke-width="12"/><rect x="420" y="480" width="80" height="50" fill="#c03030"/>${L(580, 650, F().train ? 'Toy railway (finished)' : 'Toy railway – a little train')}`, act: () => openTrain() },
        { id: 'shelf', photo: [1200, 40, 400, 655], x: 1040, y: 120, w: 440, h: 360, art: () => `${[0, 1, 2].map(i => `<rect x="${1080 + i * 130}" y="200" width="90" height="120" fill="#c9a24a"/>`).join('')}${L(1260, 480, 'Shelf of toys')}`,
          act: () => E.say('Wooden soldiers, a rocking horse and a jack-in-the-box. A note: “The lights key rides the little train – it’ll stop at the right station.”') },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['case', () => F().case, ['The cake case wants three numbers.', 'The recipe chalkboard.', '3 carrots, 2 eggs, 7 spoons: 327.']],
    ['nose', () => F().nose, ['The snowman wants his nose back.', 'You found a carrot in the cake case.', 'Use the carrot on the snowman.']],
    ['shop', () => F().shop, ['The snowman gave you a key.', 'It jingles – try the toy shop.', 'Use the toy shop key on the toy shop door.']],
    ['train', () => F().train, ['The toy train must stop at the stations in order.', 'The village map shows the route.', 'Hill, Pond, Mill.']],
    ['lights', () => F().won, ['You have the golden key.', 'The switch box in the town square.', 'Use the lights key on the switch box.']],
  ],
  intro: ['Little Frostwick · 24 December · 17:00', 'The Snowman’s Secret',
    `<p>Tonight is the Christmas lights switch-on in the village of Little Frostwick – but the golden lights key is missing, and the Mayor is stuck in the snow on the way home!</p><p>The whole village gathers at six o’clock. Follow the clues around the snowy square and switch on the lights in time.</p><p>Level 1: perfect for families and first-time players.</p>`,
    'Snow is falling softly on the square. A snowman is watching you. Look around.'],
  timesUp: ['Six o’clock!', 'The crowd is waiting in the dark… you can still switch on the lights!'],
  win: ['Let there be lights!', 'Click – thousands of little lights twinkle on all over Little Frostwick. The crowd cheers, the church bells ring, and the snowman winks at you with his brand new carrot nose.'],
};

function openCase() {
  if (F().case) return E.say('The cake case is open. Mmm, carrot cake.');
  E.numLock('Cake case', 'A glass cake case with three number wheels.', 3, c => { if (c !== '327') return false; F().case = 1; E.give('carrot'); E.say('The case opens: carrot cake – and a spare carrot!'); return true; });
}
function openTrain() {
  if (F().train) return E.say('The little train sits at the station, its wagon empty.');
  E.cycler('Toy railway', 'Three signal levers decide where the train stops – first, second, third.', ['1st stop', '2nd stop', '3rd stop'].map(n => ({ name: n, opts: STOPS })), v => { if (v.join() !== 'Hill,Pond,Mill') return false; F().train = 1; E.give('lightKey'); E.say('Choo-choo! The little train runs round – Hill, Pond, Mill – and stops at your feet. In its wagon: the golden lights key!'); return true; }, 'The train goes off the rails. Oops.', 'Go!');
}
});
