from flask import Flask

# definindo o app principal do Flask
app = Flask(__name__)


# definindo a primeira rota do app flask
# colocando os methods GET e POST
@app.route('/<numero>', methods=['GET', 'POST'])
def ola(numero):
    return "Olá Mundo! {}".format(numero)


# roda o app flask
if __name__ == "__main__":
    app.run(debug=True)
