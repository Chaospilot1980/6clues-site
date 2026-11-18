/* Six Clues escape room #10 – The Séance (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const RAPS = [12, 9, 5, 19];
const TAROT = ['The Sun', 'The Moon', 'The Star', 'The Tower', 'The Fool'];
const parlour = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 16 }, (_, i) => `<rect x="${i * 100}" y="0" width="50" height="660" fill="${c2}"/>`).join('')}<rect y="660" width="1600" height="240" fill="#1e140e"/><ellipse cx="800" cy="0" rx="500" ry="320" fill="url(#lamp)"/>`;
const EVIDENCE = ['photo', 'cylinder', 'slide'];

return {
  start: 'parlour', v: 1,
  items: {
    studyKey: ['🗝️', 'Study key', 'A brass key wrapped in black muslin – from inside the spirit cabinet.'],
    notebook: ['📓', 'Accomplice’s notebook', 'A cheap notebook in a woman’s hand: rehearsal notes for the séance.'],
    lens: ['🔍', 'Magnifying glass', 'Lord Ashworth’s reading glass with an ivory handle.'],
    atticKey: ['🗝️', 'Attic key', 'A small iron key on a ribbon.'],
    photo: ['🖼️', 'Spirit photograph', 'The “spirit photograph” of the late Lord – proof that it is a fake.'],
    cylinder: ['🎵', 'Phonograph cylinder 7', 'A wax cylinder with the “spirit voice” on it.'],
    slide: ['🎞️', 'Lantern slide', 'A glass magic-lantern slide of a ghostly lady.'],
  },
  rooms: {
    parlour: {
      name: 'The séance parlour',
      bg: () => parlour('#3a1e24', '#43242a'),
      spots: [
        { id: 'table', photo: [460, 545, 625, 350], x: 420, y: 380, w: 620, h: 280, art: () => `<ellipse cx="730" cy="520" rx="290" ry="90" fill="#2a1a12"/>${L(730, 690, 'Séance table')}`, act: () => openTable() },
        { id: 'ball', photo: [775, 465, 120, 115], x: 640, y: 300, w: 180, h: 120, art: () => `<circle cx="730" cy="350" r="50" fill="#9fc3d8" opacity=".7"/>${L(730, 290, 'Crystal ball')}`,
          act: () => E.say('A glass ball on a velvet cushion. Look closely and you see – your own nose, upside down.') },
        { id: 'cabinet', photo: [1095, 20, 360, 700], x: 1120, y: 100, w: 400, h: 560, art: () => `<rect x="1140" y="120" width="360" height="520" fill="#140a0a" stroke="#6b4a2a" stroke-width="10"/>${L(1320, 690, F().cabinet ? 'Spirit cabinet (open)' : 'Spirit cabinet (padlocked)')}`, act: () => openCabinet() },
        { id: 'portrait', photo: [170, 5, 270, 385], x: 80, y: 80, w: 300, h: 360, art: () => `<rect x="100" y="100" width="260" height="320" fill="#5a3a20" stroke="#c9a24a" stroke-width="10"/>${L(230, 460, 'Portrait of the late Lord')}`,
          act: () => { E.note('brooch', 'Portrait of the late Lord Ashworth, wearing a mourning ribbon in the frame: “Edmund, Lord Ashworth, 1820–1883. Ever beloved.”'); E.say('The late Lord Ashworth glowers down. On the frame: “Edmund, Lord Ashworth, 1820–1883. Ever beloved.”'); } },
        { id: 'toStudy', photo: [0, 80, 130, 640], x: 20, y: 740, w: 300, h: 130, art: () => E.exit(F().study ? '← Study' : '← Study door (locked)'), act: () => F().study ? E.go('study') : E.say('The study door is locked.'),
          use: { studyKey: () => { F().study = 1; E.take('studyKey'); E.say('The study door opens.'); return true; } } },
        { id: 'front', photo: [1475, 10, 125, 720], x: 1260, y: 740, w: 330, h: 130, art: () => E.exit('Front door →', 1290),
          act: () => E.say('Locked and bolted from outside. Madame Zara’s accomplice locked you in “for the spirits’ sake” – the servants’ stair in the attic is the only other way out.') },
      ],
    },
    study: {
      name: 'Lord Ashworth’s study',
      bg: () => parlour('#2a2a24', '#33332c'),
      spots: [
        { id: 'back', photo: [1515, 100, 85, 680], x: 1300, y: 740, w: 290, h: 130, art: () => E.exit('Parlour →', 1320), act: () => E.go('parlour') },
        { id: 'desk', photo: [0, 500, 820, 400], x: 300, y: 400, w: 520, h: 260, art: () => `<rect x="320" y="460" width="480" height="40" fill="#5b3c25"/><rect x="340" y="500" width="440" height="140" fill="#4a3020"/>${L(560, 690, 'Writing desk')}`, act: () => openDesk() },
        { id: 'will', photo: [1035, 460, 250, 90], x: 860, y: 420, w: 260, h: 200, art: () => `${E.paper(880, 440, 220, 150, 5)}${L(990, 640, 'Papers on the side table')}`,
          act: () => { E.note('will', 'A new will, unsigned: Lady Ashworth leaves her whole fortune “to Madame Zara, for her guidance from the other side”. To be signed at midnight “when Edmund speaks”.'); E.say('A new will, waiting for Lady Ashworth’s signature at midnight: everything to Madame Zara.'); } },
        { id: 'spiritphoto', photo: [85, 5, 305, 365], x: 100, y: 100, w: 300, h: 300, art: () => `<rect x="120" y="120" width="260" height="240" fill="#d8ccb0" stroke="#3a2a1a" stroke-width="8"/>${L(250, 400, 'Framed spirit photograph')}`,
          act: () => F().photo ? E.say('You have the photograph.') : E.say('A photograph of Lady Ashworth at the séance table, a pale ghost of her husband floating behind her. Something tiny is printed in the corner – too small to read.'),
          use: { lens: () => { F().photo = 1; E.give('photo'); E.note('photo', 'Under the magnifying glass, the spirit photograph’s corner reads: “Zara &amp; Co. – double exposure – plate 7”. You take it as proof.'); E.say('Under the glass, tiny print in the corner: “Zara & Co. – double exposure – plate 7”. A trick photograph! You take it.'); return true; } } },
        { id: 'toAttic', photo: [1320, 110, 190, 640], x: 1200, y: 100, w: 260, h: 480, art: () => E.door(1220, 140, 220, 420, F().attic, F().attic ? 'Attic stair ↑' : 'Narrow attic door'), act: () => F().attic ? E.go('attic') : E.say('A narrow locked door. Stairs go up behind it.'),
          use: { atticKey: () => { F().attic = 1; E.take('atticKey'); E.say('The little iron key turns. A cold draught comes down the attic stair.'); return true; } } },
      ],
    },
    attic: {
      name: 'The attic',
      bg: () => `<rect width="1600" height="900" fill="#1e1a16"/><path d="M0 0 L800 -100 L1600 0 V660 H0z" fill="#2a241e"/><rect y="660" width="1600" height="240" fill="#14100c"/>`,
      spots: [
        { id: 'down', photo: [0, 570, 370, 330], x: 20, y: 740, w: 280, h: 130, art: () => E.exit('↓ Study'), act: () => E.go('study') },
        { id: 'phonograph', photo: [85, 115, 405, 365], x: 160, y: 300, w: 380, h: 360, art: () => `<rect x="200" y="500" width="300" height="140" fill="#5b3c25"/><path d="M350 500 L300 340 Q350 300 440 330z" fill="#c9a24a"/>${L(350, 690, 'Phonograph & wax cylinders')}`, act: () => openPhono() },
        { id: 'lantern', photo: [665, 225, 485, 305], x: 600, y: 300, w: 380, h: 360, art: () => `<rect x="680" y="440" width="220" height="200" fill="#3a3a38"/><circle cx="790" cy="420" r="40" fill="#c9a24a"/>${L(790, 690, 'Magic lantern & slide box')}`, act: () => openLantern() },
        { id: 'stair', photo: [1255, 80, 320, 600], x: 1100, y: 120, w: 420, h: 540, art: () => `<rect x="1140" y="160" width="340" height="480" fill="#2a1a12"/>${[0, 1, 2].map(i => `<rect x="${1180 + i * 100}" y="300" width="70" height="110" rx="6" fill="#d8ccb0"/>`).join('')}${L(1310, 690, 'Servants’ stair door – three cards')}`, act: () => openStair() },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['raps', () => F().cabinet, ['The spirit cabinet’s padlock has four letter wheels. The table raps when you touch it.', 'The card on the table: one rap for A, two for B, and so on.', '12, 9, 5, 19 = L, I, E, S: LIES.']],
    ['study', () => F().study, ['The cabinet held a key wrapped in muslin.', 'There is a locked door in the parlour.', 'Use the study key on the study door.']],
    ['desk', () => F().drawer, ['The desk drawer wants four figures. The late Lord is watching.', 'His portrait in the parlour gives two years.', 'The year he died: 1883.']],
    ['photo', () => F().photo, ['The spirit photograph has tiny print in its corner.', 'You found a magnifying glass in the desk.', 'Use the magnifying glass on the spirit photograph.']],
    ['attic', () => F().attic, ['The attic door is locked.', 'The desk drawer held a small iron key.', 'Use the attic key on the narrow door in the study.']],
    ['voice', () => F().cylinder, ['The “voice of Lord Ashworth” was a recording.', 'Which cylinder? The photograph’s plate number is a clue – the trickster numbers everything the same.', 'Play cylinder 7 and keep it.']],
    ['slide', () => F().slide, ['The ghostly lady was projected.', 'Look in the slide box of the magic lantern.', 'Take the slide of the ghost.']],
    ['stair', () => F().won, ['The servants’ stair door has three cards.', 'The accomplice’s notebook says how the cards go: as the night goes.', 'Moon, Star, Sun.']],
  ],
  intro: ['Ashworth House, Belgravia · 31 October 1888 · 23:00', 'The Séance',
    `<p>You are Lady Ashworth’s young nephew. Tonight the famous medium Madame Zara will let the old lady “speak” to her dead husband – and at midnight, at the spirit’s request, Lady Ashworth will sign away her whole fortune.</p><p>You have said out loud that it is all a trick. So Zara’s assistant has locked you in the parlour “so as not to disturb the spirits”. Find the proof, and get out before the clock strikes twelve.</p><p>Level 2: not everything that knocks here is a ghost.</p>`,
    'Heavy curtains, one oil lamp and a smell of incense. Look around.'],
  timesUp: ['Midnight.', 'From downstairs comes the scratch of a pen. Lady Ashworth has signed.'],
  win: ['Down the servants’ stair', 'You burst into the drawing room at five to twelve with a trick photograph, a wax cylinder and a lantern slide. Lady Ashworth listens to her “husband” say the same words twice from the phonograph – and tears up the will. Madame Zara is gone through the kitchen door before the constable arrives.'],
};

function openTable() {
  E.note('raps', 'The séance table raps when touched: 12 raps … 9 raps … 5 raps … 19 raps. A card under the table edge: “One rap for A, two for B – the spirits spell slowly.”');
  E.modal(`<h2>The séance table</h2><p>You lay your hands on the table. It rocks, and a sharp knocking comes from underneath:</p><p class="paper" style="font-size:1.3rem">${RAPS.map(n => `${n} raps`).join(' · ')}</p><p class="small">Tucked under the table edge: a card in Zara’s hand – “One rap for A, two for B – the spirits spell slowly.” Under the table: a hidden pedal.</p>`);
}
function openCabinet() {
  if (F().cabinet) return E.say('The spirit cabinet stands open: a tin trumpet, yards of muslin and a hidden pedal wire.');
  E.wordLock('Spirit cabinet', 'A padlock with four letter wheels on the black curtained cabinet.', 4, w => { if (w !== 'LIES') return false; F().cabinet = 1; E.give('studyKey'); E.give('notebook'); E.note('nb', 'Accomplice’s notebook: “Lamp low at 11. Raps by pedal. Voice: cylinder from the attic. Ghost: lantern slide. If anyone gets curious, use the back stair – the cards go as the night goes: first the Moon, then the Star, last the Sun.”'); E.say('The padlock opens: a muslin “ghost”, a tin trumpet – and a notebook and a brass key.'); return true; });
}
function openDesk() {
  if (F().drawer) return E.say('The drawer is empty now.');
  E.numLock('Desk drawer', 'A drawer with four number wheels. A black mourning ribbon is tied round the handle.', 4, c => { if (c !== '1883') return false; F().drawer = 1; E.give('lens'); E.give('atticKey'); E.say('The drawer slides open: Lord Ashworth’s magnifying glass and a small iron key on a ribbon.'); return true; });
}
function openPhono() {
  if (F().cylinder) return E.say('The phonograph sits silent. Cylinder 7 is in your pocket.');
  let n = 1;
  E.modal(`<h2>Phonograph</h2><p>A rack of numbered wax cylinders, 1 to 9.</p><div class="dial"><span>Cylinder</span><button id="cm">◀</button><b id="cv">1</b><button id="cp">▶</button></div><button class="btn" id="play">Play</button><p id="cres" class="res"></p>`, m => {
    const draw = () => { m.querySelector('#cv').textContent = n; };
    m.querySelector('#cm').addEventListener('click', () => { n = n > 1 ? n - 1 : 9; draw(); }); m.querySelector('#cp').addEventListener('click', () => { n = n < 9 ? n + 1 : 1; draw(); });
    m.querySelector('#play').addEventListener('click', () => {
      if (n === 7) { F().cylinder = 1; E.give('cylinder'); E.say('Through the horn, crackling: “Margaret… sign for Madame Zara… sign…” – a man’s voice, but it is Zara’s assistant putting it on. You take the cylinder.'); E.closeModal(); E.save(); }
      else m.querySelector('#cres').textContent = ['A brass band.', 'A music-hall song.', 'A recitation of “The Charge of the Light Brigade”.', 'Silence and hiss.'][n % 4];
    }); draw();
  });
}
function openLantern() {
  if (F().slide) return E.say('The slide box holds only views of the Alps now.');
  F().slide = 1; E.give('slide'); E.say('In the slide box, among views of the Alps: a glass slide of a pale lady in white, the “ghost” from the séance. You take it.');
}
function openStair() {
  if (!EVIDENCE.every(k => F()[k])) return E.say('The servants’ stair. But Lady Ashworth won’t believe you without proof – the photograph, the voice and the ghost. ' + (EVIDENCE.filter(k => F()[k]).length) + ' of 3 found.');
  E.cycler('Servants’ stair door', 'Three card slots, each with a carved tarot card that turns.', [0, 1, 2].map(i => ({ name: String(i + 1), opts: TAROT })), v => {
    if (v.join() !== 'The Moon,The Star,The Sun') return false; E.win(); return true;
  }, 'The cards click back. The door stays shut.', 'Turn the handle');
}
});
