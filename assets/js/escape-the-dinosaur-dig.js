/* Six Clues escape room #15 – The Dinosaur Dig (level 1, family). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const SIZES = ['Small', 'Medium', 'Large'];

return {
  start: 'camp', v: 2,
  items: {
    brush: ['🖌️', 'Dig brush', 'A soft brush for sweeping sand off fossils.'],
    radioPart: ['📻', 'Radio battery', 'A heavy battery for the camp radio.'],
    tooth: ['🦷', 'Fossil tooth', 'A huge pointed fossil tooth, as long as your hand.'],
    egg: ['🥚', 'Fossil egg', 'A round stone egg – a real dinosaur egg!'],
    bone: ['🦴', 'Claw bone', 'A curved fossil claw.'],
    jeepKey: ['🔑', 'Jeep key', 'A dusty key on a dinosaur key ring.'],
  },
  rooms: {
    camp: {
      name: 'The dig camp',
      bg: () => `<rect width="1600" height="900" fill="#e8b878"/><rect y="560" width="1600" height="340" fill="#c88a4a"/><circle cx="1400" cy="140" r="70" fill="#fff0a0"/>`,
      spots: [
        { id: 'tent', photo: [0, 75, 575, 445], x: 80, y: 260, w: 440, h: 360, art: () => `<path d="M100 600 L300 300 L500 600z" fill="#5a7a4a"/>${L(300, 640, 'Professor’s tent')}`, act: () => E.go('tent') },
        { id: 'radio', photo: [545, 270, 290, 250], x: 600, y: 380, w: 300, h: 220, art: () => `<rect x="620" y="420" width="260" height="140" fill="#4a4a3a"/>${L(750, 600, F().radio ? 'Camp radio (working)' : 'Camp radio (dead)')}`,
          act: () => { if (!F().radio) return E.say('The camp radio is dead. The battery slot is empty.'); E.note('radio', 'Radio: “Dig team, this is base. Storm coming in one hour! Drive out the north track. The jeep key is in the professor’s safe – her code is the year the museum opened.”'); E.say('“Storm in one hour! Drive out the north track. The jeep key is in the professor’s safe – her code is the year the museum opened.”'); },
          use: { radioPart: () => { F().radio = 1; E.take('radioPart'); E.say('The battery clicks in. The radio crackles to life!'); return true; } } },
        { id: 'jeep', photo: [1030, 200, 570, 360], x: 1000, y: 380, w: 520, h: 260, art: () => `<rect x="1040" y="460" width="420" height="140" rx="20" fill="#5a6a3a"/><circle cx="1120" cy="610" r="40" fill="#222"/><circle cx="1380" cy="610" r="40" fill="#222"/>${L(1250, 660, 'Old jeep')}`,
          act: () => E.say('The old jeep. Plenty of fuel – but no key!'), use: { jeepKey: () => { E.take('jeepKey'); E.win(); return true; } } },
        { id: 'sign', photo: [830, 40, 250, 150], x: 900, y: 120, w: 320, h: 200, art: () => `<rect x="920" y="140" width="280" height="140" fill="#8a5a2a"/>${L(1060, 320, 'Camp sign')}`,
          act: () => { E.note('sign', 'Camp sign: “Dino Dig – run by the Riverside Museum, open since 1987. Diggers, please brush gently!”'); E.say('“Dino Dig – run by the Riverside Museum, open since 1987. Diggers, please brush gently!”'); } },
        { id: 'toPit', photo: [0, 560, 880, 340], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('↓ Dig pit'), act: () => E.go('pit') },
      ],
    },
    tent: {
      name: 'The professor’s tent',
      bg: () => `<rect width="1600" height="900" fill="#4a5a3a"/><path d="M0 0 L800 -60 L1600 0 V660 H0z" fill="#5a6a4a"/><rect y="660" width="1600" height="240" fill="#8a6a3a"/>`,
      spots: [
        { id: 'back', photo: [1405, 0, 195, 900], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Camp →', 1240), act: () => E.go('camp') },
        { id: 'poster', photo: [25, 20, 335, 435], x: 100, y: 120, w: 380, h: 320, art: () => `${E.paper(120, 140, 340, 260, 3)}${L(290, 440, 'Dinosaur poster')}`,
          act: () => { E.note('poster', 'Poster: “Our dinosaurs from small to large: Stegosaurus (small claw), Triceratops (egg), T. rex (giant tooth).” Someone has written: “Display shelf – put the fossils from small to large!”'); E.say('A poster of the dig’s dinosaurs – Stegosaurus, Triceratops, T. rex – and a scribble: “Display shelf: fossils from small to large!”'); } },
        { id: 'display', photo: [420, 300, 500, 160], x: 540, y: 300, w: 480, h: 300, art: () => `<rect x="560" y="440" width="440" height="20" fill="#5a3a20"/>${[0, 1, 2].map(i => `<rect x="${600 + i * 140}" y="360" width="80" height="80" fill="none" stroke="#c9a24a" stroke-width="4"/>`).join('')}${L(780, 620, F().display ? 'Display shelf (complete)' : 'Display shelf – three empty spaces')}`, act: () => openDisplay(),
          use: { tooth: () => place('tooth'), egg: () => place('egg'), bone: () => place('bone') } },
        { id: 'safe', photo: [955, 460, 230, 280], x: 1080, y: 380, w: 300, h: 260, art: () => `<rect x="1100" y="400" width="260" height="220" fill="#3a3a3a"/><circle cx="1230" cy="510" r="40" fill="#888"/>${L(1230, 660, F().safe ? 'Safe (open)' : 'Safe (4 numbers)')}`, act: () => openSafe() },
        { id: 'cot', photo: [1100, 305, 300, 145], x: 1100, y: 140, w: 400, h: 200, art: () => `<rect x="1120" y="200" width="360" height="80" fill="#6a7a5a"/>${L(1300, 330, 'Camp bed')}`,
          act: () => { if (F().cot) return E.say('Just a lumpy pillow.'); F().cot = 1; E.give('brush'); E.say('Under the pillow: a soft dig brush.'); } },
      ],
    },
    pit: {
      name: 'The dig pit',
      bg: () => `<rect width="1600" height="900" fill="#b8783a"/>${[0, 1, 2, 3].map(i => `<rect x="0" y="${200 + i * 160}" width="1600" height="8" fill="#9a5a2a"/>`).join('')}`,
      spots: [
        { id: 'up', photo: [1255, 225, 345, 640], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('↑ Camp', 1240), act: () => E.go('camp') },
        { id: 'sand1', photo: [800, 440, 335, 155], x: 80, y: 300, w: 340, h: 260, art: () => `<ellipse cx="250" cy="440" rx="150" ry="70" fill="#d8a868"/>${L(250, 580, 'Sandy patch A')}`, act: () => dig('a', 'tooth', 'a huge pointed fossil tooth!') },
        { id: 'sand2', photo: [360, 605, 415, 180], x: 500, y: 420, w: 340, h: 240, art: () => `<ellipse cx="670" cy="540" rx="150" ry="70" fill="#d8a868"/>${L(670, 660, 'Sandy patch B')}`, act: () => dig('b', 'egg', 'a round stone dinosaur egg!') },
        { id: 'sand3', photo: [185, 400, 255, 160], x: 920, y: 260, w: 340, h: 260, art: () => `<ellipse cx="1090" cy="400" rx="150" ry="70" fill="#d8a868"/>${L(1090, 540, 'Sandy patch C')}`, act: () => dig('c', 'bone', 'a curved fossil claw!') },
        { id: 'box', photo: [1185, 15, 370, 260], x: 1300, y: 120, w: 260, h: 200, art: () => `<rect x="1320" y="160" width="220" height="120" fill="#5a3a20"/>${L(1430, 320, 'Tool box')}`,
          act: () => { if (F().box) return E.say('Trowels and string. Nothing useful.'); F().box = 1; E.give('radioPart'); E.say('In the tool box: a heavy battery labelled RADIO.'); } },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['radio', () => F().radio, ['The camp radio is dead.', 'Look for a battery in the dig pit.', 'Take the battery from the tool box and use it on the radio.']],
    ['dig', () => F().a && F().b && F().c, ['There are three sandy patches in the pit.', 'You need something to brush the sand away gently.', 'The brush is under the pillow in the tent. Brush all three patches.']],
    ['display', () => F().display, ['The display shelf has three spaces.', 'The poster says small to large.', 'Claw, egg, tooth – then check the shelf.']],
    ['safe', () => F().safe, ['The safe wants four numbers.', 'The radio said: the year the museum opened.', 'The camp sign: 1987.']],
    ['jeep', () => F().won, ['Now drive!', 'The safe held the jeep key.', 'Use the key on the jeep.']],
  ],
  intro: ['The badlands · summer · 14:00', 'The Dinosaur Dig',
    `<p>You are helping at a real dinosaur dig. The professor has driven to town – and now the sky is turning black. A sandstorm is coming!</p><p>You must get the camp jeep out before the storm hits in one hour. But the key is locked away, and the professor said nobody leaves until the fossils are safe on the shelf…</p><p>Level 1: perfect for families and first-time players.</p>`,
    'Hot sun, a dusty camp and a dark sky in the north. Look around.'],
  timesUp: ['The storm is here!', 'Sand whips past the tent… hold on and finish the job!'],
  win: ['Out of the storm!', 'The jeep roars down the north track with the fossils safe on the back seat. The professor waves from the town museum steps: you saved the dig!'],
};

function dig(k, item, what) {
  if (F()[k]) return E.say('Just sand now.');
  if (!E.has('brush')) return E.say('Something is buried here – you can see a corner. You need something soft to sweep the sand away without breaking it.');
  F()[k] = 1; E.give(item); E.say('You brush gently… and find ' + what);
}
function place(item) {
  F()['on_' + item] = 1; E.take(item); E.say('You set the fossil on the display shelf.');
  return true;
}
function openDisplay() {
  if (F().display) return E.say('Claw, egg, tooth – all safe on the shelf.');
  if (!(F().on_tooth && F().on_egg && F().on_bone)) return E.say('Three empty spaces on the shelf, labelled SMALL, MEDIUM and LARGE. Put the fossils on it.');
  E.cycler('Display shelf', 'Arrange the fossils on the labelled spaces.', SIZES.map(n => ({ name: n, opts: ['Tooth', 'Egg', 'Claw'] })), v => { if (v.join() !== 'Claw,Egg,Tooth') return false; F().display = 1; E.say('Click! A little drawer slides out under the shelf: “Good digger! Safe code = museum year.”'); E.note('drawer', 'Under the display shelf: “Good digger! Safe code = the year the museum opened.”'); return true; }, 'Nothing happens. Small to large!', 'Done');
}
function openSafe() {
  if (F().safe) return E.say('The safe is open and empty.');
  if (!F().display) return E.say('A safe with four number wheels. A sticker: “Fossils on the shelf first!” It won’t turn.');
  E.numLock('Professor’s safe', 'Four number wheels.', 4, c => { if (c !== '1987') return false; F().safe = 1; E.give('jeepKey'); E.say('The safe swings open: a dusty jeep key on a dinosaur key ring!'); return true; });
}
});
