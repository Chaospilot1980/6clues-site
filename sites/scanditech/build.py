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
CSSV = '6'
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
  dict(slug='lighting-control', title='Lighting Control', h1='Lighting control systems and scene design for Marbella villas',
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
VALUES = [('Discreet by default', 'We never publish client names, addresses or photos of their homes, and we sign an NDA on request. Our clients value privacy; so do we.'),
          ('Open systems only', "KNX and other open standards. Your house should not depend on one manufacturer's cloud, or on us being the only ones who can maintain it."),
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
GA_ID = 'G-S3EFCCVQCF'  # GA4 property scanditech.es
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
  <div class="wrap"><div class="base"><span>© {datetime.date.today().year} Scandinavian Technical Solutions S.L. · CIF B44771731 · EU VAT ESB44771731</span><span>{T["foot"]} · {"Discreción por defecto" if lang == "es" else "Discreet by default"}</span></div></div>
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



DISC = {'en': {'eb': 'Discretion', 'h': 'Your home stays <em>yours.</em>', 'intro': 'Many of our clients would rather nobody knew what their house can do, or who lives in it. We treat that as a matter of honour, not a line in a policy.', 'items': [('No names, no addresses', 'We never publish who we work for or where. Not on our website, not on social media, not in conversation with other clients.'), ('No photos of your home', 'What we show is hardware and craft: boards, keypads, details. Never your house, your garden or your view.'), ('Confidentiality in writing', 'We are happy to sign a non-disclosure agreement before the first site visit.'), ('Your data stays in the house', 'The system runs locally. No cloud account in our name, and remote support only when you allow it.'), ('Documentation belongs to you', 'The ETS project, drawings and access codes are handed over to you, not held back.')], 'seal': 'Discreet by default'}, 'es': {'eb': 'Discreción', 'h': 'Su casa sigue siendo <em>suya.</em>', 'intro': 'Muchos de nuestros clientes prefieren que nadie sepa lo que su casa puede hacer, ni quién vive en ella. Para nosotros es una cuestión de honor, no una cláusula.', 'items': [('Sin nombres ni direcciones', 'Nunca publicamos para quién trabajamos ni dónde. Ni en la web, ni en redes sociales, ni en conversaciones con otros clientes.'), ('Sin fotos de su casa', 'Lo que mostramos es técnica y oficio: cuadros, pulsadores, detalles. Nunca su casa, su jardín ni sus vistas.'), ('Confidencialidad por escrito', 'Firmamos un acuerdo de confidencialidad antes de la primera visita, si lo desea.'), ('Sus datos se quedan en casa', 'El sistema funciona en local. Sin cuentas en la nube a nuestro nombre y con soporte remoto solo cuando usted lo autoriza.'), ('La documentación es suya', 'El proyecto ETS, los planos y los códigos de acceso se le entregan a usted.')], 'seal': 'Discreción por defecto'}}
CRAFT = {'en': {'eb': 'The craft', 'h': 'Hardware up close. <em>Never your house.</em>', 'note': 'We show the work, not the homes: panels, boards and keypads from manufacturers we trust.', 'caps': ['Basalte · keypad', 'Tense · keypad', 'Hager · KNX board', 'Home Assistant · visualisation'], 'more': 'Why these components →', 'link': '/services/#technologies'}, 'es': {'eb': 'El oficio', 'h': 'La técnica de cerca. <em>Nunca su casa.</em>', 'note': 'Mostramos el trabajo, no las casas: pulsadores, cuadros y pantallas de fabricantes en los que confiamos.', 'caps': ['Basalte · pulsador', 'Tense · pulsador', 'Hager · cuadro KNX', 'Home Assistant · visualización'], 'more': 'Por qué estos componentes →', 'link': '/services/#technologies'}}

def disc_html(lang, num):
    d = DISC[lang]
    items = ''.join(f'<li><div><b>{e(t)}</b><span>{e(b)}</span></div></li>' for t, b in d['items'])
    return f"""<section class="sec dark" id="discretion"><div class="wrap disc">
  <div><p class="eyebrow">{num} · {d['eb']}</p><h2>{d['h']}</h2><p class="intro">{e(d['intro'])}</p><span class="seal">{d['seal']}</span></div>
  <ol>{items}</ol>
</div></section>"""

def craft_html(lang, num):
    c = CRAFT[lang]
    imgs = [('tech-basalte.jpg', c['caps'][0]), ('tech-tense.jpg', c['caps'][1]), ('tech-hager.jpg', c['caps'][2]), ('tech-homeassistant.jpg', c['caps'][3])]
    figs = ''.join(f'<figure><img src="/images/{f}" alt="{e(cap)}" loading="lazy" width="800" height="600"><figcaption>{e(cap)}</figcaption></figure>' for f, cap in imgs)
    doc = '<figure style="background:var(--graphite);display:flex;flex-direction:column;justify-content:flex-end;padding:22px"><span style="font-family:var(--serif);font-size:30px;line-height:1.1;color:var(--linen)">ETS + as-built</span><span style="font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--brass-l);margin-top:10px">' + ('Documented, always' if lang == 'en' else 'Siempre documentado') + '</span></figure>'
    return f"""<section class="sec"><div class="wrap">
  <div class="craft-note"><div><p class="eyebrow">{num} · {c['eb']}</p><h2 class="h2">{c['h']}</h2></div><p class="body">{e(c['note'])} <a href="{c['link']}" style="color:var(--brass-d)">{c['more']}</a></p></div>
  <div class="craft">{figs}{doc}</div>
</div></section>"""

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
    <p class="eyebrow">KNX home automation · Marbella · Costa del Sol</p>
    <h1>A house that understands<br><em>how you live in it.</em></h1>
    <p class="sub">We design, program and maintain KNX systems for private villas and developments in Marbella — light, climate, shade, security and energy, held together as one calm system.</p>
    <div class="btns"><a class="btn light" href="/contact/">Book a visit</a><a class="btn ghost-l" href="{WA}" rel="noopener">WhatsApp us</a></div>
    <div class="trust"><span>Open KNX standard</span><span>Fully documented</span><span>Discreet by default</span></div>
  </div></div>
</section>
<div class="wrap"><div class="stats">
  <div><b>KNX</b><span>Open standard, no vendor lock-in</span></div>
  <div><b>Marbella</b><span>Av. Ricardo Soriano, on the coast</span></div>
  <div><b>1:1</b><span>The designer commissions your system</span></div>
  <div><b>EN · SV · DA</b><span>Working languages</span></div>
</div></div>
<section class="sec"><div class="wrap split">
  <p class="eyebrow">01 · Our approach</p>
  <div>
    <h2 class="h2">Scandinavian precision, <em>Mediterranean living.</em></h2>
    <div class="cols2">
      <p class="body">Automation goes wrong when it is sold as gadgets. We start from the plans and the way the house is actually used — where you walk in at night, which terrace takes the afternoon sun, how the pool and the guest wing are managed when nobody is here.</p>
      <p class="body">Then we build it on <a href="/services/knx-design-programming/" style="border-bottom:1px solid rgba(168,122,69,.4)">KNX</a>: an open, vendor-neutral standard with three decades of installed base behind it. Nothing depends on one manufacturer staying in business, and every project leaves our hands fully documented.</p>
    </div>
  </div>
</div></section>
<section class="sec dark"><div class="wrap">
  <p class="eyebrow">02 · Services</p>
  <div class="cap-top"><h2 class="h2 s">Light, climate, shade. <em>One calm system.</em></h2><a href="/services/">All services →</a></div>
  {cap_grid()}
</div></section>
{craft_html('en', '03')}
{disc_html('en', '04')}
<section class="sec"><div class="wrap x2">
  <div class="xbox"><span class="big">Xcover</span><dl>
    <div><dt>Surface</dt><dd>Walkable, load-bearing</dd></div><div><dt>Level</dt><dd>Flush with the terrace</dd></div>
    <div><dt>Control</dt><dd>KNX · keypad · app</dd></div><div><dt>Status</dt><dd style="color:var(--brass-l)">Prototype</dd></div></dl></div>
  <div>
    <p class="eyebrow">05 · Our own product · In development</p>
    <h2 class="h2" style="font-size:52px;line-height:1.06">Xcover</h2>
    <p class="lead" style="font-size:18px;margin-top:26px">A smart, walkable pool covering. Closed, it is terrace you can stand on — safe around children and pets, and it gives back the square metres the pool takes up for nine months of the year. Open, it disappears.</p>
    <p class="body muted" style="margin-top:20px">Designed to be driven from the same KNX system as the rest of the house.</p>
    <div class="btns"><a class="btn dark" href="/xcover/">See the concept</a><a class="btn ghost" href="https://www.xcover.eu" rel="noopener">xcover.eu</a></div>
  </div>
</div></section>
<section class="sec sand"><div class="wrap">
  <p class="eyebrow">06 · Process</p>
  <h2 class="h2 s" style="margin-bottom:60px">How a project runs</h2>
  <div class="steps">{''.join(f'<div><p class="num">{n}</p><h3>{t}</h3><p>{b}</p></div>' for n, t, b in PROCESS)}</div>
  <div class="btns"><a class="btn dark" href="/contact/">Book a visit</a></div>
</div></section>
{faq_html(HOME_FAQ)}
'''
PAGES.append(page('/', 'Home Automation & KNX Smart Home in Marbella | Scanditech',
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
  <p class="lead">We work as the automation partner on new villas and renovations in Marbella and along the Costa del Sol, and as an independent consultant for architects, developers and other installers who need a second set of eyes on a KNX specification. Working in <a href="/areas/benahavis/" style="color:var(--brass-d)">Benahavís</a> , <a href="/areas/estepona/" style="color:var(--brass-d)">Estepona</a> or <a href="/areas/sotogrande/" style="color:var(--brass-d)">Sotogrande</a>? See our area pages.</p>
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
<section class="sec tight"><div class="wrap"><div class="cards" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr))">{''.join(f'<div><h3>{t}</h3><p>{b}</p></div>' for t, b in VALUES)}</div></div></section>
<section class="sec sand"><div class="wrap x2">
  <div><h2 class="h2 s" style="font-size:34px;margin-bottom:32px">Company details</h2>
  <dl class="rows">{''.join(f'<div><dt>{k}</dt><dd>{e(v)}</dd></div>' for k, v in COMPANY)}</dl></div>
  <div><h2 class="h2 s" style="font-size:34px;margin-bottom:32px">Where we work</h2>
  <p class="body">Our office is in central Marbella. We work on villas and developments along the Costa del Sol — Marbella, Nueva Andalucía, the Golden Mile, <a href="/areas/benahavis/" style="color:var(--brass-d)">Benahavís</a>, La Zagaleta, <a href="/areas/estepona/" style="color:var(--brass-d)">Estepona</a>, San Pedro de Alcántara, <a href="/areas/sotogrande/" style="color:var(--brass-d)">Sotogrande</a>, Mijas, Fuengirola and Málaga.</p>
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
        <p style="font-size:13.5px;line-height:1.7;color:var(--mute);margin:0">Everything you send us is treated in confidence. We are happy to sign an NDA before the first visit.</p>
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
    <div class="btns"><a class="btn light" href="/es/contacto/">Solicitar visita</a><a class="btn ghost-l" href="{WA}" rel="noopener">WhatsApp</a></div>
    <div class="trust"><span>Estándar KNX abierto</span><span>Totalmente documentado</span><span>Discreción por defecto</span></div>
  </div></div>
</section>
<div class="wrap"><div class="stats">
  <div><b>KNX</b><span>Estándar abierto, sin depender de una marca</span></div>
  <div><b>Marbella</b><span>Av. Ricardo Soriano</span></div>
  <div><b>1:1</b><span>Quien diseña, programa y pone en marcha</span></div>
  <div><b>ES · EN · SV · DA</b><span>Idiomas de trabajo</span></div>
</div></div>
<section class="sec"><div class="wrap split">
  <p class="eyebrow">01 · Nuestro enfoque</p>
  <div>
    <h2 class="h2">Precisión escandinava, <em>vida mediterránea.</em></h2>
    <div class="cols2">
      <p class="body">La domótica sale mal cuando se vende como un conjunto de aparatos. Nosotros empezamos por los planos y por cómo se vive la casa: por dónde entra de noche, qué terraza recibe el sol de la tarde, cómo se gestionan la piscina y la zona de invitados cuando no hay nadie.</p>
      <p class="body">Después lo construimos sobre <a href="/es/servicios/programacion-knx/" style="border-bottom:1px solid rgba(168,122,69,.4)">KNX</a>, un estándar abierto con más de treinta años de instalaciones. Nada depende de que un fabricante siga existiendo, y cada proyecto se entrega totalmente documentado.</p>
    </div>
  </div>
</div></section>
<section class="sec dark"><div class="wrap">
  <p class="eyebrow">02 · Servicios</p>
  <div class="cap-top"><h2 class="h2 s">Soluciones de domótica KNX. <em>Un solo sistema.</em></h2><a href="/es/servicios/">Todos los servicios →</a></div>
  {cap_grid_es()}
</div></section>
{craft_html('es', '03')}
{disc_html('es', '04')}
<section class="sec sand"><div class="wrap">
  <p class="eyebrow">05 · Proceso</p>
  <h2 class="h2 s" style="margin-bottom:60px">Cómo trabajamos</h2>
  <div class="steps">
    <div><p class="num">01</p><h3>Consulta</h3><p>Visita a la obra o llamada con sus planos. Le decimos qué merece la pena automatizar y qué no.</p></div>
    <div><p class="num">02</p><h3>Proyecto</h3><p>Topología, cuadros, listado de cargas y un alcance cerrado que su electricista puede presupuestar.</p></div>
    <div><p class="num">03</p><h3>Puesta en marcha</h3><p>Programación ETS, ajuste en obra de iluminación, persianas y clima, y explicación a la familia.</p></div>
    <div><p class="num">04</p><h3>Mantenimiento</h3><p>Documentación as-built, soporte remoto y cambios a medida que cambia la vida en la casa.</p></div>
  </div>
  <div class="btns"><a class="btn dark" href="/es/contacto/">Solicitar visita</a></div>
</div></section>
{faq_html(ES_FAQ, 'Preguntas frecuentes sobre domótica KNX')}
"""
PAGES.append(page('/es/', 'Domótica en Marbella – Instalador e integrador KNX | Scanditech',
                  'Domótica KNX en Marbella y la Costa del Sol. Integrador KNX: diseño, programación ETS y mantenimiento de instalaciones domóticas para villas. Iluminación, clima, persianas y seguridad.',
                  es_home, '/es/', lang='es', ld=[faq_ld(ES_FAQ)], alternates=ES_ALT_HOME, preload='/images/hero-villa.jpg'))

es_list = ''.join(f"""<div class="svc"><p class="num">{i+1:02d}</p><h2><a href="/es/servicios/{d['slug']}/">{e(d['title'])}</a></h2><div><p class="body" style="font-size:16.5px">{e(d['long'])}</p>
<ul class="tags">{''.join(f'<li>{e(t)}</li>' for t in d['tags'])}</ul><a class="go" href="/es/servicios/{d['slug']}/">Más información →</a></div></div>""" for i, d in enumerate(ES_SERVICES))
es_svc = f"""
<section class="phead"><div class="wrap">
  <p class="eyebrow">Servicios</p>
  <h1>Servicios de domótica KNX: un solo sistema para toda la casa.</h1>
  <p class="lead">Somos el integrador KNX en obra nueva y reformas en Marbella y la Costa del Sol, y consultores independientes para arquitectos, promotores e instaladores que necesitan revisar un proyecto KNX. Trabajamos en toda la costa, también en <a href="/es/zonas/benahavis/" style="color:var(--brass-d)">Benahavís</a>, <a href="/es/zonas/estepona/" style="color:var(--brass-d)">Estepona</a> y <a href="/es/zonas/sotogrande/" style="color:var(--brass-d)">Sotogrande</a>.</p>
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
  .replace('Send enquiry', 'Enviar consulta').replace('Everything you send us is treated in confidence. We are happy to sign an NDA before the first visit.', 'Todo lo que nos envíe se trata con total confidencialidad. Firmamos un acuerdo de confidencialidad antes de la primera visita si lo desea.').replace('Or email', 'O escriba a').replace('directly.', 'directamente.').replace('>Office<', '>Oficina<') \
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

# ---------------------------------------------------------------- area pages (EN /areas/<slug>/, ES /es/zonas/<slug>/)
AREAS = [
 dict(slug='benahavis', name='Benahavís',
  en=dict(title='Home Automation in Benahavís – KNX Smart Villas | Scanditech',
          desc='KNX home automation for villas in Benahavís, La Zagaleta, El Madroñal and Los Arqueros: lighting, climate, shading, security and remote access, from a Marbella-based engineer.',
          h1='Home automation in Benahavís.',
          lead='Benahavís is where many of the largest homes on the coast sit: hillside estates, several buildings on one plot, long distances between the gate, the main house and the pool house. That is exactly the kind of project where a well-designed KNX system pays for itself, and where a poorly documented one becomes a problem.',
          blocks=[('Large plots, one system', 'Main house, guest house, staff quarters, gatehouse and garden lighting on one KNX installation, with sensible line and area topology so the system stays fast and easy to extend.'),
                  ('Run from a distance', 'Many owners in La Zagaleta, El Madroñal and Los Arqueros are away for months at a time. Holiday mode, leak protection, presence simulation and secure remote access keep the house looked after.'),
                  ('Climate on a hillside', 'Sun on one façade, wind on another. Room-by-room climate, automated shading and weather-station logic keep a large villa comfortable without wasting energy.'),
                  ('Audits and takeovers', 'Bought a villa with an undocumented system? We audit, document and take over existing KNX installations, including ones where the original installer has disappeared.')],
          also='Nearby we also work in Marbella, Nueva Andalucía, the Golden Mile, Estepona and Sotogrande.',
          cta='Book a visit in Benahavís', faq=[
            ('Do you work in La Zagaleta and El Madroñal?', 'Yes. We work on villas throughout Benahavís, including gated communities such as La Zagaleta, El Madroñal, Los Arqueros and Monte Mayor, and we coordinate access with security and estate management.'),
            ('How far is Benahavís from your office?', 'Our office is in central Marbella, roughly 20–30 minutes away, so site visits and service calls are quick.'),
            ('Can you work alongside our architect and builder?', 'Yes. On new builds and major renovations we join early, specify the KNX system with the architect and electrician, and then programme and commission it ourselves.'),
            ('Is everything kept confidential?', 'Always. We do not publish client names, addresses or photos of your home, and we are happy to sign an NDA before the first visit.')]),
  es=dict(title='Domótica en Benahavís – Villas KNX | Scanditech',
          desc='Domótica KNX para villas en Benahavís, La Zagaleta, El Madroñal y Los Arqueros: iluminación, clima, persianas, seguridad y acceso remoto. Integrador KNX con oficina en Marbella.',
          h1='Domótica en Benahavís.',
          lead='En Benahavís están muchas de las viviendas más grandes de la costa: fincas en ladera, varios edificios en una misma parcela y largas distancias entre la entrada, la casa principal y la casa de la piscina. Es justo el tipo de proyecto en el que un buen sistema KNX se amortiza, y en el que uno mal documentado se convierte en un problema.',
          blocks=[('Parcelas grandes, un solo sistema', 'Casa principal, casa de invitados, zona de servicio, garita y alumbrado de jardín en una sola instalación KNX, con una topología de líneas y áreas pensada para que el sistema sea rápido y fácil de ampliar.'),
                  ('Control a distancia', 'Muchos propietarios de La Zagaleta, El Madroñal y Los Arqueros pasan meses fuera. Modo vacaciones, protección contra fugas, simulación de presencia y acceso remoto seguro mantienen la casa vigilada.'),
                  ('Clima en ladera', 'Sol en una fachada y viento en otra. Clima por estancias, persianas automatizadas y lógica de estación meteorológica para que una villa grande sea confortable sin derrochar energía.'),
                  ('Auditorías y traspasos', '¿Ha comprado una villa con un sistema sin documentar? Auditamos, documentamos y nos hacemos cargo de instalaciones KNX existentes, también cuando el instalador original ya no está.')],
          also='Cerca también trabajamos en Marbella, Nueva Andalucía, la Milla de Oro, Estepona y Sotogrande.',
          cta='Solicitar visita en Benahavís', faq=[
            ('¿Trabajan en La Zagaleta y El Madroñal?', 'Sí. Trabajamos en villas de todo Benahavís, incluidas urbanizaciones cerradas como La Zagaleta, El Madroñal, Los Arqueros y Monte Mayor, y coordinamos el acceso con seguridad y la administración.'),
            ('¿A qué distancia está Benahavís de su oficina?', 'Nuestra oficina está en el centro de Marbella, a unos 20–30 minutos, así que las visitas y el servicio técnico son rápidos.'),
            ('¿Pueden trabajar con nuestro arquitecto y constructor?', 'Sí. En obra nueva y reformas integrales entramos pronto, definimos el sistema KNX con el arquitecto y el electricista, y luego lo programamos y ponemos en marcha nosotros.'),
            ('¿Todo es confidencial?', 'Siempre. No publicamos nombres de clientes, direcciones ni fotos de su casa, y firmamos un acuerdo de confidencialidad antes de la primera visita si lo desea.')])),
 dict(slug='estepona', name='Estepona',
  en=dict(title='Home Automation in Estepona – KNX Smart Homes | Scanditech',
          desc='KNX home automation in Estepona, the New Golden Mile and Casares: new-build villas and apartments with lighting, climate, shading, security and remote access, from a Marbella-based KNX engineer.',
          h1='Home automation in Estepona.',
          lead='Estepona and the New Golden Mile are where much of the coast is being built right now: new villas, frontline apartments and complete developments. The best moment to plan a KNX system is before the walls are closed – and the second best is when you take over a home whose system nobody has documented.',
          blocks=[('New builds, planned properly', 'We join architects and electricians at drawing stage, specify the KNX system and cabling, and programme and commission it ourselves – so the house works the day you move in.'),
                  ('Apartments and penthouses', 'Compact KNX systems for lighting scenes, climate per room, motorised blinds and a single calm keypad per room – designed to fit community rules and existing wiring.'),
                  ('Sea-front climate', 'Salt air, strong sun and wind from the sea. Automated shading, weather-station logic and room-by-room climate keep a frontline home comfortable and efficient.'),
                  ('Developer support', 'Independent KNX specification and quality checks for developers in Estepona who want a system that buyers can actually use and maintain.')],
          also='Nearby we also work in Marbella, San Pedro de Alcántara, Benahavís, Casares and Sotogrande.',
          cta='Book a visit in Estepona', faq=[
            ('Do you work in Estepona and the New Golden Mile?', 'Yes. We work throughout Estepona, the New Golden Mile and Casares, on new builds, renovations and existing KNX systems.'),
            ('Can KNX be added to a new-build apartment?', 'Usually yes. The earlier we are involved, the better – ideally before the electrical installation is finished – but compact systems can also be added to existing apartments.'),
            ('Do you work for developers?', 'Yes. We specify KNX systems, review installers\' work and commission systems for small and mid-size developments.'),
            ('Is everything kept confidential?', 'Always. We never publish client names, addresses or photos of your home, and we sign an NDA on request.')]),
  es=dict(title='Domótica en Estepona – Viviendas KNX | Scanditech',
          desc='Domótica KNX en Estepona, la Nueva Milla de Oro y Casares: villas y apartamentos de obra nueva con iluminación, clima, persianas, seguridad y acceso remoto. Integrador KNX con oficina en Marbella.',
          h1='Domótica en Estepona.',
          lead='En Estepona y la Nueva Milla de Oro se construye buena parte de la costa: villas nuevas, apartamentos en primera línea y promociones completas. El mejor momento para planificar un sistema KNX es antes de cerrar las paredes; el segundo mejor, cuando se hace cargo de una vivienda cuyo sistema nadie ha documentado.',
          blocks=[('Obra nueva, bien planificada', 'Entramos con el arquitecto y el electricista en fase de proyecto, definimos el sistema KNX y el cableado, y lo programamos y ponemos en marcha nosotros, para que la casa funcione el día de la mudanza.'),
                  ('Apartamentos y áticos', 'Sistemas KNX compactos para escenas de iluminación, clima por estancias, persianas motorizadas y un único pulsador elegante por estancia, adaptados a las normas de la comunidad.'),
                  ('Clima en primera línea', 'Aire salino, sol intenso y viento del mar. Persianas automatizadas, estación meteorológica y clima por estancias para una vivienda confortable y eficiente.'),
                  ('Apoyo a promotores', 'Especificación KNX independiente y control de calidad para promotores en Estepona que quieren un sistema que el comprador pueda usar y mantener.')],
          also='Cerca también trabajamos en Marbella, San Pedro de Alcántara, Benahavís, Casares y Sotogrande.',
          cta='Solicitar visita en Estepona', faq=[
            ('¿Trabajan en Estepona y la Nueva Milla de Oro?', 'Sí. Trabajamos en todo Estepona, la Nueva Milla de Oro y Casares, en obra nueva, reformas y sistemas KNX existentes.'),
            ('¿Se puede instalar KNX en un apartamento de obra nueva?', 'Normalmente sí. Cuanto antes entremos, mejor (idealmente antes de terminar la instalación eléctrica), pero también se pueden añadir sistemas compactos a apartamentos existentes.'),
            ('¿Trabajan para promotores?', 'Sí. Especificamos sistemas KNX, revisamos el trabajo de instaladores y ponemos en marcha sistemas para promociones pequeñas y medianas.'),
            ('¿Todo es confidencial?', 'Siempre. Nunca publicamos nombres de clientes, direcciones ni fotos de su casa, y firmamos un acuerdo de confidencialidad si lo desea.')])),
 dict(slug='sotogrande', name='Sotogrande',
  en=dict(title='Home Automation in Sotogrande – KNX Villas | Scanditech',
          desc='KNX home automation in Sotogrande, La Reserva, Valderrama and the Marina: lighting, climate, shading, security and remote access for large villas and second homes, from a Marbella-based KNX engineer.',
          h1='Home automation in Sotogrande.',
          lead='Sotogrande is quieter than Marbella and the homes are often larger: wide plots, separate guest houses, staff quarters and owners who spend part of the year elsewhere. A KNX system here has to run for months on its own – and has to be documented well enough that the next technician understands it.',
          blocks=[('Second homes that look after themselves', 'Holiday mode, leak protection, frost and humidity control, presence simulation and secure remote access – so the house is ready when you arrive and safe while you are away.'),
                  ('Large plots, one system', 'Main house, guest house, staff quarters, gatehouse and garden on one KNX installation with a clean topology, so it stays fast and easy to extend.'),
                  ('Golf, polo and sea views', 'Automated shading and lighting scenes that follow the sun, and climate that adapts to an open-plan house facing the course or the sea.'),
                  ('Takeovers and audits', 'Many homes in Sotogrande have KNX systems installed years ago. We audit, document and take over existing installations, including undocumented ones.')],
          also='Nearby we also work in Estepona, Casares, San Roque, Benahavís and Marbella.',
          cta='Book a visit in Sotogrande', faq=[
            ('Do you work in Sotogrande?', 'Yes. We work throughout Sotogrande – Sotogrande Alto, La Reserva, Valderrama, Almenara and the Marina – and the surrounding area.'),
            ('Can you look after a house we only use part of the year?', 'Yes. We set up remote monitoring and alarms (with your permission) and can visit for service and seasonal checks.'),
            ('Can you take over a KNX system another installer put in?', 'Yes. We audit the installation, recover or rebuild the ETS project and document everything before making changes.'),
            ('Is everything kept confidential?', 'Always. We never publish client names, addresses or photos of your home, and we sign an NDA on request.')]),
  es=dict(title='Domótica en Sotogrande – Villas KNX | Scanditech',
          desc='Domótica KNX en Sotogrande, La Reserva, Valderrama y la Marina: iluminación, clima, persianas, seguridad y acceso remoto para villas y segundas residencias. Integrador KNX con oficina en Marbella.',
          h1='Domótica en Sotogrande.',
          lead='Sotogrande es más tranquilo que Marbella y las viviendas suelen ser más grandes: parcelas amplias, casas de invitados, zona de servicio y propietarios que pasan parte del año fuera. Aquí un sistema KNX tiene que funcionar solo durante meses y estar documentado para que el siguiente técnico lo entienda.',
          blocks=[('Segundas residencias que se cuidan solas', 'Modo vacaciones, protección contra fugas, control de heladas y humedad, simulación de presencia y acceso remoto seguro, para que la casa esté lista cuando llegue y protegida mientras está fuera.'),
                  ('Parcelas grandes, un solo sistema', 'Casa principal, casa de invitados, zona de servicio, garita y jardín en una sola instalación KNX con una topología limpia, rápida y fácil de ampliar.'),
                  ('Golf, polo y vistas al mar', 'Persianas automatizadas y escenas de iluminación que siguen al sol, y un clima que se adapta a una casa abierta hacia el campo o el mar.'),
                  ('Traspasos y auditorías', 'Muchas viviendas de Sotogrande tienen sistemas KNX instalados hace años. Auditamos, documentamos y nos hacemos cargo de instalaciones existentes, también sin documentar.')],
          also='Cerca también trabajamos en Estepona, Casares, San Roque, Benahavís y Marbella.',
          cta='Solicitar visita en Sotogrande', faq=[
            ('¿Trabajan en Sotogrande?', 'Sí. Trabajamos en todo Sotogrande (Sotogrande Alto, La Reserva, Valderrama, Almenara y la Marina) y alrededores.'),
            ('¿Pueden ocuparse de una casa que solo usamos parte del año?', 'Sí. Configuramos supervisión remota y alarmas (con su permiso) y podemos hacer visitas de mantenimiento y revisiones de temporada.'),
            ('¿Pueden hacerse cargo de un sistema KNX de otro instalador?', 'Sí. Auditamos la instalación, recuperamos o reconstruimos el proyecto ETS y lo documentamos todo antes de hacer cambios.'),
            ('¿Todo es confidencial?', 'Siempre. Nunca publicamos nombres de clientes, direcciones ni fotos de su casa, y firmamos un acuerdo de confidencialidad si lo desea.')])),
]
for A in AREAS:
    for lang in ('en', 'es'):
        L = A[lang]
        path = f'/areas/{A["slug"]}/' if lang == 'en' else f'/es/zonas/{A["slug"]}/'
        alts = [('en', f'/areas/{A["slug"]}/'), ('es', f'/es/zonas/{A["slug"]}/')]
        home, svc, contact_u = ('/', '/services/', '/contact/') if lang == 'en' else ('/es/', '/es/servicios/', '/es/contacto/')
        lbl = ('Home', 'Areas') if lang == 'en' else ('Inicio', 'Zonas')
        grid = cap_grid() if lang == 'en' else cap_grid_es()
        body = f"""
<section class="phead"><div class="wrap">
  <p class="crumbs"><a href="{home}">{lbl[0]}</a> / {lbl[1]} / {e(A['name'])}</p>
  <h1>{e(L['h1'])}</h1>
  <p class="lead">{e(L['lead'])}</p>
</div></section>
<section class="sec tight"><div class="wrap"><div class="cards">{''.join(f'<div><h2 style="font-size:19px;font-weight:500;margin:0 0 12px">{e(t)}</h2><p>{e(b)}</p></div>' for t, b in L['blocks'])}</div>
<div class="btns"><a class="btn dark" href="{contact_u}">{e(L['cta'])}</a><a class="btn ghost" href="{WA}" rel="noopener">WhatsApp</a></div></div></section>
{disc_html(lang, '02')}
<section class="sec"><div class="wrap"><div class="cap-top"><h2 class="h2 s">{'Services' if lang == 'en' else 'Servicios'}</h2><a href="{svc}">{'All services' if lang == 'en' else 'Todos los servicios'} →</a></div>{grid}
<p class="body muted" style="margin-top:40px">{e(L['also'])}</p></div></section>
{faq_html(L['faq'], 'Questions we are often asked' if lang == 'en' else 'Preguntas frecuentes')}
"""
        ld = [crumbs_ld([(home, lbl[0]), (path, A['name'])]), faq_ld(L['faq']),
              {"@type": "Service", "name": L['h1'].rstrip('.'), "serviceType": "KNX home automation", "provider": {"@id": SITE + "/#business"},
               "areaServed": {"@type": "Place", "name": A['name'] + ', Málaga, Spain'}, "url": SITE + path, "inLanguage": lang}]
        PAGES.append(page(path, L['title'], L['desc'], body, svc, lang=lang, ld=ld, alternates=alts))

# ---------------------------------------------------------------- 404, enquiry, robots, sitemap, htaccess
page('/404.html', 'Page not found | Scanditech', 'The page you were looking for does not exist.',
     '<section class="phead"><div class="wrap"><p class="eyebrow">404</p><h1>This page does not exist.</h1><p class="lead">It may have moved. Start from the <a href="/" style="color:var(--brass)">home page</a> or look at our <a href="/services/" style="color:var(--brass)">services</a>.</p></div></section>')

llms = f"""# Scanditech – KNX home automation in Marbella (scanditech.es)

> Scandinavian Technical Solutions S.L. (Scanditech) is a small KNX engineering practice in Marbella, Spain (Av. Ricardo Soriano 72, 29601 Marbella). It designs, programs (ETS), commissions and maintains KNX smart-home systems for villas and developments on the Costa del Sol: lighting control, climate/HVAC, shading and blinds, security and access, energy monitoring and pool automation. It also audits and takes over undocumented KNX installations. Languages: English, Spanish, Danish, Swedish. Known for discretion: no client names, addresses or photos of homes are published; NDA on request; systems run locally with remote access only with the owner's permission.

## Areas served
Marbella, Nueva Andalucía, the Golden Mile, Benahavís (La Zagaleta, El Madroñal, Los Arqueros), Estepona, San Pedro de Alcántara, Sotogrande, Mijas, Fuengirola, Málaga.

## Key pages
- [Home (EN)]({SITE}/): KNX smart home automation in Marbella
- [Inicio (ES)]({SITE}/es/): domótica KNX en Marbella, integrador KNX
- [Services]({SITE}/services/)
""" + ''.join(f"- [{s['title']}]({SITE}/services/{s['slug']}/): {s['short']}\n" for s in SERVICES) + ''.join(f"- [{A['name']} (EN)]({SITE}/areas/{A['slug']}/) · [{A['name']} (ES)]({SITE}/es/zonas/{A['slug']}/)\n" for A in AREAS) + f"""- [About]({SITE}/about/)
- [Contact]({SITE}/contact/): WhatsApp +45 20 90 30 50, phone +34 608 266 620, dnh@scanditech.es
"""
open(os.path.join(OUT, 'llms.txt'), 'w').write(llms)

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
''')

print(len(PAGES), 'pages')
for p in PAGES: print(' ', p)
