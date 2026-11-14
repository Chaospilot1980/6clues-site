# Six Clues – opsætning på Simply.com

## Det skal du have klar
1. **MySQL-database** – Simply kontrolpanel → Databaser → opret MySQL. Notér host, databasenavn, bruger og adgangskode.
2. **Google-login (OAuth client ID)** – console.cloud.google.com → APIs & Services:
   - *OAuth consent screen*: External, appnavn "Six Clues", support-mail, link til `https://DITDOMÆNE/privacy`. Scopes: email, profile, openid. Publish app.
   - *Credentials → Create credentials → OAuth client ID → Web application*.
     Authorized JavaScript origins: `https://DITDOMÆNE` (og `https://www.DITDOMÆNE` hvis du bruger www).
   - Kopiér Client ID (slutter på `.apps.googleusercontent.com`).
3. **Google Analytics 4** – analytics.google.com → Admin → opret property → Web stream for dit domæne → kopiér Measurement ID (`G-XXXXXXX`).

## Installation
1. Upload **hele indholdet** af denne mappe til `public_html` (FTP, f.eks. FileZilla, eller Simplys filhåndtering). Husk de skjulte `.htaccess`-filer.
2. Kopiér `app/config.sample.php` til `app/config.php` og udfyld:
   `base_url`, `db_dsn` (`mysql:host=…;dbname=…;charset=utf8mb4`), `db_user`, `db_pass`, `google_client_id`, `ga4_id`, `admin_emails` (din Google-mail), `company_name`, `contact_email`.
3. Åbn sitet. Databasetabellerne oprettes automatisk ved første besøg.
4. Log ind med den Google-konto, du har skrevet i `admin_emails`, og gå til `/admin`.

## SEO-tjekliste efter lancering
- Google Search Console → tilføj domænet → indsend `https://DITDOMÆNE/sitemap.xml`.
- Del forsiden og et mysterie på Facebook/LinkedIn for at teste delingsbilledet.

## Nyhedsbrev
Kun brugere, der selv har sat flueben, kommer på listen. Hent den som CSV under `/admin` og importér i f.eks. Mailchimp eller Brevo.

## Nye mysterier
Mysterierne ligger i `app/mysteries.php` (genereres automatisk). Bed Claude om et nyt mysterie, så opdateres filen – upload den igen.
