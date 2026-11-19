/* Six Clues escape room #18 – The Inventor's Laboratory (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const brick = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 22 }, (_, r) => `<rect x="${r % 2 ? 0 : -60}" y="${r * 30}" width="1700" height="2" fill="${c2}"/>`).join('')}<rect y="660" width="1600" height="240" fill="#2a1e16"/><ellipse cx="800" cy="0" rx="500" ry="300" fill="url(#lamp)"/>`;
const CARDS = ['Card A', 'Card B', 'Card C', 'Card D'];
const LAMPS = ['Red', 'Yellow', 'Green', 'Blue', 'Violet'];
const COGS = ['12 teeth', '24 teeth', '36 teeth'];

return {
  start: 'workshop', v: 2,
  items: {
    brass: ['⚙️', 'Brass cog', 'A small brass cog with 12 teeth.'],
    silver: ['⚙️', 'Silver cog', 'A middle-sized silver cog with 24 teeth.'],
    copper: ['⚙️', 'Copper cog', 'A big copper cog with 36 teeth.'],
    roofKey: ['🗝️', 'Roof key', 'An iron key with a tiny lightning bolt on it.'],
    cable: ['➰', 'Copper cable', 'A thick coil of copper cable with a clamp.'],
  },
  rooms: {
    workshop: {
      name: 'The workshop',
      bg: () => brick('#3a2418', '#2a1810'),
      spots: [
        { id: 'automaton', photo: [220, 165, 165, 640], x: 80, y: 160, w: 300, h: 460, art: () => `<rect x="150" y="260" width="160" height="300" rx="20" fill="#b08a40"/><circle cx="230" cy="220" r="50" fill="#c9a24a"/>${L(230, 600, 'Brass automaton')}`, act: () => openAutomaton() },
        { id: 'diagram', photo: [365, 125, 275, 210], x: 420, y: 100, w: 340, h: 260, art: () => `${E.paper(440, 120, 300, 200, 5)}${L(590, 360, 'Diagram on the wall')}`,
          act: () => { E.note('diagram', 'Wall diagram: “Automaton – feeding card: holes in the first and last rows only, never the middle.” Sketch of a card with two rows of holes, top and bottom.'); E.say('A diagram of the automaton’s punch card: holes in the top and bottom rows only, never the middle.'); } },
        { id: 'gears', photo: [645, 150, 395, 250], x: 800, y: 140, w: 440, h: 380, art: () => `<rect x="820" y="160" width="400" height="320" fill="#4a3a2a"/>${[0, 1, 2].map(i => `<circle cx="${900 + i * 120}" cy="320" r="${30 + i * 15}" fill="none" stroke="#c9a24a" stroke-width="6"/>`).join('')}${L(1020, 520, F().gears ? 'Gear board (complete)' : 'Gear board – three empty pegs')}`, act: () => openGears(),
          use: { brass: () => put('brass'), silver: () => put('silver'), copper: () => put('copper') } },
        { id: 'crate', photo: [1040, 585, 325, 215], x: 1280, y: 420, w: 280, h: 220, art: () => `<rect x="1300" y="460" width="240" height="160" fill="#7a5a30"/>${L(1420, 660, 'Packing crate')}`,
          act: () => { if (F().crate) return E.say('Straw and an invoice from a London electrical company.'); F().crate = 1; E.give('cable'); E.say('In the straw: a thick coil of copper cable with a clamp.'); } },
        { id: 'manual', photo: [1110, 270, 255, 145], x: 1280, y: 120, w: 280, h: 240, art: () => `${E.paper(1300, 140, 240, 180, 5)}${L(1420, 350, 'Engine manual')}`,
          act: () => { E.note('manual', 'Engine manual, page 3: “The great door opens when lightning drives the gears. Biggest cog on the left peg, then middle, then smallest on the right – big turns small, never the other way.”'); E.say('“Biggest cog on the left peg, then middle, then smallest on the right – big turns small.”'); } },
        { id: 'door', photo: [690, 420, 300, 335], x: 520, y: 400, w: 240, h: 260, art: () => `<rect x="540" y="420" width="200" height="220" fill="#2a2a2a" stroke="#c9a24a" stroke-width="8"/>${L(640, 660, 'The great door')}`, act: () => openDoor() },
        { id: 'toStudy', photo: [0, 55, 180, 800], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Study'), act: () => E.go('study') },
        { id: 'toGreen', photo: [1405, 105, 195, 710], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Greenhouse →', 1240), act: () => E.go('green') },
      ],
    },
    study: {
      name: 'The professor’s study',
      bg: () => brick('#2a1e2a', '#20161e'),
      spots: [
        { id: 'back', photo: [1385, 55, 215, 800], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Workshop →', 1240), act: () => E.go('workshop') },
        { id: 'desk', photo: [40, 490, 600, 310], x: 100, y: 400, w: 440, h: 240, art: () => `<rect x="120" y="440" width="400" height="30" fill="#5a3a20"/><rect x="140" y="470" width="360" height="140" fill="#4a2e1a"/>${L(320, 650, F().desk ? 'Desk (open)' : 'Desk – the drawer has a word lock')}`, act: () => openDesk() },
        { id: 'portrait', photo: [725, 0, 395, 405], x: 600, y: 100, w: 320, h: 380, art: () => `<rect x="620" y="120" width="280" height="320" fill="#4a3a2a" stroke="#c9a24a" stroke-width="10"/>${L(760, 470, 'Portrait of the professor')}`,
          act: () => { E.note('portrait', 'Portrait: “Prof. Ada Thornbury, inventor.” In her hand: a letter that reads “My password grows in my greenhouse.”'); E.say('“Prof. Ada Thornbury, inventor.” The painted letter in her hand says: “My password grows in my greenhouse.”'); } },
        { id: 'rival', photo: [1180, 100, 145, 200], x: 980, y: 140, w: 420, h: 260, art: () => `${E.paper(1000, 160, 380, 200, 6)}${L(1190, 400, 'Threatening letter')}`,
          act: () => { E.note('rival', 'Letter from her rival, Mr Crake: “Your machine is mine, Ada. At midnight my men come for it. Your door will not open in time.”'); E.say('From her rival, Mr Crake: “At midnight my men come for your machine.”'); } },
        { id: 'globe', photo: [1105, 375, 270, 450], x: 1000, y: 440, w: 300, h: 200, art: () => `<circle cx="1150" cy="520" r="70" fill="#3a6a8a"/>${L(1150, 630, 'Globe')}`,
          act: () => E.say('A globe with a pencil line from London to New York: “Demonstration, Jan. 1896”.') },
      ],
    },
    green: {
      name: 'The greenhouse',
      bg: () => `<rect width="1600" height="900" fill="#1e3a2a"/>${Array.from({ length: 9 }, (_, i) => `<rect x="${i * 180}" y="0" width="8" height="660" fill="#8a9a8a"/>`).join('')}<rect y="660" width="1600" height="240" fill="#3a2a1a"/>`,
      spots: [
        { id: 'back', photo: [0, 0, 200, 865], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Workshop'), act: () => E.go('workshop') },
        { id: 'labels', photo: [240, 420, 335, 180], x: 100, y: 360, w: 540, h: 260, art: () => `${[0, 1, 2, 3].map(i => `<rect x="${130 + i * 130}" y="460" width="90" height="120" fill="#6a4a2a"/><circle cx="${175 + i * 130}" cy="430" r="40" fill="#3a8a3a"/>`).join('')}${L(370, 620, 'Pots with labels')}`,
          act: () => { E.note('labels', 'Plant pots in a row, left to right: Valerian · Orchid · Lavender · Thyme. “My password grows in my greenhouse” – first letters?'); E.say('Four pots, left to right: Valerian, Orchid, Lavender, Thyme.'); } },
        { id: 'lamps', photo: [565, 65, 540, 200], x: 700, y: 80, w: 440, h: 260, art: () => `${[0, 1, 2].map(i => `<circle cx="${800 + i * 120}" cy="200" r="40" fill="#e8e0a0"/>`).join('')}${L(920, 320, 'Three growing lamps')}`, act: () => openLamps() },
        { id: 'notebook', photo: [1190, 370, 200, 120], x: 1200, y: 120, w: 320, h: 240, art: () => `${E.paper(1220, 140, 280, 180, 5)}${L(1360, 360, 'Gardening notebook')}`,
          act: () => { E.note('garden', 'Gardening notebook: “The great flytrap wakes only under red, then green, then blue light – left to right. Do NOT use violet, it sulks for a week.”'); E.say('“The great flytrap wakes only under red, then green, then blue light – left to right.”'); } },
        { id: 'flytrap', photo: [600, 360, 505, 425], x: 760, y: 380, w: 380, h: 260, art: () => `<path d="M950 600 Q850 420 950 380 Q1050 420 950 600z" fill="#3a9a3a"/>${L(950, 640, F().lamps ? 'Giant flytrap (open)' : 'Giant flytrap (shut tight)')}`,
          act: () => F().lamps ? E.say('The flytrap yawns open, empty now.') : E.say('A flytrap as big as a dog, shut tight. Something glints between its teeth.') },
        { id: 'toRoof', photo: [1390, 0, 210, 890], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit(F().roof ? 'Roof ladder ↑' : 'Roof hatch (locked)', 1240), act: () => F().roof ? E.go('roof') : E.say('An iron ladder to a locked roof hatch with a lightning bolt on it.'),
          use: { roofKey: () => { F().roof = 1; E.take('roofKey'); E.say('The roof hatch opens. Rain and thunder pour in.'); return true; } } },
      ],
    },
    roof: {
      name: 'The roof',
      bg: () => `<rect width="1600" height="900" fill="#141a26"/><path d="M0 660 L400 400 L800 660 L1200 380 L1600 660 V900 H0z" fill="#2a2a30"/><path d="M1300 0 L1240 140 L1290 140 L1220 300" stroke="#e8e0a0" stroke-width="8" fill="none"/>`,
      spots: [
        { id: 'down', photo: [15, 480, 505, 400], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('↓ Greenhouse'), act: () => E.go('green') },
        { id: 'rod', photo: [1335, 20, 195, 760], x: 1100, y: 80, w: 260, h: 520, art: () => `<rect x="1220" y="100" width="16" height="440" fill="#c9a24a"/>${L(1228, 580, F().cable ? 'Lightning rod (connected)' : 'Lightning rod – loose wire')}`,
          act: () => F().cable ? E.say('The cable runs from the rod down to the workshop. Thunder rumbles closer.') : E.say('A tall lightning rod. Its wire to the workshop has snapped – the end flaps in the wind.'),
          use: { cable: () => { F().cable = 1; E.take('cable'); E.say('You clamp the copper cable to the rod and drop the other end down the chimney to the workshop.'); return true; } } },
        { id: 'chimney', photo: [195, 40, 465, 430], x: 400, y: 300, w: 260, h: 300, art: () => `<rect x="460" y="320" width="140" height="240" fill="#5a2a1a"/>${L(530, 600, 'Chimney')}`,
          act: () => E.say('A wide brick chimney straight down to the workshop.') },
        { id: 'street', photo: [665, 305, 665, 390], x: 700, y: 480, w: 360, h: 160, art: () => L(880, 580, 'Edge of the roof'),
          act: () => E.say('Down in the street, under the gas lamps: three men in bowler hats, waiting. Mr Crake’s men.') },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['card', () => F().card, ['The automaton wants a punch card.', 'The wall diagram: holes in the top and bottom rows only.', 'Card C.']],
    ['desk', () => F().desk, ['The desk drawer has a word lock.', 'The portrait: “My password grows in my greenhouse.”', 'Valerian, Orchid, Lavender, Thyme: VOLT.']],
    ['lamps', () => F().lamps, ['The flytrap is shut tight.', 'The gardening notebook says which light wakes it.', 'Red, Green, Blue.']],
    ['roof', () => F().roof, ['The roof hatch is locked.', 'The desk drawer had a key with a lightning bolt.', 'Use the roof key on the hatch.']],
    ['cable', () => F().cable, ['The lightning rod’s wire is broken.', 'There is a cable in the packing crate.', 'Use the copper cable on the lightning rod.']],
    ['gears', () => F().gears, ['The gear board needs three cogs.', 'Put all three on, then set them as the manual says.', 'Left 36, middle 24, right 12.']],
    ['door', () => F().won, ['Everything is ready.', 'Pull the lever on the great door.', 'Tap the great door.']],
  ],
  intro: ['London · 31 December 1895 · 23:00', 'The Inventor’s Laboratory',
    `<p>You are Professor Ada Thornbury’s new assistant. Tonight the professor is away, and her rival Mr Crake has sent word: at midnight his men will break in and steal her great invention.</p><p>The invention is safe behind the great door – but it only opens when lightning drives the gears, and the professor took the cogs apart before she left. Put her machine back together and open the door before the clock strikes twelve.</p><p>Level 2: not every light, card or word in this house is the right one.</p>`,
    'Hissing pipes, ticking clocks and thunder outside. Look around.'],
  timesUp: ['Midnight!', 'Boots on the stairs… you can still finish, but off the leaderboard.'],
  win: ['Lightning!', 'A white flash, a crack of thunder – the gears spin and the great door swings open. Inside, glowing softly, is Professor Thornbury’s electric carriage. You drive it straight out through the back wall, past three very surprised men in bowler hats.'],
};

function openAutomaton() {
  if (F().card) return E.say('The automaton bows politely. It has nothing more to give.');
  E.cycler('Brass automaton', 'The automaton holds out its hand for a punch card. On the table lie four cards: A – holes in all three rows; B – holes in the middle row only; C – holes in the top and bottom rows; D – holes in the top row only.', [{ name: 'Feed', opts: CARDS }], v => { if (v[0] !== 'Card C') return false; F().card = 1; E.give('brass'); E.say('Whirr-click. The automaton reads the card, opens its brass chest and offers you a small brass cog.'); return true; }, 'The automaton spits the card back out.', 'Feed the card');
}
function openDesk() {
  if (F().desk) return E.say('The drawer is empty now.');
  E.wordLock('Desk drawer', 'A brass word lock with four letters.', 4, w => { if (w !== 'VOLT') return false; F().desk = 1; E.give('copper'); E.give('roofKey'); E.say('The drawer opens: a big copper cog and a key with a lightning bolt on it.'); return true; });
}
function openLamps() {
  if (F().lamps) return E.say('Red, green and blue glow softly. The flytrap is awake.');
  E.cycler('Growing lamps', 'Three lamps with coloured glass you can turn.', ['Left', 'Middle', 'Right'].map(n => ({ name: n, opts: LAMPS })), v => { if (v.join() !== 'Red,Green,Blue') return false; F().lamps = 1; E.give('silver'); E.say('The flytrap stretches, yawns – and drops a silver cog at your feet.'); return true; }, 'The flytrap grumbles and stays shut.', 'Switch on');
}
function put(k) { F()['on_' + k] = 1; E.take(k); E.say('You slide the cog onto a peg.'); return true; }
function openGears() {
  if (F().gears) return E.say('The three cogs mesh perfectly.');
  if (!(F().on_brass && F().on_silver && F().on_copper)) return E.say('Three empty pegs: LEFT, MIDDLE, RIGHT. The cogs are missing.');
  E.cycler('Gear board', 'Arrange the three cogs on the pegs.', ['Left', 'Middle', 'Right'].map(n => ({ name: n, opts: COGS })), v => { if (v.join() !== '36 teeth,24 teeth,12 teeth') return false; F().gears = 1; E.say('The cogs mesh with a satisfying clunk.'); return true; }, 'The cogs grind and jam.', 'Set');
}
function openDoor() {
  if (!F().gears) return E.say('The great door: a steel slab with a lever. The gear board beside it is incomplete.');
  if (!F().cable) return E.say('The gears are ready – but with no lightning, nothing will turn them. The roof wire is broken.');
  E.modal(`<h2>The great door</h2><p>Gears set. Cable connected. Thunder overhead.</p><button class="btn btn-big" id="lever">Pull the lever</button>`, m => m.querySelector('#lever').addEventListener('click', () => { E.closeModal(); E.win(); }));
}
});
