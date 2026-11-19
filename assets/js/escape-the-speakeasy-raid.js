/* Six Clues escape room #16 – The Speakeasy Raid (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const deco = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 10 }, (_, i) => `<path d="M${i * 170} 660 L${i * 170 + 85} 520 L${i * 170 + 170} 660" fill="${c2}"/>`).join('')}<rect y="660" width="1600" height="240" fill="#1a120c"/><ellipse cx="800" cy="0" rx="500" ry="300" fill="url(#lamp)"/>`;
const KNOBS = ['Off', 'Low', 'High'];

return {
  start: 'bar', v: 2,
  items: {
    officeKey: ['🗝️', 'Brass key', 'A brass key with a tag: OFFICE.'],
    cellarKey: ['🗝️', 'Cellar key', 'A long iron key: CELLAR.'],
    matches: ['🔥', 'Matches', 'A matchbook from “The Blue Parrot”.'],
    kettle: ['♨️', 'Kettle of hot water', 'A kettle of boiling water.'],
    tunnelKey: ['🔑', 'Tunnel key', 'A small steel key that was frozen in a block of ice.'],
    lantern: ['🏮', 'Oil lantern', 'An unlit oil lantern.'],
    lit: ['🔥', 'Lit lantern', 'An oil lantern, burning.'],
    ledger: ['📒', 'The real ledger', 'The boss’s real account book – every bribe, every name, the mayor’s too.'],
    card: ['🃏', 'Bouncer’s card', 'A playing card with pencil marks on the back.'],
  },
  rooms: {
    bar: {
      name: 'The Blue Parrot – bar room',
      bg: () => deco('#1e2a3a', '#26344a'),
      spots: [
        { id: 'menu', photo: [200, 20, 295, 280], x: 80, y: 120, w: 300, h: 300, art: () => `${E.paper(100, 140, 260, 240, 6)}${L(230, 420, 'Cocktail menu (gold print)')}`,
          act: () => { E.note('menu', 'Menu card, the boss’s specials printed in gold: Gin Fizz · Old Fashioned · Lemon Drop · Daiquiri.'); E.say('The boss’s specials, printed in gold: Gin Fizz, Old Fashioned, Lemon Drop, Daiquiri.'); } },
        { id: 'chalk', photo: [530, 75, 210, 255], x: 420, y: 100, w: 360, h: 220, art: () => `<rect x="440" y="120" width="320" height="170" fill="#1a2a1a"/>${L(600, 320, 'Chalkboard')}`,
          act: () => { E.note('chalk', 'Chalkboard: “Tonight – Bee’s Knees, Applejack, Rum Punch. Ask Sal!”'); E.say('“Tonight – Bee’s Knees, Applejack, Rum Punch. Ask Sal!”'); } },
        { id: 'piano', photo: [300, 420, 420, 325], x: 380, y: 400, w: 440, h: 260, art: () => `<rect x="400" y="440" width="400" height="180" fill="#120c08"/><rect x="420" y="560" width="360" height="30" fill="#eee"/>${L(600, 650, F().bench ? 'Piano (bench open)' : 'Piano – the bench has a letter lock')}`, act: () => openBench() },
        { id: 'coats', photo: [1025, 115, 300, 545], x: 900, y: 140, w: 300, h: 420, art: () => `<rect x="920" y="160" width="260" height="380" fill="#3a2a1a"/>${[0, 1, 2].map(i => `<rect x="${950 + i * 70}" y="200" width="50" height="160" fill="#4a3a3a"/>`).join('')}${L(1050, 580, 'Coat check')}`,
          act: () => { if (F().coats) return E.say('Coats and hats. Nothing else in the pockets.'); F().coats = 1; E.give('card'); E.give('matches'); E.note('card', 'Bouncer’s card (ace of spades). On the back in pencil: “Tunnel knock – 3, then 1, then 2.”'); E.say('In a coat pocket: a matchbook and a playing card. On the back: “Tunnel knock – 3, then 1, then 2.”'); } },
        { id: 'clock', photo: [1355, 40, 200, 195], x: 1240, y: 80, w: 220, h: 220, art: () => `<circle cx="1350" cy="190" r="90" fill="#e8dcb8" stroke="#c9a24a" stroke-width="10"/>${L(1350, 310, 'Bar clock')}`,
          act: () => E.say('A quarter past midnight. The tip-off said the Feds raid at one o’clock.') },
        { id: 'trap', photo: [1100, 715, 395, 125], x: 1240, y: 600, w: 340, h: 120, art: () => `<rect x="1260" y="620" width="300" height="80" fill="#2a1a10" stroke="#5a3a20" stroke-width="6"/>${L(1410, 740, F().cellar ? 'Trapdoor (open) ↓' : 'Trapdoor (locked)')}`,
          act: () => F().cellar ? E.go('cellar') : E.say('A trapdoor behind the bar. Locked with a heavy iron lock.'),
          use: { cellarKey: () => { F().cellar = 1; E.take('cellarKey'); E.say('The cellar key turns. Cold air and a smell of wine come up.'); return true; } } },
        { id: 'toOffice', photo: [0, 140, 180, 555], x: 20, y: 740, w: 340, h: 130, art: () => E.exit(F().office ? '← Boss’s office' : '← Office (locked)'), act: () => F().office ? E.go('office') : E.say('A frosted-glass door: PRIVATE. Locked.'),
          use: { officeKey: () => { F().office = 1; E.take('officeKey'); E.say('The office door clicks open.'); return true; } } },
        { id: 'toKitchen', photo: [760, 175, 240, 480], x: 520, y: 740, w: 340, h: 130, art: () => E.exit('Kitchen ↗', 540), act: () => E.go('kitchen') },
      ],
    },
    office: {
      name: 'The boss’s office',
      bg: () => deco('#2a1e1a', '#3a2a22'),
      spots: [
        { id: 'back', photo: [1400, 55, 200, 730], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Bar →', 1240), act: () => E.go('bar') },
        { id: 'photo', photo: [35, 40, 295, 260], x: 120, y: 120, w: 320, h: 260, art: () => `<rect x="140" y="140" width="280" height="200" fill="#c8b890" stroke="#c9a24a" stroke-width="10"/>${L(280, 380, 'Family photo')}`,
          act: () => { E.note('photo', 'Family photo, written on the back: “My girls – Maria 3, Rosa 8, Lucia 5. My luck, oldest first.”'); E.say('Three little girls in Sunday dresses. On the back: “My girls – Maria 3, Rosa 8, Lucia 5. My luck, oldest first.”'); } },
        { id: 'fakeLedger', photo: [490, 520, 340, 120], x: 500, y: 420, w: 380, h: 200, art: () => `<rect x="520" y="480" width="340" height="30" fill="#5a3a20"/><rect x="600" y="440" width="160" height="40" fill="#2a4a2a"/>${L(690, 640, 'Desk and account book')}`,
          act: () => { E.note('fake', 'The account book on the desk: just bar tabs and laundry bills. “The real one is never on the desk,” you think.'); E.say('An account book – but it’s only bar tabs and laundry bills. The real ledger must be hidden.'); } },
        { id: 'safe', photo: [875, 120, 245, 340], x: 960, y: 260, w: 340, h: 360, art: () => `<rect x="980" y="300" width="300" height="300" fill="#2a2a2a"/><circle cx="1130" cy="450" r="60" fill="#777"/>${L(1130, 640, F().safe ? 'Wall safe (open)' : 'Wall safe (3 numbers)')}`, act: () => openSafe() },
        { id: 'phone', photo: [1200, 275, 160, 180], x: 1340, y: 160, w: 220, h: 200, art: () => `<rect x="1370" y="220" width="160" height="100" fill="#111"/>${L(1450, 370, 'Telephone')}`,
          act: () => E.say('You lift the receiver. An operator: “Number, please?” – you put it down quickly.') },
      ],
    },
    kitchen: {
      name: 'The kitchen',
      bg: () => `<rect width="1600" height="900" fill="#3a3a32"/>${Array.from({ length: 16 }, (_, i) => `<rect x="${i * 100}" y="0" width="98" height="660" fill="${i % 2 ? '#e8e8e0' : '#d8d8d0'}" opacity=".15"/>`).join('')}<rect y="660" width="1600" height="240" fill="#2a2a24"/>`,
      spots: [
        { id: 'back', photo: [0, 0, 235, 765], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Bar'), act: () => E.go('bar') },
        { id: 'recipe', photo: [285, 70, 125, 220], x: 80, y: 120, w: 320, h: 260, art: () => `${E.paper(100, 140, 280, 200, 5)}${L(240, 380, 'Cook’s note')}`,
          act: () => { E.note('cook', 'Cook’s note by the stove: “The old stove is tricky! Front burner HIGH, back burner OFF, oven LOW – or the gas won’t catch. – Sal”'); E.say('“The old stove is tricky! Front burner HIGH, back burner OFF, oven LOW – or the gas won’t catch.”'); } },
        { id: 'stove', photo: [325, 340, 470, 475], x: 460, y: 340, w: 420, h: 300, art: () => `<rect x="480" y="400" width="380" height="220" fill="#1a1a1a"/>${[0, 1, 2].map(i => `<circle cx="${560 + i * 110}" cy="580" r="22" fill="#888"/>`).join('')}${L(670, 660, F().stove ? 'Stove (kettle boiled)' : 'Gas stove with a kettle')}`, act: () => openStove() },
        { id: 'icebox', photo: [915, 125, 405, 655], x: 960, y: 200, w: 300, h: 440, art: () => `<rect x="980" y="220" width="260" height="400" fill="#b8c8c8"/>${L(1110, 660, 'Icebox')}`,
          act: () => F().ice ? E.say('Melting ice and a side of beef.') : E.say('A big block of ice. Frozen inside it you can see a small steel key! You can’t chip it out.'),
          use: { kettle: () => { F().ice = 1; E.take('kettle'); E.give('tunnelKey'); E.say('You pour the boiling water over the ice. It cracks and melts – and the steel key drops out!'); return true; } } },
        { id: 'shelf', photo: [1325, 0, 275, 625], x: 1300, y: 140, w: 260, h: 300, art: () => `<rect x="1320" y="160" width="220" height="240" fill="#5a3a20"/>${L(1430, 440, 'Kitchen shelf')}`,
          act: () => { if (F().lanternTaken) return E.say('Pots and pans.'); F().lanternTaken = 1; E.give('lantern'); E.say('Behind the pans: an old oil lantern, unlit.'); } },
      ],
    },
    cellar: {
      name: 'The wine cellar',
      bg: () => `<rect width="1600" height="900" fill="#14100c"/><path d="M0 0 Q800 160 1600 0" fill="#0c0806"/><rect y="660" width="1600" height="240" fill="#1e1610"/>`,
      spots: [
        { id: 'up', photo: [0, 495, 480, 405], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('↑ Bar'), act: () => E.go('bar') },
        { id: 'rack', photo: [175, 40, 510, 450], x: 100, y: 120, w: 560, h: 480, art: () => `<rect x="120" y="140" width="520" height="440" fill="#2a1a10"/>${Array.from({ length: 20 }, (_, i) => `<circle cx="${170 + (i % 5) * 100}" cy="${190 + Math.floor(i / 5) * 100}" r="30" fill="#3a0a14"/>`).join('')}${L(380, 630, F().ledger ? 'Wine rack (empty slot)' : 'Wine rack')}`, act: () => openRack() },
        { id: 'tunnel', photo: [1205, 115, 355, 610], x: 980, y: 140, w: 480, h: 500, art: () => `<rect x="1000" y="160" width="440" height="460" rx="20" fill="#0a0806" stroke="#4a3a2a" stroke-width="12"/>${L(1220, 660, 'Steel door to the tunnel')}`, act: () => openTunnel(),
          use: { tunnelKey: () => { F().keyIn = 1; E.take('tunnelKey'); E.say('The steel key turns one of the locks. There is still a knocker and pitch dark beyond.'); return true; }, lit: () => { F().lightIn = 1; E.take('lit'); E.say('You hang the lantern on the hook by the door. Now you can see the knocker.'); return true; } } },
        { id: 'note', photo: [740, 410, 160, 170], x: 700, y: 400, w: 240, h: 200, art: () => `${E.paper(720, 420, 200, 140, 4)}${L(820, 590, 'Scrap of paper')}`,
          act: () => { E.note('wine', 'Scrap in the cellar, in the boss’s hand: “The book sleeps behind the year the country went dry.”'); E.say('“The book sleeps behind the year the country went dry.”'); } },
      ],
    },
  },
  combine: (a, b) => { if ([a, b].sort().join() === 'lantern,matches') { E.take('lantern'); E.take('matches'); E.give('lit'); F().lit = 1; E.say('You strike a match and light the lantern.'); return true; } return false; },
  stages: [
    ['bench', () => F().bench, ['The piano bench has a four-letter lock.', 'The boss’s specials are printed in gold. The chalkboard is just today’s drinks.', 'First letters: Gin, Old, Lemon, Daiquiri = GOLD.']],
    ['office', () => F().office, ['The bench held a key.', 'The office door says PRIVATE.', 'Use the brass key on the office door.']],
    ['safe', () => F().safe, ['The wall safe wants three numbers.', 'The family photo: his luck, oldest first.', 'Rosa 8, Lucia 5, Maria 3: 853.']],
    ['cellar', () => F().cellar, ['The safe held a cellar key.', 'The trapdoor behind the bar.', 'Use the cellar key on the trapdoor.']],
    ['ledger', () => F().ledger, ['The real ledger is in the cellar.', 'The scrap says: behind the year the country went dry.', 'Prohibition began in 1920.']],
    ['ice', () => F().ice, ['There is a key frozen in the icebox.', 'Boil the kettle – the stove is tricky.', 'Front HIGH, back OFF, oven LOW; then pour the hot water on the ice.']],
    ['lit', () => F().lit, ['The tunnel is dark.', 'There is a lantern in the kitchen and matches in the coat check.', 'Combine the lantern and the matches.']],
    ['tunnel', () => F().won, ['The tunnel door needs a key, light and the right knock.', 'Use the tunnel key and the lit lantern on the door.', 'Knock 3, 1, 2 – and have the ledger with you.']],
  ],
  intro: ['Chicago · 14 February 1927 · 00:15', 'The Speakeasy Raid',
    `<p>You are a reporter for the Chicago Daily Clarion, undercover at the Blue Parrot – the speakeasy where the mayor’s men drink for free. Somewhere in here is the boss’s real ledger, with every bribe written down.</p><p>The bartender caught you snooping and locked every door. Worse: a tip-off says the Feds raid the place at one o’clock. Find the ledger and get out through the smugglers’ tunnel before the sirens.</p><p>Level 2: some menus lie, and some account books are only for show.</p>`,
    'Smoke, jazz on the gramophone and a locked front door. Look around.'],
  timesUp: ['Sirens!', 'Whistles and boots upstairs… you can still finish, but off the leaderboard.'],
  win: ['Through the tunnel', 'You come up in a laundry two streets away with the ledger under your coat. Next morning the Clarion’s front page names every bribe – and the mayor’s too.'],
};

function openBench() {
  if (F().bench) return E.say('The piano bench is open: sheet music and dust.');
  E.wordLock('Piano bench', 'The bench lid has four letter wheels, engraved: “What the boss likes best.”', 4, w => { if (w !== 'GOLD') return false; F().bench = 1; E.give('officeKey'); E.say('The bench lid lifts: sheet music – and a brass key tagged OFFICE.'); return true; });
}
function openSafe() {
  if (F().safe) return E.say('The safe is empty except for a stack of cash. You leave it – you’re a reporter, not a crook.');
  E.numLock('Wall safe', 'A heavy safe with three number wheels.', 3, c => { if (c !== '853') return false; F().safe = 1; E.give('cellarKey'); E.say('The safe swings open: cash, a pistol you don’t touch – and a long iron key marked CELLAR.'); return true; });
}
function openStove() {
  if (F().stove) return E.say('The stove is off. You already boiled the kettle.');
  E.cycler('Gas stove', 'Three gas knobs.', ['Front burner', 'Back burner', 'Oven'].map(n => ({ name: n, opts: KNOBS })), v => { if (v.join() !== 'High,Off,Low') return false; F().stove = 1; E.give('kettle'); E.say('Whoomph – the gas catches. A few minutes later the kettle whistles. You take it.'); return true; }, 'Hiss… a smell of gas. You turn it off fast.', 'Strike a match');
}
function openRack() {
  if (F().ledger) return E.say('An empty slot where the 1920 bottle was.');
  E.numLock('Wine rack', 'Dusty bottles with year labels: 1912, 1915, 1917, 1919, 1920, 1921, 1923, 1926… Which year’s bottle do you pull out?', 4, c => { if (c !== '1920') return false; F().ledger = 1; E.give('ledger'); E.say('Behind the 1920 bottle: a thick black book – the real ledger! Every bribe, every name.'); return true; }, 'Just wine behind that one.');
}
function openTunnel() {
  if (!F().keyIn || !F().lightIn) return E.say(`A steel door with a lock, a knocker and a lantern hook. ${F().keyIn ? 'Unlocked.' : 'Locked.'} ${F().lightIn ? 'Lit.' : 'Too dark to see the knocker.'}`);
  if (!E.has('ledger')) return E.say('You could knock and go… but without the real ledger, tonight was for nothing.');
  E.numLock('Tunnel knocker', 'Someone on the other side waits for the right knock. How many knocks each time?', 3, c => { if (c !== '312') return false; E.win(); return true; }, 'Silence on the other side.');
}
});
