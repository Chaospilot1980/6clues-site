<?php
// Contact form handler for scanditech.es
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { header('Location: /contact/'); exit; }
$f = fn($k) => trim(str_replace(["\r", "\n"], ' ', (string)($_POST[$k] ?? '')));
if ($f('website') !== '') { header('Location: /contact/?sent=1'); exit; } // honeypot
$name = mb_substr($f('name'), 0, 120); $email = $f('email'); $phone = mb_substr($f('phone'), 0, 40);
$msg = mb_substr(trim((string)($_POST['message'] ?? '')), 0, 5000);
if ($name === '' || !filter_var($email, FILTER_VALIDATE_EMAIL) || $msg === '') { header('Location: ' . (($_POST['lang'] ?? '') === 'es' ? '/es/contacto/' : '/contact/') . '?error=1'); exit; }
$body = "Name: $name\nEmail: $email\nPhone: " . ($phone ?: '-') . "\n\nAbout the project:\n$msg\n\n-- Sent from scanditech.es (" . ($_SERVER['REMOTE_ADDR'] ?? '') . ")\n";
$headers = "From: Scanditech website <noreply@scanditech.es>\r\nReply-To: $email\r\nContent-Type: text/plain; charset=UTF-8";
@mail('dnh@scanditech.es', '=?UTF-8?B?' . base64_encode('Website enquiry - ' . $name) . '?=', $body, $headers, '-fnoreply@scanditech.es');
header('Location: ' . (($_POST['lang'] ?? '') === 'es' ? '/es/contacto/' : '/contact/') . '?sent=1');
