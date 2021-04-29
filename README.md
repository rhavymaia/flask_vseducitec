
# Flask e SQlite
# Flask
Disponibiliza na Internet, via HTTP, o acesso a funções das aplicações. Não utiliza bibliotecas de terceiros: microframework. Disponível em: https://flask.palletsprojects.com/.
	
## Instalação
Instalar no Linux ou Windows a versão do **Python 3.8** e preparar o ambiente virtualizado utilizando **Virtual Environment**.

### Virtual Environment (venv)
- Instalar o python-virtualenv:
```sh
$ sudo apt-get install python-virtualenv
```
- Criar o venv:
```sh
python3 -m venv servicoapp_venv
```
- Ativar venv:
```sh
source minha_env/bin/activate
```
- Adicionar o Flask no ambiente isolado do venv:
```sh
pip3 install flask
```
- Desativar venv
```sh
deactivate
```
## Hello, world.
```py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

if(__name__ == '__main__'):
	app.run(host='0.0.0.0', debug=True, use_reloader=True)
```

## Execução
### Declarar variáveis de ambiente
- Ubuntu
```sh
[diretorio_da_app]$ export FLASK_APP=app.py
```
- Uindous
```sh
c:[diretorio_da_app]/> set FLASK_APP=hello.py
```
### Modo depuração
	[diretorio_da_app]$ export FLASK_ENV=development
	
### Executando
	flask run

## Recebendo Valores 
### Path parameter
```py
@app.route('/alunos/<int:id>')
def getAluno(id):
	return {'id': id, 'nome': 'João', 'email': 'joao@academico.ifpb.edu.br'}
```
## Métodos HTTP
- POST
```py
@app.route('/aluno', methods=['POST'])
def setAluno():
	return  'requisição via post'
```
# SQlite
Banco de dados leve para execução embarcada em aplicações.
```py
import sqlite3
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()
cursor.execute(""" CREATE TABLE tb_aluno(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR(30) NOT NULL,
	email TEXT NOT NULL
);
""")
conn.close()
print("Tabelas criadas com sucesso!")
```
