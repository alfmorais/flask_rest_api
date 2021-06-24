from utils import Pessoas, db_session, Atividades


def insere_pessoas():
    pessoa = Pessoas(nome="Alfredo", idade=29)
    print(pessoa)
    db_session.add(pessoa)
    db_session.commit()


def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome="Alfredo")
    print(pessoa)
    # acessando a idade da pessoa
    pessoa = Pessoas.query.filter_by(nome="Alfredo").first()
    print(pessoa.idade)


def altera_pessoas():
    pessoa = Pessoas.query


if __name__ == "__main__":
    insere_pessoas()
    consulta_pessoas()
