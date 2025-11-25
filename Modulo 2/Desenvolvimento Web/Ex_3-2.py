from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    lista = ['Jorge', 'Pedro', 'Lucas', 'Eduardo', 'Enzo']
    sala_cheia = False
    return render_template('ex_3-2.html', lista=lista, sala_cheia=sala_cheia)


if __name__ == '__main__':
    app.run(debug=True)