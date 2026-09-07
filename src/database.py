import sqlite3

conn = sqlite3.connect("data/jobs.db")

conn.execute("""

CREATE TABLE IF NOT EXISTS jobs(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT not null,
link TEXT UNIQUE,
description TEXT not null,
embedding BLOB
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


