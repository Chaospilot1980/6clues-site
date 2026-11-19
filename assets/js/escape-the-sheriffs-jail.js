/* Six Clues escape room #19 – The Sheriff's Jail (level 2). Uses escape-engine.js. */
EscapeEngine(E => {
const F = () => E.F, L = E.label;
const wood = (c1, c2) => `<rect width="1600" height="900" fill="${c1}"/>${Array.from({ length: 16 }, (_, i) => `<rect x="${i * 100}" y="0" width="4" height="660" fill="${c2}"/>`).join('')}<rect y="660" width="1600" height="240" fill="#4a3220"/><ellipse cx="800" cy="0" rx="520" ry="300" fill="url(#lamp)"/>`;

return {
  start: 'cell', v: 2,
  items: {
    spoon: ['🥄', 'Tin spoon', 'A bent tin spoon from your dinner plate.'],
    belt: ['🪢', 'Leather belt', 'Your own belt.'],
    hook: ['🪝', 'Belt hook', 'Your belt with a bent spoon tied on the end – a hook!'],
    stableKey: ['🗝️', 'Stable key', 'A big iron key with a horseshoe tag.'],
    lasso: ['➰', 'Lasso', 'A coiled rope lasso.'],
    evidence: ['💰', 'Stolen gold & letter', 'The bank’s gold bag and Black Jack Lyle’s letter to his gang.'],
  },
  rooms: {
    cell: {
      name: 'The jail cell',
      bg: () => `${wood('#5a4028', '#4a3420')}${Array.from({ length: 9 }, (_, i) => `<rect x="${500 + i * 70}" y="80" width="14" height="580" fill="#2a2a2a"/>`).join('')}`,
      spots: [
        { id: 'plate', photo: [205, 745, 255, 110], x: 80, y: 520, w: 260, h: 140, art: () => `<ellipse cx="210" cy="590" rx="100" ry="30" fill="#8a8a8a"/>${L(210, 650, 'Dinner plate')}`,
          act: () => { if (F().spoon) return E.say('Cold beans. You’re not that hungry.'); F().spoon = 1; E.give('spoon'); E.give('belt'); E.say('Cold beans and a tin spoon. You take the spoon – and pull off your belt while you think.'); } },
        { id: 'keys', photo: [1470, 35, 110, 320], x: 1180, y: 160, w: 260, h: 220, art: () => `<circle cx="1310" cy="260" r="40" fill="none" stroke="#c9a24a" stroke-width="10"/>${L(1310, 360, F().out ? 'Hook (empty)' : 'Keys on a hook – out of reach')}`,
          act: () => F().out ? E.say('An empty hook.') : E.say('The sheriff’s key ring hangs on a hook across the room. Your arm through the bars is a foot too short.'),
          use: { hook: () => { F().out = 1; E.take('hook'); E.say('You swing the belt hook through the bars… snag! The key ring slides along the floor to you. Click – the cell door opens.'); return true; } } },
        { id: 'scratch', photo: [30, 90, 190, 135], x: 80, y: 120, w: 340, h: 260, art: () => `<rect x="100" y="140" width="300" height="200" fill="#6a4a2a"/>${L(250, 380, 'Scratches on the wall')}`,
          act: () => { E.note('scratch', 'Scratched into the cell wall by a past prisoner: “Sheriff Boone is honest. The judge isn’t. Find the gold and you’re free.”'); E.say('Scratched in the wall: “Sheriff Boone is honest. The judge isn’t. Find the gold and you’re free.”'); } },
        { id: 'toOffice', photo: [1205, 0, 260, 850], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit(F().out ? 'Sheriff’s office →' : 'Cell door (locked)', 1240), act: () => F().out ? E.go('office') : E.say('The cell door is locked. The keys hang across the room.') },
      ],
    },
    office: {
      name: 'The sheriff’s office',
      bg: () => wood('#6a4a2a', '#5a3e22'),
      spots: [
        { id: 'back', photo: [0, 20, 145, 780], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Cell'), act: () => E.go('cell') },
        { id: 'posters', photo: [200, 20, 340, 240], x: 100, y: 100, w: 520, h: 300, art: () => `${[0, 1, 2].map(i => `<rect x="${120 + i * 165}" y="120" width="140" height="200" fill="#e8d8a8"/>`).join('')}${L(360, 360, 'Wanted posters')}`,
          act: () => { E.note('posters', 'Wanted posters: DUSTY PETE – scar on right cheek, rides a brown mule – $300. BLACK JACK LYLE – scar on left cheek, rides a white horse – $750. MAD MOLLY FINN – no scars, rides a black horse – $500.'); E.say('Three wanted posters – Dusty Pete, Black Jack Lyle and Mad Molly Finn. You copy them into your notebook.'); } },
        { id: 'telegram', photo: [705, 100, 170, 95], x: 680, y: 120, w: 320, h: 220, art: () => `${E.paper(700, 140, 280, 160, 4)}${L(840, 340, 'Telegram')}`,
          act: () => { E.note('telegram', 'Telegram to Sheriff Boone: “BANK ROBBER SEEN BY STAGE DRIVER STOP SCAR ON LEFT CHEEK STOP WHITE HORSE STOP REWARD IS THE CODE YOU SET STOP – MARSHAL”'); E.say('“BANK ROBBER SEEN: SCAR ON LEFT CHEEK. WHITE HORSE. REWARD IS THE CODE YOU SET.”'); } },
        { id: 'desk', photo: [435, 460, 690, 340], x: 600, y: 420, w: 440, h: 220, art: () => `<rect x="620" y="470" width="400" height="30" fill="#4a2e1a"/><rect x="640" y="500" width="360" height="120" fill="#3a2414"/>${L(820, 650, F().desk ? 'Desk (open)' : 'Sheriff’s desk (3-number lock)')}`, act: () => openDesk() },
        { id: 'judge', photo: [1200, 95, 100, 160], x: 1100, y: 120, w: 340, h: 240, art: () => `${E.paper(1120, 140, 300, 180, 5)}${L(1270, 360, 'Judge’s letter')}`,
          act: () => { E.note('judge', 'Letter from Judge Hartley: “Hang the stranger at noon. No trial. And send me my share of the gold as agreed. – H.”'); E.say('From Judge Hartley: “Hang the stranger at noon. No trial. And send me my share of the gold as agreed.”'); } },
        { id: 'toSaloon', photo: [1395, 40, 205, 760], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit('Street – saloon →', 1240), act: () => E.go('saloon') },
      ],
    },
    saloon: {
      name: 'The Silver Spur saloon',
      bg: () => wood('#5a2e1e', '#4a2418'),
      spots: [
        { id: 'back', photo: [0, 135, 215, 625], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Sheriff’s office'), act: () => E.go('office') },
        { id: 'register', photo: [350, 340, 210, 80], x: 120, y: 380, w: 380, h: 240, art: () => `<rect x="140" y="440" width="340" height="30" fill="#4a2e1a"/>${E.paper(200, 400, 220, 60, 2)}${L(310, 520, 'Hotel register on the bar')}`,
          act: () => { E.note('register', 'Hotel register: “Room 4 – Mr J. Smith, white horse kept in stall 3. Paid in new gold coins.”'); E.say('“Room 4 – Mr J. Smith, white horse kept in stall 3. Paid in new gold coins.”'); } },
        { id: 'poker', photo: [770, 480, 390, 140], x: 560, y: 420, w: 400, h: 220, art: () => `<ellipse cx="760" cy="540" rx="180" ry="70" fill="#2a6a3a"/>${L(760, 640, 'Poker table')}`,
          act: () => E.say('An abandoned poker hand: aces and eights. A cowboy at the next table mutters: “Dead man’s hand. Bad luck.”') },
        { id: 'hat', photo: [1075, 200, 165, 160], x: 1040, y: 160, w: 280, h: 240, art: () => `<path d="M1080 340 Q1180 220 1280 340z" fill="#2a1a10"/>${L(1180, 380, 'Coat rack')}`,
          act: () => { if (F().lasso) return E.say('Dusters and hats.'); F().lasso = 1; E.give('lasso'); E.say('On the coat rack: a coiled lasso. Might come in handy.'); } },
        { id: 'piano', photo: [1345, 320, 255, 545], x: 1080, y: 420, w: 400, h: 220, art: () => `<rect x="1100" y="440" width="360" height="180" fill="#2a1a10"/>${L(1280, 650, 'Piano')}`,
          act: () => E.say('The piano player winks: “Stall 3, stranger. That fella in room 4 never takes his saddlebag off his horse.”') },
        { id: 'toStable', photo: [1240, 125, 205, 460], x: 1220, y: 740, w: 360, h: 130, art: () => E.exit(F().stable ? 'Livery stable →' : 'Livery stable (locked)', 1240), act: () => F().stable ? E.go('stable') : E.say('The livery stable doors are padlocked.'),
          use: { stableKey: () => { F().stable = 1; E.take('stableKey'); E.say('The padlock clanks open. Horses whinny inside.'); return true; } } },
      ],
    },
    stable: {
      name: 'The livery stable',
      bg: () => `${wood('#4a3220', '#3a2618')}<rect y="600" width="1600" height="300" fill="#8a7a4a"/>`,
      spots: [
        { id: 'back', photo: [0, 135, 145, 745], x: 20, y: 740, w: 300, h: 130, art: () => E.exit('← Saloon'), act: () => E.go('saloon') },
        { id: 'horse', photo: [745, 235, 280, 185], x: 500, y: 200, w: 500, h: 400, art: () => `<ellipse cx="750" cy="420" rx="200" ry="110" fill="#e8e8e8"/>${L(750, 600, 'White horse in stall 3')}`, act: () => openHorse() },
        { id: 'brand', photo: [1100, 185, 180, 110], x: 1060, y: 160, w: 300, h: 240, art: () => `<rect x="1080" y="180" width="260" height="180" fill="#6a4a2a"/>${L(1210, 400, 'Stall 3 board')}`,
          act: () => { E.note('brand', 'Board on stall 3: “White mare, brand 9-6-2, owner J. Smith.”'); E.say('“White mare, brand 9-6-2, owner J. Smith.”'); } },
        { id: 'tack', photo: [205, 135, 300, 480], x: 100, y: 160, w: 340, h: 320, art: () => `<rect x="120" y="180" width="300" height="260" fill="#5a3a20"/>${L(270, 480, 'Saddle and tack')}`,
          act: () => { E.note('tack', 'A card on the tack wall: “Saddling up, boys – blanket first, then saddle, then the cinch, bridle last.”'); E.say('A card on the tack wall: “Blanket first, then saddle, then the cinch, bridle last.”'); } },
        { id: 'door', photo: [1380, 240, 210, 310], x: 1220, y: 420, w: 340, h: 260, art: () => `<rect x="1240" y="440" width="300" height="220" fill="#3a2414"/>${L(1390, 690, 'Back gate – out of town')}`, act: () => openGate() },
      ],
    },
  },
  combine: (a, b) => { if ([a, b].sort().join() === 'belt,spoon') { E.take('belt'); E.take('spoon'); E.give('hook'); F().hook = 1; E.say('You bend the spoon into a hook and tie it to the end of your belt.'); return true; } return false; },
  stages: [
    ['hook', () => F().hook, ['The keys are out of reach.', 'You have a spoon and a belt.', 'Combine the spoon and the belt.']],
    ['out', () => F().out, ['Now you have a hook.', 'Use it on the keys across the room.', 'Use the belt hook on the keys.']],
    ['desk', () => F().desk, ['The sheriff’s desk wants three numbers.', 'The telegram describes the robber; one wanted poster matches. “Reward is the code.”', 'Black Jack Lyle – left cheek, white horse – $750: 750.']],
    ['stable', () => F().stable, ['The desk had a key with a horseshoe.', 'The livery stable is behind the saloon.', 'Use the stable key on the stable doors.']],
    ['bag', () => F().bag, ['The robber’s horse is in stall 3.', 'The saddlebag has a number padlock – look at the stall board.', 'Brand 9-6-2: 962.']],
    ['gate', () => F().won, ['You have the gold. Now ride.', 'Saddle the horse in the right order – then the back gate.', 'Blanket, Saddle, Cinch, Bridle.']],
  ],
  intro: ['Copper Creek, Arizona · 3 June 1881 · 11:00', 'The Sheriff’s Jail',
    `<p>You rode into Copper Creek yesterday – and woke up in jail. Someone robbed the bank last night, and the town says it was the stranger. You.</p><p>The circuit judge rides in at noon, and he doesn’t believe in long trials. Get out of the cell, find the real robber and the stolen gold, and ride for the marshal before the clock strikes twelve.</p><p>Level 2: not every wanted poster tells you who you’re looking for.</p>`,
    'Iron bars, a hard bunk and flies buzzing in the heat. Look around.'],
  timesUp: ['High noon.', 'Hoofbeats in the street – the judge is here. You can still finish, but off the leaderboard.'],
  win: ['Ride out!', 'You gallop out of Copper Creek on the robber’s own white mare with the gold and the letters in the saddlebag. By sunset the marshal has arrested Black Jack Lyle – and a very crooked judge.'],
};

function openDesk() {
  if (F().desk) return E.say('The desk drawer is empty now.');
  E.numLock('Sheriff’s desk', 'The drawer has three number wheels. Scratched on the brass: “Reward.”', 3, c => { if (c !== '750') return false; F().desk = 1; E.give('stableKey'); E.say('The drawer opens: the sheriff’s badge, a sandwich – and a big key with a horseshoe tag.'); return true; });
}
function openHorse() {
  if (F().bag) return E.say('The white mare nuzzles your pocket. Her saddlebag is empty.');
  E.numLock('Saddlebag padlock', 'A heavy saddlebag on the white horse with a three-number padlock.', 3, c => { if (c !== '962') return false; F().bag = 1; E.give('evidence'); E.say('Inside: the bank’s gold bag – and a letter signed Black Jack Lyle: “Split with the judge, then ride for Mexico.”'); return true; });
}
function openGate() {
  if (!E.has('evidence')) return E.say('You could run… but without proof, you’ll be a wanted man forever.');
  E.orderer('Saddle up', 'Tap the tack in the order you put it on the horse.', ['Bridle', 'Saddle', 'Blanket', 'Cinch'], v => { if (v.join() !== 'Blanket,Saddle,Cinch,Bridle') return false; E.win(); return true; }, 'The mare snorts and shakes it all off.');
}
});
