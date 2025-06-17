# importa biblioteca
import os

while True:
    nome = input(f"Informe seu Nome: ")
    os.system("cls")
    print(f"Seja beja vindo, {nome}!")
   

    prosseguir = input("Deseja inserir outro nome? (s/n)").lower().strip()

    match prosseguir:
        case "s":
            os.system("cls")
            continue
        case "n":
            break
        case _:
            print("Opção inválida.")
            break