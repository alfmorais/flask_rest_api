# REST VS RESTful

- REST é um estilo de arquitetônico, um modelo para ser seguido ao desenvolver API
- RESTful é um serviço web que utiliza desse paradigma. É utilizado para definir aplicações que implementar webservices que utilizam a arquitetura REST.
- Podemos dizer que uma aplicação Web que segue a arquitetura REST, ela é RESTful, ou seja, tem a capacidade de seguir a arquitetura REST

## Flask RESTfull

- É uma extensão do Flask que adiciona suporte para construção rapida de REST API
- O uso Flask-RESTful acaba incentivando as práticas recomendadas para a arquitetura REST com uma configuração leve.

~~~python
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}

api.add_resource(HelloWorld, "/")

if __name__ == "__main__":
    app.run(debug=True)
~~~