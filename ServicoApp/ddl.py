import sqlite3

conn = sqlite3.connect('escola.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE tb_aluno(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(30) NOT NULL,
        email TEXT NOT NULL
    );
""")

conn.close()
print("Tabelas criadas com sucesso!")
