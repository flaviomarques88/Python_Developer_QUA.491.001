# Importar Biblioteca sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import entidades as ent
import modulo as md

    # Prepared Statement
    # SQL Injection
    #NOTE: ENGINE PARA O MYSQL -- CODIGO PARA CONECTAR O BANCO MYSQL COM PYTHON.
    # engine = create_engine("mysql+mysqlconnector//senha:root@localhost:3306/nome_banco")

def main():
    engine = create_engine("sqlite:///01_crud_uma_entidade/database/db_crud.db")
    Base = declarative_base()
    Pessoa = ent.criar_tb_pessoa(engine, Base)
    Session = sessionmaker(bind=engine)
    session = Session()

    md.limpar()
    while True:
        print(f"{'-'*20} CRUD DA SERPENTE🐍 {'-'*20}")
        print("1 - Cadastrar Nova Pessoa")
        print("2 - Listar Pessoas")
        print("3 - Pesquisar Pessoas")
        print("4 - Alterar Dados de uma Pessoa")
        print("5 - Excluir uma Pessoa")
        print("6 - Sair do Programa")
        opcao = input("Informe a Opção Desejada: ").strip()
        md.limpar()
        match opcao:
            case "1":
                md.cadastrar_pessoa(session, Pessoa)
                continue
            case "2":
                md.listar_pessoas(session, Pessoa)
                continue
            case "3":
                md.pesquisar_pessoas(session, Pessoa)
                continue
            case "4":
                pass
            case "5":
                pass
            case "6":
                print("Programa Encerrado.")
                break
            case _:
                print("Opção Inválida.")
                continue

    session.close()

if __name__ == "__main__":
    main()