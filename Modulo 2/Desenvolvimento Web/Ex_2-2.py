from flask import Flask, render_template

app = Flask(__name__) #Cria o app flask

@app.route('/') #Decorador de função( Onde a gente define a rota)
def index(): #A função da rota
    return render_template('ex_2-2.html')

@app.route('/sobre')
def sobre():
    return 'Aluno Enzo De Pyhton!'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'Olá {nome}'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    return f'O dobro de {numero} é {numero*2}'  

#Pra rodar o flask da maneira certa
if __name__ == '__main__':
    app.run(debug=True)