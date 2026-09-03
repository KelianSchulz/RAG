"""Tests für Phase 2 — Speicherung."""

# TODO: Insert + Dedupe-Verhalten testen


import sqlite3
from database import insert_job


def test_insert_job_dedupe():
    conn = sqlite3.connect(":memory:")

    conn.execute("""

    CREATE TABLE IF NOT EXISTS jobs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT not null,
    link TEXT UNIQUE,
    description TEXT not null
    );
    """
    )
    job = {"title": "Werkstudent Data", "link_tag": "https://www.absolventa.de/jobs/beispiel-job", "description" : "Das ist eine beispiel Beschreibung"}

    insert_job(conn, job)
    insert_job(conn, job)

    cursor = conn.execute("Select Count(*) FROM jobs")
    row_count = cursor.fetchone()[0]

    assert row_count == 1