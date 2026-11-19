/* Six Clues escape room #32 – The Gingerbread House (level 1, family). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const ginger = c => `<rect width="1600" height="900" fill="${c}"/>${Array.from({ length: 16 }, (_, i) => `<path d="M${i * 100} 40 q50 30 100 0" fill="none" stroke="#fff" stroke-width="8"/>`).join('')}<rect y="640" width="1600" height="260" fill="#6a3a1a"/><ellipse cx="800" cy="0" rx="520" ry="300" fill="url(#lamp)"/>`;
const COLS = ['Red', 'White', 'Green', 'Gold'];

return {
  start: 'kitchen', v: 1,
  items: {
    bag: ['🧁', 'Empty piping bag', 'A cloth piping bag. Empty.'],
    icing: ['🍬', 'Tube of icing', 'A big tube of thick white icing – the glue of every gingerbread house.'],
    fullBag: ['🎂', 'Piping bag of icing', 'A piping bag full of sticky white icing.'],
    sugarKey: ['🔑', 'Sugar key', 'A key made of hard pink sugar. Don’t lick it!'],
  },
  rooms: {
    kitchen: {
      name: 'The gingerbread kitchen',
      bg: () => ginger('#a0602a'),
      spots: [
        { id: 'window', x: 80, y: 100, w: 380, h: 320, art: () => `<rect x="100" y="120" width="340" height="240" fill="#cfe4f4" stroke="#fff" stroke-width="14"/>${[['#d33', 3], ['#3a3', 5], ['#ec3', 8]].map(([c, n], k) => Array.from({ length: n }, (_, i) => `<circle cx="${115 + i * 40}" cy="${135 + k * 100}" r="13" fill="${c}"/>`).join('')).join('')}${L(270, 410, 'Window with gumdrops')}`,
          act: () => { E.note('window', 'Gumdrops on the window frame: 3 red, 5 green, 8 yellow.'); E.say('The window frame is decorated with gumdrops: 3 red, 5 green and 8 yellow.'); } },
        { id: 'cupboard', x: 520, y: 340, w: 360, h: 300, art: () => `<rect x="540" y="360" width="320" height="260" fill="#7a4a1a" stroke="#fff" stroke-width="8"/>${L(700, 650, F().cupboard ? 'Candy cupboard (open)' : 'Candy cupboard (3 numbers)')}`, act: () => openCupboard() },
        { id: 'door', x: 1000, y: 120, w: 460, h: 520, art: () => `<path d="M1060 640 V260 Q1230 120 1400 260 V640z" fill="#e05090"/><circle cx="1230" cy="300" r="70" fill="none" stroke="#2a8a3a" stroke-width="22"/>${L(1230, 680, F().wreath ? 'Candy door – a keyhole!' : 'Candy door with a wreath')}`,
          act: () => F().wreath ? E.say('A little pink keyhole has appeared under the wreath.') : openWreath(),
          use: { sugarKey: () => { if (!F().wreath) { E.say('There’s no keyhole anywhere! Maybe the wreath is part of the lock.'); return true; } E.take('sugarKey'); E.win(); return true; } } },
        { id: 'toParlour', x: 20, y: 740, w: 340, h: 130, art: () => E.exit('← Candy parlour'), act: () => E.go('parlour') },
      ],
    },
    parlour: {
      name: 'The candy parlour',
      bg: () => ginger('#c07a3a'),
      spots: [
        { id: 'back', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Kitchen →', 1240), act: () => E.go('kitchen') },
        { id: 'painting', x: 80, y: 100, w: 360, h: 300, art: () => `<rect x="100" y="120" width="320" height="240" fill="#f4e4c4" stroke="#c9a24a" stroke-width="12"/><circle cx="260" cy="240" r="70" fill="none" stroke="#2a8a3a" stroke-width="20"/>${L(260, 400, 'Painting of a wreath')}`,
          act: () => { E.note('painting', 'Painting “Grandma Ginny’s front-door wreath”: a white candy at the top, a red candy on the left, a green candy on the right.'); E.say('A painting called “Grandma Ginny’s front-door wreath”: a white candy at the top, a red one on the left and a green one on the right.'); } },
        { id: 'jar', x: 520, y: 380, w: 300, h: 260, art: () => `<rect x="560" y="420" width="220" height="200" rx="40" fill="#cfe4f4" opacity=".7"/>${L(670, 650, 'Candy cane jar')}`,
          act: () => { if (F().icing) return E.say('Just candy canes now. Very stripy.'); F().icing = 1; E.give('icing'); E.say('Under the candy canes you find a big tube of white icing!'); } },
        { id: 'stairs', x: 900, y: 120, w: 560, h: 520, art: () => `${[0, 1, 2, 3, 4].map(i => `<rect x="${940 + i * 90}" y="${560 - i * 90}" width="100" height="40" fill="#a0602a" ${!F().stairs && i === 2 ? 'opacity=".2"' : ''}/>`).join('')}${L(1180, 640, F().stairs ? 'Stairs to the attic' : 'Stairs – one step broken')}`,
          act: () => F().stairs ? E.go('attic') : E.say('The gingerbread stairs go up to the attic – but the middle step has snapped in two. You’d need something to stick it back together.'),
          use: { icing: () => { E.say('The tube is too thick to squeeze neatly. You need something to pipe it with.'); return true; }, fullBag: () => { F().stairs = 1; E.take('fullBag'); E.say('Squish, squish – you pipe a thick line of icing and press the step back together. It holds!'); return true; } } },
      ],
    },
    attic: {
      name: 'The attic',
      bg: () => `<rect width="1600" height="900" fill="#5a3418"/><path d="M0 0 L800 -100 L1600 0 V120 H0z" fill="#3a2010"/><rect y="640" width="1600" height="260" fill="#3a2010"/><ellipse cx="800" cy="0" rx="520" ry="300" fill="url(#lamp)"/>`,
      spots: [
        { id: 'back', x: 20, y: 740, w: 340, h: 130, art: () => E.exit('← Down the stairs'), act: () => E.go('parlour') },
        { id: 'cookies', x: 120, y: 200, w: 600, h: 300, art: () => `<rect x="140" y="420" width="560" height="20" fill="#3a2010"/>${[[60, 'R', 20], [80, 'G', 40], [120, 'S', 70], [100, 'U', 55], [70, 'A', 30]].map(([s, c, r], i) => `<circle cx="${210 + i * 110}" cy="${420 - r}" r="${r}" fill="#c07a3a"/><text x="${210 + i * 110}" y="${428 - r}" font-size="${r}" text-anchor="middle" fill="#fff">${c}</text>`).join('')}${L(420, 490, 'Shelf of letter cookies')}`,
          act: () => { E.note('cookies', 'Letter cookies on the shelf: a tiny R, a middle-sized G, the biggest S, a big U and a small A.'); E.say('Five round cookies with icing letters: a tiny R, a middle-sized G, the biggest one is S, a big U and a small A.'); } },
        { id: 'chest', x: 820, y: 380, w: 520, h: 260, art: () => `<rect x="860" y="440" width="440" height="180" fill="#e05090" stroke="#fff" stroke-width="8"/>${L(1080, 650, F().chest ? 'Candy chest (open)' : 'Candy chest (5 letters)')}`, act: () => openChest() },
      ],
    },
  },
  combine: (a, b) => { if ([a, b].sort().join() === 'bag,icing') { E.take('bag'); E.take('icing'); E.give('fullBag'); F().fullBag = 1; E.say('You squeeze the icing into the piping bag. Perfect for repairs!'); return true; } return false; },
  stages: [
    ['cupboard', () => F().cupboard, ['The candy cupboard has three number wheels.', 'Read the note on the cupboard, then look at the window.', 'Green 5, red 3, yellow 8: 538.']],
    ['icing', () => F().icing, ['The stairs need glue. What glues gingerbread?', 'Look in the candy cane jar in the parlour.', 'Take the icing from the jar.']],
    ['fullBag', () => F().fullBag, ['The icing tube is too thick on its own.', 'You found an empty piping bag in the cupboard.', 'Combine the piping bag with the icing.']],
    ['stairs', () => F().stairs, ['The attic stairs are broken.', 'Icing is gingerbread glue.', 'Use the piping bag of icing on the stairs.']],
    ['chest', () => F().chest, ['The candy chest wants five letters.', 'The cookies on the shelf – but in which order? Read the chest.', 'Biggest to smallest: S, U, G, A, R – SUGAR.']],
    ['wreath', () => F().wreath, ['The front door has no keyhole… yet.', 'The wreath has three candy spots. A painting shows how it should look.', 'Top white, left red, right green.']],
    ['door', () => F().won, ['The keyhole is showing.', 'You have the sugar key.', 'Use the sugar key on the candy door.']],
  ],
  intro: ['The Christmas fair · 11:30', 'The Gingerbread House',
    `<p>Grandma Ginny has built a gingerbread house so big you can walk inside it – her entry for the Christmas fair. You stepped in for a closer look… and the candy door clicked shut behind you!</p><p>The judges arrive at noon. Find the sugar key and get out before they do.</p><p>Level 1: perfect for families and first-time players.</p>`,
    'It smells of cinnamon and warm honey. Everything is edible – but please don’t eat the walls. Look around.'],
  timesUp: ['The judges are here!', 'They’re knocking on the candy door… keep going!'],
  win: ['Sweet freedom!', 'The candy door swings open and you step out into the snow just as the judges arrive. They take one look at the perfect wreath and the mended stairs – and give Grandma Ginny first prize!'],
};

function openCupboard() {
  if (F().cupboard) return E.say('The cupboard is empty now.');
  E.numLock('Candy cupboard', 'Three number wheels. A note in icing: “Count my window gumdrops – green, then red, then yellow.”', 3, c => { if (c !== '538') return false; F().cupboard = 1; E.give('bag'); E.say('The cupboard opens. Inside: an empty piping bag.'); return true; });
}
function openChest() {
  if (F().chest) return E.say('The chest is empty.');
  E.wordLock('Candy chest', 'Five letter wheels. Painted on the lid: “Line up my cookies, biggest to smallest.”', 5, w => { if (w !== 'SUGAR') return false; F().chest = 1; E.give('sugarKey'); E.say('The lid pops open. Inside, on a doily: a key made of pink sugar!'); return true; });
}
function openWreath() {
  E.cycler('The wreath', 'Three empty candy spots on the wreath. Pick a candy for each.', ['Top', 'Left', 'Right'].map(n => ({ name: n, opts: COLS })), v => { if (v.join() !== 'White,Red,Green') return false; F().wreath = 1; E.say('Click! The wreath turns, and a little pink keyhole appears in the door.'); return true; }, 'The candies wobble and fall out.');
}
});
