
from openai import OpenAI
import sqlite3
import json

from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def prepare_text(job):
    return f"{job['title']}\n\n{job['description']}"


def embed_and_store(conn):
    cursor = conn.execute("SELECT id, title, description FROM jobs WHERE embedding IS NULL")
    jobs = cursor.fetchall() 

    for job in jobs:

        id, title, description = job

        text = prepare_text({"title": title, "description": description})
        embedding = get_embedding(text)
        embedding_bytes = json.dumps(embedding).encode("utf-8")
        conn.execute("UPDATE jobs SET embedding = ? WHERE id = ?", (embedding_bytes, id))
        conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect("data/jobs.db")
    embed_and_store(conn)
    conn.close()
