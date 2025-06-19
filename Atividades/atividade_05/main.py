# Import necessary libraries
import os 
import datetime
from datetime import date

date = date.today().strftime("%d/%m/%Y")
hora = datetime.datetime.now().strftime("%H:%M:%S")

#Filmes das Salas
Sala_1 = "A Roda Quadrada"
Sala_2 = "A Volta dos Que Não Foram"
Sala_3 = "Poeira em alto Mar"
Sala_4 = "As Tranças do Rei Careca"
Sala_5 = "A Vingança do Peixe Frito"

#Tratamento de Exeção
while True:
    try:
    nome = input("Informe seu nome: ").strip().title()
    idade = int(input("Informe sua idade: "))
    while True:
        print(f"{"-"*20} CINE COBRA {"-"*20}")
        print(f"Sala 1 - {Sala_1} - Livre")
        print(f"Sala 2 - {Sala_2} - 12 Anos")
        print(f"Sala 3 - {Sala_3} - 14 Anos")
        print(f"Sala 4 - {Sala_4} - 16 Anos")
        print(f"Sala 5 - {Sala_5} - 18 Anos")
        sala = input("Informe a sala desejada:").strip()
        os .system("cls" if os.name == "nt" else "clear")
        match sala:
            case "1":
               idade_minima = 0
               filmes = Sala_1
            case "2":
                idade_minima = 12
                filmes = Sala_2
            case "3":
                idade_minima = 14
                filmes = Sala_3
            case "4":
                idade_minima = 16
                filmes = Sala_4
            case "5":
                idade_minima = 18
                filmes = Sala_5
            case _:
                print("Sala Inexistente, Favor, Escolha outra sala.")
                continue
        if idade > idade_minima:
                print(f"{"-"*20} CINE COBRA {"-"*20}")
                print(f"{"-"*60}\n")
                print(f" filmes: {filmes} - {idade_minima}")
                print(f" Ingresso comprado com sucesso!")
        else:
            print(f"{nome} não possui a idade minima para ver {filmes}")
            continue
        print(f"{"-"*60}\n")
        print(f"Obrigado por escolher o CINE COBRA, {nome}!")
        print(f"Data: {date} - Hora: {hora}")
        print(f"{"-"*60}\n")
        break               
        except Exception as e:                                              
            # Handle any exceptions that occur  
        print("Ocorreu um erro ao processar sua solicitação. Por favor, tente novamente.")
        
        print(f"Não foi possível comprar ingresso. Erro: {e}.")