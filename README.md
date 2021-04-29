# Flask e SQlite
---
## Definição do Flask
	- Disponibilizar na Internet, via HTTP, o acesso# Flask e SQlite
---
## Flask
---
- Disponibilizar na Internet, via HTTP, o acesso a funções das aplicações.
- Não utilizar bibliotecas de terceiros: microframework.
- Site oficial: https://flask.palletsprojects.com/.
	
## Instalação
---
### Python3.8
Instalar no Linux ou Windows.

### Virtual Environment (venv)
- Ubuntu
```sh
$ sudo apt-get install python-virtualenv
```
- Criando
```sh
python3 -m venv servicoapp_venv
```
- Ativando venv
```sh
source minha_env/bin/activate
```

- Adicionar o Flask nas bibliotecas do Python3.8
```sh
pip3 install flask
```

- Desativando venv
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

### Execução
	Ubuntu
		[diretorio_da_app]$ export FLASK_APP=app.py
		[diretorio_da_app]$ export FLASK_ENV=development
	Uindous
		C:[diretorio_da_app]> set FLASK_APP=hello.py
	
	Modo depuração
		[diretorio_da_app]$ export FLASK_ENV=development
		
	Executando
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

 a funções das aplicações.
	- Não utilizar bibliotecas de terceiros: microframework.
	
## Site oficial
	https://flask.palletsprojects.com/
	
## Instalação
	Python3.8
	Virtual Environment (venv)
		Ubuntu
			$ sudo apt-get install python-virtualenv
		Criando 
			python3 -m venv servicoapp_venv
		Ativando venv
			source minha_env/bin/activate
		
		Adicionar o Flask nas bibliotecas do Python3.8
			pip3 install flask
		
		Desativando venv
			deactivate
		
Hello, world
	Aplicação minima
		from flask import Flask
		app = Flask(__name__)

		@app.route('/')
		def hello_world():
			return 'Hello, World!'
		
		if(__name__ == '__main__'):
    			app.run(host='0.0.0.0', debug=True, use_reloader=True)
	
	Ubuntu
		[diretorio_da_app]$ export FLASK_APP=app.py
		[diretorio_da_app]$ export FLASK_ENV=development
	Uindous
		C:[diretorio_da_app]> set FLASK_APP=hello.py
	
	Modo depuração
		[diretorio_da_app]$ export FLASK_ENV=development
		
	Executando
		flask run

Recebendo valores
	Aplicação com passagem de valores
		@app.route('/user/<username>')
		def show_user_profile(username):
		    # show the user profile for that user
		    return 'User %s' % escape(username)

		@app.route('/post/<int:post_id>')
		def show_post(post_id):
		    # show the post with the given id, the id is an integer
		    return 'Post %d' % post_id
		    
Métodos HTTP
	from flask import request

	@app.route('/login', methods=['GET', 'POST'])
	def login():
	    if request.method == 'POST':
		return do_the_login()
	    else:
		return show_the_login_form()


