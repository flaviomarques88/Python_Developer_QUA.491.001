# Importar Biblioteca sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os

    # prepared statement
    # SQL Injection
    #NOTE: ENGINE PARA O MYSQL -- CODIGO PARA CONECTAR O BANCO MYSQL COM PYTHON.
    # engine = create_engine("mysql+mysqlconnector//senha:root@localhost:3306/nome_banco")


Limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def criar_tb_pessoa(engine, Base):
    try:
        class Pessoa(Base):
            __tablename__ = "pessoa"

            id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
            nome = Column(String, nullable=False)
            email = Column(String, nullable=False, unique=True)
            data_nascimento = Column(Date, nullable=False)

        Base.metadata.create_all(engine)  # Comando Para Criar a Tabela no Banco

        return Pessoa
    except Exception as e:
        print(f"Erro ao Conectar ao Banco. {e}")

def cadastrar_pessoa(session, Pessoa):
    nome = input("Digite o Nome do Usuário: ").strip().title()
    email = input("Digite o E-Mail do Usuário: ").strip().lower()
    data_nascimento = input("Digite a Data de Nascimento (dd/mm/aaaa): ").strip()
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()

    nova_pessoa = Pessoa(nome=nome, email=email, data_nascimento=data_nascimento)

    session.add(nova_pessoa)
    session.commit()

    print(f"Pessoa {nome} Cadastrado com Sucesso.")

def listar_pessoas(session):
    pessoas = session.query(pessoa).all()

    print("\nPessoas Cadastradas:\n")
    for pessoa in pessoas:
        print(f"ID:{pessoa.id_pessoa}")
        print(f"Nome:{pessoa.nome}")
        print(f"E-Mail:{pessoa.email}")
        print(f"Data de Nascimento:{pessoa.data_nascimento.strftime("%d/%m/%Y")}")
        print(f"{'-'*40}")


def main():
    engine = create_engine("sqlite:///01_crud_uma_entidade/database/db_crud.db")
    Base = declarative_base()  # Objeto que representa Classe nativa do banco SQLite

    Pessoa = criar_tb_pessoa(engine, Base)

    Session = sessionmaker(bind=engine)
    session = Session()

    Limpar()
    while True:
        print(f"{'-'*20} CRUD DA SERPENTE {'-'*20}")
        print("1 - Cadastrar nova Pessoa")
        print("2 - Listar Pessoas")
        print("3 - Alterar Dados de uma Pessoa")
        print("4 - Excluir uma Pessoa")
        print("5 - Sair do Programa")
        opcao = input("Informe a Opção Desejada: ").strip()
        Limpar()
        cadastrar_pessoa(session, Pessoa)
        match opcao:
            case"1":
                cadastrar_pessoa(session, Pessoa)
                continue
            case"2":
                listar_pessoas(session, Pessoa)
                continue
            case"3":
                ...
            case"4":
                ...
            case"5":
                print("Programa Encerrado.")
                break
            case _:
                print("Opção Inválido.")

    session.close()

if __name__ == "__main__":
    main()