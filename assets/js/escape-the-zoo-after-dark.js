/* Six Clues escape room #22 – The Zoo After Dark (level 1, family). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const night = c => `<rect width="1600" height="900" fill="${c}"/><circle cx="1400" cy="120" r="60" fill="#f0f0d0"/><rect y="640" width="1600" height="260" fill="#2a3a22"/>`;
const CHAM = ['Red', 'Blue', 'Yellow', 'Green'];

return {
  start: 'hut', v: 1,
  items: {
    torch: ['🔦', 'Torch', 'A big zookeeper’s torch.'],
    fish: ['🐟', 'Bucket of fish', 'A cold bucket of fish. Smelly!'],
    reptileKey: ['🗝️', 'Reptile house key', 'A key with a little lizard on the tag.'],
    keycard: ['💳', 'Gate keycard', 'The zookeeper’s keycard for the main gate.'],
  },
  rooms: {
    hut: {
      name: 'The zookeeper’s hut',
      bg: () => `<rect width="1600" height="900" fill="#6a5a3a"/>${Array.from({ length: 16 }, (_, i) => `<rect x="${i * 100}" y="0" width="4" height="660" fill="#5a4a2a"/>`).join('')}<rect y="660" width="1600" height="240" fill="#4a3a22"/><ellipse cx="800" cy="0" rx="500" ry="300" fill="url(#lamp)"/>`,
      spots: [
        { id: 'chart', x: 80, y: 100, w: 400, h: 300, art: () => `${E.paper(100, 120, 360, 240, 6)}${L(280, 400, 'Feeding chart')}`,
          act: () => { E.note('chart', 'Feeding chart: “Penguins – 6 fish. Seals – 9 fish. Otters – 4 fish. Freezer code = penguins, seals, otters.”'); E.say('Feeding chart: penguins 6 fish, seals 9 fish, otters 4 fish. “Freezer code = penguins, seals, otters.”'); } },
        { id: 'drawer', x: 520, y: 460, w: 320, h: 180, art: () => `<rect x="540" y="480" width="280" height="140" fill="#5a3a20"/>${L(680, 660, 'Desk drawer')}`,
          act: () => { if (F().torch) return E.say('Pencils and a squashed banana.'); F().torch = 1; E.give('torch'); E.say('In the drawer: a big zookeeper’s torch.'); } },
        { id: 'freezer', x: 900, y: 300, w: 320, h: 340, art: () => `<rect x="920" y="320" width="280" height="300" fill="#d8e8f0"/>${L(1060, 650, F().freezer ? 'Freezer (open)' : 'Fish freezer (3 numbers)')}`, act: () => openFreezer() },
        { id: 'poster', x: 1260, y: 100, w: 300, h: 320, art: () => `<rect x="1280" y="120" width="260" height="260" fill="#e0a040"/>${L(1410, 420, 'Lion poster')}`,
          act: () => { E.note('poster', 'Lion poster: “Leo says: ROAR loudly, sleep softly! – the zoo motto.”'); E.say('A big lion poster: “Leo says: ROAR loudly, sleep softly!”'); } },
        { id: 'toPool', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Penguin pool →', 1240), act: () => E.go('pool') },
      ],
    },
    pool: {
      name: 'The penguin pool',
      bg: () => `${night('#1a2a3a')}<ellipse cx="600" cy="560" rx="420" ry="110" fill="#3a6a9a"/>`,
      spots: [
        { id: 'back', x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Keeper’s hut'), act: () => E.go('hut') },
        { id: 'penguins', x: 220, y: 360, w: 760, h: 260, art: () => `${[0, 1, 2, 3, 4].map(i => `<ellipse cx="${320 + i * 130}" cy="500" rx="30" ry="50" fill="#111"/>`).join('')}${L(600, 640, F().fed ? 'Happy penguins' : 'Grumpy penguins')}`,
          act: () => F().fed ? E.say('The penguins are munching happily.') : E.say('The penguins are huddled on something shiny and squawking crossly. They look hungry.'),
          use: { fish: () => { F().fed = 1; E.take('fish'); E.give('reptileKey'); E.say('The penguins dive for the fish – and leave behind the shiny thing they were sitting on: a key with a lizard tag!'); return true; } } },
        { id: 'gate', x: 1120, y: 200, w: 420, h: 440, art: () => `${Array.from({ length: 8 }, (_, i) => `<rect x="${1140 + i * 50}" y="220" width="12" height="400" fill="#555"/>`).join('')}${L(1330, 660, 'Main gate')}`, act: () => openGate(),
          use: { keycard: () => { F().card = 1; E.take('keycard'); E.say('Beep! The gate light turns orange: “ENTER WORD”.'); return true; } } },
        { id: 'toReptile', x: 620, y: 740, w: 360, h: 130, art: () => E.exit(F().reptile ? 'Reptile house ↓' : 'Reptile house (locked)', 640), act: () => F().reptile ? E.go('reptile') : E.say('The reptile house door is locked. A lizard is painted on it.'),
          use: { reptileKey: () => { F().reptile = 1; E.take('reptileKey'); E.say('The lizard key fits. It’s pitch black inside.'); return true; } } },
      ],
    },
    reptile: {
      name: 'The reptile house',
      bg: () => F().light ? `<rect width="1600" height="900" fill="#1e3a22"/><rect y="640" width="1600" height="260" fill="#2a2a1a"/>` : `<rect width="1600" height="900" fill="#050805"/>`,
      spots: [
        { id: 'up', x: 20, y: 740, w: 300, h: 130, art: () => E.exit('↑ Penguin pool'), act: () => E.go('pool') },
        { id: 'dark', x: 300, y: 100, w: 1000, h: 540, hide: () => F().light, art: () => L(800, 380, 'Pitch black. Something hisses…'),
          act: () => E.say('It’s too dark to see. Something hisses softly.'), use: { torch: () => { F().light = 1; E.say('Click! The torch shows glass tanks: a snake, a crocodile and a chameleon.'); return true; } } },
        { id: 'snake', x: 100, y: 200, w: 380, h: 300, hide: () => !F().light, art: () => `<rect x="120" y="220" width="340" height="240" fill="#2a4a2a" stroke="#888" stroke-width="6"/>${L(290, 500, 'Snake tank')}`,
          act: () => E.say('A long python, fast asleep. A sign: “Monty – 4 metres long. Please don’t tap the glass.”') },
        { id: 'croc', x: 540, y: 380, w: 460, h: 240, hide: () => !F().light, art: () => `<rect x="560" y="420" width="420" height="180" fill="#2a4a3a"/>${L(770, 640, 'Crocodile pond')}`,
          act: () => E.say('A crocodile opens one eye and closes it again. You decide not to go any closer.') },
        { id: 'cham', x: 1060, y: 160, w: 440, h: 420, hide: () => !F().light, art: () => `<rect x="1080" y="180" width="400" height="340" fill="#3a5a2a" stroke="#888" stroke-width="6"/>${L(1280, 560, F().cham ? 'Chameleon tank (open)' : 'Chameleon tank')}`, act: () => openCham() },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['freezer', () => F().freezer, ['The fish freezer wants three numbers.', 'The feeding chart says which numbers.', 'Penguins 6, seals 9, otters 4: 694.']],
    ['fed', () => F().fed, ['The penguins are sitting on something shiny.', 'They’re hungry.', 'Use the bucket of fish on the penguins.']],
    ['reptile', () => F().reptile, ['The penguins gave you a key.', 'It has a lizard on it.', 'Use the reptile house key on the reptile house door.']],
    ['light', () => F().light, ['The reptile house is dark.', 'There was a torch in the keeper’s desk.', 'Use the torch on the darkness.']],
    ['cham', () => F().cham, ['Watch the chameleon.', 'It changes colour in an order. Copy it on the tank buttons.', 'Red, Blue, Yellow.']],
    ['gate', () => F().won, ['The main gate needs the keycard and a word.', 'The zoo motto on the lion poster.', 'ROAR.']],
  ],
  intro: ['City Zoo · after closing · 19:00', 'The Zoo After Dark',
    `<p>You stayed a little too long watching the penguins – and now the City Zoo is closed and the main gate is locked!</p><p>The night keeper finishes his round in one hour, and then the alarm goes on for the whole night. Find the keeper’s keycard and get out of the main gate before then.</p><p>Level 1: perfect for families and first-time players.</p>`,
    'The zoo is dark and quiet. Something somewhere is snoring. Look around.'],
  timesUp: ['The alarm is on!', 'But you can still finish – keep going!'],
  win: ['Out of the zoo!', 'The gate slides open and you step out under the street lamps. Behind you, a lion yawns a sleepy “roar”. Good night, zoo!'],
};

function openFreezer() {
  if (F().freezer) return E.say('The freezer is empty now.');
  E.numLock('Fish freezer', 'A big freezer with three number wheels. A sticker of a fish.', 3, c => { if (c !== '694') return false; F().freezer = 1; E.give('fish'); E.say('Brrr! Inside: a bucket of fish.'); return true; });
}
function openCham() {
  if (F().cham) return E.say('The tank’s little hatch is open and empty.');
  E.note('cham', 'The chameleon changes colour: first RED, then BLUE, then YELLOW – and then back to green to rest. Under the tank: three colour buttons.');
  E.cycler('Chameleon tank', 'The chameleon flashes RED… then BLUE… then YELLOW… then rests. Three colour buttons under the tank.', ['1st', '2nd', '3rd'].map(n => ({ name: n, opts: CHAM })), v => { if (v.join() !== 'Red,Blue,Yellow') return false; F().cham = 1; E.give('keycard'); E.say('A little hatch opens under the tank: the zookeeper’s gate keycard!'); return true; }, 'The chameleon turns grumpy grey.', 'Press');
}
function openGate() {
  if (!F().card) return E.say('The main gate is locked. A card reader blinks red.');
  E.wordLock('Main gate', 'The gate screen: “ENTER THE ZOO MOTTO WORD”. Four letters.', 4, w => { if (w !== 'ROAR') return false; E.win(); return true; }, 'BZZT. Wrong word.');
}
});
