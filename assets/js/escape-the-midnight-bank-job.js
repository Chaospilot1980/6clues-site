/* Six Clues escape room #30 – The Midnight Bank Job (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const marble = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 6 }, (_, i) => `<rect x="${i * 300 + 60}" y="60" width="60" height="600" fill="${c2}"/>`).join('')}<rect y="660" width="1600" height="240" fill="#2a2a2a"/><ellipse cx="800" cy="0" rx="520" ry="300" fill="url(#lamp)"/>`;
const WIRES = ['Red', 'Green', 'Yellow', 'White'];
const HOURS = ['00', '06', '09', '12'];

return {
  start: 'lobby', v: 2,
  items: {
    deskKey: ['🗝️', 'Desk key', 'A small brass key from a plant pot.'],
    basementKey: ['🗝️', 'Basement key', 'An iron key tagged BASEMENT.'],
    fuse: ['🔌', 'Fuse', 'A ceramic fuse marked ALARM.'],
    vaultCard: ['💳', 'Time lock card', 'The manager’s card for the vault time lock.'],
  },
  rooms: {
    lobby: {
      name: 'The banking hall',
      bg: () => marble('#3a3a40', '#4a4a52'),
      spots: [
        { id: 'plaque', photo: [67, 53, 180, 187], x: 80, y: 100, w: 340, h: 200, art: () => `<rect x="100" y="120" width="300" height="140" fill="#c9a24a"/>${L(250, 290, 'Bronze plaque')}`,
          act: () => { E.note('plaque', 'Bronze plaque: “The Hudson Merchants’ Bank – founded 1889.”'); E.say('“The Hudson Merchants’ Bank – founded 1889.”'); } },
        { id: 'plant', photo: [0, 290, 187, 550], x: 80, y: 400, w: 260, h: 240, art: () => `<rect x="140" y="520" width="140" height="100" fill="#6a3a20"/><circle cx="210" cy="480" r="60" fill="#3a7a3a"/>${L(210, 640, 'Potted palm')}`,
          act: () => { if (F().deskKey) return E.say('Just soil.'); F().deskKey = 1; E.give('deskKey'); E.say('Buried in the soil of the palm: a small brass key. The manager’s hiding place!'); } },
        { id: 'alarm', photo: [800, 140, 100, 100], x: 520, y: 120, w: 340, h: 300, art: () => `<rect x="540" y="140" width="300" height="240" fill="#5a2a2a"/><circle cx="690" cy="220" r="40" fill="#c9a24a"/>${L(690, 410, F().alarm ? 'Alarm (ARMED)' : 'Alarm bell panel')}`, act: () => openAlarm(),
          use: { fuse: () => { F().fuseIn = 1; E.take('fuse'); E.say('The fuse clicks in. The alarm panel lights up: ENTER CODE.'); return true; } } },
        { id: 'phone', photo: [1413, 487, 187, 367], x: 920, y: 380, w: 300, h: 260, art: () => `<rect x="940" y="460" width="260" height="140" fill="#3a2a1a"/><rect x="1000" y="420" width="140" height="40" fill="#111"/>${L(1070, 640, F().phone ? 'Telephone (connected)' : 'Telephone (dead)')}`, act: () => openPhone() },
        { id: 'toOffice', photo: [160, 307, 133, 420], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Manager’s office'), act: () => E.go('office') },
        { id: 'toBasement', photo: [720, 587, 267, 213], x: 620, y: 740, w: 340, h: 130, art: () => E.exit(F().basement ? 'Basement ↓' : 'Basement (locked)', 640), act: () => F().basement ? E.go('basement') : E.say('The basement door is locked. From below: a faint scraping noise.'),
          use: { basementKey: () => { F().basement = 1; E.take('basementKey'); E.say('The basement door opens. The scraping noise is louder now – digging.'); return true; } } },
        { id: 'toVault', photo: [1213, 307, 240, 267], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Vault corridor →', 1240), act: () => E.go('vault') },
      ],
    },
    office: {
      name: 'The manager’s office',
      bg: () => marble('#3a2a20', '#46342a'),
      spots: [
        { id: 'back', photo: [1400, 53, 200, 760], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Banking hall →', 1240), act: () => E.go('lobby') },
        { id: 'desk', photo: [0, 507, 840, 393], x: 100, y: 380, w: 460, h: 260, art: () => `<rect x="120" y="440" width="420" height="30" fill="#5a3a20"/><rect x="140" y="470" width="380" height="140" fill="#4a2e1a"/>${L(330, 650, F().desk ? 'Desk (open)' : 'Manager’s desk (locked)')}`,
          act: () => F().desk ? E.say('The drawer is empty now.') : E.say('The manager’s desk drawer is locked.'),
          use: { deskKey: () => { F().desk = 1; E.take('deskKey'); E.give('basementKey'); E.give('vaultCard'); E.say('The drawer opens: a basement key and the manager’s time lock card.'); return true; } } },
        { id: 'memo', photo: [840, 160, 93, 127], x: 640, y: 120, w: 360, h: 280, art: () => `${E.paper(660, 140, 320, 220, 7)}${L(820, 400, 'Manager’s memo')}`,
          act: () => { E.note('memo', 'Manager’s memo to the night watchman: “Alarm code = the year the bank was founded. In an emergency, set the vault time lock to stay shut until 09 hours – it cannot be opened before then by anyone. The phone line is fixed by the colours on the diagram in the basement.”'); E.say('Memo: alarm code = the bank’s founding year. Set the vault time lock to 09 hours in an emergency. Phone wires: diagram in the basement.'); } },
        { id: 'safe', photo: [1107, 353, 193, 307], x: 1080, y: 160, w: 380, h: 340, art: () => `<rect x="1100" y="180" width="340" height="280" fill="#2a2a2a"/>${L(1270, 500, 'Small safe')}`,
          act: () => E.say('A small safe for petty cash. It isn’t what the robbers want – they’re after the gold in the main vault.') },
      ],
    },
    basement: {
      name: 'The basement',
      bg: () => `<rect width="1600" height="900" fill="#2a261e"/><rect y="660" width="1600" height="240" fill="#1e1a14"/>${Array.from({ length: 6 }, (_, i) => `<rect x="0" y="${i * 110}" width="1600" height="4" fill="#1a160e"/>`).join('')}`,
      spots: [
        { id: 'up', photo: [0, 267, 293, 633], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('↑ Banking hall'), act: () => E.go('lobby') },
        { id: 'wall', photo: [1333, 107, 267, 667], x: 1000, y: 200, w: 500, h: 440, art: () => `<rect x="1020" y="220" width="460" height="400" fill="#3a3028"/><path d="M1200 400 l40 -30 l30 50 l-50 20z" fill="#111"/>${L(1250, 650, 'Cracking wall')}`,
          act: () => E.say('Scrape, scrape, THUD. The wall is cracking – someone is tunnelling in from the street next door! You can hear voices: “Half an hour and we’re in the vault, boys.”') },
        { id: 'fusebox', photo: [173, 167, 280, 287], x: 100, y: 160, w: 360, h: 320, art: () => `<rect x="120" y="180" width="320" height="260" fill="#5a5a50"/>${L(280, 480, 'Fuse box')}`,
          act: () => { if (F().fuse) return E.say('Fuses in a row. The spare box is empty now.'); F().fuse = 1; E.give('fuse'); E.say('The ALARM fuse has been pulled out – the robbers’ inside man! But in the spare box there’s another one marked ALARM.'); } },
        { id: 'diagram', photo: [573, 140, 413, 287], x: 520, y: 140, w: 400, h: 300, art: () => `${E.paper(540, 160, 360, 240, 5)}${L(720, 440, 'Telephone wiring diagram')}`,
          act: () => { E.note('wires', 'Telephone wiring diagram: “Line to the street exchange: terminal 1 – Red, terminal 2 – Yellow, terminal 3 – Green. (White is earth, never on a terminal.)”'); E.say('“Terminal 1 – Red, terminal 2 – Yellow, terminal 3 – Green. White is earth, never on a terminal.”'); } },
      ],
    },
    vault: {
      name: 'The vault corridor',
      bg: () => marble('#2a2e34', '#363a42'),
      spots: [
        { id: 'back', photo: [0, 120, 173, 467], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Banking hall'), act: () => E.go('lobby') },
        { id: 'door', photo: [460, 53, 840, 733], x: 520, y: 100, w: 560, h: 540, art: () => `<circle cx="800" cy="370" r="250" fill="#5a5a5a" stroke="#888" stroke-width="20"/><circle cx="800" cy="370" r="60" fill="#c9a24a"/>${L(800, 650, F().locked ? 'Vault door (TIME-LOCKED)' : 'Vault door')}`, act: () => openTimeLock() },
        { id: 'clock', photo: [1313, 40, 253, 233], x: 1180, y: 120, w: 280, h: 280, art: () => `<circle cx="1320" cy="260" r="110" fill="#e8dcb8"/>${L(1320, 400, 'Corridor clock')}`,
          act: () => E.say('Twenty to one in the morning. The robbers said “half an hour”.') },
      ],
    },
  },
  combine: () => false,
  stages: [
    ['deskKey', () => F().deskKey, ['The manager hides his desk key somewhere in the banking hall.', 'Plants make good hiding places.', 'Search the potted palm.']],
    ['desk', () => F().desk, ['You have the desk key.', 'The manager’s office.', 'Use the desk key on the manager’s desk.']],
    ['locked', () => F().locked, ['Stop the robbers getting into the vault.', 'The memo says what to set the time lock to.', 'Use the time lock card on the vault door and set 09.']],
    ['basement', () => F().basement, ['The basement is locked.', 'The desk had a basement key.', 'Use the basement key on the basement door.']],
    ['alarm', () => F().alarm, ['The alarm is dead – someone pulled its fuse.', 'There is a spare fuse in the basement fuse box. Then the code.', 'Put the fuse in the alarm panel, then 1889.']],
    ['phone', () => F().won, ['Now call the police.', 'The phone wires: the diagram in the basement.', 'Red, Yellow, Green – then the police come.']],
  ],
  intro: ['New York · 14 March 1935 · 00:30', 'The Midnight Bank Job',
    `<p>You are the night watchman at the Hudson Merchants’ Bank. Tonight, everything has gone wrong: the alarm is dead, the phone is cut – and from somewhere below, you can hear digging.</p><p>A gang is tunnelling into the vault, and they’ll be through in about an hour. Lock the vault, get the alarm working and call the police before the gold is gone.</p><p>Level 2: someone inside the bank has helped the robbers.</p>`,
    'Marble floors, brass lamps and a scraping sound from below. Look around.'],
  timesUp: ['They’re through!', 'Voices in the vault corridor… you can still finish, but off the leaderboard.'],
  win: ['Police! Hands up!', 'The alarm bell rings out over the street, the phone gets through, and within minutes the bank is surrounded. The gang crawls out of their tunnel straight into the arms of the police – and the vault never opened. The bank gives you a gold watch.'],
};

function openAlarm() {
  if (F().alarm) return E.say('The alarm panel glows green: ARMED.');
  if (!F().fuseIn) return E.say('The alarm panel is dead. Behind a little door: an empty fuse slot.');
  E.numLock('Alarm panel', 'Four number wheels: ENTER CODE.', 4, c => { if (c !== '1889') return false; F().alarm = 1; E.say('ARMED. The alarm panel glows green.'); return true; });
}
function openTimeLock() {
  if (F().locked) return E.say('The vault time lock is set: no one can open it before 09:00.');
  if (!E.has('vaultCard')) return E.say('A huge round vault door with a time lock. A card slot glows next to it.');
  E.cycler('Vault time lock', 'Insert the manager’s card. Set the hour the vault may next open.', [{ name: 'Hour', opts: HOURS }], v => { if (v[0] !== '09') return false; F().locked = 1; E.take('vaultCard'); E.say('Clunk – the bolts shoot home. The vault will not open again before nine o’clock in the morning, whatever happens.'); return true; }, 'That would open the vault too soon!', 'Set the lock');
}
function openPhone() {
  if (!F().locked || !F().alarm) return E.say('The telephone is dead – its wires are pulled out at the back. First make sure the vault and the alarm are safe.');
  E.cycler('Telephone wires', 'Four loose wires and three terminals.', ['Terminal 1', 'Terminal 2', 'Terminal 3'].map(n => ({ name: n, opts: WIRES })), v => { if (v.join() !== 'Red,Yellow,Green') return false; F().phone = 1; E.win(); return true; }, 'Crackle – nothing.', 'Lift the receiver');
}
});
