/* Six Clues escape room #35 – Locked In the Mall (level 1, family, Black Friday). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const mall = c => `<rect width="1600" height="900" fill="${c}"/>${Array.from({ length: 8 }, (_, i) => `<rect x="${i * 200 + 40}" y="0" width="120" height="40" fill="#fff" opacity=".15"/>`).join('')}<rect y="640" width="1600" height="260" fill="#cfcac0"/>`;
const BAGS = ['Red', 'Blue', 'Green', 'Yellow'];

return {
  start: 'atrium', v: 2,
  items: {
    coin: ['🪙', 'Big gold token', 'A chunky gold token with a smiling carousel horse on it.'],
    badge: ['🪪', 'Staff badge', 'A staff key card: “MALL SECURITY – Bob”.'],
    keys: ['🔑', 'Main door keys', 'A heavy ring of keys labelled “MAIN DOORS”.'],
  },
  rooms: {
    atrium: {
      name: 'The mall atrium',
      bg: () => mall('#3a4258'),
      spots: [
        { id: 'sign', photo: [135, 50, 265, 250], x: 80, y: 100, w: 400, h: 280, art: () => `<rect x="100" y="120" width="360" height="220" fill="#111"/><text x="280" y="250" font-size="54" fill="#f33" text-anchor="middle">−70%</text>${L(280, 380, 'Black Friday sign')}`,
          act: () => { E.note('sign', 'Big sign: “BLACK FRIDAY! Spend 3 bags, get 1 free – lucky colours today: RED, then YELLOW, then BLUE.”'); E.say('A flashing sign: “BLACK FRIDAY! Lucky colours today: RED, then YELLOW, then BLUE.”'); } },
        { id: 'ride', photo: [600, 330, 270, 400], x: 540, y: 340, w: 380, h: 300, art: () => `<ellipse cx="730" cy="600" rx="170" ry="40" fill="#c9a24a"/><rect x="700" y="400" width="60" height="200" fill="#c33"/>${L(730, 640, F().ride ? 'Carousel ride (played)' : 'Kiddie carousel ride')}`,
          act: () => F().ride ? E.say('The little carousel has stopped. You already got its prize.') : E.say('A coin-operated carousel ride for small children. The slot says: “1 GOLD TOKEN”.'),
          use: { coin: () => { F().ride = 1; E.take('coin'); E.give('badge'); E.say('Plink! The carousel jingles round once – and something clatters out of the prize chute: a staff badge with a lanyard. Bob the guard must have dropped it on the ride!'); return true; } } },
        { id: 'doors', photo: [950, 390, 300, 240], x: 980, y: 140, w: 360, h: 500, art: () => `<rect x="1000" y="160" width="320" height="460" fill="#9ab" opacity=".6" stroke="#ccc" stroke-width="10"/>${L(1160, 660, 'Main doors (locked)')}`,
          act: () => E.say('The big glass doors are locked for the night. Outside, your family waves at you from the car park!'),
          use: { keys: () => { E.take('keys'); E.win(); return true; } } },
        { id: 'fountain', photo: [1170, 540, 430, 280], x: 1360, y: 400, w: 220, h: 240, art: () => `<ellipse cx="1470" cy="600" rx="100" ry="30" fill="#6ab"/>${L(1470, 650, 'Fountain')}`,
          act: () => E.say('A little fountain full of wishing coins. Just pennies – nothing gold.') },
        { id: 'toToys', photo: [0, 320, 330, 380], x: 20, y: 740, w: 360, h: 130, art: () => E.exit('← Toy store'), act: () => E.go('toys') },
        { id: 'toSecurity', photo: [1390, 380, 180, 280], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit(F().sec ? 'Security office →' : 'Security office (badge)', 1240), act: () => F().sec ? E.go('security') : E.say('A grey door: “SECURITY – STAFF ONLY”. There’s a badge reader by the handle.'),
          use: { badge: () => { F().sec = 1; E.say('Beep! The green light flashes and the security office door clicks open.'); return true; } } },
      ],
    },
    toys: {
      name: 'The toy store',
      bg: () => mall('#5a2a3a'),
      spots: [
        { id: 'back', photo: [1350, 90, 250, 620], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Atrium →', 1240), act: () => E.go('atrium') },
        { id: 'bags', photo: [70, 520, 560, 270], x: 80, y: 360, w: 480, h: 280, art: () => `${BAGS.map((c, i) => `<rect x="${110 + i * 110}" y="460" width="80" height="120" fill="${['#c33', '#36c', '#3a3', '#ec3'][i]}"/>`).join('')}${L(320, 650, F().bags ? 'Shopping bags (done)' : 'Four shopping bags')}`, act: () => openBags() },
        { id: 'poster', photo: [710, 60, 400, 200], x: 640, y: 100, w: 360, h: 300, art: () => `${E.paper(660, 120, 320, 240, 4)}${L(820, 400, 'Store poster')}`,
          act: () => { E.note('poster', 'Toy store poster: “Black Friday surprise! Lift the lucky-colour bags in the right order to win the gold token.”'); E.say('“Black Friday surprise! Lift the lucky-colour bags in the right order to win the gold token.”'); } },
        { id: 'teddies', photo: [1010, 210, 340, 490], x: 1060, y: 160, w: 440, h: 420, art: () => `${[0, 1, 2].map(i => `<circle cx="${1140 + i * 130}" cy="420" r="50" fill="#a0602a"/>`).join('')}${L(1280, 600, 'Pile of teddies')}`,
          act: () => E.say('A mountain of half-price teddies. One has a tag: “Sold out by 7 a.m.!”') },
      ],
    },
    security: {
      name: 'The security office',
      bg: () => mall('#2a2e34'),
      spots: [
        { id: 'back', photo: [0, 0, 260, 800], x: 20, y: 740, w: 340, h: 130, art: () => E.exit('← Atrium'), act: () => E.go('atrium') },
        { id: 'screens', photo: [310, 25, 400, 430], x: 80, y: 80, w: 620, h: 340, art: () => `${[0, 1, 2, 3].map(i => `<rect x="${100 + (i % 2) * 300}" y="${100 + Math.floor(i / 2) * 150}" width="280" height="130" fill="#1c3a2a"/>`).join('')}${L(390, 440, 'CCTV screens')}`,
          act: () => { E.note('screens', 'CCTV, 21:00: Bob the guard hangs the main door keys in the key box, then sets the code by looking at the clock: hour, then minutes.'); E.say('On the replay: at exactly 9 o’clock, Bob hangs the main door keys in the key box, glances at the clock and taps in a code.'); } },
        { id: 'clock', photo: [860, 60, 230, 230], x: 780, y: 100, w: 260, h: 260, art: () => `<circle cx="910" cy="230" r="110" fill="#eee" stroke="#333" stroke-width="10"/>${L(910, 380, 'Wall clock')}`,
          act: () => E.say('A big round office clock. On the CCTV it showed exactly 21:00 when Bob locked the keys away.') },
        { id: 'keybox', photo: [1330, 180, 180, 260], x: 1100, y: 160, w: 380, h: 440, art: () => `<rect x="1120" y="180" width="340" height="380" fill="#555" stroke="#888" stroke-width="8"/>${L(1290, 600, F().box ? 'Key box (open)' : 'Key box (4 numbers)')}`, act: () => openBox() },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['bags', () => F().bags, ['The toy store has a game with shopping bags.', 'The Black Friday sign in the atrium lists the lucky colours.', 'Red, Yellow, Blue – then Green.']],
    ['ride', () => F().ride, ['You won a gold token.', 'Something in the atrium takes tokens.', 'Use the token on the carousel ride.']],
    ['sec', () => F().sec, ['You have Bob’s staff badge.', 'Which door has a badge reader?', 'Use the badge on the security office door.']],
    ['box', () => F().box, ['The key box wants four numbers.', 'Watch the CCTV – what time was it?', '21:00 → 2100.']],
    ['won', () => F().won, ['You have the main door keys.', 'Your family is waiting outside.', 'Use the keys on the main doors.']],
  ],
  intro: ['Brightside Mall · Black Friday · 21:30', 'Locked In the Mall',
    `<p>What a Black Friday! You were so busy hunting bargains that you didn’t hear the closing announcement – and now the lights are dim, the shutters are down and the mall is locked.</p><p>Your family is waving at you from the car park. Find a way to open the main doors!</p><p>Level 1: perfect for families and first-time players.</p>`,
    'The fountain gurgles in the empty atrium. A Black Friday sign is still flashing. Look around.'],
  timesUp: ['The night cleaners are coming!', 'You can still get out before they find you – keep going!'],
  win: ['Bargain of the day: freedom!', 'The keys turn, the glass doors slide open and you run out into the cold night air. Your family cheers – and the best deal of the whole Black Friday is a lift home.'],
};

function openBags() {
  if (F().bags) return E.say('The bags are empty now.');
  E.orderer('Four shopping bags', 'Lift the bags in the lucky order.', BAGS, v => { if (v.slice(0, 3).join() !== 'Red,Yellow,Blue') return false; F().bags = 1; E.give('coin'); E.say('Ta-da! Confetti bursts out of the blue bag – and a big gold token falls into your hand.'); return true; }, 'A sad little “bloop” – try again.');
}
function openBox() {
  if (F().box) return E.say('The key box is empty now.');
  E.numLock('Key box', 'A metal key box with four number wheels.', 4, c => { if (c !== '2100') return false; F().box = 1; E.give('keys'); E.say('The key box swings open: a heavy ring labelled “MAIN DOORS”!'); return true; });
}
});
