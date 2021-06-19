from flask import Flask, jsonify, request
import json

# configurando a classe do Flask
app = Flask(__name__)


# definindo a rota da api
# primeira rota da api
@app.route("/<int:id>", methods=["GET", "POST"])
def pessoas(id):
    # função jsonify() -> Retorna dados em formato JSON
    return jsonify({"id": id,
                    "nome": "Alfredo de Morais Neto",
                    "profissao": "Desenvolvedor Python"})


# definindo a rota da api soma
@app.route("/soma/<int:valor1>/<int:valor2>/")
def soma(valor1, valor2):
    soma = valor1 + valor2
    return jsonify({"soma": valor1 + valor2})


# definindo a rota da api somatoria
# informando valores por postman e recebendo na api do python
@app.route("/somatoria", methods=["POST", "GET"])
def somatoria():
    if request.method == "POST":
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == "GET":
        frase = 'Você não está fazendo soma alguma!!!'
        return jsonify({"frase": frase})
    return jsonify({"soma": total})


# verificando se a classe é do __name__
if __name__ == "__main__":
    app.run(debug=True)
