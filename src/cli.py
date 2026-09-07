import sqlite3
from rag import answer_query



query = input()

conn = sqlite3.connect("data/jobs.db")
answer = answer_query(conn, query)
print(answer)
conn.close()


