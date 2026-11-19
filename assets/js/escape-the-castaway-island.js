/* Six Clues escape room #25 – The Castaway Island (level 1, family). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const PARROTS = ['Red', 'Blue', 'Green', 'Yellow'];

return {
  start: 'beach', v: 2,
  items: {
    wood: ['🪵', 'Dry driftwood', 'A bundle of dry, silver-grey driftwood.'],
    banana: ['🍌', 'Banana', 'A ripe yellow banana.'],
    flint: ['🪨', 'Flint stone', 'A sharp flint that sparks when you strike it.'],
    lens: ['🔍', 'Glass lens', 'A big round glass lens from an old ship’s lamp.'],
    machete: ['🔪', 'Old machete', 'A rusty but sharp jungle machete.'],
  },
  rooms: {
    beach: {
      name: 'The beach',
      bg: () => `<rect width="1600" height="900" fill="#7ac8e8"/><rect y="380" width="1600" height="200" fill="#2a8ab8"/><rect y="560" width="1600" height="340" fill="#f0d8a0"/><circle cx="1350" cy="130" r="70" fill="#fff4a0"/>`,
      spots: [
        { id: 'bottle', photo: [185, 640, 200, 145], x: 100, y: 580, w: 260, h: 140, art: () => `<rect x="180" y="620" width="90" height="36" rx="16" fill="#6ab08a" transform="rotate(-15 225 638)"/>${L(230, 710, 'Bottle in the sand')}`,
          act: () => { E.note('bottle', 'Message in a bottle, from the last castaway: “To call a ship, build a signal fire on the big rock: dry wood, a spark – and a lens to make it shine for miles. I hid the lens in the cave. The monkey stole my flint!”'); E.say('A message in a bottle: build a signal fire – dry wood, a spark and a lens. The lens is in the cave, and the monkey stole the flint!'); } },
        { id: 'driftwood', photo: [500, 610, 610, 195], x: 420, y: 600, w: 360, h: 140, art: () => `<rect x="440" y="650" width="320" height="30" rx="14" fill="#b8b0a0"/>${L(600, 720, 'Driftwood')}`,
          act: () => { if (F().wood) return E.say('Only wet driftwood left.'); F().wood = 1; E.give('wood'); E.say('You pick out the driest pieces of driftwood.'); } },
        { id: 'rock', photo: [1110, 370, 490, 425], x: 1060, y: 360, w: 460, h: 300, art: () => `<path d="M1080 640 Q1160 380 1300 380 Q1480 400 1500 640z" fill="#7a7a7a"/>${L(1290, 660, 'Big rock – signal fire spot')}`, act: () => openFire(),
          use: { wood: () => { F().woodIn = 1; E.take('wood'); E.say('You stack the dry wood on the big rock.'); return true; }, flint: () => { if (!F().woodIn) return false; F().spark = 1; E.take('flint'); E.say('Strike! Sparks fly and the wood starts to smoke.'); return true; }, lens: () => { if (!F().spark) return false; F().lensIn = 1; E.take('lens'); E.say('You set the lens on its stand above the fire. It catches the sunlight…'); return true; } } },
        { id: 'toJungle', photo: [0, 330, 230, 500], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Jungle'), act: () => E.go('jungle') },
      ],
    },
    jungle: {
      name: 'The jungle',
      bg: () => `<rect width="1600" height="900" fill="#1e4a2a"/>${Array.from({ length: 12 }, (_, i) => `<ellipse cx="${i * 140}" cy="${100 + (i % 3) * 60}" rx="120" ry="60" fill="#2a6a3a"/>`).join('')}<rect y="640" width="1600" height="260" fill="#3a2a1a"/>`,
      spots: [
        { id: 'back', photo: [1200, 720, 400, 180], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Beach →', 1240), act: () => E.go('beach') },
        { id: 'monkey', photo: [130, 45, 240, 190], x: 100, y: 140, w: 340, h: 340, art: () => `<circle cx="270" cy="300" r="60" fill="#8a5a2a"/>${L(270, 420, 'Cheeky monkey')}`,
          act: () => F().monkey ? E.say('The monkey munches its banana and ignores you.') : E.say('A cheeky monkey in the tree, juggling a grey stone – the flint! It chatters at you and holds out its hand.'),
          use: { banana: () => { F().monkey = 1; E.take('banana'); E.give('flint'); E.say('The monkey grabs the banana – and drops the flint into your hands. Fair swap!'); return true; } } },
        { id: 'bananas', photo: [780, 55, 165, 240], x: 520, y: 100, w: 300, h: 300, art: () => `<path d="M600 180 q60 60 120 0" stroke="#f0d040" stroke-width="22" fill="none"/>${L(670, 360, F().cut ? 'Banana tree (picked)' : 'Banana tree (too high)')}`,
          act: () => F().cut ? E.say('You already have a banana.') : E.say('A bunch of bananas, high up and tied in thick vines. You can’t pull them free with your hands.'),
          use: { machete: () => { F().cut = 1; E.give('banana'); E.say('Swish! You cut the vines and a banana drops down.'); return true; } } },
        { id: 'parrots', photo: [1190, 45, 345, 210], x: 900, y: 120, w: 460, h: 280, art: () => `${PARROTS.map((c, i) => `<ellipse cx="${960 + i * 110}" cy="240" rx="30" ry="50" fill="${['#d03030', '#3060d0', '#30a040', '#e0c030'][i]}"/>`).join('')}${L(1130, 380, 'Four parrots')}`,
          act: () => { E.note('parrots', 'The parrots squawk in turn: “Red! Yellow! Blue! … Red! Yellow! Blue!”'); E.say('The parrots squawk in turn: “Red! Yellow! Blue!” – again and again.'); } },
        { id: 'toCave', photo: [530, 465, 250, 250], x: 600, y: 740, w: 360, h: 130, art: () => E.exit(F().cave ? 'Cave ↓' : 'Cave (blocked)', 620), act: () => F().cave ? E.go('cave') : E.say('A cave entrance blocked by a stone door with three coloured feathers carved on it.') },
        { id: 'stonedoor', photo: [1150, 360, 290, 350], x: 980, y: 440, w: 380, h: 200, art: () => `<rect x="1000" y="460" width="340" height="160" fill="#6a6a6a"/>${L(1170, 650, F().cave ? 'Stone door (open)' : 'Stone door – three feather buttons')}`, act: () => openStone() },
      ],
    },
    cave: {
      name: 'The cave',
      bg: () => `<rect width="1600" height="900" fill="#1a1612"/><ellipse cx="800" cy="320" rx="700" ry="320" fill="#2a2420"/><rect y="640" width="1600" height="260" fill="#14100c"/>`,
      spots: [
        { id: 'up', photo: [0, 345, 200, 370], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('↑ Jungle'), act: () => E.go('jungle') },
        { id: 'tally', photo: [240, 60, 270, 190], x: 120, y: 120, w: 440, h: 280, art: () => `${Array.from({ length: 5 }, (_, i) => `<path d="M${160 + i * 70} 180 v100 M${175 + i * 70} 180 v100 M${190 + i * 70} 180 v100 M${205 + i * 70} 180 v100 M${150 + i * 70} 240 l70 -40" stroke="#c8b890" stroke-width="5"/>`).join('')}${L(340, 400, 'Marks scratched on the wall')}`,
          act: () => { E.note('tally', 'Marks on the cave wall: the last castaway counted his days on the island – 5 groups of 5, then 2 more. Under them: “Days on the island – the chest remembers.”'); E.say('Tally marks: 5 groups of five, and 2 more. “Days on the island – the chest remembers.”'); } },
        { id: 'chest', photo: [455, 445, 510, 335], x: 640, y: 400, w: 380, h: 240, art: () => `<rect x="660" y="440" width="340" height="180" rx="16" fill="#6a3a1a"/>${L(830, 660, F().chest ? 'Old chest (open)' : 'Old chest (2 numbers)')}`, act: () => openChest() },
        { id: 'skeleton', photo: [1115, 400, 485, 350], x: 1100, y: 300, w: 380, h: 340, art: () => `<rect x="1160" y="400" width="260" height="200" fill="#4a3a2a"/>${L(1290, 640, 'Castaway’s bed of leaves')}`,
          act: () => { if (F().machete) return E.say('A bed of dry leaves.'); F().machete = 1; E.give('machete'); E.say('Under the leaves: an old rusty machete!'); } },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['cave', () => F().cave, ['The cave has a stone door with feather buttons.', 'Listen to the parrots.', 'Red, Yellow, Blue.']],
    ['machete', () => F().machete || F().cut, ['The bananas are tied in thick vines.', 'You need something sharp. Look around the cave.', 'Search the bed of leaves in the cave, then use the machete on the banana tree.']],
    ['monkey', () => F().monkey, ['The monkey has the flint.', 'Monkeys love bananas.', 'Cut a banana with the machete and give it to the monkey.']],
    ['chest', () => F().chest, ['The old chest wants two numbers.', 'Count the castaway’s days on the wall.', '5 × 5 + 2 = 27.']],
    ['fire', () => F().won, ['Build the signal fire on the big rock.', 'Wood first, then the flint, then the lens.', 'Then light it!']],
  ],
  intro: ['A tiny island · the Pacific · 08:00', 'The Castaway Island',
    `<p>Your little sailing boat sank in the night, and you woke up on a tiny tropical island with nothing but the clothes you’re wearing.</p><p>A ship passes the island once a day – in one hour. Build a signal fire big enough to be seen for miles, and get rescued!</p><p>Level 1: perfect for families and first-time players.</p>`,
    'Warm sand, palm trees and waves. Look around.'],
  timesUp: ['The ship is passing!', 'It hasn’t seen you yet… hurry!'],
  win: ['Ship ahoy!', 'The lens makes your fire blaze bright, and a column of smoke rises into the sky. A horn sounds out at sea – the ship turns towards the island! Soon you are on deck, wrapped in a blanket, waving goodbye to the monkey.'],
};

function openStone() {
  if (F().cave) return E.say('The stone door is open.');
  E.cycler('Stone door', 'Three carved feather buttons. Each can be pressed to change its colour.', ['1st', '2nd', '3rd'].map(n => ({ name: n, opts: PARROTS })), v => { if (v.join() !== 'Red,Yellow,Blue') return false; F().cave = 1; E.say('Rumble! The stone door slides open. A dark cave goes down into the hill.'); return true; }, 'The door doesn’t move.', 'Push');
}
function openChest() {
  if (F().chest) return E.say('The chest is empty now.');
  E.numLock('Old chest', 'A sea chest with two number wheels.', 2, c => { if (c !== '27') return false; F().chest = 1; E.give('lens'); E.say('Creak… inside: a big round glass lens from a ship’s lamp!'); return true; });
}
function openFire() {
  if (!F().woodIn) return E.say('The big rock at the end of the beach – the best spot for a signal fire. It needs dry wood.');
  if (!F().spark) return E.say('The wood is stacked. Now you need a spark.');
  if (!F().lensIn) return E.say('The fire smokes a little. The bottle said a lens makes it shine for miles.');
  E.modal(`<h2>Signal fire</h2><p>Wood, spark, lens – all ready. The ship’s smoke is on the horizon.</p><button class="btn btn-big" id="blaze">Blow on the fire!</button>`, m => m.querySelector('#blaze').addEventListener('click', () => { E.closeModal(); E.win(); }));
}
});
