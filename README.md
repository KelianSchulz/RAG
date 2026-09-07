# Job-RAG

Job-RAG ist ein kleines Tool, das Stellenanzeigen automatisiert sammelt, sie inhaltlich versteht und einem erlaubt, in ganz normaler Sprache danach zu fragen. Man tippt also nicht "Python UND hybrid", sondern schreibt zum Beispiel "zeig mir Jobs mit Python und hybridem Arbeiten" und bekommt eine Antwort, die wirklich auf die gefundenen Anzeigen eingeht, inklusive Links.

Der Grund, warum ich das gebaut habe, war nicht nur "ein RAG-System haben", sondern verstehen, wie so etwas unter der Haube wirklich funktioniert, statt einfach eine fertige Library wie LangChain draufzuwerfen. Deshalb ist hier jeder Schritt der Pipeline von Hand geschrieben: das Scraping, die Datenbank samt Deduplizierung, die Embeddings, die Vektorsuche und am Ende die eigentliche Antwortgenerierung über GPT.

## Wie das Ganze funktioniert

Am Anfang steht der Scraper (`src/scraper.py`), der Stellenanzeigen von Absolventa lädt (einfach zu scrapen), mit BeautifulSoup den HTML-Code durchsucht und daraus Titel, Link und Beschreibung pro Anzeige extrahiert. Diese Rohdaten landen in einer lokalen SQLite-Datenbank (`src/database.py`), wobei jede Anzeige über ihren Link eindeutig identifiziert wird, damit beim erneuten Scrapen keine Duplikate entstehen.

Damit man später sinnvoll danach suchen kann, wird jede gespeicherte Anzeige in ein Embedding umgewandelt, also einen Vektor, der die inhaltliche Bedeutung des Textes einfängt (`src/embeddings.py`, über die OpenAI Embeddings API). Wenn man dann eine Frage stellt, wird auch diese Frage in einen Vektor umgewandelt, und über Cosine Similarity wird berechnet, welche gespeicherten Anzeigen der Frage inhaltlich am nächsten kommen (`src/search.py`). Am Ende nimmt `src/rag.py` die paar besten Treffer, baut daraus zusammen mit der ursprünglichen Frage einen Prompt und lässt GPT eine echte, verständliche Antwort formulieren, statt nur eine trockene Trefferliste auszugeben.

`src/cli.py` bindet das alles zu einem kleinen Kommandozeilen-Interface zusammen: man startet es, tippt seine Frage ein und bekommt die Antwort direkt im Terminal.

## Projekt starten

Zuerst braucht man eine virtuelle Umgebung und die Abhängigkeiten aus der `requirements.txt`:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Da die Embeddings und die Antwortgenerierung über die OpenAI API laufen, braucht man außerdem einen eigenen API-Key. Der wird in einer `.env`-Datei im Projektordner erwartet, als `OPENAI_API_KEY=dein-key-hier`.

Danach lässt sich die Pipeline Schritt für Schritt durchlaufen. Erst wird gescrapt und in der Datenbank gespeichert:

```
python3 src/scraper.py
```

Anschließend werden für alle neuen Anzeigen die Embeddings berechnet:

```
python3 src/embeddings.py
```

Und schließlich kann man über die Kommandozeile Fragen stellen:

```
python3 src/cli.py
```

## Tests

Jede Phase der Pipeline ist einzeln getestet, von der Parsing-Logik des Scrapers bis zur Cosine-Similarity-Berechnung und dem gemockten GPT-Aufruf. Die Tests lassen sich mit

```
pytest -v
```

ausführen.
