/* Six Clues escape room #34 – The Miser's Christmas Eve (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const office = c => `<rect width="1600" height="900" fill="${c}"/>${Array.from({ length: 8 }, (_, i) => `<rect x="${i * 200}" y="0" width="8" height="640" fill="#000" opacity=".25"/>`).join('')}<rect y="640" width="1600" height="260" fill="#2a1c12"/><ellipse cx="800" cy="200" rx="420" ry="260" fill="url(#lamp)"/>`;
const SYM = ['Bell', 'Holly', 'Star', 'Candle'];

return {
  start: 'office', v: 1,
  items: {
    candle: ['🕯️', 'Candle stub', 'A short stub of tallow candle.'],
    matches: ['🔥', 'Box of matches', 'Three matches left.'],
    lit: ['🕯️', 'Lit candle', 'A small, brave flame.'],
    cellarKey: ['🗝️', 'Cellar key', 'A rusty key with a paper tag: “CELLAR”.'],
    frontKey: ['🔑', 'Street door key', 'The big brass key to the street door.'],
  },
  rooms: {
    office: {
      name: 'The counting house',
      bg: () => office('#3a3020'),
      spots: [
        { id: 'clocks', x: 480, y: 60, w: 640, h: 220, art: () => `${[0, 1, 2].map(i => `<circle cx="${600 + i * 200}" cy="150" r="70" fill="#e8dcc0" stroke="#5a4a3a" stroke-width="10"/>`).join('')}${L(800, 260, 'Three stopped clocks')}`,
          act: () => { E.note('clocks', 'Three stopped clocks with brass labels – left: FUTURE, stopped at 9; middle: PAST, stopped at 7; right: PRESENT, stopped at 1.'); E.say('Three clocks, all stopped. Left, labelled FUTURE: 9 o’clock. Middle, labelled PAST: 7 o’clock. Right, labelled PRESENT: 1 o’clock.'); } },
        { id: 'desk', x: 80, y: 360, w: 400, h: 280, art: () => `<rect x="100" y="440" width="360" height="160" fill="#5a3a20"/>${L(280, 640, 'Your clerk’s desk')}`,
          act: () => { if (F().candle) return E.say('Your desk: a cold inkwell and a sad heap of ledgers.'); F().candle = 1; E.give('candle'); E.say('Your own desk. In the drawer, a candle stub – Mr Grimble only allows one a week.'); } },
        { id: 'jar', x: 540, y: 380, w: 260, h: 260, art: () => `<rect x="580" y="440" width="180" height="180" rx="30" fill="#c8d8e8" opacity=".6"/>${L(670, 650, 'Coin jar')}`,
          act: () => { E.note('jar', 'Coin jar: five old coins, each scratched with a number and a letter – 3-N, 1-P, 5-Y, 2-E, 4-N.'); E.say('Mr Grimble’s coin jar. Five old coins, each scratched with a number and a letter: 3-N, 1-P, 5-Y, 2-E, 4-N.'); } },
        { id: 'street', x: 1240, y: 300, w: 320, h: 340, art: () => `<rect x="1280" y="320" width="240" height="320" fill="#4a2a1a" stroke="#c9a24a" stroke-width="6"/>${L(1400, 670, 'Street door (locked)')}`,
          act: () => E.say('The street door is locked, and Mr Grimble has the only key… or does he? Outside, carol singers are going from door to door.'),
          use: { frontKey: () => { if (!F().safe) return false; E.take('frontKey'); E.win(); return true; } } },
        { id: 'toStudy', x: 860, y: 340, w: 320, h: 300, art: () => `<rect x="900" y="360" width="240" height="280" fill="#3a2414" stroke="#c9a24a" stroke-width="6"/>${L(1020, 660, F().study ? 'Mr Grimble’s study' : 'Study door (3 numbers)')}`,
          act: () => F().study ? E.go('study') : openStudy() },
        { id: 'toCellar', x: 20, y: 740, w: 360, h: 130, art: () => E.exit(F().cellar ? '← Cellar stairs' : '← Cellar (locked)'),
          act: () => !F().cellar ? E.say('The cellar door is locked.') : !F().light ? E.say('The cellar stairs vanish into pitch darkness. You need a light.') : E.go('cellar'),
          use: { cellarKey: () => { F().cellar = 1; E.take('cellarKey'); E.say('The cellar door creaks open. Below: pitch darkness.'); return true; },
            candle: () => { E.say('A candle with no flame won’t help much.'); return true; },
            lit: () => { if (!F().cellar) return false; F().light = 1; E.say('You hold up the candle. Narrow stone steps lead down.'); return true; } } },
      ],
    },
    study: {
      name: 'Mr Grimble’s study',
      bg: () => office('#4a2a20'),
      spots: [
        { id: 'back', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Counting house →', 1240), act: () => E.go('office') },
        { id: 'mantel', x: 80, y: 260, w: 420, h: 380, art: () => `<rect x="100" y="280" width="380" height="40" fill="#6a5a4a"/><rect x="140" y="320" width="300" height="300" fill="#111"/>${L(290, 650, 'Cold fireplace')}`,
          act: () => { if (F().matches) return E.say('A cold grate. Mr Grimble never lights it – “coal costs money”.'); F().matches = 1; E.give('matches'); E.say('A cold fireplace – never lit. On the mantel: a box of matches, three left.'); } },
        { id: 'drawer', x: 560, y: 400, w: 440, h: 240, art: () => `<rect x="580" y="440" width="400" height="160" fill="#5a3a20" stroke="#c9a24a" stroke-width="6"/>${L(780, 630, F().drawer ? 'Desk drawer (open)' : 'Desk drawer (5 letters)')}`, act: () => openDrawer() },
        { id: 'safe', x: 1060, y: 280, w: 420, h: 360, art: () => `<rect x="1100" y="300" width="340" height="320" fill="#2a2a2a" stroke="#888" stroke-width="10"/>${[0, 1, 2].map(i => `<circle cx="${1180 + i * 90}" cy="460" r="30" fill="#c9a24a"/>`).join('')}${L(1270, 660, F().safe ? 'Safe (open)' : 'Safe – 3 symbol dials')}`, act: () => openSafe() },
        { id: 'motto', x: 560, y: 100, w: 420, h: 220, art: () => `${E.paper(580, 120, 380, 160, 2)}${L(770, 310, 'Framed motto')}`,
          act: () => { E.note('motto', 'Framed motto: “Look after the pennies and the pounds will look after themselves.” – S. Grimble'); E.say('“Look after the pennies and the pounds will look after themselves.” – S. Grimble'); } },
      ],
    },
    cellar: {
      name: 'The cellar',
      bg: () => `<rect width="1600" height="900" fill="#141010"/><circle cx="800" cy="420" r="420" fill="url(#lamp)"/><rect y="640" width="1600" height="260" fill="#0a0808"/>`,
      spots: [
        { id: 'back', x: 20, y: 740, w: 340, h: 130, art: () => E.exit('← Up the stairs'), act: () => E.go('office') },
        { id: 'box', x: 520, y: 380, w: 520, h: 260, art: () => `<rect x="560" y="440" width="440" height="180" fill="#5a3a20"/>${L(780, 650, 'Old box of letters')}`,
          act: () => { E.note('letter', 'Old letter: “Dear Silas, I painted holly, a bell and a star on your new safe so you’d never forget Christmas – the holly first, then the bell, then the star. Your loving sister, Fan.”'); E.say('A box of old letters. The top one: “Dear Silas, I painted holly, a bell and a star on your new safe so you’d never forget Christmas – the holly first, then the bell, then the star. Your loving sister, Fan.”'); } },
        { id: 'coal', x: 1120, y: 420, w: 360, h: 220, art: () => `<ellipse cx="1300" cy="580" rx="160" ry="60" fill="#222"/>${L(1300, 650, 'Coal heap')}`,
          act: () => E.say('A whole heap of coal – while the clerks freeze upstairs!') },
      ],
    },
  },
  combine: (a, b) => { if ([a, b].sort().join() === 'candle,matches') { E.take('candle'); E.take('matches'); E.give('lit'); F().lit = 1; E.say('Scratch – fizz – the candle stub catches.'); return true; } return false; },
  stages: [
    ['study', () => F().study, ['The study door has three number wheels. Look at its brass plate.', 'Past, present, future – and the three clocks have labels.', 'Past 7, present 1, future 9: 719.']],
    ['drawer', () => F().drawer, ['The desk drawer wants five letters.', 'The coin jar in the counting house – and the motto on the wall.', 'Coins in number order: P, E, N, N, Y – PENNY.']],
    ['cellar', () => F().cellar, ['You have the cellar key.', 'The cellar door is in the counting house.', 'Use the cellar key on the cellar door.']],
    ['lit', () => F().lit, ['The cellar is pitch dark.', 'Your desk had a candle; the study fireplace had matches.', 'Combine the candle with the matches.']],
    ['light', () => F().light, ['You have a lit candle.', 'Hold it up at the cellar door.', 'Use the lit candle on the cellar door.']],
    ['safe', () => F().safe, ['The safe has three symbol dials.', 'Someone painted these symbols on the safe. A letter in the cellar.', 'Holly, Bell, Star.']],
    ['won', () => F().won, ['You have the street door key and the wages.', 'Out you go!', 'Use the street door key on the street door.']],
  ],
  intro: ['London · 24 December 1843 · 23:00', 'The Miser’s Christmas Eve',
    `<p>You are the junior clerk at Grimble &amp; Co. Old Mr Grimble has gone home – and locked the clerks’ Christmas wages in his safe “until the New Year”, and you in the counting house with them.</p><p>Five families are waiting for that money for their Christmas dinner. Open the safe, find the street door key, and get out before the bells ring midnight.</p><p>Level 2: for players with a few escape rooms behind them.</p>`,
    'The fire is out, the ink is freezing, and the three clocks above the door have all stopped. Look around.'],
  timesUp: ['The bells ring midnight!', 'Christmas Day has begun… but the families are still waiting. Keep going!'],
  win: ['God bless us, every one!', 'You step out into the snow with the wages bag under your arm. Five front doors open, five kitchens fill with the smell of roast goose – and the next morning, Mr Grimble finds a letter from his sister on his desk, and for the first time in years, he smiles.'],
};

function openStudy() {
  E.numLock('Study door', 'Three number wheels. The brass plate reads: “PAST – PRESENT – FUTURE”.', 3, c => { if (c !== '719') return false; F().study = 1; E.say('The study door swings open. It’s even colder in there.'); return true; });
}
function openDrawer() {
  if (F().drawer) return E.say('The drawer is empty.');
  E.wordLock('Desk drawer', 'Five letter wheels. Scratched beside them: “My favourite word lives in the coin jar.”', 5, w => { if (w !== 'PENNY') return false; F().drawer = 1; E.give('cellarKey'); E.say('The drawer opens. Inside: a rusty key tagged “CELLAR”.'); return true; });
}
function openSafe() {
  if (F().safe) return E.say('The safe is empty now.');
  E.cycler('The safe', 'Three dials, each painted with little symbols.', ['1st dial', '2nd dial', '3rd dial'].map(n => ({ name: n, opts: SYM })), v => { if (v.join() !== 'Holly,Bell,Star') return false; F().safe = 1; E.give('frontKey'); E.say('Clunk. The safe door swings open: the bag of wages – every penny – and the brass key to the street door!'); return true; }, 'The dials won’t budge.', 'Turn the handle');
}
});
