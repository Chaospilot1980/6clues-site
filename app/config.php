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

    'google_client_id' => '',
    'ga4_id'        => '',

    'admin_emails'  => ['dennis.norgaard.hansen@gmail.com'],
    'company_name'  => 'Scandinavian Technical Solutions, S.L.',
    'contact_email' => 'hello@6clues.com',
    'dev_login'     => false,
];
