/* Six Clues escape room #20 – Christmas Eve at Holly Manor (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const paper = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 16 }, (_, i) => `<rect x="${i * 100}" y="0" width="40" height="660" fill="${c2}"/>`).join('')}<rect y="660" width="1600" height="240" fill="#3a1e14"/><ellipse cx="800" cy="0" rx="520" ry="300" fill="url(#lamp)"/>`;
const HOOKS = ['Drawing room', 'Library', 'Dining room', 'Nursery', 'Front door'];

return {
  start: 'drawing', v: 2,
  items: {
    libKey: ['🗝️', 'Library key', 'A small key tied with a red ribbon.'],
    knife: ['🔪', 'Pudding knife', 'A silver knife from the sideboard.'],
    sixpence: ['🪙', 'Silver sixpence', 'The lucky sixpence from the Christmas pudding.'],
    frontKey: ['🔑', 'Front door key', 'The big iron front door key.'],
    star: ['⭐', 'The Holly Star', 'The family’s diamond star brooch – stolen and found again.'],
  },
  rooms: {
    drawing: {
      name: 'The drawing room',
      bg: () => paper('#2e4a2e', '#365636'),
      spots: [
        { id: 'tree', photo: [155, 25, 340, 560], x: 80, y: 80, w: 380, h: 580, art: () => `<path d="M270 100 L100 620 H440z" fill="#1e5a2e"/>${L(270, 650, 'Christmas tree')}`,
          act: () => { E.note('tree', 'The Christmas tree: the top branch is empty – the Holly Star brooch was pinned there when the lights went out at nine. On the branches: gold rings, little bird ornaments and glass hens. A tag: “Sing the days to open my music box.”'); E.say('The top of the tree is bare – the Holly Star was there before the lights went out. A tag: “Sing the days to open my music box.”'); } },
        { id: 'carol', photo: [520, 285, 170, 100], x: 520, y: 100, w: 320, h: 260, art: () => `${E.paper(540, 120, 280, 200, 6)}${L(680, 360, 'Carol sheet on the piano')}`,
          act: () => { E.note('carol', 'Carol sheet: “On the fifth day of Christmas, my true love sent to me: five gold rings, four calling birds, three French hens…” Pencilled at the bottom: “Rings, then birds, then hens.”'); E.say('“…five gold rings, four calling birds, three French hens…” Pencilled at the bottom: “Rings, then birds, then hens.”'); } },
        { id: 'musicbox', photo: [715, 445, 180, 150], x: 540, y: 440, w: 300, h: 200, art: () => `<rect x="560" y="480" width="260" height="120" fill="#7a3a2a" stroke="#c9a24a" stroke-width="6"/>${L(690, 640, F().box ? 'Music box (open)' : 'Music box (3 numbers)')}`, act: () => openBox() },
        { id: 'fire', photo: [895, 245, 325, 290], x: 920, y: 280, w: 380, h: 360, art: () => `<rect x="940" y="300" width="340" height="320" fill="#5a3a2a"/><rect x="1000" y="420" width="220" height="200" fill="#111"/>${L(1110, 650, 'Fireplace (cold)')}`,
          act: () => { E.note('fire', 'The fireplace is stone cold, with a note from the maid: “Do not light – chimney blocked by snow. Not lit all evening. – Elsie”'); E.say('The fireplace is stone cold. A maid’s note: “Do not light – chimney blocked by snow. Not lit all evening.”'); } },
        { id: 'window', photo: [1275, 0, 205, 400], x: 1340, y: 80, w: 220, h: 400, art: () => `<rect x="1360" y="100" width="180" height="340" fill="#c8d8e8"/>${L(1450, 470, 'Window')}`,
          act: () => E.say('Snow, snow and more snow. By the gate, a sleigh is waiting to take the guests to the midnight train.') },
        { id: 'toLib', photo: [0, 95, 155, 650], x: 20, y: 740, w: 300, h: 130, art: () => E.exit(F().lib ? '← Library' : '← Library (locked)'), act: () => F().lib ? E.go('library') : E.say('The library door is locked.'),
          use: { libKey: () => { F().lib = 1; E.take('libKey'); E.say('The library door opens.'); return true; } } },
        { id: 'toHall', photo: [305, 740, 415, 160], x: 620, y: 740, w: 340, h: 130, art: () => E.exit('Hall ↓', 640), act: () => E.go('hall') },
        { id: 'toKitchen', photo: [1500, 140, 100, 645], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Kitchen →', 1240), act: () => E.go('kitchen') },
      ],
    },
    library: {
      name: 'The library',
      bg: () => paper('#3a2a1e', '#2e2218'),
      spots: [
        { id: 'back', photo: [1495, 180, 105, 620], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Drawing room →', 1240), act: () => E.go('drawing') },
        { id: 'statements', photo: [140, 540, 430, 130], x: 100, y: 120, w: 520, h: 360, art: () => `${E.paper(120, 140, 480, 300, 8)}${L(360, 480, 'Guests’ statements')}`,
          act: () => { E.note('statements', 'The guests’ statements, written down by Lady Holly: Colonel Ash – “At the piano when the lights went out.” · Miss Rose Penn – “At the window with Mrs Dove.” · Mrs Dove – “At the window with Miss Penn.” · Mr Lyle – “Warming my hands by the fire.”'); E.say('Four guests, four statements: the Colonel at the piano, Miss Penn and Mrs Dove at the window, Mr Lyle warming his hands by the fire.'); } },
        { id: 'bellboard', photo: [660, 85, 420, 165], x: 700, y: 120, w: 380, h: 280, art: () => `<rect x="720" y="140" width="340" height="220" fill="#5a3a20"/>${[0, 1, 2, 3, 4].map(i => `<circle cx="${760 + i * 65}" cy="250" r="18" fill="#c9a24a"/>`).join('')}${L(890, 400, 'Servants’ bell board (copy)')}`,
          act: () => E.say('A copy of the servants’ bell board. The library bell is tied with a red ribbon: “Rang last – the master wants his front door key kept on this room’s hook.”') },
        { id: 'portrait', photo: [1115, 15, 280, 370], x: 1140, y: 100, w: 320, h: 380, art: () => `<rect x="1160" y="120" width="280" height="320" fill="#4a3a2a" stroke="#c9a24a" stroke-width="10"/>${L(1300, 470, 'Portrait with the Holly Star')}`,
          act: () => E.say('Lady Holly’s grandmother, wearing the Holly Star – a brooch of diamonds shaped like a holly leaf around a star.') },
      ],
    },
    kitchen: {
      name: 'The kitchen',
      bg: () => paper('#3a3a30', '#33332a'),
      spots: [
        { id: 'back', photo: [0, 95, 135, 800], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Drawing room'), act: () => E.go('drawing') },
        { id: 'sideboard', photo: [135, 460, 420, 340], x: 100, y: 380, w: 380, h: 260, art: () => `<rect x="120" y="440" width="340" height="180" fill="#5a3a20"/>${L(290, 650, 'Sideboard')}`,
          act: () => { if (F().knife) return E.say('Plates and napkins.'); F().knife = 1; E.give('knife'); E.say('A silver pudding knife lies ready on the sideboard.'); } },
        { id: 'pudding', photo: [765, 500, 200, 120], x: 560, y: 380, w: 360, h: 260, art: () => `<ellipse cx="740" cy="540" rx="140" ry="80" fill="#4a2410"/><path d="M700 470 l40 -20 l40 20" fill="#3a8a3a"/>${L(740, 650, 'Christmas pudding')}`,
          act: () => F().pudding ? E.say('A Christmas pudding with a slice missing.') : E.say('A big round Christmas pudding with a sprig of holly on top. Cook always hides a lucky sixpence in it.'),
          use: { knife: () => { F().pudding = 1; E.give('sixpence'); E.say('You cut a slice – and there it is: a shiny silver sixpence!'); return true; } } },
        { id: 'pantry', photo: [1305, 215, 275, 120], x: 1000, y: 160, w: 420, h: 440, art: () => `<rect x="1020" y="180" width="380" height="380" fill="#4a3a2a"/>${[0, 1, 2, 3, 4].map(i => `<circle cx="${1070 + i * 70}" cy="300" r="12" fill="#c9a24a"/>`).join('')}${L(1210, 590, F().hook ? 'Butler’s key hooks (taken)' : 'Butler’s key hooks')}`, act: () => openHooks() },
        { id: 'cook', photo: [865, 120, 115, 100], x: 600, y: 100, w: 320, h: 220, art: () => `${E.paper(620, 120, 280, 160, 4)}${L(760, 320, 'Cook’s note')}`,
          act: () => { E.note('cook', 'Cook’s note: “Gas meter in the hall ran out at nine sharp – all the lights went with it! Put a sixpence in, someone. And who left pine needles all over Mr Lyle’s good shoes?”'); E.say('“The gas meter ran out at nine – all the lights went with it! And who left pine needles all over Mr Lyle’s good shoes?”'); } },
      ],
    },
    hall: {
      name: 'The front hall',
      bg: () => F().gas ? paper('#3a2e2a', '#443630') : `<rect width="1600" height="900" fill="#08080a"/>`,
      spots: [
        { id: 'up', photo: [0, 420, 320, 480], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('↑ Drawing room'), act: () => E.go('drawing') },
        { id: 'meter', photo: [125, 235, 135, 215], x: 80, y: 200, w: 300, h: 280, art: () => `<rect x="120" y="240" width="220" height="200" fill="#5a5a50"/>${L(230, 480, F().gas ? 'Gas meter (lit)' : 'Coin gas meter')}`,
          act: () => F().gas ? E.say('The meter ticks. The gas lamps burn bright.') : E.say('It’s dark. You feel a cold iron box with a coin slot: the gas meter. It wants a sixpence.'),
          use: { sixpence: () => { F().gas = 1; E.take('sixpence'); E.say('The sixpence drops in, the meter clicks, and the gas lamps flare up all over the hall!'); return true; } } },
        { id: 'cases', photo: [595, 565, 585, 170], x: 460, y: 380, w: 560, h: 260, hide: () => !F().gas, art: () => `${[0, 1, 2, 3].map(i => `<rect x="${480 + i * 135}" y="460" width="115" height="150" fill="#5a3a2a"/>`).join('')}${L(740, 650, 'Guests’ suitcases, packed for the train')}`, act: () => openCases() },
        { id: 'front', photo: [1240, 35, 360, 705], x: 1180, y: 120, w: 360, h: 540, art: () => `<rect x="1200" y="140" width="320" height="500" fill="#3a2414" stroke="#2a1a10" stroke-width="10"/>${L(1360, 680, F().gas ? 'Front door' : 'Something big – a door?')}`, act: () => openFront(),
          use: { frontKey: () => { F().keyIn = 1; E.take('frontKey'); E.say('The big key turns in the lock. Outside, sleigh bells.'); return true; } } },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['box', () => F().box, ['The music box wants three numbers.', 'The carol sheet: rings, then birds, then hens.', 'Five gold rings, four calling birds, three French hens: 543.']],
    ['lib', () => F().lib, ['The music box had a key.', 'The library is locked.', 'Use the library key on the library door.']],
    ['gas', () => F().gas, ['The hall is pitch dark.', 'The gas meter needs a sixpence – Cook always hides one somewhere.', 'Cut the pudding with the knife and put the sixpence in the meter.']],
    ['thief', () => F().star, ['Which guest took the star?', 'Someone lied: the fire was never lit – and who had pine needles on his shoes?', 'Mr Lyle. Open his suitcase: LYLE.']],
    ['hook', () => F().hook, ['The butler keeps the front door key on a hook.', 'The bell board in the library says which room’s hook.', 'The Library hook.']],
    ['door', () => F().won, ['Now stop the sleigh!', 'Use the front door key on the front door.', 'Then open the door – with the star.']],
  ],
  intro: ['Holly Manor, Yorkshire · 24 December 1923 · 23:00', 'Christmas Eve at Holly Manor',
    `<p>You are Lady Holly’s grand-niece, snowed in for Christmas. At nine o’clock the lights went out – and when they came back on, the family’s diamond brooch, the Holly Star, was gone from the top of the tree.</p><p>At midnight the guests take the sleigh to the last train, and the thief with them. The butler has locked the front door and gone to bed with the key. Find the star, unmask the thief and get that door open before the sleigh leaves.</p><p>Level 2: one of the guests is lying.</p>`,
    'Pine, cinnamon and candle smoke. A bare branch at the top of the tree. Look around.'],
  timesUp: ['Midnight bells.', 'The sleigh bells jingle away down the drive… but you can still finish, off the leaderboard.'],
  win: ['Stop that sleigh!', 'You run out into the snow holding the Holly Star high. The sleigh stops, Mr Lyle tries to run and falls flat in a snowdrift – and Lady Holly pins her star back on the tree just as the clock strikes twelve. Merry Christmas!'],
};

function openBox() {
  if (F().box) return E.say('The music box tinkles a carol. It’s empty now.');
  E.numLock('Music box', 'A red music box with three little number wheels.', 3, c => { if (c !== '543') return false; F().box = 1; E.give('libKey'); E.say('The lid lifts and a carol tinkles out. Under the dancing figure: a small key with a red ribbon.'); return true; });
}
function openCases() {
  if (F().star) return E.say('Mr Lyle’s suitcase stands open.');
  E.wordLock('Suitcases', 'Four suitcases, each with a name lock. Whose do you try? (Enter a name.)', 4, w => {
    if (w === 'LYLE') { F().star = 1; E.give('star'); E.say('Under Mr Lyle’s shirts, wrapped in a sock: the Holly Star! There are pine needles all over the lining.'); return true; }
    return false;
  }, 'Locked – and anyway, wrong guest.');
}
function openHooks() {
  if (F().hook) return E.say('Five hooks. You took the front door key.');
  E.cycler('Butler’s key hooks', 'Five hooks, each under a room name. Only one key is the front door key – the rest are dummies on a spring that ring the butler’s bell.', [{ name: 'Hook', opts: HOOKS }], v => { if (v[0] !== 'Library') return false; F().hook = 1; E.give('frontKey'); E.say('Under the Library label hangs a big iron key – the front door key!'); return true; }, 'Ding! A dummy key – somewhere upstairs the butler mumbles in his sleep.', 'Take the key');
}
function openFront() {
  if (!F().gas) return E.say('Too dark to see anything.');
  if (!F().keyIn) return E.say('The heavy front door. Locked – the butler has the key… or does he?');
  if (!E.has('star')) return E.say('You could run out to the sleigh – but without the star, nobody will believe you.');
  E.modal(`<h2>The front door</h2><p>The key is turned. Sleigh bells outside. The Holly Star is in your hand.</p><button class="btn btn-big" id="out">Fling the door open</button>`, m => m.querySelector('#out').addEventListener('click', () => { E.closeModal(); E.win(); }));
}
});
