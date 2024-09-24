import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('prova_simples.db')
cursor = conn.cursor()

# Consulta para a tabela alunos
cursor.execute("SELECT * FROM alunos")
alunos = cursor.fetchall()
print("Tabela alunos:")
for aluno in alunos:
    print(aluno)

# Consulta para a tabela resultados
cursor.execute("SELECT * FROM resultados")
resultados = cursor.fetchall()
print("\nTabela resultados:")
for resultado in resultados:
    print(resultado)

# Fechando a conexão
conn.close()
