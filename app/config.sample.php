<?php
// Copy this file to config.php and fill in your own values.
return [
    'site_name'     => 'Six Clues',
    'tagline'       => 'Free printable murder mysteries',
    'base_url'      => 'https://www.example.com',   // no trailing slash

    // Simply.com: Control panel → Databases → MySQL. Host is usually mysqlXX.unoeuro.com
    'db_dsn'        => 'mysql:host=MYSQL_HOST;dbname=DB_NAME;charset=utf8mb4',
    'db_user'       => 'DB_USER',
    'db_pass'       => 'DB_PASSWORD',

    // Google Cloud Console → APIs & Services → Credentials → OAuth client ID (Web application)
    'google_client_id' => 'XXXXXXXX.apps.googleusercontent.com',

    // Google Analytics 4 measurement ID (G-XXXXXXX). Leave empty to disable.
    'ga4_id'        => '',

    // Google accounts that may open /admin
    'admin_emails'  => ['you@example.com'],

    // Shown in the privacy policy
    'company_name'  => '[YOUR COMPANY NAME]',
    'contact_email' => 'hello@example.com',

    // Long random string used to sign unsubscribe links
    'secret'        => 'CHANGE-ME-TO-A-LONG-RANDOM-STRING',

    // Local testing only: allows a fake login at /auth/dev. Must be false in production.
    'dev_login'     => false,
];
