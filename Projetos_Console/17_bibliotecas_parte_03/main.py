#importa biblioteca
import math as m

print(f"Número do pi; {m.pi}. ")

#raiz quadrada 
try:
    n = int(input("Informe um número inteiro: "))
    print(f"A raiz quadrada de (n) é {m.sqrt(n)}.")
except Exception as e:
    print(f"Não foi possivel calcular a raiz quadrada. {e}.")
