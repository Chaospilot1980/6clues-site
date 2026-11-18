/* Six Clues escape room #14 – The Enchanted Library (level 1, family). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const hall = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 8 }, (_, i) => `<rect x="${i * 200 + 20}" y="40" width="160" height="600" fill="${c2}"/>`).join('')}<rect y="660" width="1600" height="240" fill="#3a2414"/><ellipse cx="800" cy="0" rx="520" ry="300" fill="url(#lamp)"/>`;
const RAINBOW = ['Red', 'Orange', 'Yellow', 'Green', 'Blue'];
const HOURS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'];

return {
  start: 'hall', v: 1,
  items: {
    potion: ['🧪', 'Glowing potion', 'A little bottle of potion that glows silver.'],
    silverKey: ['🗝️', 'Silver key', 'A silver key with a crescent moon on the bow.'],
    wand: ['🪄', 'Wand', 'A slim wand of dark wood that tingles in your fingers.'],
    mirror: ['🪞', 'Hand mirror', 'A small silver hand mirror.'],
  },
  rooms: {
    hall: {
      name: 'The great library',
      bg: () => hall('#2a1e2e', '#4a2e1e'),
      spots: [
        { id: 'owl', x: 80, y: 80, w: 240, h: 240, art: () => `<ellipse cx="200" cy="200" rx="70" ry="90" fill="#8a6a4a"/><circle cx="175" cy="170" r="18" fill="#f0d060"/><circle cx="225" cy="170" r="18" fill="#f0d060"/>${L(200, 330, 'Stuffed owl')}`,
          act: () => { E.note('owl', 'The owl blinked and spoke! “Sort my books like the rainbow after rain, and a door will open again.”'); E.say('The owl blinks – it’s alive! “Sort my books like the rainbow after rain, and a door will open again.”'); } },
        { id: 'shelf', x: 400, y: 160, w: 480, h: 420, art: () => `<rect x="420" y="180" width="440" height="380" fill="#5a3a20"/>${['#d04030', '#e08a30', '#e8d040', '#3aa04a', '#3a6ad0'].map((c, i) => `<rect x="${460 + i * 80}" y="300" width="50" height="160" fill="${c}"/>`).join('')}${L(640, 600, F().shelf ? 'Bookshelf (swung open)' : 'Bookshelf – five coloured books')}`, act: () => openShelf() },
        { id: 'clock', x: 960, y: 80, w: 260, h: 560, art: () => `<rect x="1000" y="100" width="180" height="520" fill="#4a2e1e"/><circle cx="1090" cy="220" r="70" fill="#e8dcb8"/>${L(1090, 660, F().clock ? 'Grandfather clock (open)' : 'Grandfather clock')}`, act: () => openClock() },
        { id: 'desk', x: 1260, y: 420, w: 300, h: 220, art: () => `<rect x="1280" y="480" width="260" height="30" fill="#5a3a20"/>${E.paper(1320, 430, 160, 50, 2)}${L(1410, 660, 'Librarian’s desk')}`,
          act: () => { if (F().mirror) return E.say('Library cards and a pot of ink. Nothing else.'); F().mirror = 1; E.give('mirror'); E.say('In the desk drawer: a small silver hand mirror.'); } },
        { id: 'toStudy', x: 20, y: 740, w: 360, h: 130, art: () => E.exit(F().shelf ? '← Secret study' : ''), hide: () => !F().shelf, act: () => E.go('study') },
        { id: 'toTower', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit(F().tower ? 'Tower stairs →' : 'Tower door (locked)', 1240), act: () => F().tower ? E.go('tower') : E.say('A round door with a crescent moon on it. Locked.'),
          use: { silverKey: () => { F().tower = 1; E.take('silverKey'); E.say('The silver key fits the moon lock. Stairs spiral up into the tower.'); return true; } } },
      ],
    },
    study: {
      name: 'The wizard’s study',
      bg: () => hall('#1e2a2e', '#2a3a3e'),
      spots: [
        { id: 'back', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Library →', 1240), act: () => E.go('hall') },
        { id: 'recipe', x: 100, y: 140, w: 320, h: 260, art: () => `${E.paper(120, 160, 280, 200, 6)}${L(260, 400, 'Potion recipe')}`,
          act: () => { E.note('recipe', 'Potion recipe: “Moonlight Potion – 3 frog eggs, 1 moonflower, 5 falling stars. Stir well.”'); E.say('“Moonlight Potion – 3 frog eggs, 1 moonflower, 5 falling stars. Stir well.”'); } },
        { id: 'cabinet', x: 480, y: 300, w: 360, h: 340, art: () => `<rect x="500" y="320" width="320" height="300" fill="#3a2a4a" stroke="#c9a24a" stroke-width="6"/>${L(660, 650, F().cabinet ? 'Potion cabinet (open)' : 'Potion cabinet (3 numbers)')}`, act: () => openCabinet() },
        { id: 'writing', x: 900, y: 120, w: 520, h: 220, art: () => `<rect x="920" y="140" width="480" height="160" fill="#e8dcb8"/>${L(1160, 340, 'Strange writing on the wall')}`,
          act: () => F().readWall ? E.say('“THE WAND SLEEPS IN THE CLOCK AT MIDNIGHT.”') : E.say('Strange writing on the wall: “THGINDIM TA KCOLC EHT NI SPEELS DNAW EHT”. It looks back to front.'),
          use: { mirror: () => { F().readWall = 1; E.note('wall', 'In the mirror, the wall writing reads: “THE WAND SLEEPS IN THE CLOCK AT MIDNIGHT.”'); E.say('In the mirror the words turn round: “THE WAND SLEEPS IN THE CLOCK AT MIDNIGHT.”'); return true; } } },
        { id: 'cauldron', x: 920, y: 420, w: 360, h: 220, art: () => `<ellipse cx="1100" cy="560" rx="150" ry="70" fill="#1a1a1a"/>${L(1100, 660, 'Bubbling cauldron')}`,
          act: () => E.say('A cauldron bubbles with purple goo. It smells of old socks. Better not drink it.') },
      ],
    },
    tower: {
      name: 'The star tower',
      bg: () => `<rect width="1600" height="900" fill="#0a0e1e"/>${Array.from({ length: 40 }, (_, i) => `<circle cx="${(i * 397) % 1600}" cy="${(i * 211) % 600}" r="3" fill="#fff"/>`).join('')}<rect y="660" width="1600" height="240" fill="#2a2a3a"/>`,
      spots: [
        { id: 'back', x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Down the stairs'), act: () => E.go('hall') },
        { id: 'chart', x: 120, y: 140, w: 380, h: 300, art: () => `${E.paper(140, 160, 340, 240, 4)}${L(310, 440, 'Star chart')}`,
          act: () => { E.note('chart', 'Star chart: four constellations are circled – the Hare, the Owl, the Moth and the Eagle. Underneath: “The first letters are the spell to go home.”'); E.say('Four constellations are circled: the Hare, the Owl, the Moth and the Eagle. “The first letters are the spell to go home.”'); } },
        { id: 'telescope', x: 600, y: 200, w: 300, h: 360, art: () => `<rect x="700" y="260" width="200" height="40" fill="#c9a24a" transform="rotate(-30 800 280)"/><rect x="760" y="300" width="20" height="240" fill="#5a3a20"/>${L(780, 600, 'Telescope')}`,
          act: () => E.say('Through the telescope, the Owl constellation winks at you. Hoo!') },
        { id: 'circle', x: 980, y: 420, w: 520, h: 220, art: () => `<ellipse cx="1240" cy="560" rx="230" ry="70" fill="none" stroke="#9a8ae0" stroke-width="8"/>${L(1240, 660, 'Magic circle on the floor')}`, act: () => openCircle(),
          use: { potion: () => { F().potionIn = 1; E.take('potion'); E.say('You pour the potion into the circle. It glows silver all around.'); return true; }, wand: () => { if (!F().potionIn) return false; F().wandIn = 1; E.take('wand'); E.say('You tap the glowing circle with the wand. Sparks rise into the air – now say the spell!'); return true; } } },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['shelf', () => F().shelf, ['The owl talks about the books.', 'Sort the five coloured books like a rainbow.', 'Red, Orange, Yellow, Green, Blue.']],
    ['cabinet', () => F().cabinet, ['The potion cabinet needs three numbers.', 'Read the potion recipe on the study wall.', '3 frog eggs, 1 moonflower, 5 stars: 315.']],
    ['tower', () => F().tower, ['The tower door has a moon on it.', 'The potion cabinet had a silver key.', 'Use the silver key on the tower door.']],
    ['wall', () => F().readWall, ['The writing on the study wall is back to front.', 'You found a mirror in the librarian’s desk.', 'Use the mirror on the strange writing.']],
    ['clock', () => F().clock, ['The wand sleeps in the clock.', 'Set the clock to midnight.', 'Set the hour hand to 12.']],
    ['circle', () => F().wandIn, ['The magic circle in the tower is waiting.', 'First the potion, then the wand.', 'Use the potion on the circle, then the wand.']],
    ['spell', () => F().won, ['Now the spell.', 'The star chart: the first letters of the four constellations.', 'Hare, Owl, Moth, Eagle: HOME.']],
  ],
  intro: ['Somewhere old · a rainy afternoon · 15:00', 'The Enchanted Library',
    `<p>You stepped into the old town library to get out of the rain. Now the door has vanished behind you and the books are whispering.</p><p>The library is enchanted – and in one hour, when the last candle burns out, you will be stuck in here for a hundred years! Find the spell that takes you home.</p><p>Level 1: perfect for families and first-time players.</p>`,
    'Dusty shelves to the ceiling, and a feeling that someone is watching. Look around.'],
  timesUp: ['The last candle flickers…', '…but it doesn’t go out yet. Keep trying!'],
  win: ['H – O – M – E', 'The circle flashes silver, the books cheer, and with a pop you are standing on the library steps in the sunshine – the rain has stopped. In your pocket is a feather from the owl.'],
};

function openShelf() {
  if (F().shelf) return E.say('The bookshelf has swung open like a door.');
  E.orderer('Bookshelf', 'Tap the five books in the right order.', ['Green', 'Red', 'Blue', 'Yellow', 'Orange'], v => { if (v.join() !== RAINBOW.join()) return false; F().shelf = 1; E.say('Click… creeeak. The whole bookshelf swings open – there’s a secret room behind!'); return true; }, 'The books shuffle themselves back. Wrong order!');
}
function openCabinet() {
  if (F().cabinet) return E.say('The potion cabinet is empty now.');
  E.numLock('Potion cabinet', 'A purple cabinet with three number wheels shaped like bubbles.', 3, c => { if (c !== '315') return false; F().cabinet = 1; E.give('potion'); E.give('silverKey'); E.say('The cabinet opens: a little glowing potion and a silver key with a moon on it!'); return true; });
}
function openClock() {
  if (F().clock) return E.say('The clock’s little door stands open.');
  E.cycler('Grandfather clock', 'The clock has stopped. You can move the hour hand.', [{ name: 'Hour', opts: HOURS }], v => { if (v[0] !== '12') return false; F().clock = 1; E.give('wand'); E.say('BONG! BONG! The clock strikes twelve and a little door opens. Inside lies a wand!'); return true; }, 'Tick… tock… nothing.', 'Let it chime');
}
function openCircle() {
  if (!F().potionIn) return E.say('A magic circle painted on the floor. In the middle: “Potion first, then the wand, then the spell.”');
  if (!F().wandIn) return E.say('The circle glows silver. Now the wand.');
  E.wordLock('Say the spell', 'Sparks dance in the circle, waiting for a four-letter word.', 4, w => { if (w !== 'HOME') return false; E.win(); return true; }, 'The sparks fizzle. That’s not the spell.');
}
});
