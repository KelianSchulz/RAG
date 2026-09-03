"""Tests für Phase 1 — Scraping."""

# TODO: Parsing-Logik gegen gespeichertes Test-HTML testen

import requests as r
from bs4 import BeautifulSoup as bs
import time as t
from scraper import parse_job_list, get_description, parse_description



def test_parse_job_list():
    with open("tests/fixture/test_page.html", "r", encoding="utf-8") as f:
        html = f.read()

        results = parse_job_list(html)

        test_job = {"title" : "Werkstudent KI-Anwendungen, Prompt Engineering & Wissensmanagement (w/m/d)", "link_tag" : "https://www.absolventa.de/stellenangebote/13063873-p-werkstudent-ki-anwendungen-prompt-engineering-wissensmanagement-w-m-d"}
        
        assert test_job in results


def test_desc_page():

    with open("tests/fixture/test_page_desc.html", "r", encoding="utf-8") as f:
            html = f.read()

            results = parse_description(html)

            description = "Die Stelle ist ab sofort in Teilzeit (15-20 Stunden/Woche) und befristet für 12 Monate zu besetzen.Künstliche Intelligenz eröffnet neue Möglichkeiten, Wissen zugänglich zu machen, Prozesse zu vereinfachen und Mitarbeitende bei ihrer täglichen Arbeit wirksam zu unterstützen. Für unser Team Arbeitsrecht suchen wir einen Werkstudenten, der Interesse daran hat, die Potenziale von KI-Anwendungen wie Microsoft Copilot und dmGPT gemeinsam mit uns nutzbar zu machen.Du unterstützt uns dabei, aus den vielfältigen Möglichkeiten der KI konkrete Mehrwerte für unseren Bereich Arbeitsrecht zu entwickeln: Von intelligenten Assistenten über standardisierte Prompt-Bibliotheken bis hin zu neuen Arbeitsweisen im Wissensmanagement und der Prozessoptimierung. Dabei erhältst Du die Möglichkeit, moderne KI-Werkzeuge praxisnah einzusetzen, neue Anwendungsfälle zu entwickeln und die digitale Weiterentwicklung eines wichtigen Unternehmensbereichs aktiv mitzugestalten.Kurze Fakten:Geschäftsbereich,Einsatzort:Mitarbeiter (HR), hybridJob Art:Teilzeit (15-20 Std./Wo.)Vertragsart:WerkstudentDatum frühestmöglicher Start:ab sofort"

            assert description in results