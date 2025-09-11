#Declaração de variaveis
x = float(input("Informe o valor de X: ").replace(",", "."))
y = float(input("Informe o valor de Y: ").replace(",", "."))

#Menu
print(f"\n{'-'*20} ESCOLHA A OPERAÇÃO {'-'*20}\n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

#Usuario escolhe a operação desejada
operador = input("Informe a Operação Desejada: ").strip() # O parametro strip elimina os espaço no campo do programa

# mach case
match operador:
    case "1":
        print(f"A Soma dos valores é {x+y}.")
    case "2":
        print(f"A Subtração dos valores é {x-y}.")
    case "3":
        print(f"A Multiplicação dos valores é {x*y}.")
    case "4":
        print(f"A Divisão dos valores é {x/y}.")
    case _: #Default
        print("Operação Inválida.")