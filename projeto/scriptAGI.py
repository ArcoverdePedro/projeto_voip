#!/usr/bin/env python3

import sqlite3
from asterisk.agi import AGI

agi = AGI()
agi.answer()

acertos = 0

# abre BD
conn = sqlite3.connect('/home/pedro/projeto/prova_simples.db')
cursor = conn.cursor()

agi.stream_file('/home/pedro/projeto/audios/inicio')
matricula = agi.get_data('/home/pedro/projeto/audios/matricula', 20000, 14)

cursor.execute("SELECT * FROM alunos WHERE matricula = ?", (matricula,))
resultado = cursor.fetchone()

if resultado:
    agi.stream_file('/home/pedro/projeto/audios/provafeita')
    agi.hangup()
else:
    # Inserir matrícula no BD
    cursor.execute("INSERT INTO alunos (matricula) VALUES (?)", (matricula,))
    conn.commit()

# Função para fazer perguntas
def fazer_pergunta(pergunta, resposta_correta):
    global acertos
    resposta = agi.get_data(f'/home/pedro/projeto/audios/{pergunta}', 60000, 1)
    if resposta == resposta_correta:
        agi.stream_file('/home/pedro/projeto/audios/acerto')
        acertos += 1
        # Inserir acerto no BD
        cursor.execute("INSERT INTO resultados (matricula, pergunta, acerto) VALUES (?, ?, ?)", (matricula, pergunta, 1))
    else:
        agi.stream_file('/home/pedro/projeto/audios/erro')
        # Inserir erro no BD
        cursor.execute("INSERT INTO resultados (matricula, pergunta, acerto) VALUES (?, ?, ?)", (matricula, pergunta, 0))
    conn.commit()

# Fazer todas as perguntas
fazer_pergunta('pergunta1', '2')
fazer_pergunta('pergunta2', '3')
fazer_pergunta('pergunta3', '4')
fazer_pergunta('pergunta4', '4')
fazer_pergunta('pergunta5', '3')
agi.stream_file(f'/home/pedro/projeto/audios/ponto{acertos}')

# Fecha o BD
conn.close()
agi.hangup()
