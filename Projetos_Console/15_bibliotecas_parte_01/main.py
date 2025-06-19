# importa bibiotecas
import os
import time

try:
    n = int(input("Informe um Número Inteiro: "))
    while n >=0:
        os.system("cls")
        print(f"{n}...")
        time.sleep(1)
        n -= 1

except Exception as e:
    print(f"Não foi possivel executar a contagem. {e}.")
finally:
    os.system("cls")
    print("BOOOMMMMM!!!!")