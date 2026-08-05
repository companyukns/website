from __future__ import annotations

import hashlib
import html
import json
import math
import re
import textwrap
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://ukns.eu"
LOCAL_DATE = "2026-06-01"
IMAGE_DIR = ROOT / "images" / "generated"


@dataclass(frozen=True)
class PageTopic:
    slug: str
    title: str
    keyword: str
    audience: str
    segment: str
    category: str
    problem: str
    outcome: str
    deliverables: tuple[str, str, str, str]
    hub: str
    cta: str


B2B_TOPICS = [
    ("microsoft-365-backup-leipzig", "Microsoft 365 Backup Leipzig", "Microsoft 365 Backup Leipzig", "Firmenkunden", "b2b", "Microsoft 365", "E-Mails, Teams, SharePoint und OneDrive sind geschäftskritisch, aber gelöschte oder verschlüsselte Daten müssen gezielt wiederherstellbar sein.", "sichere Wiederherstellung von Postfächern, Dateien und Teams-Daten"),
    ("microsoft-intune-leipzig", "Microsoft Intune Einrichtung Leipzig", "Microsoft Intune Leipzig", "Firmenkunden", "b2b", "Moderner Arbeitsplatz", "Laptops, Smartphones und Homeoffice-Geräte sollen zentral verwaltet, abgesichert und standardisiert ausgerollt werden.", "kontrollierte Geräteverwaltung für mobile und hybride Arbeit"),
    ("entra-id-mfa-conditional-access-leipzig", "Entra ID, MFA & Conditional Access Leipzig", "Entra ID MFA Leipzig", "Firmenkunden", "b2b", "Identität & Zugriff", "Konten sind oft der wichtigste Angriffspunkt, besonders wenn Microsoft 365 ohne klare Zugriffsregeln genutzt wird.", "stärkere Anmeldung, MFA und klare Zugriffsrichtlinien"),
    ("it-monitoring-leipzig", "IT-Monitoring Leipzig", "IT Monitoring Leipzig", "Firmenkunden", "b2b", "Managed Services", "Server, Backups, Speicher, Internet und Sicherheitsdienste fallen selten geplant aus und sollten frühzeitig überwacht werden.", "frühe Warnungen und weniger ungeplante Ausfälle"),
    ("patch-management-leipzig", "Patch-Management Leipzig", "Patch Management Leipzig", "Firmenkunden", "b2b", "Managed Services", "Updates werden oft unkoordiniert installiert oder bleiben liegen, obwohl Sicherheitslücken schnell ausgenutzt werden.", "planbare Sicherheitsupdates für Systeme und Anwendungen"),
    ("nis2-beratung-leipzig", "NIS2 Beratung Leipzig", "NIS2 Beratung Leipzig", "Firmenkunden", "b2b", "Compliance & Security", "Viele mittelständische Unternehmen müssen technische und organisatorische Sicherheitsmaßnahmen nachvollziehbar verbessern.", "eine realistische technische NIS2-Roadmap"),
    ("vpn-homeoffice-sicherheit-leipzig", "VPN & Homeoffice Sicherheit Leipzig", "VPN Homeoffice Sicherheit Leipzig", "Firmenkunden", "b2b", "Remote Work", "Remote-Zugänge müssen funktionieren, dürfen aber keine offene Tür ins Unternehmensnetz werden.", "sichere Zugänge für Homeoffice und mobile Teams"),
    ("voip-teams-telefonie-leipzig", "VoIP & Teams Telefonie Leipzig", "VoIP Teams Telefonie Leipzig", "Firmenkunden", "b2b", "Kommunikation", "Klassische Telefonanlagen werden teuer und unflexibel, während Teams und VoIP bessere Integration ermöglichen.", "moderne Telefonie mit klarer Rufnummern- und Nutzerstruktur"),
    ("it-dokumentation-asset-management-leipzig", "IT-Dokumentation & Asset Management Leipzig", "IT Dokumentation Leipzig", "Firmenkunden", "b2b", "IT-Betrieb", "Ohne aktuelle Dokumentation werden Störungen, Audits und Mitarbeiterwechsel unnötig riskant.", "transparente Systeme, Verträge, Geräte und Verantwortlichkeiten"),
    ("it-sicherheitsaudit-leipzig", "IT-Sicherheitsaudit Leipzig", "IT Sicherheitsaudit Leipzig", "Firmenkunden", "b2b", "Security Audit", "Viele Risiken bleiben unsichtbar, bis ein Ausfall oder Angriff sie schmerzhaft sichtbar macht.", "priorisierte Sicherheitsmaßnahmen statt Bauchgefühl"),
    ("edr-xdr-leipzig", "EDR & XDR Leipzig", "EDR XDR Leipzig", "Firmenkunden", "b2b", "Endpoint Security", "Klassische Virenscanner reichen gegen moderne Angriffe, laterale Bewegung und verdächtige Aktivitäten oft nicht aus.", "bessere Erkennung und Reaktion auf Angriffe"),
    ("managed-antivirus-leipzig", "Managed Antivirus Leipzig", "Managed Antivirus Leipzig", "Firmenkunden", "b2b", "Endpoint Security", "Antivirus muss aktuell, überwacht und sauber ausgerollt sein, statt nur lokal installiert zu werden.", "zentral verwalteter Schutz für Firmenrechner"),
    ("serverraum-wartung-leipzig", "Serverraum Wartung Leipzig", "Serverraum Wartung Leipzig", "Firmenkunden", "b2b", "Infrastruktur", "Serverräume wachsen oft ungeplant und leiden unter Kabelchaos, Wärme, Stromrisiken und fehlender Dokumentation.", "stabilere Infrastruktur mit klarer Wartung"),
    ("wlan-ausleuchtung-leipzig", "WLAN-Ausleuchtung Leipzig", "WLAN Ausleuchtung Leipzig", "Firmenkunden", "b2b", "Netzwerk", "Schlechtes WLAN kostet Zeit, stört Telefonie und lässt sich ohne Messung selten sauber planen.", "messbar bessere WLAN-Abdeckung im Büro"),
    ("sharepoint-beratung-leipzig", "SharePoint Beratung Leipzig", "SharePoint Beratung Leipzig", "Firmenkunden", "b2b", "Microsoft 365", "Dateiablagen in SharePoint brauchen Struktur, Berechtigungen und Regeln, sonst entsteht digitales Chaos.", "saubere Dokumentenablage mit sicheren Rechten"),
    ("teams-einrichtung-leipzig", "Microsoft Teams Einrichtung Leipzig", "Teams Einrichtung Leipzig", "Firmenkunden", "b2b", "Microsoft 365", "Teams wird schnell eingeführt, aber ohne Kanäle, Rechte und Regeln verliert es seinen Nutzen.", "strukturierte Zusammenarbeit in Microsoft Teams"),
    ("email-archivierung-leipzig", "E-Mail-Archivierung Leipzig", "E-Mail Archivierung Leipzig", "Firmenkunden", "b2b", "E-Mail & Compliance", "Geschäftliche E-Mails müssen auffindbar, nachvollziehbar und vor Verlust geschützt bleiben.", "rechtssichere und praktische E-Mail-Ablage"),
    ("spamfilter-leipzig", "Spamfilter & E-Mail-Schutz Leipzig", "Spamfilter Leipzig", "Firmenkunden", "b2b", "E-Mail-Sicherheit", "Spam, Phishing und schädliche Anhänge treffen fast jedes Unternehmen täglich.", "weniger gefährliche E-Mails und bessere Postfachsicherheit"),
    ("it-onboarding-offboarding-leipzig", "IT-Onboarding & Offboarding Leipzig", "IT Onboarding Leipzig", "Firmenkunden", "b2b", "IT-Prozesse", "Neue Mitarbeitende brauchen schnell funktionierende Zugänge, ausscheidende Personen müssen sauber gesperrt werden.", "kontrollierte Nutzerprozesse ohne Sicherheitslücken"),
    ("passwortmanager-firmen-leipzig", "Passwortmanager für Firmen Leipzig", "Passwortmanager Firmen Leipzig", "Firmenkunden", "b2b", "Identität & Zugriff", "Geteilte Passwörter in Excel, Browsern oder Notizen sind ein reales Sicherheitsrisiko.", "sichere Passwortverwaltung für Teams"),
    ("firewall-wartung-leipzig", "Firewall Wartung Leipzig", "Firewall Wartung Leipzig", "Firmenkunden", "b2b", "Netzwerksicherheit", "Firewall-Regeln, VPN-Zugänge und Firmware müssen regelmäßig geprüft werden.", "dauerhaft sichere Netzwerkgrenzen"),
    ("vpn-einrichtung-firma-leipzig", "VPN Einrichtung für Firmen Leipzig", "VPN Einrichtung Firma Leipzig", "Firmenkunden", "b2b", "Remote Work", "Sichere Verbindungen zu Büro, Servern und Anwendungen müssen zuverlässig und nachvollziehbar funktionieren.", "stabile VPN-Zugänge mit klarer Rechtevergabe"),
    ("mobile-device-management-leipzig", "Mobile Device Management Leipzig", "Mobile Device Management Leipzig", "Firmenkunden", "b2b", "Moderner Arbeitsplatz", "Firmenhandys und Tablets brauchen Richtlinien, Schutz und eine einfache Verwaltung.", "kontrollierte Mobilgeräte ohne manuelle Einzelpflege"),
    ("azure-cloud-beratung-leipzig", "Azure Cloud Beratung Leipzig", "Azure Cloud Beratung Leipzig", "Firmenkunden", "b2b", "Cloud", "Cloud-Ressourcen sollen sicher, kosteneffizient und passend zur bestehenden IT geplant werden.", "eine belastbare Azure-Strategie für Firmen"),
    ("cloud-backup-leipzig", "Cloud Backup Leipzig", "Cloud Backup Leipzig", "Firmenkunden", "b2b", "Backup", "Lokale Backups allein schützen nicht vor Brand, Diebstahl oder verschlüsselten Systemen.", "externe Datensicherung mit Wiederherstellungsplan"),
    ("server-migration-leipzig", "Server Migration Leipzig", "Server Migration Leipzig", "Firmenkunden", "b2b", "Server", "Alte Server müssen ersetzt oder in die Cloud überführt werden, ohne den Betrieb unnötig zu unterbrechen.", "sichere Migration von Servern und Diensten"),
    ("domain-dns-management-leipzig", "Domain & DNS Management Leipzig", "DNS Management Leipzig", "Firmenkunden", "b2b", "Web & Infrastruktur", "DNS, Domains, Mail-Einträge und Zertifikate sind kritisch, werden aber oft verstreut verwaltet.", "saubere technische Verwaltung wichtiger Internetdienste"),
    ("office-arbeitsplatz-einrichten-leipzig", "Office-Arbeitsplatz einrichten Leipzig", "Office Arbeitsplatz einrichten Leipzig", "Firmenkunden", "b2b", "Arbeitsplätze", "Neue Büroarbeitsplätze brauchen Hardware, Microsoft 365, Drucker, Sicherheit und Dokumentation.", "startklare Arbeitsplätze für produktive Teams"),
    ("pc-rollout-firma-leipzig", "PC-Rollout für Firmen Leipzig", "PC Rollout Firma Leipzig", "Firmenkunden", "b2b", "Arbeitsplätze", "Viele neue Rechner manuell einzurichten kostet Zeit und führt zu unterschiedlichen Konfigurationen.", "standardisierte Rechnerauslieferung für Unternehmen"),
    ("it-inventarisierung-leipzig", "IT-Inventarisierung Leipzig", "IT Inventarisierung Leipzig", "Firmenkunden", "b2b", "IT-Betrieb", "Unklare Geräte-, Lizenz- und Vertragsdaten erschweren Planung und Support.", "vollständiger Überblick über die Firmen-IT"),
    ("lizenzmanagement-leipzig", "Lizenzmanagement Leipzig", "Lizenzmanagement Leipzig", "Firmenkunden", "b2b", "IT-Betrieb", "Ungenutzte, fehlende oder falsch gebuchte Lizenzen verursachen Kosten und Compliance-Risiken.", "passende Lizenzen mit besserer Kostenkontrolle"),
    ("datenschutz-it-technik-leipzig", "Datenschutz & IT-Technik Leipzig", "Datenschutz IT Leipzig", "Firmenkunden", "b2b", "Compliance & Security", "Datenschutz braucht technische Maßnahmen wie Rechte, Protokolle, Verschlüsselung und Backup.", "praktische IT-Maßnahmen für Datenschutzanforderungen"),
    ("zero-trust-beratung-leipzig", "Zero Trust Beratung Leipzig", "Zero Trust Beratung Leipzig", "Firmenkunden", "b2b", "Security", "Pauschales Vertrauen im Netzwerk passt nicht mehr zu Cloud, Homeoffice und mobilen Geräten.", "schrittweise Zero-Trust-Sicherheitsarchitektur"),
    ("penetrationstest-vorbereitung-leipzig", "Penetrationstest Vorbereitung Leipzig", "Penetrationstest Vorbereitung Leipzig", "Firmenkunden", "b2b", "Security Audit", "Vor Audits und Tests sollten Systeme dokumentiert, Risiken priorisiert und Altlasten beseitigt werden.", "bessere Vorbereitung auf externe Sicherheitstests"),
    ("security-awareness-schulung-leipzig", "Security Awareness Schulung Leipzig", "Security Awareness Leipzig", "Firmenkunden", "b2b", "Schulung", "Mitarbeitende sind ein wichtiger Schutzfaktor gegen Phishing, Betrug und Datenpannen.", "verständliche Sicherheitsroutinen im Alltag"),
    ("phishing-simulation-leipzig", "Phishing Simulation Leipzig", "Phishing Simulation Leipzig", "Firmenkunden", "b2b", "Schulung", "Phishing-Risiken lassen sich besser verbessern, wenn sie realistisch gemessen und nachgeschult werden.", "messbares Sicherheitsbewusstsein im Team"),
    ("backup-restore-test-leipzig", "Backup Restore Test Leipzig", "Backup Restore Test Leipzig", "Firmenkunden", "b2b", "Backup", "Ein Backup zählt erst, wenn die Wiederherstellung getestet und dokumentiert wurde.", "nachweisbar wiederherstellbare Daten"),
    ("disaster-recovery-plan-leipzig", "Disaster Recovery Plan Leipzig", "Disaster Recovery Plan Leipzig", "Firmenkunden", "b2b", "Notfallplanung", "Bei größeren IT-Ausfällen braucht das Unternehmen ein klares Wiederanlauf-Drehbuch.", "schnellerer Wiederanlauf nach Ausfällen"),
    ("business-continuity-it-leipzig", "Business Continuity IT Leipzig", "Business Continuity IT Leipzig", "Firmenkunden", "b2b", "Notfallplanung", "IT-Ausfälle betreffen Prozesse, Kundenkommunikation und Umsatz direkt.", "belastbare IT-Prozesse für den Ernstfall"),
    ("nas-einrichtung-firma-leipzig", "NAS Einrichtung für Firmen Leipzig", "NAS Einrichtung Firma Leipzig", "Firmenkunden", "b2b", "Speicher & Backup", "NAS-Systeme brauchen Rechte, Backup, Updates und Monitoring, nicht nur Speicherplatz.", "sicherer zentraler Speicher für Teams"),
    ("netzwerk-segmentierung-leipzig", "Netzwerksegmentierung Leipzig", "Netzwerksegmentierung Leipzig", "Firmenkunden", "b2b", "Netzwerksicherheit", "Ungetrennte Netze erhöhen Risiken, wenn Gäste, IoT, Server und Arbeitsplätze alles sehen.", "klar getrennte Netzwerkbereiche"),
    ("bitlocker-verschluesselung-leipzig", "BitLocker Verschlüsselung Leipzig", "BitLocker Verschlüsselung Leipzig", "Firmenkunden", "b2b", "Endpoint Security", "Verlorene Laptops dürfen nicht automatisch verlorene Unternehmensdaten bedeuten.", "verschlüsselte Geräte mit verwalteten Wiederherstellungsschlüsseln"),
    ("remote-desktop-sicherheit-leipzig", "Remote Desktop Sicherheit Leipzig", "Remote Desktop Sicherheit Leipzig", "Firmenkunden", "b2b", "Remote Work", "Offene RDP-Zugänge sind ein häufiges Einfallstor für Angriffe.", "sichere Fernzugriffe ohne unnötige Angriffsfläche"),
    ("filialvernetzung-leipzig", "Filialvernetzung Leipzig", "Filialvernetzung Leipzig", "Firmenkunden", "b2b", "Netzwerk", "Mehrere Standorte brauchen stabile, sichere und zentral verwaltbare Verbindungen.", "zuverlässige Standortvernetzung für Teams"),
    ("wlan-gastnetz-leipzig", "WLAN-Gastnetz Leipzig", "WLAN Gastnetz Leipzig", "Firmenkunden", "b2b", "Netzwerk", "Gäste-WLAN darf Kundenkomfort bieten, ohne interne Systeme offenzulegen.", "sicher getrenntes Gäste-WLAN"),
    ("drucker-management-firma-leipzig", "Drucker Management für Firmen Leipzig", "Drucker Management Firma Leipzig", "Firmenkunden", "b2b", "Arbeitsplätze", "Druckerprobleme kosten im Alltag erstaunlich viel Zeit, besonders bei mehreren Standorten.", "einfachere Druckerbereitstellung und Support"),
    ("it-helpdesk-outsourcing-leipzig", "IT-Helpdesk Outsourcing Leipzig", "IT Helpdesk Outsourcing Leipzig", "Firmenkunden", "b2b", "IT-Support", "Interne Teams werden durch Standardanfragen, Passwortprobleme und Arbeitsplatzsupport blockiert.", "entlasteter Support mit klaren Reaktionswegen"),
    ("exchange-online-migration-leipzig", "Exchange Online Migration Leipzig", "Exchange Online Migration Leipzig", "Firmenkunden", "b2b", "Microsoft 365", "Lokale Exchange-Server sind wartungsintensiv und oft ein Sicherheitsrisiko.", "moderner E-Mail-Betrieb in Microsoft 365"),
    ("microsoft-defender-beratung-leipzig", "Microsoft Defender Beratung Leipzig", "Microsoft Defender Beratung Leipzig", "Firmenkunden", "b2b", "Endpoint Security", "Microsoft Defender bietet viel Schutz, muss aber korrekt konfiguriert und überwacht werden.", "besser genutzter Microsoft-Sicherheitsschutz"),
    ("proaktive-it-wartung-leipzig", "Proaktive IT-Wartung Leipzig", "Proaktive IT Wartung Leipzig", "Firmenkunden", "b2b", "Managed Services", "Reaktive IT kostet Nerven, wenn Probleme erst auffallen, sobald sie den Betrieb stören.", "laufend betreute IT mit weniger Überraschungen"),
]


B2C_TOPICS = [
    ("pc-hilfe-leipzig", "PC-Hilfe Leipzig", "PC Hilfe Leipzig", "Privatkunden", "b2c", "Computerhilfe", "Der PC macht Probleme, Programme starten nicht oder die Ursache ist unklar.", "schnelle Hilfe per Fernwartung oder vor Ort"),
    ("computerhilfe-leipzig", "Computerhilfe Leipzig", "Computerhilfe Leipzig", "Privatkunden", "b2c", "Computerhilfe", "Alltägliche Computerprobleme kosten Zeit und sind ohne Erfahrung schwer einzugrenzen.", "verständliche Unterstützung ohne Fachchinesisch"),
    ("pc-support-fernwartung-leipzig", "PC-Support per Fernwartung Leipzig", "PC Support Fernwartung Leipzig", "Privatkunden", "b2c", "Fernwartung", "Viele Software-, E-Mail- und Einstellungsprobleme lassen sich direkt aus der Ferne lösen.", "bequeme Hilfe ohne Anfahrt"),
    ("pc-langsam-leipzig", "PC langsam? Hilfe in Leipzig", "PC langsam Leipzig", "Privatkunden", "b2c", "Performance", "Der Computer startet langsam, reagiert träge oder hängt bei einfachen Aufgaben.", "spürbar schnelleres Arbeiten"),
    ("laptop-langsam-leipzig", "Laptop langsam? Hilfe in Leipzig", "Laptop langsam Leipzig", "Privatkunden", "b2c", "Performance", "Der Laptop braucht lange zum Starten, wird heiß oder ist im Alltag kaum nutzbar.", "saubere Diagnose und Optimierung"),
    ("windows-fehler-beheben-leipzig", "Windows Fehler beheben Leipzig", "Windows Fehler beheben Leipzig", "Privatkunden", "b2c", "Windows", "Windows meldet Fehler, startet nicht richtig oder zeigt Bluescreens.", "stabileres Windows-System"),
    ("windows-neuinstallation-leipzig", "Windows Neuinstallation Leipzig", "Windows Neuinstallation Leipzig", "Privatkunden", "b2c", "Windows", "Manchmal ist ein sauberer Neustart des Systems sinnvoller als endlose Reparaturversuche.", "saubere Installation mit Treibern und Updates"),
    ("windows-setup-hilfe-leipzig", "Windows Setup Hilfe Leipzig", "Windows Setup Hilfe Leipzig", "Privatkunden", "b2c", "Windows", "Ein neuer PC muss eingerichtet, aktualisiert und mit Programmen ausgestattet werden.", "fertig eingerichteter Windows-PC"),
    ("windows-update-probleme-leipzig", "Windows Update Probleme Leipzig", "Windows Update Probleme Leipzig", "Privatkunden", "b2c", "Windows", "Updates bleiben hängen, schlagen fehl oder verursachen neue Fehler.", "funktionierende Updates ohne Datenverlust"),
    ("outlook-hilfe-leipzig", "Outlook Hilfe Leipzig", "Outlook Hilfe Leipzig", "Privatkunden", "b2c", "E-Mail", "Outlook empfängt keine Mails, fragt ständig nach Passwörtern oder synchronisiert nicht.", "wieder funktionierende E-Mail-Kommunikation"),
    ("email-einrichten-leipzig", "E-Mail einrichten Leipzig", "E-Mail einrichten Leipzig", "Privatkunden", "b2c", "E-Mail", "Neue Mailkonten, Smartphones und Programme sollen richtig zusammenarbeiten.", "korrekt eingerichtete E-Mail auf Ihren Geräten"),
    ("thunderbird-hilfe-leipzig", "Thunderbird Hilfe Leipzig", "Thunderbird Hilfe Leipzig", "Privatkunden", "b2c", "E-Mail", "Thunderbird zeigt Fehler, lädt keine Nachrichten oder braucht ein neues Konto.", "saubere Thunderbird-Konfiguration"),
    ("drucker-einrichten-leipzig", "Drucker einrichten Leipzig", "Drucker einrichten Leipzig", "Privatkunden", "b2c", "Drucker", "Drucker, Scanner und WLAN-Verbindung sollen zuverlässig funktionieren.", "eingerichteter Drucker auf PC, Laptop oder Smartphone"),
    ("druckerprobleme-leipzig", "Druckerprobleme Leipzig", "Druckerprobleme Leipzig", "Privatkunden", "b2c", "Drucker", "Der Drucker ist offline, druckt nicht oder scannt nicht richtig.", "schnelle Fehlerbehebung bei Druck und Scan"),
    ("wlan-router-einrichten-leipzig", "WLAN-Router einrichten Leipzig", "WLAN Router einrichten Leipzig", "Privatkunden", "b2c", "Internet & WLAN", "Der Router muss eingerichtet, abgesichert oder mit Geräten verbunden werden.", "stabiles Heimnetz mit sicherem WLAN"),
    ("internet-langsam-leipzig", "Internet langsam Leipzig", "Internet langsam Leipzig", "Privatkunden", "b2c", "Internet & WLAN", "Webseiten laden langsam, Videokonferenzen ruckeln oder das WLAN bricht ab.", "bessere Verbindung und klare Fehlerursache"),
    ("smartphone-mit-pc-verbinden-leipzig", "Smartphone mit PC verbinden Leipzig", "Smartphone PC verbinden Leipzig", "Privatkunden", "b2c", "Geräte", "Fotos, Kontakte oder Dateien sollen zwischen Smartphone und Computer synchronisiert werden.", "saubere Verbindung zwischen Handy und PC"),
    ("datensicherung-privat-leipzig", "Datensicherung privat Leipzig", "Datensicherung privat Leipzig", "Privatkunden", "b2c", "Backup", "Fotos, Dokumente und Erinnerungen sollten nicht nur auf einem Gerät liegen.", "sichere private Backup-Lösung"),
    ("fotos-sichern-leipzig", "Fotos sichern Leipzig", "Fotos sichern Leipzig", "Privatkunden", "b2c", "Backup", "Familienfotos liegen oft verstreut auf Handy, PC, Cloud und Speicherkarten.", "geordnet gesicherte Fotos"),
    ("externe-festplatte-hilfe-leipzig", "Externe Festplatte Hilfe Leipzig", "Externe Festplatte Hilfe Leipzig", "Privatkunden", "b2c", "Speicher", "Die externe Festplatte wird nicht erkannt oder soll als Backup genutzt werden.", "funktionierende Festplatte oder klare Diagnose"),
    ("usb-stick-datenrettung-leipzig", "USB-Stick Datenrettung Leipzig", "USB Stick Datenrettung Leipzig", "Privatkunden", "b2c", "Datenrettung", "Wichtige Dateien auf einem USB-Stick sind gelöscht oder nicht mehr lesbar.", "realistische Datenrettungsprüfung"),
    ("sd-karte-datenrettung-leipzig", "SD-Karte Datenrettung Leipzig", "SD Karte Datenrettung Leipzig", "Privatkunden", "b2c", "Datenrettung", "Fotos oder Videos auf SD-Karten verschwinden oft nach Kamerafehlern oder Formatierung.", "Schonende Prüfung der Speicherkarte"),
    ("virus-entfernung-privat-leipzig", "Virus Entfernung privat Leipzig", "Virus Entfernung privat Leipzig", "Privatkunden", "b2c", "Sicherheit", "Popups, Warnungen oder unerklärliche Änderungen deuten auf Schadsoftware hin.", "sauberer Rechner und besserer Schutz"),
    ("malware-entfernung-leipzig", "Malware Entfernung Leipzig", "Malware Entfernung Leipzig", "Privatkunden", "b2c", "Sicherheit", "Malware kann Browser, Startseite, Werbung und Sicherheitseinstellungen manipulieren.", "entfernte Schadsoftware und geprüftes System"),
    ("phishing-hilfe-privat-leipzig", "Phishing Hilfe Leipzig", "Phishing Hilfe Leipzig", "Privatkunden", "b2c", "Sicherheit", "Nach einem verdächtigen Link oder Anhang ist schnelles, ruhiges Handeln wichtig.", "Kontoprüfung und nächste sichere Schritte"),
    ("passwort-hilfe-leipzig", "Passwort Hilfe Leipzig", "Passwort Hilfe Leipzig", "Privatkunden", "b2c", "Sicherheit", "Vergessene, unsichere oder mehrfach genutzte Passwörter machen den Alltag schwer.", "bessere Passwortstruktur und Kontoschutz"),
    ("microsoft-office-hilfe-leipzig", "Microsoft Office Hilfe Leipzig", "Microsoft Office Hilfe Leipzig", "Privatkunden", "b2c", "Office", "Word, Excel, Outlook oder PowerPoint funktionieren nicht wie erwartet.", "schnelle Hilfe bei Office-Problemen"),
    ("excel-hilfe-leipzig", "Excel Hilfe Leipzig", "Excel Hilfe Leipzig", "Privatkunden", "b2c", "Office", "Formeln, Tabellen, Formatierungen oder Dateien machen Probleme.", "verständliche Hilfe bei Excel-Dateien"),
    ("word-hilfe-leipzig", "Word Hilfe Leipzig", "Word Hilfe Leipzig", "Privatkunden", "b2c", "Office", "Word-Dokumente brauchen Layout, Korrektur, Formatierung oder Fehlerbehebung.", "saubere Word-Dokumente und Einstellungen"),
    ("powerpoint-hilfe-leipzig", "PowerPoint Hilfe Leipzig", "PowerPoint Hilfe Leipzig", "Privatkunden", "b2c", "Office", "Präsentationen sollen funktionieren, gut aussehen und sich öffnen lassen.", "fertige Präsentationen ohne Technikstress"),
    ("mac-hilfe-leipzig", "Mac Hilfe Leipzig", "Mac Hilfe Leipzig", "Privatkunden", "b2c", "Apple", "Mac, macOS, E-Mail, Drucker oder Programme verhalten sich ungewohnt.", "verständliche Hilfe für Apple-Systeme"),
    ("macbook-hilfe-leipzig", "MacBook Hilfe Leipzig", "MacBook Hilfe Leipzig", "Privatkunden", "b2c", "Apple", "Das MacBook ist langsam, hat Speicherprobleme oder braucht Einrichtung.", "stabiler MacBook-Alltag"),
    ("imac-hilfe-leipzig", "iMac Hilfe Leipzig", "iMac Hilfe Leipzig", "Privatkunden", "b2c", "Apple", "Ein iMac soll eingerichtet, gesichert oder bei Softwareproblemen geprüft werden.", "ein sauber eingerichteter iMac"),
    ("iphone-backup-hilfe-leipzig", "iPhone Backup Hilfe Leipzig", "iPhone Backup Hilfe Leipzig", "Privatkunden", "b2c", "Apple", "iPhone-Fotos, Kontakte und Backups sollen zuverlässig gesichert werden.", "sichere iPhone-Backups und Datenübertragung"),
    ("android-hilfe-leipzig", "Android Hilfe Leipzig", "Android Hilfe Leipzig", "Privatkunden", "b2c", "Mobilgeräte", "Android-Geräte brauchen Hilfe bei Konten, Fotos, Speicher oder Verbindung zum PC.", "besser eingerichtetes Android-Smartphone"),
    ("tablet-hilfe-leipzig", "Tablet Hilfe Leipzig", "Tablet Hilfe Leipzig", "Privatkunden", "b2c", "Mobilgeräte", "Tablets sollen für E-Mail, Video, Fotos oder Alltagseinsatz eingerichtet werden.", "ein verständlich eingerichtetes Tablet"),
    ("senioren-computerhilfe-leipzig", "Senioren Computerhilfe Leipzig", "Senioren Computerhilfe Leipzig", "Privatkunden", "b2c", "Lernen & Alltag", "Computerfragen brauchen manchmal besonders viel Ruhe und verständliche Erklärung.", "geduldige Hilfe Schritt für Schritt"),
    ("computerkurs-leipzig", "Computerkurs Leipzig", "Computerkurs Leipzig", "Privatkunden", "b2c", "Lernen & Alltag", "Viele Menschen möchten sicherer mit PC, Internet, E-Mail und Dateien umgehen.", "mehr Sicherheit im digitalen Alltag"),
    ("pc-einrichtung-zuhause-leipzig", "PC Einrichtung zuhause Leipzig", "PC Einrichtung zuhause Leipzig", "Privatkunden", "b2c", "Einrichtung", "Ein neuer Computer soll mit Internet, Drucker, E-Mail und Programmen funktionieren.", "startklar eingerichteter Computer"),
    ("laptop-einrichtung-leipzig", "Laptop Einrichtung Leipzig", "Laptop Einrichtung Leipzig", "Privatkunden", "b2c", "Einrichtung", "Ein neuer Laptop braucht Konten, Updates, Programme, Drucker und Schutz.", "fertig eingerichteter Laptop"),
    ("gaming-pc-hilfe-leipzig", "Gaming-PC Hilfe Leipzig", "Gaming PC Hilfe Leipzig", "Privatkunden", "b2c", "Hardware", "Gaming-PCs brauchen passende Treiber, Temperaturen, Leistung und stabile Updates.", "mehr Stabilität beim Spielen"),
    ("pc-aufruesten-leipzig", "PC aufrüsten Leipzig", "PC aufrüsten Leipzig", "Privatkunden", "b2c", "Hardware", "Ein älterer PC kann durch gezielte Upgrades oft deutlich länger genutzt werden.", "mehr Leistung ohne unnötigen Neukauf"),
    ("ssd-upgrade-leipzig", "SSD Upgrade Leipzig", "SSD Upgrade Leipzig", "Privatkunden", "b2c", "Hardware", "Eine SSD macht viele ältere PCs und Laptops spürbar schneller.", "schnellerer Start und kürzere Ladezeiten"),
    ("ram-aufruestung-leipzig", "RAM Aufrüstung Leipzig", "RAM Aufrüstung Leipzig", "Privatkunden", "b2c", "Hardware", "Zu wenig Arbeitsspeicher macht Multitasking, Browser und Office langsam.", "passender Arbeitsspeicher für bessere Leistung"),
    ("bios-uefi-hilfe-leipzig", "BIOS & UEFI Hilfe Leipzig", "BIOS UEFI Hilfe Leipzig", "Privatkunden", "b2c", "Hardware", "Bootreihenfolge, Secure Boot oder Firmware-Einstellungen können schnell verwirren.", "korrekte Grundeinstellungen ohne Risiko"),
    ("bluescreen-hilfe-leipzig", "Bluescreen Hilfe Leipzig", "Bluescreen Hilfe Leipzig", "Privatkunden", "b2c", "Windows", "Bluescreens deuten auf Treiber, Hardware, Speicher oder Windows-Probleme hin.", "gezielte Diagnose statt Rätselraten"),
    ("browser-probleme-leipzig", "Browser Probleme Leipzig", "Browser Probleme Leipzig", "Privatkunden", "b2c", "Internet & Browser", "Browser starten langsam, zeigen Werbung oder öffnen Seiten nicht richtig.", "sauberer Browser und sicherere Einstellungen"),
    ("chrome-firefox-hilfe-leipzig", "Chrome & Firefox Hilfe Leipzig", "Chrome Firefox Hilfe Leipzig", "Privatkunden", "b2c", "Internet & Browser", "Erweiterungen, Profile, Passwörter und Synchronisierung können Probleme verursachen.", "funktionierende Browser ohne Datenchaos"),
    ("zoom-teams-hilfe-privat-leipzig", "Zoom & Teams Hilfe privat Leipzig", "Zoom Teams Hilfe privat Leipzig", "Privatkunden", "b2c", "Video & Kommunikation", "Videoanrufe scheitern oft an Kamera, Mikrofon, Konto oder Berechtigungen.", "funktionierende Videotelefonie"),
    ("smart-home-wlan-hilfe-leipzig", "Smart Home & WLAN Hilfe Leipzig", "Smart Home WLAN Hilfe Leipzig", "Privatkunden", "b2c", "Smart Home", "Smart-Home-Geräte brauchen stabiles WLAN, Apps und sichere Konten.", "zuverlässig verbundenes Smart Home"),
]


def make_topic(row: tuple[str, ...]) -> PageTopic:
    slug, title, keyword, audience, segment, category, problem, outcome = row
    if segment == "b2b":
        deliverables = (
            f"Analyse der bestehenden Umgebung und der wichtigsten Risiken rund um {keyword}.",
            "Konzept, Einrichtung und Dokumentation mit klaren Verantwortlichkeiten.",
            "Sichere Umsetzung inklusive Tests, Übergabe und verständlicher Empfehlung.",
            "Optionale laufende Betreuung durch UKNS als externer IT-Partner.",
        )
        hub = "/it-service-leipzig/"
        cta = "Beratung für Unternehmen anfragen"
    else:
        deliverables = (
            "Kurze Ersteinschätzung Ihres Problems und ein nachvollziehbarer Lösungsvorschlag.",
            "Hilfe per Fernwartung, telefonisch oder nach Absprache vor Ort in Leipzig.",
            "Saubere Einrichtung, Reparatur oder Optimierung ohne unnötige Fachsprache.",
            "Tipps, damit das Problem möglichst nicht direkt wieder auftaucht.",
        )
        hub = "/computer-reparatur-leipzig/"
        cta = "Computerhilfe anfragen"
    return PageTopic(slug, title, keyword, audience, segment, category, problem, outcome, deliverables, hub, cta)


TOPICS = [make_topic(t) for t in B2B_TOPICS + B2C_TOPICS]


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    line = ""
    for word in words:
        test = f"{line} {word}".strip()
        width = draw.textbbox((0, 0), test, font=font)[2]
        if width <= max_width or not line:
            line = test
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def palette(topic: PageTopic) -> tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]:
    digest = hashlib.sha256(topic.slug.encode("utf-8")).digest()
    if topic.segment == "b2b":
        base = (28 + digest[0] % 28, 45 + digest[1] % 40, 120 + digest[2] % 70)
        accent = (255, 204, 0)
    else:
        base = (34 + digest[0] % 40, 92 + digest[1] % 60, 126 + digest[2] % 70)
        accent = (255, 204, 0)
    second = (min(255, base[0] + 38), min(255, base[1] + 42), min(255, base[2] + 46))
    return base, second, accent


def generate_image(topic: PageTopic) -> None:
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    base, second, accent = palette(topic)
    w, h = 1200, 675
    img = Image.new("RGB", (w, h), base)
    pix = img.load()
    for y in range(h):
        for x in range(w):
            t = (x / w * 0.68) + (y / h * 0.32)
            wave = int(16 * math.sin((x + y) / 85))
            pix[x, y] = (
                int(base[0] * (1 - t) + second[0] * t) + wave // 3,
                int(base[1] * (1 - t) + second[1] * t) + wave // 3,
                int(base[2] * (1 - t) + second[2] * t) + wave // 3,
            )
    draw = ImageDraw.Draw(img, "RGBA")
    for i in range(18):
        x = 80 + (i * 137) % 1100
        y = 60 + (i * 91) % 560
        r = 34 + (i * 13) % 76
        draw.ellipse((x - r, y - r, x + r, y + r), outline=(255, 255, 255, 34), width=2)
    for i in range(14):
        x1 = (i * 173) % w
        y1 = (i * 97) % h
        x2 = (x1 + 210 + i * 17) % w
        y2 = (y1 + 120 + i * 23) % h
        draw.line((x1, y1, x2, y2), fill=(255, 255, 255, 38), width=2)
        draw.ellipse((x2 - 5, y2 - 5, x2 + 5, y2 + 5), fill=accent + (190,))

    draw.rounded_rectangle((70, 70, 1130, 605), radius=30, fill=(7, 15, 42, 72), outline=(255, 255, 255, 60), width=2)
    draw.rounded_rectangle((92, 92, 360, 142), radius=25, fill=accent + (255,))
    label = "FIRMENKUNDEN" if topic.segment == "b2b" else "PRIVATKUNDEN"
    draw.text((122, 105), label, font=font(23, True), fill=(43, 57, 144, 255))
    title_font = font(58, True)
    lines = wrap_text(draw, topic.title, title_font, 940)
    y = 210
    for line in lines[:3]:
        draw.text((105, y), line, font=title_font, fill=(255, 255, 255, 255))
        y += 68
    small_font = font(28, False)
    sub = f"{topic.category} · Leipzig"
    draw.text((105, 520), sub, font=small_font, fill=(235, 240, 255, 235))
    draw.text((105, 555), "UKNS IT-Premium Services", font=font(23, True), fill=accent + (255,))

    for size in (1200, 800, 480):
        resized = img if size == 1200 else img.resize((size, int(size * h / w)), Image.Resampling.LANCZOS)
        jpg = IMAGE_DIR / f"{topic.slug}-{size}.jpg"
        webp = IMAGE_DIR / f"{topic.slug}-{size}.webp"
        resized.save(jpg, quality=82, optimize=True)
        resized.save(webp, quality=78, method=6)


def generate_detail_image(topic: PageTopic) -> None:
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    base, second, accent = palette(topic)
    w, h = 1200, 760
    img = Image.new("RGB", (w, h), (246, 248, 252))
    draw = ImageDraw.Draw(img, "RGBA")

    draw.rounded_rectangle((48, 48, 1152, 712), radius=34, fill=(255, 255, 255, 255), outline=(214, 221, 235, 255), width=2)
    draw.rounded_rectangle((82, 82, 1118, 250), radius=26, fill=base + (255,))
    draw.ellipse((960, -20, 1220, 240), fill=second + (105,))
    draw.ellipse((760, 48, 920, 208), outline=(255, 255, 255, 58), width=3)
    draw.text((112, 114), "FIRMEN-IT" if topic.segment == "b2b" else "COMPUTERHILFE", font=font(24, True), fill=accent + (255,))
    title_font = font(38, True)
    title_lines = wrap_text(draw, topic.title, title_font, 790)
    y = 148
    for line in title_lines[:2]:
        draw.text((112, y), line, font=title_font, fill=(255, 255, 255, 255))
        y += 44

    # Laptop/dashboard visual.
    draw.rounded_rectangle((105, 300, 575, 585), radius=28, fill=(24, 32, 62, 255))
    draw.rounded_rectangle((132, 330, 548, 552), radius=18, fill=(250, 252, 255, 255))
    draw.rounded_rectangle((175, 602, 505, 628), radius=13, fill=(111, 124, 150, 255))
    for i, color in enumerate([(43, 57, 144, 255), accent + (255,), second + (255,)]):
        x = 166 + i * 118
        draw.rounded_rectangle((x, 376, x + 82, 492), radius=18, fill=color)
        draw.ellipse((x + 24, 402, x + 58, 436), fill=(255, 255, 255, 170))
        draw.rectangle((x + 20, 456, x + 62, 464), fill=(255, 255, 255, 180))
    for i in range(4):
        y_line = 350 + i * 42
        draw.rounded_rectangle((415, y_line, 515, y_line + 12), radius=6, fill=(214, 221, 235, 255))

    labels = (
        ("01", "Analyse", "Situation verstehen und Risiken sortieren"),
        ("02", "Umsetzung", "sauber einrichten, testen und absichern"),
        ("03", "Übergabe", "verständlich erklären und dokumentieren"),
    )
    if topic.segment == "b2c":
        labels = (
            ("01", "Einordnen", "Problem ruhig ansehen und Ursache finden"),
            ("02", "Lösen", "Daten schützen und Technik reparieren"),
            ("03", "Erklären", "verständlich zeigen, was künftig hilft"),
        )
    for i, (number, title, body) in enumerate(labels):
        top = 300 + i * 125
        draw.rounded_rectangle((640, top, 1088, top + 106), radius=22, fill=(255, 255, 255, 255), outline=(216, 224, 239, 255), width=2)
        draw.ellipse((668, top + 29, 716, top + 77), fill=base + (255,))
        draw.text((692, top + 53), number, font=font(16, True), fill=(255, 255, 255, 255), anchor="mm")
        draw.text((742, top + 20), title, font=font(28, True), fill=(43, 57, 144, 255))
        body_lines = wrap_text(draw, body, font(19, False), 310)
        body_y = top + 54
        for body_line in body_lines[:2]:
            draw.text((742, body_y), body_line, font=font(19, False), fill=(71, 84, 103, 255))
            body_y += 23

    draw.rounded_rectangle((105, 655, 575, 682), radius=13, fill=accent + (255,))
    draw.text((126, 658), f"{topic.category} · UKNS Leipzig", font=font(18, True), fill=(43, 57, 144, 255))

    for size in (1200, 800, 480):
        resized = img if size == 1200 else img.resize((size, int(size * h / w)), Image.Resampling.LANCZOS)
        jpg = IMAGE_DIR / f"{topic.slug}-detail-{size}.jpg"
        webp = IMAGE_DIR / f"{topic.slug}-detail-{size}.webp"
        resized.save(jpg, quality=84, optimize=True)
        resized.save(webp, quality=80, method=6)


def trim_meta(text: str, limit: int = 158) -> str:
    if len(text) <= limit:
        return text
    shortened = text[: limit - 1].rsplit(" ", 1)[0].rstrip(" ,;:")
    return shortened + "."


def meta_title(topic: PageTopic) -> str:
    suffix = "Beratung & Umsetzung in Leipzig | UKNS" if topic.segment == "b2b" else "Hilfe verständlich in Leipzig | UKNS"
    add = "IT-Service Leipzig" if topic.segment == "b2b" else "Computerhilfe Leipzig"
    options = [
        f"{topic.title}: {suffix}",
        f"{topic.keyword}: {suffix}",
        f"{topic.title}: {add} | UKNS",
        f"{topic.keyword}: {add} | UKNS",
        f"{topic.title} | UKNS",
    ]
    for candidate in options:
        if 45 <= len(candidate) <= 70:
            return candidate
    for candidate in options:
        if len(candidate) <= 70:
            return candidate
    compact = f"{topic.keyword}: Leipzig | UKNS"
    return compact[:70].rsplit(" ", 1)[0].rstrip(" ,;:")


def meta_description(topic: PageTopic) -> str:
    if topic.segment == "b2b":
        text = f"{topic.title}: UKNS hilft Unternehmen in Leipzig mit Analyse, Umsetzung, Sicherheit und klarer Übergabe. Jetzt unverbindlich beraten lassen."
    else:
        text = f"{topic.title}: verständliche Hilfe in Leipzig bei Einrichtung, Fehlern, Internet, E-Mail, Sicherheit und digitalen Alltagsproblemen."
    return trim_meta(text)


def related_topics(topic: PageTopic) -> list[PageTopic]:
    pool = [t for t in TOPICS if t.segment == topic.segment and t.slug != topic.slug]
    same = [t for t in pool if t.category == topic.category]
    rest = [t for t in pool if t.category != topic.category]
    return (same + rest)[:3]


def faq(topic: PageTopic) -> tuple[tuple[str, str], ...]:
    if topic.segment == "b2b":
        return (
            (f"Für welche Unternehmen eignet sich {topic.keyword}?", f"{topic.keyword} eignet sich besonders für kleine und mittelständische Unternehmen in Leipzig, die ihre IT planbarer, sicherer und besser dokumentiert betreiben möchten."),
            (f"Kann UKNS {topic.keyword} laufend betreuen?", f"Ja. UKNS kann die Einrichtung übernehmen und die Lösung anschließend im Rahmen von IT-Service, Managed Services oder Wartungsverträgen weiter betreuen."),
            ("Wie starten wir sinnvoll?", "Am besten mit einer kurzen Bestandsaufnahme: Was funktioniert heute, wo gibt es wiederkehrende Störungen und welche Systeme wären bei einem Ausfall wirklich kritisch? Daraus entsteht eine klare Reihenfolge."),
        )
    return (
        (f"Kann UKNS bei {topic.keyword} per Fernwartung helfen?", f"Viele Probleme rund um {topic.keyword} lassen sich per Fernwartung lösen. Wenn Hardware oder Vor-Ort-Arbeit nötig ist, besprechen wir den passenden nächsten Schritt."),
        (f"Was kostet Hilfe bei {topic.keyword}?", "Die Kosten hängen vom Aufwand ab. Sie erhalten zuerst eine verständliche Einschätzung, bevor kostenpflichtige Arbeiten starten."),
        ("Muss ich mich mit Technik gut auskennen?", "Nein. Es reicht, wenn Sie beschreiben, was Sie sehen oder was nicht mehr funktioniert. Wir fragen ruhig nach und erklären die Schritte ohne unnötige Fachbegriffe."),
    )


def story_paragraphs(topic: PageTopic) -> tuple[str, str, str]:
    if topic.segment == "b2b":
        category_text = {
            "Microsoft 365": "Bei Microsoft 365 geht es selten nur um Lizenzen. Entscheidend ist, ob Dateien, Postfächer, Teams-Strukturen, Rechte und Wiederherstellung zusammenpassen.",
            "Cloud": "Cloud ist dann sinnvoll, wenn Kosten, Sicherheit und Zugriff sauber geplant werden. Eine schnelle Migration ohne Konzept verschiebt Probleme nur an einen anderen Ort.",
            "Managed Services": "Laufende Betreuung ist besonders wertvoll, wenn Störungen nicht erst auffallen sollen, sobald jemand nicht mehr arbeiten kann.",
            "IT-Betrieb": "Im IT-Betrieb zählt Überblick. Ohne saubere Inventarisierung, Zuständigkeiten und Dokumentation werden kleine Aufgaben schnell zu langen Suchaktionen.",
            "Endpoint Security": "Endpoint-Schutz muss nicht nur installiert, sondern überwacht, aktuell gehalten und verständlich ausgewertet werden.",
            "Netzwerk": "Netzwerkprobleme wirken oft diffus: langsame Programme, abbrechende Telefonie oder WLAN-Lücken. Gute Analyse trennt Ursache von Bauchgefühl.",
            "Netzwerksicherheit": "Sichere Netzwerkgrenzen entstehen nicht durch eine einzelne Firewall-Regel, sondern durch Updates, Rechte, VPN, Segmentierung und regelmäßige Prüfung.",
            "Remote Work": "Homeoffice-Zugänge müssen bequem genug für den Alltag und streng genug für Unternehmensdaten sein.",
            "Backup": "Ein Backup beruhigt erst dann wirklich, wenn auch die Wiederherstellung getestet wurde.",
            "Notfallplanung": "Notfallplanung ist kein Ordner für die Schublade. Sie muss im Ernstfall von Menschen verstanden und genutzt werden können.",
            "Arbeitsplätze": "Standardisierte Arbeitsplätze sparen Zeit, weil neue Geräte nicht jedes Mal neu erfunden werden müssen.",
            "Schulung": "Sicherheitsschulungen funktionieren besser, wenn sie echte Situationen aus dem Arbeitsalltag aufgreifen statt abstrakte Regeln zu sammeln.",
        }.get(topic.category, "Wichtig ist ein Vorgehen, das zu Größe, Risiko und Arbeitsalltag des Unternehmens passt.")
        return (
            "Wie das Thema im Alltag auftaucht",
            f"{topic.problem} Häufig beginnt das nicht als großes IT-Projekt, sondern als wiederkehrender Zeitverlust: jemand sucht Zugangsdaten, ein Dienst fällt aus, ein neues Gerät dauert zu lange oder niemand weiß sicher, ob die letzte Änderung dokumentiert wurde.",
            category_text,
        )
    category_text = {
        "Windows": "Bei Windows-Problemen ist Geduld wichtiger als blindes Klicken. Erst wird geprüft, ob Daten, Benutzerprofil, Updates oder Hardware betroffen sind.",
        "Performance": "Ein langsamer Rechner muss nicht automatisch ersetzt werden. Oft zeigen Autostart, Speicher, Festplatte oder veraltete Programme, was wirklich bremst.",
        "Hardware": "Bei Hardware-Fragen ist eine ehrliche Einschätzung wichtig: Reparieren, aufrüsten oder lieber nichts mehr investieren.",
        "E-Mail": "E-Mail-Probleme sind besonders nervig, weil sie sofort den Alltag treffen. Wir prüfen Konto, Passwort, Serverdaten und Geräte Schritt für Schritt.",
        "Drucker": "Druckerprobleme wirken banal, kosten aber erstaunlich viel Zeit. Meist spielen Verbindung, Treiber, Warteschlange oder WLAN zusammen.",
        "Internet & WLAN": "Wenn Internet oder WLAN zickt, liegt die Ursache nicht immer beim Anbieter. Router, Funkabdeckung, Geräte und Einstellungen müssen zusammen betrachtet werden.",
        "Sicherheit": "Bei Viren, Phishing oder Passwortproblemen geht es zuerst darum, Ruhe zu bewahren und keine wichtigen Spuren zu verwischen.",
        "Datenrettung": "Bei Datenverlust zählt vorsichtiges Vorgehen. Je weniger ausprobiert wird, desto besser stehen oft die Chancen.",
        "Apple": "Auch bei Mac, iPhone oder iPad geht es nicht um Fachbegriffe, sondern um saubere Synchronisation, Backups und verständliche Einstellungen.",
        "Mobilgeräte": "Smartphone- und Tablet-Hilfe soll den Alltag leichter machen: Fotos sichern, Konten verbinden, Apps einrichten und Geräte verständlich koppeln.",
        "Office": "Office-Hilfe ist am besten, wenn am Ende nicht nur ein Dokument funktioniert, sondern Sie den nächsten Schritt selbst wiederfinden.",
    }.get(topic.category, "Viele private Technikprobleme sind lösbar, wenn man ruhig sortiert und nicht zehn Dinge gleichzeitig ausprobiert.")
    return (
        "Wie sich das Problem meistens bemerkbar macht",
        f"{topic.problem} Oft ist gar nicht klar, ob es an Gerät, Programm, Konto, Internet oder einer Einstellung liegt. Genau deshalb lohnt eine ruhige Einordnung, bevor Daten, Passwörter oder wichtige Einstellungen verändert werden.",
        category_text,
    )


def quality_points(topic: PageTopic) -> tuple[str, str, str]:
    if topic.segment == "b2b":
        return (
            "Wir priorisieren nach Betriebsrisiko, nicht nach Buzzwords.",
            "Sie bekommen eine verständliche Übergabe statt loser technischer Einzelnotizen.",
            "Empfehlungen werden so formuliert, dass Geschäftsführung und Team damit arbeiten können.",
        )
    return (
        "Wir erklären, was wir tun, bevor wir wichtige Einstellungen ändern.",
        "Wir achten auf Daten, Fotos, Passwörter und persönliche Konten.",
        "Wir sagen ehrlich, wenn eine Reparatur wirtschaftlich wenig Sinn ergibt.",
    )


def prep_points(topic: PageTopic) -> tuple[str, str, str]:
    if topic.segment == "b2b":
        return (
            "Welche Systeme oder Arbeitsplätze sind aktuell betroffen?",
            "Welche Änderung, Störung oder neue Anforderung war der Auslöser?",
            "Wer muss nach der Lösung damit arbeiten oder sie freigeben?",
        )
    return (
        "Welche Meldung erscheint und seit wann tritt sie auf?",
        "Welche Geräte, Konten oder Programme sind beteiligt?",
        "Gibt es wichtige Daten, die vor jeder Reparatur geschützt werden sollen?",
    )


def visual_points(topic: PageTopic) -> tuple[str, tuple[str, str, str]]:
    if topic.segment == "b2b":
        return (
            "Der Ablauf als visuelle Orientierung",
            (
                "Systeme, Verträge, Geräte und Zugänge werden zuerst sichtbar gemacht.",
                "Risiken und schnelle Verbesserungen werden nach Wirkung priorisiert.",
                "Die Umsetzung wird so dokumentiert, dass Ihr Team später nicht raten muss.",
            ),
        )
    return (
        "So wird aus einem Technikproblem wieder Alltag",
        (
            "Wir klären zuerst ruhig, was tatsächlich nicht funktioniert.",
            "Wichtige Daten, Konten und Einstellungen werden nicht unnötig gefährdet.",
            "Zum Abschluss erklären wir verständlich, was geändert wurde.",
        ),
    )


def ai_detail_stem(topic: PageTopic) -> str:
    page_specific = f"{topic.slug}-ai-detail"
    if (IMAGE_DIR / f"{page_specific}-1200.jpg").exists():
        return page_specific

    if topic.segment == "b2b":
        category_map = {
            "Microsoft 365": "ai-b2b-microsoft-cloud",
            "Cloud": "ai-b2b-microsoft-cloud",
            "Kommunikation": "ai-b2b-microsoft-cloud",
            "E-Mail & Compliance": "ai-b2b-microsoft-cloud",
            "E-Mail-Sicherheit": "ai-b2b-microsoft-cloud",
            "Compliance & Security": "ai-b2b-security",
            "Endpoint Security": "ai-b2b-security",
            "Identität & Zugriff": "ai-b2b-security",
            "Netzwerksicherheit": "ai-b2b-security",
            "Security": "ai-b2b-security",
            "Security Audit": "ai-b2b-security",
            "Schulung": "ai-b2b-security",
            "Managed Services": "ai-b2b-managed-operations",
            "IT-Betrieb": "ai-b2b-managed-operations",
            "IT-Support": "ai-b2b-managed-operations",
            "Netzwerk": "ai-b2b-network-infrastructure",
            "Infrastruktur": "ai-b2b-network-infrastructure",
            "Server": "ai-b2b-network-infrastructure",
            "Web & Infrastruktur": "ai-b2b-network-infrastructure",
            "Backup": "ai-b2b-backup-continuity",
            "Notfallplanung": "ai-b2b-backup-continuity",
            "Speicher & Backup": "ai-b2b-backup-continuity",
            "Arbeitsplätze": "ai-b2b-workplace-devices",
            "Moderner Arbeitsplatz": "ai-b2b-workplace-devices",
            "Remote Work": "ai-b2b-workplace-devices",
            "IT-Prozesse": "ai-b2b-workplace-devices",
        }
    else:
        category_map = {
            "Computerhilfe": "ai-b2c-computer-help",
            "Fernwartung": "ai-b2c-computer-help",
            "Einrichtung": "ai-b2c-computer-help",
            "Lernen & Alltag": "ai-b2c-computer-help",
            "Windows": "ai-b2c-windows-performance",
            "Performance": "ai-b2c-windows-performance",
            "Hardware": "ai-b2c-windows-performance",
            "E-Mail": "ai-b2c-email-office",
            "Office": "ai-b2c-email-office",
            "Internet & Browser": "ai-b2c-email-office",
            "Video & Kommunikation": "ai-b2c-email-office",
            "Drucker": "ai-b2c-printer-wifi",
            "Internet & WLAN": "ai-b2c-printer-wifi",
            "Smart Home": "ai-b2c-printer-wifi",
            "Backup": "ai-b2c-data-security",
            "Datenrettung": "ai-b2c-data-security",
            "Sicherheit": "ai-b2c-data-security",
            "Speicher": "ai-b2c-data-security",
            "Apple": "ai-b2c-mobile-apple",
            "Mobilgeräte": "ai-b2c-mobile-apple",
            "Geräte": "ai-b2c-mobile-apple",
        }

    candidate = category_map.get(topic.category, f"{topic.slug}-detail")
    if (IMAGE_DIR / f"{candidate}-1200.jpg").exists():
        return candidate
    return f"{topic.slug}-detail"


def lifestyle_image_stem(topic: PageTopic) -> str | None:
    page_specific = f"{topic.slug}-lifestyle"
    if (IMAGE_DIR / f"{page_specific}-1200.jpg").exists():
        return page_specific
    if topic.segment == "b2b":
        category_map = {
            "Microsoft 365": "ai-lifestyle-b2b-cloud-workplace",
            "Cloud": "ai-lifestyle-b2b-cloud-workplace",
            "Kommunikation": "ai-lifestyle-b2b-cloud-workplace",
            "E-Mail & Compliance": "ai-lifestyle-b2b-cloud-workplace",
            "E-Mail-Sicherheit": "ai-lifestyle-b2b-cloud-workplace",
            "Compliance & Security": "ai-lifestyle-b2b-security",
            "Endpoint Security": "ai-lifestyle-b2b-security",
            "Identität & Zugriff": "ai-lifestyle-b2b-security",
            "Netzwerksicherheit": "ai-lifestyle-b2b-security",
            "Security": "ai-lifestyle-b2b-security",
            "Security Audit": "ai-lifestyle-b2b-security",
            "Schulung": "ai-lifestyle-b2b-security",
            "Managed Services": "ai-lifestyle-b2b-managed-it",
            "IT-Betrieb": "ai-lifestyle-b2b-managed-it",
            "IT-Support": "ai-lifestyle-b2b-managed-it",
            "Netzwerk": "ai-lifestyle-b2b-managed-it",
            "Infrastruktur": "ai-lifestyle-b2b-managed-it",
            "Server": "ai-lifestyle-b2b-managed-it",
            "Web & Infrastruktur": "ai-lifestyle-b2b-managed-it",
            "Backup": "ai-lifestyle-b2b-managed-it",
            "Notfallplanung": "ai-lifestyle-b2b-managed-it",
            "Speicher & Backup": "ai-lifestyle-b2b-managed-it",
            "Arbeitsplätze": "ai-lifestyle-b2b-managed-it",
            "Moderner Arbeitsplatz": "ai-lifestyle-b2b-managed-it",
            "Remote Work": "ai-lifestyle-b2b-managed-it",
            "IT-Prozesse": "ai-lifestyle-b2b-managed-it",
        }
    else:
        category_map = {
            "Computerhilfe": "ai-lifestyle-b2c-computer-help",
            "Fernwartung": "ai-lifestyle-b2c-computer-help",
            "Einrichtung": "ai-lifestyle-b2c-computer-help",
            "Lernen & Alltag": "ai-lifestyle-b2c-computer-help",
            "Windows": "ai-lifestyle-b2c-computer-help",
            "Performance": "ai-lifestyle-b2c-computer-help",
            "Hardware": "ai-lifestyle-b2c-computer-help",
            "E-Mail": "ai-lifestyle-b2c-computer-help",
            "Office": "ai-lifestyle-b2c-computer-help",
            "Internet & Browser": "ai-lifestyle-b2c-computer-help",
            "Video & Kommunikation": "ai-lifestyle-b2c-computer-help",
            "Drucker": "druckerprobleme-leipzig-lifestyle",
            "Internet & WLAN": "druckerprobleme-leipzig-lifestyle",
            "Smart Home": "druckerprobleme-leipzig-lifestyle",
            "Backup": "ai-lifestyle-b2c-data-backup",
            "Datenrettung": "ai-lifestyle-b2c-data-backup",
            "Sicherheit": "ai-lifestyle-b2c-data-backup",
            "Speicher": "ai-lifestyle-b2c-data-backup",
            "Apple": "ai-lifestyle-b2c-mobile-devices",
            "Mobilgeräte": "ai-lifestyle-b2c-mobile-devices",
            "Geräte": "ai-lifestyle-b2c-mobile-devices",
        }
    candidate = category_map.get(topic.category)
    if candidate and (IMAGE_DIR / f"{candidate}-1200.jpg").exists():
        return candidate
    return None


def lifestyle_copy(topic: PageTopic) -> tuple[str, str, str, str, str]:
    if topic.category == "Drucker":
        return (
            "Entspannter Technikalltag",
            "Druckerhilfe darf ruhig aussehen",
            "Oft reicht ein sauberer Blick auf WLAN, Warteschlange, Treiber und Ger\u00e4t. Das zus\u00e4tzliche Bild macht den Abschnitt weniger trocken und zeigt direkt, worum es geht: Drucken, Scannen und Verbinden ohne Stress.",
            "Was wir im Blick behalten",
            "Verbindung, Standarddrucker, Papierlauf, Scanprofil und die Ger\u00e4te, die wirklich im Haushalt genutzt werden.",
        )
    if topic.segment == "b2b":
        return (
            "Moderner Arbeitsalltag",
            "IT soll Arbeit leiser machen",
            "Ein gutes Setup f\u00e4llt im Alltag kaum auf: Systeme laufen stabil, Zust\u00e4ndigkeiten sind klar und kleine Probleme werden fr\u00fch sichtbar. Genau daf\u00fcr setzen wir Technik, Dokumentation und Service zusammen.",
            "Der praktische Blick",
            "Wir achten nicht nur auf Tools, sondern auf Menschen, Abl\u00e4ufe, Verantwortlichkeiten und die Frage, was im Tagesgesch\u00e4ft wirklich hilft.",
        )
    return (
        "Lockerer Technikalltag",
        "Technik soll sich wieder leicht anf\u00fchlen",
        "Ob Einrichtung, Fehlerbehebung oder Sicherheit: Gute Hilfe nimmt Druck aus dem Thema und macht die n\u00e4chsten Schritte verst\u00e4ndlich. So bleibt nicht nur das Ger\u00e4t, sondern auch der Alltag besser nutzbar.",
        "Worauf es ankommt",
        "Wir schauen auf die konkrete Situation zuhause, wichtige Daten, vorhandene Ger\u00e4te und darauf, dass Sie die L\u00f6sung danach nachvollziehen k\u00f6nnen.",
    )


def page_html(topic: PageTopic) -> str:
    rels = related_topics(topic)
    faqs = faq(topic)
    img = f"/images/generated/{topic.slug}-1200.jpg"
    webp = f"/images/generated/{topic.slug}-1200.webp"
    detail_stem = ai_detail_stem(topic)
    lifestyle_stem = lifestyle_image_stem(topic)
    visual_title, visual_bullets = visual_points(topic)
    story_title, story_intro, story_detail = story_paragraphs(topic)
    canonical = f"{SITE_URL}/{topic.slug}/"
    schema = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": topic.title,
        "serviceType": topic.keyword,
        "areaServed": {"@type": "City", "name": "Leipzig"},
        "provider": {
            "@type": "LocalBusiness",
            "name": "UKNS IT-Premium Services",
            "url": SITE_URL,
            "telephone": "",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Friedrich-Ebert-Straße 85",
                "postalCode": "04109",
                "addressLocality": "Leipzig",
                "addressCountry": "DE",
            },
        },
        "description": meta_description(topic),
        "audience": {"@type": "Audience", "audienceType": topic.audience},
        "url": canonical,
    }
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }
    breadcrumbs = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Startseite", "item": f"{SITE_URL}/"},
            {"@type": "ListItem", "position": 2, "name": "IT-Wissen", "item": f"{SITE_URL}/it-wissen/"},
            {"@type": "ListItem", "position": 3, "name": topic.title, "item": canonical},
        ],
    }
    cards = "\n".join(
        f'<a class="related-card" href="/{esc(r.slug)}/"><span>{esc(r.category)}</span><strong>{esc(r.title)}</strong><small>{esc(r.outcome)}</small></a>'
        for r in rels
    )
    deliverables = "\n".join(f"<li>{esc(item)}</li>" for item in topic.deliverables)
    visual_items = "\n".join(f"<li>{esc(item)}</li>" for item in visual_bullets)
    quality_items = "\n".join(f"<li>{esc(item)}</li>" for item in quality_points(topic))
    prep_items = "\n".join(f"<li>{esc(item)}</li>" for item in prep_points(topic))
    faq_items = "\n".join(
        f"<div class=\"faq-item\"><h3>{esc(q)}</h3><p>{esc(a)}</p></div>" for q, a in faqs
    )
    lifestyle_section = ""
    if lifestyle_stem:
        life_eyebrow, life_title, life_intro, life_note_title, life_note = lifestyle_copy(topic)
        lifestyle_section = f"""
<section id="lockerer-eindruck" class="content-section lifestyle-section" style="padding-top:0">
  <div class="seo-container lifestyle-grid">
    <picture class="lifestyle-picture">
      <source type="image/webp" srcset="/images/generated/{lifestyle_stem}-480.webp 480w, /images/generated/{lifestyle_stem}-800.webp 800w, /images/generated/{lifestyle_stem}-1200.webp 1200w" sizes="(min-width: 900px) 58vw, 100vw"/>
      <img class="lifestyle-image" src="/images/generated/{lifestyle_stem}-1200.jpg" srcset="/images/generated/{lifestyle_stem}-480.jpg 480w, /images/generated/{lifestyle_stem}-800.jpg 800w, /images/generated/{lifestyle_stem}-1200.jpg 1200w" sizes="(min-width: 900px) 58vw, 100vw" width="1200" height="750" alt="{esc(life_title)} - {esc(topic.title)}" loading="lazy" decoding="async"/>
    </picture>
    <article class="lifestyle-copy">
      <span class="lifestyle-eyebrow">{esc(life_eyebrow)}</span>
      <h2>{esc(life_title)}</h2>
      <p>{esc(life_intro)}</p>
      <div class="lifestyle-note">
        <strong>{esc(life_note_title)}</strong>
        <p>{esc(life_note)}</p>
      </div>
    </article>
  </div>
</section>"""
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0"/>
<meta name="robots" content="index, follow"/>
<meta name="author" content="UKNS IT-Premium Services"/>
<meta name="geo.region" content="DE-SN"/>
<meta name="geo.placename" content="Leipzig"/>
<title>{esc(meta_title(topic))}</title>
<meta name="description" content="{esc(meta_description(topic))}"/>
<link rel="canonical" href="{canonical}"/>
<link rel="alternate" hreflang="de-DE" href="{canonical}"/>
<link rel="alternate" hreflang="x-default" href="{canonical}"/>
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png"/>
<link rel="icon" sizes="32x32" type="image/png" href="/favicon-32x32.png"/>
<link rel="icon" sizes="16x16" type="image/png" href="/favicon-16x16.png"/>
<link rel="manifest" href="/site.webmanifest"/>
<meta name="theme-color" content="#ffffff"/>
<meta property="og:type" content="website"/>
<meta property="og:locale" content="de_DE"/>
<meta property="og:site_name" content="UKNS IT-Premium Services"/>
<meta property="og:url" content="{canonical}"/>
<meta property="og:title" content="{esc(topic.title)}"/>
<meta property="og:description" content="{esc(meta_description(topic))}"/>
<meta property="og:image" content="{SITE_URL}{img}"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{esc(topic.title)}"/>
<meta name="twitter:description" content="{esc(meta_description(topic))}"/>
<meta name="twitter:image" content="{SITE_URL}{img}"/>
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_schema, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(breadcrumbs, ensure_ascii=False)}</script>
<link rel="preload" as="font" crossorigin href="/fonts/montserrat-v30-latin-700.woff2" type="font/woff2"/>
<link rel="preload" as="font" crossorigin href="/fonts/open-sans-v43-latin-regular.woff2" type="font/woff2"/>
<link rel="stylesheet" href="/css/style.optimized.css?v=20260531-icons"/>
<style>
  .seo-page {{ background:#f5f7fb; color:#101828; }}
  .seo-hero {{ background:linear-gradient(135deg,rgba(12,25,79,.98),rgba(43,57,144,.94)); color:#fff; padding:7.5rem 0 4.5rem; }}
  .seo-nav {{ position:fixed; inset:0 0 auto; z-index:40; background:rgba(255,255,255,.93); backdrop-filter:blur(16px); border-bottom:1px solid rgba(16,24,40,.09); }}
  .seo-nav-inner {{ max-width:1180px; margin:0 auto; padding:.85rem 1rem; display:flex; align-items:center; justify-content:space-between; gap:1rem; }}
  .seo-brand {{ display:flex; align-items:center; gap:.65rem; color:#2B3990; font-weight:800; }}
  .seo-links {{ display:flex; gap:1rem; flex-wrap:wrap; font-weight:700; color:#344054; }}
  .seo-container {{ max-width:1180px; margin:0 auto; padding:0 1rem; }}
  .hero-grid {{ display:grid; grid-template-columns:1.05fr .95fr; gap:3rem; align-items:center; }}
  .eyebrow {{ color:#FFCC00; font-weight:800; margin-bottom:1rem; }}
  .seo-hero h1 {{ font-size:clamp(2.25rem,5vw,4.2rem); line-height:1.04; font-weight:800; margin:0 0 1.25rem; letter-spacing:0; }}
  .lead {{ font-size:1.17rem; line-height:1.8; opacity:.94; margin-bottom:1.7rem; }}
  .hero-image {{ border-radius:.5rem; box-shadow:0 26px 70px rgba(0,0,0,.26); width:100%; }}
  .detail-image {{ width:100%; border-radius:.5rem; box-shadow:0 20px 48px rgba(16,24,40,.13); border:1px solid rgba(43,57,144,.12); }}
  .lifestyle-grid {{ display:grid; grid-template-columns:1.1fr .9fr; gap:2rem; align-items:center; }}
  .lifestyle-picture {{ display:block; }}
  .lifestyle-image {{ display:block; width:100%; border-radius:.5rem; box-shadow:0 22px 56px rgba(16,24,40,.14); border:1px solid rgba(43,57,144,.1); }}
  .lifestyle-copy {{ background:#fff; border:1px solid rgba(43,57,144,.12); border-radius:.5rem; padding:2rem; box-shadow:0 16px 38px rgba(16,24,40,.07); }}
  .lifestyle-eyebrow {{ display:block; color:#2B3990; font-weight:800; margin-bottom:.65rem; }}
  .lifestyle-copy h2 {{ color:#2B3990; font-size:2rem; line-height:1.18; font-weight:800; margin:0 0 1rem; }}
  .lifestyle-copy p {{ color:#475467; line-height:1.75; margin:0; }}
  .lifestyle-note {{ margin-top:1.2rem; padding:1rem 1.1rem; background:#f9fafb; border-left:4px solid #FFCC00; border-radius:.5rem; }}
  .lifestyle-note strong {{ display:block; color:#2B3990; margin-bottom:.35rem; }}
  .button-row {{ display:flex; flex-wrap:wrap; gap:.9rem; }}
  .primary-btn,.secondary-btn {{ display:inline-flex; align-items:center; justify-content:center; padding:.9rem 1.2rem; border-radius:.5rem; font-weight:800; min-height:48px; }}
  .primary-btn {{ background:#FFCC00; color:#2B3990; }}
  .secondary-btn {{ border:2px solid rgba(255,255,255,.86); color:#fff; }}
  .content-section {{ padding:4.5rem 0; }}
  .split {{ display:grid; grid-template-columns:1fr 1fr; gap:2rem; align-items:start; }}
  .visual-grid {{ display:grid; grid-template-columns:.95fr 1.05fr; gap:2rem; align-items:center; }}
  .visual-copy ul {{ padding-left:1.2rem; margin:1rem 0 0; }}
  .human-grid {{ display:grid; grid-template-columns:1.05fr .95fr; gap:2rem; align-items:start; }}
  .seo-card {{ background:#fff; border:1px solid rgba(43,57,144,.12); border-radius:.5rem; padding:2rem; box-shadow:0 18px 44px rgba(16,24,40,.08); }}
  .seo-card h2,.seo-card h3 {{ color:#2B3990; font-weight:800; line-height:1.18; }}
  .seo-card h2 {{ font-size:2rem; margin-bottom:1rem; }}
  .seo-card h3 {{ font-size:1.35rem; margin-bottom:.75rem; }}
  .seo-card p,.seo-card li {{ color:#475467; line-height:1.75; }}
  .seo-card ul {{ padding-left:1.2rem; margin:1rem 0 0; }}
  .process-grid,.related-grid {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:1.2rem; }}
  .step,.related-card,.faq-item {{ background:#fff; border:1px solid rgba(43,57,144,.12); border-radius:.5rem; padding:1.4rem; box-shadow:0 12px 30px rgba(16,24,40,.06); }}
  .step strong,.related-card strong {{ display:block; color:#2B3990; font-size:1.08rem; margin:.45rem 0; }}
  .step span,.related-card span {{ color:#2B3990; font-weight:800; font-size:.85rem; }}
  .related-card small {{ display:block; color:#667085; line-height:1.55; }}
  .cta-band {{ background:#2B3990; color:#fff; border-radius:.5rem; padding:2.2rem; display:flex; justify-content:space-between; align-items:center; gap:2rem; }}
  .cta-band p {{ opacity:.9; line-height:1.7; }}
  .faq-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:1rem; }}
  footer {{ background:#333; color:#d1d5db; padding:3rem 0; }}
  @media(max-width:820px) {{ .hero-grid,.split,.visual-grid,.human-grid,.lifestyle-grid,.process-grid,.related-grid,.faq-grid {{ grid-template-columns:1fr; }} .seo-links {{ display:none; }} .seo-hero {{ padding-top:6rem; }} .cta-band {{ display:block; }} }}
</style>
</head>
<body class="seo-page">
<header class="seo-nav">
  <nav class="seo-nav-inner">
    <a class="seo-brand" href="/"><span>UKNS</span><small>IT-Premium Services</small></a>
    <div class="seo-links"><a href="/it-service-leipzig/">IT-Service</a><a href="/computer-reparatur-leipzig/">Computerhilfe</a><a href="/it-wissen/">IT-Wissen</a><a href="/kontakt/">Kontakt</a></div>
  </nav>
</header>
<main>
<section class="seo-hero">
  <div class="seo-container hero-grid">
    <div>
      <p class="eyebrow">{esc(topic.audience)} · {esc(topic.category)}</p>
      <h1>{esc(topic.title)}</h1>
      <p class="lead">{esc(topic.problem)} UKNS hilft in Leipzig mit klarer Analyse, verständlicher Umsetzung und dem Ziel: {esc(topic.outcome)}.</p>
      <div class="button-row"><a class="primary-btn" href="/kontakt/?subject={esc(topic.title)}">{esc(topic.cta)}</a><a class="secondary-btn" href="{esc(topic.hub)}">Passende Leistungen ansehen</a></div>
    </div>
    <picture>
      <source type="image/webp" srcset="/images/generated/{topic.slug}-480.webp 480w, /images/generated/{topic.slug}-800.webp 800w, /images/generated/{topic.slug}-1200.webp 1200w" sizes="(min-width: 900px) 48vw, 100vw"/>
      <img class="hero-image" src="{img}" srcset="/images/generated/{topic.slug}-480.jpg 480w, /images/generated/{topic.slug}-800.jpg 800w, /images/generated/{topic.slug}-1200.jpg 1200w" sizes="(min-width: 900px) 48vw, 100vw" width="1200" height="675" alt="{esc(topic.title)} bei UKNS in Leipzig" fetchpriority="high" decoding="async"/>
    </picture>
  </div>
</section>
<section class="content-section">
  <div class="seo-container split">
    <article class="seo-card">
      <h2>Wann {esc(topic.keyword)} sinnvoll ist</h2>
      <p>{esc(topic.problem)} Sinnvoll wird Unterstützung immer dann, wenn das Thema im Alltag Zeit kostet, Unsicherheit erzeugt oder wichtige Daten und Abläufe berührt.</p>
      <ul>
        <li>Wenn technische Probleme wiederholt auftreten oder Zeit kosten.</li>
        <li>Wenn Einrichtung, Sicherheit oder Dokumentation nicht eindeutig sind.</li>
        <li>Wenn Sie eine Lösung möchten, die verständlich erklärt und sauber übergeben wird.</li>
      </ul>
    </article>
    <article class="seo-card">
      <h2>Was UKNS übernimmt</h2>
      <ul>{deliverables}</ul>
    </article>
  </div>
</section>
<section class="content-section" style="padding-top:0">
  <div class="seo-container human-grid">
    <article class="seo-card">
      <h2>{esc(story_title)}</h2>
      <p>{esc(story_intro)}</p>
      <p>{esc(story_detail)}</p>
    </article>
    <article class="seo-card">
      <h2>Woran wir gute Hilfe festmachen</h2>
      <ul>{quality_items}</ul>
      <h3 style="margin-top:1.35rem">Hilfreich vor dem ersten Gespräch</h3>
      <ul>{prep_items}</ul>
    </article>
  </div>
</section>
<section class="content-section" style="padding-top:0">
  <div class="seo-container visual-grid">
    <picture>
      <source type="image/webp" srcset="/images/generated/{detail_stem}-480.webp 480w, /images/generated/{detail_stem}-800.webp 800w, /images/generated/{detail_stem}-1200.webp 1200w" sizes="(min-width: 900px) 46vw, 100vw"/>
      <img class="detail-image" src="/images/generated/{detail_stem}-1200.jpg" srcset="/images/generated/{detail_stem}-480.jpg 480w, /images/generated/{detail_stem}-800.jpg 800w, /images/generated/{detail_stem}-1200.jpg 1200w" sizes="(min-width: 900px) 46vw, 100vw" width="1200" height="760" alt="Visuelle Übersicht zu {esc(topic.title)}" loading="lazy" decoding="async"/>
    </picture>
    <article class="seo-card visual-copy">
      <h2>{esc(visual_title)}</h2>
      <p>Die Grafik fasst die wichtigsten Schritte zusammen, damit der Nutzen nicht abstrakt bleibt. So erkennen Sie schneller, was zuerst geprüft wird und welches Ergebnis am Ende greifbar sein sollte.</p>
      <ul>{visual_items}</ul>
    </article>
  </div>
</section>
{lifestyle_section}
<section class="content-section" style="padding-top:0">
  <div class="seo-container">
    <div class="process-grid">
      <div class="step"><span>01</span><strong>Erstcheck</strong><p>Wir klären Ziel, Problem, Umgebung und Dringlichkeit, bevor unnötiger Aufwand entsteht.</p></div>
      <div class="step"><span>02</span><strong>Umsetzung</strong><p>Die Lösung wird nachvollziehbar umgesetzt, getestet und so dokumentiert, dass sie später wartbar bleibt.</p></div>
      <div class="step"><span>03</span><strong>Übergabe</strong><p>Sie erhalten eine klare Erklärung, Empfehlungen und auf Wunsch laufende Betreuung durch UKNS.</p></div>
    </div>
  </div>
</section>
<section class="content-section" style="padding-top:0">
  <div class="seo-container">
    <div class="cta-band">
      <div><h2>{esc(topic.title)} unverbindlich besprechen</h2><p>Schildern Sie kurz, was gerade passiert oder welches Ziel erreicht werden soll. Danach lässt sich meist gut einschätzen, ob Fernwartung, Vor-Ort-Service oder ein geplanter Termin der richtige nächste Schritt ist.</p></div>
      <a class="primary-btn" href="/kontakt/?subject={esc(topic.title)}">Anfrage senden</a>
    </div>
  </div>
</section>
<section class="content-section" style="padding-top:0">
  <div class="seo-container">
    <h2 style="color:#2B3990;font-size:2rem;font-weight:800;margin-bottom:1rem">Häufige Fragen</h2>
    <div class="faq-grid">{faq_items}</div>
  </div>
</section>
<section class="content-section" style="padding-top:0">
  <div class="seo-container">
    <h2 style="color:#2B3990;font-size:2rem;font-weight:800;margin-bottom:1rem">Weitere passende Themen</h2>
    <div class="related-grid">{cards}</div>
  </div>
</section>
</main>
<footer>
  <div class="seo-container"><strong>UKNS IT-Premium Services Leipzig</strong><p>IT-Service, Computerhilfe, Sicherheit, Cloud und Support aus Leipzig.</p><p><a href="/impressum/">Impressum</a> · <a href="/datenschutz/">Datenschutz</a> · <a href="/kontakt/">Kontakt</a></p></div>
</footer>
</body>
</html>
"""


def hub_html(segment: str, title: str, description: str, topics: list[PageTopic]) -> str:
    cards = "\n".join(
        f"""
        <a class="hub-card" href="/{esc(t.slug)}/">
          <img src="/images/generated/{esc(t.slug)}-480.jpg" width="480" height="270" loading="lazy" decoding="async" alt="{esc(t.title)}"/>
          <span>{esc(t.category)}</span>
          <strong>{esc(t.title)}</strong>
          <small>{esc(t.outcome)}</small>
        </a>
        """
        for t in topics
    )
    canonical = f"{SITE_URL}/it-wissen/{segment}.html"
    item_list_schema = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": title,
        "description": description,
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": index,
                "name": topic.title,
                "url": f"{SITE_URL}/{topic.slug}/",
            }
            for index, topic in enumerate(topics, start=1)
        ],
    }
    collection_schema = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": title,
        "description": description,
        "url": canonical,
        "publisher": {"@type": "Organization", "name": "UKNS IT-Premium Services", "url": SITE_URL},
    }
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0"/>
<meta name="robots" content="index, follow"/>
<title>{esc(title)} | UKNS</title>
<meta name="description" content="{esc(description)}"/>
<link rel="canonical" href="{canonical}"/>
<script type="application/ld+json">{json.dumps(collection_schema, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(item_list_schema, ensure_ascii=False)}</script>
<link rel="stylesheet" href="/css/style.optimized.css?v=20260531-icons"/>
<style>
  body {{ background:#f5f7fb; color:#101828; }}
  .hub-hero {{ background:#2B3990; color:#fff; padding:7rem 1rem 4rem; }}
  .hub-container {{ max-width:1180px; margin:0 auto; padding:0 1rem; }}
  .hub-hero h1 {{ font-size:clamp(2.4rem,5vw,4rem); font-weight:800; line-height:1.04; }}
  .hub-hero p {{ max-width:760px; line-height:1.8; opacity:.9; }}
  .hub-grid {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:1.2rem; padding:4rem 0; }}
  .hub-card {{ background:#fff; border-radius:.5rem; overflow:hidden; box-shadow:0 18px 44px rgba(16,24,40,.08); border:1px solid rgba(43,57,144,.12); display:block; }}
  .hub-card img {{ width:100%; height:170px; object-fit:cover; }}
  .hub-card span,.hub-card strong,.hub-card small {{ display:block; margin-left:1.2rem; margin-right:1.2rem; }}
  .hub-card span {{ color:#2B3990; font-weight:800; font-size:.85rem; margin-top:1rem; }}
  .hub-card strong {{ color:#101828; font-size:1.1rem; margin-top:.4rem; }}
  .hub-card small {{ color:#667085; line-height:1.55; margin-top:.45rem; margin-bottom:1.2rem; }}
  .topbar {{ position:fixed; inset:0 0 auto; background:rgba(255,255,255,.94); border-bottom:1px solid rgba(16,24,40,.08); z-index:30; }}
  .topbar div {{ max-width:1180px; margin:auto; padding:.9rem 1rem; display:flex; justify-content:space-between; font-weight:800; color:#2B3990; }}
  @media(max-width:900px) {{ .hub-grid {{ grid-template-columns:1fr; }} }}
</style>
</head>
<body>
<header class="topbar"><div><a href="/">UKNS</a><a href="/it-wissen/">IT-Wissen</a></div></header>
<main>
<section class="hub-hero"><div class="hub-container"><h1>{esc(title)}</h1><p>{esc(description)}</p></div></section>
<section class="hub-container"><div class="hub-grid">{cards}</div></section>
</main>
</body>
</html>
"""


def update_it_wissen() -> None:
    path = ROOT / "it-wissen" / "index.html"
    text = path.read_text(encoding="utf-8")
    block = """
<section class="py-16 md:py-20 bg-gray-100" id="seo-service-hubs">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
<div class="text-center mb-12">
<h2 class="text-3xl font-bold text-primary-blue mb-4">Neue IT-Service-Themen</h2>
<p class="text-lg text-gray-600 max-w-3xl mx-auto">Zusätzliche Ratgeber- und Leistungsseiten für Firmenkunden und Privatkunden, sauber nach Themenclustern sortiert.</p>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-8">
<div class="bg-white rounded-lg shadow-lg overflow-hidden">
<a class="block" href="/it-wissen/firmenkunden-it-dienstleistungen.html">
<img alt="Firmenkunden IT-Dienstleistungen in Leipzig" class="w-full h-48 object-cover" src="/images/generated/microsoft-365-backup-leipzig-1200.jpg" loading="lazy" decoding="async" width="1200" height="675"/>
<div class="p-6">
<p class="text-sm text-primary-blue font-semibold mb-2">Firmenkunden</p>
<h3 class="text-xl font-bold text-gray-900 mb-3">50 neue IT-Dienstleistungen für Unternehmen</h3>
<p class="text-gray-600 text-sm mb-4">Microsoft 365, Security, Monitoring, Backup, Netzwerk, Compliance und Managed Services als eigene Themencluster.</p>
<span class="font-semibold text-primary-blue hover:underline">Alle Firmenkunden-Themen ansehen →</span>
</div>
</a>
</div>
<div class="bg-white rounded-lg shadow-lg overflow-hidden">
<a class="block" href="/it-wissen/privatkunden-computerhilfe-themen.html">
<img alt="Privatkunden Computerhilfe in Leipzig" class="w-full h-48 object-cover" src="/images/generated/pc-hilfe-leipzig-1200.jpg" loading="lazy" decoding="async" width="1200" height="675"/>
<div class="p-6">
<p class="text-sm text-primary-blue font-semibold mb-2">Privatkunden</p>
<h3 class="text-xl font-bold text-gray-900 mb-3">50 neue Computerhilfe-Themen für Privatkunden</h3>
<p class="text-gray-600 text-sm mb-4">PC-Hilfe, Outlook, Drucker, WLAN, Windows, Viren, Datenrettung, Mac, Smartphone und digitale Alltagshilfe.</p>
<span class="font-semibold text-primary-blue hover:underline">Alle Privatkunden-Themen ansehen →</span>
</div>
</a>
</div>
</div>
</div>
</section>
"""
    pattern = re.compile(r"\n<!-- SEO service hubs generated -->.*?<!-- /SEO service hubs generated -->\n", re.S)
    text = pattern.sub("\n", text)
    marker = "</main>"
    wrapped = f"\n<!-- SEO service hubs generated -->\n{block}\n<!-- /SEO service hubs generated -->\n"
    text = text.replace(marker, wrapped + marker, 1)
    path.write_text(text, encoding="utf-8", newline="\n")


def update_sitemap(urls: list[str]) -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    for url in urls:
        if f"<loc>{url}</loc>" in text:
            continue
        entry = f"""    <url>
        <loc>{url}</loc>
        <lastmod>{LOCAL_DATE}</lastmod>
        <priority>0.65</priority>
    </url>
"""
        text = text.replace("\n</urlset>", "\n" + entry + "\n</urlset>")
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    for topic in TOPICS:
        generate_image(topic)
        generate_detail_image(topic)
        page_dir = ROOT / topic.slug
        page_dir.mkdir(exist_ok=True)
        (page_dir / "index.html").write_text(page_html(topic), encoding="utf-8", newline="\n")

    b2b = [t for t in TOPICS if t.segment == "b2b"]
    b2c = [t for t in TOPICS if t.segment == "b2c"]
    (ROOT / "it-wissen" / "firmenkunden-it-dienstleistungen.html").write_text(
        hub_html("firmenkunden-it-dienstleistungen", "IT-Dienstleistungen für Firmenkunden in Leipzig", "50 konkrete UKNS-Leistungsseiten für Unternehmen: Microsoft 365, Security, Monitoring, Backup, Netzwerk, Compliance und Managed Services.", b2b),
        encoding="utf-8",
        newline="\n",
    )
    (ROOT / "it-wissen" / "privatkunden-computerhilfe-themen.html").write_text(
        hub_html("privatkunden-computerhilfe-themen", "Computerhilfe für Privatkunden in Leipzig", "50 konkrete Hilfethemen für Privatkunden: PC-Hilfe, Windows, Outlook, Drucker, WLAN, Sicherheit, Mac, Smartphone und Datensicherung.", b2c),
        encoding="utf-8",
        newline="\n",
    )
    update_it_wissen()
    new_urls = [f"{SITE_URL}/{t.slug}/" for t in TOPICS]
    new_urls.extend([
        f"{SITE_URL}/it-wissen/firmenkunden-it-dienstleistungen.html",
        f"{SITE_URL}/it-wissen/privatkunden-computerhilfe-themen.html",
    ])
    update_sitemap(new_urls)
    manifest = {
        "generated_at": LOCAL_DATE,
        "pages": len(TOPICS),
        "b2b_pages": len(b2b),
        "b2c_pages": len(b2c),
        "urls": [f"/{t.slug}/" for t in TOPICS],
        "hub_pages": [
            "/it-wissen/firmenkunden-it-dienstleistungen.html",
            "/it-wissen/privatkunden-computerhilfe-themen.html",
        ],
    }
    (ROOT / "seo-generated-pages-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps({"generated_pages": len(TOPICS), "images": len(TOPICS) * 12, "hubs": 2}, ensure_ascii=False))


if __name__ == "__main__":
    main()
