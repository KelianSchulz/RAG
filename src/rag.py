

# TODO: Prompt aus Frage + Kontext (Top-Treffer) bauen
# TODO: GPT-Call absetzen
# TODO: Antwort formatieren/zurückgeben

from openai import OpenAI
from search import search_jobs
import sqlite3

client = OpenAI()

def build_prompt(jobs, query_text):

    context = ""

    for i, job in enumerate (jobs, start=1):
        context += f"{i}. Titel: {job['title']}\nBeschreibung: {job['description']}\nLink: {job['link']}\n\n"


    prompt = f"""Hier sind relevante Stellenanzeigen:

    {context}
    Frage des Nutzers: "{query_text}"

    Beantworte die Frage nur basierend auf den oben genannten Anzeigen."""
    
    return prompt


def get_answer(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content


def answer_query(conn, query_text):

    jobs = search_jobs(conn, query_text)
    prompt = build_prompt(jobs, query_text)
    answer = get_answer(prompt)
    return answer


if __name__ == "__main__":
    
    conn = sqlite3.connect("data/jobs.db")
    answer = answer_query(conn, "Jobs mit Python und Machine Learning, hybrides Arbeiten")
    print(answer)
    conn.close()
