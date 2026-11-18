/* Six Clues escape room #9 – The Codebreakers' Hut (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const PLAIN = 'CONVOY SC TWELVE ATTACK AT SIX GRID SQUARE AJ THIRTY SEVEN';
const KEY = 'BLQ';
// a simple three-wheel Vigenère-style machine: wheel letters repeat over the message
const crypt = (t, key, dir) => { let i = 0; return t.replace(/[A-Z]/g, c => { const k = A.indexOf(key[i++ % key.length]); return A[(A.indexOf(c) + dir * k + 26) % 26]; }); };
const TAPE = crypt(PLAIN, KEY, 1);
const hut = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 10 }, (_, i) => `<rect x="${i * 160}" y="0" width="10" height="660" fill="${c2}"/>`).join('')}<rect y="660" width="1600" height="240" fill="#2a2420"/><ellipse cx="800" cy="0" rx="560" ry="360" fill="url(#lamp)"/>`;
const CROSS = [['A chess piece that moves in straight lines', 4], ['A woodwind instrument with a reed', 4], ['What keeps Hut 9 awake at 3 a.m.', 3], ['A night bird', 3], ['Typical English weather', 4]];

return {
  start: 'hut', v: 1,
  items: {
    pass: ['🪪', 'Commander’s pass', 'Commander Hale’s pass for the mansion – found in his greatcoat.'],
    keysheet: ['📄', 'Key sheet', 'The machine key sheet for May 1943. TOP SECRET.'],
    teleKey: ['🗝️', 'Teleprinter key', 'A small key labelled “Teleprinter – lock”.'],
    ribbon: ['🎞️', 'Ink ribbon', 'A fresh teleprinter ink ribbon in a tin.'],
  },
  rooms: {
    hut: {
      name: 'Hut 9 – the office',
      bg: () => hut('#4a4436', '#3e392d'),
      spots: [
        { id: 'crossword', x: 80, y: 420, w: 380, h: 240, art: () => `<rect x="100" y="460" width="340" height="40" fill="#5b3c25"/>${E.paper(160, 400, 200, 70, 2)}${L(270, 690, 'Desk with a crossword')}`, act: () => openCrossword() },
        { id: 'cabinet', x: 500, y: 200, w: 260, h: 460, art: () => `<rect x="520" y="220" width="220" height="420" fill="#556050"/>${L(630, 690, F().cabinet ? 'Filing cabinet (open)' : 'Filing cabinet (letter lock)')}`, act: () => openCabinet() },
        { id: 'calendar', x: 800, y: 100, w: 260, h: 260, art: () => `${E.paper(820, 120, 220, 200, 5)}${L(930, 360, 'Wall calendar')}`, act: () => openCalendar() },
        { id: 'coat', x: 1100, y: 120, w: 180, h: 440, art: () => `<path d="M1190 140 L1130 200 L1120 540 L1260 540 L1250 200z" fill="#2c3440"/>${L(1190, 580, 'Greatcoat on a hook')}`,
          act: () => { if (F().pass) return E.say('The Commander’s greatcoat. Empty pockets now.'); F().pass = 1; E.give('pass'); E.say('In the greatcoat pocket: Commander Hale’s pass for the mansion.'); } },
        { id: 'toMachine', x: 1320, y: 120, w: 260, h: 540, art: () => E.door(1340, 160, 220, 480, true, 'Machine room →'), act: () => E.go('machine') },
        { id: 'toTele', x: 20, y: 740, w: 340, h: 130, art: () => E.exit('← Teleprinter room'), act: () => E.go('tele') },
        { id: 'toMansion', x: 600, y: 740, w: 420, h: 130, art: () => E.exit(F().mansion ? '↓ Path to the mansion' : '↓ Path to the mansion (guard)', 620),
          act: () => F().mansion ? E.go('library') : E.say('A sentry stops you at the mansion door. “Pass, please.”'),
          use: { pass: () => { F().mansion = 1; E.take('pass'); E.say('The sentry salutes the Commander’s pass. “Library’s on the left.”'); E.go('library'); return true; } } },
      ],
    },
    machine: {
      name: 'The machine room',
      bg: () => hut('#3a3a36', '#2e2e2a'),
      spots: [
        { id: 'back', x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Hut office'), act: () => E.go('hut') },
        { id: 'typex', x: 360, y: 240, w: 560, h: 420, art: () => `<rect x="380" y="380" width="520" height="260" rx="10" fill="#2a2a2a"/>${[0, 1, 2].map(i => `<circle cx="${520 + i * 120}" cy="330" r="44" fill="#c9a24a"/><text x="${520 + i * 120}" y="342" text-anchor="middle" font-size="34" fill="#111">${(F().rotors || '???')[i]}</text>`).join('')}${L(640, 690, 'Cipher machine (three wheels)')}`, act: () => openMachine() },
        { id: 'tape', x: 980, y: 300, w: 300, h: 300, art: () => `<rect x="1000" y="420" width="260" height="140" fill="#8a7a5a"/>${L(1130, 600, 'Tray of intercepts')}`, act: () => openTape() },
        { id: 'board', x: 1320, y: 100, w: 260, h: 360, art: () => `${E.paper(1340, 120, 220, 300, 8)}${L(1450, 460, 'Duty roster')}`,
          act: () => { E.note('roster', 'Duty roster: “Night shift, Tue 18 May → Wed 19 May: Hale, Mortimer, Price, YOU. Day shift Mon 17: Hale, Lacey, Bell.”'); E.say('The duty roster: tonight’s night shift runs from Tuesday 18 May into Wednesday 19 May.'); } },
      ],
    },
    tele: {
      name: 'The teleprinter room',
      bg: () => hut('#403a32', '#352f28'),
      spots: [
        { id: 'back', x: 1300, y: 740, w: 290, h: 130, art: () => E.exit('Hut office →', 1320), act: () => E.go('hut') },
        { id: 'teleprinter', x: 300, y: 260, w: 640, h: 400, art: () => `<rect x="320" y="380" width="600" height="260" rx="10" fill="#4a4a40"/><rect x="380" y="320" width="480" height="70" fill="#e9dcb8"/>${L(620, 690, 'Teleprinter to the Admiralty')}`, act: () => openTele(),
          use: { teleKey: () => { F().teleUnlocked = 1; E.take('teleKey'); E.say('The teleprinter lock turns. The machine hums.'); return true; }, ribbon: () => { F().ribbon = 1; E.take('ribbon'); E.say('You thread the new ink ribbon. Somebody had pulled the old one out.'); return true; } } },
        { id: 'drawer', x: 1000, y: 420, w: 280, h: 240, art: () => `<rect x="1020" y="480" width="240" height="140" fill="#5b3c25"/>${L(1140, 690, 'Typist’s desk')}`,
          act: () => { if (F().ribbonFound) return E.say('Carbon paper and a hairpin.'); F().ribbonFound = 1; E.give('ribbon'); E.say('In the typist’s drawer: a fresh ink ribbon in a tin.'); } },
        { id: 'bin', x: 80, y: 480, w: 200, h: 180, art: () => `<rect x="110" y="520" width="140" height="130" fill="#555"/>${L(180, 690, 'Waste-paper bin')}`,
          act: () => { E.note('bin', 'In the bin: the old teleprinter ribbon, cut into pieces, and a scrap: “…make sure nothing goes out tonight. – M.”'); E.say('In the bin: the old ink ribbon, cut to pieces, and a scrap of paper: “…make sure nothing goes out tonight. – M.”'); } },
      ],
    },
    library: {
      name: 'The mansion library',
      bg: () => hut('#3a2a20', '#46342a'),
      spots: [
        { id: 'back', x: 20, y: 740, w: 300, h: 130, art: () => E.exit('↑ Back to the hut'), act: () => E.go('hut') },
        { id: 'fireplace', x: 400, y: 220, w: 480, h: 440, art: () => `<rect x="420" y="280" width="440" height="360" fill="#6a5a4a"/><rect x="520" y="420" width="240" height="220" fill="#140d08"/><text x="640" y="350" text-anchor="middle" font-size="30" fill="#e9dcb8">MDCCCLXXVII</text>${L(640, 690, 'Carved fireplace')}`,
          act: () => { E.note('fire', 'Carved over the fireplace: MDCCCLXXVII.'); E.say('Carved into the stone over the fireplace: MDCCCLXXVII – the year the house was built.'); } },
        { id: 'painting', x: 940, y: 120, w: 340, h: 380, art: () => `<rect x="960" y="140" width="300" height="300" fill="#5a3a20" stroke="#c9a24a" stroke-width="10"/>${L(1110, 480, F().safe ? 'Safe behind the painting (open)' : 'Portrait of the old Lord')}`, act: () => openSafe() },
        { id: 'chess', x: 1300, y: 420, w: 260, h: 240, art: () => `<rect x="1320" y="480" width="220" height="140" fill="#d8ccb0"/>${L(1430, 690, 'Chess board')}`,
          act: () => E.say('A game in progress between two codebreakers. Black is about to lose. Nothing to do with you – tonight.') },
        { id: 'note', x: 80, y: 120, w: 260, h: 260, art: () => `${E.paper(100, 140, 220, 200, 5)}${L(210, 380, 'Note on the desk')}`,
          act: () => { E.note('hale', 'Commander Hale’s note: “Safe code = the year this house was built. Codeword card and teleprinter key inside. If I’m not back, send the warning yourself. – H.”'); E.say('Commander Hale’s handwriting: “Safe code = the year this house was built. Codeword card and teleprinter key inside. If I’m not back, send the warning yourself. – H.”'); } },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['cabinet', () => F().cabinet, ['The filing cabinet wants a five-letter word. The crossword has five answers.', 'Solve the five clues and read their first letters.', 'Rook, Oboe, Tea, Owl, Rain: ROTOR.']],
    ['date', () => F().decoded, ['The machine needs today’s three wheel letters from the key sheet. Which day is today?', 'The calendar is crossed off each evening; the duty roster says when tonight’s shift began. Ignore the pencilled arrow.', 'Tonight began on Tuesday 18 May: wheels B L Q. Then read the intercept.']],
    ['mansion', () => F().mansion, ['The warning needs the codeword and key from the Commander’s safe in the mansion.', 'The sentry wants a pass. The Commander left his coat in the hut.', 'Take the pass from the greatcoat and use it on the path to the mansion.']],
    ['safe', () => F().safe, ['The safe is behind the portrait. Hale’s note gives the code.', 'The year the house was built is carved over the fireplace in Roman numerals.', 'MDCCCLXXVII = 1877.']],
    ['tele', () => F().teleUnlocked && F().ribbon, ['The teleprinter is locked and someone has sabotaged it.', 'The key came from the safe. Look in the typist’s desk for what is missing.', 'Use the teleprinter key and the new ink ribbon on the teleprinter.']],
    ['send', () => F().won, ['Send the warning: codeword, then the grid number.', 'The codeword card was in the safe. The grid square was in the decoded intercept.', 'Codeword LARK, then grid square AJ 37.']],
  ],
  intro: ['Hut 9 · a country house in Buckinghamshire · 19 May 1943 · 05:00', 'The Codebreakers’ Hut',
    `<p>You are the youngest codebreaker on the night shift. An hour ago Commander Hale ran out of the hut with an intercept in his hand – and has not come back. The others are asleep in the mansion, and someone has been tampering with the machines.</p><p>A convoy is crossing the Atlantic. If tonight’s German message is what Hale thought, the warning must reach the Admiralty before six o’clock.</p><p>Level 2: not every mark in this hut was made to help you.</p>`,
    'A single lamp, the hiss of a kettle and a desk covered in paper. Look around.'],
  timesUp: ['06:00.', 'The teleprinter stays silent. Far away in the Atlantic, the convoy sails on unwarned.'],
  win: ['ADMIRALTY ACKNOWLEDGES', '“Message received. Convoy SC 12 turning north.” At half past six Commander Hale bursts in, mud to the knees – he had been chasing Mortimer, the mole, across the park – and finds the warning already sent. The convoy reaches Liverpool without losing a ship.'],
};

function openCrossword() {
  E.note('crossword', 'Crossword on the desk – five clues: ' + CROSS.map((c, i) => `${i + 1}. ${c[0]} (${c[1]})`).join(' · ') + '. Scribbled beside it: “first letters – my cabinet”.');
  E.modal(`<h2>The Times crossword (half done)</h2><div class="paper">${CROSS.map((c, i) => `<p>${i + 1}. ${c[0]} (${c[1]})</p>`).join('')}</div><p class="small">Scribbled in the margin: “first letters – my cabinet”.</p>`);
}
function openCabinet() {
  if (F().cabinet) return E.say('The cabinet drawers stand open – the key sheet is in your pocket.');
  E.wordLock('Filing cabinet', 'A combination bar with five letter wheels.', 5, w => { if (w !== 'ROTOR') return false; F().cabinet = 1; E.give('keysheet'); E.say('The bar drops. In the top drawer: the machine key sheet for May 1943.'); return true; });
}
function openCalendar() {
  E.note('calendar', 'Wall calendar, May 1943: each day crossed off at the end of the shift, up to and including Tuesday 18. Someone has pencilled an arrow at Monday 17 – “TODAY”.');
  E.modal(`<h2>Wall calendar – May 1943</h2><p class="paper">Mon 17 ✗ · Tue 18 ✗ · Wed 19 · Thu 20 · Fri 21</p><p class="small">The days are crossed off at the end of each shift. Someone has pencilled an arrow at Monday 17 with the word “TODAY”.</p>`);
}
function openMachine() {
  const ks = E.has('keysheet') ? '<div class="paper"><table style="width:100%"><tr><td>Mon 17 May</td><td>K X F</td></tr><tr><td>Tue 18 May</td><td>B L Q</td></tr><tr><td>Wed 19 May</td><td>M Z T</td></tr></table><p class="small">Each night shift uses the key of the day it began.</p></div>' : '<p class="small">You need the key sheet to know how to set it.</p>';
  E.wordLock('Cipher machine', `Set the three wheels.${ks}`, 3, w => { F().rotors = w; if (w === KEY) { F().decoded = 1; E.say('Wheels set to B L Q. The machine is ready to read the intercepts.'); } else E.say(`Wheels set to ${w}.`); return true; });
}
function openTape() {
  const out = F().rotors ? crypt(TAPE, F().rotors, -1) : TAPE;
  if (F().rotors === KEY) E.note('decrypt', 'Decrypted intercept: “' + PLAIN + '”');
  E.modal(`<h2>Tonight’s intercept</h2><p class="small">Raw tape:</p><p class="paper" style="font-family:monospace">${TAPE}</p><p class="small">Through the machine (wheels ${F().rotors || 'not set'}):</p><p class="paper" style="font-family:monospace">${out}</p>`);
}
function openSafe() {
  if (F().safe) return E.say('The safe stands open behind the portrait.');
  E.numLock('Wall safe', 'Behind the portrait of the old Lord: a small safe with four number wheels.', 4, c => { if (c !== '1877') return false; F().safe = 1; E.give('teleKey'); E.note('codeword', 'Codeword card from the safe: “Admiralty codeword this week: LARK.”'); E.say('The safe opens: the teleprinter key and a card – “Admiralty codeword this week: LARK.”'); return true; });
}
function openTele() {
  if (!F().teleUnlocked) return E.say('The teleprinter is locked – a small keyhole in its side.');
  if (!F().ribbon) return E.say('The keys clatter but nothing prints. The ink ribbon has been pulled out.');
  if (!F().decoded) return E.say('The line to the Admiralty is open. But what will you tell them? You haven’t read tonight’s intercept yet.');
  E.wordLock('Teleprinter – codeword', 'The Admiralty asks for this week’s codeword.', 4, w => {
    if (w !== 'LARK') return false;
    setTimeout(() => E.numLock('Teleprinter – warning', 'Codeword accepted. Type the grid square of the attack: AJ and two figures.', 2, c => { if (c !== '37') return false; E.win(); return true; }, 'The Admiralty asks you to repeat.'), 50);
    return true;
  }, 'The Admiralty does not recognise that codeword.');
}
});
