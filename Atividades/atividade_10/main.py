"""
# TODO - Atividade: faça um GRUD (Create, Read, Update, Delete) em um JSON.
Opções do Menu:
- Criar novo usuário arquivo JSON(usuário irá informar o diretório).
- Lista todos os usuários de um arquivo JSON.
- Cadastrar novo usuário em um JSON.
- Listar todos os usuários de um arquivo JSON.
- Pesquisar usuário através do valor de uma chave em um arquivo JSON.
- Alterar dados de um usuário em um arquivo JSON.
- Deletar usuário de um arquivo JSON.
- Sair do programa
Dados do Usuário:
- Nome
- Data de Nascimento
- CPF
- E-Mail
- Telefone
- Filme Favorito do Usuário
"""

# ---CODIGO FONTE---
#IMPORTAÇÃO
import json
import os

usuario = []
novo_arquivo = ""

while True:
    usuario = {}
print("\n===🐍MENU DO SISTEMA===")
print("1 - Criar um Novo Usuário ")
print("2 - Cadastrar um Novo Usuário ")
print("3 - Listar Todos Usuários  ")
print("4 - Pesquisar um Usuário ")
print("5 - Cadastrar Usuários ")
print("6 - Alterar os Dados de um Usuário ")
print("7 - Excluir um Usuário ")
print("8 - Excluir  Usuário ")
opcao = input("Informe uma Opção Deseja no Sistama:")
os.system ("cls" if os.name == "nt" else "clear")
match opcao:
    case"1":
        usuario = input("Digite um Nome do Arquivo: ").strip().lower
        with open(f"atividade_10/arquivo_json/"{novo_arquivo}.json", "w", encoding="uft-8") as f:
                  jason.load(f)
        
    case"2":
        ...
    case"3":
        ...
    case"4":
        ...
    case"5":
        ...
    case"6":
        ...
    case"7":
        ...
    case"8":
        print("Programa Encerrado com Sucesso.")
    case _:
        print("Opção Invalida Tente Novamente.")
        continue