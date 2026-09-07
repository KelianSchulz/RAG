"""Phase 6 — Optionale CLI.

Einfaches Kommandozeilen-Interface: Frage eingeben, Antwort ausgeben.
"""

# TODO: Frage per input() entgegennehmen
# TODO: search.py + rag.py aufrufen
# TODO: Antwort ausgeben


import sqlite3
from rag import answer_query



query = input()

conn = sqlite3.connect("data/jobs.db")
answer = answer_query(conn, query)
print(answer)
conn.close()


