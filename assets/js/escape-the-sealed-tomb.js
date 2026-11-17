/* Six Clues escape room #6 – The Sealed Tomb (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const SIGNS = [['🦅', 'A'], ['🦶', 'B'], ['🐍', 'F'], ['🦁', 'L'], ['🦉', 'M'], ['🌊', 'N'], ['👄', 'R'], ['🍞', 'T'], ['🐤', 'U']];
const CARTOUCHE = ['🍞', '🦅', '🦉', '🐤', '🌊'];
const HEADS = ['Human', 'Baboon', 'Jackal', 'Falcon'];
const stone = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 8 }, (_, r) => Array.from({ length: 9 }, (_, c) => `<rect x="${c * 180 + (r % 2) * 90}" y="${r * 84}" width="174" height="78" fill="${c2}"/>`).join('')).join('')}<rect y="660" width="1600" height="240" fill="#2a2016"/><ellipse cx="800" cy="0" rx="560" ry="360" fill="url(#lamp)"/>`;
const egNum = n => '➰'.repeat(Math.floor(n / 100)) + '∩'.repeat(Math.floor(n % 100 / 10)) + '|'.repeat(n % 10);

return {
  start: 'corridor', v: 1,
  items: {
    camera: ['📷', 'Camera & flash', 'Your folding camera with a magnesium flash tray. One flash left.'],
    crowbar: ['🪛', 'Crowbar', 'A workman’s iron crowbar from the rubble.'],
    scarab: ['🪲', 'Heart scarab', 'A green stone scarab, the kind laid over a mummy’s heart.'],
    ankh: ['☥', 'Bronze ankh', 'A heavy bronze ankh, shaped like a key.'],
    rope: ['🪢', 'Rope', 'Thirty feet of good rope from the workmen’s baskets.'],
  },
  rooms: {
    corridor: {
      name: 'The descending corridor',
      bg: () => stone('#6a5236', '#735a3c'),
      spots: [
        { id: 'bag', x: 60, y: 520, w: 260, h: 150, art: () => `<rect x="80" y="560" width="220" height="100" rx="14" fill="#5a3a22"/>${L(190, 690, 'Your camera bag')}`, act: () => openBag() },
        { id: 'board', x: 380, y: 160, w: 300, h: 260, art: () => `<rect x="390" y="170" width="280" height="220" fill="#222" stroke="#6b4a2a" stroke-width="10"/><text x="530" y="300" text-anchor="middle" font-size="44" fill="#ddd">${egNum(254)}</text>${L(530, 430, 'Foreman’s chalk board')}`,
          act: () => { E.note('board', 'Foreman’s chalk board: “Gate code – written the old way so the diggers can’t read it:” ➰➰ ∩∩∩∩∩ ||||'); E.modal(`<h2>Foreman’s chalk board</h2><p class="paper">Gate code – written the old way, so the diggers can’t read it:</p><p style="font-size:2.6rem;text-align:center;letter-spacing:.2em">➰➰ ∩∩∩∩∩ ||||</p>`); } },
        { id: 'rubble', x: 720, y: 500, w: 360, h: 170, art: () => `<path d="M720 670 Q800 520 900 560 Q980 500 1080 670z" fill="#8a7050"/>${L(900, 700, 'Rubble')}`,
          act: () => { if (F().crowbar) return E.say('Limestone chips and dust.'); F().crowbar = 1; E.give('crowbar'); E.say('Under the chips, a workman’s crowbar.'); } },
        { id: 'entrance', x: 40, y: 40, w: 280, h: 300, art: () => `<rect x="60" y="60" width="240" height="260" fill="#2a2016"/>${L(180, 360, 'Sealed entrance')}`,
          act: () => E.say('Somebody has rolled a slab across the entrance from outside. Through a crack you hear a lorry drive away. Your lamp has about an hour of oil.') },
        { id: 'toAnte', x: 1200, y: 120, w: 340, h: 540, art: () => `<rect x="1220" y="140" width="300" height="500" fill="#140d08"/>${F().gate ? '' : Array.from({ length: 6 }, (_, i) => `<line x1="${1240 + i * 52}" y1="140" x2="${1240 + i * 52}" y2="640" stroke="#555" stroke-width="10"/>`).join('')}${L(1370, 120, F().gate ? 'Antechamber →' : 'Iron gate (padlock)')}`,
          act: () => F().gate ? E.go('ante') : E.numLock('Expedition padlock', 'The expedition’s own iron gate, with a three-figure padlock.', 3, c => { if (c !== '254') return false; F().gate = 1; E.say('The padlock clicks. The iron gate swings into the dark antechamber.'); return true; }) },
      ],
    },
    ante: {
      name: 'The antechamber',
      bg: () => stone('#5a4630', '#634d34'),
      spots: [
        { id: 'back', x: 20, y: 740, w: 280, h: 130, art: () => E.exit('← Corridor'), act: () => E.go('corridor') },
        { id: 'mural', x: 60, y: 80, w: 520, h: 300, art: () => `<rect x="70" y="90" width="500" height="260" fill="#c8a870"/>${HEADS.map((h, i) => `<circle cx="${140 + i * 120}" cy="200" r="40" fill="#5a3a22"/><text x="${140 + i * 120}" y="300" text-anchor="middle" font-size="22" fill="#3a2a1a">${h}</text>`).join('')}${L(320, 400, 'Painted wall')}`, act: () => openMural() },
        { id: 'chest', x: 620, y: 400, w: 400, h: 260, art: () => `<rect x="650" y="460" width="340" height="180" fill="#8a6a2a" stroke="#c9a24a" stroke-width="6"/>${[0, 1, 2, 3].map(i => `<rect x="${670 + i * 80}" y="400" width="44" height="60" rx="16" fill="#d8ccb0"/>`).join('')}${L(820, 690, 'Gilded chest & four jars')}`, act: () => openJars() },
        { id: 'baskets', x: 1060, y: 480, w: 240, h: 180, art: () => `<ellipse cx="1180" cy="600" rx="100" ry="50" fill="#a08050"/>${L(1180, 690, 'Workmen’s baskets')}`,
          act: () => { if (F().rope) return E.say('Empty baskets.'); F().rope = 1; E.give('rope'); E.say('In the bottom basket: thirty feet of good rope.'); } },
        { id: 'note', x: 640, y: 120, w: 260, h: 220, art: () => `${E.paper(660, 140, 220, 170, 5)}${L(770, 350, 'Dr Crane’s notes')}`, act: () => openCrane() },
        { id: 'toBurial', x: 1320, y: 120, w: 260, h: 540, art: () => `<rect x="1340" y="140" width="220" height="500" fill="${F().burialOpen ? '#140d08' : '#7a6040'}"/><rect x="1380" y="250" width="140" height="70" rx="35" fill="none" stroke="#3a2a1a" stroke-width="5"/>${L(1450, 120, F().burialOpen ? 'Burial chamber →' : 'Sealed door with cartouche')}`,
          act: () => F().burialOpen ? E.go('burial') : openCartouche() },
      ],
    },
    burial: {
      name: 'The burial chamber',
      bg: () => stone('#3a2c20', '#433224'),
      spots: [
        { id: 'back', x: 20, y: 740, w: 280, h: 130, art: () => E.exit('← Antechamber'), act: () => E.go('ante') },
        { id: 'ceiling', x: 300, y: 20, w: 1000, h: 200, art: () => `<rect x="300" y="20" width="1000" height="180" fill="${F().flashed ? '#1a2a5a' : '#1a140e'}"/>${L(800, 240, F().flashed ? 'Painted ceiling' : 'Dark ceiling')}`, act: () => openCeiling(),
          use: { camera: () => { F().flashed = 1; E.take('camera'); E.note('ceiling', 'In the magnesium flash the ceiling shows the sun’s boat on its journey: a scarab rising at dawn, a falcon at noon, an old man at dusk, and the sky-goddess Nut swallowing the sun at night. An arrow points to the treasury: “the workmen’s way – behind the one who guards”.'); E.say('FLASH! For a second the whole ceiling blazes with paint: the sun’s journey in four pictures – and a painted arrow pointing toward the treasury.'); return true; } } },
        { id: 'sarcophagus', x: 500, y: 380, w: 600, h: 280, art: () => `<rect x="520" y="440" width="560" height="200" rx="40" fill="#8a7a5a" stroke="#3a2a1a" stroke-width="6"/>${L(800, 690, F().lid ? 'Sarcophagus (open)' : 'Sarcophagus')}`,
          act: () => F().lid ? openPapyrus() : E.say('A granite sarcophagus. The lid has been moved before – there is a gap you could get something into.'),
          use: { crowbar: () => { F().lid = 1; E.take('crowbar'); E.give('scarab'); E.say('You lever the lid aside. On the linen-wrapped king lies a green heart scarab – and a rolled papyrus.'); return true; } } },
        { id: 'fresco', x: 1140, y: 240, w: 300, h: 300, art: () => `<rect x="1150" y="250" width="280" height="260" fill="#c8a870"/><line x1="1290" y1="300" x2="1290" y2="460" stroke="#3a2a1a" stroke-width="6"/><line x1="1220" y1="320" x2="1360" y2="320" stroke="#3a2a1a" stroke-width="6"/>${L(1290, 560, 'Fresco of the scales')}`,
          act: () => { E.note('fresco', 'Fresco: Anubis weighs a heart against a feather. The expedition’s catalogue card: “Wall B – the Hall of Two Truths. Book of the Dead, spell 125.”'); E.modal(`<h2>Fresco of the scales</h2><p>Jackal-headed Anubis weighs a heart against a single feather; ibis-headed Thoth writes down the result.</p><p class="paper">Expedition catalogue card, pinned below: <i>Wall B – the Hall of Two Truths. Book of the Dead, spell 125.</i></p>`); } },
        { id: 'toTreasury', x: 40, y: 260, w: 220, h: 400, art: () => `<rect x="60" y="280" width="180" height="360" fill="${F().treasury ? '#140d08' : '#6a5236'}"/>${L(150, 260, F().treasury ? '← Treasury' : 'Low door (numbered lock)')}`,
          act: () => F().treasury ? E.go('treasury') : E.numLock('Treasury door', 'A bronze lock with three number wheels, cut in the shape of a feather. Scratched beside it: <i>“The spell of the scales.”</i>', 3, c => { if (c !== '125') return false; F().treasury = 1; E.say('The bronze feather turns. The low door to the treasury grinds open.'); return true; }) },
      ],
    },
    treasury: {
      name: 'The treasury',
      bg: () => stone('#4a3a22', '#54412a'),
      spots: [
        { id: 'back', x: 1340, y: 740, w: 250, h: 130, art: () => E.exit('Burial chamber →', 1360), act: () => E.go('burial') },
        { id: 'scale', x: 120, y: 300, w: 320, h: 360, art: () => `<line x1="280" y1="320" x2="280" y2="640" stroke="#c9a24a" stroke-width="10"/><line x1="160" y1="360" x2="400" y2="${F().weighed ? 360 : 330}" stroke="#c9a24a" stroke-width="8"/>${L(280, 690, 'Golden scales')}`,
          act: () => E.say(F().weighed ? 'The scales hang level: heart against feather.' : 'Golden scales. On one pan lies a golden feather. The other pan is empty – it is shaped to hold something small and oval.'),
          use: { scarab: () => { F().weighed = 1; E.take('scarab'); E.give('ankh'); E.say('You lay the heart scarab on the empty pan. Heart and feather balance – and a drawer in the base slides open: a heavy bronze ankh.'); return true; } } },
        { id: 'gold', x: 500, y: 420, w: 360, h: 240, art: () => `<ellipse cx="680" cy="600" rx="160" ry="50" fill="#c9a24a"/>${L(680, 690, 'Treasure')}`,
          act: () => E.say('Gold, alabaster, a gilded chariot wheel. Beautiful – and no use at all if you never get out.') },
        { id: 'anubis', x: 960, y: 140, w: 340, h: 520, art: () => `<rect x="1000" y="420" width="260" height="220" fill="#1a1410"/><path d="M1060 420 L1080 220 L1110 160 L1150 220 L1200 420z" fill="#111"/>${L(1130, 690, F().anubis ? 'Anubis (turned aside)' : 'Statue of Anubis')}`,
          act: () => F().anubis ? openShaft() : E.say('A black Anubis on a shrine, guarding the treasury. In its base: a keyhole shaped like a loop on a cross.'),
          use: { ankh: () => { F().anubis = 1; E.take('ankh'); E.say('The ankh fits. With a groan of stone the whole shrine swings aside – behind it, a narrow workmen’s shaft and a panel of four carved pictures.'); return true; }, rope: () => { if (!F().shaftOpen) return false; E.take('rope'); E.win(); return true; } } },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['gate', () => F().gate, ['The gate code is on the foreman’s board – in ancient numbers.', 'Your camera bag has a card about Egyptian numerals.', 'Two coils = 200, five heels = 50, four strokes = 4: 254.']],
    ['jars', () => F().scarabChest, ['The four jars belong on the four sides of the chest.', 'The painted wall names each son of Horus and the direction he guards.', 'North baboon, East jackal, South human, West falcon.']],
    ['cartouche', () => F().burialOpen, ['The door wants the king’s name. It is written in a cartouche.', 'Use the sign alphabet in your handbook, not Dr Crane’s notes – the expedition handbook is the trusted one.', 'Bread T, vulture A, owl M, chick U, water N: TAMUN.']],
    ['lid', () => F().lid, ['The sarcophagus lid has a gap.', 'You found a tool in the corridor rubble.', 'Use the crowbar on the sarcophagus.']],
    ['treasury', () => F().treasury, ['The treasury lock wants “the spell of the scales”.', 'The fresco of the scales has a catalogue card.', 'Book of the Dead, spell 125.']],
    ['weigh', () => F().weighed, ['The golden scales have an empty pan for something small and oval.', 'You took something from the king’s chest – his heart, in stone.', 'Use the heart scarab on the scales.']],
    ['flash', () => F().flashed, ['The burial chamber ceiling is too dark to see.', 'You have one flash left in your camera.', 'Use the camera on the ceiling.']],
    ['anubis', () => F().anubis, ['The ceiling arrow says “behind the one who guards”.', 'Anubis guards the treasury. His base has a keyhole like a loop on a cross.', 'Use the bronze ankh on the Anubis statue.']],
    ['sun', () => F().shaftOpen, ['The shaft panel shows four pictures. The ceiling showed the order.', 'The sun’s journey: dawn, noon, dusk, night.', 'Scarab, falcon, old man, Nut.']],
    ['rope', () => F().won, ['The shaft is too deep to climb bare-handed.', 'Something from the antechamber baskets.', 'Use the rope on the shaft behind Anubis.']],
  ],
  intro: ['Valley of the Kings · 26 November 1922 · 23:00', 'The Sealed Tomb',
    `<p>You are the photographer of a small British expedition. Tonight you went back down alone to photograph the newly opened tomb of a forgotten king – and someone rolled the slab back over the entrance behind you.</p><p>Outside, a lorry drives off. Your oil lamp has about one hour left. Somewhere in this tomb the workmen of three thousand years ago left another way out.</p><p>Level 2: not every translation down here is honest.</p>`,
    'Dust settles in the lamplight. Painted walls slope down into the dark. Look around.'],
  timesUp: ['The lamp gutters out.', 'Darkness. Hours later, the expedition finds you, very cross and very thirsty – and the rival expedition has already cabled the newspapers.'],
  win: ['Out under the stars', 'You climb the workmen’s shaft and come up behind the hill, under a sky full of stars. By dawn the police have stopped Dr Crane’s lorry on the Luxor road, and your photographs of the painted ceiling make every front page in London.'],
};

function openBag() {
  if (!F().bag) { F().bag = 1; E.give('camera'); }
  E.note('handbook', 'Expedition handbook: numerals | = 1, ∩ (heel bone) = 10, ➰ (coil of rope) = 100. Sign alphabet: ' + SIGNS.map(s => s.join(' = ')).join(', ') + '.');
  E.modal(`<h2>Your camera bag</h2><p>Your camera with one magnesium flash left, and the expedition handbook.</p><h3>Egyptian numerals</h3><p class="paper" style="font-size:1.3rem">| = 1 · ∩ = 10 · ➰ = 100</p><h3>Sign alphabet</h3><p class="paper" style="font-size:1.3rem">${SIGNS.map(s => `${s[0]} = ${s[1]}`).join(' · ')}</p>`);
}
function openMural() {
  E.note('mural', 'Painted wall – the four sons of Horus: Hapy (baboon) guards the north, Duamutef (jackal) the east, Imsety (human) the south, Qebehsenuef (falcon) the west.');
  E.modal(`<h2>The four sons of Horus</h2><p class="paper">Hapy, baboon-headed, keeps the lungs and faces the <b>north</b>.<br>Duamutef, jackal-headed, keeps the stomach and faces the <b>east</b>.<br>Imsety, human-headed, keeps the liver and faces the <b>south</b>.<br>Qebehsenuef, falcon-headed, keeps the intestines and faces the <b>west</b>.</p>`);
}
function openJars() {
  if (F().scarabChest) return E.say('The gilded chest stands open and empty, the four jars in their places.');
  E.cycler('Gilded chest', 'Four canopic jars with carved lids, and a recess on each side of the chest marked with the four winds.', [{ name: 'North', opts: HEADS }, { name: 'East', opts: HEADS }, { name: 'South', opts: HEADS }, { name: 'West', opts: HEADS }], v => {
    if (v.join() !== 'Baboon,Jackal,Human,Falcon') return false; F().scarabChest = 1; E.say('As the fourth jar settles, the gilded lid lifts a finger’s width. Inside: nothing but dust – and a draught from the sealed door. The cartouche on that door is lit for the first time.'); return true;
  }, 'The jars rock in their recesses. Nothing happens.', 'Set the jars');
}
function openCrane() {
  E.note('crane', 'Dr Crane’s notes (the rival expedition): his own sign list – 🍞 = P, 🦅 = A, 🦉 = M, 🐤 = U, 🌊 = N – “the king is PAMUN, I am certain.”');
  E.modal(`<h2>Dr Crane’s notes</h2><p class="paper">My own reading of the signs: 🍞 = P · 🦅 = A · 🦉 = M · 🐤 = U · 🌊 = N.<br>The king is PAMUN, I am certain of it. The handbook men are amateurs.</p><p class="small">Dr Crane leads the rival expedition. What is his notebook doing down here?</p>`);
}
function openCartouche() {
  if (!F().scarabChest) return E.say('A sealed door with a cartouche – but the paint is so faint in this light you can’t make out the signs. Something here must be set right first.');
  E.wordLock('The sealed door', `The cartouche on the door reads: <span style="font-size:2rem">${CARTOUCHE.join(' ')}</span><br>Below it, five letter wheels.`, 5, w => {
    if (w === 'PAMUN') { E.say('Nothing. Dr Crane’s reading is wrong – or deliberately misleading.'); return false; }
    if (w !== 'TAMUN') return false; F().burialOpen = 1; E.say('TAMUN. The seal cracks, and the door swings inward on stone pivots.'); return true;
  });
}
function openCeiling() {
  if (!F().flashed) return E.say('The ceiling is lost in darkness. Your lamp doesn’t reach that far.');
  E.modal(`<h2>The painted ceiling</h2><p>The sun’s boat sails across the sky: a <b>scarab</b> pushing the sun up at dawn, a <b>falcon</b> at noon, an <b>old man</b> leaning on a stick at dusk, and the sky-goddess <b>Nut</b> swallowing the sun at night.</p><p class="small">A painted arrow points toward the treasury: “the workmen’s way – behind the one who guards”.</p>`);
}
function openPapyrus() {
  E.note('papyrus', 'Papyrus from the sarcophagus: “Let the heart be weighed in the Hall of Two Truths, and if it is light as the feather, the way will open.”');
  E.modal(`<h2>The papyrus</h2><p class="paper">Let the heart be weighed in the Hall of Two Truths. If it is light as the feather, the way will open for him who comes after.</p>`);
}
function openShaft() {
  if (F().shaftOpen) return E.say('The shaft climbs steeply into the dark. Far above, a breath of night air. You need something to climb with.');
  E.orderer('Panel of the sun', 'Four carved pictures, each a button.', ['Nut', 'Falcon', 'Scarab', 'Old man'], o => { if (o.join() !== 'Scarab,Falcon,Old man,Nut') return false; F().shaftOpen = 1; E.say('The last stone sinks in. A grate at the bottom of the shaft drops away – fresh air! The shaft is deep and smooth-sided.'); return true; }, 'The stones spring back out.');
}
});
