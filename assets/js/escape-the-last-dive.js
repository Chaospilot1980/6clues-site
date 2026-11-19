/* Six Clues escape room #17 – The Last Dive (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const steel = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 9 }, (_, i) => `<rect x="${i * 190}" y="0" width="12" height="660" fill="${c2}"/>`).join('')}<path d="M0 0 Q800 120 1600 0" fill="${c2}"/><rect y="660" width="1600" height="240" fill="#1a1e1e"/>`;
const SW = ['Off', 'On'];

return {
  start: 'control', v: 2,
  items: {
    codebook: ['📕', 'Codebook', 'The captain’s red codebook: a letter-for-number table.'],
    engineKey: ['🗝️', 'Engine room key', 'A heavy key stamped ENG.'],
    torch: ['🔦', 'Torch (no battery)', 'A rubber torch. The battery is missing.'],
    battery: ['🔋', 'Battery', 'A big square torch battery.'],
    lit: ['🔦', 'Working torch', 'A torch with a strong beam.'],
    wrench: ['🔧', 'Valve wrench', 'A long wrench for seized valves.'],
    patch: ['🩹', 'Leak patch kit', 'A rubber pad, clamps and sealant.'],
  },
  rooms: {
    control: {
      name: 'The control room',
      bg: () => steel('#1e2a28', '#2a3a36'),
      spots: [
        { id: 'plaque', photo: [245, 130, 195, 130], x: 80, y: 80, w: 320, h: 160, art: () => `<rect x="100" y="100" width="280" height="100" fill="#c9a24a"/>${L(240, 230, 'Brass plaque')}`,
          act: () => { E.note('plaque', 'Brass plaque: “HMS Narwhal – hull number S-417 – launched 1958.”'); E.say('“HMS Narwhal – hull number S-417 – launched 1958.”'); } },
        { id: 'locker', photo: [260, 305, 290, 495], x: 80, y: 300, w: 320, h: 320, art: () => `<rect x="100" y="320" width="280" height="280" fill="#3a4a46"/>${L(240, 640, F().locker ? 'Captain’s locker (open)' : 'Captain’s locker (3 numbers)')}`, act: () => openLocker() },
        { id: 'periscope', photo: [700, 0, 185, 850], x: 600, y: 60, w: 200, h: 460, art: () => `<rect x="680" y="60" width="40" height="400" fill="#555"/><rect x="640" y="400" width="120" height="60" fill="#444"/>${L(700, 500, 'Periscope')}`,
          act: () => E.say('You look through the periscope: only black water and a flicker of silt. You are far too deep – a hundred metres down.') },
        { id: 'orders', photo: [1000, 130, 145, 230], x: 840, y: 100, w: 320, h: 240, art: () => `${E.paper(860, 120, 280, 180, 6)}${L(1000, 330, 'Emergency orders')}`,
          act: () => { E.note('orders', 'Emergency orders: “1. Seal any leak. 2. Restore power to the ballast pumps. 3. Blow the ballast tanks in the order radioed from the surface – never guess, the boat will roll.”'); E.say('Emergency orders: seal the leak, restore pump power, then blow the tanks in the order radioed from the surface.'); } },
        { id: 'aid', photo: [1195, 100, 170, 150], x: 1240, y: 120, w: 260, h: 200, art: () => `<rect x="1260" y="140" width="220" height="140" fill="#e8e8e8"/><rect x="1350" y="170" width="40" height="80" fill="#c03030"/><rect x="1330" y="190" width="80" height="40" fill="#c03030"/>${L(1370, 320, 'First-aid box')}`,
          act: () => { if (F().aid) return E.say('Bandages and smelling salts.'); F().aid = 1; E.give('battery'); E.say('Bandages, smelling salts – and a big spare torch battery.'); } },
        { id: 'ballast', photo: [995, 385, 280, 220], x: 860, y: 400, w: 440, h: 240, art: () => `<rect x="880" y="420" width="400" height="200" fill="#2a2a2a"/>${Array.from({ length: 8 }, (_, i) => `<circle cx="${920 + i * 46}" cy="520" r="16" fill="#c03030"/>`).join('')}${L(1080, 660, 'Ballast panel – 8 tanks')}`, act: () => openBallast() },
        { id: 'toRadio', photo: [0, 200, 225, 600], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Radio room'), act: () => E.go('radio') },
        { id: 'toEngine', photo: [1315, 255, 285, 545], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit(F().engine ? 'Engine room →' : 'Engine room (locked)', 1240), act: () => F().engine ? E.go('engine') : E.say('A watertight door marked ENGINE ROOM. Locked.'),
          use: { engineKey: () => { F().engine = 1; E.take('engineKey'); E.say('The heavy door swings open. Beyond it, total darkness.'); return true; } } },
      ],
    },
    radio: {
      name: 'The radio room',
      bg: () => steel('#1a2228', '#26323a'),
      spots: [
        { id: 'back', photo: [1405, 40, 195, 825], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Control room →', 1240), act: () => E.go('control') },
        { id: 'printout', photo: [15, 305, 445, 355], x: 120, y: 160, w: 380, h: 280, art: () => `${E.paper(140, 180, 340, 220, 5)}${L(310, 440, 'Teleprinter message')}`,
          act: () => F().decoded ? E.say('Decoded: “BLOW TANKS TWO FIVE SEVEN. NO OTHERS.”') : (E.note('print', 'Teleprinter message from the surface, in code: “14-9-8 / 26 – 5 – 3”. Stamped: USE CAPTAIN’S CODEBOOK.'), E.say('A coded message from the surface: “14-9-8 / 26 – 5 – 3”. Stamped: USE CAPTAIN’S CODEBOOK.')),
          use: { codebook: () => { F().decoded = 1; E.note('decoded', 'Decoded with the codebook: “BLOW TANKS 2 – 5 – 7. NO OTHERS.” (Codebook: 14-9-8 = BLOW TANKS; 26 = 2, 5 = 5, 3 = 7.)'); E.say('With the codebook, the message reads: “BLOW TANKS 2 – 5 – 7. NO OTHERS.”'); return true; } } },
        { id: 'oldmsg', photo: [420, 155, 155, 245], x: 560, y: 160, w: 300, h: 240, art: () => `${E.paper(580, 180, 260, 180, 4)}${L(710, 400, 'Old message, crumpled')}`,
          act: () => { E.note('old', 'A crumpled old message from last week: “Exercise: blow tanks 1-3-8.” Stamped EXERCISE ONLY.'); E.say('An old crumpled message: “Exercise: blow tanks 1-3-8.” Stamped EXERCISE ONLY.'); } },
        { id: 'desk', photo: [655, 535, 740, 365], x: 920, y: 420, w: 400, h: 220, art: () => `<rect x="940" y="480" width="360" height="30" fill="#4a4a40"/>${L(1120, 660, 'Radio operator’s desk')}`,
          act: () => { if (F().desk) return E.say('Pencils and a cold cup of tea.'); F().desk = 1; E.give('torch'); E.say('In the drawer: a rubber torch. Its battery is missing.'); } },
        { id: 'set', photo: [755, 35, 590, 350], x: 920, y: 120, w: 520, h: 260, art: () => `<rect x="940" y="140" width="480" height="200" fill="#2a2a24"/>${[0, 1, 2, 3].map(i => `<circle cx="${1000 + i * 110}" cy="240" r="30" fill="#888"/>`).join('')}${L(1180, 370, 'Radio set')}`,
          act: () => E.say('The surface ship is calling: “Narwhal, Narwhal, do you read? Air will last fifty minutes. Blow your tanks!” Your transmitter is broken – but you can still read their message.') },
      ],
    },
    engine: {
      name: 'The engine room',
      bg: () => F().light ? steel('#2a2620', '#3a3428') : `<rect width="1600" height="900" fill="#050505"/>`,
      spots: [
        { id: 'back', photo: [0, 80, 190, 720], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Control room'), act: () => E.go('control') },
        { id: 'dark', keep: 1, x: 300, y: 100, w: 1000, h: 560, hide: () => F().light, art: () => `<rect x="190" width="1410" height="900" fill="#030406" opacity=".96" pointer-events="none"/>${L(800, 400, 'Pitch black. You can’t see a thing.')}`,
          act: () => E.say('It’s pitch black. You hear dripping and something humming.'), use: { lit: () => { F().light = 1; E.take('lit'); E.say('The torch beam swings over pipes, valves and a big breaker panel.'); return true; } } },
        { id: 'diagram', photo: [225, 115, 195, 400], x: 100, y: 120, w: 340, h: 280, hide: () => !F().light, art: () => `${E.paper(120, 140, 300, 220, 6)}${L(270, 400, 'Wiring diagrams')}`,
          act: () => { E.note('wiring', 'Two wiring diagrams on the wall. Old one (crossed out, “superseded 1961”): A on, B on, C off, D off. New one (1962): “Ballast pumps – A ON, B OFF, C ON, D ON.”'); E.say('Two wiring diagrams. The old one is crossed out. The new one says: A ON, B OFF, C ON, D ON.'); } },
        { id: 'breakers', photo: [495, 180, 345, 345], x: 500, y: 140, w: 420, h: 360, hide: () => !F().light, art: () => `<rect x="520" y="160" width="380" height="320" fill="#2a2a2a"/>${[0, 1, 2, 3].map(i => `<rect x="${560 + i * 85}" y="260" width="40" height="80" fill="#888"/>`).join('')}${L(710, 520, F().power ? 'Breakers (pumps powered)' : 'Breaker panel A–D')}`, act: () => openBreakers() },
        { id: 'toolbox', photo: [1085, 620, 250, 180], x: 1000, y: 420, w: 320, h: 220, hide: () => !F().light, art: () => `<rect x="1020" y="480" width="280" height="140" fill="#a03020"/>${L(1160, 660, 'Toolbox')}`,
          act: () => { if (F().tools) return E.say('Spanners and screwdrivers, nothing else useful.'); F().tools = 1; E.give('wrench'); E.give('patch'); E.say('In the toolbox: a long valve wrench and a leak patch kit.'); } },
        { id: 'toTorpedo', photo: [1335, 95, 265, 705], x: 1220, y: 740, w: 360, h: 130, hide: () => !F().light, art: () => E.exit(F().hatch ? 'Torpedo room →' : 'Hatch (seized)', 1240), act: () => F().hatch ? E.go('torpedo') : E.say('The hatch to the torpedo room is seized solid. You can hear water spraying on the other side!'),
          use: { wrench: () => { F().hatch = 1; E.say('You lean on the wrench. With a screech, the hatch wheel turns.'); return true; } } },
      ],
    },
    torpedo: {
      name: 'The torpedo room',
      bg: () => steel('#1a2228', '#283038'),
      spots: [
        { id: 'back', photo: [0, 0, 225, 900], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Engine room'), act: () => E.go('engine') },
        { id: 'leak', photo: [800, 250, 240, 480], x: 500, y: 140, w: 400, h: 340, art: () => `<rect x="520" y="160" width="360" height="40" fill="#555"/>${F().patched ? '' : '<path d="M700 200 L660 460 M700 200 L740 460 M700 200 L700 480" stroke="#7ab8d8" stroke-width="10"/>'}${L(700, 520, F().patched ? 'Pipe (sealed)' : 'Spraying leak!')}`,
          act: () => F().patched ? E.say('The patch holds. The water has stopped.') : E.say('Sea water sprays from a cracked pipe! You need to seal it.'),
          use: { patch: () => { F().patched = 1; E.take('patch'); E.say('You clamp the rubber patch over the crack and tighten it. The spray stops!'); return true; } } },
        { id: 'tubes', photo: [1235, 45, 245, 700], x: 980, y: 200, w: 520, h: 400, art: () => `${[0, 1, 2].map(i => `<circle cx="${1080 + i * 160}" cy="400" r="60" fill="#3a3a3a" stroke="#777" stroke-width="10"/>`).join('')}${L(1240, 620, 'Torpedo tubes')}`,
          act: () => E.say('Three torpedo tubes, all empty and sealed. Thankfully – this is no time for a war.') },
        { id: 'bunks', photo: [245, 185, 435, 510], x: 80, y: 200, w: 340, h: 360, art: () => `<rect x="100" y="240" width="300" height="80" fill="#4a5a5a"/><rect x="100" y="400" width="300" height="80" fill="#4a5a5a"/>${L(250, 580, 'Crew bunks')}`,
          act: () => E.say('Two sailors asleep from the gas, breathing slowly. They’ll wake up once you get fresh air in.') },
      ],
    },
  },
  combine: (a, b) => { if ([a, b].sort().join() === 'battery,torch') { E.take('battery'); E.take('torch'); E.give('lit'); F().lit = 1; E.say('The battery clicks in. The torch shines bright.'); return true; } return false; },
  stages: [
    ['locker', () => F().locker, ['The captain’s locker wants three numbers.', 'Look at the brass plaque.', 'Hull number S-417: 417.']],
    ['decoded', () => F().decoded, ['The radio room has a coded message from the surface.', 'The captain’s locker had a codebook. The crumpled message is only an old exercise.', 'Use the codebook on the teleprinter message.']],
    ['light', () => F().light, ['The engine room is pitch black.', 'There is a torch in the radio desk and a battery in the first-aid box.', 'Combine them and use the torch on the darkness.']],
    ['power', () => F().power, ['The ballast pumps need power.', 'The new wiring diagram, not the old one.', 'A ON, B OFF, C ON, D ON.']],
    ['hatch', () => F().hatch, ['The torpedo room hatch is seized.', 'The toolbox has a long wrench.', 'Use the wrench on the hatch.']],
    ['patch', () => F().patched, ['Water is spraying in the torpedo room.', 'You have a patch kit.', 'Use the patch kit on the leak.']],
    ['ballast', () => F().won, ['Now blow the ballast tanks.', 'The decoded message, not the exercise.', '2, 5, 7.']],
  ],
  intro: ['North Atlantic · 9 October 1962 · 03:00', 'The Last Dive',
    `<p>You are the youngest radio operator on the submarine HMS Narwhal. An explosion in the batteries has filled the boat with gas – the rest of the crew are unconscious, and the Narwhal is lying on the seabed a hundred metres down, slowly flooding.</p><p>The surface ship says your air will last one hour. Seal the leak, get power to the pumps and blow the ballast tanks – in exactly the right order.</p><p>Level 2: not every order you find is the right one.</p>`,
    'Red emergency lights, dripping pipes and an awful silence. Look around.'],
  timesUp: ['The air is thin…', 'Your head spins – but you can still save the boat.'],
  win: ['Surface!', 'With a roar of air the tanks blow, the Narwhal tilts up and rises through a hundred metres of black water into grey morning light. The hatch opens, fresh air pours in – and the crew start to wake up.'],
};

function openLocker() {
  if (F().locker) return E.say('The captain’s locker is empty now.');
  E.numLock('Captain’s locker', 'A steel locker with three number wheels and a brass nameplate: “Ship before self.”', 3, c => { if (c !== '417') return false; F().locker = 1; E.give('codebook'); E.give('engineKey'); E.say('The locker opens: the captain’s red codebook and the engine room key.'); return true; });
}
function openBreakers() {
  if (F().power) return E.say('The breakers hum. Green light: BALLAST PUMPS – POWER.');
  E.cycler('Breaker panel', 'Four big breakers, A to D.', ['A', 'B', 'C', 'D'].map(n => ({ name: n, opts: SW })), v => { if (v.join() !== 'On,Off,On,On') return false; F().power = 1; E.say('Clunk-clunk-clunk. A green light: BALLAST PUMPS – POWER.'); return true; }, 'Sparks! The breakers trip back. Wrong setting.', 'Throw the switches');
}
function openBallast() {
  if (!F().patched) return E.say('A warning light on the ballast panel: LEAK – SEAL BEFORE BLOWING.');
  if (!F().power) return E.say('The ballast panel is dead: NO PUMP POWER.');
  E.numLock('Ballast panel', 'Eight red tank buttons. Enter the three tanks to blow, in order.', 3, c => { if (c !== '257') return false; E.win(); return true; }, 'The boat lurches and rolls! You stop the pumps just in time. Wrong tanks.');
}
});
