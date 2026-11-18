/* Six Clues escape room #13 – Countdown on the Space Station (level 1, family). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const space = c => `<rect width="1600" height="900" fill="${c}"/>${Array.from({ length: 6 }, (_, i) => `<rect x="0" y="${i * 150}" width="1600" height="6" fill="#3a4a5a"/>`).join('')}<rect y="680" width="1600" height="220" fill="#2a3440"/>`;
const PLANETS = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn'];

return {
  start: 'module', v: 1,
  items: {
    card: ['💳', 'Access card', 'Commander Okoye’s blue access card.'],
    fuse: ['🔌', 'Fuse', 'A glowing green power fuse.'],
    wrench: ['🔧', 'Space wrench', 'A wrench tied to a cord so it can’t float away.'],
    chip: ['💾', 'Navigation chip', 'A small silver chip labelled NAV.'],
    suit: ['🧑‍🚀', 'Space helmet', 'A spacesuit helmet with a working radio.'],
  },
  rooms: {
    module: {
      name: 'The crew module',
      bg: () => space('#1e2a36'),
      spots: [
        { id: 'window', x: 560, y: 100, w: 480, h: 320, art: () => `<circle cx="800" cy="260" r="150" fill="#05080e" stroke="#9aaabb" stroke-width="16"/><circle cx="860" cy="230" r="40" fill="#3a7ad0"/>${L(800, 450, 'Round window')}`,
          act: () => E.say('Earth turns slowly below, blue and white. Somewhere down there, mission control is waiting.') },
        { id: 'bunk', x: 60, y: 300, w: 380, h: 300, art: () => `<rect x="80" y="340" width="340" height="220" rx="20" fill="#4a5a6a"/>${L(250, 600, 'Sleeping bag on the wall')}`,
          act: () => { if (F().card) return E.say('An empty sleeping bag, strapped to the wall.'); F().card = 1; E.give('card'); E.say('Floating inside the sleeping bag: Commander Okoye’s access card!'); } },
        { id: 'board', x: 1120, y: 120, w: 380, h: 280, art: () => `${E.paper(1140, 140, 340, 220, 6)}${L(1310, 400, 'Message board')}`,
          act: () => { E.note('board', 'Message board: “Kids’ school quiz from Earth: put the planets in order from the Sun! – Mercury, Venus, Earth, Mars, Jupiter, Saturn. Ten points each!”'); E.say('A school quiz from Earth is pinned to the board: the planets in order from the Sun.'); } },
        { id: 'locker', x: 520, y: 480, w: 360, h: 180, art: () => `<rect x="540" y="500" width="320" height="140" fill="#6a7a8a"/>${L(700, 680, F().locker ? 'Tool locker (open)' : 'Tool locker (card reader)')}`,
          act: () => F().locker ? E.say('The tool locker is empty now.') : E.say('A tool locker with a card reader blinking red.'),
          use: { card: () => { F().locker = 1; E.give('wrench'); E.say('Beep! The locker opens. A space wrench floats out on its cord.'); return true; } } },
        { id: 'toLab', x: 20, y: 740, w: 300, h: 130, art: () => E.exit(F().hatch ? '← Science lab' : '← Hatch to lab (stuck)'), act: () => F().hatch ? E.go('lab') : E.say('The hatch wheel is stuck tight. You’d need a tool to turn it.'),
          use: { wrench: () => { F().hatch = 1; E.say('With the wrench, the hatch wheel turns. Clunk – it swings open.'); return true; } } },
        { id: 'toCockpit', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit(F().power ? 'Cockpit →' : 'Cockpit (no power)', 1240), act: () => F().power ? E.go('cockpit') : E.say('The cockpit door won’t open – no power. The fuse box must be dead.') },
      ],
    },
    lab: {
      name: 'The science lab',
      bg: () => space('#1a2e2a'),
      spots: [
        { id: 'back', x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Crew module →', 1240), act: () => E.go('module') },
        { id: 'plants', x: 80, y: 260, w: 380, h: 340, art: () => `<rect x="100" y="420" width="340" height="140" fill="#5a4a3a"/>${[0, 1, 2].map(i => `<circle cx="${170 + i * 100}" cy="380" r="40" fill="#3aa04a"/>`).join('')}${L(270, 600, 'Space garden')}`,
          act: () => { E.note('plants', 'Space garden labels: lettuce – 4 leaves · tomato – 2 fruits · bean – 9 pods. A note: “Robot code = how many leaves, fruits and pods, in that order.”'); E.say('Three little plants under purple light. Labels: lettuce 4 leaves, tomato 2 fruits, bean 9 pods. A note says the robot code is those numbers in order.'); } },
        { id: 'robot', x: 540, y: 300, w: 340, h: 340, art: () => `<rect x="600" y="340" width="220" height="200" rx="30" fill="#c0c8d0"/><circle cx="660" cy="420" r="20" fill="#2a7ad0"/><circle cx="760" cy="420" r="20" fill="#2a7ad0"/>${L(710, 600, 'Helper robot')}`, act: () => openRobot() },
        { id: 'planets', x: 960, y: 120, w: 520, h: 300, art: () => `<rect x="980" y="140" width="480" height="240" fill="#0a0e18"/>${PLANETS.map((p, i) => `<circle cx="${1020 + i * 80}" cy="260" r="${14 + i * 3}" fill="#c9a24a"/>`).join('')}${L(1220, 410, F().planets ? 'Planet panel (done)' : 'Planet panel – put them in order')}`, act: () => openPlanets() },
        { id: 'fusebox', x: 980, y: 470, w: 300, h: 190, art: () => `<rect x="1000" y="490" width="260" height="150" fill="#3a3a3a"/>${L(1130, 680, F().power ? 'Fuse box (power on)' : 'Fuse box (empty slot)')}`,
          act: () => F().power ? E.say('Green lights everywhere. Power is back.') : E.say('One fuse slot is empty. Without it, the cockpit has no power.'),
          use: { fuse: () => { F().power = 1; E.take('fuse'); E.say('The fuse clicks in. Lights flicker on all over the station!'); return true; } } },
      ],
    },
    cockpit: {
      name: 'The cockpit',
      bg: () => space('#141a2a'),
      spots: [
        { id: 'back', x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Crew module'), act: () => E.go('module') },
        { id: 'console', x: 360, y: 380, w: 880, h: 280, art: () => `<rect x="380" y="420" width="840" height="220" fill="#2a3440"/>${[0, 1, 2, 3, 4].map(i => `<rect x="${420 + i * 160}" y="460" width="120" height="60" fill="#3a7ad0"/>`).join('')}${L(800, 680, 'Flight console')}`, act: () => openConsole(),
          use: { chip: () => { F().chipIn = 1; E.take('chip'); E.say('The navigation chip slides into the console. A screen lights up: “ENTER RE-ENTRY ANGLE”.'); return true; } } },
        { id: 'radio', x: 1260, y: 160, w: 280, h: 260, art: () => `<rect x="1280" y="180" width="240" height="200" fill="#3a4a3a"/>${L(1400, 410, 'Radio')}`,
          act: () => { if (!F().helmet) return E.say('Static. The radio speaker is broken – but you might hear through a spacesuit helmet radio.'); E.note('radio', 'Mission control on the helmet radio: “Capsule, set re-entry angle to 4-0 and press LAUNCH. Over.”'); E.say('Through the helmet radio, crackling: “Set re-entry angle to 4-0 and press LAUNCH. Over.”'); },
          use: { suit: () => { F().helmet = 1; E.note('radio', 'Mission control on the helmet radio: “Capsule, set re-entry angle to 4-0 and press LAUNCH. Over.”'); E.say('You hold the helmet to the radio. Crackling: “Set re-entry angle to 4-0 and press LAUNCH. Over.”'); return true; } } },
        { id: 'suits', x: 80, y: 120, w: 300, h: 460, art: () => `<rect x="120" y="160" width="200" height="380" rx="60" fill="#e8e8e8"/>${L(220, 600, 'Spacesuit')}`,
          act: () => { if (F().suit) return E.say('The spacesuit hangs there without its helmet.'); F().suit = 1; E.give('suit'); E.say('You unclip the spacesuit’s helmet. The little radio in it crackles.'); } },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['card', () => F().locker, ['The tool locker needs a card.', 'Look where the commander sleeps.', 'Take the card from the sleeping bag and use it on the locker.']],
    ['hatch', () => F().hatch, ['The hatch to the lab is stuck.', 'The locker had a tool.', 'Use the space wrench on the hatch.']],
    ['planets', () => F().planets, ['The planet panel wants six planets in order.', 'The school quiz on the message board has the order.', 'Mercury, Venus, Earth, Mars, Jupiter, Saturn.']],
    ['robot', () => F().robot, ['The helper robot wants a three-number code.', 'Count things in the space garden.', 'Lettuce 4, tomato 2, bean 9: 429.']],
    ['power', () => F().power, ['The cockpit has no power.', 'The robot gave you something that glows green.', 'Use the fuse on the fuse box in the lab.']],
    ['radio', () => F().helmet, ['The radio speaker is broken.', 'A spacesuit helmet has a radio in it.', 'Take the helmet and use it on the radio.']],
    ['launch', () => F().won, ['The console needs the navigation chip and an angle.', 'Put in the chip, then listen to mission control.', 'Angle 40.']],
  ],
  intro: ['Low Earth orbit · 2049 · 13:00', 'Countdown on the Space Station',
    `<p>You are the youngest astronaut on Star Station Lyra. A meteor storm has knocked out the power, and the rest of the crew have already flown home in the first capsule.</p><p>The last escape capsule must leave in one hour, before the station drifts out of range. Get the power back, find the navigation chip and fly home!</p><p>Level 1: perfect for families and first-time players.</p>`,
    'Everything floats a little. A red light blinks. Look around.'],
  timesUp: ['Out of range!', 'The radio crackles: “We can still bring you home – keep going!”'],
  win: ['Splashdown!', 'The capsule drops out of the sky under three big orange parachutes and lands with a splash in the ocean. Mission control cheers. You are the hero of the station!'],
};

function openRobot() {
  if (F().robot) return E.say('The robot hums happily.');
  if (!F().planets) return E.say('The robot is asleep. Its screen says: “WAKE ME WITH THE PLANET PANEL.”');
  E.numLock('Helper robot', 'The robot’s chest screen says: “HELLO! ENTER GARDEN CODE.”', 3, c => { if (c !== '429') return false; F().robot = 1; E.give('fuse'); E.give('chip'); E.say('“CODE CORRECT!” The robot opens its tummy: a green fuse and a silver navigation chip.'); return true; }, 'The robot beeps sadly: “WRONG CODE.”');
}
function openPlanets() {
  if (F().planets) return E.say('The planets glow in a neat row.');
  E.orderer('Planet panel', 'Tap the planets in order, starting nearest the Sun.', ['Mars', 'Earth', 'Saturn', 'Mercury', 'Jupiter', 'Venus'], v => { if (v.join() !== PLANETS.join()) return false; F().planets = 1; E.note('pl', 'The planet panel lit up and showed a message: “Well done! Robot needs the garden code.”'); E.say('Ding! “Well done! The robot needs the garden code.”'); return true; }, 'Bzzt! The planets go dark again.');
}
function openConsole() {
  if (!F().chipIn) return E.say('The flight console is dark. A slot says NAV CHIP.');
  E.numLock('Re-entry angle', 'Two number wheels for the re-entry angle. Then LAUNCH.', 2, c => { if (c !== '40') return false; E.win(); return true; }, 'WARNING: wrong angle. The capsule would bounce off the air!');
}
});
