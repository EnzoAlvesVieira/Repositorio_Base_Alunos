from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Ola mundo'

@app.route('/sobre')
def sobre():
    return 'Muito Prazer! Me chamo Enzo, sou um Progamador'

@app.route('/ola/<nome>')
def ola(nome):
    if nome == 'Enzo':
        return f'Olá Craque! Prazer rever-lo denovo'
    else:
        return f'Olá {nome}!'


if __name__ == '__main__':
    app.run(debug=True)