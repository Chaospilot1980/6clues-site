/* Six Clues escape room #7 – The Polar Night (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const wood = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 12 }, (_, i) => `<rect x="0" y="${i * 56}" width="1600" height="50" fill="${c2}"/>`).join('')}<rect y="660" width="1600" height="240" fill="#2a2016"/><ellipse cx="800" cy="0" rx="560" ry="360" fill="url(#lamp)"/>`;
const snow = () => `<rect width="1600" height="900" fill="#0b1424"/>${Array.from({ length: 70 }, (_, i) => `<circle cx="${(i * 131) % 1600}" cy="${(i * 67) % 640}" r="2" fill="#dfe8f5" opacity=".7"/>`).join('')}<rect y="620" width="1600" height="280" fill="#cfd8e4"/>`;
const STEPS = ['Fuel tap ON', 'Choke CLOSED', 'Prime ×3', 'Pull cord', 'Choke OPEN'];

return {
  start: 'hut', v: 1,
  items: {
    kettle: ['🫖', 'Hot kettle', 'A kettle of boiling water from the stove. Steam pours from the spout.'],
    fuel: ['⛽', 'Jerrycan', 'A jerrycan of diesel, nearly full.'],
    pliers: ['🔧', 'Insulated pliers', 'Rubber-handled pliers from the shed toolbox.'],
    crystal: ['💎', 'Radio crystal', 'A quartz crystal in a small brass holder, marked “500 kc/s”.'],
  },
  rooms: {
    hut: {
      name: 'The station hut',
      bg: () => wood('#4a3424', '#523a28'),
      spots: [
        { id: 'stove', x: 60, y: 360, w: 280, h: 300, art: () => `<rect x="90" y="420" width="220" height="220" fill="#2a2a2a"/><rect x="170" y="380" width="60" height="40" rx="10" fill="#888"/>${L(200, 690, 'Stove & kettle')}`,
          act: () => { if (E.has('kettle') || F().steamed) return E.say('The stove ticks quietly.'); E.give('kettle'); E.say('You lift the kettle off the stove. It is boiling.'); } },
        { id: 'window', x: 380, y: 100, w: 340, h: 280, art: () => `<rect x="400" y="120" width="300" height="240" fill="${F().steamed ? '#41566e' : '#c8d6e6'}" stroke="#6b4a2a" stroke-width="12"/>${L(550, 400, F().steamed ? 'Window (writing in the frost)' : 'Frosted window')}`,
          act: () => E.say(F().steamed ? 'Scratched into the frost from outside: “SHED – OUR STATION NUMBER, LAST FOUR. – H.D.”' : 'Thick ice on the inside of the glass. You think there are marks under it.'),
          use: { kettle: () => { F().steamed = 1; E.take('kettle'); E.note('frost', 'Message scratched in the window frost by the chief, Henrik Dahl: “SHED – OUR STATION NUMBER, LAST FOUR. – H.D.”'); E.say('Steam softens the ice. Letters scratched from outside appear: “SHED – OUR STATION NUMBER, LAST FOUR. – H.D.”'); return true; } } },
        { id: 'photo', x: 760, y: 120, w: 200, h: 240, art: () => `<rect x="780" y="140" width="160" height="200" fill="#d8ccb0" stroke="#3a2a1a" stroke-width="8"/>${L(860, 380, 'Photo on the wall')}`,
          act: () => { E.note('photo', 'Photo on the wall: the chief kneeling beside a grey husky. Written on the back: “Me and my best friend, KIRA, 1956.”'); E.modal(`<h2>A photograph</h2><p>Henrik Dahl in his parka, kneeling in the snow beside a big grey husky. On the back, in pencil:</p><p class="paper">Me and my best friend, KIRA – Kapp Ruth, 1956.</p>`); } },
        { id: 'desk', x: 980, y: 400, w: 320, h: 260, art: () => `<rect x="990" y="460" width="300" height="40" fill="#5b3c25"/><rect x="1010" y="500" width="260" height="140" fill="#4a3020"/>${L(1140, 690, 'Chief’s desk')}`, act: () => openDesk() },
        { id: 'thermo', x: 1320, y: 140, w: 120, h: 260, art: () => `<rect x="1360" y="160" width="40" height="220" rx="20" fill="#eee"/><circle cx="1380" cy="370" r="22" fill="#c4232b"/>${L(1380, 420, 'Thermometer')}`,
          act: () => { E.note('indoor', 'Thermometer on the hut wall: +18 °C (indoors, by the stove).'); E.say('The thermometer on the wall reads +18 °C. Cosy – it’s right beside the stove.'); } },
        { id: 'jerry', x: 1460, y: 480, w: 130, h: 180, art: () => `<rect x="1480" y="520" width="90" height="120" fill="#7a2a1a"/>${L(1525, 690, 'Jerrycan')}`,
          act: () => { if (F().jerry) return E.say('An empty space by the door.'); F().jerry = 1; E.give('fuel'); E.say('A jerrycan of diesel, nearly full. Heavy.'); } },
        { id: 'toRadio', x: 20, y: 740, w: 280, h: 130, art: () => E.exit('← Radio room'), act: () => E.go('radio') },
        { id: 'toShed', x: 560, y: 720, w: 300, h: 150, art: () => E.exit(F().shedOpen ? '↓ Generator shed' : '↓ Path to the shed (padlocked)', 580), act: () => F().shedOpen ? E.go('shed') : E.numLock('Shed padlock', 'A frozen four-figure padlock on the shed door, twenty steps out in the storm.', 4, c => { if (c !== '1008') return false; F().shedOpen = 1; E.say('The frozen padlock gives. You haul the shed door open against the wind.'); E.go('shed'); return true; }) },
        { id: 'toTower', x: 1300, y: 740, w: 290, h: 130, art: () => E.exit('Instrument mast →', 1320), act: () => E.go('tower') },
      ],
    },
    radio: {
      name: 'The radio room',
      bg: () => wood('#3e2e22', '#463426'),
      spots: [
        { id: 'back', x: 1340, y: 740, w: 250, h: 130, art: () => E.exit('Hut →', 1360), act: () => E.go('hut') },
        { id: 'log', x: 80, y: 420, w: 300, h: 240, art: () => `${E.paper(100, 440, 260, 180, 6)}${L(230, 660, 'Station logbook')}`, act: () => openLog() },
        { id: 'tx', x: 440, y: 160, w: 560, h: 500, art: () => `<rect x="460" y="200" width="520" height="300" rx="10" fill="#2a2e2a"/>${[0, 1, 2, 3].map(i => `<circle cx="${540 + i * 120}" cy="300" r="34" fill="${F().power ? '#c9a24a' : '#555'}"/>`).join('')}<rect x="680" y="400" width="80" height="50" fill="${F().crystalIn ? '#9fc3d8' : '#111'}"/>${L(720, 690, `Transmitter${F().power ? ' (power on)' : ' (dead)'}`)}`, act: () => openTx(),
          use: { crystal: () => { F().crystalIn = 1; E.take('crystal'); E.say('The crystal clicks into its socket. 500 kc/s – the distress and calling frequency.'); return true; } } },
        { id: 'card', x: 1060, y: 160, w: 260, h: 280, art: () => `${E.paper(1080, 180, 220, 220, 6)}${L(1190, 440, 'Report card')}`,
          act: () => { E.note('card', 'Report card by the transmitter: “Weather report for aircraft: DD FF TT. DD = direction the wind comes FROM, in tens of degrees (two figures). FF = wind speed in knots. TT = outside temperature, whole degrees below zero.”'); E.modal(`<h2>Report card</h2><p class="paper"><b>Weather for aircraft: DD FF TT</b><br>DD – direction the wind blows FROM, in tens of degrees (two figures)<br>FF – wind speed in knots<br>TT – OUTSIDE temperature, whole degrees below zero</p>`); } },
      ],
    },
    shed: {
      name: 'The generator shed',
      bg: () => wood('#2e2a26', '#36312c'),
      spots: [
        { id: 'back', x: 20, y: 740, w: 280, h: 130, art: () => E.exit('↑ Back to the hut'), act: () => E.go('hut') },
        { id: 'manual', x: 80, y: 120, w: 280, h: 300, art: () => `${E.paper(100, 140, 240, 240, 7)}${L(220, 420, 'Generator manual')}`, act: () => openManual() },
        { id: 'generator', x: 420, y: 300, w: 640, h: 360, art: () => `<rect x="450" y="380" width="580" height="260" rx="20" fill="${F().power ? '#3a6a3a' : '#5a5a50'}"/><circle cx="560" cy="510" r="60" fill="#333"/>${L(740, 690, F().power ? 'Generator (running)' : F().fuelled ? 'Generator (fuelled)' : 'Generator (empty)')}`, act: () => openGenerator(),
          use: { fuel: () => { F().fuelled = 1; E.take('fuel'); E.say('You pour the diesel in. The tank gauge swings to full.'); return true; } } },
        { id: 'toolbox', x: 1120, y: 480, w: 300, h: 180, art: () => `<rect x="1140" y="540" width="260" height="100" fill="#a33"/>${L(1270, 690, 'Toolbox')}`,
          act: () => { if (F().pliers) return E.say('Spanners, a hammer, a coil of wire.'); F().pliers = 1; E.give('pliers'); E.say('You take a pair of insulated pliers.'); } },
      ],
    },
    tower: {
      name: 'The instrument mast',
      bg: () => snow(),
      spots: [
        { id: 'back', x: 20, y: 740, w: 280, h: 130, art: () => E.exit('← Hut'), act: () => E.go('hut') },
        { id: 'vane', x: 120, y: 60, w: 300, h: 300, art: () => `<line x1="270" y1="120" x2="270" y2="340" stroke="#888" stroke-width="10"/><path d="M190 160 L350 80 L330 110 L380 140z" fill="#c9a24a"/>${L(270, 380, 'Wind vane')}`, act: () => openVane() },
        { id: 'anemo', x: 480, y: 60, w: 300, h: 300, art: () => `<line x1="630" y1="160" x2="630" y2="340" stroke="#888" stroke-width="10"/>${[0, 1, 2].map(i => `<circle cx="${630 + Math.cos(i * 2.1) * 70}" cy="${150 + Math.sin(i * 2.1) * 20}" r="22" fill="#c9a24a"/>`).join('')}${L(630, 380, 'Anemometer')}`, act: () => openAnemo() },
        { id: 'screen', x: 860, y: 260, w: 260, h: 380, art: () => `<rect x="890" y="300" width="200" height="200" fill="#eee" stroke="#888" stroke-width="6"/><line x1="990" y1="500" x2="990" y2="620" stroke="#888" stroke-width="12"/>${L(990, 660, 'Thermometer screen')}`,
          act: () => { E.note('screen', 'Thermometer inside the white louvred screen outside: −27 °C.'); E.say('Inside the white louvred box, the outdoor thermometer reads −27 °C.'); } },
        { id: 'aerial', x: 1180, y: 40, w: 380, h: 560, art: () => `<line x1="1370" y1="60" x2="1370" y2="600" stroke="#666" stroke-width="12"/><line x1="1370" y1="80" x2="1220" y2="${F().aerial ? 80 : 400}" stroke="#222" stroke-width="5"/>${L(1370, 640, F().aerial ? 'Aerial (reconnected)' : 'Aerial mast – wire hanging loose')}`,
          act: () => E.say(F().aerial ? 'The aerial wire is back on its insulator.' : 'The aerial wire has been cut at the insulator and is whipping in the wind. You need a tool to twist it back on.'),
          use: { pliers: () => { F().aerial = 1; E.take('pliers'); E.say('Fingers numb, you twist the aerial wire back onto the insulator with the pliers.'); return true; } } },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['frost', () => F().steamed, ['The window is iced over on the inside – but there are marks under the ice.', 'Something hot would melt it. The stove has a kettle.', 'Take the kettle and use it on the window.']],
    ['shed', () => F().shedOpen, ['The chief wrote: our station number, last four figures.', 'The station logbook gives the official station number.', 'WMO station 01008 → 1008.']],
    ['fuel', () => F().fuelled, ['The generator tank is empty.', 'There is a jerrycan by the hut door.', 'Use the jerrycan on the generator.']],
    ['start', () => F().power, ['Diesel generators in the cold must be started in the right order.', 'The manual on the shed wall gives the order.', 'Fuel tap ON, Choke CLOSED, Prime ×3, Pull cord, Choke OPEN.']],
    ['crystal', () => F().crystalIn, ['The transmitter has an empty crystal socket.', 'The chief’s desk drawer has a word lock: his best friend.', 'The photo: KIRA, the husky. Take the crystal and use it on the transmitter.']],
    ['aerial', () => F().aerial, ['Without an aerial nobody will hear you.', 'The aerial wire at the mast has been cut loose. The shed toolbox has something insulated.', 'Use the pliers on the aerial at the instrument mast.']],
    ['report', () => F().won, ['The aircraft needs DD FF TT. Read the card in the radio room.', 'A wind vane’s arrow points INTO the wind. The anemometer card turns counts into knots. Use the OUTSIDE thermometer.', 'Vane points to 050° → 05; 46 turns ÷ 2 = 23 knots; −27 °C → 27. Send 052327.']],
  ],
  intro: ['Kapp Ruth weather station, Svalbard · 12 January 1958 · 23:55', 'The Polar Night',
    `<p>You are the young radio operator at a four-man weather station at the top of the world. It is polar night – no sun for weeks. This evening the chief, Henrik Dahl, went out to check the aerial and did not come back. Then the lights died.</p><p>At 01:00 the last supply plane of the winter flies over. If it does not get a weather report from Kapp Ruth, it turns back to Norway – and nobody will search the ice for Dahl.</p><p>Level 2: not every reading in this hut tells you what you need.</p>`,
    'The stove is the only light. Wind screams around the hut. Look around.'],
  timesUp: ['01:00.', 'Far above the storm, the drone of the supply plane fades away south.'],
  win: ['The plane banks overhead', '“Kapp Ruth, Kapp Ruth, we read you.” The pilot drops flares over the ice – and in their light the crew spots a figure waving outside the old trappers’ hut a mile north: Henrik Dahl, frostbitten and furious, alive. He had gone to fix the aerial and found the wire cut. That is a story for the morning.'],
};

function openDesk() {
  if (F().drawer) return E.say('The drawer stands open. Pencils, a pipe and a ration of chocolate.');
  E.wordLock('Chief’s desk drawer', 'A little brass letter lock with four wheels. On the drawer front someone has carved: <i>“my best friend”</i>.', 4, w => { if (w !== 'KIRA') return false; F().drawer = 1; E.give('crystal'); E.say('The drawer slides open: a quartz radio crystal in a brass holder, marked “500 kc/s”.'); return true; });
}
function openLog() {
  E.note('log', 'Station logbook: “Kapp Ruth meteorological station, WMO no. 01008, call sign LMR7. Synop every three hours.” Last entry, 22:40: “Aerial signal weak. H.D. going out to look.”');
  E.modal(`<h2>Station logbook</h2><p class="paper">Kapp Ruth meteorological station<br>WMO station no. 01008 · call sign LMR7<br><br>22:40 – Aerial signal weak. H.D. going out to look.<br>23:20 – H.D. not back. Lights out.</p>`);
}
function openTx() {
  if (!F().power) return E.say('Dead. No power – the generator in the shed has stopped.');
  if (!F().crystalIn) return E.say('The valves glow orange, but the crystal socket is empty. Without it the set can’t find its frequency.');
  if (!F().aerial) return E.say('The set hums, but the aerial meter doesn’t move. Your signal goes nowhere – the aerial must be broken.');
  E.numLock('Morse key', 'Everything is ready. Tap out the weather report for the aircraft: six figures.', 6, c => { if (c !== '052327') return false; E.say('Dah-dit-dah… The headphones crackle back: “LMR7, QSL – we read you.”'); E.win(); return true; }, 'Silence in the headphones. The plane doesn’t answer that.');
}
function openManual() {
  E.note('manual', 'Generator manual, cold start: 1 Fuel tap ON · 2 Choke CLOSED · 3 Prime ×3 · 4 Pull cord · 5 Choke OPEN when running.');
  E.modal(`<h2>Generator manual – cold start</h2><p class="paper">1. Fuel tap ON<br>2. Choke CLOSED<br>3. Prime ×3<br>4. Pull cord<br>5. Choke OPEN once running</p>`);
}
function openGenerator() {
  if (F().power) return E.say('The generator thumps steadily. Light in every window of the station.');
  if (!F().fuelled) return E.say('The generator has run dry. The tank gauge reads empty.');
  E.orderer('Generator controls', 'Five controls. The engine is ice cold.', ['Pull cord', 'Choke OPEN', 'Fuel tap ON', 'Prime ×3', 'Choke CLOSED'], o => { if (o.join() !== STEPS.join()) return false; F().power = 1; E.say('It coughs, catches and thunders into life. Across the yard the hut windows light up.'); return true; }, 'The engine coughs and dies. You set the controls back.');
}
function openVane() {
  E.note('vane', 'The wind vane’s arrow points to 050° (north-east) on the compass ring. (A wind vane’s arrow points into the wind.)');
  E.modal(`<h2>Wind vane</h2><svg viewBox="0 0 300 300" class="close" style="max-width:300px"><circle cx="150" cy="150" r="120" fill="#e9dcb8"/>${['N', 'E', 'S', 'W'].map((d, i) => `<text x="${150 + Math.sin(i * Math.PI / 2) * 100}" y="${158 - Math.cos(i * Math.PI / 2) * 100}" text-anchor="middle" font-size="24" font-family="Georgia">${d}</text>`).join('')}<g transform="rotate(50 150 150)"><line x1="150" y1="230" x2="150" y2="70" stroke="#3a2a1a" stroke-width="6"/><path d="M150 50 L135 85 L165 85z" fill="#c4232b"/><path d="M135 230 h30 l-5 30 h-20z" fill="#3a2a1a"/></g></svg><p class="small">The red arrow head points to 050°. A weather vane always turns its arrow into the wind.</p>`);
}
function openAnemo() {
  E.note('anemo', 'Anemometer counter: 46 turns in the last minute. Card on the mast: “knots = turns per minute ÷ 2”.');
  E.modal(`<h2>Anemometer</h2><p>The cups spin in a blur. The counter box on the mast shows <b>46 turns</b> in the last minute.</p><p class="paper">Calibration card: knots = turns per minute ÷ 2</p>`);
}
});
