/* Six Clues escape room #27 – The Berlin Safehouse (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const flat = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 20 }, (_, i) => `<rect x="${i * 80}" y="0" width="2" height="660" fill="${c2}"/>`).join('')}<rect y="660" width="1600" height="240" fill="#3a3028"/><ellipse cx="800" cy="0" rx="500" ry="300" fill="url(#lamp)"/>`;
const RECORDS = ['Bach – Mass in B minor', 'Mozart – Requiem', 'Beethoven – Symphony No. 5', 'Wagner – Ride of the Valkyries'];
const TRAYS = ['Fixer', 'Developer', 'Stop bath', 'Water'];

return {
  start: 'flat', v: 1,
  items: {
    film: ['🎞️', 'Microfilm (undeveloped)', 'A tiny roll of film, hidden in a record sleeve.'],
    photo: ['🖼️', 'Developed photo', 'A photograph of a cellar door and a mailbox – the escape route.'],
    passport: ['📘', 'Blank passport', 'A West German passport with no stamp.'],
    stamp: ['🔖', 'Rubber stamp', 'An official exit stamp, stolen from a border office.'],
    papers: ['📗', 'Travel papers', 'A stamped passport in your new name.'],
    pad: ['📄', 'One-time pad', 'A strip of paper with numbers and letters – a code key.'],
  },
  rooms: {
    flat: {
      name: 'The safe flat',
      bg: () => flat('#4a4a3a', '#3e3e30'),
      spots: [
        { id: 'radio', x: 80, y: 360, w: 360, h: 280, art: () => `<rect x="100" y="420" width="320" height="180" rx="16" fill="#6a4a2a"/><circle cx="360" cy="510" r="36" fill="#c9a24a"/>${L(260, 640, 'Shortwave radio')}`,
          act: () => { E.note('radio', 'Shortwave radio, numbers station at midnight: a woman’s voice reads “Achtung – 3 – 1 – 4 – 1 – 5”. Earlier, at 23:00, a test broadcast: “8 – 8 – 8 – 8 – 8” (ignore tests!).'); E.say('A numbers station: “Achtung – 3 – 1 – 4 – 1 – 5.” (The 23:00 broadcast was only a test: “8-8-8-8-8”.)'); } },
        { id: 'books', x: 500, y: 100, w: 400, h: 300, art: () => `<rect x="520" y="120" width="360" height="240" fill="#5a3a20"/>${[0, 1, 2, 3, 4, 5].map(i => `<rect x="${540 + i * 55}" y="160" width="40" height="160" fill="${['#8a2a2a', '#2a4a8a', '#2a6a3a', '#8a7a2a', '#5a2a6a', '#2a2a2a'][i]}"/>`).join('')}${L(700, 400, 'Bookshelf')}`,
          act: () => { if (F().pad) return E.say('Poetry and a phone book.'); F().pad = 1; E.give('pad'); E.note('pad', 'One-time pad hidden in a poetry book: 1=A 2=B 3=C 4=D 5=E … and the line “Cellar code = the digits of the midnight message, minus the test.”'); E.say('Inside a poetry book: a one-time pad. “Cellar code = the digits of the midnight message.”'); } },
        { id: 'records', x: 960, y: 380, w: 400, h: 260, art: () => `<rect x="980" y="440" width="360" height="160" fill="#2a2a2a"/><circle cx="1160" cy="500" r="50" fill="#111"/>${L(1160, 640, 'Record player and records')}`, act: () => openRecords() },
        { id: 'postcard', x: 960, y: 100, w: 320, h: 220, art: () => `${E.paper(980, 120, 280, 160, 4)}${L(1120, 320, 'Postcard on the wall')}`,
          act: () => { E.note('postcard', 'Postcard from your handler, “Onkel Max”: “Remember how fate knocks at the door? Listen to it once more – it holds what you need.”'); E.say('“Remember how fate knocks at the door? Listen to it once more – it holds what you need.”'); } },
        { id: 'toDark', x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Darkroom'), act: () => E.go('dark') },
        { id: 'toStairs', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Stairwell →', 1240), act: () => E.go('stairs') },
      ],
    },
    dark: {
      name: 'The darkroom',
      bg: () => `<rect width="1600" height="900" fill="#3a0a0a"/><rect y="660" width="1600" height="240" fill="#1a0505"/><circle cx="800" cy="60" r="50" fill="#e02020" opacity=".6"/>`,
      spots: [
        { id: 'back', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Flat →', 1240), act: () => E.go('flat') },
        { id: 'chart', x: 100, y: 120, w: 340, h: 260, art: () => `${E.paper(120, 140, 300, 200, 5)}${L(270, 380, 'Darkroom chart')}`,
          act: () => { E.note('chart', 'Darkroom chart: “Developing film: 1. Developer 2. Stop bath 3. Fixer 4. Water. Wrong order = blank film!”'); E.say('“1. Developer 2. Stop bath 3. Fixer 4. Water. Wrong order = blank film!”'); } },
        { id: 'trays', x: 500, y: 420, w: 700, h: 220, art: () => `${[0, 1, 2, 3].map(i => `<rect x="${520 + i * 170}" y="500" width="140" height="80" fill="#5a5a5a"/>`).join('')}${L(850, 620, F().developed ? 'Trays (done)' : 'Four developing trays')}`, act: () => openTrays() },
        { id: 'line', x: 500, y: 100, w: 700, h: 200, art: () => `<path d="M520 160 H1180" stroke="#888" stroke-width="4"/>${L(850, 260, 'Drying line')}`,
          act: () => E.say('Old photos pegged on a line: tourists at the Brandenburg Gate, a dog, a birthday cake.') },
      ],
    },
    stairs: {
      name: 'The stairwell',
      bg: () => flat('#5a5a50', '#4a4a42'),
      spots: [
        { id: 'back', x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Flat'), act: () => E.go('flat') },
        { id: 'mailboxes', x: 100, y: 200, w: 600, h: 360, art: () => `${Array.from({ length: 12 }, (_, i) => `<rect x="${130 + (i % 4) * 140}" y="${230 + Math.floor(i / 4) * 100}" width="110" height="80" fill="#6a6a5a"/>`).join('')}${L(400, 600, 'Mailboxes')}`, act: () => openMailbox() },
        { id: 'window', x: 900, y: 100, w: 400, h: 400, art: () => `<rect x="920" y="120" width="360" height="340" fill="#1a2030"/>${L(1100, 500, 'Stairwell window')}`,
          act: () => E.say('Down in the street, soldiers are unrolling barbed wire across the road. Trucks full of concrete posts. By morning, the city will be cut in two.') },
        { id: 'toCellar', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Cellar ↓', 1240), act: () => E.go('cellar') },
      ],
    },
    cellar: {
      name: 'The cellar',
      bg: () => `<rect width="1600" height="900" fill="#1e1a16"/><path d="M0 0 Q800 160 1600 0" fill="#141210"/><rect y="660" width="1600" height="240" fill="#141210"/>`,
      spots: [
        { id: 'up', x: 20, y: 740, w: 300, h: 130, art: () => E.exit('↑ Stairwell'), act: () => E.go('stairs') },
        { id: 'coal', x: 200, y: 300, w: 500, h: 340, art: () => `<rect x="220" y="320" width="460" height="300" fill="#2a2a2a"/>${L(450, 650, 'Coal bunker door (5 numbers)')}`, act: () => openCoal() },
        { id: 'bikes', x: 900, y: 300, w: 500, h: 300, art: () => `<circle cx="1000" cy="540" r="60" fill="none" stroke="#888" stroke-width="8"/><circle cx="1200" cy="540" r="60" fill="none" stroke="#888" stroke-width="8"/>${L(1100, 630, 'Old bicycles')}`,
          act: () => E.say('Rusty bicycles and a pram. Nothing useful – but a draught of cold air comes from behind the coal bunker.') },
      ],
    },
  },
  combine: (a, b) => { if ([a, b].sort().join() === 'passport,stamp') { E.take('passport'); E.take('stamp'); E.give('papers'); F().papers = 1; E.say('You press the exit stamp into the passport. Your travel papers are ready.'); return true; } return false; },
  stages: [
    ['record', () => F().record, ['The postcard talks about fate knocking at the door.', 'Which piece of music is famous for “fate knocking”?', 'Beethoven – Symphony No. 5.']],
    ['developed', () => F().developed, ['The microfilm must be developed.', 'Follow the darkroom chart.', 'Developer, Stop bath, Fixer, Water.']],
    ['mailbox', () => F().mailbox, ['The photo shows a mailbox.', 'Its number is in the developed photo.', 'Mailbox 7.']],
    ['papers', () => F().papers, ['You have a blank passport and a stamp.', 'Combine them.', 'Tap the passport, then the stamp.']],
    ['coal', () => F().won, ['The coal bunker hides the tunnel.', 'The midnight numbers broadcast – not the test.', '31415 – and have your papers with you.']],
  ],
  intro: ['East Berlin · 13 August 1961 · 02:00', 'The Berlin Safehouse',
    `<p>You are a courier for the West. Tonight, without warning, soldiers began building a wall straight through Berlin. Your contact never came – but he left everything you need somewhere in this safe flat.</p><p>At dawn the last way out will be sealed. Find the microfilm, make your papers and reach the tunnel before the city is cut in two.</p><p>Level 2: not every broadcast is a real message.</p>`,
    'Peeling wallpaper, a dripping tap and engines in the street. Look around.'],
  timesUp: ['Dawn.', 'The wire is up across the street. You can still finish, but off the leaderboard.'],
  win: ['Under the wall', 'Behind the coal bunker a narrow tunnel runs under the street. Twenty minutes later you climb out into a West Berlin bakery, coal-black, with the microfilm in your sock. The baker hands you a coffee without a word.'],
};

function openRecords() {
  if (F().record) return E.say('The Beethoven sleeve is empty now.');
  E.cycler('Record player', 'Four records in their sleeves. Which one do you play?', [{ name: 'Record', opts: RECORDS }], v => { if (v[0] !== 'Beethoven – Symphony No. 5') return false; F().record = 1; E.give('film'); E.say('Da-da-da-DUM! As you pull the record out, a tiny roll of microfilm drops out of the sleeve.'); return true; }, 'Lovely music. But nothing hidden in that sleeve.', 'Play');
}
function openTrays() {
  if (F().developed) return E.say('The trays are empty now.');
  if (!E.has('film')) return E.say('Four empty developing trays. You have nothing to develop – yet.');
  E.orderer('Developing trays', 'Dip the film in the trays – tap them in order.', TRAYS, v => { if (v.join() !== 'Developer,Stop bath,Fixer,Water') return false; F().developed = 1; E.take('film'); E.give('photo'); E.note('photo', 'The developed photo: a coal bunker door in a cellar, chalked “TUNNEL”, and mailbox number 7 in this building with a note: “Papers in box 7. Key: the year Berlin was founded – 1237.”'); E.say('The picture appears: a coal bunker chalked TUNNEL – and “Papers in mailbox 7. Key: 1237.”'); return true; }, 'The film turns black. Lucky it was only a test strip – try again.');
}
function openMailbox() {
  if (F().mailbox) return E.say('Mailbox 7 is empty now.');
  if (!F().developed) return E.say('Twelve mailboxes with little number locks. Which one? You don’t know yet.');
  E.numLock('Mailbox 7', 'A little lock with four number wheels.', 4, c => { if (c !== '1237') return false; F().mailbox = 1; E.give('passport'); E.give('stamp'); E.say('Inside mailbox 7: a blank West German passport and a stolen exit stamp.'); return true; });
}
function openCoal() {
  if (!E.has('papers')) return E.say('A coal bunker door with five number wheels. Even if you get through, without papers you’ll be arrested on the other side.');
  E.numLock('Coal bunker door', 'Five number wheels.', 5, c => { if (c !== '31415') return false; E.win(); return true; }, 'The lock doesn’t budge.');
}
});
