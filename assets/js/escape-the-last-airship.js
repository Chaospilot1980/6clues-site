/* Six Clues escape room #8 – The Last Airship (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const SECRET = 'CLOSE NOTHING. VALVE SEVEN STAYS OPEN TILL DAWN. WRENCH IN THE PULLEY.';
const enc = (t, k) => t.replace(/[A-Z]/g, c => A[(A.indexOf(c) + k) % 26]);
const CIPHER = enc(SECRET, 13);
const cabin = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 8 }, (_, i) => `<rect x="${i * 200}" y="0" width="14" height="660" fill="${c2}"/>`).join('')}<rect y="660" width="1600" height="240" fill="#2a2016"/><ellipse cx="800" cy="0" rx="560" ry="360" fill="url(#lamp)"/>`;
// treble-clef staff: notes C (space 3), A (space 2), G (line 2), E (line 1)
const staff = () => { const y0 = 60; let s = Array.from({ length: 5 }, (_, i) => `<line x1="20" y1="${y0 + i * 20}" x2="380" y2="${y0 + i * 20}" stroke="#222" stroke-width="2"/>`).join('');
  s += `<text x="24" y="${y0 + 72}" font-size="92" font-family="serif">𝄞</text>`;
  const pos = { E: 80, G: 60, A: 50, C: 30 }; // offset from top line (y0) – E bottom line, G second line, A second space, C third space
  ['C', 'A', 'G', 'E'].forEach((n, i) => { const y = y0 + pos[n]; s += `<ellipse cx="${130 + i * 65}" cy="${y}" rx="11" ry="8" fill="#111" transform="rotate(-20 ${130 + i * 65} ${y})"/><line x1="${141 + i * 65}" y1="${y}" x2="${141 + i * 65}" y2="${y - 55}" stroke="#111" stroke-width="2"/>`; });
  return s; };

return {
  start: 'lounge', v: 1,
  items: {
    radioKey: ['🗝️', 'Radio-room key', 'A small brass key tagged “W/T”.'],
    notebook: ['📒', 'Navigator’s notebook', 'Navigator Brandt’s pocket notebook, full of bearings and sums.'],
    crank: ['🔩', 'Hatch crank', 'An iron crank handle for the cargo-hold hatch winch.'],
    wrench: ['🔧', 'Wrench', 'A big steel wrench, found jammed in the elevator cable pulley.'],
  },
  rooms: {
    lounge: {
      name: 'The passenger lounge',
      bg: () => cabin('#4a3424', '#5a4430'),
      spots: [
        { id: 'piano', photo: [170, 250, 430, 420], x: 60, y: 300, w: 380, h: 360, art: () => `<rect x="80" y="400" width="340" height="200" fill="#1a1410"/><rect x="100" y="340" width="300" height="70" fill="#e9dcb8"/>${L(250, 690, 'Aluminium piano')}`, act: () => openPiano() },
        { id: 'bench', photo: [390, 540, 270, 170], x: 460, y: 500, w: 260, h: 160, art: () => `<rect x="480" y="540" width="220" height="80" fill="#3a2a1a"/>${L(590, 690, F().bench ? 'Piano bench (open)' : 'Piano bench (letter lock)')}`, act: () => openBench() },
        { id: 'windows', photo: [480, 95, 850, 320], x: 760, y: 60, w: 520, h: 300, art: () => `<rect x="780" y="80" width="480" height="240" fill="#0b1424" stroke="#c9a24a" stroke-width="8"/>${L(1020, 360, 'Promenade windows')}`,
          act: () => E.say('Far below, the dark Atlantic. The stars wheel slowly – the ship is turning when it should fly straight.') },
        { id: 'list', photo: [1405, 110, 175, 300], x: 1300, y: 140, w: 240, h: 280, art: () => `${E.paper(1320, 160, 200, 220, 6)}${L(1420, 420, 'Passenger list')}`, act: () => openList() },
        { id: 'toRadio', photo: [0, 145, 145, 550], x: 20, y: 740, w: 300, h: 130, art: () => E.exit(F().radioOpen ? '← Radio room' : '← Radio room (locked)'),
          act: () => F().radioOpen ? E.go('radio') : E.say('A door marked W/T – crew only. Locked.'),
          use: { radioKey: () => { F().radioOpen = 1; E.take('radioKey'); E.say('The brass key turns. The radio room is empty, the set still warm.'); return true; } } },
        { id: 'toGondola', photo: [1300, 465, 300, 300], x: 1260, y: 740, w: 330, h: 130, art: () => E.exit('Control car ↓', 1300), act: () => E.go('gondola') },
      ],
    },
    radio: {
      name: 'The radio room',
      bg: () => cabin('#3a2c22', '#463426'),
      spots: [
        { id: 'back', photo: [1465, 480, 135, 420], x: 1340, y: 740, w: 250, h: 130, art: () => E.exit('Lounge →', 1360), act: () => E.go('lounge') },
        { id: 'telegram', photo: [60, 190, 170, 185], x: 100, y: 160, w: 300, h: 260, art: () => `${E.paper(120, 180, 260, 200, 5)}${L(250, 420, 'Telegram on the spike')}`, act: () => openTelegram() },
        { id: 'wheel', photo: [265, 515, 200, 115], x: 460, y: 380, w: 360, h: 280, art: () => `<circle cx="640" cy="520" r="110" fill="#c9a24a"/><circle cx="640" cy="520" r="70" fill="#e9dcb8"/>${L(640, 690, 'Cipher wheel')}`, act: () => openWheel() },
        { id: 'cupboard', photo: [810, 70, 255, 625], x: 900, y: 200, w: 300, h: 460, art: () => `<rect x="920" y="220" width="260" height="420" fill="#5b3c25"/>${L(1050, 690, 'Tool cupboard')}`,
          act: () => { if (F().crank) return E.say('Spare valves and a roll of tape.'); F().crank = 1; E.give('crank'); E.say('In the tool cupboard: an iron crank handle, labelled “cargo hatch”.'); } },
        { id: 'set', photo: [1095, 120, 370, 330], x: 1220, y: 300, w: 340, h: 360, art: () => `<rect x="1240" y="360" width="300" height="200" fill="#2a2e2a"/>${L(1390, 690, 'Wireless set')}`,
          act: () => E.say('The wireless is tuned to nothing. The operator’s chair is cold – he went off watch at midnight and someone used his set after that.') },
      ],
    },
    gondola: {
      name: 'The control car',
      bg: () => cabin('#2e3036', '#3a3c42'),
      spots: [
        { id: 'up', photo: [0, 465, 185, 365], x: 20, y: 740, w: 280, h: 130, art: () => E.exit('↑ Lounge'), act: () => E.go('lounge') },
        { id: 'altimeter', photo: [75, 115, 165, 185], x: 80, y: 120, w: 240, h: 240, art: () => `<circle cx="200" cy="240" r="100" fill="#e9dcb8" stroke="#c9a24a" stroke-width="10"/>${L(200, 380, 'Altimeter')}`,
          act: () => { E.note('alt', 'Altimeter in the control car: 1,300 feet.'); E.say('The altimeter needle stands at 1,300 feet.'); } },
        { id: 'compass', photo: [320, 345, 260, 135], x: 360, y: 120, w: 300, h: 260, art: () => `<circle cx="510" cy="240" r="100" fill="#111" stroke="#c9a24a" stroke-width="10"/>${L(510, 380, 'Compass & deviation card')}`, act: () => openCompass() },
        { id: 'helm', photo: [695, 255, 280, 450], x: 700, y: 300, w: 440, h: 360, art: () => `<circle cx="920" cy="470" r="150" fill="none" stroke="#6b4a2a" stroke-width="22"/>${L(920, 690, F().freed ? 'Helm' : 'Helm (stiff – something is jamming it)')}`, act: () => openHelm() },
        { id: 'toHold', photo: [990, 320, 580, 530], x: 1200, y: 300, w: 380, h: 380, art: () => `<rect x="1220" y="420" width="340" height="220" fill="${F().hatch ? '#140d08' : '#4a4a48'}"/>${L(1390, 690, F().hatch ? 'Cargo hold →' : 'Hatch to the cargo hold (winch)')}`,
          act: () => F().hatch ? E.go('hold') : E.say('A heavy hatch on a winch. The crank handle has been taken off.'),
          use: { crank: () => { F().hatch = 1; E.take('crank'); E.say('You fit the crank and wind the hatch open. A ladder leads up into the dark hull.'); return true; } } },
      ],
    },
    hold: {
      name: 'The cargo hold',
      bg: () => `<rect width="1600" height="900" fill="#1e1c1a"/>${Array.from({ length: 9 }, (_, i) => `<path d="M${i * 200} 0 Q${i * 200 + 100} 300 ${i * 200} 660" stroke="#4a4440" stroke-width="10" fill="none"/>`).join('')}<rect y="660" width="1600" height="240" fill="#141210"/>`,
      spots: [
        { id: 'back', photo: [0, 595, 425, 305], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('↓ Control car'), act: () => E.go('gondola') },
        { id: 'valves', photo: [65, 190, 370, 325], x: 100, y: 200, w: 520, h: 300, art: () => `<rect x="120" y="220" width="480" height="240" fill="#3a3c40"/>${[1, 2, 3, 4, 5, 6, 7, 8].map(i => `<circle cx="${150 + (i - 1) * 62}" cy="340" r="22" fill="${i === 7 && !F().valve ? '#c4232b' : '#2a6a3a'}"/>`).join('')}${L(360, 500, 'Ballast valve panel')}`, act: () => openValves() },
        { id: 'pulley', photo: [775, 105, 210, 225], x: 700, y: 120, w: 300, h: 360, art: () => `<circle cx="850" cy="260" r="80" fill="#555"/>${F().freed ? '' : '<rect x="800" y="250" width="110" height="20" fill="#999"/>'}${L(850, 500, 'Elevator cable pulley')}`,
          act: () => { if (F().freed) return E.say('The cables run freely over the pulley.'); F().freed = 1; E.give('wrench'); E.note('pulley', 'A wrench had been jammed into the elevator cable pulley – the helm could not move the elevators.'); E.say('A steel wrench is jammed into the pulley! You work it loose – the cables twang free.'); } },
        { id: 'crates', photo: [1035, 315, 565, 530], x: 1060, y: 380, w: 480, h: 280, art: () => `<rect x="1080" y="440" width="200" height="200" fill="#8a6a3a"/><rect x="1300" y="480" width="200" height="160" fill="#7a5a2a"/>${L(1290, 690, 'Mail crates')}`,
          act: () => { E.note('crates', 'Mail crates: one is stencilled “H. GRAY – CABIN 7 – NOT TO BE OPENED”. Inside: a parachute.'); E.say('One crate is stencilled “H. GRAY – CABIN 7”. Inside, packed in straw: a parachute. Someone was planning to leave early.'); } },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['bench', () => F().bench, ['The bench has a four-letter lock. The music on the piano has four notes.', 'Treble clef: the lines from the bottom are E G B D F, the spaces F A C E.', 'The notes are C, A, G, E: CAGE.']],
    ['radio', () => F().radioOpen, ['The bench held a key tagged W/T.', 'W/T means wireless telegraphy – the radio room.', 'Use the radio-room key on the door in the lounge.']],
    ['decode', () => F().decoded, ['The telegram is in cipher. The cipher wheel needs a number.', 'The telegram says: “Set the wheel to our height in hundreds of feet.” Check the control car.', 'The altimeter reads 1,300 feet: set the wheel to 13.']],
    ['hatch', () => F().hatch, ['The cargo hold hatch needs its crank.', 'The radio room has a tool cupboard.', 'Take the crank and use it on the hatch in the control car.']],
    ['valve', () => F().valve, ['The message mentions a valve that must stay open.', 'Close it on the ballast panel in the cargo hold.', 'Close valve 7.']],
    ['pulley', () => F().freed, ['The message mentions a wrench in the pulley.', 'Look at the elevator cable pulley in the cargo hold.', 'Pull the wrench out of the pulley.']],
    ['helm', () => F().won, ['Steer for Lakehurst. The navigator wrote down the true course.', 'A compass needs correcting: the deviation card tells you how.', 'True course 247°, deviation card says add 4° on that heading: steer 251.']],
  ],
  intro: ['Airship Valkyrie · over the North Atlantic · 6 May 1936 · 04:00', 'The Last Airship',
    `<p>You are a passenger on the giant airship Valkyrie, bound for Lakehurst, New Jersey. You woke to find the ship turning slowly in the dark, the navigator gone from his post and the crew asleep in their bunks behind a jammed door.</p><p>At dawn the Valkyrie will be over open sea with half her ballast gone and no way to steer. You have one hour to put her back on course.</p><p>Level 2: one passenger aboard is not who he says.</p>`,
    'The lounge lamps flicker. The floor tilts gently under your feet. Look around.'],
  timesUp: ['Dawn.', 'The Valkyrie drifts on over an empty grey sea. Rescue ships will find her – eventually.'],
  win: ['The bow swings west', 'The Valkyrie steadies on 251 by her compass – 247° true – and the engines settle into their drone. At sunrise the crew breaks out of their quarters and finds “Mr H. Gray” of cabin 7 strapping on a parachute in the cargo hold. Lakehurst comes up out of the mist at noon, right on time.'],
};

function openPiano() {
  E.note('piano', 'Sheet music on the piano: four notes in the treble clef – third space, second space, second line, bottom line. A card tucked in the music: “Lines: E G B D F. Spaces: F A C E.”');
  E.modal(`<h2>Sheet music on the piano</h2><svg viewBox="0 0 400 180" class="close" style="background:#efe3c4;max-width:420px">${staff()}</svg><p class="small">Pencilled on a card in the music: “Lines from the bottom: E G B D F. Spaces: F A C E.”</p>`);
}
function openBench() {
  if (F().bench) return E.say('The piano bench is empty now apart from old sheet music.');
  E.wordLock('Piano bench', 'A brass letter lock with four wheels, set into the lid.', 4, w => { if (w !== 'CAGE') return false; F().bench = 1; E.give('radioKey'); E.give('notebook'); E.say('The lid opens: a brass key tagged “W/T” and the navigator’s pocket notebook.'); return true; });
}
function openList() {
  E.note('list', 'Passenger list: 1 Mrs E. Vance · 2 Dr & Mrs Okafor · 4 Mr L. Brandt (navigator’s brother) · 5 Miss I. Petrov · 7 Mr H. Gray (no luggage declared) · 9 You.');
  E.modal(`<h2>Passenger list</h2><div class="paper"><table style="width:100%">${[['1', 'Mrs E. Vance'], ['2', 'Dr and Mrs Okafor'], ['4', 'Mr L. Brandt'], ['5', 'Miss I. Petrov'], ['7', 'Mr H. Gray – no luggage declared'], ['9', 'You']].map(r => `<tr><td>Cabin ${r[0]}</td><td>${r[1]}</td></tr>`).join('')}</table></div>`);
}
function openTelegram() {
  E.note('telegram', 'Telegram on the spike (in cipher): ' + CIPHER + ' – pencilled underneath: “Set the wheel to our height in hundreds of feet.”');
  E.modal(`<h2>Telegram on the spike</h2><p class="paper" style="font-family:monospace;letter-spacing:.1em">${CIPHER}</p><p class="small">Pencilled underneath: “Set the wheel to our height in hundreds of feet.”</p>`);
}
function openWheel() {
  let k = 0;
  E.modal(`<h2>Cipher wheel</h2><p>Turn the inner wheel back by a number of letters, and read the telegram through it.</p><div class="dial"><span>Shift</span><button id="km">◀</button><b id="kv">0</b><button id="kp">▶</button></div><p class="paper" id="out" style="font-family:monospace;letter-spacing:.1em"></p>`, m => {
    const draw = () => { m.querySelector('#kv').textContent = k; const t = enc(CIPHER, (26 - k) % 26); m.querySelector('#out').textContent = t; if (k === 13) { F().decoded = 1; E.note('decoded', 'Decoded telegram: “' + SECRET + '”'); E.save(); } };
    m.querySelector('#km').addEventListener('click', () => { k = (k + 25) % 26; draw(); }); m.querySelector('#kp').addEventListener('click', () => { k = (k + 1) % 26; draw(); }); draw();
  });
}
function openCompass() {
  E.note('compass', 'Compass deviation card: heading 220–239° add 2°; 240–259° add 4°; 260–279° add 3°. (Compass course = true course + deviation.)');
  E.modal(`<h2>Compass deviation card</h2><p>The ship’s steel girders pull the compass needle a little. The card says how much to add to a true course to get the course to steer by compass.</p><div class="paper"><table style="width:100%"><tr><td>True 220–239°</td><td>add 2°</td></tr><tr><td>True 240–259°</td><td>add 4°</td></tr><tr><td>True 260–279°</td><td>add 3°</td></tr></table></div>`);
}
function openValves() {
  if (F().valve) return E.say('All eight ballast valves show green. The water stays aboard.');
  E.numLock('Ballast valve panel', 'Eight valves; one light is red – water is draining out somewhere. Which valve do you close?', 1, c => {
    if (c !== '7') return false; F().valve = 1; E.say('You spin valve 7 shut. The gurgle of draining water stops.'); return true;
  }, 'That valve was already closed.');
}
function openHelm() {
  if (!F().freed) return E.say('The elevator wheel won’t turn more than an inch. Something is jamming the cables.');
  if (!F().valve) return E.say('The helm moves now – but the ship is getting lighter by the minute. Stop the ballast draining first.');
  const nb = E.has('notebook') ? '<p class="paper">Navigator’s notebook, last page: “04:00 – Lakehurst bears 247° TRUE from here.”</p>' : '';
  E.numLock('The helm', `Set the compass course to steer – three figures.${nb}`, 3, c => { if (c !== '251') return false; E.win(); return true; }, 'The ship swings – and the stars say that is the wrong way.');
}
});
