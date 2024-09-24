import sqlite3
import os

conn = sqlite3.connect('/home/pedro/projeto/prova_simples.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matricula TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS resultados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matricula TEXT NOT NULL,
    pergunta TEXT NOT NULL,
    acerto INTEGER NOT NULL
)
''')

conn.commit()
conn.close()

os.chmod("/home/pedro/projeto/prova_simples.db", 0o774)
os.chown("/home/pedro/projeto/prova_simples.db", 108, 114)

print("criado")
