from flask_restful import Api, Resource

lista_habilidades = ["Python", "Java", "PHP", "Django"]


class Habilidades(Resource):
    def get(self):
        return lista_habilidades
