"""
# TODO - Atividade:  Crie um programa que faça as seguintes operações:
- Calcule área de um circulo
- Calcule Tamanho de uma circuferência
- Sair do Programa
# NOTE - Para cada loop, o programa deverá limpar o terminal.
"""



# #importa biblioteca
# import os
# #entrada de dados
# area = float(input(" Calcula a área de um círculo:" ))
# circunferencia = float(input("Calcula o tamanho de uma circunferência:" ))


import os
import math
while True:
    os.system("cls" if os.name == "nt" else "clear")
    
print("===MENU===")
print("1- Calcula a área de um círculo")
print("2- Calcula o tamanho de uma circunferência")
print("3- Limpar")

while True:
    limpar_terminal()

    print("Escolha uma opção:")
    print("1 - Calcular área do círculo")
    print("2 - Calcular tamanho da circunferência")
    print("3 - Sair do programa")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        try:
            raio = float(input("Digite o raio do círculo: "))
            area = calcular_area_circulo(raio)
            print(f"A área do círculo é: {area:.2f}")
        except ValueError:
            print("Entrada inválida. Digite um número.")
    elif opcao == '2':
        try:
            raio = float(input("Digite o raio da circunferência: "))
            circunferencia = calcular_circunferencia(raio)
            print(f"O tamanho da circunferência é: {circunferencia:.2f}")
        except ValueError:
            print("Entrada inválida. Digite um número.")
    elif opcao == '3':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Escolha uma opção entre 1 e 3.")
    input("Pressione Enter para continuar...")