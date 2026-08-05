from __future__ import annotations

import json
from dataclasses import dataclass
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-06-01"


@dataclass
class Section:
    title: str
    body: str
    bullets: list[str]


@dataclass
class Article:
    slug: str
    title: str
    meta_title: str
    description: str
    kicker: str
    hero: str
    hero_alt: str
    intro: str
    image_stem: str
    sections: list[Section]
    steps: list[tuple[str, str, str]]
    faqs: list[tuple[str, str]]
    related: list[tuple[str, str, str]]

    @property
    def url_path(self) -> str:
        return f"/it-wissen/{self.slug}.html"


ARTICLES = [
    Article(
        slug="it-service-leipzig-anbieter-vergleichen",
        title="IT-Service in Leipzig vergleichen",
        meta_title="IT-Service Leipzig vergleichen: Anbieter richtig bewerten | UKNS",
        description="Woran Sie einen guten IT-Service in Leipzig erkennen: klare Abläufe, ehrliche Preise, Sicherheit, Reaktionszeit und passende Betreuung statt reiner Werbeversprechen.",
        kicker="Ratgeber für Firmenkunden",
        hero="Woran Sie merken, ob ein IT-Dienstleister wirklich zu Ihrem Unternehmen passt",
        hero_alt="IT-Service Anbieter in Leipzig vergleichen",
        intro=(
            "Viele IT-Websites klingen auf den ersten Blick ähnlich: schnell, sicher, zuverlässig. "
            "Entscheidend ist aber, was im Alltag passiert, wenn Montagmorgen niemand auf den Server kommt, "
            "ein neues Notebook eingerichtet werden muss oder eine Geschäftsführung endlich wissen möchte, ob die Backups wirklich funktionieren."
        ),
        image_stem="it-service-leipzig-team",
        sections=[
            Section(
                "Nicht das größte Versprechen zählt, sondern der nächste klare Schritt",
                (
                    "Ein guter Anbieter nimmt Ihr Problem ernst, ohne es sofort größer zu machen als nötig. "
                    "Sie sollten nach dem ersten Gespräch wissen, was geprüft wird, welche Risiken dringend sind und welche Themen warten können."
                ),
                [
                    "Gibt es eine verständliche Ersteinschätzung, bevor Aufwand entsteht?",
                    "Wer entscheidet, ob Fernwartung reicht oder ein Vor-Ort-Termin sinnvoller ist?",
                    "Wird erklärt, was gemacht wurde, oder bleibt alles eine technische Blackbox?",
                ],
            ),
            Section(
                "Managed Services müssen zum Betrieb passen",
                (
                    "Monitoring, Patchmanagement und Helpdesk klingen gut. Für ein kleines Leipziger Büro mit acht Arbeitsplätzen "
                    "braucht es aber andere Abläufe als für einen Produktionsbetrieb mit Schichtbetrieb. Gute IT-Betreuung fühlt sich nicht wie ein Paket von der Stange an."
                ),
                [
                    "Welche Systeme sind geschäftskritisch und brauchen zuerst Schutz?",
                    "Wie werden Updates geplant, damit sie nicht mitten im Tagesgeschäft stören?",
                    "Welche Reaktionszeit ist realistisch und wirtschaftlich sinnvoll?",
                ],
            ),
            Section(
                "Sicherheit ist mehr als Antivirus",
                (
                    "Viele Wettbewerber sprechen über Cybersecurity. Wichtig ist, ob daraus konkrete Routinen werden: MFA, Backup-Tests, "
                    "Benutzerrechte, Dokumentation und ein Notfallplan, den im Ernstfall auch jemand findet."
                ),
                [
                    "Wer prüft regelmäßig, ob Backups wiederherstellbar sind?",
                    "Sind Admin-Zugänge, Passwörter und Fernwartung sauber geregelt?",
                    "Gibt es eine kurze Notfallliste für Ausfall, Verschlüsselung oder Datenverlust?",
                ],
            ),
        ],
        steps=[
            ("01", "Ausgangslage klären", "Wir fragen zuerst nach Arbeitsalltag, Risiken und aktuellen Schmerzen, nicht nur nach Hardwaredaten."),
            ("02", "Prioritäten sortieren", "Was blockiert sofort? Was ist ein Sicherheitsrisiko? Was kann geplant verbessert werden?"),
            ("03", "Sauber übergeben", "Nach der Umsetzung bekommen Sie verständliche Empfehlungen statt loser Fachbegriffe."),
        ],
        faqs=[
            (
                "Woran erkenne ich einen guten IT-Dienstleister in Leipzig?",
                "An klaren Abläufen, nachvollziehbarer Kommunikation, sauberer Dokumentation und der Bereitschaft, auch unbequeme Prioritäten ehrlich anzusprechen.",
            ),
            (
                "Sollte ich nach Stundensatz oder Pauschale entscheiden?",
                "Beides kann sinnvoll sein. Für einzelne Probleme ist ein transparenter Stundensatz fair, für laufende Betreuung sind feste Zuständigkeiten und Reaktionszeiten oft wichtiger.",
            ),
            (
                "Muss ein IT-Anbieter immer vor Ort sein?",
                "Nein. Viele Themen lassen sich per Fernwartung schnell lösen. Vor Ort ist wichtig, wenn Hardware, Verkabelung, WLAN-Ausleuchtung oder persönliche Übergabe entscheidend sind.",
            ),
        ],
        related=[
            ("/it-service-leipzig/", "IT-Service Leipzig", "Unsere zentrale Leistungsseite für Firmenkunden."),
            ("/managed-services-leipzig/", "Managed Services", "Laufende Betreuung statt reiner Feuerwehr-Einsätze."),
            ("/it-notfallplan-unternehmen-leipzig/", "IT-Notfallplan", "Was im Ernstfall in den ersten Minuten zählt."),
        ],
    ),
    Article(
        slug="it-betreuung-kleine-firmen-leipzig-praxis",
        title="IT-Betreuung für kleine Firmen in Leipzig",
        meta_title="IT-Betreuung für kleine Firmen Leipzig: praxisnah erklärt | UKNS",
        description="Praxisnaher Ratgeber für kleine Firmen in Leipzig: Welche IT-Betreuung wirklich hilft, wie Prioritäten entstehen und wann laufender Support sinnvoll ist.",
        kicker="Aus dem Alltag kleiner Unternehmen",
        hero="Wenn IT nicht Ihr Kerngeschäft ist, darf sie trotzdem nicht jeden Tag stören",
        hero_alt="IT-Betreuung für kleine Firmen in Leipzig",
        intro=(
            "In kleinen Unternehmen gibt es selten eine eigene IT-Abteilung. Trotzdem hängen Angebote, Buchhaltung, Kundentermine, E-Mail, WLAN und Datensicherung an derselben Technik. "
            "Gute Betreuung heißt deshalb: Probleme verständlich machen, Reihenfolge schaffen und die Dinge so einrichten, dass Ihr Team arbeiten kann."
        ),
        image_stem="IT-Analyse-Leipzig-Team",
        sections=[
            Section(
                "Typische Situationen, in denen Hilfe zu spät kommt",
                (
                    "Viele Firmen melden sich erst, wenn etwas steht. Das ist menschlich, aber teuer: Dann muss gleichzeitig analysiert, repariert und beruhigt werden. "
                    "Besser ist eine kleine, realistische Grundordnung."
                ),
                [
                    "Neue Mitarbeitende bekommen Geräte und Zugänge erst am ersten Arbeitstag.",
                    "Backups laufen angeblich, wurden aber nie testweise zurückgespielt.",
                    "Passwörter, Lizenzen und Admin-Zugänge liegen bei verschiedenen Personen.",
                ],
            ),
            Section(
                "Was zuerst stabil sein sollte",
                (
                    "Nicht jede Firma braucht sofort ein großes IT-Projekt. Meist reichen die richtigen ersten Schritte: sichere Konten, funktionierende Updates, klare Zuständigkeiten und ein Backup, das wirklich rettet."
                ),
                [
                    "Microsoft 365, E-Mail und MFA sauber einrichten.",
                    "Arbeitsplätze standardisieren, damit Support schneller geht.",
                    "WLAN, Firewall und Netzwerk so dokumentieren, dass niemand raten muss.",
                ],
            ),
            Section(
                "Menschliche IT-Betreuung heißt auch: erklären",
                (
                    "Ein Team hält sich eher an Sicherheitsregeln, wenn es versteht, warum sie existieren. Darum erklären wir lieber kurz und konkret, statt nur Verbote auszusprechen."
                ),
                [
                    "Warum MFA nervt, aber Konten schützt.",
                    "Warum Updates geplant werden und nicht einfach irgendwann laufen.",
                    "Warum ein kurzer Anruf manchmal besser ist als drei Tage Selbstversuch.",
                ],
            ),
        ],
        steps=[
            ("01", "Bestandsaufnahme", "Welche Geräte, Konten, Lizenzen, Backups und Risiken gibt es wirklich?"),
            ("02", "Sofortmaßnahmen", "Wir schließen die Lücken, die den Betrieb oder die Sicherheit am stärksten gefährden."),
            ("03", "Betreuungsrhythmus", "Danach entscheiden wir gemeinsam, ob Wartung, Helpdesk oder Projektarbeit sinnvoll ist."),
        ],
        faqs=[
            (
                "Ab wann lohnt sich laufende IT-Betreuung?",
                "Sobald Ausfälle regelmäßig Zeit kosten oder mehrere Menschen von denselben Systemen abhängig sind. Oft reicht schon ein kleiner Wartungsrhythmus, um Chaos zu vermeiden.",
            ),
            (
                "Kann UKNS auch einzelne Projekte übernehmen?",
                "Ja. Viele Kunden starten mit einem konkreten Thema wie Microsoft 365, Backup, WLAN oder Arbeitsplatz-Einrichtung und entscheiden danach über laufende Betreuung.",
            ),
            (
                "Muss alles sofort modernisiert werden?",
                "Nein. Gute IT-Planung unterscheidet zwischen dringend, sinnvoll und später. Genau diese Reihenfolge spart Budget.",
            ),
        ],
        related=[
            ("/microsoft-365-beratung-leipzig/", "Microsoft 365 Beratung", "Konten, Teams, Mail und Sicherheit sauber planen."),
            ("/backup-loesungen-leipzig/", "Backup-Lösungen", "Daten schützen, bevor der Ernstfall da ist."),
            ("/it-monitoring-leipzig/", "IT-Monitoring", "Ausfälle früher sehen und ruhiger reagieren."),
        ],
    ),
    Article(
        slug="computerhilfe-leipzig-ohne-fachchinesisch",
        title="Computerhilfe in Leipzig ohne Fachchinesisch",
        meta_title="Computerhilfe Leipzig ohne Fachchinesisch | UKNS",
        description="Computerhilfe in Leipzig für Privatkunden: verständlich, ruhig und nachvollziehbar bei PC, Laptop, Outlook, Drucker, WLAN, Viren und Datensicherung.",
        kicker="Ratgeber für Privatkunden",
        hero="Wenn der Computer stresst, brauchen Sie keine Fachbegriffe, sondern jemanden, der ruhig sortiert",
        hero_alt="Verständliche Computerhilfe in Leipzig",
        intro=(
            "Computerprobleme fühlen sich oft größer an, als sie sind. Ein Drucker druckt nicht, Outlook fragt immer wieder nach dem Passwort, das WLAN bricht ab oder der Laptop ist plötzlich langsam. "
            "Wir schauen gemeinsam drauf, erklären die Ursache und sagen ehrlich, ob Fernwartung reicht oder ein Termin vor Ort sinnvoller ist."
        ),
        image_stem="computer-reparatur-leipzig",
        sections=[
            Section(
                "Erst verstehen, dann klicken",
                (
                    "Gerade bei Privatkunden ist Vertrauen wichtig. Deshalb erklären wir, was wir sehen, welche Schritte wir gehen und wann Sie etwas bestätigen müssen. "
                    "Sie behalten den Überblick, auch wenn Sie sich selbst nicht als Technikmensch sehen."
                ),
                [
                    "Outlook, Thunderbird oder E-Mail-Konto einrichten.",
                    "Drucker, Scanner, WLAN oder Router wieder verbinden.",
                    "Langsame PCs prüfen, aufräumen und sinnvoll verbessern.",
                ],
            ),
            Section(
                "Sicherheit ohne Panik",
                (
                    "Virenmeldungen, angebliche Microsoft-Anrufe oder merkwürdige Pop-ups machen nervös. Wir trennen echte Gefahr von Fehlalarm und helfen dabei, Daten, Passwörter und Geräte wieder in Ordnung zu bringen."
                ),
                [
                    "Malware prüfen und entfernen.",
                    "Passwörter und Konten absichern.",
                    "Backups für Fotos, Dokumente und wichtige Erinnerungen einrichten.",
                ],
            ),
            Section(
                "Hilfe, die zum Alltag passt",
                (
                    "Manchmal ist die beste Lösung kein neues Gerät, sondern eine kleine Einstellung. Manchmal lohnt ein SSD-Upgrade. Und manchmal sagen wir auch: Reparatur lohnt sich nicht mehr."
                ),
                [
                    "Ehrliche Einschätzung statt unnötigem Neukauf.",
                    "Geduldige Erklärung für wiederkehrende Fragen.",
                    "Konkrete Empfehlung, was Sie künftig selbst tun können.",
                ],
            ),
        ],
        steps=[
            ("01", "Problem schildern", "Sie erzählen, was passiert ist. Auch wenn es nur 'irgendwas ist anders' lautet."),
            ("02", "Gemeinsam prüfen", "Wir grenzen die Ursache ein und erklären die nächsten Schritte verständlich."),
            ("03", "Alltagstauglich abschließen", "Am Ende soll nicht nur das Problem weg sein, sondern auch klar sein, was verändert wurde."),
        ],
        faqs=[
            (
                "Kann ich auch anrufen, wenn ich das Problem nicht genau beschreiben kann?",
                "Ja. Genau dafür ist Computerhilfe da. Eine ungenaue Beschreibung ist kein Problem, wir stellen die passenden Fragen.",
            ),
            (
                "Ist Fernwartung sicher?",
                "Fernwartung ist sicher, wenn sie nur mit Ihrer Zustimmung startet und Sie sehen, was passiert. Für Hardware oder sensible Situationen empfehlen wir vor Ort zu prüfen.",
            ),
            (
                "Helfen Sie auch bei älteren Menschen?",
                "Ja. Wir erklären ruhig, ohne Druck und ohne vorauszusetzen, dass Begriffe wie Treiber, Browserprofil oder IMAP bekannt sind.",
            ),
        ],
        related=[
            ("/pc-hilfe-leipzig/", "PC-Hilfe Leipzig", "Schnelle Hilfe bei allgemeinen PC-Problemen."),
            ("/druckerprobleme-leipzig/", "Druckerprobleme", "Wenn Drucker, WLAN oder Warteschlange blockieren."),
            ("/senioren-computerhilfe-leipzig/", "Senioren-Computerhilfe", "Geduldige Unterstützung für digitale Alltagsthemen."),
        ],
    ),
    Article(
        slug="fernwartung-oder-vor-ort-it-service-leipzig",
        title="Fernwartung oder Vor-Ort-Service?",
        meta_title="Fernwartung oder Vor-Ort IT-Service in Leipzig? Entscheidungshilfe | UKNS",
        description="Wann Fernwartung reicht und wann Vor-Ort-Service in Leipzig besser ist: praktische Entscheidungshilfe für Privatkunden und Unternehmen.",
        kicker="Entscheidungshilfe",
        hero="Nicht jeder IT-Fall braucht Anfahrt. Aber manche Probleme muss man sehen, anfassen und sauber übergeben.",
        hero_alt="Fernwartung oder Vor-Ort IT-Service in Leipzig",
        intro=(
            "Viele IT-Probleme lassen sich aus der Ferne schneller lösen als mit einem Termin vor Ort. Trotzdem gibt es Situationen, in denen ein Techniker am Schreibtisch, im Serverraum oder neben dem Router die bessere Wahl ist. "
            "Die Kunst liegt darin, beides sauber zu unterscheiden."
        ),
        image_stem="it-support-leipzig",
        sections=[
            Section(
                "Fernwartung ist stark bei Software und Einstellungen",
                (
                    "Wenn Windows startet, Internet verfügbar ist und Sie zustimmen können, ist Fernwartung oft der schnellste Weg. "
                    "Sie sparen Wartezeit und sehen direkt, was passiert."
                ),
                [
                    "E-Mail, Outlook, Microsoft 365 und Benutzerkonten.",
                    "Programme, Updates, Fehlermeldungen und Browserprobleme.",
                    "Sicherheitsprüfung, Bereinigung und kurze Einrichtungsschritte.",
                ],
            ),
            Section(
                "Vor Ort ist besser, wenn Technik räumlich eine Rolle spielt",
                (
                    "WLAN-Funklöcher, defekte Hardware, Verkabelung, Serverräume oder Drucker mit Papierstau lassen sich nicht vollständig durch einen Bildschirm verstehen. "
                    "Dann zählt der Blick auf die Umgebung."
                ),
                [
                    "Router, Switches, Access Points und Netzwerkschränke prüfen.",
                    "PC, Laptop, Drucker, NAS oder Server physisch kontrollieren.",
                    "Arbeitsplätze einrichten und direkt mit dem Nutzer testen.",
                ],
            ),
            Section(
                "Sicherheit entscheidet mit",
                (
                    "Bei Fernwartung gilt: Sie müssen zustimmen, sehen die Schritte und können die Verbindung beenden. "
                    "Wenn sensible Daten, Betrugsverdacht oder unklare Zugänge im Spiel sind, sprechen wir vorher offen über den passenden Weg."
                ),
                [
                    "Keine Fernwartung ohne Ihre aktive Freigabe.",
                    "Keine unnötigen Tools, wenn ein Telefonat oder Vor-Ort-Termin besser ist.",
                    "Klare Erklärung, was geprüft und verändert wurde.",
                ],
            ),
        ],
        steps=[
            ("01", "Kurz einordnen", "Wir klären, ob das Gerät erreichbar ist und ob Hardware beteiligt sein könnte."),
            ("02", "Schnellster sinnvoller Weg", "Fernwartung, Telefon oder Vor-Ort-Termin werden nicht ideologisch entschieden, sondern praktisch."),
            ("03", "Saubere Übergabe", "Sie wissen am Ende, was gemacht wurde und was beim nächsten Mal hilft."),
        ],
        faqs=[
            (
                "Ist Fernwartung günstiger?",
                "Oft ja, weil keine Anfahrt und weniger Wartezeit entstehen. Entscheidend bleibt aber, ob das Problem damit zuverlässig lösbar ist.",
            ),
            (
                "Kann UKNS in Leipzig auch vor Ort helfen?",
                "Ja. Vor Ort ist besonders sinnvoll bei Hardware, Netzwerk, WLAN, Servern, Druckern oder wenn mehrere Arbeitsplätze betroffen sind.",
            ),
            (
                "Sehe ich bei Fernwartung, was gemacht wird?",
                "Ja. Seriöse Fernwartung läuft mit Ihrer Zustimmung und nachvollziehbar. Sie behalten die Kontrolle über die Sitzung.",
            ),
        ],
        related=[
            ("/pc-support-fernwartung-leipzig/", "PC-Support per Fernwartung", "Schnelle Hilfe aus der Ferne."),
            ("/it-support-leipzig/", "IT-Support Leipzig", "Support für Unternehmen und private Technikfragen."),
            ("/preisliste/", "Preise", "Transparente Abrechnung für IT-Hilfe in Leipzig."),
        ],
    ),
]


def picture_html(stem: str, alt: str) -> str:
    return f"""
<picture>
  <source type="image/webp" srcset="/images/{stem}-480.webp 480w, /images/{stem}-800.webp 800w, /images/{stem}-1200.webp 1200w" sizes="(min-width: 960px) 44vw, 100vw">
  <img class="article-hero-image" src="/images/{stem}-1200.jpg" srcset="/images/{stem}-480.jpg 480w, /images/{stem}-800.jpg 800w, /images/{stem}-1200.jpg 1200w" sizes="(min-width: 960px) 44vw, 100vw" width="1200" height="800" alt="{escape(alt)}" fetchpriority="high" decoding="async">
</picture>"""


def json_script(data: dict) -> str:
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "</script>"


def render_article(article: Article) -> str:
    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": article.title,
        "description": article.description,
        "image": f"https://ukns.eu/images/{article.image_stem}-1200.jpg",
        "datePublished": TODAY,
        "dateModified": TODAY,
        "inLanguage": "de-DE",
        "author": {"@type": "Organization", "name": "UKNS IT-Premium Services"},
        "publisher": {"@type": "Organization", "name": "UKNS IT-Premium Services", "url": "https://ukns.eu/"},
        "mainEntityOfPage": f"https://ukns.eu{article.url_path}",
    }
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in article.faqs
        ],
    }
    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Startseite", "item": "https://ukns.eu/"},
            {"@type": "ListItem", "position": 2, "name": "IT-Wissen", "item": "https://ukns.eu/it-wissen/"},
            {"@type": "ListItem", "position": 3, "name": article.title, "item": f"https://ukns.eu{article.url_path}"},
        ],
    }

    section_html = "\n".join(
        f"""
<section class="content-card">
  <h2>{escape(section.title)}</h2>
  <p>{escape(section.body)}</p>
  <ul>{"".join(f"<li>{escape(item)}</li>" for item in section.bullets)}</ul>
</section>"""
        for section in article.sections
    )
    steps_html = "\n".join(
        f"""
<article class="step-card">
  <span>{escape(number)}</span>
  <h3>{escape(title)}</h3>
  <p>{escape(body)}</p>
</article>"""
        for number, title, body in article.steps
    )
    faq_html = "\n".join(
        f"""
<details class="faq-item">
  <summary>{escape(question)}</summary>
  <p>{escape(answer)}</p>
</details>"""
        for question, answer in article.faqs
    )
    related_html = "\n".join(
        f"""
<a class="related-card" href="{escape(href)}">
  <strong>{escape(title)}</strong>
  <small>{escape(text)}</small>
</a>"""
        for href, title, text in article.related
    )

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
<meta name="robots" content="index, follow">
<meta name="author" content="UKNS IT-Premium Services">
<meta name="geo.region" content="DE-SN">
<meta name="geo.placename" content="Leipzig">
<title>{escape(article.meta_title)}</title>
<meta name="description" content="{escape(article.description)}">
<link rel="canonical" href="https://ukns.eu{article.url_path}">
<link rel="alternate" hreflang="de-DE" href="https://ukns.eu{article.url_path}">
<link rel="alternate" hreflang="x-default" href="https://ukns.eu{article.url_path}">
<meta property="og:type" content="article">
<meta property="og:locale" content="de_DE">
<meta property="og:site_name" content="UKNS IT-Premium Services">
<meta property="og:url" content="https://ukns.eu{article.url_path}">
<meta property="og:title" content="{escape(article.title)}">
<meta property="og:description" content="{escape(article.description)}">
<meta property="og:image" content="https://ukns.eu/images/{article.image_stem}-1200.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(article.title)}">
<meta name="twitter:description" content="{escape(article.description)}">
<meta name="twitter:image" content="https://ukns.eu/images/{article.image_stem}-1200.jpg">
<link href="/apple-touch-icon.png" rel="apple-touch-icon" sizes="180x180">
<link href="/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png">
<link href="/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png">
<link href="/site.webmanifest" rel="manifest">
<meta name="theme-color" content="#ffffff">
{json_script(article_schema)}
{json_script(faq_schema)}
{json_script(breadcrumb_schema)}
<link as="font" crossorigin href="/fonts/montserrat-v30-latin-700.woff2" rel="preload" type="font/woff2">
<link as="font" crossorigin href="/fonts/open-sans-v43-latin-regular.woff2" rel="preload" type="font/woff2">
<link href="/css/style.optimized.css?v=20260531-icons" rel="stylesheet">
<style>
  body.humanized-article {{ margin:0; background:#f6f8fc; color:#111827; }}
  .article-nav {{ position:fixed; inset:0 0 auto; z-index:40; background:rgba(255,255,255,.94); border-bottom:1px solid rgba(17,24,39,.08); backdrop-filter:blur(16px); }}
  .article-nav-inner {{ max-width:1180px; margin:0 auto; padding:.85rem 1rem; display:flex; align-items:center; justify-content:space-between; gap:1rem; }}
  .article-brand {{ color:#2B3990; font-weight:800; display:flex; align-items:baseline; gap:.5rem; }}
  .article-brand small {{ color:#667085; font-weight:700; }}
  .article-links {{ display:flex; gap:1rem; flex-wrap:wrap; font-weight:700; color:#344054; }}
  .article-container {{ max-width:1180px; margin:0 auto; padding:0 1rem; }}
  .article-hero {{ padding:7.5rem 0 4.5rem; background:linear-gradient(135deg,#101b4d,#2B3990); color:#fff; }}
  .article-hero-grid {{ display:grid; grid-template-columns:1.05fr .95fr; gap:3rem; align-items:center; }}
  .article-kicker {{ color:#FFCC00; font-weight:800; margin-bottom:1rem; }}
  .article-hero h1 {{ font-size:clamp(2.25rem,5vw,4.25rem); line-height:1.05; margin:0 0 1.25rem; font-weight:800; letter-spacing:0; }}
  .article-lead {{ font-size:1.16rem; line-height:1.82; opacity:.94; margin:0 0 1.8rem; }}
  .article-hero-image {{ width:100%; border-radius:.5rem; box-shadow:0 28px 72px rgba(0,0,0,.28); object-fit:cover; aspect-ratio:3/2; }}
  .article-button-row {{ display:flex; flex-wrap:wrap; gap:.9rem; }}
  .article-primary,.article-secondary {{ display:inline-flex; align-items:center; justify-content:center; min-height:48px; padding:.9rem 1.2rem; border-radius:.5rem; font-weight:800; }}
  .article-primary {{ background:#FFCC00; color:#2B3990; }}
  .article-secondary {{ border:2px solid rgba(255,255,255,.84); color:#fff; }}
  .article-main {{ padding:4.5rem 0; }}
  .article-intro {{ max-width:860px; font-size:1.15rem; line-height:1.86; color:#344054; margin:0 auto 2.4rem; }}
  .content-grid {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:1.25rem; }}
  .content-card,.step-card,.faq-item,.related-card {{ background:#fff; border:1px solid rgba(43,57,144,.12); border-radius:.5rem; box-shadow:0 16px 38px rgba(16,24,40,.07); }}
  .content-card {{ padding:1.7rem; }}
  .content-card h2,.step-card h3,.article-section-title {{ color:#2B3990; font-weight:800; line-height:1.2; }}
  .content-card h2 {{ font-size:1.45rem; margin:0 0 .85rem; }}
  .content-card p,.content-card li,.step-card p,.faq-item p,.related-card small {{ color:#475467; line-height:1.75; }}
  .content-card ul {{ padding-left:1.15rem; margin:1rem 0 0; }}
  .article-section {{ margin-top:3.6rem; }}
  .article-section-title {{ font-size:2rem; margin:0 0 1.2rem; }}
  .steps-grid,.faq-grid,.related-grid {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:1rem; }}
  .step-card {{ padding:1.4rem; }}
  .step-card span {{ color:#2B3990; font-weight:900; font-size:.9rem; }}
  .step-card h3 {{ margin:.4rem 0 .6rem; font-size:1.15rem; }}
  .faq-grid {{ grid-template-columns:1fr 1fr; }}
  .faq-item {{ padding:1.2rem 1.35rem; }}
  .faq-item summary {{ cursor:pointer; color:#2B3990; font-weight:800; line-height:1.4; }}
  .related-card {{ display:block; padding:1.35rem; }}
  .related-card strong {{ display:block; color:#2B3990; margin-bottom:.4rem; }}
  .article-cta {{ margin-top:3.6rem; background:#2B3990; color:#fff; border-radius:.5rem; padding:2rem; display:flex; align-items:center; justify-content:space-between; gap:2rem; }}
  .article-cta h2 {{ font-size:1.7rem; margin:0 0 .5rem; font-weight:800; }}
  .article-cta p {{ opacity:.92; line-height:1.72; margin:0; }}
  footer.article-footer {{ background:#333; color:#d1d5db; padding:3rem 0; }}
  @media(max-width:900px) {{
    .article-links {{ display:none; }}
    .article-hero-grid,.content-grid,.steps-grid,.faq-grid,.related-grid {{ grid-template-columns:1fr; }}
    .article-hero {{ padding-top:6.5rem; }}
    .article-cta {{ display:block; }}
    .article-cta .article-primary {{ margin-top:1.25rem; }}
  }}
</style>
</head>
<body class="humanized-article">
<header class="article-nav">
  <nav class="article-nav-inner">
    <a class="article-brand" href="/"><span>UKNS</span><small>IT-Premium Services</small></a>
    <div class="article-links"><a href="/it-service-leipzig/">IT-Service</a><a href="/computer-reparatur-leipzig/">Computerhilfe</a><a href="/preisliste/">Preise</a><a href="/kontakt/">Kontakt</a></div>
  </nav>
</header>
<main>
<section class="article-hero">
  <div class="article-container article-hero-grid">
    <div>
      <p class="article-kicker">{escape(article.kicker)}</p>
      <h1>{escape(article.hero)}</h1>
      <p class="article-lead">{escape(article.description)}</p>
      <div class="article-button-row"><a class="article-primary" href="/kontakt/?subject={escape(article.title)}">Anfrage stellen</a><a class="article-secondary" href="/it-wissen/">Weitere Ratgeber</a></div>
    </div>
    {picture_html(article.image_stem, article.hero_alt)}
  </div>
</section>
<section class="article-main">
  <div class="article-container">
    <p class="article-intro">{escape(article.intro)}</p>
    <div class="content-grid">{section_html}</div>
    <section class="article-section">
      <h2 class="article-section-title">So gehen wir vor</h2>
      <div class="steps-grid">{steps_html}</div>
    </section>
    <section class="article-section">
      <h2 class="article-section-title">Häufige Fragen</h2>
      <div class="faq-grid">{faq_html}</div>
    </section>
    <section class="article-section">
      <h2 class="article-section-title">Passende nächste Schritte</h2>
      <div class="related-grid">{related_html}</div>
    </section>
    <section class="article-cta">
      <div><h2>Lieber kurz sortieren als lange rätseln?</h2><p>Schildern Sie uns kurz die Situation. Wir sagen Ihnen ehrlich, welcher nächste Schritt sinnvoll ist und ob Fernwartung, Vor-Ort-Service oder ein geplantes Projekt besser passt.</p></div>
      <a class="article-primary" href="/kontakt/">Kontakt aufnehmen</a>
    </section>
  </div>
</section>
</main>
<footer class="article-footer">
  <div class="article-container"><strong>UKNS IT-Premium Services Leipzig</strong><p>IT-Service, Computerhilfe, Sicherheit, Cloud und Support aus Leipzig.</p><p><a href="/impressum/">Impressum</a> · <a href="/datenschutz/">Datenschutz</a> · <a href="/kontakt/">Kontakt</a></p></div>
</footer>
</body>
</html>
"""


def article_card(article: Article) -> str:
    return f"""
<div class="bg-white rounded-lg shadow-lg overflow-hidden transform hover:-translate-y-2 transition-transform duration-300">
<a class="block" href="{article.url_path}">
<img alt="{escape(article.hero_alt)}" class="w-full h-48 object-cover" src="/images/{article.image_stem}-1200.jpg" loading="lazy" decoding="async" width="1200" height="800"/>
<div class="p-6">
<p class="text-sm text-primary-blue font-semibold mb-2">Humanized Ratgeber</p>
<h3 class="text-xl font-bold text-gray-900 mb-3">{escape(article.title)}</h3>
<p class="text-gray-600 text-sm mb-4">{escape(article.description)}</p>
<span class="font-semibold text-primary-blue hover:underline">Lesen →</span>
</div>
</a>
</div>"""


def update_it_wissen_index() -> None:
    path = ROOT / "it-wissen" / "index.html"
    text = path.read_text(encoding="utf-8")
    cards = "\n".join(article_card(article) for article in ARTICLES)
    section = f"""
<!-- Humanized competitor content generated -->
<section class="py-16 md:py-20 bg-white" id="humanized-ratgeber">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
<div class="text-center mb-12">
<h2 class="text-3xl font-bold text-primary-blue mb-4">Ratgeber mit echter Alltagsperspektive</h2>
<p class="text-lg text-gray-600 max-w-3xl mx-auto">Aus der Wettbewerbsanalyse abgeleitet, aber bewusst menschlich geschrieben: klare Orientierung, typische Situationen, ehrliche nächste Schritte.</p>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
{cards}
</div>
</div>
</section>
<!-- /Humanized competitor content generated -->
"""
    start = "<!-- Humanized competitor content generated -->"
    end = "<!-- /Humanized competitor content generated -->"
    if start in text and end in text:
        before = text.split(start, 1)[0]
        after = text.split(end, 1)[1]
        text = before + section + after
    else:
        text = text.replace("<!-- SEO service hubs generated -->", section + "\n<!-- SEO service hubs generated -->")
    path.write_text(text, encoding="utf-8", newline="\n")


def update_preisliste() -> None:
    path = ROOT / "preisliste" / "index.html"
    text = path.read_text(encoding="utf-8")
    section = """
<!-- Humanized price guidance generated -->
<section class="py-16 md:py-20 bg-gray-50" id="preis-orientierung">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
<div class="text-center mb-12">
<h2 class="text-3xl md:text-4xl font-bold text-primary-blue mb-4">Was kostet ein typischer IT-Einsatz wirklich?</h2>
<p class="text-lg text-gray-600 max-w-3xl mx-auto">Der Stundensatz ist nur die halbe Wahrheit. Wichtig ist, ob vorher sauber eingegrenzt wird, ob Fernwartung reicht und ob Sie am Ende verstehen, was erledigt wurde.</p>
</div>
<div class="grid md:grid-cols-3 gap-8">
<div class="benefit-card bg-white rounded-lg p-8 shadow-md blue-accent-box">
<div class="benefit-card-icon-wrapper w-16 h-16 bg-primary-yellow rounded-lg flex items-center justify-center mb-4"><i class="fas fa-headset text-primary-blue text-2xl"></i></div>
<h3 class="text-xl font-semibold mb-3 text-primary-blue">Kleines Problem, schnelle Hilfe</h3>
<p class="text-gray-600 text-sm">Outlook fragt nach dem Passwort, der Drucker hängt oder WLAN bricht ab. Oft lässt sich das per Telefon oder Fernwartung eingrenzen, bevor ein Vor-Ort-Termin nötig wird.</p>
</div>
<div class="benefit-card bg-white rounded-lg p-8 shadow-md accent-box">
<div class="benefit-card-icon-wrapper w-16 h-16 bg-primary-blue rounded-lg flex items-center justify-center mb-4"><i class="fas fa-tools text-white text-2xl"></i></div>
<h3 class="text-xl font-semibold mb-3 text-primary-blue">PC, Laptop oder Gerät prüfen</h3>
<p class="text-gray-600 text-sm">Wenn Hardware, Daten oder ein langsames Gerät im Spiel sind, sagen wir ehrlich, ob Reparatur, Aufrüstung oder Austausch wirtschaftlich sinnvoller ist.</p>
</div>
<div class="benefit-card bg-white rounded-lg p-8 shadow-md blue-accent-box">
<div class="benefit-card-icon-wrapper w-16 h-16 bg-primary-yellow rounded-lg flex items-center justify-center mb-4"><i class="fas fa-shield-alt text-primary-blue text-2xl"></i></div>
<h3 class="text-xl font-semibold mb-3 text-primary-blue">Firmen-IT mit Priorität</h3>
<p class="text-gray-600 text-sm">Bei Server, Microsoft 365, Backup oder Sicherheitsproblemen sortieren wir zuerst: Was blockiert den Betrieb, was ist Risiko, was kann geplant gelöst werden?</p>
</div>
</div>
<div class="mt-10 bg-white rounded-lg shadow-md p-8">
<h3 class="text-2xl font-bold text-primary-blue mb-4">Unser Ablauf, damit Preise fair bleiben</h3>
<div class="grid md:grid-cols-3 gap-6 text-gray-600 text-sm">
<p><strong class="text-primary-blue">1. Kurz einschätzen:</strong> Wir hören zu, stellen die entscheidenden Fragen und sagen, welcher Weg realistisch ist.</p>
<p><strong class="text-primary-blue">2. Aufwand erklären:</strong> Bevor kostenpflichtige Arbeit startet, wissen Sie, was wir prüfen oder ändern wollen.</p>
<p><strong class="text-primary-blue">3. Verständlich abschließen:</strong> Sie bekommen keine Fachbegriffe als Nebelwand, sondern eine klare Übergabe.</p>
</div>
<div class="mt-6 flex flex-wrap gap-4">
<a class="bg-primary-blue text-white px-6 py-3 rounded-lg font-semibold hover:bg-opacity-90 transition" href="/it-wissen/fernwartung-oder-vor-ort-it-service-leipzig.html">Fernwartung oder Vor-Ort?</a>
<a class="bg-primary-yellow text-primary-blue px-6 py-3 rounded-lg font-semibold hover:bg-opacity-90 transition" href="/kontakt/">Fall kurz schildern</a>
</div>
</div>
</div>
</section>
<!-- /Humanized price guidance generated -->
"""
    start = "<!-- Humanized price guidance generated -->"
    end = "<!-- /Humanized price guidance generated -->"
    if start in text and end in text:
        before = text.split(start, 1)[0]
        after = text.split(end, 1)[1]
        text = before + section + after
    else:
        text = text.replace('<section class="py-16 bg-contact-section text-white scroll-mt-custom" data-aos="fade-in" id="contact-preise">', section + '\n<section class="py-16 bg-contact-section text-white scroll-mt-custom" data-aos="fade-in" id="contact-preise">')
    path.write_text(text, encoding="utf-8", newline="\n")


def update_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    additions = []
    for article in ARTICLES:
        loc = f"https://ukns.eu{article.url_path}"
        if loc not in text:
            additions.append(
                f"""
    <url>
        <loc>{loc}</loc>
        <lastmod>{TODAY}</lastmod>
        <priority>0.7</priority>
    </url>
"""
            )
    if additions:
        text = text.replace("\n</urlset>", "\n" + "\n".join(additions) + "\n</urlset>")
        path.write_text(text, encoding="utf-8", newline="\n")


def write_analysis() -> None:
    path = ROOT / "seo-wettbewerberanalyse-humanized-content-2026-06-01.md"
    content = """# Wettbewerberanalyse und Content-Ableitung

Stand: 2026-06-01

## Quellen

- https://www.computerhilfe-leipzig.de/
- https://www.expertiger.de/
- https://www.expertiger.de/druckerprobleme
- https://microcat.de/unternehmen/standorte/leipzig/
- https://www.medialine.com/unternehmen/standorte/it-service-in-leipzig
- https://www.paro-it.de/
- https://www.lorop.de/it-service/managed-services-leipzig/
- https://www.pc-bitt.de/
- https://www.connputer.de/
- https://simteva.de/

## Muster, die auffallen

1. Lokale Computerhilfe-Seiten gewinnen Vertrauen über Empathie, Privatsphäre, persönliche Termine und klare Einstiegspreise.
2. Expertiger besetzt sehr viele konkrete Problem-Intents: Outlook, Drucker, Internet langsam, PC langsam, Malware, Windows, Computerkurse.
3. Firmenkunden-Anbieter betonen Managed Services, Cybersecurity, Helpdesk, Fieldservice, Hardware-Beschaffung, Cloud, Microsoft 365, Backup und NIS2.
4. Gute Wettbewerber erklären Abläufe: anrufen, Problem schildern, einschätzen, freigeben, lösen.
5. Häufig fehlen aber echte Entscheidungshilfen: Wann reicht Fernwartung? Wann braucht man Vor-Ort-Service? Woran erkennt man einen passenden IT-Partner?

## Was UKNS übernehmen sollte

- Nicht Texte, Preise oder Bewertungen kopieren.
- Suchintentionen übernehmen: konkrete Probleme, transparente Abläufe, Sicherheitsfragen, Vergleichsfragen.
- Menschlicher schreiben: kurze Alltagsszenen, klare Sprache, keine überladenen Buzzwords.
- Mehr interne Verlinkung zwischen Preis, Fernwartung, Computerhilfe, Managed Services und IT-Notfall.

## Umgesetzte Inhalte

- /it-wissen/it-service-leipzig-anbieter-vergleichen.html
- /it-wissen/it-betreuung-kleine-firmen-leipzig-praxis.html
- /it-wissen/computerhilfe-leipzig-ohne-fachchinesisch.html
- /it-wissen/fernwartung-oder-vor-ort-it-service-leipzig.html

Zusätzlich wurde die Preisliste um eine menschlichere Preisorientierung ergänzt.
"""
    path.write_text(content, encoding="utf-8", newline="\n")


def main() -> None:
    for article in ARTICLES:
        target = ROOT / "it-wissen" / f"{article.slug}.html"
        target.write_text(render_article(article), encoding="utf-8", newline="\n")
    update_it_wissen_index()
    update_preisliste()
    update_sitemap()
    write_analysis()
    print(f"created_articles={len(ARTICLES)}")


if __name__ == "__main__":
    main()
