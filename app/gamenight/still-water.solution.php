<?php
// SPOILERS. Answer key and solution text for Still Water.
return [
 'culprit' => 'henrik-lund',
 'stop' => 'b',
 'lock' => 'c',
 'motive' => 'b',
 'evidence' => ['A02', 'A03', 'A06', 'B01', 'B02', 'B03', 'B04', 'C01', 'C02', 'C03', 'C04', 'C05'],
 'summary' => [
  'The saboteur is <b>Henrik Lund</b>, project manager for the new pump station. At 23:17 he collected the key fob for service computer SCADA-SVC1, and at 01:58 he opened a remote session from the company’s meeting room with his personal account HENRIK-PRJ.',
  'At 02:10 he switched on <b>TEST_LOCK</b>, which blocks the backup pump P2, and at 02:13:58 he sent a remote <b>STOP</b> to P1. With P2 locked out, nothing took over. At 02:35 he restarted P1 and closed the session at 02:42 – exactly the sequence in his handwritten note. He ignored Freja’s warning at 02:07 that basin 3 was already at 73 %.',
  'His motive: the ‘Pump 2027’ project was 11 weeks late, an audit was due the next morning, and his bonus depended on approval. At 01:42 – before anything had happened – he was already writing a slide about the plant’s ‘documented critical instability’. His claim that he was asleep at home is contradicted by the key fob, the signed log and his own note.',
 ],
 'conclusions' => [
  ['P1 stopped on a remote command, not a power failure.', 'A02, A03'],
  ['P2 was blocked by TEST_LOCK, which the approved plan ruled out.', 'A02, A04, A06'],
  ['Both commands came from HENRIK-PRJ without the required second approver.', 'B01, B02, B03'],
  ['The session is tied to Henrik’s service computer and key fob – he was not asleep at home.', 'B04, C03, B06'],
  ['He planned the sequence and wrote about the ‘failure’ before it happened.', 'C02, C04'],
  ['He was warned at 02:07 and went ahead anyway.', 'C05'],
 ],
 'timeline' => [
  ['Day before, 17:20', 'Henrik creates ticket #771 – no approver', 'B03'],
  ['23:17', 'Henrik collects the key fob for SCADA-SVC1', 'B04'],
  ['01:42', 'Henrik edits a slide about a ‘critical failure’', 'C02'],
  ['01:58', 'Remote session HENRIK-PRJ opens from the meeting room', 'B01, B04'],
  ['02:05', 'Basin 3 is at 73 %', 'C05'],
  ['02:07', 'Freja’s warning is delivered to Henrik', 'C05'],
  ['02:10', 'TEST_LOCK switched on', 'B01'],
  ['02:13:58', 'Remote STOP to P1; P2 inhibited', 'A02'],
  ['02:35', 'P1 restarted', 'A02, B01'],
  ['02:42', 'Session closed', 'B01'],
 ],
 'others' => [
  '<b>Karin</b> signed a plan with no pump stop and no TEST_LOCK, and never approved ticket #771 (A06, B03, B06).',
  '<b>Oliver</b> was at home from 22:00; he only checked the voltage logs the next morning (A03, B06).',
  '<b>Freja</b> warned against the test – she didn’t cause it (C05).',
  '<b>Asta</b> was by basin 3 and has no SCADA account (A05, B02).',
  '<b>Rune</b> was on a ferry and his account was deactivated; both pumps worked mechanically (B05, C06).',
 ],
 'fairness' => 'An account name alone could be borrowed. Here it is backed up by the key fob Henrik collected, the device certificate of his service computer, his unapproved ticket, his handwritten plan and a slide written before the incident.',
];
