/* Six Clues escape room #26 – The Venetian Masquerade (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const palazzo = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 8 }, (_, i) => `<path d="M${i * 200 + 30} 640 V200 Q${i * 200 + 100} 100 ${i * 200 + 170} 200 V640" fill="${c2}"/>`).join('')}<rect y="640" width="1600" height="260" fill="#3a2a2a"/><ellipse cx="800" cy="0" rx="520" ry="300" fill="url(#lamp)"/>`;
const MASKS = ['Sun', 'Moon', 'Cat', 'Plague Doctor', 'Harlequin'];
const TURNS = ['Left', 'Right', 'Straight'];

return {
  start: 'ballroom', v: 1,
  items: {
    wheel: ['☸️', 'Cipher wheel', 'Two brass rings with the alphabet, one turning inside the other. Set to “+3”.'],
    archiveKey: ['🗝️', 'Archive key', 'A long key with a winged lion on the bow.'],
    letter: ['✉️', 'Sealed letter', 'A letter sealed with black wax – in code.'],
    chainKey: ['🔑', 'Gondola chain key', 'A small iron key for a mooring chain.'],
    map: ['🗺️', 'Canal route', 'A little sketch of a route through the canals.'],
  },
  rooms: {
    ballroom: {
      name: 'The ballroom of Palazzo Contarini',
      bg: () => palazzo('#4a1e2a', '#5a2634'),
      spots: [
        { id: 'harpsichord', x: 100, y: 380, w: 460, h: 260, art: () => `<rect x="120" y="440" width="420" height="160" fill="#2a1a10"/>${L(330, 640, 'Harpsichord')}`,
          act: () => { E.note('music', 'On the harpsichord: two pieces of music. One, crossed out in red ink: “B – A – D – E”. The other, signed by the composer: “The key to the mask room is the tune I end every song on: F – A – C – E.”'); E.say('Two sheets of music: “B – A – D – E” crossed out in red, and “F – A – C – E – the tune I end every song on”.'); } },
        { id: 'guests', x: 620, y: 120, w: 360, h: 300, art: () => `${E.paper(640, 140, 320, 240, 7)}${L(800, 420, 'Guest list')}`,
          act: () => { E.note('guests', 'Guest list for the masquerade: Count Morosini, Signora Bassi, Captain Ruiz of Spain, Doctor Falier, Signor Grimani. “All guests masked until midnight.”'); E.say('The guest list: Count Morosini, Signora Bassi, Captain Ruiz of Spain, Doctor Falier and Signor Grimani.'); } },
        { id: 'chandelier', x: 1040, y: 40, w: 300, h: 220, art: () => `<path d="M1190 60 v60 M1100 160 q90 60 180 0" stroke="#c9a24a" stroke-width="10" fill="none"/>${L(1190, 250, 'Chandelier')}`,
          act: () => E.say('A thousand candles. Someone tore the Doge’s letter from your hands under this very chandelier – and now the guards think you stole it.') },
        { id: 'toMasks', x: 1100, y: 340, w: 380, h: 300, art: () => `<rect x="1120" y="360" width="340" height="260" fill="#2a1a10"/>${L(1290, 650, F().masks ? 'Mask room (open)' : 'Mask room (letter lock)')}`, act: () => F().masks ? E.go('masks') : openMaskDoor() },
        { id: 'toArchive', x: 20, y: 740, w: 340, h: 130, art: () => E.exit(F().archive ? '← Archive' : '← Archive (locked)'), act: () => F().archive ? E.go('archive') : E.say('A heavy door with a winged lion carved on it. Locked.'),
          use: { archiveKey: () => { F().archive = 1; E.take('archiveKey'); E.say('The winged-lion key turns. Dusty air and old paper.'); return true; } } },
        { id: 'toDock', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Water gate →', 1240), act: () => E.go('dock') },
      ],
    },
    masks: {
      name: 'The mask room',
      bg: () => palazzo('#2a1e3a', '#342648'),
      spots: [
        { id: 'back', x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Ballroom'), act: () => E.go('ballroom') },
        { id: 'wall', x: 100, y: 100, w: 700, h: 320, art: () => `${MASKS.map((m, i) => `<ellipse cx="${170 + i * 135}" cy="240" rx="50" ry="70" fill="${['#e8c040', '#d8d8e8', '#2a2a2a', '#e8e0d0', '#c03040'][i]}"/>`).join('')}${L(450, 400, 'Wall of masks')}`,
          act: () => E.say('Sun, Moon, Cat, Plague Doctor and Harlequin masks hang on the wall. One hook is empty – the Plague Doctor’s.') },
        { id: 'ledger', x: 860, y: 120, w: 340, h: 280, art: () => `${E.paper(880, 140, 300, 220, 7)}${L(1030, 400, 'Mask maker’s order book')}`,
          act: () => { E.note('ledger', 'Mask maker’s order book: Count Morosini – Moon. Signora Bassi – Cat. Doctor Falier – Sun. Signor Grimani – Harlequin. “Stranger in black – Plague Doctor – paid in Spanish gold.”'); E.say('Orders: Morosini – Moon, Bassi – Cat, Falier – Sun, Grimani – Harlequin. And a stranger in black – Plague Doctor – paid in Spanish gold.'); } },
        { id: 'drawer', x: 300, y: 460, w: 420, h: 180, art: () => `<rect x="320" y="480" width="380" height="140" fill="#5a3a20"/>${L(510, 650, F().drawer ? 'Workbench drawer (open)' : 'Workbench drawer (mask lock)')}`, act: () => openDrawer() },
        { id: 'tools', x: 900, y: 440, w: 380, h: 200, art: () => `<rect x="920" y="480" width="340" height="120" fill="#4a3a2a"/>${L(1090, 640, 'Mask maker’s tools')}`,
          act: () => { if (F().wheel) return E.say('Brushes, feathers and gold leaf.'); F().wheel = 1; E.give('wheel'); E.say('Among the brushes and feathers: a brass cipher wheel, set to “+3”.'); } },
      ],
    },
    archive: {
      name: 'The archive',
      bg: () => palazzo('#2a2a1e', '#343426'),
      spots: [
        { id: 'back', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Ballroom →', 1240), act: () => E.go('ballroom') },
        { id: 'desk', x: 100, y: 380, w: 460, h: 260, art: () => `<rect x="120" y="440" width="420" height="30" fill="#5a3a20"/>${E.paper(220, 400, 220, 50, 2)}${L(330, 650, 'Desk – a sealed letter')}`,
          act: () => { if (F().letterTaken) return E.say('The desk is bare.'); F().letterTaken = 1; E.give('letter'); E.say('On the desk: a letter sealed with black wax – the stolen letter! It is written in code.'); } },
        { id: 'portrait', x: 640, y: 100, w: 340, h: 380, art: () => `<rect x="660" y="120" width="300" height="320" fill="#4a3a2a" stroke="#c9a24a" stroke-width="10"/>${L(810, 470, 'Portrait of the Doge')}`,
          act: () => E.say('The Doge in his golden cap. On the frame: “Francesco Loredan, Doge of Venice, 1752–1762”.') },
        { id: 'box', x: 1060, y: 300, w: 360, h: 300, art: () => `<rect x="1080" y="320" width="320" height="240" fill="#6a2a1a" stroke="#c9a24a" stroke-width="6"/>${L(1240, 590, F().box ? 'Strongbox (open)' : 'Strongbox (letter lock)')}`, act: () => openBox() },
      ],
    },
    dock: {
      name: 'The water gate',
      bg: () => `<rect width="1600" height="900" fill="#141e2e"/><rect y="520" width="1600" height="380" fill="#1e3a4a"/>${Array.from({ length: 6 }, (_, i) => `<rect x="${i * 300}" y="200" width="20" height="320" fill="#4a3a5a"/>`).join('')}`,
      spots: [
        { id: 'back', x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Ballroom'), act: () => E.go('ballroom') },
        { id: 'gondola', x: 520, y: 460, w: 620, h: 200, art: () => `<path d="M540 560 Q840 660 1120 520 L1100 600 Q840 700 560 600z" fill="#111"/>${L(830, 680, 'Gondola, chained')}`, act: () => openGondola(),
          use: { chainKey: () => { F().chain = 1; E.take('chainKey'); E.say('The chain falls into the water with a splash. The gondola is free.'); return true; } } },
        { id: 'bell', x: 1200, y: 80, w: 300, h: 300, art: () => `<path d="M1300 120 Q1350 100 1400 120 L1420 260 H1280z" fill="#c9a24a"/>${L(1350, 300, 'Church bell across the canal')}`,
          act: () => E.say('Across the canal, the church clock says a quarter to midnight. At midnight, the masks come off – and the guards come for you.') },
      ],
    },
  },
  combine: (a, b) => { if ([a, b].sort().join() === 'letter,wheel') { F().decoded = 1; E.note('decoded', 'Decoded with the cipher wheel (+3): “THE DOCTOR TAKES THE FLEET PLANS TO THE SPANISH SHIP AT DAWN.” Underneath, a second line: “Strongbox word: the mask he wears.”'); E.say('With the cipher wheel the letter reads: “THE DOCTOR TAKES THE FLEET PLANS TO THE SPANISH SHIP AT DAWN.” And: “Strongbox word: the mask he wears.”'); return true; } return false; },
  stages: [
    ['masks', () => F().masks, ['The mask room door has a letter lock.', 'The harpsichord music – but one sheet is crossed out.', 'FACE.']],
    ['drawer', () => F().drawer, ['The workbench drawer has a mask lock.', 'Who paid in Spanish gold? Which mask is missing?', 'The Plague Doctor.']],
    ['archive', () => F().archive, ['The drawer gave you a winged-lion key.', 'The archive door has a winged lion.', 'Use the archive key on the archive door.']],
    ['decoded', () => F().decoded, ['The stolen letter is in code.', 'You found a cipher wheel in the mask room.', 'Combine the letter and the cipher wheel.']],
    ['box', () => F().box, ['The strongbox wants a word.', 'The letter says: the mask he wears.', 'DOCTOR – six letters.']],
    ['chain', () => F().chain, ['The gondola is chained.', 'The strongbox had a small iron key.', 'Use the gondola chain key on the gondola.']],
    ['route', () => F().won, ['Now the route through the canals.', 'The map from the strongbox.', 'Left, Right, Straight.']],
  ],
  intro: ['Venice · Carnival night · 23:00 · 1756', 'The Venetian Masquerade',
    `<p>You are a page at the great masquerade ball in Palazzo Contarini. You were carrying a sealed letter for the Doge – and under the chandelier, a masked guest tore it from your hands. Now the guards think <i>you</i> stole it.</p><p>At midnight the masks come off and you will be arrested. Find out which guest is the spy, recover the letter and escape by gondola to the Doge’s palace before the bells ring twelve.</p><p>Level 2: one tune is crossed out, and every guest hides behind a mask.</p>`,
    'Candles, violins and a hundred masks. Look around.'],
  timesUp: ['Midnight bells.', 'The masks come off… you can still finish, but off the leaderboard.'],
  win: ['To the Doge!', 'The gondola slides out of the water gate and through the dark canals – left, right, straight on – to the Doge’s palace. By dawn the Spanish ship is searched, and the stranger in the Plague Doctor mask is unmasked: Captain Ruiz of Spain. You are made a captain of the guard.'],
};

function openMaskDoor() {
  E.wordLock('Mask room door', 'A brass lock with four letter wheels shaped like musical notes.', 4, w => { if (w !== 'FACE') return false; F().masks = 1; E.say('The note-wheels click. The mask room door opens.'); return true; });
}
function openDrawer() {
  if (F().drawer) return E.say('The drawer is empty now.');
  E.cycler('Workbench drawer', 'A lock with a little turning picture of a mask. “Show me the face of the one who paid in foreign gold.”', [{ name: 'Mask', opts: MASKS }], v => { if (v[0] !== 'Plague Doctor') return false; F().drawer = 1; E.give('archiveKey'); E.say('The drawer opens: a long key with a winged lion on it.'); return true; }, 'The drawer stays shut.', 'Turn');
}
function openBox() {
  if (F().box) return E.say('The strongbox is empty now.');
  if (!F().decoded) return E.say('An iron strongbox with six letter wheels. You have no idea what word it wants – yet.');
  E.wordLock('Strongbox', 'Six letter wheels.', 6, w => { if (w !== 'DOCTOR') return false; F().box = 1; E.give('chainKey'); E.give('map'); E.note('route', 'Map from the strongbox: “From the water gate to the Doge’s palace: LEFT at the bridge, RIGHT at the church, STRAIGHT on to the lagoon.”'); E.say('Inside: a small iron key and a route through the canals: left at the bridge, right at the church, straight on.'); return true; });
}
function openGondola() {
  if (!F().chain) return E.say('A black gondola, chained to the mooring post with a padlock.');
  if (!E.has('letter') || !F().decoded) return E.say('You could row away – but without the letter and its secret, the guards will never believe you.');
  E.cycler('The canals', 'Which way at each turning?', ['The bridge', 'The church', 'The square'].map(n => ({ name: n, opts: TURNS })), v => { if (v.join() !== 'Left,Right,Straight') return false; E.win(); return true; }, 'A dead end! You row back to the water gate.', 'Row');
}
});
