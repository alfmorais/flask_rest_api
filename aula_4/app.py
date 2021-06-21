"""
AGENDA: 
1) Criando uma lista de registros
2) Implementando métodos GET, POST, PUT, DELETE
3) Manipulando dados com as API e métodos implementados

TAREFAS QUE REALIZAREMOS
- Veremos como implementar uma API para inclusão de novos desenvolvedores e seus conhecimentos
- Iremos manipular uma lista que irá conter o nome desenvolvedor e suas habilidades (linguagens que domina)
- Tudo isso será feito através de APIs.

"""

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

desenvolvedores = [
    {"nome": "Alfredo de Morais Neto",
     "habilidades": ["Python", "Flask"]},
    {"nome": "Joaquim Morais",
     "habilidades": ["HTML", "Django", "Python"]}
]


# definindo as rotas
# testando a primeira rota do app, consultar, alterar e deletar
@app.route('/dev/<int:id>/', methods=["GET", "PUT", "DELETE"])
def desenvolvedor(id):
    if request.method == "GET":
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = "Desenvolvedor de ID {} não existe".format(id)
            response = {"status": "erro", "mensagem": mensagem}
        except Exception:
            mensagem = "Erro desconhecido. Procure o DEV!!!"
            response = {"status": "erro", "mensagem": mensagem}
        return jsonify(response)
    elif request.method == "PUT":
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify({"status": "REGISTRO DELETADO!!!"})


# configurando uma nova rota
# para inserir o desenvolvedor e lista todos
@app.route('/dev/', methods=["POST", "GET"])
def lista_desenvolvedores():
    if request.method == "POST":
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({"status": "sucesso",
                        "mensagem": "registro inserido!"})
    elif request.method == "GET":
        return jsonify(desenvolvedores)


# configurando o app para debug True
if __name__ == "__main__":
    app.run(debug=True)
