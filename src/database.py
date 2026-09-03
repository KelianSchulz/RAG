"""Phase 2 — Speicherung in SQLite.

Legt gescrapte Jobs strukturiert und dedupliziert in einer lokalen
SQLite-Datenbank ab (data/jobs.db).
"""

# TODO: Tabelle für Jobs anlegen (Titel, Beschreibung, Link, Datum, ...)
# TODO: Insert-Funktion
# TODO: Deduplizierung (z.B. über den Link als Unique Key)




import sqlite3

conn = sqlite3.connect("data/jobs.db")

conn.execute("""

CREATE TABLE IF NOT EXISTS jobs(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT not null,
link TEXT UNIQUE,
description TEXT not null
);
"""
)

conn.commit()

def insert_job(conn, job):
    conn.execute(
        "INSERT OR IGNORE INTO jobs (title, link, description) VALUES (?, ?, ?)",
        (job["title"], job["link_tag"], job["description"])
    )
    conn.commit()


