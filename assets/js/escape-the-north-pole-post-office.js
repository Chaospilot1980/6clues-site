/* Six Clues escape room #31 – The North Pole Post Office (level 1, family). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const wall = c => `<rect width="1600" height="900" fill="${c}"/>${Array.from({ length: 30 }, (_, i) => `<circle cx="${(i * 331) % 1600}" cy="${(i * 97) % 600}" r="4" fill="#fff" opacity=".35"/>`).join('')}<rect y="640" width="1600" height="260" fill="#4a3020"/><ellipse cx="800" cy="0" rx="520" ry="300" fill="url(#lamp)"/>`;
const ELVES = ['Holly', 'Pip', 'Jingle', 'Tinsel'];

return {
  start: 'sorting', v: 1,
  items: {
    letter: ['✉️', 'Lost letter', 'A crumpled letter with no stamp: “Dear Santa, all I want is for Grandpa to come home for Christmas. Love, Mia.”'],
    stamp: ['🔖', 'Golden stamp', 'A golden rubber stamp. It prints the word JOY.'],
    stamped: ['💌', 'Stamped letter', 'Mia’s letter with a shiny golden JOY stamp. Ready to fly!'],
  },
  rooms: {
    sorting: {
      name: 'The sorting room',
      bg: () => wall('#7a2a2a'),
      spots: [
        { id: 'chalk', x: 80, y: 100, w: 380, h: 280, art: () => `<rect x="100" y="120" width="340" height="220" fill="#2a2a2a" stroke="#8a5a3a" stroke-width="10"/>${L(270, 380, 'Postmaster’s chalkboard')}`,
          act: () => { E.note('chalk', 'Chalkboard: “Stamp room door code: count tonight’s mail sacks – red, then green, then blue.”'); E.say('“Stamp room door code: count tonight’s mail sacks – red, then green, then blue.”'); } },
        { id: 'sacks', x: 500, y: 380, w: 520, h: 260, art: () => `${[['#c03030', 4], ['#2a8a3a', 7], ['#3050b0', 2]].map(([c, n], k) => Array.from({ length: n }, (_, i) => `<ellipse cx="${560 + k * 170 + (i % 3) * 40}" cy="${600 - Math.floor(i / 3) * 50}" rx="30" ry="34" fill="${c}"/>`).join('')).join('')}${L(760, 650, 'Mail sacks')}`,
          act: () => { E.note('sacks', 'Mail sacks: 4 red, 7 green and 2 blue.'); E.say('Mountains of mail! You count 4 red sacks, 7 green sacks and 2 blue sacks.'); } },
        { id: 'basket', x: 1080, y: 420, w: 300, h: 220, art: () => `<rect x="1100" y="500" width="260" height="120" fill="#a07a3a"/>${L(1230, 650, '“Return to sender” basket')}`,
          act: () => { if (F().letter) return E.say('The basket is empty now.'); F().letter = 1; E.give('letter'); E.say('At the bottom of the basket: one crumpled letter with no stamp. “Dear Santa, all I want is for Grandpa to come home for Christmas. Love, Mia.” It will never reach the sleigh without a stamp!'); } },
        { id: 'belt', x: 1100, y: 100, w: 440, h: 280, art: () => `<rect x="1120" y="200" width="400" height="60" fill="#555"/>${[0, 1, 2, 3].map(i => `<circle cx="${1180 + i * 95}" cy="320" r="24" fill="${F().belt ? '#3a3' : '#c33'}"/>`).join('')}${L(1320, 380, F().belt ? 'Conveyor belt (running)' : 'Conveyor belt – 4 elf buttons')}`, act: () => openBelt() },
        { id: 'toStamp', x: 20, y: 740, w: 340, h: 130, art: () => E.exit(F().stampRoom ? '← Stamp room' : '← Stamp room (locked)'), act: () => F().stampRoom ? E.go('stamp') : openStampDoor() },
        { id: 'toDock', x: 1200, y: 740, w: 380, h: 130, art: () => E.exit(F().belt ? 'Loading dock →' : 'Loading dock (closed)', 1220), act: () => F().belt ? E.go('dock') : E.say('The loading dock gate is shut. A sign: “Opens when the conveyor belt is running.”') },
      ],
    },
    stamp: {
      name: 'The stamp room',
      bg: () => wall('#2a4a6a'),
      spots: [
        { id: 'back', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Sorting room →', 1240), act: () => E.go('sorting') },
        { id: 'poster', x: 80, y: 100, w: 340, h: 300, art: () => `${E.paper(100, 120, 300, 240, 6)}${L(250, 400, 'Poster')}`,
          act: () => { E.note('poster', 'Poster: “Every letter for Santa’s sleigh needs the golden stamp! The stamp drawer opens with the happiest Christmas word – look at the window.”'); E.say('“Every letter for Santa’s sleigh needs the golden stamp! The stamp drawer opens with the happiest Christmas word – look at the window.”'); } },
        { id: 'window', x: 500, y: 80, w: 420, h: 340, art: () => `<rect x="520" y="100" width="380" height="280" fill="#cfe4f4" stroke="#fff" stroke-width="10"/>${L(710, 420, 'Frosty window')}`,
          act: () => { E.note('window', 'Frosty window: three big letters drawn in the frost – J, O, Y.'); E.say('Someone has drawn in the frost with a finger: three big letters – J… O… Y.'); } },
        { id: 'drawer', x: 520, y: 460, w: 420, h: 180, art: () => `<rect x="540" y="480" width="380" height="120" fill="#8a5a3a" stroke="#c9a24a" stroke-width="6"/>${L(730, 630, F().stamp ? 'Stamp drawer (open)' : 'Stamp drawer (3 letters)')}`, act: () => openDrawer() },
        { id: 'rota', x: 1040, y: 120, w: 420, h: 300, art: () => `${E.paper(1060, 140, 380, 240, 5)}${L(1250, 420, 'Elf rota')}`,
          act: () => { E.note('rota', 'Elf rota: “Starting the conveyor belt tonight – first Pip, then Tinsel, then Holly, and last of all Jingle.”'); E.say('“Starting the conveyor belt tonight – first Pip, then Tinsel, then Holly, and last of all Jingle.”'); } },
      ],
    },
    dock: {
      name: 'The loading dock',
      bg: () => `<rect width="1600" height="900" fill="#1a2440"/>${Array.from({ length: 50 }, (_, i) => `<circle cx="${(i * 389) % 1600}" cy="${(i * 173) % 600}" r="${1 + i % 3}" fill="#fff"/>`).join('')}<rect y="640" width="1600" height="260" fill="#e8eef4"/>`,
      spots: [
        { id: 'back', x: 20, y: 740, w: 340, h: 130, art: () => E.exit('← Sorting room'), act: () => E.go('sorting') },
        { id: 'sleigh', x: 500, y: 300, w: 700, h: 340, art: () => `<path d="M560 560 Q600 640 700 640 H1120 Q1180 640 1160 560 Z" fill="#c03030"/><ellipse cx="900" cy="470" rx="140" ry="110" fill="#8a2020"/>${L(860, 680, 'Santa’s sleigh – the mailbag')}`,
          act: () => E.say('Santa’s sleigh, ready for take-off. The big red mailbag is open. A sign: “Only stamped letters, please!”'),
          use: { letter: () => { E.say('An elf shakes her head: “No stamp, no flight!”'); return true; }, stamped: () => { E.take('stamped'); E.win(); return true; } } },
        { id: 'reindeer', x: 1240, y: 300, w: 320, h: 340, art: () => `<ellipse cx="1400" cy="520" rx="110" ry="60" fill="#8a5a3a"/>${L(1400, 640, 'Reindeer')}`,
          act: () => E.say('The reindeer stamp their hooves. Midnight is very close!') },
      ],
    },
  },
  combine: (a, b) => { if ([a, b].sort().join() === 'letter,stamp') { E.take('letter'); E.give('stamped'); F().stamped = 1; E.say('Ka-chunk! A shiny golden JOY on the corner. Mia’s letter is ready to fly.'); return true; } return false; },
  stages: [
    ['letter', () => F().letter, ['Is anything lost in the sorting room?', 'Look in the “Return to sender” basket.', 'Take the letter from the basket.']],
    ['stampRoom', () => F().stampRoom, ['The stamp room door has three number wheels.', 'The chalkboard tells you what to count.', '4 red, 7 green, 2 blue: 472.']],
    ['stamp', () => F().stamp, ['The stamp drawer wants a word.', 'Look at the frosty window.', 'JOY.']],
    ['stamped', () => F().stamped, ['Mia’s letter has no stamp.', 'You have the golden stamp.', 'Combine the stamp with the letter.']],
    ['belt', () => F().belt, ['The loading dock opens when the conveyor belt runs.', 'The elves must press their buttons in the right order. Check the stamp room.', 'Pip, Tinsel, Holly, Jingle.']],
    ['sleigh', () => F().won, ['Santa’s sleigh is in the loading dock.', 'The mailbag only takes stamped letters.', 'Use the stamped letter on the sleigh.']],
  ],
  intro: ['North Pole Post Office · 24 December · 23:30', 'The North Pole Post Office',
    `<p>Every letter to Santa ends up here, in the busiest post office in the world. Tonight the last sleigh leaves at midnight – and the elves have just found out that one very important letter is missing!</p><p>Find the lost letter, get it stamped and put it on Santa’s sleigh before midnight.</p><p>Level 1: perfect for families and first-time players.</p>`,
    'Bells jingle, letters fly along the belt, and an elf runs past shouting “Thirty minutes!” Look around.'],
  timesUp: ['Midnight!', 'The reindeer are pawing the snow… there’s still time if you hurry!'],
  win: ['Special delivery!', 'Mia’s letter drops into the mailbag just as the clock strikes twelve. The reindeer leap into the stars – and somewhere far away, a grandpa packs his suitcase to come home for Christmas.'],
};

function openStampDoor() {
  E.numLock('Stamp room door', 'A green door with three number wheels.', 3, c => { if (c !== '472') return false; F().stampRoom = 1; E.say('Click! The stamp room door swings open.'); return true; });
}
function openDrawer() {
  if (F().stamp) return E.say('The drawer is empty now.');
  E.wordLock('Stamp drawer', 'A drawer with three letter wheels.', 3, w => { if (w !== 'JOY') return false; F().stamp = 1; E.give('stamp'); E.say('The drawer slides out. On a velvet cushion: the golden stamp!'); return true; });
}
function openBelt() {
  if (F().belt) return E.say('The belt rattles along happily. Letters whizz past.');
  E.orderer('Conveyor belt', 'Four buttons, each with an elf’s name. Press them in the right order.', ELVES, v => { if (v.join() !== 'Pip,Tinsel,Holly,Jingle') return false; F().belt = 1; E.say('Whirr! The belt starts rolling – and the loading dock gate creaks open.'); return true; }, 'Bzzt! The belt shudders and stops.');
}
});
