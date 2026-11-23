#!/usr/bin/env python3
"""Static site generator for scanditech.es -> sites/scanditech/public/"""
import json, os, html, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'public')
SITE = 'https://scanditech.es'
TODAY = datetime.date.today().isoformat()
WA = 'https://wa.me/4520903050'
TEL = 'tel:+34608266620'
MAIL = 'dnh@scanditech.es'
CSSV = '3'
e = html.escape

# ---------------------------------------------------------------- data
SERVICES = [
  dict(slug='knx-design-programming', title='KNX Design & Programming', h1='KNX design and programming in Marbella',
       meta='KNX system design, ETS programming and commissioning for villas in Marbella and the Costa del Sol. Bus topology, panel design and full as-built documentation.',
       short='System architecture, ETS programming, commissioning and full documentation.',
       long="We take the architect's plans and produce the bus topology, panel layout, load schedule and ETS project behind them — then commission on site and hand over a documented system, not a black box. New builds and staged renovations alike.",
       tags=['ETS6', 'Panel design', 'As-built documentation', 'Commissioning'],
       body=[
         ('What KNX design actually covers', [
           "A KNX installation is only as good as the design behind it. Before a single cable is pulled we work out what every room needs to do, which circuits are switched or dimmed, where the sensors and keypads go, and how the bus is divided into lines and areas so the system can grow without being rebuilt.",
           "The result is a design package your electrician can price and build against: bus topology, panel layout, actuator and load schedule, device list and a fixed scope. No guesswork on site, and no surprises in the budget."]),
         ('ETS programming and commissioning', [
           "We programme the system in ETS6, the official KNX engineering tool, and commission it on site ourselves. Scenes, timers, presence logic, astro functions and the links between lighting, shading and climate are tuned in the house, at the times of day they are actually used — not left at factory defaults.",
           "The person who designed your system is the person who commissions it. That is the main reason our installations behave the way the owners expect them to."]),
         ('Documentation you own', [
           "Every project is handed over with the ETS project file, as-built drawings and a plain-language guide for the household. If you ever change installer, the next engineer can pick it up in an afternoon. That is the point of an open standard, and we take it seriously."]),
         ('Taking over existing KNX systems', [
           "Many villas on the Costa del Sol have KNX installations that were never documented, or whose installer has disappeared. We can audit an existing system, recover or rebuild the ETS project, fix what does not work and document it properly."]),
       ],
       faq=[('Do you work with my electrician?', 'Yes. We usually deliver the design and programming while a local electrician does the cabling and board installation to our drawings. We can also recommend electricians we have worked with.'),
            ('Can you take over a KNX system someone else installed?', 'Yes. We audit the installation, recover the ETS project where possible, and document everything so the system can be maintained by anyone qualified.'),
            ('Is KNX only for new builds?', 'No. KNX works well in renovations, and wireless KNX RF or line-by-line upgrades make staged projects possible.')]),
  dict(slug='lighting-control', title='Lighting Control', h1='Lighting control and scene design for Marbella villas',
       meta='KNX and DALI lighting control for villas in Marbella: dimming, tunable white, presence and astro control, and lighting scenes designed on site after dark.',
       short='Scenes, dimming and tunable white that flatter the architecture instead of fighting it.',
       long='Circuit planning with the electrician, dimming curves matched to the actual fittings, and scene design done on site after dark — because a lighting scene that was set in a spreadsheet always looks like it. DALI gateways where the fittings call for it.',
       tags=['DALI', 'Dimming & tunable white', 'Scene design', 'Astro & presence'],
       body=[
         ('Light that suits the house', [
           "Good lighting control is mostly invisible: the corridor lights up softly when you walk through it at night, the terrace comes on at dusk, and one button at the door switches the whole house to 'away'. We plan circuits together with the lighting designer and electrician so the control matches the fittings, not the other way round.",
           "Dimming curves are matched to the actual drivers and lamps, so LEDs dim smoothly without flicker or sudden jumps at the bottom of the range."]),
         ('Scenes set on site, after dark', [
           "We design scenes in the house at the time they will be used — evening, dinner, cinema, night — and adjust them with the household. Tunable white can follow the time of day, warm in the evening and cooler at midday."]),
         ('KNX, DALI and presence control', [
           "KNX handles switching, dimming and logic; DALI gateways are used where the fittings call for individual addressing. Presence and daylight sensors switch light where nobody remembers to, which matters in garages, utility rooms, guest wings and outdoor areas."]),
       ],
       faq=[('Can I keep normal light switches?', 'Yes. KNX keypads from Tense or Basalte replace ordinary switches and can look like simple push buttons — just with scenes behind them.'),
            ('What is the difference between KNX and DALI?', 'KNX is the building-wide control bus. DALI is a lighting-specific protocol for addressing individual fittings. We use DALI gateways on the KNX bus where the lighting design benefits from it.')]),
  dict(slug='climate-hvac-control', title='Climate & HVAC', h1='Climate and HVAC control with KNX',
       meta='Room-by-room KNX climate control for villas on the Costa del Sol: underfloor heating, fancoils, ventilation, holiday modes and shading-aware cooling.',
       short='Zone-by-zone heating, cooling and ventilation, coordinated with shading.',
       long='Per-room setpoints, underfloor and fancoil control, and logic that closes the blinds before the air conditioning has to fight the sun. Guest-wing and holiday-mode profiles so an empty house costs nothing to keep.',
       tags=['Zoned setpoints', 'Underfloor & fancoil', 'Holiday profiles', 'Humidity'],
       body=[
         ('Every room at the right temperature', [
           "We control underfloor heating, fancoils, heat pumps and ventilation per room, with setpoints the household can adjust from keypads, phone or wall panel. Bedrooms, living areas and the guest wing each follow their own schedule."]),
         ('Climate and shading working together', [
           "On the Costa del Sol the cheapest kilowatt-hour is the one the sun never puts into the house. Our climate logic works with the shading: blinds close on the sunny façade before the air conditioning has to fight the heat, and open again when the sun has moved on."]),
         ('Holiday and absence modes', [
           "Many of our clients spend part of the year elsewhere. Holiday profiles keep the house dry and protected at minimum cost, and can bring it back to comfort temperature before you land in Málaga."]),
       ],
       faq=[('Can KNX control my existing air conditioning?', 'In most cases yes, through KNX gateways for the major HVAC brands. We check compatibility during the consultation.'),
            ('Can I control the climate while I am abroad?', 'Yes, through Home Assistant with secure remote access. The system itself runs locally in the house.')]),
  dict(slug='shading-blinds', title='Shading & Blinds', h1='Motorised blinds, awnings and pergolas with KNX',
       meta='KNX shading control for Marbella villas: motorised blinds, awnings and pergolas driven by sun position, wind and rain sensors, tuned per façade.',
       short='Motorised blinds, awnings and pergolas driven by sun position and weather.',
       long='Sun-tracking, wind and rain protection, and glare control tuned per façade. Terraces on the Costa del Sol live or die on this: get it right and the house cools itself, get it wrong and nothing else in the system can save it.',
       tags=['Sun tracking', 'Wind & rain safety', 'Per-façade logic', 'Pergolas'],
       body=[
         ('Shading that follows the sun', [
           "We programme blinds, screens and louvres per façade using the sun's position through the day and the year. Rooms stay bright without glare, and the heat stays outside."]),
         ('Protection from wind and rain', [
           "A weather station on the roof retracts awnings and opens pergola louvres when the wind picks up, and closes them when it rains. Safety functions run on the KNX bus itself, so they work even if the internet is down."]),
         ('Terraces and pergolas', [
           "Bioclimatic pergolas, awnings and outdoor screens are tied into the same scenes as the lighting and heating, so an evening on the terrace is one button, not five remote controls."]),
       ],
       faq=[('Which blind motors do you work with?', 'Most professional motors from Somfy, Becker and others can be integrated via KNX actuators or KNX interfaces.'),
            ('Will the awnings retract automatically in strong wind?', 'Yes. Wind and rain safety is handled by the KNX weather station and has priority over all other commands.')]),
  dict(slug='security-access', title='Security & Access', h1='Integrated security, video entry and access control',
       meta='Alarm, video door entry, gates and access control integrated with KNX for villas in Marbella. Presence simulation and remote access while you are abroad.',
       short='Alarm, video door entry and access, integrated rather than bolted on.',
       long='Presence simulation, perimeter and gate control, video entry that reaches your phone abroad, and alarm integration that also puts the house into a safe state — lights on, blinds up, water off — instead of only making noise.',
       tags=['Video entry', 'Gates & access', 'Presence simulation', 'Leak & panic'],
       body=[
         ('Security as part of the house', [
           "An alarm that only makes noise is half a system. Integrated with KNX, an alarm can switch on all outdoor lighting, open the blinds, cut the water supply and send you a notification with camera images."]),
         ('Video entry and gates', [
           "Video door stations and gate control that reach your phone wherever you are, so you can let in the gardener, the pool service or a delivery while you are in Copenhagen or Stockholm."]),
         ('Presence simulation and leak protection', [
           "When the house is empty, lighting and blinds can follow a realistic daily pattern. Water leak sensors close the main valve automatically — one of the most valuable functions in a house that stands empty for weeks."]),
       ],
       faq=[('Can you connect my existing alarm?', 'Most professional alarm panels can be integrated via KNX interfaces or Home Assistant. We assess this on site.')]),
  dict(slug='energy-monitoring', title='Energy Monitoring', h1='Energy monitoring, solar and EV charging control',
       meta='Circuit-level energy metering, solar PV and battery integration, and load management for villas on the Costa del Sol, with clear reporting for remote owners.',
       short='Circuit-level metering, PV and battery visibility, and load management.',
       long='See what the house actually consumes, per circuit and per hour. Solar self-consumption logic that runs the pool pump, heat pump and car charger when your own production is highest, and clear reporting for owners managing a property remotely.',
       tags=['Circuit metering', 'PV self-consumption', 'EV charging', 'Owner reporting'],
       body=[
         ('Know where the energy goes', [
           "Circuit-level metering shows what the pool pump, air conditioning, underfloor heating and kitchen actually use, hour by hour. Most owners find at least one surprise in the first month."]),
         ('Use your own solar power', [
           "With solar panels and a battery, the cheapest energy is the energy you produce yourself. We schedule the pool pump, heat pump, water heating and EV charger to run when production is highest."]),
         ('Reporting for remote owners', [
           "Clear dashboards and monthly summaries in Home Assistant, so you can see from abroad that the house is behaving — and spot a fault before it becomes an expensive bill."]),
       ],
       faq=[('Can you integrate my existing inverter?', 'Most common inverters and batteries (e.g. SMA, Fronius, Huawei, Victron) can be read through Home Assistant or KNX gateways.')]),
  dict(slug='pool-outdoor-automation', title='Pool & Outdoor Automation', h1='Pool and garden automation in Marbella',
       meta='Pool pumps, heating, lighting, irrigation and covers on the same KNX system as the house. Pool and garden automation for villas on the Costa del Sol.',
       short='Pumps, heating, lighting, irrigation and covers on the same system as the house.',
       long='Filtration and heating schedules, pool and garden lighting scenes, irrigation tied to weather data, and cover control with safety interlocks. This is the domain our own product, Xcover, comes from.',
       tags=['Filtration & heating', 'Irrigation', 'Garden scenes', 'Cover interlocks'],
       body=[
         ('The pool as part of the house', [
           "Filtration, heating and pool lighting are usually run from a separate control box nobody understands. We bring them onto the KNX system, so the pool follows the same schedules, scenes and holiday modes as the rest of the house."]),
         ('Garden and irrigation', [
           "Irrigation zones that skip watering when rain is forecast, garden lighting scenes, and outdoor sockets and fountains on timers — all from the same keypads and app."]),
         ('Pool covers with proper safety', [
           "Motorised pool covers need hardware interlocks, not just an app button. We design cover control with safety logic in the system itself. This is where our own walkable pool cover, Xcover, comes from."]),
       ],
       faq=[('Can you automate an existing pool?', 'Usually yes. Pumps, heat pumps, lighting and salt chlorinators can be controlled or monitored via KNX actuators and interfaces.')]),
]
for i, s in enumerate(SERVICES):
    s['num'] = f'{i+1:02d}'

TECH = [
  dict(num='01', role='Visualisation & interface', vendors='Home Assistant', shots=[('tech-homeassistant.jpg', 'Home Assistant dashboard showing a room overview for a KNX villa')],
       body='The visualisation layer on top of KNX: floor plans, dashboards and remote access on phone, tablet and wall panel. It runs locally in the house, so the system keeps working when the internet does not — and it lets us bring in what is not KNX (media, EV chargers, inverters, appliances) without compromising the bus.',
       links=[('home-assistant.io', 'https://www.home-assistant.io')]),
  dict(num='02', role='Electrical board', vendors='Hager · ABB', shots=[('tech-hager.jpg', 'Hager KNX switching actuator in a distribution board')],
       body='The board is where a KNX installation is won or lost. We build with Hager or ABB actuators, dimmers and power supplies — European industrial hardware with long product lifecycles and spares you can still buy in ten years. Generously sized, clearly labelled, and documented so any electrician can work in it after us.',
       links=[('hager.com', 'https://www.hager.com'), ('abb.com', 'https://new.abb.com/low-voltage/products/building-automation')]),
  dict(num='03', role='Sensors & touch controls', vendors='Tense · Basalte', shots=[('tech-tense.jpg', 'Tense KNX keypad in concrete finish'), ('tech-basalte.jpg', 'Basalte KNX keypad in brushed copper')],
       body='What you actually touch. Tense and Basalte KNX keypads, thermostats and presence sensors in glass, steel, brass and stone — a long way from the white plastic rocker that comes as standard here. Chosen with the architect so the wall plates belong to the interior instead of interrupting it, and native KNX, so nothing depends on a proprietary protocol.',
       links=[('tense.be', 'https://www.tense.be'), ('basalte.be', 'https://www.basalte.be')]),
]

PROCESS = [('01', 'Consultation', 'A site visit or a call with your plans. We tell you what is worth automating and what is not.'),
           ('02', 'Design', 'Topology, panel layout, load schedule and a fixed scope your electrician can price and build against.'),
           ('03', 'Commissioning', 'ETS programming, on-site tuning of light, shade and climate, and a walkthrough with the household.'),
           ('04', 'Aftercare', "As-built documentation handed over, remote support, and changes made as the house's life changes.")]

HOME_FAQ = [
  ('What is KNX?', 'KNX is an open, worldwide standard for home and building control (ISO/IEC 14543), supported by around 500 manufacturers. Lighting, climate, shading, security and energy all communicate on the same bus, so you are never tied to one brand.'),
  ('Do you work outside Marbella?', 'Yes. We are based on Avenida Ricardo Soriano in Marbella and work along the Costa del Sol — from Sotogrande and Estepona through Benahavís, Nueva Andalucía and San Pedro to Fuengirola and Málaga.'),
  ('Can you help if my house already has a KNX system?', 'Yes. We audit and take over existing installations, recover or rebuild the ETS project and document the system — including installations where the original installer is no longer available.'),
  ('Which languages do you work in?', 'English, Swedish and Danish, with Spanish on site with electricians and builders.'),
  ('How much does a KNX system cost?', 'It depends on the size of the house and what you want to control. After a consultation we deliver a fixed scope and load schedule your electrician can price against, so you know the cost before work starts.'),
]

XB = [('Usable square metres', 'Closed, the cover is terrace. A pool that is out of use for most of the year becomes floor you can furnish, dine on and host on.'),
      ('Safety by default', 'A load-bearing surface rather than a floating sheet: no gap to slip through for children, guests or animals.'),
      ('Heat and water kept in', 'A sealed cover holds warmth overnight and cuts evaporation — less heating, less refilling, fewer chemicals.'),
      ('Clean and quiet', 'Leaves, dust and Saharan calima stay out of the water, so filtration runs shorter and the pool is ready when you are.'),
      ('Part of the house', 'Designed for KNX: one command puts the terrace, its lighting and the cover into the same evening scene.'),
      ('Architect-led detailing', 'Flush edge profiles and material choices intended to read as continuous terrace, not as pool equipment.')]
XS = [('Concept', 'Motorised, load-bearing walkable cover'), ('Installed level', 'Flush with surrounding terrace'), ('Control', 'KNX bus · local keypad · app'),
      ('Safety', 'Hardware interlocks, edge detection'), ('Configurations', 'Rectangular pools first, bespoke to follow'), ('Status', 'Prototype · pilot sites 2026–27')]
VALUES = [('Open systems only', "KNX and other open standards. Your house should not depend on one manufacturer's cloud, or on us being the only ones who can maintain it."),
          ('Documented, always', 'Every project leaves with as-built drawings and an ETS project file. If you ever replace us, the next engineer will thank you.'),
          ('Small on purpose', 'A handful of projects a year. Fewer clients, more attention, and a phone number that still works after handover.')]
COMPANY = [('Legal name', 'Scandinavian Technical Solutions S.L.'), ('Trading as', 'Scanditech · www.scanditech.es'),
           ('Address', 'Av. Ricardo Soriano, Edificio Golden 72, B, 1 · 29601 Marbella, Málaga'), ('CIF', 'B44771731'),
           ('EU VAT', 'ESB44771731'), ('Telephone', '+34 608 266 620 (call / text) · +45 20 90 30 50 (WhatsApp)')]

ORG = {
  "@type": ["Electrician", "HomeAndConstructionBusiness"], "@id": SITE + "/#business",
  "name": "Scanditech", "legalName": "Scandinavian Technical Solutions S.L.", "url": SITE + "/",
  "logo": SITE + "/images/favicon-512.png", "image": SITE + "/images/hero-villa.jpg",
  "description": "KNX smart home and building automation for villas and developments in Marbella and on the Costa del Sol: design, ETS programming, commissioning and aftercare.",
  "telephone": "+34608266620", "email": MAIL, "vatID": "ESB44771731", "priceRange": "€€€",
  "address": {"@type": "PostalAddress", "streetAddress": "Av. Ricardo Soriano 72, Edificio Golden, B, 1", "addressLocality": "Marbella", "addressRegion": "Málaga", "postalCode": "29601", "addressCountry": "ES"},
  "geo": {"@type": "GeoCoordinates", "latitude": 36.5098, "longitude": -4.8909},
  "areaServed": [{"@type": "City", "name": n} for n in ["Marbella", "Estepona", "Benahavís", "San Pedro de Alcántara", "Sotogrande", "Fuengirola", "Málaga"]],
  "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "18:00"}],
  "knowsLanguage": ["en", "sv", "da", "es"],
  "knowsAbout": ["KNX", "ETS", "Home automation", "Smart home", "Lighting control", "DALI", "HVAC control", "Motorised shading", "Home Assistant", "Energy monitoring"],
  "sameAs": ["https://www.xcover.eu"],
}

# ---------------------------------------------------------------- layout
NAV = [('/', 'Home'), ('/services/', 'Services'), ('/xcover/', 'Xcover'), ('/about/', 'About'), ('/contact/', 'Contact')]
LANGS = [('en', '/'), ('es', '/es/'), ('da', '/da/'), ('sv', '/sv/')]

from es_data import ES_SERVICES, ES_FAQ
GA_ID = ''  # GA4 measurement id, e.g. G-XXXXXXX
ES_SLUG = {d['en']: d['slug'] for d in ES_SERVICES}
UI = {
 'en': dict(nav=NAV, skip='Skip to content', home='/', tag='Smart Building Automation · Marbella', menu='Menu', svc='Services', site='Site', contact='Contact',
            call='Call or text', langs='We work in English, Swedish and Danish', foot='KNX smart home automation · Marbella · Costa del Sol',
            svclinks=[(f"/services/{s['slug']}/", s['title']) for s in SERVICES]),
 'es': dict(nav=[('/es/', 'Inicio'), ('/es/servicios/', 'Servicios'), ('/xcover/', 'Xcover'), ('/about/', 'Empresa'), ('/es/contacto/', 'Contacto')],
            skip='Ir al contenido', home='/es/', tag='Domótica KNX · Marbella', menu='Menú', svc='Servicios', site='Web', contact='Contacto',
            call='Llamar o SMS', langs='Español, inglés, sueco y danés', foot='Domótica KNX · Integrador KNX en Marbella · Costa del Sol',
            svclinks=[(f"/es/servicios/{d['slug']}/", d['title']) for d in ES_SERVICES]),
}

def ga_head():
    if not GA_ID:
        return ''
    return ("<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}"
            "var c=null;try{c=localStorage.getItem('st_consent')}catch(e){}"
            "gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:c==='yes'?'granted':'denied'});"
            "gtag('js',new Date());gtag('config','" + GA_ID + "');</script>"
            "<script async src=\"https://www.googletagmanager.com/gtag/js?id=" + GA_ID + "\"></script>")

def consent_html(lang):
    if not GA_ID:
        return ''
    t = {'es': ('Usamos cookies analíticas (Google Analytics) para saber cómo se usa la web.', 'Aceptar', 'Rechazar'),
         'da': ('Vi bruger analyse-cookies (Google Analytics) til at se, hvordan siden bruges.', 'Accepter', 'Afvis'),
         'sv': ('Vi använder analyscookies (Google Analytics) för att se hur webbplatsen används.', 'Godkänn', 'Avvisa')}.get(lang, ('We use analytics cookies (Google Analytics) to understand how the site is used.', 'Accept', 'Decline'))
    return f"""<div id="cc" class="cc" hidden><p>{t[0]}</p><div><button type="button" data-v="yes">{t[1]}</button><button type="button" data-v="no" class="no">{t[2]}</button></div></div>
<script>(function(){{var c=null;try{{c=localStorage.getItem('st_consent')}}catch(e){{}}var b=document.getElementById('cc');if(!c)b.hidden=false;b.addEventListener('click',function(ev){{var v=ev.target.getAttribute('data-v');if(!v)return;try{{localStorage.setItem('st_consent',v)}}catch(e){{}}if(v==='yes')gtag('consent','update',{{analytics_storage:'granted'}});b.hidden=true}});document.addEventListener('click',function(ev){{var a=ev.target.closest&&ev.target.closest('a');if(!a||!window.gtag)return;var h=a.getAttribute('href')||'';var k=h.indexOf('wa.me')>-1?'whatsapp_click':h.indexOf('tel:')===0?'phone_click':h.indexOf('mailto:')===0?'email_click':null;if(k)gtag('event',k,{{link_url:h}})}});var f=document.querySelector('form.form');if(f)f.addEventListener('submit',function(){{gtag('event','generate_lead',{{form:'contact'}})}});}})();</script>"""



def jsonld(*objs):
    return ''.join('<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", **o}, ensure_ascii=False) + '</script>' for o in objs)


def crumbs_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (u, n) in enumerate(items)]}


def faq_ld(faq):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def faq_html(faq, title='Questions we are often asked'):
    return f'''<section class="sec bt"><div class="wrap"><h2 class="h2 s" style="margin-bottom:40px">{title}</h2><div class="faq">''' + ''.join(
        f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in faq) + '</div></div></section>'


def page(path, title, desc, body, active='/', lang='en', ld=(), alternates=None, og_image='/images/hero-villa.jpg', preload=None, noindex=False):
    T = UI['es' if lang == 'es' else 'en']
    nav = ''.join(f'<a class="l" href="{u}"' + (' aria-current="page"' if u == active else '') + f'>{n}</a>' for u, n in T['nav'])
    nav += ''.join(f'<a class="lang" href="{u}" hreflang="{l}">{l.upper()}</a>' for l, u in (alternates or [('en','/'),('es','/es/')]) if l != lang and l in ('en','es'))
    alt = ''
    if alternates:
        alt = ''.join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{u}">' for l, u in alternates) + f'<link rel="alternate" hreflang="x-default" href="{SITE}/">'
    pre = f'<link rel="preload" as="image" href="{preload}" fetchpriority="high">' if preload else ''
    doc = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{'<meta name="robots" content="noindex, follow">' if noindex else ''}
<link rel="canonical" href="{SITE}{path}">
{alt}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Scanditech">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}{og_image}">
<meta property="og:locale" content="{ {'en':'en_GB','es':'es_ES','da':'da_DK','sv':'sv_SE'}[lang] }">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#15181A">
<link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32.png">
<link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
<link rel="preload" href="/fonts/instrument-serif.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/schibsted-grotesk.woff2" as="font" type="font/woff2" crossorigin>
{pre}
<link rel="stylesheet" href="/css/site.css?v={CSSV}">
{jsonld(ORG, *ld)}
{ga_head()}
</head>
<body>
<a class="skip" href="#main">{T["skip"]}</a>
<header class="hdr" id="hdr"><div class="wrap">
  <a class="logo" href="{T["home"]}" aria-label="Scanditech"><span class="mono">STS</span><span><b>Scanditech</b><small>{T["tag"]}</small></span></a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" onclick="var h=document.getElementById('hdr');var o=h.classList.toggle('open');this.setAttribute('aria-expanded',o)">{T["menu"]}</button>
  <nav class="nav" id="nav" aria-label="Main">{nav}<a class="btn-dark" href="{TEL}"><span class="dot"></span>+34 608 266 620</a></nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="ftr">
  <div class="wrap g">
    <div>
      <span class="logo"><span class="mono">STS</span><b>Scanditech</b></span>
      <p>Scandinavian Technical Solutions S.L.<br>Av. Ricardo Soriano, Edificio Golden 72, B, 1<br>29601 Marbella, Málaga, Spain</p>
      <p style="font-size:13px;color:rgba(244,241,235,.5);margin-top:16px">{T["langs"]} · <a href="/">English</a> · <a href="/es/">Español</a> · <a href="/da/">Dansk</a> · <a href="/sv/">Svenska</a></p>
    </div>
    <div><h2>{T['svc']}</h2><ul>{''.join(f'<li><a href="{u}">{e(n)}</a></li>' for u, n in T['svclinks'])}</ul></div>
    <div><h2>{T['site']}</h2><ul>{''.join(f'<li><a href="{u}">{n}</a></li>' for u, n in T['nav'])}</ul></div>
    <div><h2>{T['contact']}</h2><ul><li><a href="{TEL}">{T['call']} +34 608 266 620</a></li><li><a href="{WA}" rel="noopener">WhatsApp +45 20 90 30 50</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="https://www.xcover.eu" rel="noopener">xcover.eu</a></li></ul></div>
  </div>
  <div class="wrap"><div class="base"><span>© {datetime.date.today().year} Scandinavian Technical Solutions S.L. · CIF B44771731 · EU VAT ESB44771731</span><span>{T["foot"]}</span></div></div>
</footer>
<a class="wa-float" href="{WA}" rel="noopener">WhatsApp</a>
{consent_html(lang)}
</body>
</html>
'''
    fn = os.path.join(OUT, path.strip('/'), 'index.html') if path.endswith('/') else os.path.join(OUT, path.lstrip('/'))
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    open(fn, 'w', encoding='utf-8').write(doc)
    return path


PAGES = []

# ---------------------------------------------------------------- home
def cap_grid():
    return '<div class="cap">' + ''.join(
        f'<a class="c" href="/services/{s["slug"]}/"><p class="num">{s["num"]}</p><h3>{e(s["title"])}</h3><p>{e(s["short"])}</p><span class="more">Read more →</span></a>' for s in SERVICES) + \
        f'<div class="ask"><a href="{WA}" rel="noopener">Not sure what your project needs?<br>Ask us directly →</a></div></div>'


home = f'''
<section class="hero">
  <img src="/images/hero-villa.jpg" alt="Villa in Marbella at dusk with warm KNX-controlled lighting on the terrace and pool" width="1600" height="900" fetchpriority="high">
  <div class="wrap"><div class="in">
    <p class="eyebrow">KNX smart home automation · Marbella · Costa del Sol</p>
    <h1>A house that understands<br><em>how you live in it.</em></h1>
    <p class="sub">We design, program and maintain KNX systems for private villas and developments in Marbella — light, climate, shade, security and energy, held together as one calm system.</p>
    <div class="btns"><a class="btn light" href="{WA}" rel="noopener">Talk to us on WhatsApp</a><a class="btn ghost-l" href="/services/">What we do</a></div>
  </div></div>
</section>
<div class="wrap"><div class="stats">
  <div><b>KNX</b><span>Open standard, no vendor lock-in</span></div>
  <div><b>Marbella</b><span>Av. Ricardo Soriano, on the coast</span></div>
  <div><b>1:1</b><span>The designer commissions your system</span></div>
  <div><b>EN · SV · DA</b><span>Working languages</span></div>
</div></div>
<section class="sec"><div class="wrap split">
  <p class="eyebrow">Our approach</p>
  <div>
    <h2 class="h2">Scandinavian engineering discipline, applied to Spanish houses.</h2>
    <div class="cols2">
      <p class="body">Automation goes wrong when it is sold as gadgets. We start from the plans and the way the house is actually used — where you walk in at night, which terrace takes the afternoon sun, how the pool and the guest wing are managed when nobody is here.</p>
      <p class="body">Then we build it on <a href="/services/knx-design-programming/" style="border-bottom:1px solid rgba(168,122,69,.4)">KNX</a>: an open, vendor-neutral standard with three decades of installed base behind it. Nothing depends on one manufacturer staying in business, and every project leaves our hands fully documented.</p>
    </div>
  </div>
</div></section>
<section class="sec dark"><div class="wrap">
  <div class="cap-top"><h2 class="h2 s">Smart home capabilities</h2><a href="/services/">All services →</a></div>
  {cap_grid()}
</div></section>
<div class="wrap"><div class="brands bb">
  <p>Built on components<br>we trust</p>
  <ul><li>Home Assistant</li><li>Hager</li><li>ABB</li><li>Tense</li><li>Basalte</li><li>KNX</li></ul>
  <a class="x" href="/services/#technologies">Why these →</a>
</div></div>
<section class="sec"><div class="wrap x2">
  <div class="xbox"><span class="big">Xcover</span><dl>
    <div><dt>Surface</dt><dd>Walkable, load-bearing</dd></div><div><dt>Level</dt><dd>Flush with the terrace</dd></div>
    <div><dt>Control</dt><dd>KNX · keypad · app</dd></div><div><dt>Status</dt><dd style="color:var(--brass-l)">Prototype</dd></div></dl></div>
  <div>
    <p class="eyebrow">In development · Our own product</p>
    <h2 class="h2" style="font-size:52px;line-height:1.06">Xcover</h2>
    <p class="lead" style="font-size:18px;margin-top:26px">A smart, walkable pool covering. Closed, it is terrace you can stand on — safe around children and pets, and it gives back the square metres the pool takes up for nine months of the year. Open, it disappears.</p>
    <p class="body muted" style="margin-top:20px">Designed to be driven from the same KNX system as the rest of the house.</p>
    <div class="btns"><a class="btn dark" href="/xcover/">See the concept</a><a class="btn ghost" href="https://www.xcover.eu" rel="noopener">xcover.eu</a></div>
  </div>
</div></section>
<section class="sec sand"><div class="wrap">
  <h2 class="h2 s" style="margin-bottom:60px">How a project runs</h2>
  <div class="steps">{''.join(f'<div><p class="num">{n}</p><h3>{t}</h3><p>{b}</p></div>' for n, t, b in PROCESS)}</div>
</div></section>
{faq_html(HOME_FAQ)}
'''
PAGES.append(page('/', 'KNX Smart Home Automation in Marbella | Scanditech',
                  'KNX smart home and villa automation in Marbella and the Costa del Sol. Lighting, climate, shading, security and energy — designed, programmed and documented by Scanditech.',
                  home, '/', ld=[faq_ld(HOME_FAQ), {"@type": "WebSite", "name": "Scanditech", "url": SITE + "/"}],
                  alternates=LANGS, preload='/images/hero-villa.jpg'))

# ---------------------------------------------------------------- services overview
tech = ''.join(f'''<div><div class="shots">{''.join(f'<img src="/images/{src}" alt="{e(alt)}" loading="lazy" width="640" height="720">' for src, alt in t["shots"])}</div>
<div class="tx"><div><span class="num" style="margin:0">{t["num"]}</span><span class="role">{t["role"]}</span></div><h3>{e(t["vendors"])}</h3><p>{e(t["body"])}</p>
<div class="lk">{''.join(f'<a href="{u}" rel="noopener">{l} ↗</a>' for l, u in t["links"])}</div></div></div>''' for t in TECH)
svc_list = ''.join(f'''<div class="svc"><p class="num">{s["num"]}</p><h2><a href="/services/{s["slug"]}/">{e(s["title"])}</a></h2><div><p class="body" style="font-size:16.5px">{e(s["long"])}</p>
<ul class="tags">{''.join(f'<li>{e(t)}</li>' for t in s["tags"])}</ul><a class="go" href="/services/{s["slug"]}/">More about {e(s["title"].lower())} →</a></div></div>''' for s in SERVICES)
cta = f'''<section class="sec"><div class="wrap"><div class="cta"><div><h2>Consulting &amp; system audits</h2>
<p>Inherited a system nobody documented? Tendering a project and unsure whether the bus topology, actuator count and load list actually add up? We review specifications, take over abandoned installations and write the documentation that should have existed.</p></div>
<div class="b"><a class="btn light" href="{WA}" rel="noopener">WhatsApp us</a><a class="btn ghost-l" href="{TEL}">+34 608 266 620</a></div></div></div></section>'''
services = f'''
<section class="phead"><div class="wrap">
  <p class="eyebrow">Services</p>
  <h1>KNX home automation services — one system for the whole house.</h1>
  <p class="lead">We work as the automation partner on new villas and renovations in Marbella and along the Costa del Sol, and as an independent consultant for architects, developers and other installers who need a second set of eyes on a KNX specification.</p>
</div></section>
<section><div class="wrap" style="padding-bottom:40px">{svc_list}</div></section>
<section class="sec sand" id="technologies"><div class="wrap">
  <div class="cols2" style="align-items:end;margin:0 0 70px">
    <div><p class="eyebrow">Technologies</p><h2 class="h2" style="font-size:42px">We commit to a small set of components we trust, and know them properly.</h2></div>
    <p class="body" style="font-size:16.5px">Everything below is open KNX or runs locally in the house — no proprietary bus, no subscription, no single supplier who can strand you. It is also, frankly, better looking than what comes as standard on a Spanish new-build.</p>
  </div>
  <div class="tech">{tech}</div>
</div></section>
{cta}
'''
PAGES.append(page('/services/', 'KNX Home Automation Services in Marbella | Scanditech',
                  'KNX design and programming, lighting control, climate, shading, security, energy monitoring and pool automation for villas in Marbella and the Costa del Sol.',
                  services, '/services/', ld=[crumbs_ld([('/', 'Home'), ('/services/', 'Services')]),
                  {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/services/{s['slug']}/", "name": s['title']} for i, s in enumerate(SERVICES)]}],
                  alternates=[('en', '/services/'), ('es', '/es/servicios/')]))

# ---------------------------------------------------------------- service detail pages
for s in SERVICES:
    path = f'/services/{s["slug"]}/'
    art = ''.join(f'<h2>{e(h)}</h2>' + ''.join(f'<p>{e(p)}</p>' for p in ps) for h, ps in s['body'])
    side = ''.join(f'<li><a href="/services/{o["slug"]}/"' + (' aria-current="page"' if o is s else '') + f'>{e(o["title"])}</a></li>' for o in SERVICES)
    others = [o for o in SERVICES if o is not s][:3]
    body = f'''
<section class="phead"><div class="wrap">
  <p class="crumbs"><a href="/">Home</a> / <a href="/services/">Services</a> / {e(s["title"])}</p>
  <h1>{e(s["h1"])}</h1>
  <p class="lead">{e(s["long"])}</p>
  <ul class="tags">{''.join(f'<li>{e(t)}</li>' for t in s["tags"])}</ul>
</div></section>
<section class="sec"><div class="wrap art">
  <div>{art}
    <div class="btns"><a class="btn dark" href="{WA}" rel="noopener">Talk to us on WhatsApp</a><a class="btn ghost" href="/contact/">Send an enquiry</a></div>
  </div>
  <aside class="aside"><h3>All services</h3><ul>{side}</ul>
    <h3>Talk to the engineer</h3><p style="font-size:15px;line-height:1.7;margin:0 0 18px;color:var(--ink2)">Send plans, photos or questions — you reach the person who designs and commissions the system.</p>
    <a class="btn dark" style="display:block;text-align:center" href="{TEL}">+34 608 266 620</a></aside>
</div></section>
{faq_html(s["faq"]) if s["faq"] else ''}
<section class="sec sand"><div class="wrap"><h2 class="h2 s" style="margin-bottom:44px">Related services</h2><div class="cards">{''.join(f'<div><p class="num">{o["num"]}</p><h3><a href="/services/{o["slug"]}/">{e(o["title"])}</a></h3><p>{e(o["short"])}</p></div>' for o in others)}</div></div></section>
'''
    ld = [crumbs_ld([('/', 'Home'), ('/services/', 'Services'), (path, s['title'])]),
          {"@type": "Service", "name": s['h1'], "serviceType": s['title'], "description": s['meta'], "provider": {"@id": SITE + "/#business"},
           "areaServed": {"@type": "Place", "name": "Marbella and the Costa del Sol"}, "url": SITE + path}]
    if s['faq']:
        ld.append(faq_ld(s['faq']))
    PAGES.append(page(path, f'{s["h1"]} | Scanditech', s['meta'], body, '/services/', ld=ld, alternates=[('en', path), ('es', f'/es/servicios/{ES_SLUG[s["slug"]]}/')]))

# ---------------------------------------------------------------- xcover
xc = f'''
<section class="xhero"><div class="wrap">
  <p class="eyebrow">A Scanditech product · Under development</p>
  <h1>Xcover</h1>
  <p>The walkable pool cover. Terrace by day, pool in seconds.</p>
</div></section>
<section class="sec bb"><div class="wrap split">
  <p class="eyebrow">The idea</p>
  <div><h2 class="h2" style="font-size:42px">A pool occupies the best part of the plot, and for most of the year nobody is in it.</h2>
  <div class="cols2"><p class="body">Xcover is a load-bearing, motorised covering that sits flush with the surrounding terrace. Closed, it reads as floor: you can put a table on it, let the children run across it, host on it. Open, the pool is simply there.</p>
  <p class="body">Because we build automation for a living, control is not an afterthought. Xcover is designed to sit on the house's KNX bus alongside lighting, shading and climate — with its safety logic in hardware, not in an app.</p></div></div>
</div></section>
<section class="sec"><div class="wrap"><h2 class="h2 s" style="margin-bottom:56px">What it is for</h2>
<div class="cards">{''.join(f'<div><h3>{t}</h3><p>{b}</p></div>' for t, b in XB)}</div></div></section>
<section class="sec dark"><div class="wrap">
  <div style="display:flex;align-items:baseline;gap:20px;flex-wrap:wrap;margin-bottom:48px"><h2 class="h2 s">Design targets</h2><p style="font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--brass);margin:0">Indicative — product in development, not final specification</p></div>
  <dl class="specs" style="margin:0">{''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in XS)}</dl>
</div></section>
<section class="sec bt"><div class="wrap"><div style="max-width:760px">
  <p class="eyebrow">Status</p>
  <h2 class="h2" style="font-size:40px">Prototyping now. Pilot installations on the Costa del Sol next.</h2>
  <p class="body" style="font-size:16.5px;margin-top:24px">We are looking for a small number of pilot sites, and talking to developers and pool builders interested in specifying Xcover. Full product information will live at xcover.eu.</p>
  <div class="btns"><a class="btn dark" href="https://www.xcover.eu" rel="noopener">Visit xcover.eu</a><a class="btn ghost" href="{WA}" rel="noopener">Register interest</a></div>
</div></div></section>
'''
page('/xcover/', 'Xcover | Scanditech',
                  'Xcover is a load-bearing, motorised pool cover that sits flush with the terrace. Developed by Scanditech in Marbella, controlled by KNX. Pilot sites wanted on the Costa del Sol.',
                  xc, '/xcover/', ld=[crumbs_ld([('/', 'Home'), ('/xcover/', 'Xcover')])], noindex=True)

# ---------------------------------------------------------------- about
about = f'''
<section class="phead"><div class="wrap split">
  <p class="eyebrow">About</p>
  <div><h1 style="font-size:58px;line-height:1.06">A Scandinavian technical practice, based in Marbella.</h1>
  <p class="lead" style="margin-top:34px">Scandinavian Technical Solutions S.L. is a small, deliberately hands-on company on Avenida Ricardo Soriano. We take on a limited number of projects a year so that the person who designs your system is the person who commissions it — and the person who picks up the phone two years later.</p>
  <p class="body muted" style="margin-top:20px;max-width:640px">Northern European standards of documentation and follow-up, Spanish site reality, and no interest in selling you more hardware than the house needs.</p></div>
</div></section>
<section class="sec tight"><div class="wrap"><div class="cards">{''.join(f'<div><h3>{t}</h3><p>{b}</p></div>' for t, b in VALUES)}</div></div></section>
<section class="sec sand"><div class="wrap x2">
  <div><h2 class="h2 s" style="font-size:34px;margin-bottom:32px">Company details</h2>
  <dl class="rows">{''.join(f'<div><dt>{k}</dt><dd>{e(v)}</dd></div>' for k, v in COMPANY)}</dl></div>
  <div><h2 class="h2 s" style="font-size:34px;margin-bottom:32px">Where we work</h2>
  <p class="body">Our office is in central Marbella. We work on villas and developments along the Costa del Sol — Marbella, Nueva Andalucía, the Golden Mile, Benahavís, La Zagaleta, Estepona, San Pedro de Alcántara, Sotogrande, Mijas, Fuengirola and Málaga.</p>
  <p class="body" style="margin-top:18px">Many of our clients are from Scandinavia and Northern Europe and spend part of the year elsewhere. We speak English, Swedish and Danish with owners, and Spanish on site.</p>
  <div class="btns"><a class="btn dark" href="/contact/">Get in touch</a></div></div>
</div></section>
'''
PAGES.append(page('/about/', 'About Scanditech – Scandinavian KNX Engineers in Marbella',
                  'Scandinavian Technical Solutions S.L. is a small KNX engineering practice on Avenida Ricardo Soriano in Marbella. English, Swedish and Danish spoken.',
                  about, '/about/', ld=[crumbs_ld([('/', 'Home'), ('/about/', 'About')]), {"@type": "AboutPage", "url": SITE + "/about/"}]))

# ---------------------------------------------------------------- contact
contact = f'''
<section class="sec" style="padding-top:100px"><div class="wrap">
  <p class="eyebrow">Contact</p>
  <h1 class="serif" style="font-size:64px;line-height:1.04;margin:0;max-width:760px">Send a message, or just call. You will reach us, not a call centre.</h1>
  <div class="ways">
    <a href="{WA}" rel="noopener"><span class="k">Fastest</span><span><span class="t">WhatsApp</span><span class="d">+45 20 90 30 50 — send plans, photos, questions</span></span></a>
    <a href="{TEL}"><span class="k">Direct</span><span><span class="t">Call or text</span><span class="d">+34 608 266 620 — Mon–Fri, 09:00–18:00 CET</span></span></a>
  </div>
  <div class="x2" style="margin-top:90px">
    <div>
      <h2 style="font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--mute);margin:0 0 26px;font-weight:400">Or write to us</h2>
      <div id="sent" class="note" hidden>Thank you — your enquiry has been sent. We usually reply within one working day.</div>
      <form class="form" method="post" action="/enquiry.php">
        <label><span>Name</span><input type="text" name="name" required autocomplete="name"></label>
        <div class="two"><label><span>Email</span><input type="email" name="email" required autocomplete="email"></label>
        <label><span>Phone</span><input type="tel" name="phone" autocomplete="tel"></label></div>
        <label><span>About the project</span><textarea name="message" rows="4" required></textarea></label>
        <label class="hp" aria-hidden="true"><span>Website</span><input type="text" name="website" tabindex="-1" autocomplete="off"></label>
        <button type="submit">Send enquiry</button>
        <p style="font-size:13.5px;line-height:1.7;color:var(--mute);margin:0">Or email <a href="mailto:{MAIL}" style="color:var(--brass)">{MAIL}</a> directly.</p>
      </form>
    </div>
    <div>
      <h2 style="font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--mute);margin:0 0 26px;font-weight:400">Office</h2>
      <address style="font-style:normal;font-size:18px;line-height:1.75">Scandinavian Technical Solutions S.L.<br>Av. Ricardo Soriano<br>Edificio Golden 72, B, 1<br>29601 Marbella, Málaga<br>Spain</address>
      <div class="map"><iframe title="Scanditech office on Avenida Ricardo Soriano, Marbella" src="https://www.google.com/maps?q=Avenida%20Ricardo%20Soriano%2072%2C%2029601%20Marbella%2C%20M%C3%A1laga%2C%20Spain&amp;z=16&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
      <a href="https://www.google.com/maps/search/?api=1&amp;query=Avenida+Ricardo+Soriano+72,+29601+Marbella,+M%C3%A1laga,+Spain" rel="noopener" style="display:inline-block;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--brass);margin-top:16px">Open in Google Maps ↗</a>
      <p style="font-size:14px;line-height:1.8;color:var(--mute);margin:30px 0 0">CIF B44771731<br>EU VAT ESB44771731</p>
    </div>
  </div>
</div></section>
<script>if(location.search.indexOf('sent=1')>-1){{document.getElementById('sent').hidden=false}}</script>
'''
PAGES.append(page('/contact/', 'Contact Scanditech – KNX Smart Home, Marbella',
                  'Contact Scanditech in Marbella: WhatsApp +45 20 90 30 50, call +34 608 266 620 or send an enquiry. Office on Avenida Ricardo Soriano.',
                  contact, '/contact/', ld=[crumbs_ld([('/', 'Home'), ('/contact/', 'Contact')]), {"@type": "ContactPage", "url": SITE + "/contact/"}], alternates=[('en', '/contact/'), ('es', '/es/contacto/')]))


# ---------------------------------------------------------------- Spanish (/es/)
def cap_grid_es():
    return '<div class="cap">' + ''.join(
        f'<a class="c" href="/es/servicios/{d["slug"]}/"><p class="num">{i+1:02d}</p><h3>{e(d["title"])}</h3><p>{e(d["short"])}</p><span class="more">Más información →</span></a>' for i, d in enumerate(ES_SERVICES)) + \
        f'<div class="ask"><a href="{WA}" rel="noopener">¿No sabe qué necesita su proyecto?<br>Pregúntenos directamente →</a></div></div>'

ES_ALT_HOME = [('en', '/'), ('es', '/es/'), ('da', '/da/'), ('sv', '/sv/')]
es_home = f"""
<section class="hero">
  <img src="/images/hero-villa.jpg" alt="Villa en Marbella al atardecer con iluminación domótica KNX en la terraza y la piscina" width="1600" height="900" fetchpriority="high">
  <div class="wrap"><div class="in">
    <p class="eyebrow">Domótica KNX · Marbella · Costa del Sol</p>
    <h1>Domótica KNX para villas<br><em>en Marbella.</em></h1>
    <p class="sub">Integrador KNX en Marbella. Diseñamos, programamos y mantenemos instalaciones domóticas para villas y promociones: iluminación, climatización, persianas, seguridad y energía en un solo sistema.</p>
    <div class="btns"><a class="btn light" href="{WA}" rel="noopener">Escríbanos por WhatsApp</a><a class="btn ghost-l" href="/es/servicios/">Servicios</a></div>
  </div></div>
</section>
<div class="wrap"><div class="stats">
  <div><b>KNX</b><span>Estándar abierto, sin depender de una marca</span></div>
  <div><b>Marbella</b><span>Av. Ricardo Soriano</span></div>
  <div><b>1:1</b><span>Quien diseña, programa y pone en marcha</span></div>
  <div><b>ES · EN · SV · DA</b><span>Idiomas de trabajo</span></div>
</div></div>
<section class="sec"><div class="wrap split">
  <p class="eyebrow">Nuestro enfoque</p>
  <div>
    <h2 class="h2">Ingeniería escandinava aplicada a la vivienda española.</h2>
    <div class="cols2">
      <p class="body">La domótica sale mal cuando se vende como un conjunto de aparatos. Nosotros empezamos por los planos y por cómo se vive la casa: por dónde entra de noche, qué terraza recibe el sol de la tarde, cómo se gestionan la piscina y la zona de invitados cuando no hay nadie.</p>
      <p class="body">Después lo construimos sobre <a href="/es/servicios/programacion-knx/" style="border-bottom:1px solid rgba(168,122,69,.4)">KNX</a>, un estándar abierto con más de treinta años de instalaciones. Nada depende de que un fabricante siga existiendo, y cada proyecto se entrega totalmente documentado.</p>
    </div>
  </div>
</div></section>
<section class="sec dark"><div class="wrap">
  <div class="cap-top"><h2 class="h2 s">Soluciones de domótica y automatización</h2><a href="/es/servicios/">Todos los servicios →</a></div>
  {cap_grid_es()}
</div></section>
<div class="wrap"><div class="brands bb">
  <p>Componentes<br>de confianza</p>
  <ul><li>Home Assistant</li><li>Hager</li><li>ABB</li><li>Tense</li><li>Basalte</li><li>KNX</li></ul>
  <a class="x" href="/services/#technologies">Por qué →</a>
</div></div>
<section class="sec sand"><div class="wrap">
  <h2 class="h2 s" style="margin-bottom:60px">Cómo trabajamos</h2>
  <div class="steps">
    <div><p class="num">01</p><h3>Consulta</h3><p>Visita a la obra o llamada con sus planos. Le decimos qué merece la pena automatizar y qué no.</p></div>
    <div><p class="num">02</p><h3>Proyecto</h3><p>Topología, cuadros, listado de cargas y un alcance cerrado que su electricista puede presupuestar.</p></div>
    <div><p class="num">03</p><h3>Puesta en marcha</h3><p>Programación ETS, ajuste en obra de iluminación, persianas y clima, y explicación a la familia.</p></div>
    <div><p class="num">04</p><h3>Mantenimiento</h3><p>Documentación as-built, soporte remoto y cambios a medida que cambia la vida en la casa.</p></div>
  </div>
</div></section>
{faq_html(ES_FAQ, 'Preguntas frecuentes sobre domótica KNX')}
"""
PAGES.append(page('/es/', 'Domótica KNX en Marbella – Integrador KNX | Scanditech',
                  'Domótica KNX en Marbella y la Costa del Sol. Integrador KNX: diseño, programación ETS y mantenimiento de instalaciones domóticas para villas. Iluminación, clima, persianas y seguridad.',
                  es_home, '/es/', lang='es', ld=[faq_ld(ES_FAQ)], alternates=ES_ALT_HOME, preload='/images/hero-villa.jpg'))

es_list = ''.join(f"""<div class="svc"><p class="num">{i+1:02d}</p><h2><a href="/es/servicios/{d['slug']}/">{e(d['title'])}</a></h2><div><p class="body" style="font-size:16.5px">{e(d['long'])}</p>
<ul class="tags">{''.join(f'<li>{e(t)}</li>' for t in d['tags'])}</ul><a class="go" href="/es/servicios/{d['slug']}/">Más información →</a></div></div>""" for i, d in enumerate(ES_SERVICES))
es_svc = f"""
<section class="phead"><div class="wrap">
  <p class="eyebrow">Servicios</p>
  <h1>Servicios de domótica KNX: un solo sistema para toda la casa.</h1>
  <p class="lead">Somos el integrador KNX en obra nueva y reformas en Marbella y la Costa del Sol, y consultores independientes para arquitectos, promotores e instaladores que necesitan revisar un proyecto KNX.</p>
</div></section>
<section><div class="wrap" style="padding-bottom:40px">{es_list}</div></section>
<section class="sec"><div class="wrap"><div class="cta"><div><h2>Consultoría y auditoría de instalaciones</h2>
<p>¿Ha heredado una instalación sin documentar? ¿Licita un proyecto y no sabe si la topología, el número de actuadores y el listado de cargas cuadran? Revisamos proyectos, nos hacemos cargo de instalaciones abandonadas y redactamos la documentación que debería existir.</p></div>
<div class="b"><a class="btn light" href="{WA}" rel="noopener">WhatsApp</a><a class="btn ghost-l" href="{TEL}">+34 608 266 620</a></div></div></div></section>
"""
PAGES.append(page('/es/servicios/', 'Servicios de domótica KNX en Marbella | Scanditech',
                  'Programación KNX, control de iluminación, climatización, persianas motorizadas, seguridad, gestión energética y domótica de piscina en Marbella y la Costa del Sol.',
                  es_svc, '/es/servicios/', lang='es', ld=[crumbs_ld([('/es/', 'Inicio'), ('/es/servicios/', 'Servicios')])], alternates=[('en', '/services/'), ('es', '/es/servicios/')]))

for i, d in enumerate(ES_SERVICES):
    path = f'/es/servicios/{d["slug"]}/'
    art = ''.join(f'<h2>{e(h)}</h2>' + ''.join(f'<p>{e(x)}</p>' for x in ps) for h, ps in d['body'])
    side = ''.join(f'<li><a href="/es/servicios/{o["slug"]}/"' + (' aria-current="page"' if o is d else '') + f'>{e(o["title"])}</a></li>' for o in ES_SERVICES)
    others = [(j, o) for j, o in enumerate(ES_SERVICES) if o is not d][:3]
    body = f"""
<section class="phead"><div class="wrap">
  <p class="crumbs"><a href="/es/">Inicio</a> / <a href="/es/servicios/">Servicios</a> / {e(d["title"])}</p>
  <h1>{e(d["h1"])}</h1>
  <p class="lead">{e(d["long"])}</p>
  <ul class="tags">{''.join(f'<li>{e(t)}</li>' for t in d["tags"])}</ul>
</div></section>
<section class="sec"><div class="wrap art">
  <div>{art}
    <div class="btns"><a class="btn dark" href="{WA}" rel="noopener">Escríbanos por WhatsApp</a><a class="btn ghost" href="/es/contacto/">Enviar consulta</a></div>
  </div>
  <aside class="aside"><h3>Servicios</h3><ul>{side}</ul>
    <h3>Hable con el ingeniero</h3><p style="font-size:15px;line-height:1.7;margin:0 0 18px;color:var(--ink2)">Envíe planos, fotos o preguntas: hablará con quien diseña y pone en marcha el sistema.</p>
    <a class="btn dark" style="display:block;text-align:center" href="{TEL}">+34 608 266 620</a></aside>
</div></section>
{faq_html(d["faq"], 'Preguntas frecuentes')}
<section class="sec sand"><div class="wrap"><h2 class="h2 s" style="margin-bottom:44px">Otros servicios</h2><div class="cards">{''.join(f'<div><p class="num">{j+1:02d}</p><h3><a href="/es/servicios/{o["slug"]}/">{e(o["title"])}</a></h3><p>{e(o["short"])}</p></div>' for j, o in others)}</div></div></section>
"""
    ld = [crumbs_ld([('/es/', 'Inicio'), ('/es/servicios/', 'Servicios'), (path, d['title'])]),
          {"@type": "Service", "name": d['h1'], "serviceType": d['title'], "description": d['meta'], "provider": {"@id": SITE + "/#business"}, "areaServed": {"@type": "Place", "name": "Marbella y Costa del Sol"}, "url": SITE + path, "inLanguage": "es"},
          faq_ld(d['faq'])]
    PAGES.append(page(path, f'{d["h1"]} | Scanditech', d['meta'], body, '/es/servicios/', lang='es', ld=ld, alternates=[('en', f'/services/{d["en"]}/'), ('es', path)]))

es_contact = contact.replace('Send a message, or just call. You will reach us, not a call centre.', 'Escríbanos o llámenos. Hablará con nosotros, no con un call center.') \
  .replace('>Contact<', '>Contacto<').replace('Fastest', 'Lo más rápido').replace('send plans, photos, questions', 'envíe planos, fotos y preguntas') \
  .replace('>Direct<', '>Directo<').replace('Call or text', 'Llamar o SMS').replace('Mon–Fri', 'lun–vie') \
  .replace('Or write to us', 'O escríbanos').replace('Thank you — your enquiry has been sent. We usually reply within one working day.', 'Gracias, hemos recibido su consulta. Normalmente respondemos en un día laborable.') \
  .replace('<span>Name</span>', '<span>Nombre</span>').replace('<span>Phone</span>', '<span>Teléfono</span>').replace('About the project', 'Sobre el proyecto') \
  .replace('Send enquiry', 'Enviar consulta').replace('Or email', 'O escriba a').replace('directly.', 'directamente.').replace('>Office<', '>Oficina<') \
  .replace('Spain</address>', 'España</address>').replace('Open in Google Maps', 'Abrir en Google Maps').replace('name="website"', 'name="website"').replace('<form class="form" method="post" action="/enquiry.php">', '<form class="form" method="post" action="/enquiry.php"><input type="hidden" name="lang" value="es">')
PAGES.append(page('/es/contacto/', 'Contacto – Domótica KNX en Marbella | Scanditech',
                  'Contacte con Scanditech, integrador KNX en Marbella: WhatsApp +45 20 90 30 50, teléfono +34 608 266 620 o formulario. Oficina en Avenida Ricardo Soriano.',
                  es_contact, '/es/contacto/', lang='es', ld=[crumbs_ld([('/es/', 'Inicio'), ('/es/contacto/', 'Contacto')])], alternates=[('en', '/contact/'), ('es', '/es/contacto/')]))

# ---------------------------------------------------------------- language landing pages
LANDING = {
 'da': dict(title='KNX smart home i Marbella – dansktalende | Scanditech',
            desc='Dansktalende KNX-ingeniør i Marbella. Vi designer, programmerer og vedligeholder smart home-systemer til villaer på Costa del Sol: lys, klima, solafskærmning, sikkerhed og energi.',
            eyebrow='KNX smart home · Marbella · Costa del Sol', h1='Smart home til din villa i Marbella – på dansk.',
            lead='Vi designer, programmerer og vedligeholder KNX-systemer til villaer og byggeprojekter i Marbella: lys, klima, solafskærmning, sikkerhed og energi samlet i ét roligt system.',
            blocks=[('Åben standard', 'KNX er en åben, international standard med hundredvis af producenter. Dit hus er ikke afhængigt af ét mærke eller en fremmed cloud.'),
                    ('Når du ikke er hjemme', 'Mange af vores kunder bor i Spanien en del af året. Feriemodus, lækagesikring, tilstedeværelsessimulering og fjernadgang gør, at huset passer sig selv.'),
                    ('Fuld dokumentation', 'Alle projekter afleveres med ETS-projektfil og as-built tegninger. Skifter du installatør, kan den næste overtage uden problemer.'),
                    ('Eksisterende anlæg', 'Vi gennemgår og overtager eksisterende KNX-installationer uden dokumentation – også når den oprindelige installatør er forsvundet.')],
            svc='Ydelser', cta='Skriv til os på WhatsApp', more='Se alle ydelser (på engelsk)', call='Ring'),
 'sv': dict(title='KNX smarta hem i Marbella – svensktalande | Scanditech',
            desc='Svensktalande KNX-tekniker i Marbella. Vi designar, programmerar och underhåller smarta hem för villor på Costa del Sol: belysning, klimat, solskydd, säkerhet och energi.',
            eyebrow='KNX smarta hem · Marbella · Costa del Sol', h1='Smarta hem för din villa i Marbella – på svenska.',
            lead='Vi designar, programmerar och underhåller KNX-system för villor och byggprojekt i Marbella: belysning, klimat, solskydd, säkerhet och energi i ett och samma lugna system.',
            blocks=[('Öppen standard', 'KNX är en öppen, internationell standard med hundratals tillverkare. Ditt hus är inte beroende av ett enda märke eller någon annans moln.'),
                    ('När du inte är på plats', 'Många av våra kunder bor i Spanien delar av året. Semesterläge, läckageskydd, närvarosimulering och fjärråtkomst gör att huset sköter sig självt.'),
                    ('Full dokumentation', 'Varje projekt lämnas över med ETS-projektfil och relationsritningar. Byter du installatör kan nästa ta över utan problem.'),
                    ('Befintliga anläggningar', 'Vi går igenom och tar över befintliga KNX-installationer utan dokumentation – även när den ursprungliga installatören inte längre finns.')],
            svc='Tjänster', cta='Skriv till oss på WhatsApp', more='Se alla tjänster (på engelska)', call='Ring'),
}
for lang, L in LANDING.items():
    body = f'''
<section class="hero" style="height:560px">
  <img src="/images/hero-villa.jpg" alt="Villa i Marbella / Villa i Marbella" width="1600" height="900">
  <div class="wrap"><div class="in"><p class="eyebrow">{L["eyebrow"]}</p><h1 style="font-size:60px">{L["h1"]}</h1><p class="sub">{L["lead"]}</p>
  <div class="btns"><a class="btn light" href="{WA}" rel="noopener">{L["cta"]}</a><a class="btn ghost-l" href="{TEL}">{L["call"]} +34 608 266 620</a></div></div></div>
</section>
<section class="sec"><div class="wrap"><div class="cards">{''.join(f'<div><h2 style="font-size:19px;font-weight:500;margin:0 0 12px">{t}</h2><p>{b}</p></div>' for t, b in L["blocks"])}</div></div></section>
<section class="sec dark"><div class="wrap"><div class="cap-top"><h2 class="h2 s">{L["svc"]}</h2><a href="/services/">{L["more"]} →</a></div>{cap_grid()}</div></section>
'''
    PAGES.append(page(f'/{lang}/', L['title'], L['desc'], body, '', lang=lang, alternates=LANGS))

# ---------------------------------------------------------------- 404, enquiry, robots, sitemap, htaccess
page('/404.html', 'Page not found | Scanditech', 'The page you were looking for does not exist.',
     '<section class="phead"><div class="wrap"><p class="eyebrow">404</p><h1>This page does not exist.</h1><p class="lead">It may have moved. Start from the <a href="/" style="color:var(--brass)">home page</a> or look at our <a href="/services/" style="color:var(--brass)">services</a>.</p></div></section>')

open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nDisallow: /enquiry.php\nDisallow: /deploy.php\n\nSitemap: {SITE}/sitemap.xml\n')
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'  <url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod><priority>{"1.0" if p == "/" else "0.8" if p.count("/") <= 2 else "0.7"}</priority></url>\n' for p in PAGES) + '</urlset>\n'
open(os.path.join(OUT, 'sitemap.xml'), 'w').write(sm)

open(os.path.join(OUT, '.htaccess'), 'w').write('''# Scanditech
Options -Indexes
DirectoryIndex index.html index.php
ErrorDocument 404 /404.html
<IfModule mod_rewrite.c>
RewriteEngine On
# force https + bare domain
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} ^www\\. [NC]
RewriteRule ^ https://scanditech.es%{REQUEST_URI} [L,R=301]
# add trailing slash to directories
RewriteCond %{REQUEST_FILENAME} -d
RewriteRule ^(.+[^/])$ /$1/ [L,R=301]
# old one-page anchors / index.html
RewriteRule ^index\\.html$ / [L,R=301]
</IfModule>
<IfModule mod_headers.c>
Header set X-Content-Type-Options "nosniff"
Header set Referrer-Policy "strict-origin-when-cross-origin"
<FilesMatch "\\.(woff2|jpg|jpeg|png|webp|svg)$">
Header set Cache-Control "public, max-age=31536000, immutable"
</FilesMatch>
<FilesMatch "\\.(css|js)$">
Header set Cache-Control "public, max-age=2592000"
</FilesMatch>
</IfModule>
<IfModule mod_deflate.c>
AddOutputFilterByType DEFLATE text/html text/css application/javascript image/svg+xml application/xml text/plain
</IfModule>
''')

open(os.path.join(OUT, 'enquiry.php'), 'w').write(r'''<?php
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
''')

print(len(PAGES), 'pages')
for p in PAGES: print(' ', p)
