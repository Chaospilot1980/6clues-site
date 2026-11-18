/* Six Clues escape room #21 – The Candy Factory (level 1, family). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const sweet = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 16 }, (_, i) => `<rect x="${i * 100}" y="0" width="50" height="660" fill="${c2}"/>`).join('')}<rect y="660" width="1600" height="240" fill="#5a3a4a"/>`;
const COLOURS = ['Pink', 'Yellow', 'Green', 'Purple', 'Orange'];

return {
  start: 'floor', v: 1,
  items: {
    scoop: ['🥄', 'Sugar scoop', 'A big metal scoop.'],
    goggles: ['🥽', 'Safety goggles', 'Bright pink factory goggles.'],
    golden: ['🎫', 'Golden wrapper', 'A shiny golden sweet wrapper with numbers inside.'],
    lever: ['🕹️', 'Lever handle', 'A red handle that fits a machine.'],
    key: ['🗝️', 'Gate key', 'A key shaped like a lollipop.'],
  },
  rooms: {
    floor: {
      name: 'The factory floor',
      bg: () => sweet('#f0c0d0', '#f8d0e0'),
      spots: [
        { id: 'belt', x: 80, y: 420, w: 640, h: 220, art: () => `<rect x="100" y="500" width="600" height="60" fill="#888"/>${[0, 1, 2, 3, 4].map(i => `<circle cx="${160 + i * 120}" cy="480" r="24" fill="${['#f06090', '#f0d040', '#50c060', '#9060d0', '#f09030'][i]}"/>`).join('')}${L(400, 610, 'Sweet conveyor belt (stopped)')}`,
          act: () => E.say('The conveyor belt has stopped. Sweets in five colours sit in a row, waiting.') },
        { id: 'sign', x: 80, y: 100, w: 380, h: 240, art: () => `${E.paper(100, 120, 340, 180, 5)}${L(270, 330, 'Mixing rules')}`,
          act: () => { E.note('rules', 'Mixing rules on the wall: “The rainbow chew machine starts when you pour the syrups in this order: Yellow first, then Pink, then Purple. Never Green – it fizzes!”'); E.say('“Pour the syrups: Yellow first, then Pink, then Purple. Never Green – it fizzes!”'); } },
        { id: 'syrups', x: 780, y: 140, w: 420, h: 360, art: () => `${[0, 1, 2].map(i => `<rect x="${820 + i * 120}" y="200" width="80" height="220" rx="20" fill="#e8e8e8"/>`).join('')}${L(990, 470, F().mix ? 'Syrup tanks (running)' : 'Three syrup taps')}`, act: () => openSyrups() },
        { id: 'locker', x: 1260, y: 160, w: 280, h: 360, art: () => `<rect x="1280" y="180" width="240" height="300" fill="#a06090"/>${L(1400, 520, 'Staff locker')}`,
          act: () => { if (F().locker) return E.say('Just a spare apron.'); F().locker = 1; E.give('goggles'); E.give('scoop'); E.say('In the locker: pink safety goggles and a big sugar scoop.'); } },
        { id: 'toSugar', x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Sugar room'), act: () => E.go('sugar') },
        { id: 'toOffice', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit(F().gate ? 'Owner’s office →' : 'Office gate (locked)', 1240), act: () => F().gate ? E.go('office') : E.say('A candy-striped gate with a lollipop-shaped keyhole.'),
          use: { key: () => { F().gate = 1; E.take('key'); E.say('The lollipop key turns. The gate swings open.'); return true; } } },
      ],
    },
    sugar: {
      name: 'The sugar room',
      bg: () => sweet('#f8f0e0', '#f0e8d8'),
      spots: [
        { id: 'back', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Factory floor →', 1240), act: () => E.go('floor') },
        { id: 'mountain', x: 200, y: 260, w: 520, h: 380, art: () => `<path d="M220 640 L460 280 L700 640z" fill="#fff"/>${L(460, 660, 'Mountain of sugar')}`,
          act: () => F().dug ? E.say('A crater in the sugar.') : E.say('A huge mountain of sugar. Something red sticks out near the top – too deep to grab with your hands.'),
          use: { scoop: () => { F().dug = 1; E.give('lever'); E.say('You scoop and scoop… and pull out a red lever handle!'); return true; } } },
        { id: 'mixer', x: 820, y: 220, w: 420, h: 420, art: () => `<ellipse cx="1030" cy="520" rx="180" ry="80" fill="#c0c0c0"/><rect x="1010" y="240" width="40" height="280" fill="#888"/>${L(1030, 650, F().mixer ? 'Giant mixer (spinning)' : 'Giant mixer (no handle)')}`,
          act: () => F().mixer ? E.say('The mixer spins and spits out sweets. One of them is golden.') : E.say('A giant mixer. Its handle is missing – there’s an empty slot.'),
          use: { lever: () => { F().mixer = 1; E.take('lever'); E.give('golden'); E.note('golden', 'The golden wrapper says inside: “Lucky winner! Your code: 3 – 8 – 5.”'); E.say('The mixer whirs! Out pops one sweet in a golden wrapper. Inside: “Lucky winner! Your code: 3 – 8 – 5.”'); return true; } } },
        { id: 'sacks', x: 1280, y: 120, w: 280, h: 300, art: () => `<rect x="1300" y="180" width="220" height="220" fill="#d8c8a0"/>${L(1410, 440, 'Sugar sacks')}`,
          act: () => E.say('Sacks of sugar, stamped: “FIZZWHISTLE’S – SINCE 1952”.') },
      ],
    },
    office: {
      name: 'Mr Fizzwhistle’s office',
      bg: () => sweet('#c0a0e0', '#b090d0'),
      spots: [
        { id: 'back', x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Factory floor'), act: () => E.go('floor') },
        { id: 'portrait', x: 120, y: 120, w: 340, h: 360, art: () => `<rect x="140" y="140" width="300" height="300" fill="#5a3a5a" stroke="#c9a24a" stroke-width="10"/>${L(290, 480, 'Portrait of Mr Fizzwhistle')}`,
          act: () => E.say('Mr Fizzwhistle in a purple top hat, grinning. On the frame: “Every good secret comes out with a smile.”') },
        { id: 'safe', x: 560, y: 300, w: 400, h: 340, art: () => `<rect x="580" y="320" width="360" height="300" rx="30" fill="#f06090"/><circle cx="760" cy="470" r="60" fill="#fff"/>${L(760, 650, 'Gumball safe (3 numbers)')}`, act: () => openSafe() },
        { id: 'window', x: 1060, y: 100, w: 420, h: 360, art: () => `<rect x="1080" y="120" width="380" height="300" fill="#a0d0f0"/>${L(1270, 450, 'Window to the street')}`,
          act: () => E.say('Outside, a crowd of children is waiting at the factory gates for the Grand Opening. They can’t start without the recipe!') },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['locker', () => F().locker, ['Look around the factory floor.', 'The staff locker isn’t locked.', 'Open the staff locker.']],
    ['dig', () => F().dug, ['Something red is buried in the sugar mountain.', 'You have a big scoop.', 'Use the sugar scoop on the sugar mountain.']],
    ['mixer', () => F().mixer, ['The giant mixer has no handle.', 'You dug a red lever out of the sugar.', 'Use the lever handle on the mixer.']],
    ['mix', () => F().mix, ['The syrup taps start the rainbow machine.', 'The mixing rules on the wall.', 'Yellow, Pink, Purple.']],
    ['gate', () => F().gate, ['The office gate needs a lollipop key.', 'The rainbow machine made something.', 'Use the gate key on the office gate.']],
    ['safe', () => F().won, ['The gumball safe wants three numbers.', 'The golden wrapper.', '3 – 8 – 5.']],
  ],
  intro: ['Fizzwhistle’s Sweet Factory · opening day · 09:00', 'The Candy Factory',
    `<p>You won a golden ticket to visit Fizzwhistle’s Sweet Factory on its Grand Opening day! But old Mr Fizzwhistle has gone missing – and the secret recipe for his famous Rainbow Chews is locked in his office.</p><p>The gates open in one hour, and hundreds of children are waiting. Get the machines running and find the recipe!</p><p>Level 1: perfect for families and first-time players.</p>`,
    'It smells of strawberries and toffee. Look around.'],
  timesUp: ['The gates open!', 'The children are coming in… quick, finish the job!'],
  win: ['Rainbow Chews for everyone!', 'The safe pops open with a jingle: the secret recipe – and Mr Fizzwhistle himself, who climbs out laughing. “I was hiding to see if anyone could solve my factory!” He makes you Head Taster for life.'],
};

function openSyrups() {
  if (F().mix) return E.say('The syrups bubble. The rainbow machine is running.');
  E.cycler('Syrup taps', 'Three taps. Choose which syrup each one pours – first, second, third.', ['First', 'Second', 'Third'].map(n => ({ name: n, opts: COLOURS })), v => { if (v.join() !== 'Yellow,Pink,Purple') return false; F().mix = 1; E.give('key'); E.say('Glug, glug, glug – the rainbow machine starts! A lollipop-shaped key drops out of the chute.'); return true; }, 'FIZZ! Sticky foam everywhere. Wrong order.', 'Pour');
}
function openSafe() {
  E.numLock('Gumball safe', 'A giant pink gumball machine with three number wheels.', 3, c => { if (c !== '385') return false; E.win(); return true; }, 'A gumball rolls out. Wrong code.');
}
});
