/* Six Clues escape room #12 – The Pirate's Cove (level 1, family). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const FLAGS = ['White', 'Red', 'Black', 'Blue'];

return {
  start: 'cave', v: 2,
  items: {
    spyglass: ['🔭', 'Spyglass', 'A brass telescope that pulls out to three times its length.'],
    bootKey: ['🗝️', 'Iron key', 'A rusty iron key that smells of old boot.'],
    coinA: ['🪙', 'Half a coin', 'The left half of a gold coin with a skull on it.'],
    coinB: ['🪙', 'Half a coin', 'The right half of a gold coin with a skull on it.'],
    coin: ['🪙', 'Skull coin', 'A whole gold coin with a grinning skull on it.'],
    lantern: ['🏮', 'Empty lantern', 'A ship’s lantern – no oil in it.'],
    oil: ['🛢️', 'Lamp oil', 'A small bottle of whale-oil.'],
    lit: ['🔥', 'Lit lantern', 'A ship’s lantern, burning bright.'],
    oar: ['🛶', 'Oar', 'A long wooden oar with a painted blade.'],
  },
  rooms: {
    cave: {
      name: 'The smugglers’ cave',
      bg: () => `<rect width="1600" height="900" fill="#1e2a2e"/><path d="M0 0 H1600 V120 Q800 40 0 140z" fill="#141c1e"/><ellipse cx="1300" cy="380" rx="200" ry="220" fill="#7fb0c8"/><rect y="660" width="1600" height="240" fill="#6a5a3a"/>`,
      spots: [
        { id: 'parrot', photo: [40, 65, 210, 270], x: 120, y: 160, w: 240, h: 260, art: () => `<ellipse cx="240" cy="300" rx="60" ry="90" fill="#2aa04a"/><circle cx="240" cy="220" r="40" fill="#d04030"/>${L(240, 440, 'Parrot on a perch')}`,
          act: () => { E.note('parrot', 'The parrot squawks the same thing over and over: “White up top! Then Red! Then Black at the bottom! Squawk!”'); E.say('“White up top! Then Red! Then Black at the bottom! Squawk!”'); } },
        { id: 'mast', photo: [320, 20, 255, 675], x: 440, y: 80, w: 260, h: 580, art: () => `<rect x="560" y="100" width="20" height="560" fill="#5a3a20"/>${[0, 1, 2].map(i => `<rect x="580" y="${140 + i * 90}" width="100" height="60" fill="#ddd"/>`).join('')}${L(570, 690, F().flags ? 'Flagpole (flags set)' : 'Flagpole – three flags')}`, act: () => openFlags() },
        { id: 'mouth', photo: [1120, 40, 480, 380], x: 1100, y: 160, w: 400, h: 440, art: () => L(1300, 640, 'Cave mouth – the bay'),
          act: () => F().seen ? E.say('Across the bay, the numbers 7 3 1 are still painted on the far rock.') : E.say('The sea glitters out in the bay. Far across it, on a grey rock, there is something painted – too far to read.'),
          use: { spyglass: () => { F().seen = 1; E.note('rock', 'Through the spyglass: on the far rock across the bay, big white numbers – 7 3 1.'); E.say('Through the spyglass: on the far rock, big white numbers – 7 3 1!'); return true; } } },
        { id: 'tunnel', photo: [585, 295, 215, 305], x: 760, y: 300, w: 260, h: 340, art: () => `<path d="M780 640 Q780 320 890 320 Q1000 320 1000 640z" fill="#050808"/>${L(890, 680, F().tunnel ? 'Dark tunnel (lit)' : 'Pitch-dark tunnel')}`,
          act: () => F().tunnel ? E.go('grotto') : E.say('A tunnel into the cliff. It is pitch black – you would need a light.'),
          use: { lit: () => { F().tunnel = 1; E.say('The lantern throws gold light down the tunnel. It goes deep into the cliff.'); return true; } } },
        { id: 'barrel', photo: [0, 605, 255, 290], x: 40, y: 500, w: 260, h: 180, art: () => `<rect x="70" y="520" width="180" height="150" rx="30" fill="#7a4a24"/>${L(160, 690, 'Old barrel')}`,
          act: () => { if (F().lantern) return E.say('An empty barrel.'); F().lantern = 1; E.give('lantern'); E.say('Inside the barrel: an old ship’s lantern. No oil in it.'); } },
        { id: 'toShip', photo: [1015, 455, 585, 330], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit(F().flags ? 'Wrecked ship →' : 'Wrecked ship (door shut)', 1240), act: () => F().flags ? E.go('cabin') : E.say('The half-sunk ship’s cabin door is shut tight. A sign: “Fly my colours right and I’ll open.”') },
      ],
    },
    cabin: {
      name: 'The captain’s cabin',
      bg: () => `<rect width="1600" height="900" fill="#4a3020"/>${Array.from({ length: 12 }, (_, i) => `<rect x="0" y="${i * 60}" width="1600" height="4" fill="#3a2414"/>`).join('')}<rect y="660" width="1600" height="240" fill="#3a2414"/>`,
      spots: [
        { id: 'back', photo: [0, 0, 110, 860], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Cave'), act: () => E.go('cave') },
        { id: 'log', photo: [340, 390, 270, 110], x: 120, y: 360, w: 340, h: 220, art: () => `${E.paper(140, 380, 300, 180, 6)}${L(290, 600, 'Captain’s log')}`,
          act: () => { E.note('log', 'Captain’s log: “Day 40. I keep the key to my sea chest where no one looks – in my left boot. The treasure sleeps in the grotto; only my ship’s name and my skull coin open it.”'); E.say('The captain’s log mentions a key in his left boot – and that the treasure needs his ship’s name and his skull coin.'); } },
        { id: 'boots', photo: [685, 520, 155, 200], x: 520, y: 520, w: 260, h: 160, art: () => `<rect x="560" y="560" width="70" height="110" fill="#2a1a10"/><rect x="660" y="560" width="70" height="110" fill="#2a1a10"/>${L(650, 700, 'Pair of sea boots')}`,
          act: () => { if (F().boot) return E.say('Just smelly boots now.'); F().boot = 1; E.give('bootKey'); E.say('You shake the left boot. Out falls a rusty iron key!'); } },
        { id: 'chest', photo: [890, 440, 365, 305], x: 820, y: 470, w: 320, h: 200, art: () => `<rect x="840" y="500" width="280" height="150" rx="14" fill="#6b3a1a" stroke="#c9a24a" stroke-width="8"/>${L(980, 690, F().chest ? 'Sea chest (open)' : 'Sea chest (locked)')}`,
          act: () => F().chest ? E.say('The sea chest is empty now.') : E.say('A heavy sea chest with an iron lock.'),
          use: { bootKey: () => { F().chest = 1; E.take('bootKey'); E.give('spyglass'); E.give('coinA'); E.say('The chest creaks open: a brass spyglass and half of a gold coin!'); return true; } } },
        { id: 'bell', photo: [1205, 30, 170, 170], x: 1180, y: 100, w: 220, h: 220, art: () => `<path d="M1240 140 Q1290 120 1340 140 L1360 260 H1220z" fill="#c9a24a"/>${L(1290, 300, 'Ship’s bell')}`,
          act: () => { E.note('bell', 'Engraved on the ship’s bell: “SEA WOLF – 1715”.'); E.say('Ding! The bell is engraved: “SEA WOLF – 1715”.'); } },
        { id: 'navbox', photo: [1300, 355, 285, 155], x: 1160, y: 420, w: 320, h: 220, art: () => `<rect x="1180" y="460" width="280" height="160" fill="#2e4a5a"/><circle cx="1320" cy="540" r="50" fill="#c9a24a"/>${L(1320, 660, F().nav ? 'Navigator’s box (open)' : 'Navigator’s box (3 numbers)')}`, act: () => openNav() },
      ],
    },
    grotto: {
      name: 'The treasure grotto',
      bg: () => `<rect width="1600" height="900" fill="#0e1a1c"/><ellipse cx="800" cy="300" rx="600" ry="260" fill="#14262a"/><rect y="620" width="1600" height="280" fill="#1e4a5a"/>`,
      spots: [
        { id: 'back', photo: [0, 345, 150, 350], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Tunnel'), act: () => E.go('cave') },
        { id: 'treasure', photo: [555, 195, 480, 290], x: 560, y: 360, w: 460, h: 260, art: () => `<rect x="600" y="420" width="380" height="180" rx="20" fill="#7a4a1a" stroke="#c9a24a" stroke-width="10"/><circle cx="790" cy="470" r="22" fill="#111"/>${L(790, 650, F().treasure ? 'Treasure chest (open)' : 'Treasure chest – a coin slot and a name lock')}`,
          act: () => openTreasure(), use: { coin: () => { F().coinIn = 1; E.take('coin'); E.say('The skull coin drops into the slot with a clunk. Now the name lock…'); return true; } } },
        { id: 'boat', photo: [1275, 465, 325, 280], x: 1120, y: 560, w: 440, h: 180, art: () => `<path d="M1140 620 Q1340 720 1540 620z" fill="#6b4226"/>${L(1340, 760, 'Little rowing boat')}`,
          act: () => E.say(F().treasure ? 'The rowing boat bobs on the water. It has no oars!' : 'A little rowing boat tied up in the grotto. The sea gate is open – but there are no oars.'),
          use: { oar: () => { E.take('oar'); E.win(); return true; } } },
        { id: 'skeleton', photo: [265, 245, 320, 320], x: 200, y: 360, w: 280, h: 260, art: () => `<circle cx="340" cy="420" r="40" fill="#e8e0c8"/><rect x="320" y="460" width="40" height="120" fill="#e8e0c8"/>${L(340, 640, 'Old skeleton')}`,
          act: () => E.say('A grinning old skeleton wearing a pirate hat. A note in its hand: “I tried to open the chest without the coin. Don’t.”') },
      ],
    },
  },
  combine: (a, b) => { if ([a, b].sort().join() === 'coinA,coinB') { E.take('coinA'); E.take('coinB'); E.give('coin'); F().coin = 1; E.say('The two halves click together: a whole gold skull coin!'); return true; }
    if ([a, b].sort().join() === 'lantern,oil') { E.take('lantern'); E.take('oil'); E.give('lit'); F().lit = 1; E.say('You fill the lantern and strike a match. It burns bright!'); return true; } return false; },
  stages: [
    ['flags', () => F().flags, ['The ship’s door wants its colours flown right.', 'Listen to the parrot.', 'Top to bottom: White, Red, Black.']],
    ['boot', () => F().chest, ['The captain’s log says where he keeps a key.', 'Look in his left boot.', 'Take the key from the boots and use it on the sea chest.']],
    ['seen', () => F().seen, ['The navigator’s box needs three numbers – and you now have a spyglass.', 'Look across the bay from the cave mouth.', 'Use the spyglass on the cave mouth: 7 3 1.']],
    ['nav', () => F().nav, ['The navigator’s box wants three numbers.', 'You saw them painted on the far rock.', '731.']],
    ['lit', () => F().lit, ['The tunnel is dark. You have an empty lantern and some oil.', 'Combine them.', 'Tap the lantern, then the oil.']],
    ['tunnel', () => F().tunnel, ['You have a lit lantern.', 'Use it on the dark tunnel in the cave.', 'Use the lit lantern on the tunnel, then go through.']],
    ['coin', () => F().coinIn, ['The treasure chest has a coin slot.', 'You have two halves of a coin.', 'Combine the halves, then use the coin on the chest.']],
    ['treasure', () => F().treasure, ['The chest also wants a name.', 'The captain’s log: his ship’s name. The ship’s bell has it.', 'WOLF – the four-letter lock.']],
    ['boat', () => F().won, ['The boat has no oars.', 'Look inside the treasure chest.', 'Use the oar on the rowing boat.']],
  ],
  intro: ['Cornwall · 1721 · low tide', 'The Pirate’s Cove',
    `<p>You followed an old map into a smugglers’ cave – and the tide has come in behind you. The way back is under water.</p><p>Somewhere in here, Captain Blackwater hid his treasure and his rowing boat. Find them both and row out through the sea gate before the tide fills the cave.</p><p>Level 1: perfect for families and first-time players.</p>`,
    'Dripping rock, a smell of salt and a parrot watching you. Look around.'],
  timesUp: ['The tide is in.', 'Water swirls around your ankles… but you can still finish.'],
  win: ['Out through the sea gate!', 'You row out into the sunshine with a chest of gold coins at your feet and a parrot on your shoulder squawking “White! Red! Black!” all the way home.'],
};

function openFlags() {
  if (F().flags) return E.say('White, red and black flap on the pole. The ship’s door is open.');
  E.cycler('Flagpole', 'Three flags on ropes, from the top down. Tap a flag to change its colour.', ['Top', 'Middle', 'Bottom'].map(n => ({ name: n, opts: FLAGS })), v => { if (v.join() !== 'White,Red,Black') return false; F().flags = 1; E.say('Creak! On the wreck, the cabin door swings open.'); return true; }, 'The flags flap. Nothing happens.', 'Hoist');
}
function openNav() {
  if (F().nav) return E.say('The navigator’s box is empty now.');
  E.numLock('Navigator’s box', 'A blue box with a gold compass on the lid and three number wheels.', 3, c => { if (c !== '731') return false; F().nav = 1; E.give('oil'); E.give('coinB'); E.say('The lid springs up: a bottle of lamp oil and the other half of the gold coin!'); return true; });
}
function openTreasure() {
  if (F().treasure) return E.say('The chest overflows with gold coins. You already took the oar.');
  if (!F().coinIn) return E.say('A huge treasure chest. It has a coin-shaped slot and a lock with four letter wheels. The slot is empty.');
  E.wordLock('Treasure chest', 'The name lock: four letter wheels under a carved wolf’s head.', 4, w => { if (w !== 'WOLF') return false; F().treasure = 1; E.give('oar'); E.say('The lid swings up: gold, pearls – and, strapped inside the lid, a painted oar!'); return true; });
}
});
