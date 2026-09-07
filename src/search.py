
# TODO: Suchanfrage zu Embedding-Vektor umwandeln
# TODO: Cosine Similarity zu allen Job-Vektoren berechnen
# TODO: Top-N Treffer zurückgeben


import numpy as np
from embeddings import get_embedding
import json
import sqlite3


def calc_cosine_similarity(vec_1, vec_2):
    vec_1 = np.array(vec_1)
    vec_2 = np.array(vec_2)
    
    dot_product = np.dot(vec_1, vec_2)
    norm_1 = np.linalg.norm(vec_1)
    norm_2 = np.linalg.norm(vec_2)
    
    similarity = dot_product / (norm_1 * norm_2)
    return similarity



def load_embeddings(conn):
    cursor = conn.execute("SELECT id, title, description, link, embedding FROM jobs WHERE embedding IS NOT NULL")
    jobs = cursor.fetchall()
    results = []

    for job in jobs:

        id, title, description, link, embedding = job
        embedding_vector = json.loads(embedding.decode("utf-8"))
        results.append({"id": id, "title": title, "description": description, "link": link, "embedding": embedding_vector})


    return results

def get_similarity(job):
    return job["similarity"]

def search_jobs(conn, query_text, top_n=5):
    query_vector = get_embedding(query_text)
    
    jobs = load_embeddings(conn)
    
    for job in jobs:
        similarity = calc_cosine_similarity(job["embedding"], query_vector)
        job["similarity"] = similarity   
    
    sorted_jobs = sorted(jobs, key=get_similarity, reverse=True)
    
    return sorted_jobs[:top_n]   



if __name__ == "__main__":
    conn = sqlite3.connect("data/jobs.db")
    results = search_jobs(conn, "Jobs mit Python und Machine Learning")
    for job in results:
        print(job["title"], "-", job["similarity"])
    conn.close()


