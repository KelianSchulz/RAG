"""Phase 3 — Chunking & Embeddings.

Wandelt Job-Texte über die OpenAI Embeddings API in Vektoren um.
"""

# TODO: Text pro Anzeige vorbereiten (ggf. chunken)
# TODO: OpenAI Embeddings API anbinden
# TODO: Embeddings zu den Jobs in der DB speichern

from openai import OpenAI
import sqlite3
import json

client = OpenAI()

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def prepare_text(job):
    return f"{job["title"]}\n\n{job["description"]}"


def embed_and_store(conn):
    cursor = conn.execute("SELECT id, title, description FROM jobs WHERE embedding IS NULL")
    jobs = cursor.fetchall()