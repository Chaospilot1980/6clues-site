<?php
// Game Night case 008: The House Without a Name. Server-side only. Translated and adapted from the Danish beta 'Huset uden navn'.
return [
 'slug' => 'the-house-without-a-name',
 'no' => '008',
 'title' => 'The House Without a Name',
 'tagline' => 'For eight years they were an ordinary family. Then the postcard came.',
 'teaser' => 'A family living under protected new names receives an unsigned postcard of their old home: WE KNOW YOUR REAL NAMES. Who found them – and what do they want?',
 'genre' => 'Intimidation',
 'level' => 1,
 'minutes' => [110, 160],
 'players' => [2, 6],
 'revision' => '1.0',
 'caseref' => 'LAN-2026-0209',
 'stamp' => 'CONFIDENTIAL',
 'envelope' => '#C9B0A0', 'flap' => '#AE927F',
 'cast' => true,
 'cover' => ['file' => 'the-house-without-a-name/cover.jpg', 'prompt' => 'Cinematic illustration of a quiet white house by a windswept North Jutland coast at dusk, a single postcard sticking out of a red letterbox at the gate, dune grass bending in the wind, cold blue and warm window-light palette, tense but calm mood, no people, no readable text, 4:3'],
 'intro' => [
  'The Elgaard family lives quietly in a house near a small coastal town in North Jutland. In February 2026 an unsigned postcard arrives. The picture shows the house they lived in eight years ago, in another city, under other names. On the back: <b>“WE KNOW YOUR REAL NAMES. FRIDAY.”</b>',
  'The family lives under a protected address scheme. They may not contact their old circle, and their teenage daughter doesn’t know the whole story. Hidden in a folder of seemingly ordinary documents is the explanation of how the family was found – and who is behind it.',
 ],
 'mission' => [
  'Find out how the family’s protected identity was discovered.',
  'Find out who sent the postcard and the messages.',
  'Explain why – what did the sender want?',
  'Back up your accusation with at least four document numbers.',
 ],
 'questions' => [
  'Who has access to both the old and the new names?',
  'Can a dramatic photo tell you who sent a card?',
  'Which small numbers appear in more than one document?',
  'Who looks like a threat – and is there evidence linking them to this?',
  'Who would gain if the family were frightened?',
  'Who did what, when – and why?',
 ],
 'suspects' => [
  ['id' => 'maja-elgaard', 'name' => 'Maja Elgaard', 'role' => 'Mother, previously known by another name'],
  ['id' => 'thomas-elgaard', 'name' => 'Thomas Elgaard', 'role' => 'Father, keeps an encrypted backup'],
  ['id' => 'freja-elgaard', 'name' => 'Freja Elgaard', 'role' => 'Daughter, 17, researching her family’s past'],
  ['id' => 'niels-vang', 'name' => 'Niels Vang', 'role' => 'The family’s former security contact'],
  ['id' => 'camilla-roed', 'name' => 'Camilla Roed', 'role' => 'Local journalist interested in property records'],
  ['id' => 'jorgen-sahl', 'name' => 'Jorgen Sahl', 'role' => 'Former business contact the family testified against'],
 ],
 'packets' => [
  'START' => ['label' => 'Start folder', 'docs' => ['S01', 'S02', 'S03', 'S04', 'S05', 'S06', 'S07']],
  'B' => ['label' => 'Envelope B', 'when' => 'you agree who could connect the family’s old names to their new address', 'docs' => ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07']],
  'C' => ['label' => 'Envelope C', 'when' => 'you can tie the postcard to a sender without guessing from a photo', 'docs' => ['C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07']],
 ],
 'docs' => [
  'S01' => ['kind' => 'photo', 'title' => 'The postcard', 'meta' => 'Received 10 February', 'img' => ['file' => 'the-house-without-a-name/postcard.jpg', 'caption' => 'Front of the postcard: the family’s former home', 'prompt' => 'Picture postcard printed photo of an ordinary red-brick Danish terraced townhouse on a quiet city street in summer, slightly faded colours, white postcard border, a tiny faint blue printed number on the top edge, nostalgic and slightly unsettling, no readable text'], 'body' => '
    {{IMG}}
    <dl class="rows"><dt>Front</dt><dd>The house in Odense where the family lived eight years ago</dd><dt>Back</dt><dd>“WE KNOW YOUR REAL NAMES. FRIDAY.”</dd><dt>Postmark</dt><dd>Aalborg, 9 February</dd><dt>Top edge</dt><dd>An almost invisible blue control number: <b>614</b></dd></dl>'],
  'S02' => ['kind' => 'report', 'title' => 'The family’s new papers', 'meta' => 'Summary', 'body' => '
    <p>The names Maja, Thomas and Freja Elgaard were set up in 2018 as part of a <b>protected address scheme</b>. They are fully legal registrations in the new names.</p>
    <p class="note">Case numbers and old identities are not available to local authorities.</p>'],
  'S03' => ['kind' => 'note', 'title' => 'Freja’s diary', 'meta' => 'Extract', 'body' => '
    <p class="handwriting">I’ve been looking for my first school, but Dad says I mustn’t. I know we lived in Odense. On 7 Feb I got a message from a profile I didn’t know: “Can you remember what you were called before?” I didn’t answer.</p>'],
  'S04' => ['kind' => 'report', 'title' => 'Camilla’s draft article', 'meta' => 'Local newspaper', 'body' => '
    <p>Camilla is writing a local story about empty holiday homes. She has taken a photo of the Elgaards’ carport from the public road.</p>
    <p class="note">The draft mentions no family members and no old names.</p>'],
  'S05' => ['kind' => 'report', 'title' => 'Security agreement, 2018', 'meta' => 'Extract', 'body' => '
    <p class="quote">“Only the central contact function may know the link between the protected identity and the physical address. Contact must go through a personal case number. Changes to the address history require two independent approvals.”</p>'],
  'S06' => ['kind' => 'log', 'title' => 'Timeline, 7–10 February', 'meta' => 'Phone and post', 'body' => '
    ' . gn_t([['7 Feb', 'Freja receives a message from an anonymous account'], ['9 Feb', 'The card is postmarked in Aalborg'], ['10 Feb', 'Thomas phones Niels Vang, who answers: “Don’t overreact.”']], ['Date', 'Event']) . '
    <p class="note">Thomas thinks Niels sounded unusually calm.</p>'],
  'S07' => ['kind' => 'messages', 'title' => 'Message from Niels Vang', 'meta' => '10 February', 'body' => '
    <p>Niels says he <b>no longer has access</b> to the family’s location. He was their contact person from 2018 to 2022 and now works privately as an emergency-preparedness consultant.</p>
    <p class="note">He suggests meeting Thomas alone.</p>'],
  'B01' => ['kind' => 'log', 'title' => 'Log of protected lookups', 'meta' => 'Protection system audit', 'body' => '
    ' . gn_t([['6 Feb, 14:11', 'Historic case file opened · service account <b>KV-14</b> · field ‘new address’ displayed · terminal <b>NV-04</b> · reason: ‘archive check’']], ['Time', 'Event']) . ''],
  'B02' => ['kind' => 'report', 'title' => 'Service account access', 'meta' => 'Account KV-14', 'body' => '
    <p>KV-14 was created for three former contact persons. Niels Vang kept access to a transition system as an external consultant <b>until 28 February</b>.</p>
    <p class="note">The two other users were closed in December.</p>'],
  'B03' => ['kind' => 'report', 'title' => 'Terminal NV-04', 'meta' => 'Device register', 'body' => '
    <p>NV-04 is a managed laptop belonging to Niels Vang’s firm, <b>NV Beredskab ApS</b>. It was logged on to the firm’s network on 6 February from 13:58 to 14:25.</p>
    <p class="note">No other employee had a company account on the machine.</p>'],
  'B04' => ['kind' => 'audit', 'title' => 'Postcard printer’s order slip', 'meta' => 'Online print service', 'body' => '
    <dl class="rows"><dt>Order</dt><dd><b>614</b> – one postcard</dd><dt>Image uploaded</dt><dd>8 February, 18:32</dd><dt>Deliver to</dt><dd>The Elgaards’ postal address</dd><dt>Paid by</dt><dd><b>NV Beredskab ApS</b></dd><dt>Dispatched</dt><dd>To the Aalborg sorting centre, 9 February</dd></dl>'],
  'B05' => ['kind' => 'report', 'title' => 'Old case names', 'meta' => 'Background', 'body' => '
    <p>The historic protection case was known internally as <b>LANTERN</b>. The family were witnesses against <b>Jorgen Sahl</b> in a financial fraud case that ended in 2019.</p>
    <p class="note">No court records contain the family’s new address.</p>'],
  'B06' => ['kind' => 'messages', 'title' => 'Message to Freja', 'meta' => 'Anonymous account', 'body' => '
    <div class="chat"><p class="msg in"><span>7 Feb · unknown account → Freja</span>What were you called before, F?</p></div>
    <p>The account was created on 5 February. The contact email used to register it belongs to the <b>NV Beredskab</b> domain.</p>
    <p class="note">That is a technical link to the firm – not proof of which person typed the message.</p>'],
  'B07' => ['kind' => 'report', 'title' => 'Camilla’s research list', 'meta' => 'Her notes', 'body' => '
    <p>Camilla found the family through a public property sale – but not their former names. Her photo of the carport is dated <b>11 February</b>, two days after the postcard was postmarked.</p>
    <p class="note">Her photo shows the family’s current carport. The postcard shows their old house in Odense, which she never researched.</p>'],
  'C01' => ['kind' => 'messages', 'title' => 'Niels Vang’s price offer', 'meta' => 'Document from NV-04', 'body' => '
    <p class="quote">“Extended private security package after suspicious incidents: 145,000 kr. to start. A quick decision is recommended.”</p>
    <p class="note">The file was created on <b>8 February at 18:50</b> – the day before the card was postmarked – and sent to Thomas on 10 February, after his phone call.</p>'],
  'C02' => ['kind' => 'audit', 'title' => 'Niels Vang’s finances', 'meta' => 'NV Beredskab ApS', 'body' => '
    <p>The firm has two large overdue supplier invoices. On 1 February Niels applied for credit with the note <b>“expected large private client”</b>.</p>
    <p class="note">The credit was refused.</p>'],
  'C03' => ['kind' => 'report', 'title' => 'Jorgen Sahl’s whereabouts', 'meta' => 'Supervision notes', 'body' => '
    <p>Jorgen still has reason to be angry with the family. But official supervision notes show he was <b>abroad from 5 to 12 February</b>.</p>
    <p class="note">He could have used a go-between, but there is no documented link between him and the postcard order.</p>'],
  'C04' => ['kind' => 'note', 'title' => 'Draft email on NV-04', 'meta' => '6 February, 14:18 · recovered from the firm’s sync', 'body' => '
    <p class="quote">“If they think Sahl has found them, Thomas will pay for the protection. Nobody needs to be physically threatened.”</p>'],
  'C05' => ['kind' => 'audit', 'title' => 'Credit note and invoice', 'meta' => '12 February', 'body' => '
    <p>A credit note cancels a draft invoice for 145,000 kr., because Thomas will not buy the package.</p>
    <p class="note">After this, the anonymous account never writes again.</p>'],
  'C06' => ['kind' => 'report', 'title' => 'Letter from the central protection unit', 'meta' => 'Official reply', 'body' => '
    <p>The central authority confirms an <b>unauthorised lookup</b>. Niels Vang is suspended from system access, and the family’s location is being reviewed.</p>
    <p class="note">The need for protection is assessed by the authority. The family should not try to track anyone down themselves.</p>'],
  'C07' => ['kind' => 'note', 'title' => 'Thomas’s closing note', 'meta' => 'Written afterwards', 'body' => '
    <p class="handwriting">We thought our past had caught up with us. It made us vulnerable – but it was someone we had trusted who used our fear. We will tell Freja the truth in our own time.</p>'],
 ],
 'checkpoints' => [
  'A' => ['title' => 'Who could know?', 'prompt' => 'The family’s old and new names are kept apart on purpose. Who could ever connect them?',
          'gate' => ['q' => 'According to the 2018 security agreement, who may know the link between the protected identity and the address?', 'choices' => ['Anyone at the local council', 'Only the central contact function', 'Anyone who finds the property sale'], 'answer' => 1,
                     'ok' => 'Only the contact function – so whoever found the family had access to the protection system, or was given it. Open envelope B.'],
          'hints' => ['Who has access to both the old and the new names?', 'Read the security agreement (S05) next to Niels’s message (S07).']],
  'B' => ['title' => 'The breach', 'prompt' => 'Which trace shows the old identity was looked up – and who can be tied to the postcard?',
          'gate' => ['q' => 'What ties the postcard to a paying customer?', 'choices' => ['Control number 614, which matches order 614 paid by NV Beredskab', 'Camilla’s photo of the carport', 'The Aalborg postmark on its own'], 'answer' => 0,
                     'ok' => 'The tiny blue 614 on the card is the print order – and NV Beredskab paid for it. Open envelope C.'],
          'hints' => ['Small control numbers can be worth more than dramatic photos.', 'Compare the blue number on the card (S01) with the order slip (B04), and the lookup (B01) with the terminal (B03).']],
  'final' => ['title' => 'The accusation', 'prompt' => 'Who was behind the threat, how did they find the family – and why?',
          'hints' => ['Read the date on the security offer against the postmark.', 'Who would earn money if the family were frightened?']],
 ],
 'accuse' => [
  'culprit_q' => 'Who was behind the postcard?',
  'wrong' => 'That’s not the person who frightened the family.',
  'items' => ['lookup' => ['The breach', 'How was the family’s protected address found?', 4], 'card' => ['The postcard', 'What ties the postcard to its sender?', 4], 'motive' => ['The motive', 'Why was the family frightened?', 3]],
 ],
 'choices' => [
  'lookup' => [
   'a' => 'From Camilla’s photo of the carport.',
   'b' => 'Through a lookup on service account KV-14 from terminal NV-04 on 6 February.',
   'c' => 'Freja gave it away by searching for her old school.',
   'd' => 'From the public court records of the 2019 fraud case.',
  ],
  'card' => [
   'a' => 'The photo of the old house on the front.',
   'b' => 'The Aalborg postmark.',
   'c' => 'Control number 614, matching a print order paid by NV Beredskab ApS.',
   'd' => 'The handwriting on the back.',
  ],
  'motive' => [
   'a' => 'Revenge for testifying in the fraud case.',
   'b' => 'To sell the family a 145,000 kr. security package.',
   'c' => 'To get a story for the local newspaper.',
   'd' => 'To make the family move away from the town.',
  ],
 ],
 'worksheet' => ['Who was behind the postcard?', 'How was the protected address found?', 'What ties the card to its sender?', 'Why was the family frightened?', 'Which details were red herrings?'],
 'solution_title' => 'Who really found the house without a name',
];
