<?php
// Six Clues – live configuration for 6clues.com
return [
    'site_name'     => 'Six Clues',
    'tagline'       => 'Free printable murder mysteries',
    'base_url'      => 'https://6clues.com',

    // SQLite database stored outside the web folder (no password needed)
    'db_dsn'        => 'sqlite:' . dirname(__DIR__, 2) . '/data/sixclues.db',
    'db_user'       => '',
    'db_pass'       => '',

    'google_client_id' => '736923593611-189rfahj1dg1um5akauojlt24e81bblb.apps.googleusercontent.com',
    'ga4_id'        => 'G-7SQE61N1HB',

    'admin_emails'  => ['dennis.norgaard.hansen@gmail.com'],
    'company_name'  => 'Scandinavian Technical Solutions, S.L.',
    'contact_email' => 'hello@6clues.com',
    'dev_login'     => false,
];
