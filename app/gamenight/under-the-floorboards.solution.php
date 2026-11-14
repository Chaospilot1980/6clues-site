<?php
// SPOILERS. Answer key and solution text for Under the Floorboards. Only loaded server-side to score an accusation or after the reveal.
return [
 'culprit' => 'peter-asmussen',
 'poa' => 'b',
 'signatures' => 'c',
 'eva' => 'a',
 'evidence' => ['S-05', 'S-06', 'B-01', 'B-02', 'B-03', 'B-04', 'B-05', 'B-06', 'B-07', 'C-04', 'C-06'],
 'summary' => [
  'This case has two truths. The first is about the family: Eva Lund was not Ruth’s birth daughter and was never adopted. She came to the house as a <b>foster child</b> in the summer of 1979, aged 12, and Ruth loved her as her own. Ruth’s will leaves the property to her three children and a personal legacy of 50,000 kr. to Eva.',
  'The second truth is the crime. The heirs only ever allowed <b>Peter Asmussen</b> to negotiate on plot 14a. On 28 May he wrote that “BR-772 can do all three signatures from my office”. The next morning, between 10:14 and 10:17, all three “heirs” signed a supplementary power of attorney for plot 14b on his office browser – while Ida was in the air, Klara was at the dentist and Mads was delivering goods. A week after promising Mads to wait, he sold 14b.',
  'The buyer, Strandblik Invest, belongs mainly to his brother’s company – a connection he never disclosed – and 40,000 kr. of the price vanished as an un-invoiced “consultancy fee”. Whether the papers are legally void is for the courts, but the grounds for suspicion all point to Peter.',
 ],
 'conclusions' => [
  ['The family never allowed the sale of 14b, and the original power of attorney only covers 14a.', 'S-05, S-06'],
  ['All three supplementary signatures were made within three minutes on browser BR-772 – Peter’s office PC.', 'B-01, B-03, B-04'],
  ['Ida was on a plane, Klara at the dentist and Mads on a delivery at the time.', 'B-02, C-06'],
  ['Peter planned the signatures in advance and broke his promise to wait.', 'B-07, C-04'],
  ['The buyer is linked to his brother, and 40,000 kr. disappeared without an invoice.', 'B-05, B-06'],
  ['Eva was Ruth’s foster child, not an heir, and is left a personal legacy.', 'C-01, C-02'],
 ],
 'timeline' => [
  ['Summer 1979', 'Eva, 12, is placed with Ruth’s family as a foster child', 'C-01, S-03'],
  ['1998', 'Ruth writes “Eva was my child too”', 'S-02'],
  ['1 May', 'Family meeting: sell 14a, look into keeping 14b', 'S-05'],
  ['10 May', 'Power of attorney for plot 14a only', 'S-06'],
  ['20–21 May', 'Mads objects; Peter promises to wait', 'B-07'],
  ['28 May', 'Peter’s draft: “BR-772 can do all three signatures”', 'C-04'],
  ['29 May · 10:10', 'Ida’s plane takes off from Madrid', 'B-02'],
  ['29 May · 10:14–10:17', 'Three signatures on BR-772 in Peter’s office', 'B-01, B-03, B-04'],
  ['3 June', 'Plot 14b sold to Strandblik Invest for 620,000 kr.', 'S-01'],
  ['After the sale', 'Only 580,000 kr. reaches the estate', 'B-05'],
 ],
 'others' => [
  '<b>Klara</b> handled the estate, but was at the dentist in Stege 10:00–10:40 when “her” signature was made in Peter’s office (C-06, B-03).',
  '<b>Mads</b> objected to selling 14b and was on a delivery at 10:15 (B-07, C-06).',
  '<b>Ida</b> was in the air from 10:10 to 13:22 with her phone off (B-02).',
  '<b>Eva</b> asked Peter to leave 14b alone and gains nothing from the sale (C-03).',
  '<b>Jens</b> owns the buyer, but was chairing a board meeting in Aarhus from 09:00 to 12:00, and the signatures came from Peter’s own PC (B-06, B-04).',
 ],
 'fairness' => 'A timestamp alone doesn’t prove who signed, and no calendar is perfect proof. The case rests on several independent things together: the limited power of attorney, one browser for three “signers”, Peter’s own draft, the alibis, and the money trail.',
];
