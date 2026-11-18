/* Six Clues escape room #11 – Santa's Locked Workshop (level 1, family). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const wall = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 9 }, (_, i) => `<rect x="${i * 180}" y="0" width="16" height="660" fill="${c2}"/>`).join('')}<rect y="660" width="1600" height="240" fill="#4a2c18"/><ellipse cx="800" cy="0" rx="520" ry="320" fill="url(#lamp)"/>`;
const POEM = ['Dasher', 'Dancer', 'Prancer', 'Vixen'];

return {
  start: 'workshop', v: 1,
  items: {
    wrapKey: ['🗝️', 'Red key', 'A red-painted key with a holly leaf on the ring.'],
    screwdriver: ['🪛', 'Screwdriver', 'A tiny elf-sized screwdriver.'],
    mapA: ['🗺️', 'Map (left half)', 'The left half of a torn flight map.'],
    mapB: ['🗺️', 'Map (right half)', 'The right half of a torn flight map.'],
    map: ['🗺️', 'Flight map', 'The whole flight map, taped together.'],
    carrot: ['🥕', 'Carrot', 'A fat orange carrot from the cookie tin.'],
    sleighKey: ['🔑', 'Sleigh key', 'A golden key shaped like a star.'],
    harness: ['🔔', 'Bell harness', 'A leather harness covered in silver bells.'],
  },
  rooms: {
    workshop: {
      name: 'The toy workshop',
      bg: () => wall('#5a1e1e', '#4a1818'),
      spots: [
        { id: 'shelf', x: 80, y: 120, w: 420, h: 420, art: () => `<rect x="100" y="140" width="380" height="380" fill="#6b4226"/>${[0, 1, 2].map(i => `<rect x="100" y="${250 + i * 110}" width="380" height="12" fill="#3a2414"/>`).join('')}${L(290, 560, 'Toy shelf')}`, act: () => openShelf() },
        { id: 'chest', x: 560, y: 470, w: 360, h: 180, art: () => `<rect x="580" y="500" width="320" height="140" rx="10" fill="#2e5a2e"/><rect x="700" y="550" width="80" height="40" fill="#c9a24a"/>${L(740, 680, F().chest ? 'Tool chest (open)' : 'Tool chest (3-number lock)')}`, act: () => openChest() },
        { id: 'tree', x: 980, y: 80, w: 260, h: 560, art: () => `<path d="M1110 100 L980 600 H1240z" fill="#1e5a2e"/><polygon points="1110,80 1122,112 1156,112 1128,132 1138,164 1110,144 1082,164 1092,132 1064,112 1098,112" fill="#e8c34a"/>${L(1110, 650, 'Christmas tree')}`,
          act: () => { E.note('tree', 'A label hanging from the tree, in elf handwriting: “Every year I go on top of the tree, and I shine the brightest. What am I?”'); E.say('A little label hangs from the lowest branch: “Every year I go on top of the tree, and I shine the brightest. What am I?”'); } },
        { id: 'bench', x: 1260, y: 420, w: 300, h: 220, art: () => `<rect x="1270" y="470" width="280" height="30" fill="#7a4a2a"/><rect x="1290" y="500" width="20" height="140" fill="#5a3418"/><rect x="1510" y="500" width="20" height="140" fill="#5a3418"/><rect x="1330" y="430" width="90" height="40" fill="#9a9a9a"/>${L(1410, 680, 'Elf workbench')}`,
          act: () => F().panel ? E.say('The panel under the bench hangs open. Empty now.') : E.say('Half-finished wooden toys and wood shavings. Under the bench is a small panel held by four tiny screws.'),
          use: { screwdriver: () => { if (F().panel) return false; F().panel = 1; E.give('mapA'); E.say('Four tiny screws come out. Behind the panel: the left half of a torn map!'); return true; } } },
        { id: 'toWrap', x: 20, y: 740, w: 360, h: 130, art: () => E.exit(F().wrap ? '← Wrapping room' : '← Wrapping room (locked)'), act: () => F().wrap ? E.go('wrap') : E.say('A red door with a holly wreath. Locked.'),
          use: { wrapKey: () => { F().wrap = 1; E.take('wrapKey'); E.say('The red key turns. The smell of paper and gingerbread drifts out.'); return true; } } },
        { id: 'toStable', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit(F().stable ? 'Stable →' : 'Stable door (barred)', 1240), act: () => F().stable ? E.go('stable') : openStableDoor() },
      ],
    },
    wrap: {
      name: 'The wrapping room',
      bg: () => wall('#1e3a5a', '#18304a'),
      spots: [
        { id: 'back', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Workshop →', 1240), act: () => E.go('workshop') },
        { id: 'tin', x: 120, y: 420, w: 300, h: 220, art: () => `<ellipse cx="270" cy="560" rx="130" ry="60" fill="#b02a2a"/><rect x="140" y="480" width="260" height="80" fill="#c03030"/>${L(270, 670, F().tin ? 'Cookie tin (open)' : 'Cookie tin (letter lock)')}`, act: () => openTin() },
        { id: 'tags', x: 520, y: 120, w: 460, h: 320, art: () => `${E.paper(540, 140, 420, 260, 6)}${L(750, 430, 'Gift tag list')}`,
          act: () => { E.note('tags', 'Gift tag list on the wall: “Train for Sam. Drum for Lily. Teddy for Max. Yo-yo for Ada. Rocket for Ben. All presents on the sleigh by seven!”'); E.say('A long list of gift tags – Sam, Lily, Max, Ada, Ben… “All presents on the sleigh by seven!”'); } },
        { id: 'drawer', x: 1040, y: 380, w: 320, h: 260, art: () => `<rect x="1060" y="420" width="280" height="200" fill="#6b4226"/><rect x="1080" y="440" width="240" height="70" fill="#5a3418"/><rect x="1080" y="530" width="240" height="70" fill="#5a3418"/>${L(1200, 660, 'Ribbon drawers')}`,
          act: () => { if (F().drawer) return E.say('Only ribbons left.'); F().drawer = 1; E.give('mapB'); E.say('Between rolls of ribbon: the right half of a torn map!'); } },
        { id: 'letter', x: 1040, y: 100, w: 320, h: 220, art: () => `${E.paper(1060, 120, 280, 170, 5)}${L(1200, 320, 'Letter from Mrs Claus')}`,
          act: () => { F().letterRead = 1; E.note('letter', 'Letter from Mrs Claus: “Dear elves, the stable bar lifts when you say something kind to the reindeer. Feed them first – they are grumpy when hungry! The sleigh needs its key, its bell harness and the map. Love, Mrs C.”'); E.say('A letter from Mrs Claus about the stable and the sleigh. You copy it into your notebook.'); } },
      ],
    },
    stable: {
      name: 'The reindeer stable',
      bg: () => `<rect width="1600" height="900" fill="#3a2a1a"/><rect y="600" width="1600" height="300" fill="#7a6a3a"/>${[0, 1, 2, 3].map(i => `<rect x="${120 + i * 240}" y="260" width="200" height="340" fill="#2a1e12" stroke="#5a4028" stroke-width="10"/>`).join('')}`,
      spots: [
        { id: 'back', x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Workshop'), act: () => E.go('workshop') },
        { id: 'stalls', x: 100, y: 240, w: 960, h: 380, art: () => `${POEM.map((n, i) => L(220 + i * 240, 250, n)).join('')}${L(580, 660, 'Four reindeer stalls')}`, act: () => openStalls() },
        { id: 'poem', x: 1120, y: 120, w: 300, h: 200, art: () => `${E.paper(1140, 140, 260, 150, 4)}${L(1270, 320, 'Old poem on the wall')}`,
          act: () => { E.note('poem', 'An old poem on the stable wall: “Now, Dasher! now, Dancer! now, Prancer and Vixen!” Underneath: “Harness them in the order they are called.”'); E.say('“Now, Dasher! now, Dancer! now, Prancer and Vixen!” Underneath: “Harness them in the order they are called.”'); } },
        { id: 'sleigh', x: 1100, y: 420, w: 480, h: 280, art: () => `<path d="M1120 560 Q1140 460 1300 460 H1520 V600 H1180 Q1120 600 1120 560z" fill="#b02a2a" stroke="#c9a24a" stroke-width="8"/>${L(1340, 690, 'Santa’s sleigh')}`, act: () => openSleigh(),
          use: { map: () => { F().mapIn = 1; E.take('map'); E.say('You clip the flight map onto the sleigh’s dashboard.'); return true; }, sleighKey: () => { F().keyIn = 1; E.take('sleighKey'); E.say('The star key slides into the sleigh. Now it’s ready to turn.'); return true; }, harness: () => { F().harnessOn = 1; E.take('harness'); E.say('You fit the bell harness. The reindeer stamp and jingle.'); return true; } } },
        { id: 'hay', x: 300, y: 640, w: 500, h: 120, art: () => `<ellipse cx="550" cy="700" rx="230" ry="50" fill="#c9a24a"/>${L(550, 780, 'Hay pile')}`,
          act: () => F().fed ? (F().hay ? E.say('Just hay.') : (F().hay = 1, E.give('sleighKey'), E.say('The happy reindeer nose through the hay – and push out a golden star-shaped key!'))) : E.say('A big soft pile of hay. A reindeer is lying on part of it and won’t move – she looks hungry.'),
          use: { carrot: () => { F().fed = 1; E.take('carrot'); E.say('Crunch! The reindeer munches the carrot and gets up, wagging her stubby tail.'); return true; } } },
      ],
    },
  },
  combine: (a, b) => { if ([a, b].sort().join() === 'mapA,mapB') { E.take('mapA'); E.take('mapB'); E.give('map'); F().map = 1; E.note('map', 'The flight map, whole again: a dotted line from the North Pole to the town. Written along it: “Fly heading 1-2-5.”'); E.say('The two halves fit. A dotted route to the town: “Fly heading 1-2-5.”'); return true; } return false; },
  stages: [
    ['chest', () => F().chest, ['The tool chest wants three numbers. Count something.', 'The lid says red, then blue, then green. Look closely at the toy shelf.', 'Red trains 4, blue drums 2, green bears 7: 427.']],
    ['wrap', () => F().wrap, ['The tool chest gave you a key.', 'A red key for a red door.', 'Use the red key on the wrapping room door.']],
    ['tin', () => F().tin, ['The cookie tin has a letter lock with four letters.', 'The label on the Christmas tree asks a riddle.', 'What goes on top of the tree? STAR.']],
    ['map', () => F().map || F().mapIn, ['There is a torn map – two halves.', 'One half was in the ribbon drawers. The other is under the elf workbench, held by screws.', 'Use the screwdriver on the workbench, then combine the two halves.']],
    ['stable', () => F().stable, ['The stable door bar has four letter wheels.', 'Mrs Claus’s letter says to say something kind – and the cookie tin had a card.', 'Spell KIND on the stable door.']],
    ['fed', () => F().hay, ['A hungry reindeer is lying on the hay.', 'The cookie tin had something reindeer love.', 'Use the carrot on the hay pile, then search the hay.']],
    ['harness', () => F().harness, ['The bells need the reindeer in the right order.', 'The poem on the wall calls their names.', 'Dasher, Dancer, Prancer, Vixen.']],
    ['sleigh', () => F().won, ['The sleigh needs three things: key, harness and map.', 'Put all three on the sleigh.', 'Then set the heading on the map: 125.']],
  ],
  intro: ['The North Pole · 24 December · 18:00', 'Santa’s Locked Workshop',
    `<p>You are the newest elf at the North Pole. Santa has a bad cold, the other elves have gone to the Christmas party – and somebody has locked you in the workshop with all the doors shut.</p><p>The sleigh must leave in one hour, or the town gets no presents this year. Find the key, the map and the bells, and get that sleigh in the air!</p><p>Level 1: perfect for families and first-time players.</p>`,
    'Wood shavings, paint pots and a smell of gingerbread. Look around.'],
  timesUp: ['The clock strikes seven.', 'Somewhere a child is waiting by the window… but you can still finish.'],
  win: ['Up, up and away!', 'The bells jingle, the runners lift off the snow and the sleigh climbs over the workshop roof. Santa sneezes, waves from the window – and the town gets its presents after all.'],
};

function openShelf() {
  E.note('shelf', 'Toy shelf: 🚂 red trains ×4 · 🥁 blue drums ×2 · 🧸 green bears ×7 · 🪀 yellow yo-yos ×5 · 🚀 silver rockets ×3');
  E.modal(`<h2>The toy shelf</h2><p>Finished toys, ready for wrapping:</p><p class="paper" style="font-size:1.4rem;line-height:2">🚂🚂🚂🚂 red trains<br>🥁🥁 blue drums<br>🧸🧸🧸🧸🧸🧸🧸 green bears<br>🪀🪀🪀🪀🪀 yellow yo-yos<br>🚀🚀🚀 silver rockets</p>`);
}
function openChest() {
  if (F().chest) return E.say('The tool chest is open – just paint pots now.');
  E.numLock('Tool chest', 'A green tool chest with a three-number lock. Painted on the lid: “Count what you need: red, then blue, then green.”', 3, c => { if (c !== '427') return false; F().chest = 1; E.give('wrapKey'); E.give('screwdriver'); E.say('Click! Inside: a red key and a tiny screwdriver.'); return true; });
}
function openTin() {
  if (F().tin) return E.say('Only crumbs left in the tin.');
  E.wordLock('Cookie tin', 'A big red cookie tin with four letter wheels. Mrs Claus’s writing on the lid: “The elf password is what shines on top.”', 4, w => { if (w !== 'STAR') return false; F().tin = 1; E.give('carrot'); F().stableHint = 1; E.say('The lid pops off: gingerbread stars – and a fat orange carrot. Under the cookies a card: “Kind words for the stable door: KIND.”'); E.note('kind', 'Card in the cookie tin: “To open the stable bar, spell KIND on the stable door.”'); return true; });
}
function openStableDoor() { E.wordLock('Stable door', 'A wooden bar with four letter wheels carved into it.', 4, w => { if (w !== 'KIND') return false; F().stable = 1; E.say('The bar lifts. Warm air and the sound of hooves.'); return true; }); }
function openStalls() {
  if (F().harness) return E.say('The four reindeer stand in a row, ready to go.');
  E.orderer('Four reindeer stalls', 'Tap the reindeer in the order to harness them.', ['Prancer', 'Vixen', 'Dasher', 'Dancer'], v => { if (v.join() !== POEM.join()) return false; F().harness = 1; E.give('harness'); E.say('Each reindeer steps out as you call its name. On the last hook: a leather harness covered in silver bells.'); return true; }, 'The reindeer snort and shuffle back into their stalls.');
}
function openSleigh() {
  if (!(F().mapIn && F().keyIn && F().harnessOn)) return E.say(`The sleigh needs its key, its bell harness and its map. ${[F().keyIn && 'Key', F().harnessOn && 'Harness', F().mapIn && 'Map'].filter(Boolean).join(', ') || 'None'} in place.`);
  E.numLock('Sleigh compass', 'A brass compass with three number wheels for the heading.', 3, c => { if (c !== '125') return false; E.win(); return true; }, 'The reindeer look at you, puzzled. Wrong way.');
}
});
