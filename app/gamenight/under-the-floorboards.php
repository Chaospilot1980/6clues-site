<?php
// Game Night case 010: Under the Floorboards. Server-side only. Translated and adapted from the Danish beta 'Arven under gulvet'.
return [
 'slug' => 'under-the-floorboards',
 'no' => '010',
 'title' => 'Under the Floorboards',
 'tagline' => 'An old letter turns up just as the family home is about to be sold.',
 'teaser' => 'Three siblings clearing their late mother’s house find a tin box under the floor – and discover that the family’s orchard was sold while none of them were there.',
 'genre' => 'Forgery',
 'level' => 2,
 'minutes' => [100, 150],
 'players' => [2, 6],
 'revision' => '1.0',
 'caseref' => 'MOEN-2026-0603',
 'stamp' => 'FORGED',
 'envelope' => '#D2B48C', 'flap' => '#B8976A',
 'cast' => true,
 'cover' => ['file' => 'under-the-floorboards/cover.jpg', 'prompt' => 'Cinematic illustration inside an old Danish country farmhouse with whitewashed walls, late summer afternoon light through a small window, two wide wooden floorboards lifted to reveal a dented old tin box with faded paint, an envelope and a curled black-and-white photograph peeking out, an apple orchard visible through the window, warm amber and dusty green palette, nostalgic mystery mood, no people, no readable text, 4:3'],
 'intro' => [
  'In August 2026, three siblings meet at their childhood home on the island of <b>Moen</b> to get it ready for sale after their mother, <b>Ruth Vester</b>, has died.',
  'Under a loose floorboard they find a tin box: a baptism certificate, an old letter and a photo of a girl nobody can quite place. At the same time they discover that the family’s most precious piece of land – the old orchard, plot <b>14b</b> – was sold on paper in June, while none of them were there.',
  'Did the inheritance disappear lawfully – or has someone close to the family forged its history?',
 ],
 'mission' => [
  'Find out who arranged the sale of plot 14b – and how.',
  'Find out what the original power of attorney actually allowed.',
  'Find out the truth about Eva and Ruth.',
  'Back up your conclusion with at least four document numbers.',
 ],
 'questions' => [
  'What is the difference between plot 14a and plot 14b in the papers?',
  'Who gave permission for what – and when?',
  'Can a signature with a timestamp prove who was at the keyboard?',
  'Where was each heir on the morning of 29 May?',
  'Where did the money go?',
  'What did Ruth mean by “Eva was my child too”?',
 ],
 'suspects' => [
  ['id' => 'klara-vester', 'name' => 'Klara Vester', 'role' => 'Eldest daughter; has handled the estate'],
  ['id' => 'mads-vester', 'name' => 'Mads Vester', 'role' => 'Middle son; wants to keep the orchard'],
  ['id' => 'ida-vester', 'name' => 'Ida Vester', 'role' => 'Youngest daughter; lives abroad'],
  ['id' => 'eva-lund', 'name' => 'Eva Lund', 'role' => 'Ruth’s old friend; grew up in the house'],
  ['id' => 'peter-asmussen', 'name' => 'Peter Asmussen', 'role' => 'The family’s estate agent, acting for the heirs'],
  ['id' => 'jens-asmussen', 'name' => 'Jens Asmussen', 'role' => 'Peter’s brother; majority owner behind the buyer'],
 ],
 'packets' => [
  'START' => ['label' => 'Start folder', 'docs' => ['S-01', 'S-02', 'S-03', 'S-04', 'S-05', 'S-06', 'S-07']],
  'B' => ['label' => 'Envelope B', 'when' => 'you can say exactly what the original power of attorney covered', 'docs' => ['B-01', 'B-02', 'B-03', 'B-04', 'B-05', 'B-06', 'B-07']],
  'C' => ['label' => 'Envelope C', 'when' => 'you can say where the three supplementary signatures were really made', 'docs' => ['C-01', 'C-02', 'C-03', 'C-04', 'C-05', 'C-06', 'C-07']],
 ],
 'docs' => [
  'S-01' => ['kind' => 'report', 'title' => 'Land registry summary', 'meta' => 'Plot 14b, Moen', 'body' => '
    <dl class="rows"><dt>Plot</dt><dd><b>14b</b> – the old orchard</dd><dt>Sold</dt><dd>3 June 2026</dd><dt>Price</dt><dd>620,000 kr.</dd><dt>Buyer</dt><dd>Strandblik Invest ApS</dd><dt>Signed</dt><dd>“On behalf of the heirs” by <b>Peter Asmussen</b></dd></dl>'],
  'S-02' => ['kind' => 'note', 'img' => ['file' => 'under-the-floorboards/tin-box.jpg', 'caption' => 'The tin box under the floor', 'prompt' => 'Close-up photo of a dented vintage tin biscuit box with faded floral paint lying between lifted wooden floorboards, lid half open showing a folded yellowed letter, an old certificate and a small black-and-white photo, dust in the light, warm natural light, realistic, no readable text'], 'title' => 'Ruth’s letter in the tin box', 'meta' => 'Dated 1998', 'body' => '
    {{IMG}}
    <p class="handwriting">The day you read this, you must know that Eva was my child too, though not in the way anyone thought. I could not bring the truth out while my father was alive. Don’t let the papers take her place.</p>'],
  'S-03' => ['kind' => 'photo', 'img' => ['file' => 'under-the-floorboards/photo-1979.jpg', 'caption' => 'Photo from 1979, found in the tin box', 'prompt' => 'Faded 1970s colour snapshot with rounded corners and a white border: a young woman in a summer dress and an older woman in an apron standing in front of a whitewashed thatched farmhouse, a girl with long plaits seen from behind running towards them, apple trees, warm washed-out Kodachrome tones, slight blur, no readable text'], 'title' => 'An old photograph', 'meta' => 'Found in the tin box', 'body' => '
    {{IMG}}
    <p>Ruth, a girl with plaits and an older woman in front of the house. On the back:</p>
    <p class="handwriting">Eva, 12 – the summer we brought her home</p>
    <p class="note">The photo shows a close bond. It proves neither adoption nor a blood relationship.</p>'],
  'S-04' => ['kind' => 'report', 'title' => 'Baptism certificate', 'meta' => 'Found in the tin box', 'body' => '
    <dl class="rows"><dt>Name</dt><dd>Eva Lund</dd><dt>Born</dt><dd>1967</dd><dt>Parents</dt><dd>Two other named birth parents – <b>not Ruth</b></dd></dl>
    <p class="note">So what did Ruth mean by “my child too”?</p>'],
  'S-05' => ['kind' => 'report', 'title' => 'Minutes of the family meeting', 'meta' => '1 May', 'body' => '
    <p>Present: Klara, Mads and Ida (Ida by video).</p>
    <ul class="plain"><li>The main house on plot 14a is to be sold.</li><li>We will look into whether the orchard, plot 14b, can be kept separate.</li></ul>
    <p class="note">Nobody gave explicit permission to sell 14b.</p>'],
  'S-06' => ['kind' => 'report', 'title' => 'Power of attorney for Peter Asmussen', 'meta' => 'Signed 10 May', 'body' => '
    <p class="quote">The undersigned heirs authorise estate agent Peter Asmussen to obtain offers and negotiate on our behalf concerning <b>the property on plot 14a</b>.</p>
    <p>Signed on paper by Klara Vester, Mads Vester and Ida Vester.</p>
    <p class="note">The document does not mention plot 14b anywhere.</p>'],
  'S-07' => ['kind' => 'report', 'title' => 'The estate agent’s advert', 'meta' => 'Asmussen Property · published 15 May', 'body' => '
    <p class="quote">Charming farmhouse on Moen with a view over the old orchard – which may be available as an optional extra.</p>
    <p class="note">Mads objected to the wording on 20 May.</p>'],
  'B-01' => ['kind' => 'report', 'title' => 'Supplementary power of attorney', 'meta' => 'Dated 29 May', 'body' => '
    <p class="quote">The heirs also authorise Peter Asmussen to <b>sell plot 14b</b> on their behalf.</p>
    ' . gn_t([['Klara Vester', '29 May · 10:14'], ['Mads Vester', '29 May · 10:15'], ['Ida Vester', '29 May · 10:17']], ['Digital signature', 'Timestamp']) . '
    <p class="note">Peter Asmussen: “All three signed digitally, each on their own device. I only did what I was asked.”</p>'],
  'B-02' => ['kind' => 'report', 'title' => 'Ida’s flight', 'meta' => 'Boarding pass and airline confirmation', 'body' => '
    <dl class="rows"><dt>Date</dt><dd>29 May</dd><dt>Route</dt><dd>Madrid → Copenhagen</dd><dt>Airborne</dt><dd><b>10:10–13:22</b></dd></dl>
    <p class="note">Ida: “My phone was switched off on the plane. I never signed anything about the orchard.”</p>'],
  'B-03' => ['kind' => 'log', 'title' => 'Digital signing audit', 'meta' => 'Signing provider’s audit trail', 'body' => '
    ' . gn_t([['10:14', 'Klara Vester', 'Browser <b>BR-772</b>', '192.168.8.14'], ['10:15', 'Mads Vester', 'Browser <b>BR-772</b>', '192.168.8.14'], ['10:17', 'Ida Vester', 'Browser <b>BR-772</b>', '192.168.8.14']], ['Time', 'Signer', 'Device', 'Local IP']) . '
    <p class="note">A signature isn’t automatically invalid because it was made on one computer – but this audit does not show three independent devices.</p>'],
  'B-04' => ['kind' => 'list', 'title' => 'Peter’s office equipment', 'meta' => 'Asmussen Property · IT list', 'body' => '
    <dl class="rows"><dt>Office PC</dt><dd>Browser ID <b>BR-772</b></dd><dt>User account</dt><dd>PTASMUSSEN</dd><dt>Office network</dt><dd>192.168.8.0–255</dd></dl>
    <p class="note">The PC is in Peter’s private office.</p>'],
  'B-05' => ['kind' => 'audit', 'title' => 'Payment voucher', 'meta' => 'Sale of plot 14b', 'body' => '
    ' . gn_t([['Purchase price paid in', '620,000 kr.', 'Client account managed by Peter Asmussen'], ['Paid on to the estate', '580,000 kr.', ''], ['Difference', '<b>40,000 kr.</b>', '“Consultancy fee” – no invoice']], ['Item', 'Amount', 'Note']) . ''],
  'B-06' => ['kind' => 'report', 'title' => 'Strandblik Invest ApS', 'meta' => 'Public company register', 'body' => '
    <p>Strandblik Invest is owned by a holding company in which <b>Jens Asmussen</b>, Peter’s brother, holds 60 per cent.</p>
    <p>Peter never told the heirs about this connection.</p>
    <p class="note">Minutes: Jens Asmussen chaired a board meeting in Aarhus on 29 May from 09:00 to 12:00 (signed by four board members).</p>'],
  'B-07' => ['kind' => 'messages', 'title' => 'Mads’s objection', 'meta' => 'Emails, May', 'body' => '
    <div class="chat"><p class="msg out"><span>20 May · Mads → Peter</span>Plot 14b must not be sold until we have gone through Eva’s letter.</p>
    <p class="msg in"><span>21 May · Peter → Mads</span>Understood – I will wait for your decision.</p></div>'],
  'C-01' => ['kind' => 'report', 'title' => 'The council’s old foster care record', 'meta' => 'Moen Council archive', 'body' => '
    <p>Eva Lund was placed as a <b>foster child</b> with Ruth’s family in the summer of 1979, aged 12. The placement continued after she turned 18.</p>
    <p class="note">There is no adoption order. The record names Ruth as “main carer”.</p>'],
  'C-02' => ['kind' => 'report', 'title' => 'Ruth’s will', 'meta' => 'Valid will', 'body' => '
    <p>Ruth leaves the property jointly to her three legal children, Klara, Mads and Ida.</p>
    <p>She leaves <b>50,000 kr.</b> to Eva Lund as a personal legacy.</p>
    <p class="note">The will does not make Eva an heir in the same way as the children, but it recognises their bond.</p>'],
  'C-03' => ['kind' => 'note', 'title' => 'Eva’s reply', 'meta' => 'Letter to the siblings', 'body' => '
    <p class="handwriting">I never wanted to take anything from you. Ruth was the mother I actually had. I kept her letter because she wanted to tell you herself. I asked Peter to leave 14b alone until you had read it.</p>'],
  'C-04' => ['kind' => 'note', 'title' => 'Peter’s internal draft', 'meta' => 'Recovered from PTASMUSSEN, 28 May', 'body' => '
    <p class="quote">If 14b is to go with 14a, the supplementary power of attorney must be in place now. BR-772 can do all three signatures from my office. They won’t notice before registration.</p>'],
  'C-05' => ['kind' => 'report', 'title' => 'The lawyer’s note', 'meta' => 'Lawyer for the estate', 'body' => '
    <p>The material raises serious questions about whether the supplementary power of attorney is genuine, about a conflict of interest and about the settlement.</p>
    <p class="note">Whether it is legally invalid must be decided in the proper way. Your job is to identify the grounds for suspicion, not to act as a court.</p>'],
  'C-06' => ['kind' => 'calendar', 'title' => 'The siblings’ calendars', 'meta' => '29 May', 'body' => '
    <table class="cal"><tr><td>10:00–10:40</td><td><b>Klara:</b> dentist in Stege (receipt 10:42)</td></tr>
    <tr><td>10:15</td><td><b>Mads:</b> delivering goods to a customer in Nykobing (signed delivery note)</td></tr>
    <tr><td>10:10–13:22</td><td><b>Ida:</b> on the plane from Madrid</td></tr></table>
    <p class="note">None of these alone is final proof of identity – but together with BR-772 they point strongly away from the siblings.</p>'],
  'C-07' => ['kind' => 'note', 'title' => 'Letter about the orchard', 'meta' => 'Ruth, 2004', 'body' => '
    <p class="handwriting">14b was the place Eva always went when she was sad. Keep it if you can, whoever’s name is on the deeds.</p>
    <p class="note">The letter expresses a wish, not a legal instruction.</p>'],
 ],
 'checkpoints' => [
  'A' => ['title' => 'Two plots', 'prompt' => 'The orchard was sold “on behalf of the heirs”. But what had the heirs actually allowed?',
          'gate' => ['q' => 'What does the power of attorney of 10 May cover?', 'choices' => ['Both plot 14a and plot 14b', 'Only plot 14a – offers and negotiation', 'Only plot 14b'], 'answer' => 1,
                     'ok' => 'The original power of attorney never mentions 14b. So how did Peter get the right to sell it? Open envelope B.'],
          'hints' => ['There are two different secrets in this case: the family relationship and the sale.', 'Compare the family meeting (S-05) with the power of attorney (S-06).']],
  'B' => ['title' => 'Three signatures in three minutes', 'prompt' => 'The supplementary power of attorney carries three digital signatures. Who was really at the keyboard?',
          'gate' => ['q' => 'Where were all three supplementary signatures made?', 'choices' => ['On three different phones', 'On one browser, BR-772, in Peter’s office', 'At the land registry office'], 'answer' => 1,
                     'ok' => 'All three came from Peter’s office PC – while Ida was in the air. Open envelope C.'],
          'hints' => ['A timestamped signature is not the same as a verified person at the keyboard.', 'Put the signing audit (B-03) next to Peter’s equipment list (B-04) and Ida’s flight (B-02).']],
  'final' => ['title' => 'The accusation', 'prompt' => 'Who forged the sale of the orchard, how – and what is the truth about Eva?',
          'hints' => ['Follow the plot numbers, the browser ID and the money.', 'Read the foster care record and Ruth’s will together.']],
 ],
 'accuse' => [
  'culprit_q' => 'Who forged the sale of plot 14b?',
  'wrong' => 'That person didn’t forge the sale.',
  'items' => ['poa' => ['The original permission', 'What did the power of attorney of 10 May cover?', 4], 'signatures' => ['The signatures', 'How were the supplementary signatures made?', 4], 'eva' => ['The truth about Eva', 'Who was Eva to Ruth?', 3]],
 ],
 'choices' => [
  'poa' => [
   'a' => 'The sale of the whole estate, both plots.',
   'b' => 'Only offers and negotiation for plot 14a.',
   'c' => 'Only the sale of plot 14b.',
   'd' => 'Nothing – it was never signed.',
  ],
  'signatures' => [
   'a' => 'Each heir signed on their own phone.',
   'b' => 'Klara signed for her brother and sister.',
   'c' => 'All three within three minutes on Peter’s office browser BR-772 – while Ida was on a plane.',
   'd' => 'The buyer forged them on paper.',
  ],
  'eva' => [
   'a' => 'Her foster child from 1979 – never adopted, but loved as family, and left a personal legacy of 50,000 kr.',
   'b' => 'Ruth’s secret birth daughter, entitled to an equal share.',
   'c' => 'A stranger who invented the story to claim the orchard.',
   'd' => 'Adopted by Ruth in 1998.',
  ],
 ],
 'worksheet' => ['What did the original power of attorney cover?', 'Who made the supplementary signatures – and where?', 'Where did the money go?', 'Who forged the sale – and why?', 'What is the truth about Eva?'],
 'solution_title' => 'What really happened to the orchard',
];
