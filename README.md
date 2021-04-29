
# Flask e SQlite
# Flask
Disponibilizar na Internet, via HTTP, o acesso as funções das aplicações. Não utiliza bibliotecas de terceiros: microframework. É extensível como, por exemplo, as bibliotecas [Flask-Restful](https://flask-restful.readthedocs.io/en/latest/) e [Flask-SQLaAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/). Disponível em: https://flask.palletsprojects.com/.

![enter image description here](https://dz2cdn1.dzone.com/storage/temp/10940394-rest-api-using-spring-boot.png)
Criado por: https://dzone.com/articles/5-courses-to-learn-restful-web-services-with-java.
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
		# parâmetros são opcionais.
		app.run(host='0.0.0.0', debug=True, use_reloader=True) 		
```
## Execução
### Declarar variáveis de ambiente
- Ubuntu
```sh
$ export FLASK_APP=App.py
```
- Uindous :)
```sh
set FLASK_APP=hello.py
```
### Modo depuração
```sh
$ export FLASK_ENV=development
```
### Executando
```sh
flask run
```
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
Banco de dados leve para execução embarcada em aplicações. Disponível em:  https://docs.python.org/3/library/sqlite3.html
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

## Referências 
### Flask:
- [User’s Guide - Installation](https://flask.palletsprojects.com/en/1.1.x/installation/).
- [User’s Guide - Quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/).
### SQLite: 

 - [Gerenciando banco de dados SQLite3 com Python - Parte 1 - Regis da Silva](http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html).
