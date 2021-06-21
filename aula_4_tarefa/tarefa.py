# Importando as bibliotecas necessárias para o projeto
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

lista_de_tarefas = [
    # Primeira tarefa
    {"id": 0,
     "responsavel": "Alfredo",
     "tarefa": "Estudar programação python",
     "status": "em andamento"},
    # Segunda tarefa
    {"id": 1,
     "responsavel": "Alfredo",
     "tarefa": "terminar o projeto blog",
     "status": "não iniciado"},
    {"id": 2,
     "responsavel": "Alfredo",
     "tarefa": "concluir o curso de flask da DIO",
     "status": "concluido"}
]


# Definindo 1° rotas do projeto tarefas
# Primeira rota: Consultar, alterar e deletar qualquer tarefa.
@app.route('/tarefa/<int:id>', methods=["GET", "PUT", "DELETE"])
def tarefa(id):
    # =========================================================================
    # código referente ao método GET
    if request.method == "GET":
        try:
            resposta = lista_de_tarefas[id]
        except IndexError:
            mensagem = "Desculpe, a tarefa {} não foi encontrada.".format(id)
            resposta = {"status": "erro", "mensagem": mensagem}
        except Exception:
            mensagem = "erro desconhecido!"
            resposta = {"status": "erro", "mensagem": mensagem}
        return jsonify(resposta)
    # =========================================================================
    # código referente ao método PUT
    elif request.method == "PUT":
        dados = json.loads(request.data)
        lista_de_tarefas[id] = dados
        return jsonify(dados)
    # =========================================================================
    # código referente ao método DELETE
    elif request.method == "DELETE":
        lista_de_tarefas.pop(id)
        mensagem = "item deletado com sucesso"
        return jsonify({"status": mensagem})


# Definindo 2° rotas do projeto tarefas
# Segunda rota: Inserir e listar tarefas
@app.route("/tarefa/", methods=["POST", "GET"])
def listar_tarefas():
    # =========================================================================
    # código referente ao método adicionar tarefas
    if request.method == "POST":
        dados = json.loads(request.data)
        lista_de_tarefas.append(dados)
        mensagem = "Registro inserido com sucesso"
        return jsonify({"status": mensagem})
    # =========================================================================
    # código referente ao método listar tarefas
    elif request.method == "GET":
        return jsonify(lista_de_tarefas)


# configurando o app para debug True
if __name__ == "__main__":
    app.run(debug=True)
