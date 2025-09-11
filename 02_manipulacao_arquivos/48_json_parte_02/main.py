#IMPORTAÇÃO
import json
import os

pessoa = {}

try:
    arquivo = input("Informe o arquivo: ").strip().lower()
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        pessoas = json.load(f)
        
        # usuario informa os dados da nova pessoa
    pessoa ['nome'] = input("Informe o Nome: ").strip().title()
    pessoa ['idade'] = input("Informe a Idade: ")
    pessoa ['cpf'] = input("Informe o CPF: ").strip()
    pessoa ['rg'] = input("Informe o RG: ").strip()
    pessoa ['rg'] = input("Informe o RG: ").strip()
    pessoa ['data_nasc'] = input("Informe a Data de Nascimento: ").strip()
    pessoa ['sexo'] = input("Informe o Sexo: ").strip()
    pessoa ['signo'] = input("Informe o Signo: ").strip().capitalize
    pessoa ['mae'] = input("Informe o nome da Mãe: ").strip().title()
    pessoa ['pai'] = input("Informe o nome do Pai: ").strip().title()
    pessoa ['email'] = input("Informe o E-mail: ").strip().lower()
    pessoa ['senha'] = input("Informe a Senha: ")
    pessoa ['cep'] = input("Informe o CEP: ").strip()
    pessoa ['endereco'] = input("Informe o Endereço: ").strip().title()
    pessoa ['numero'] = int(input("Informe o Endereço: "))
    pessoa ['bairro'] = input("Informe o Bairro: ").strip().capitalize
    pessoa ['cidade'] = input("Informe a Cidade: ").strip().title()
    pessoa ['estado'] = input("Informe o Estado: ").strip().upper()
    pessoa ['telefone_fixo'] = int(input("Informe o Endereço: ")).strip()
    pessoa ['celular'] = input("Informe o Celular: ").strip()
    pessoa ['altura'] = float(input("Informe o Endereço: ").replace(",", "."))
    pessoa ['peso'] = float(input("Informe o peso: ").replace(",", "."))
    pessoa ['tipo_sanguineo'] = input("Informe o tipo sanguineo: ").strip().capitalize
    pessoa ['cor'] = input("Informe a cor: ").strip()

    pessoa.append(pessoa)
    with open(f"{arquivo}.json", "w", encoding="utf-8") as f:
        json.dump(pessoa, f, ensure_ascii=False, indent=4)
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        pessoa = json.load(f)

    print(f"{'-'*20} LISTA DE PESSOAS {'-'*20} ")
    for pessoa in pessoa:
        for chave in pessoa:
            print(f"{chave.capitalize()}: {pessoa.get(chave)}")
            print({'-'*40})
        print(f"Não foi possivel inserir pessoa. {e}.")
