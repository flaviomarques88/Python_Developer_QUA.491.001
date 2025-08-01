import os
#Função Normal

# def somar(x, y):
#     result = x + y
#     return result

# Função Lambda
somar = lambda x, y: x+y
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

# algoritmo principal
if __name__ == "__main__":
    try:
        x = int(input("Informe o Valor de X: "))
        y = int(input("Informe o Valor de Y: "))
        result = somar (x, y)

        limpar()
        print(f"O Resultado da Soma é {result}.")
    except Exception as e:
        print(f"Não foi possível soma. {e}.")