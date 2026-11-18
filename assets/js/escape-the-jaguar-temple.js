/* Six Clues escape room #28 – The Jaguar Temple (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const stone = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 12 }, (_, r) => Array.from({ length: 8 }, (_, c) => `<rect x="${c * 200 + (r % 2 ? 100 : 0)}" y="${r * 60}" width="196" height="56" fill="${c2}"/>`).join('')).join('')}<rect y="660" width="1600" height="240" fill="#2a2a1e"/>`;
const SIGNS = ['Jaguar', 'Eagle', 'Serpent', 'Monkey', 'Deer'];
const BODIES = ['Sun', 'Moon', 'Venus'];

return {
  start: 'entrance', v: 1,
  items: {
    journal: ['📔', 'Explorer’s journal', 'Dr Lindqvist’s field journal, 1925.'],
    mirror: ['🪞', 'Obsidian mirror', 'A disc of polished black stone that reflects light.'],
    jadeA: ['🟢', 'Jade eye', 'A round jade stone, carved like an eye.'],
    jadeB: ['🟢', 'Second jade eye', 'The other jade eye.'],
    rope: ['🪢', 'Rope', 'A coil of strong rope.'],
  },
  rooms: {
    entrance: {
      name: 'The temple entrance',
      bg: () => stone('#3a4a2a', '#44542e'),
      spots: [
        { id: 'camp', x: 80, y: 420, w: 380, h: 220, art: () => `<rect x="100" y="480" width="340" height="120" fill="#6a5a3a"/>${L(270, 640, 'Abandoned camp')}`,
          act: () => { if (F().camp) return E.say('A broken lamp and an empty tin of beans.'); F().camp = 1; E.give('journal'); E.give('rope'); E.note('journal', 'Dr Lindqvist’s journal: “Maya numbers: a dot is one, a bar is five. The temple door counts in Maya numbers.” Later: “The calendar chamber: the Jaguar day comes when Venus rises – do not trust the painted sign by the door, the looters made it!” Last page: “Never touch the golden idol.”'); E.say('An abandoned camp: an explorer’s journal and a coil of rope. The journal is full of notes about the temple.'); } },
        { id: 'door', x: 560, y: 120, w: 480, h: 520, art: () => `<rect x="580" y="140" width="440" height="480" fill="#2a2a1e"/>${L(800, 660, F().door ? 'Temple door (open)' : 'Stone door – three carved numbers')}`, act: () => F().door ? E.go('calendar') : openDoor() },
        { id: 'glyphs', x: 1100, y: 120, w: 400, h: 280, art: () => `<rect x="1120" y="140" width="360" height="200" fill="#5a5a40"/>${L(1300, 380, 'Carvings above the door')}`,
          act: () => { E.note('glyphs', 'Carvings above the door, three numbers: first ●●● · second ▬ ● · third ▬ ●●●●'); E.say('Three carved numbers: ●●●, then ▬ ●, then ▬ ●●●●.'); } },
        { id: 'idol', x: 1140, y: 440, w: 300, h: 200, art: () => `<rect x="1240" y="480" width="80" height="120" fill="#e8c040"/>${L(1290, 640, 'Golden idol')}`,
          act: () => E.say('A golden idol on a pedestal. Every instinct says: grab it! The journal says: never touch it. You leave it alone.') },
      ],
    },
    calendar: {
      name: 'The calendar chamber',
      bg: () => stone('#4a3a2a', '#54442e'),
      spots: [
        { id: 'back', x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Entrance'), act: () => E.go('entrance') },
        { id: 'painted', x: 80, y: 120, w: 360, h: 260, art: () => `<rect x="100" y="140" width="320" height="200" fill="#a04a2a"/>${L(260, 380, 'Painted sign by the door')}`,
          act: () => E.say('A freshly painted sign: “JAGUAR DAY – SUN”. The paint is still bright. Too bright for a thousand years.') },
        { id: 'wheel', x: 520, y: 100, w: 560, h: 540, art: () => `<circle cx="800" cy="370" r="240" fill="#6a5a3a" stroke="#c9a24a" stroke-width="12"/><circle cx="800" cy="370" r="120" fill="#5a4a2e"/>${L(800, 660, F().wheel ? 'Calendar wheel (turned)' : 'Great calendar wheel – two rings')}`, act: () => openWheel() },
        { id: 'altar', x: 1140, y: 380, w: 360, h: 260, art: () => `<rect x="1160" y="460" width="320" height="140" fill="#4a4a3a"/>${L(1320, 640, 'Small altar')}`,
          act: () => F().wheel ? (F().altar ? E.say('An empty altar.') : (F().altar = 1, E.give('mirror'), E.give('jadeA'), E.say('In the altar’s opened top: an obsidian mirror and a jade eye!'))) : E.say('A stone altar with a closed lid, carved with a jaguar.') },
        { id: 'toWater', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Water chamber →', 1240), act: () => E.go('water') },
      ],
    },
    water: {
      name: 'The water chamber',
      bg: () => `${stone('#2a3a3a', '#324444')}<rect y="520" width="1600" height="140" fill="#1e4a5a"/>`,
      spots: [
        { id: 'back', x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Calendar chamber'), act: () => E.go('calendar') },
        { id: 'beam', x: 100, y: 60, w: 360, h: 260, art: () => `<path d="M200 60 L360 300" stroke="#fff4a0" stroke-width="20" opacity=".6"/>${L(280, 320, 'Shaft of sunlight')}`,
          act: () => E.say('A shaft of sunlight falls through a crack in the roof and hits the floor. On the far wall, a glyph sits in shadow.'),
          use: { mirror: () => { F().light = 1; E.say('You catch the sunlight in the obsidian mirror and turn it onto the far wall. The glyph lights up – a jaguar – and a stone slides open under it.'); return true; } } },
        { id: 'glyph', x: 1000, y: 100, w: 400, h: 300, art: () => `<rect x="1020" y="120" width="360" height="240" fill="${F().light ? '#8a7a4a' : '#2a2a22'}"/>${L(1200, 400, F().light ? 'Lit glyph – a niche below' : 'Glyph in shadow')}`,
          act: () => F().light ? (F().jadeTaken ? E.say('An empty niche.') : (F().jadeTaken = 1, E.give('jadeB'), E.say('In the niche under the glyph: the second jade eye!'))) : E.say('Too dark to see the glyph properly.') },
        { id: 'pool', x: 300, y: 520, w: 700, h: 140, art: () => L(650, 600, 'Deep pool'),
          act: () => E.say('Deep, clear water – too deep to wade. On the far side, a dark passage. A stone post stands on this bank.'),
          use: { rope: () => { F().rope = 1; E.take('rope'); E.say('You tie the rope to the stone post and throw it to a hook on the far side. Now you can cross!'); return true; } } },
        { id: 'toThrone', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit(F().rope ? 'Across the pool →' : 'Far side (too deep)', 1240), act: () => F().rope ? E.go('throne') : E.say('The pool is too deep to cross.') },
      ],
    },
    throne: {
      name: 'The jaguar throne',
      bg: () => stone('#2a1e1a', '#34261e'),
      spots: [
        { id: 'back', x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Water chamber'), act: () => E.go('water') },
        { id: 'jaguar', x: 500, y: 100, w: 600, h: 540, art: () => `<path d="M560 600 Q560 300 800 260 Q1040 300 1040 600z" fill="#3a3a2a"/><circle cx="740" cy="360" r="20" fill="${F().eyeA ? '#3aa04a' : '#111'}"/><circle cx="860" cy="360" r="20" fill="${F().eyeB ? '#3aa04a' : '#111'}"/>${L(800, 650, 'Stone jaguar on the throne')}`, act: () => openJaguar(),
          use: { jadeA: () => { F().eyeA = 1; E.take('jadeA'); E.say('The jade eye clicks into the jaguar’s left socket.'); return true; }, jadeB: () => { F().eyeB = 1; E.take('jadeB'); E.say('The jade eye clicks into the jaguar’s right socket.'); return true; } } },
        { id: 'skeleton', x: 1180, y: 380, w: 320, h: 260, art: () => `<rect x="1200" y="480" width="280" height="80" fill="#e8e0c8"/>${L(1340, 620, 'Old bones')}`,
          act: () => E.say('A looter’s bones, still clutching a fake golden idol. A lesson.') },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['camp', () => F().camp, ['Look around the entrance.', 'The abandoned camp may have something useful.', 'Search the abandoned camp.']],
    ['door', () => F().door, ['The temple door wants three numbers.', 'The journal explains Maya numbers: dot = 1, bar = 5. Read the carvings.', '●●● = 3, ▬● = 6, ▬●●●● = 9: 369.']],
    ['wheel', () => F().wheel, ['The calendar wheel has two rings.', 'The painted sign is a looters’ fake. The journal says when the Jaguar day comes.', 'Jaguar and Venus.']],
    ['light', () => F().light, ['The glyph in the water chamber is in shadow.', 'You have something that reflects light.', 'Use the obsidian mirror on the shaft of sunlight.']],
    ['rope', () => F().rope, ['The pool is too deep.', 'You have a rope from the camp.', 'Use the rope on the pool.']],
    ['jaguar', () => F().won, ['The stone jaguar has empty eyes.', 'You found two jade eyes.', 'Put both eyes in the jaguar.']],
  ],
  intro: ['Yucatán jungle · 1925 · 15:00', 'The Jaguar Temple',
    `<p>Your mentor, Dr Lindqvist, vanished a week ago searching for the lost Jaguar Temple. You have found it – and his camp, abandoned at the door.</p><p>As you step inside, the stone door grinds shut behind you. The guides say the river floods the valley at sunset, in one hour. Follow his journal through the temple and find the hidden way out.</p><p>Level 2: looters have left false signs behind.</p>`,
    'Vines, carved stone and the hum of insects. Look around.'],
  timesUp: ['Sunset.', 'Water trickles in under the stones… you can still finish, off the leaderboard.'],
  win: ['The jaguar wakes', 'The jade eyes glow, the stone jaguar slides back on its throne, and a stair opens into daylight on the hillside above the river. And there, sitting on a rock with a broken leg and a huge grin, is Dr Lindqvist.'],
};

function openDoor() {
  E.numLock('Temple door', 'Three stone wheels carved with Maya numbers 0–9.', 3, c => { if (c !== '369') return false; F().door = 1; E.say('Grinding stone – the door rolls aside.'); return true; });
}
function openWheel() {
  if (F().wheel) return E.say('The calendar wheel is set: Jaguar and Venus.');
  E.cycler('Calendar wheel', 'Turn the outer ring to a day sign, and the inner ring to a sky body.', [{ name: 'Day sign', opts: SIGNS }, { name: 'Sky', opts: BODIES }], v => { if (v.join() !== 'Jaguar,Venus') return false; F().wheel = 1; E.say('CLUNK. Deep in the wall, something moves. The lid of the little altar slides open.'); return true; }, 'The wheel shudders and sticks.', 'Turn');
}
function openJaguar() {
  if (!(F().eyeA && F().eyeB)) return E.say('A great stone jaguar on a throne. Its eye sockets are empty.');
  E.modal(`<h2>The jaguar throne</h2><p>Both jade eyes glow green. A low rumble runs through the stone.</p><button class="btn btn-big" id="push">Push the jaguar</button>`, m => m.querySelector('#push').addEventListener('click', () => { E.closeModal(); E.win(); }));
}
});
