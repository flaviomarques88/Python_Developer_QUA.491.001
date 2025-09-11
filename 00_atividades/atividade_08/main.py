# TODO - Atividade: Crie um programa que receba de um professor várias notas de uma aluno de 0 a 10
#(Não importa quantas notas). Ao final do programa, a media das notas devera ser calcular e informada, e em 
# seguida o programa ira informar se o aluno:
# foi aprovado, caso media for maior ou igual a 7 
# ficou de recuperação, caso media for entre 5 e 7 
# foi reprovado , caso media for menor que 5
#declaração de variaveis
import os
notas = []
# loop para receber as notas
#MENU
while True:
   print("1 - Informe uma nota do aluno de 0 a 10")
   print("2 - Informe uma nota do aluno de 0 a 10")
   opcao    = input("Escolha uma opção Desejado(1 ou 2): ").strip()
   os.system('cls' if os.name == 'nt' else 'clear')
   match opcao:
    case '1':
       try:
          nova_nota = float(input("Insira a nova nota: ")).replace(',', '.')
          if nova_nota >= 0 and nova_nota <= 10:
             os.system('cls' if os.name == 'nt' else 'clear')
            notas.append(nova_nota)
            print("Nota inserida com sucesso.")
            else:
            print("Nota Invalida.")
       except Exception as e:
          print(f"Não foi possivel inseir a nota. {e}.")
       finally:
          continue
    case '2':
       try:
          media = sum(notas) / len(notas)
          print(f"media: {media:.2f}")
          if media >= 7:
            print("Aluno Aprovado!")
          elif  media >= 5:
            print("Aluno em Recuperação!")
          else:
              print("Aluno Reprovado!")
       except Exception as e:
            print(f"Não foi possivel calcular a média.")
       finally:
           break
    case _:
       print("Opção Invalidal.")
       continue