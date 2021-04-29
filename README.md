
# Flask e SQlite
# Flask
- Disponibilizar na Internet, via HTTP, o acesso a funções das aplicações.
- Não utiliza bibliotecas de terceiros: microframework.
- Site oficial: https://flask.palletsprojects.com/.
	
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

## Recebendo valores
```py
@app.route('/user/<username>')
def show_user_profile(username):
  # show the user profile for that user
  return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
  # show the post with the given id, the id is an integer
  return 'Post %d' % post_id
```
Métodos HTTP
	from flask import request

	@app.route('/login', methods=['GET', 'POST'])
	def login():
	    if request.method == 'POST':
		return do_the_login()
	    else:
		return show_the_login_form()

