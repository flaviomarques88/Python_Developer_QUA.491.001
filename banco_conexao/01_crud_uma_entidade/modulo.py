from datetime import datetime
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def cadastrar_pessoa(session, Pessoa):
    try:
        nome = input("Digite o Nome do Usuário: ").strip().title()
        email = input("Digite o E-Mail do Usuário: ").strip().lower()
        data_nascimento = input("Digite a Data de Nascimento (DD/MM/AAAA): ").strip()
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()

        nova_pessoa = Pessoa(nome=nome, email=email, data_nascimento=data_nascimento)

        session.add(nova_pessoa)
        session.commit()

        print(f"Pessoa {nome} Cadastrada com Sucesso.")
    except Exception as e:
        print(f"Não Foi Possível Cadastrar Pessoa. {e}.")

def listar_pessoas(session, Pessoa):
    try:
        pessoas = session.query(Pessoa).all()

        print("\nPessoas Cadastradas:\n")
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"E-Mail: {pessoa.email}")
            print(f"Data de Nascimento: {pessoa.data_nascimento.strftime("%d/%m/%Y")}")
            print(f"{'-'*40}")
    except Exception as e:
        print(f"Não Foi Possível Listar Pessoas. {e}.")

def pesquisar_pessoas(session, Pessoa):
    print("Filtrar Pessoas por Campo:")
    print("1 - ID")
    print("2 - Nome")
    print("3 - E-Mail")
    print("4 - Data de Nascimento")
    print("5 - Retornar")
    campo = input("Escolha o Campo a ser Pesquisado: ").strip()
    limpar()
    match campo:
        case "1":
            valor = input("Digite o ID para Buscar: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.id_pessoa.like(f"{valor}")).all()
        case "2":
            valor = input("Digite o Nome para Buscar: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.nome.like(f"%{valor}%")).all()
        case "3":
            valor = input("Digite o E-Mail para Buscar: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.email.like(f"%{valor}%")).all()
        case "4":
            valor = input("Digite a Data de Nascimento (DD/MM/AAAA) Para Buscar: ").strip()
            data_nascimento = datetime.strptime(valor, "%d/%m/%Y").date()
            pessoas = session.query(Pessoa).filter(Pessoa.data_nascimento == data_nascimento).all()
        case "5":
            pass
        case _:
            print("Campo Inexistente.")

    limpar()
    print("\nResultado da Pesquisa:\n")
    if pessoas:
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"E-Mail: {pessoa.email}")
            print(f"Data de Nascimento: {pessoa.data_nascimento.strftime("%d/%m/%Y")}")
            print(f"{'-'*40}")
    else:
        print("Nenhuma Pessoa Foi Encontrada.")