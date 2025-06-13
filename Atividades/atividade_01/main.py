"""
# TODO - Atividade
# Crie um programa que receba do usuário o valor do etanol e da gasolina em reais, e informe para o usuário
qual o melhor combustível para abastecer.
# Note - o usuário poderá informar várias vezes os valores, e irá encerrar o 
programa quando desejar.
# NOTE - compensa etanol caso ele tenha 70% do valor da gasolina.
# NOTE - DIVIRTAM-SE!!! =D
"""

# declaração de variaveis
while True:
    gasolina = float(input("Informe o valor da gasolina: "))
    etanol = float(input("Informe o valor do etanol: "))
    
    if etanol / gasolina <= 0.7:
        print("Compensa abastecer com etanol.")
    else:
        print("Compensa abastecer com gasolina.")
    
    continuar = input("Deseja informar novos valores? (s/n): ").strip().lower()
    if continuar != 's':
        break
