# Job-RAG

Ein Tool, das Stellenanzeigen scrapt, versteht (semantisch, nicht nur nach Keywords)
und dir erlaubt, in natürlicher Sprache danach zu fragen — z.B. *"zeig mir Jobs mit
Python und hybrid Arbeiten"*.

**Prinzip: Phase für Phase.** Jede Phase ist einzeln testbar, einzeln lauffähig und
einen eigenen Commit wert, bevor die nächste beginnt. Nicht vorgreifen.

---

## Phase 0 — Setup

- [X] `python3 -m venv venv && source venv/bin/activate`
- [X] `pip install -r requirements.txt`
- [X] `.env.example` zu `.env` kopieren, `OPENAI_API_KEY` eintragen
- [ ] `git init && git add . && git commit -m "Projekt-Skeleton"`

---

## Phase 1 — Scraping (Daten sammeln)

Stellenanzeigen automatisiert per Code holen statt von Hand zu kopieren.

- [ ] Quelle wählen (z.B. Indeed) und eine Beispielseite manuell im Browser inspizieren
- [ ] HTTP-Request + HTML-Parsing für eine einzelne Suchergebnis-Seite bauen
- [ ] Titel, Beschreibung, Link pro Anzeige extrahieren
- [ ] Pagination handhaben (mehrere Seiten durchlaufen)
- [ ] Ergebnis: Liste von Dicts/Objekten mit den gescrapten Anzeigen
- [ ] `tests/test_scraper.py`: Parsing-Logik gegen gespeichertes Test-HTML testen

**Datei:** `src/scraper.py`

---

## Phase 2 — Speicherung (SQLite)

Gescrapte Daten strukturiert und dedupliziert lokal ablegen.

- [ ] SQLite-Datenbank + Tabelle für Jobs anlegen (Schema: Titel, Beschreibung, Link, Datum, ...)
- [ ] Insert-Funktion schreiben
- [ ] Deduplizierung: gleiche Anzeige bei erneutem Scrapen nicht doppelt speichern
- [ ] `jobs.db` landet in `data/` (gitignored)
- [ ] `tests/test_database.py`: Insert + Dedupe-Verhalten testen

**Datei:** `src/database.py`

---

## Phase 3 — Chunking & Embeddings

Jede Anzeige in einen Vektor umwandeln, der die Bedeutung des Texts codiert.

- [ ] Text pro Anzeige vorbereiten (ggf. chunken, wenn Beschreibung lang ist)
- [ ] OpenAI Embeddings API anbinden
- [ ] Embeddings zu den Jobs in der DB speichern
- [ ] `tests/test_embeddings.py`: API-Call mocken, Rückgabeform testen

**Datei:** `src/embeddings.py`

---

## Phase 4 — Vector Search

Aus einer natürlichsprachigen Frage die ähnlichsten gespeicherten Anzeigen finden.

- [ ] Suchanfrage ebenfalls in einen Embedding-Vektor umwandeln
- [ ] Cosine Similarity zwischen Anfrage-Vektor und allen Job-Vektoren berechnen
- [ ] Top-N ähnlichste Treffer zurückgeben
- [ ] `tests/test_search.py`: Similarity-Berechnung mit festen Beispiel-Vektoren testen

**Datei:** `src/search.py`

---

## Phase 5 — LLM-Antwort (RAG-Teil)

Aus den Top-Treffern + der Frage eine echte, verständliche Antwort formulieren lassen.

- [ ] Prompt bauen: Frage + relevante Treffer als Kontext
- [ ] GPT-Call mit diesem Prompt absetzen
- [ ] Antwort sauber zurückgeben/formatieren
- [ ] `tests/test_rag.py`: Prompt-Aufbau testen (API-Call mocken)

**Datei:** `src/rag.py`

---

## Phase 6 — Interface (optional)

Damit man's nicht nur direkt im Code bedienen muss.

- [ ] Einfache CLI (`src/cli.py`): Frage eingeben → Antwort ausgeben
- [ ] Optional: kleines Streamlit-Interface (`app.py`)

---

## Fortschritt

| Phase | Status |
|---|---|
| 0 — Setup | ☐ |
| 1 — Scraping | ☐ |
| 2 — Speicherung | ☐ |
| 3 — Embeddings | ☐ |
| 4 — Vector Search | ☐ |
| 5 — RAG-Antwort | ☐ |
| 6 — Interface | ☐ |
