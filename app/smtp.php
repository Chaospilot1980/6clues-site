<?php
// Authenticated SMTP via websmtp.simply.com (PHP mail() is rejected by Gmail under 6clues.com's DMARC policy).
// Credentials live in data/smtp.json outside the web root, set by an admin at /admin/smtp – never in git.

function smtp_conf(): ?array {
    $f = dirname(__DIR__, 2) . '/data/smtp.json';
    if (!is_file($f)) return null;
    $c = json_decode((string)file_get_contents($f), true);
    return is_array($c) && !empty($c['user']) && !empty($c['pass']) ? $c : null;
}

/** Send one plain-text mail. $from = [email, name]. Returns true on success; last error in $GLOBALS['smtp_error']. */
function smtp_send(string $to, string $subject, string $body, array $from, array $extraHeaders = []): bool {
    $c = smtp_conf();
    if (!$c) { $GLOBALS['smtp_error'] = 'SMTP not configured'; return false; }
    $host = $c['host'] ?? 'websmtp.simply.com'; $port = (int)($c['port'] ?? 587);
    $fp = @stream_socket_client("tcp://$host:$port", $errno, $errstr, 20);
    if (!$fp) { $GLOBALS['smtp_error'] = "connect: $errstr"; return false; }
    stream_set_timeout($fp, 20);
    $read = function () use ($fp) { $d = ''; while (($l = fgets($fp, 515)) !== false) { $d .= $l; if (isset($l[3]) && $l[3] === ' ') break; } return $d; };
    $cmd = function (string $c, array $ok) use ($fp, $read) { fwrite($fp, $c . "\r\n"); $r = $read(); if (!in_array((int)substr($r, 0, 3), $ok, true)) throw new RuntimeException(trim($r)); return $r; };
    try {
        $r = $read(); if ((int)substr($r, 0, 3) !== 220) throw new RuntimeException(trim($r));
        $cmd('EHLO 6clues.com', [250]);
        $cmd('STARTTLS', [220]);
        if (!stream_socket_enable_crypto($fp, true, STREAM_CRYPTO_METHOD_TLSv1_2_CLIENT | STREAM_CRYPTO_METHOD_TLSv1_3_CLIENT)) throw new RuntimeException('TLS failed');
        $cmd('EHLO 6clues.com', [250]);
        $cmd('AUTH LOGIN', [334]); $cmd(base64_encode($c['user']), [334]); $cmd(base64_encode($c['pass']), [235]);
        $cmd('MAIL FROM:<' . $from[0] . '>', [250]);
        $cmd('RCPT TO:<' . $to . '>', [250, 251]);
        $cmd('DATA', [354]);
        $h = ['Date: ' . date('r'), 'From: ' . mb_encode_mimeheader($from[1], 'UTF-8') . ' <' . $from[0] . '>', 'To: <' . $to . '>',
              'Subject: ' . mb_encode_mimeheader($subject, 'UTF-8'), 'Message-ID: <' . bin2hex(random_bytes(12)) . '@6clues.com>',
              'MIME-Version: 1.0', 'Content-Type: text/plain; charset=UTF-8', 'Content-Transfer-Encoding: 8bit'];
        foreach ($extraHeaders as $x) $h[] = $x;
        $b = preg_replace('/\r?\n/', "\r\n", $body);
        $b = preg_replace('/^\./m', '..', $b);
        $cmd(implode("\r\n", $h) . "\r\n\r\n" . $b . "\r\n.", [250]);
        @$cmd('QUIT', [221]);
        fclose($fp); return true;
    } catch (Throwable $e) { $GLOBALS['smtp_error'] = $e->getMessage(); @fclose($fp); return false; }
}
