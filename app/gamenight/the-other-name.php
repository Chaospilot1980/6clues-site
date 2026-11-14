<?php
// Game Night case 006: The Other Name. Server-side only. Translated and adapted from the Danish beta 'Det andet navn'.
return [
 'slug' => 'the-other-name',
 'no' => '006',
 'title' => 'The Other Name',
 'tagline' => 'She doesn’t remember who she was. Someone else does.',
 'teaser' => 'A woman with no memory was found on a ferry quay eight months ago. Now an anonymous photo arrives: YOU PROMISED TO COME BACK. Who is she – and who wants her back?',
 'genre' => 'Psychological thriller',
 'level' => 3,
 'minutes' => [100, 150],
 'players' => [2, 6],
 'revision' => '1.0',
 'caseref' => 'SUN-2026-0303',
 'stamp' => 'MISSING',
 'envelope' => '#C9B8C9', 'flap' => '#AE98AE',
 'cast' => true,
 'cover' => ['file' => 'the-other-name/cover.jpg', 'prompt' => 'Cinematic illustration of an empty ferry quay at dawn in a small Scandinavian harbour town, cold blue mist over the water, a lone woman seen from behind in a thin coat standing by a ticket machine, an old brass locker key with a stamped number tag in the foreground on wet concrete, muted blue and grey palette with a faint yellow sunrise, quiet and uneasy mood, no readable text, 4:3'],
 'intro' => [
  'At 05:42 on 3 March 2026, a confused woman is found by the ticket machine on the ferry quay in <b>Sundby</b> – no bag, no phone, no name. She slowly starts calling herself <b>Liv</b>, and Signe Birk gives her a room and work at her small guesthouse.',
  'Eight months later, in October, an anonymous envelope arrives at the guesthouse. Inside is a photo of Liv at a yellow gate with a small boy, and on the back: <b>YOU PROMISED TO COME BACK</b>. At the same time, strangers begin asking for her – and a man turns up who says he is her husband.',
  'The Birk family want to know who Liv was – and who is trying to fetch her home. <i>Mature theme · 16+: this case deals with a controlling relationship. Nothing graphic is described.</i>',
 ],
 'mission' => [
  'Find out who Liv really is, and why she was on the ferry quay.',
  'Find out who sent the photo – and on whose orders.',
  'Decide what the right next step is for Liv.',
  'Back up your conclusion with at least four document numbers.',
 ],
 'questions' => [
  'Where does key 218 really lead?',
  'Does a marriage certificate prove who Liv is – or give anyone rights over her?',
  'What had Liv planned before she lost her memory?',
  'Who could know about the yellow gate?',
  'Who paid for the photo and the postage – and why?',
  'What would Liv want to happen now?',
 ],
 'suspects' => [
  ['id' => 'liv', 'name' => 'Liv (unknown)', 'role' => 'The woman with no memory, found on the quay 3 March'],
  ['id' => 'signe-birk', 'name' => 'Signe Birk', 'role' => 'Runs the small guesthouse; took Liv in'],
  ['id' => 'jonas-birk', 'name' => 'Jonas Birk', 'role' => 'Signe’s grown-up son; thinks Liv is hiding something'],
  ['id' => 'martin-holm', 'name' => 'Martin Holm', 'role' => 'Says he is Liv’s husband'],
  ['id' => 'ada-krog', 'name' => 'Ada Krog', 'role' => 'Volunteer at the Havblik crisis centre'],
  ['id' => 'mikkel-gade', 'name' => 'Mikkel Gade', 'role' => 'Private investigator, hired by Martin'],
 ],
 'packets' => [
  'START' => ['label' => 'Start folder', 'docs' => ['S-01', 'S-02', 'S-03', 'S-04', 'S-05', 'S-06', 'S-07', 'S-08']],
  'B' => ['label' => 'Envelope B', 'when' => 'you can explain where key 218 leads – and where it doesn’t', 'docs' => ['B-01', 'B-02', 'B-03', 'B-04', 'B-05', 'B-06', 'B-07']],
  'C' => ['label' => 'Envelope C', 'when' => 'you can say what locker 218 reveals about Liv’s past', 'docs' => ['C-01', 'C-02', 'C-03', 'C-04', 'C-05', 'C-06', 'C-07']],
 ],
 'docs' => [
  'S-01' => ['kind' => 'report', 'title' => 'Ferry guard’s report', 'meta' => '3 March · 05:42', 'body' => '
    <p>A woman of about 35 is sitting by the ticket machine. No ticket, phone or luggage. She asks three times which town she is in.</p>
    <dl class="rows"><dt>On her wrist</dt><dd>A faded bluish mark</dd><dt>In her pocket</dt><dd>A key stamped with the number <b>218</b></dd><dt>Also</dt><dd>A folded bus ticket dated <b>2 March</b></dd></dl>
    <p class="note">The guard called an ambulance at 05:49. The woman was taken to the emergency department in Sundby with no name.</p>'],
  'S-02' => ['kind' => 'medical', 'title' => 'Emergency department notes', 'meta' => 'Sundby Hospital · 3 March', 'body' => '
    <p>Mild concussion and a small injury at the hairline. The cause cannot be determined – a fall on the icy quay cannot be ruled out.</p>
    <p>The patient cannot remember her name or address. She reads, counts and talks about her childhood without difficulty, but struggles to recall the last few months.</p>
    <p class="note">The doctor stresses: memory loss proves neither a lie nor a crime.</p>'],
  'S-03' => ['kind' => 'report', 'title' => 'Bus ticket – route 71', 'body' => '
    <dl class="rows"><dt>Bought</dt><dd>2 March, 21:18, at the terminal in <b>Linde</b></dd><dt>Departure</dt><dd>21:40 towards Sundby (the slow route, not the direct evening bus to the ferry)</dd><dt>Ticket no.</dt><dd>…8821</dd></dl>
    <p class="note">Linde is 70 km from Sundby. The bus arrives in Sundby at 23:55.</p>'],
  'S-04' => ['kind' => 'report', 'title' => 'The key marked 218', 'meta' => 'Statement from a locksmith', 'body' => '
    <p>The key profile is used for the luggage lockers at <b>Linde bus terminal</b>. Number 218 is a locker number, not a room number.</p>
    <p class="note">The lockers have anonymous access, but the system records the time each locker is opened, locked or tried.</p>'],
  'S-05' => ['kind' => 'photo', 'img' => ['file' => 'the-other-name/yellow-gate.jpg', 'caption' => 'The photo sent to the guesthouse', 'prompt' => 'Faded instant-camera style photograph of a woman in her thirties and a small boy in a yellow raincoat seen from behind, standing hand in hand at a painted yellow wooden garden gate set in a white fence, overcast early-spring day, bare trees, soft washed-out colours, nostalgic and slightly unsettling, faces not visible, no readable text'], 'title' => 'The photo sent to the guesthouse', 'meta' => 'Arrived at the guesthouse 20 October', 'body' => '
    {{IMG}}
    <p>An instant-camera-style copy: the woman stands at a yellow gate with a small boy. On the back, in printed capitals:</p>
    <p class="handwriting">YOU PROMISED TO COME BACK</p>
    <p class="note">The photo is printed on modern photo paper. The anonymous envelope is postmarked Linde, 19 October.</p>'],
  'S-06' => ['kind' => 'calendar', 'title' => 'Signe’s diary', 'meta' => 'Birk Guesthouse', 'body' => '
    <table class="cal"><tr><td>3 Mar</td><td>Unknown woman gets breakfast and a room (sent by the hospital’s social worker).</td></tr>
    <tr><td>6 Mar</td><td>She calls herself Liv, after a name in a book in her room.</td></tr>
    <tr><td>14 Mar</td><td>First time she asks about a boy in a yellow raincoat.</td></tr>
    <tr><td>21 Mar</td><td>Starts helping out at the guesthouse of her own free will.</td></tr>
    <tr><td>20 Oct</td><td>The envelope with the photo arrives. Liv is very upset.</td></tr></table>'],
  'S-07' => ['kind' => 'interview', 'title' => 'Martin Holm’s visit', 'meta' => 'Notes by Signe Birk, 24 October', 'body' => '
    <p>Martin shows a marriage certificate for <b>Anna Holm</b>, born 1990. He says Anna disappeared after a row, and he wants his wife home.</p>
    <p>“I won’t talk to her here. You will hand her over to me. She’s confused – she doesn’t know what’s good for her.”</p>
    <p class="note">The marriage certificate has no photo. Martin refused to leave a phone number.</p>'],
  'S-08' => ['kind' => 'interview', 'title' => 'Interview: Jonas Birk', 'meta' => 'Signe’s son · 25 October', 'body' => '
    <p>“I like Liv, but she’s hiding something. She never wants to be in photos, and she jumps every time the phone rings.”</p>
    <p>“In mid-October a man phoned twice asking if we had a woman of about 35 staying here. I said no. I’d never send her something like that photo – I didn’t even know there was a boy.”</p>'],
  'B-01' => ['kind' => 'log', 'title' => 'Locker 218 – system log', 'meta' => 'Linde bus terminal', 'body' => '
    ' . gn_t([['2 Mar · 20:56', 'Locker 218 locked with the key', 'Camera: woman in a red raincoat'], ['10 Mar · 11:12', '<b>Failed attempt</b> – wrong key', 'Camera: man in a cap'], ['24 Oct · 14:05', 'Opened with the key, with Liv’s written consent', 'Police present']], ['Time', 'Event', 'Note']) . '
    <p class="note">Faces cannot be identified on the camera. The original key has been with Liv since she was found.</p>'],
  'B-02' => ['kind' => 'report', 'title' => 'What was in locker 218', 'meta' => 'Opened 24 October with Liv’s consent', 'body' => '
    <ul class="plain"><li>A receipt from the <b>Havblik crisis centre</b>.</li><li>A child’s drawing signed <b>ELIAS</b>.</li><li>A USB stick in a sealed envelope.</li><li>A red raincoat.</li></ul>
    <p class="note">Liv recognises the drawing straight away. She does not recognise the USB stick.</p>'],
  'B-03' => ['kind' => 'report', 'title' => 'Havblik admission note', 'meta' => 'Havblik crisis centre, Linde', 'body' => '
    <dl class="rows"><dt>Client</dt><dd>A.H., arrived 27 February with her son <b>Elias, 7</b></dd><dt>Contact</dt><dd>Ada Krog</dd></dl>
    <p>On 2 March, at the client’s own request, client and child were moved to two separate temporary addresses for safety reasons. Elias is staying with an approved carer.</p>
    <p class="note">Addresses are never given out.</p>'],
  'B-04' => ['kind' => 'note', 'img' => ['file' => 'the-other-name/drawing.jpg', 'caption' => 'The drawing from locker 218', 'prompt' => 'A child’s wax-crayon drawing on slightly crumpled white paper: a big yellow gate in a fence, a tall stick figure and a small stick figure in a yellow raincoat holding hands, a blue sky with a round sun, naive childlike style, scanned flat, no readable letters'], 'title' => 'The child’s drawing', 'body' => '
    {{IMG}}
    <p>The drawing shows the same yellow gate as the photo. It is signed <b>ELIAS, 1 MARCH</b>. Beside the gate, in a child’s writing: <b>MUM AND ME</b>.</p>'],
  'B-05' => ['kind' => 'report', 'title' => 'Text file on the USB stick', 'meta' => 'readme.txt · last changed 2 March, 19:12', 'body' => '
    <p class="quote">If you are reading this, I have left Martin. I am not taking Elias back to him. Contact Ada through Havblik. I have saved the recordings here, because he always says nobody will believe me. – Anna</p>'],
  'B-06' => ['kind' => 'log', 'title' => 'Havblik phone list', 'body' => '
    ' . gn_t([['2 Mar · 20:14', 'Ada calls Anna – 4 min 12 s'], ['3 Mar · 06:08', 'Ada calls the social worker at <b>Linde</b> Hospital: “Has Anna Holm been brought in?” Answer: no'], ['10 Mar · 11:19', 'Mikkel Gade calls Havblik’s main number and asks for Anna Holm. He is told nothing.']], ['Time', 'Call']) . ''],
  'B-07' => ['kind' => 'audit', 'title' => 'Mikkel Gade’s invoice', 'meta' => 'Gade Investigations · to Martin Holm', 'body' => '
    <dl class="rows"><dt>Job</dt><dd>“Locating spouse”, from 5 March</dd><dt>Expense 10 Mar</dt><dd>Parking, Linde bus terminal, 10:49</dd><dt>Expense 18 Oct</dt><dd><b>Photo print and postage</b></dd><dt>Approved</dt><dd>19 October by M. Holm</dd></dl>'],
  'C-01' => ['kind' => 'report', 'title' => 'Recordings on the USB stick', 'meta' => 'Police summary – contents not reproduced', 'body' => '
    <p>Three sound files dated 21, 24 and 27 February.</p>
    <ul class="plain"><li><b>21 Feb:</b> A man threatens to take Elias away from his mother.</li><li><b>24 Feb:</b> Anna asks him to stay away from her.</li><li><b>27 Feb:</b> Anna says clearly that she is seeking protection.</li></ul>
    <p class="note">The material documents her fear. It is not a verdict on anyone.</p>'],
  'C-02' => ['kind' => 'report', 'title' => 'Where is the yellow gate?', 'meta' => 'Address check', 'body' => '
    <p>The yellow gate stands at Havblik’s <b>former premises</b> in Linde – not at Martin’s home. The council’s old photo of the building shows identical gate fittings.</p>
    <p class="note">The photo was taken on a visiting day at the crisis centre on 1 March, two days before Anna was found in Sundby.</p>'],
  'C-03' => ['kind' => 'interview', 'title' => 'Ada Krog’s written statement', 'meta' => '26 October', 'body' => '
    <p>“Anna had planned to leave the relationship. I helped her with a safety plan, but she took the bus on her own. Elias was placed safely somewhere else.”</p>
    <p>“When Anna didn’t answer the next morning, I called the hospital in Linde. Nobody had seen her. I never knew she had ended up in Sundby, and I didn’t know why she had lost her memory.”</p>'],
  'C-04' => ['kind' => 'report', 'title' => 'Letter from the social worker', 'meta' => 'Linde Council', 'body' => '
    <p>Anna is an adult and can decide for herself whether to contact Martin. Elias is staying with an approved carer under the temporary safety plan.</p>
    <p class="note">Any reunion between mother and child must be arranged through the social worker – not through the husband who is seeking her out.</p>'],
  'C-05' => ['kind' => 'log', 'title' => 'Photo lab order confirmation', 'meta' => 'Order 55120', 'body' => '
    ' . gn_t([['18 Oct · 11:40', 'Customer: <b>Mikkel Gade</b> · one photo print + one postage label to Birk Guesthouse, Sundby'], ['', 'Order note printed on the back: “YOU PROMISED TO COME BACK”'], ['19 Oct', 'Posted from Linde']], ['Time', 'Order']) . '
    <p class="note">The original file was taken on 1 March with Anna’s phone and stored in an old family cloud album. Mikkel received it from Martin, who still had the password.</p>'],
  'C-06' => ['kind' => 'messages', 'title' => 'Martin’s messages to Mikkel', 'meta' => 'Handed over by Mikkel Gade’s lawyer', 'body' => '
    <div class="chat"><p class="msg in"><span>18 Oct, 10:06 · Martin → Mikkel</span>She doesn’t believe she’s Anna. Make her unsure. Remind her of the boy. Don’t mention my name.</p>
    <p class="msg in"><span>19 Oct, 08:32 · Martin → Mikkel</span>She’ll come home when she’s scared enough.</p></div>'],
  'C-07' => ['kind' => 'note', 'title' => 'Liv’s note after talking it through', 'meta' => '27 October', 'body' => '
    <p class="handwriting">I remember the yellow gate now, and Elias. I don’t know if I’ll remember every day. I want to talk to Ada and the social worker. I don’t want anyone to give Martin my address. I will choose what happens now.</p>'],
 ],
 'checkpoints' => [
  'A' => ['title' => 'The key', 'prompt' => 'Liv had a key, a bus ticket and no memory. Where was she coming from – and where does key 218 lead?',
          'gate' => ['q' => 'Where does key 218 belong?', 'choices' => ['A room in Martin Holm’s house', 'A luggage locker at Linde bus terminal', 'A room at the Birk guesthouse'], 'answer' => 1,
                     'ok' => 'The key belongs to locker 218 at Linde bus terminal – the start of a journey Liv planned herself. Open envelope B.'],
          'hints' => ['A marriage certificate gives nobody the right to decide over an adult.', 'Put the bus ticket, the locksmith’s statement and the locker together.']],
  'B' => ['title' => 'The past gets an address', 'prompt' => 'What does locker 218 tell you about who Liv was – and what she had planned?',
          'gate' => ['q' => 'What does the locker show about Liv’s past?', 'choices' => ['She is Anna Holm, who planned to leave Martin and keep Elias safe', 'She was taken from the crisis centre against her will', 'She stole a stranger’s belongings and identity'], 'answer' => 0,
                     'ok' => 'The admission note, the drawing and her own text file show that Anna planned to leave and made Elias safe. Open envelope C.'],
          'hints' => ['Read the text file on the USB stick and the Havblik admission note side by side.', 'Who tried locker 218 on 10 March – and who parked at Linde terminal that morning?']],
  'final' => ['title' => 'The accusation', 'prompt' => 'Who is behind the photo, who sent it, and what should happen now?',
          'hints' => ['Who paid for the photo print and the postage – and what was the goal?', 'Read Martin’s messages and Liv’s own note. Whose choice is it?']],
 ],
 'accuse' => [
  'culprit_q' => 'Who is behind the photo meant to frighten Liv?',
  'wrong' => 'That person is not the one behind the photo.',
  'items' => ['sender' => ['The sender', 'Who ordered and posted the photo?', 4], 'past' => ['Liv’s past', 'Who is Liv – and why was she on the ferry quay?', 4], 'next' => ['The right ending', 'What is the right next step?', 3]],
 ],
 'choices' => [
  'sender' => [
   'a' => 'Jonas Birk, to make Liv leave the guesthouse.',
   'b' => 'Mikkel Gade, the private investigator, on Martin’s orders.',
   'c' => 'Ada Krog, to help Liv remember.',
   'd' => 'Liv herself, to find out who she was.',
  ],
  'past' => [
   'a' => 'A stranger who had stolen Anna Holm’s papers.',
   'b' => 'Anna Holm, who ran away from her family on a whim.',
   'c' => 'Anna Holm, who chose to leave a controlling husband, made Elias safe and hid her evidence in locker 218.',
   'd' => 'A woman running from the police after a crime.',
  ],
  'next' => [
   'a' => 'Hand her over to Martin – he has a marriage certificate.',
   'b' => 'Keep the truth from Liv so she doesn’t get upset.',
   'c' => 'Ask Jonas to go and find Elias.',
   'd' => 'Contact Ada and the social worker, keep her address secret and let Anna decide for herself.',
  ],
 ],
 'worksheet' => ['Who is Liv?', 'Why was she on the ferry quay?', 'Who ordered and sent the photo?', 'Who was behind it – and why?', 'What should happen now?'],
 'solution_title' => 'Who Liv really is',
];
