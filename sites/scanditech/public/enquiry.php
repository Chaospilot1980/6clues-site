<?php
// Contact form handler for scanditech.es.
// Delivery: relayed via 6clues.com authenticated SMTP (mail() from this host is not accepted by Microsoft 365).
// Every enquiry is also logged outside the web root, so nothing is lost.
$lang = (($_POST['lang'] ?? '') === 'es') ? 'es' : 'en';
$back = $lang === 'es' ? '/es/contacto/' : '/contact/';
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { header('Location: ' . $back); exit; }
$f = fn($k) => trim(str_replace(["\r", "\n"], ' ', (string)($_POST[$k] ?? '')));
if ($f('website') !== '') { header('Location: ' . $back . '?sent=1'); exit; } // honeypot
$name = mb_substr($f('name'), 0, 120); $email = $f('email'); $phone = mb_substr($f('phone'), 0, 40);
$msg = mb_substr(trim((string)($_POST['message'] ?? '')), 0, 5000);
if ($name === '' || !filter_var($email, FILTER_VALIDATE_EMAIL) || $msg === '') { header('Location: ' . $back . '?error=1'); exit; }
$rec = ['at' => gmdate('c'), 'lang' => $lang, 'name' => $name, 'email' => $email, 'phone' => $phone, 'message' => $msg, 'ip' => $_SERVER['REMOTE_ADDR'] ?? ''];
$key = trim((string)@file_get_contents(dirname(__DIR__) . '/enquiry_key.txt'));
$ok = false; $err = 'no key';
if ($key !== '') {
    $payload = json_encode(['key' => $key] + $rec, JSON_UNESCAPED_UNICODE);
    $ctx = stream_context_create(['http' => ['method' => 'POST', 'header' => "Content-Type: application/json\r\nUser-Agent: scanditech-form\r\n", 'content' => $payload, 'timeout' => 20, 'ignore_errors' => true]]);
    $res = @file_get_contents('https://6clues.com/hook/scanditech-enquiry', false, $ctx);
    $j = json_decode((string)$res, true);
    $ok = !empty($j['ok']); $err = $ok ? '' : substr((string)$res, 0, 200);
}
$rec['delivered'] = $ok; if (!$ok) $rec['error'] = $err;
@file_put_contents(dirname(__DIR__) . '/enquiries.log', json_encode($rec, JSON_UNESCAPED_UNICODE) . "\n", FILE_APPEND | LOCK_EX);
header('Location: ' . $back . '?sent=1');
