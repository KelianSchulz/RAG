"""Phase 1 — Stellenanzeigen scrapen.

Holt Stellenanzeigen von einer Quelle (z.B. Indeed) und liefert eine Liste
mit Titel, Beschreibung und Link pro Anzeige.
"""

# TODO: Requests + HTML-Parsing für eine Suchergebnis-Seite
# TODO: Titel, Beschreibung, Link extrahieren
# TODO: Pagination handhaben



import requests as r
from bs4 import BeautifulSoup as bs
import time as t
import sqlite3
from database import insert_job

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"}

"""with open("test_page.html", "w", encoding="utf-8") as f:
    f.write(response.text)"""





#for t in titles:
#    print(t.get_text(strip=True))


#flex flex-col lg:p-8 lg:rounded-xl lg:border-solid lg:border lg:border-outline space-y-sm class für beschreibung


#Loop durch die Job Cards, und Link, Beschreibung finden.

def parse_job_list(html):
    soup = bs(html, "html.parser") 
    titles = soup.find_all("h2")
    seen_links = set()
    results = []
    for h2 in titles:
        title = h2.get_text(strip=True)
        link_tag = h2.find_parent("a")
        if link_tag is None:
            continue
        href = link_tag.get("href")
        href = ("https://www.absolventa.de" + href)
        if href in seen_links:
            continue
        else:
           
            seen_links.add(href)
        results.append({"title":title, "link_tag": href})    
    print(len(results))
    print(len(seen_links))    
    return results



def get_description(results):
    for job in results:
        t.sleep(1)
        response = r.get(job["link_tag"], headers=headers)
        soup = bs(response.text, "html.parser")
        description_div = soup.find("div", class_="prose")
        description = description_div.get_text(strip = True)
        job["description"] = description
        """print(job)
        print("\n\n\n")"""



def parse_description(html):
    soup = bs(html, "html.parser")
    description_div = soup.find("div", class_ = "prose")
    description = description_div.get_text(strip = True)
    return description

if __name__ == "__main__":
    response = r.get("https://www.absolventa.de/jobs?text=Werkstudent+Data&location=&radius=100", headers=headers)
    results = parse_job_list(response.text)
    get_description(results)

    conn = sqlite3.connect("data/jobs.db")
    for job in results:
        insert_job(conn, job)
    conn.close()    
        

