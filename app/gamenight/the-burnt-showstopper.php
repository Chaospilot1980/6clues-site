<?php
// Game Night case 016: The Burnt Showstopper. Server-side only.
return [
 'slug' => 'the-burnt-showstopper',
 'no' => '016',
 'title' => 'The Burnt Showstopper',
 'tagline' => 'Live on air, the favourite’s cake turns to charcoal. The oven was working perfectly.',
 'teaser' => 'In the live final of a TV baking contest, the favourite’s showstopper collapses in a cloud of smoke. The channel calls it bad luck. The baker says someone turned up his oven – and he is right.',
 'genre' => 'Sabotage',
 'level' => 1,
 'minutes' => [90, 120],
 'players' => [2, 6],
 'revision' => '1.0',
 'caseref' => 'BBK-2026-FINAL',
 'stamp' => 'SABOTAGE',
 'envelope' => '#F2C9B1', 'flap' => '#E0A988',
 'cast' => true,
 'cover' => ['file' => 'the-burnt-showstopper/cover.jpg', 'prompt' => 'Cinematic illustration of a TV baking contest set under bright studio lights, a row of pastel kitchen benches, one oven door open with dark smoke curling out and a collapsed blackened cake on the rack, TV cameras in silhouette, playful noir mood, warm pastel and smoky grey palette, no people, no text, 4:3'],
 'intro' => [
  'It is the live final of <b>“Britain Bakes”</b>. Three bakers, one hour, ten million viewers. At 14:40 favourite Kofi Mensah opens oven 3 – and pulls out a charred, collapsed showstopper. The studio gasps. The clip goes round the world.',
  'The channel says the oven must have been faulty. Kofi swears he set it to 160 °C. The channel’s lawyer has asked you, quietly, to find out what really happened before the press does.',
 ],
 'mission' => [
  'Find out what really happened to oven 3.',
  'Find out where the change came from.',
  'Name the saboteur – and the reason.',
  'Back up your accusation with at least four document numbers.',
 ],
 'questions' => [
  'Was the oven faulty, or was it changed?',
  'Can the ovens be controlled from anywhere but their own dial?',
  'Whose device sent the change – and where was that device?',
  'Who was where between 14:05 and 14:20?',
  'Who wanted a disaster on air?',
  'Which suspicious moments were innocent?',
 ],
 'suspects' => [
  ['id' => 'neil-harte', 'name' => 'Neil Harte', 'role' => 'Producer'],
  ['id' => 'gemma-lowe', 'name' => 'Gemma Lowe', 'role' => 'Finalist'],
  ['id' => 'ollie-park', 'name' => 'Ollie Park', 'role' => 'Finalist'],
  ['id' => 'marjorie-bell', 'name' => 'Marjorie Bell', 'role' => 'Judge'],
  ['id' => 'saskia-rowe', 'name' => 'Saskia Rowe', 'role' => 'Floor manager'],
  ['id' => 'dev-iyer', 'name' => 'Dev Iyer', 'role' => 'Oven technician'],
 ],
 'packets' => [
  'START' => ['label' => 'Start folder', 'docs' => ['A01', 'A02', 'A03', 'A04', 'A05', 'A06']],
  'B' => ['label' => 'Envelope B', 'when' => 'you can say what happened to oven 3', 'docs' => ['B01', 'B02', 'B03', 'B04', 'B05', 'B06']],
  'C' => ['label' => 'Envelope C', 'when' => 'you can say where the change was sent from', 'docs' => ['C01', 'C02', 'C03', 'C04', 'C05', 'C06']],
 ],
 'docs' => [
  'A01' => ['kind' => 'report', 'title' => 'Incident note', 'meta' => 'Studio 2 · Saturday, live final', 'body' => '
    <dl class="rows"><dt>14:00</dt><dd>Live final starts – showstopper round, 60 minutes</dd><dt>14:03</dt><dd>Kofi puts his cake in oven 3</dd><dt>14:40</dt><dd>Kofi opens oven 3 – cake <b>burnt and collapsed</b>, smoke on air</dd></dl>
    <p class="note">Kofi says he set oven 3 to 160 °C and never touched it again.</p>'],
  'A02' => ['kind' => 'log', 'title' => 'Oven 3 temperature record', 'meta' => 'Built-in data logger', 'body' => '
    ' . gn_t([['14:03', '160 °C', '160 °C'], ['14:10', '160 °C', '161 °C'], ['14:12', '<b>250 °C</b>', '163 °C'], ['14:25', '250 °C', '246 °C'], ['14:40', '250 °C', '251 °C']], ['Time', 'Set to', 'Inside']) . ''],
  'A03' => ['kind' => 'photo', 'title' => 'Floor camera stills', 'meta' => 'Camera 4, wide shot', 'img' => ['file' => 'the-burnt-showstopper/floor.jpg', 'caption' => 'Camera 4 at 14:10', 'prompt' => 'Wide shot of a bright TV baking studio with three pastel workbenches and wall ovens, a contestant reaching up to a shared ingredients shelf near the third oven, TV camera framing, playful documentary style, no readable text, 4:3'], 'body' => '
    <p><b>14:10</b> – Gemma at the shared ingredients shelf beside oven 3.</p>
    <p><b>14:15</b> – All three bakers at their own benches.</p>
    <p><b>14:30</b> – Ollie and Kofi in a heated discussion over a piping bag.</p>
    {{IMG}}'],
  'A04' => ['kind' => 'lab', 'title' => 'Oven inspection', 'meta' => 'Manufacturer’s engineer, Sunday', 'body' => '
    <p>Oven 3 was taken apart and tested for six hours. Thermostat, element, fan and dial: <b>no fault of any kind</b>.</p>
    <p class="note">The oven heated to exactly the temperature it was set to.</p>'],
  'A05' => ['kind' => 'note', 'title' => 'Kofi’s recipe card', 'meta' => 'From his bench', 'body' => '
    <p class="handwriting">Mango &amp; lime tower. Oven 160 °C, fan off, 50 min. DO NOT open door before 40 min!</p>'],
  'A06' => ['kind' => 'calendar', 'title' => 'Running order', 'meta' => 'Live final', 'body' => '
    <dl class="rows"><dt>13:55</dt><dd>Judges and bakers on the floor</dd><dt>14:00</dt><dd>Live: showstopper round</dd><dt>14:00–14:25</dt><dd>Technician’s break (ovens are not touched during the round)</dd><dt>15:00</dt><dd>Judging and winner</dd></dl>
    <p class="note">The producer runs the show from the gallery (control room) above the studio.</p>'],
  'B01' => ['kind' => 'log', 'title' => 'Oven control log', 'meta' => 'Studio oven network', 'body' => '
    ' . gn_t([['14:03', 'Oven 1', 'Dial on oven'], ['14:03', 'Oven 3', 'Dial on oven – 160 °C'], ['14:12', 'Oven 3', 'Studio app, device <b>TECH-2</b> – 250 °C'], ['14:41', 'Oven 3', 'Dial on oven – OFF']], ['Time', 'Oven', 'Changed by']) . '
    <p class="note">The studio ovens can be set from their own dial or from the technicians’ tablets.</p>'],
  'B02' => ['kind' => 'list', 'title' => 'Equipment register', 'meta' => 'Technical department', 'body' => '
    ' . gn_t([['TECH-1', 'Tablet', 'Locked in the tech store'], ['TECH-2', 'Tablet', 'Dev Iyer – left charging on the gallery desk during his break'], ['CAM-4', 'Camera', 'Studio floor']], ['Device', 'Type', 'Where, Saturday 14:00–14:25']) . ''],
  'B03' => ['kind' => 'interview', 'title' => 'The technician', 'meta' => 'Dev Iyer', 'body' => '
    <p>“I put my tablet on charge in the gallery at two o’clock and went to the canteen with the sound team. Nobody touches the ovens during the round – that’s the rule.”</p>
    <p class="note">Canteen till: Dev and two sound engineers, 14:02–14:26.</p>'],
  'B04' => ['kind' => 'log', 'title' => 'Gallery door log', 'meta' => 'Control room above Studio 2', 'body' => '
    ' . gn_t([['14:01', 'D. Iyer', 'In'], ['14:02', 'D. Iyer', 'Out'], ['14:04', 'N. Harte', 'In'], ['14:21', 'N. Harte', 'Out'], ['14:22', 'N. Harte', 'In']], ['Time', 'Card', 'Door']) . '
    <p class="note">The vision mixer works from a desk in the studio corner during live shows.</p>'],
  'B05' => ['kind' => 'interview', 'title' => 'The floor manager', 'meta' => 'Saskia Rowe', 'body' => '
    <p>“I was on the studio floor with my headset the whole round, cueing the cameras. Neil was in my ear from the gallery all through the first twenty minutes.”</p>
    <p class="note">Talkback log: Saskia on channel 1, studio floor, 14:00–15:00.</p>'],
  'B06' => ['kind' => 'interview', 'title' => 'The finalist by the shelf', 'meta' => 'Gemma Lowe', 'body' => '
    <p>“I went to the shared shelf for icing sugar at ten past two – it happens to be next to oven 3. I never touched any dial. Ask camera 4.”</p>
    <p class="note">Camera 4 zoomed shot, 14:10: Gemma’s hands on a bag of icing sugar; the oven 3 dial is in view and does not move.</p>'],
  'C01' => ['kind' => 'messages', 'title' => 'Producer’s messages', 'meta' => 'Neil Harte’s phone, Friday', 'body' => '
    <div class="chat"><p class="msg in"><span>Fri 18:20 · Channel boss</span>Final needs big numbers or the series is gone, Neil.</p><p class="msg out"><span>Fri 18:24 · Neil</span>Leave it with me. Tears and smoke – a proper disaster moment. Live TV gold.</p></div>'],
  'C02' => ['kind' => 'audit', 'title' => 'Series renewal memo', 'meta' => 'Channel controller', 'body' => '
    <p>“Britain Bakes” will be renewed only if the final reaches <b>8 million viewers</b>. The producer’s contract runs out with the series.</p>
    <p class="note">Overnight figures: 10.4 million – after the “burnt showstopper” clip went viral at 14:41.</p>'],
  'C03' => ['kind' => 'interview', 'title' => 'The judge', 'meta' => 'Marjorie Bell', 'body' => '
    <p>“I have a cookery book coming out, and yes, Kofi once called my scones ‘dry’ on air. But I sat at the judges’ table in full view of three cameras for the whole round.”</p>'],
  'C04' => ['kind' => 'interview', 'title' => 'The other finalist', 'meta' => 'Ollie Park', 'body' => '
    <p>“Kofi and I argued over a piping bag at half past two – heat of the moment. I was at my own bench the whole hour, you can see me in every shot.”</p>
    <p class="note">Camera 2 follows Ollie’s bench continuously from 14:00 to 14:40.</p>'],
  'C05' => ['kind' => 'report', 'title' => 'Studio app audit', 'meta' => 'IT department', 'body' => '
    <p>Command at 14:12 on TECH-2: the tablet’s PIN is <b>written on a label on its back</b> (“so the technicians can share it”). The tablet was on the gallery Wi-Fi throughout.</p>
    <p class="note">The gallery Wi-Fi only reaches the control room itself.</p>'],
  'C06' => ['kind' => 'interview', 'title' => 'The producer’s statement', 'meta' => 'Neil Harte', 'body' => '
    <p>“A terrible accident. I was down on the studio floor with Saskia for the whole first half of the round, watching the bakers. I didn’t even know the ovens could be changed from a tablet.”</p>'],
 ],
 'checkpoints' => [
  'A' => ['title' => 'The oven', 'prompt' => 'What really happened to oven 3 – was it faulty, or was it changed?',
          'gate' => ['q' => 'What burnt the cake?', 'choices' => ['A faulty oven', 'The temperature was turned up to 250 °C', 'The wrong recipe'], 'answer' => 1,
                     'ok' => 'The oven worked perfectly – somebody changed it from 160 °C to 250 °C at 14:12. Open envelope B.'],
          'hints' => ['Compare what the oven was set to with what the engineer found.', 'A02 shows the setting jump at 14:12; A04 shows there was no fault.']],
  'B' => ['title' => 'The device', 'prompt' => 'Where did the change at 14:12 come from?',
          'gate' => ['q' => 'Where was the command sent from?', 'choices' => ['Oven 3’s own dial', 'Dev’s tablet, charging in the gallery', 'Gemma’s phone'], 'answer' => 1,
                     'ok' => 'TECH-2 sent the change – and TECH-2 was on the gallery desk while Dev was in the canteen. Open envelope C.'],
          'hints' => ['The oven control log names a device.', 'B01 names TECH-2; B02 says where it was; B03 says where Dev was.']],
  'final' => ['title' => 'The accusation', 'prompt' => 'Who turned up oven 3, and why?',
          'hints' => ['Who was in the gallery at 14:12?', 'B04 and C05 put the tablet and one person in the gallery; C01 and C02 give the reason.']],
 ],
 'accuse' => [
  'culprit_q' => 'Who sabotaged Kofi’s showstopper?',
  'wrong' => 'That’s not the person who turned up the oven.',
  'items' => ['what' => ['The method', 'What happened to oven 3?', 4], 'where' => ['The device', 'How was it done?', 4], 'motive' => ['The motive', 'Why was it done?', 3]],
 ],
 'choices' => [
  'what' => [
   'a' => 'The thermostat broke.',
   'b' => 'The oven was turned up from 160 °C to 250 °C at 14:12.',
   'c' => 'Kofi used the wrong recipe.',
   'd' => 'The oven door was opened too early.',
  ],
  'where' => [
   'a' => 'Someone turned the dial while passing the oven.',
   'b' => 'With Dev’s tablet TECH-2, from the gallery, using the PIN on its back.',
   'c' => 'From a phone on the studio floor.',
   'd' => 'From the tech store.',
  ],
  'motive' => [
   'a' => 'To win the final.',
   'b' => 'To create a “disaster moment” so the series would hit its viewing target and be renewed.',
   'c' => 'Revenge for a remark about scones.',
   'd' => 'To get the oven company sued.',
  ],
 ],
 'worksheet' => ['Who did it?', 'What happened to oven 3?', 'How was it done?', 'Why?', 'Which details were red herrings?'],
 'solution_title' => 'What really happened in Studio 2',
];
