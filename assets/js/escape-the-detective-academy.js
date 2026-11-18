/* Six Clues escape room #24 – The Detective Academy (level 1, family). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const school = c => `<rect width="1600" height="900" fill="${c}"/><rect y="0" width="1600" height="40" fill="#3a2a1a"/><rect y="640" width="1600" height="260" fill="#6a4a2a"/><ellipse cx="800" cy="0" rx="520" ry="300" fill="url(#lamp)"/>`;

return {
  start: 'classroom', v: 1,
  items: {
    glass: ['🔍', 'Magnifying glass', 'A real detective’s magnifying glass.'],
    officeKey: ['🗝️', 'Office key', 'The headmaster’s brass key.'],
  },
  rooms: {
    classroom: {
      name: 'Classroom 6',
      bg: () => school('#3a5a4a'),
      spots: [
        { id: 'board', x: 300, y: 80, w: 800, h: 320, art: () => `<rect x="320" y="100" width="760" height="260" fill="#1e3a2a" stroke="#6a4a2a" stroke-width="12"/>${L(700, 390, 'Blackboard')}`,
          act: () => { E.note('board', 'Blackboard: “FINAL EXAM! Someone has stolen the Golden Badge. Search the evidence room, then write the thief’s name on the answer machine in the headmaster’s office. Our motto: every detective needs a C _ _ E.”'); E.say('“FINAL EXAM! Someone stole the Golden Badge. Search the evidence room, then name the thief in the headmaster’s office. Our motto: every detective needs a C _ _ E.”'); } },
        { id: 'desks', x: 200, y: 440, w: 800, h: 200, art: () => `${[0, 1, 2, 3].map(i => `<rect x="${230 + i * 190}" y="500" width="150" height="80" fill="#8a6a3a"/>`).join('')}${L(600, 620, 'Pupils’ desks')}`,
          act: () => { if (F().glass) return E.say('Pencils, rubbers and a half-eaten apple.'); F().glass = 1; E.give('glass'); E.say('Your desk has your name on it – and inside, a real magnifying glass!'); } },
        { id: 'door', x: 1180, y: 200, w: 340, h: 440, art: () => `<rect x="1200" y="220" width="300" height="400" fill="#5a3a20"/>${L(1350, 660, F().evidence ? 'Evidence room (open)' : 'Evidence room (2 numbers)')}`, act: () => F().evidence ? E.go('evidence') : openDoor() },
        { id: 'poster', x: 40, y: 120, w: 220, h: 300, art: () => `<rect x="60" y="140" width="180" height="240" fill="#e8d8a0"/>${L(150, 420, 'Poster')}`,
          act: () => E.say('A poster: “The evidence room code is the number of pupils in this class.” Underneath, a class list with 12 names.') },
        { id: 'toOffice', x: 20, y: 740, w: 360, h: 130, art: () => E.exit(F().office ? '← Headmaster’s office' : '← Headmaster’s office (locked)'), act: () => F().office ? E.go('office') : E.say('The headmaster’s door is locked.'),
          use: { officeKey: () => { F().office = 1; E.take('officeKey'); E.say('The headmaster’s door clicks open.'); return true; } } },
      ],
    },
    evidence: {
      name: 'The evidence room',
      bg: () => school('#4a4a5a'),
      spots: [
        { id: 'back', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Classroom →', 1240), act: () => E.go('classroom') },
        { id: 'suspects', x: 80, y: 100, w: 560, h: 300, art: () => `${[0, 1, 2].map(i => `<rect x="${100 + i * 180}" y="120" width="160" height="220" fill="#e8e0d0"/>`).join('')}${L(360, 380, 'Three suspect cards')}`,
          act: () => { E.note('suspects', 'Suspect cards: MR PLUM, the gardener – shoe size 10, wears wellies, grey hair. MISS LARK, the cook – shoe size 5, always floury, red hair. COACH BURKE – shoe size 8, trainers, black hair.'); E.say('Three suspects: Mr Plum the gardener, Miss Lark the cook, Coach Burke. You copy their details.'); } },
        { id: 'footprint', x: 700, y: 480, w: 320, h: 160, art: () => `<ellipse cx="860" cy="560" rx="60" ry="30" fill="#5a3a20"/>${L(860, 640, 'Muddy footprint')}`,
          act: () => F().foot ? E.say('Size 10 welly print, with grass in the mud.') : E.say('A muddy footprint on the floor. Too small to see the details.'),
          use: { glass: () => { F().foot = 1; E.note('foot', 'Footprint (magnified): a welly boot, size 10, with grass in the mud.'); E.say('Through the glass: a welly print, size 10, with grass in the mud!'); return true; } } },
        { id: 'case', x: 1080, y: 200, w: 400, h: 300, art: () => `<rect x="1100" y="220" width="360" height="240" fill="#c8d8e8" opacity=".6" stroke="#888" stroke-width="6"/>${L(1280, 500, 'Empty badge case')}`,
          act: () => F().hair ? E.say('A grey hair from the empty case.') : E.say('The empty glass case where the Golden Badge was. Something tiny is caught on the edge.'),
          use: { glass: () => { F().hair = 1; E.note('hair', 'Caught on the badge case (magnified): a single GREY hair.'); E.say('Through the glass: a single grey hair, caught on the case!'); return true; } } },
        { id: 'cabinet', x: 120, y: 440, w: 380, h: 200, art: () => `<rect x="140" y="460" width="340" height="160" fill="#5a5a6a"/>${L(310, 650, F().cab ? 'Cabinet (open)' : 'Cabinet (letter lock)')}`, act: () => openCabinet() },
      ],
    },
    office: {
      name: 'The headmaster’s office',
      bg: () => school('#5a3a3a'),
      spots: [
        { id: 'back', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Classroom →', 1240), act: () => E.go('classroom') },
        { id: 'machine', x: 500, y: 300, w: 600, h: 340, art: () => `<rect x="520" y="320" width="560" height="280" fill="#3a3a3a"/><rect x="560" y="360" width="480" height="120" fill="#7ac0a0"/>${L(800, 640, 'Answer machine')}`, act: () => openMachine() },
        { id: 'photo', x: 80, y: 120, w: 340, h: 300, art: () => `<rect x="100" y="140" width="300" height="220" fill="#c8b890" stroke="#c9a24a" stroke-width="10"/>${L(250, 400, 'Class photo')}`,
          act: () => E.say('Last year’s graduates, all holding their Golden Badges and grinning.') },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['glass', () => F().glass, ['Every detective needs a tool.', 'Look in the pupils’ desks.', 'Take the magnifying glass from your desk.']],
    ['evidence', () => F().evidence, ['The evidence room has a two-number lock.', 'The poster says what the code is.', '12 pupils: 12.']],
    ['clues', () => F().foot && F().hair, ['Look at the evidence closely.', 'Use the magnifying glass on things in the evidence room.', 'The muddy footprint and the empty badge case.']],
    ['cab', () => F().cab, ['The cabinet has a letter lock.', 'The motto on the blackboard.', 'CLUE.']],
    ['office', () => F().office, ['The cabinet gave you a key.', 'The headmaster’s office.', 'Use the office key on the headmaster’s door.']],
    ['answer', () => F().won, ['Who left a size-10 welly print and a grey hair?', 'Check the suspect cards.', 'PLUM.']],
  ],
  intro: ['The Six Clues Detective Academy · exam day · 14:00', 'The Detective Academy',
    `<p>Today is your final exam at the Detective Academy. The Golden Badge – the prize for the best young detective – has been stolen from its case!</p><p>You have one hour to find the clues, work out who did it and type the answer into the headmaster’s answer machine. Pass, and the badge is yours.</p><p>Level 1: perfect for families and first-time players.</p>`,
    'Chalk dust, wooden desks and a ticking clock. Look around.'],
  timesUp: ['The bell rings!', 'Time’s up – but a real detective never gives up. Finish the case!'],
  win: ['Case closed!', '“PLUM – CORRECT!” the machine dings. Mr Plum the gardener confesses at once: he only borrowed the badge to polish it for you. The headmaster pins the Golden Badge on your jumper. Congratulations, Detective!'],
};

function openDoor() {
  E.numLock('Evidence room', 'The door has two number wheels.', 2, c => { if (c !== '12') return false; F().evidence = 1; E.say('Click – the evidence room is open.'); return true; });
}
function openCabinet() {
  if (F().cab) return E.say('The cabinet is open and empty.');
  E.wordLock('Evidence cabinet', 'A cabinet with four letter wheels. On it: “What every detective needs.”', 4, w => { if (w !== 'CLUE') return false; F().cab = 1; E.give('officeKey'); E.say('The cabinet opens: inside, the headmaster’s brass office key.'); return true; });
}
function openMachine() {
  if (!(F().foot && F().hair)) return E.say('The answer machine: “ENTER THE THIEF’S NAME.” Better examine the evidence closely first.');
  E.wordLock('Answer machine', '“ENTER THE THIEF’S SURNAME.”', 4, w => { if (w !== 'PLUM') return false; E.win(); return true; }, '“WRONG – CHECK THE EVIDENCE AGAIN.”');
}
});
