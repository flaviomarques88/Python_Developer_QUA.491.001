"""
# TODO - Atividade: Crie um programa de aplicativo de banco, onde:
- O usuário cria uma conta no banco com os seguintes dados:
-- Titula da conta
-- CPF do titular
-- Agência
-- Número da conta
-- Saldo
- O usuário pode fazer no programa:
- Consultar dados
- Depositar valor
- Sacar valor
- Imprimir extrato (entende-se: gerar arquivo com os dados da conta)
- Sair do programa
# NOTE - O nome da classe é Conta
"""


# CODIGO
import classe as c
import os
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    cc = c.Conta(titular="", cpf="", agencia="", conta="", saldo=0.0)

    cc.titular = input("Informe Nome do Titular da Conta: ").strip().title()
    cc.cpf = input("Informe CPF do Titular: ").strip()
    cc.agencia = "0408-1"
    cc.conta = "2025-1"

    limpar()
    while True:
        print(f"{'-'*20} 🐍 BANCO PYTHON BRASIL 🐍 {'-'*20}")
        print("1 - Consultar Dados.")
        print("2 - Depositar Valor.")
        print("3 - Sacar Valor.")
        print("4 - Imprimir Extrato.")
        print("5 - Sair do Programa.")
        opcao = input("Informe a Operação Desejada: ").strip()
        limpar()

        match opcao:
            case "1":
                cc.Consultar_dados()
                continue
            case "2":
                try:
                    valor = float(input("Informe O Valor do Depósito: R$ ").replace(",", "."))
                    limpar()
                    if valor > 0:
                        print(f"Depósito Efetuado com Sucesso! Saldo: R$ {cc.depositar(valor):.2f}")
                    else:
                        print("Valor do Depósito Inválido.")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "3":
                try:
                    valor = float(input("Informe O Valor do Saque: R$ ").replace(",", "."))
                    limpar()
                    if valor > 0:
                        if valor <= cc.saldo:
                            print(f"Saque Efetuado com Sucesso! Saldo: R$ {cc.sacar(valor):.2f}.")
                        else:
                            print("Saldo Insuficiente.")
                    else:
                        print("Valor do Saque Inválido!")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "4":
                try:
                    cc.imprimir_extrato()
                    print("Extrato Impresso com Sucesso!")
                except Exception as e:
                    print(f"Não Foi Possível Imprimir Extrato. {e}.")
                finally:
                    continue
            case "5":
                print("Programa Encerrado Com Sucesso!")
                break
            case _:
                print("Opção Inválida!")
                continue