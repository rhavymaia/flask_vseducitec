from flask import Flask
from flask import jsonify
import sqlite3

app = Flask(__name__)


@app.route('/')
def hello_world():
    return {'mensagem': 'Olá, mundo!'}


@app.route('/alunos/<int:id>')
def getAluno(id):
    print(id)
    return {'id': id, 'nome': 'João', 'email': 'joao@academico.ifpb.edu.br'}


@app.route('/aluno', methods=['POST'])
def setAluno():
    return 'requisição via post'


@app.route("/alunos")
def getAlunos():

    try:
        # abrir conexão com o banco de dados.
        conn = sqlite3.connect('escola.db')
        cursor = conn.cursor()
        # executar a consulta.​
        cursor.execute("""
            SELECT * FROM tb_aluno;
        """)
        # iterando os registros.
        alunos = []
        for linha in cursor.fetchall():
            aluno = {
                "id": linha[0],
                "nome": linha[1],
                "email": linha[2]
            }
            alunos.append(aluno)
        # fechar conexão.
        conn.close()

    except(sqlite3.Error):
        print("Aconteceu um erro.")

    return jsonify(alunos)


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=4000, debug=True, use_reloader=True)
