"""
# TODO - Atividade: crie um programa que receba do usuário um número
inteiro e o programa calcula o valor da sequência de Fibonacci.
"""

import modulo as mo

if __name__ == "__main__":
    while True:
            try:
                print("1 - Calcular o Fibonacci: ")
                print("2 - Sair do Programa:")
                opcao = input("Escolha a Opção. ").strip()
                match opcao:
                    case"1":
                        n = int(input("Informe um Número Inteiro: "))
                        print(f"{n}! = {mo.fibonacci(n)}")
                    case"2":
                        print("Sair do Programa")
                        break
                    case _:
                        print("Opção Invalido!")
                        continue
            except Exception as e:
                print(f"Erro. {e}.")
                continue