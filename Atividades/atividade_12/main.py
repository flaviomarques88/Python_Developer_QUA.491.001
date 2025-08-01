"""
# TODO - Atividade: crie um programa que calcule a área e a 
circunferência de um circulo.
# Note - use Lambda.
"""

import math
import os
#lambda
area_circunferencia = lambda r: math.pi*r**2
comprimento_circunferencia = lambda r: 2*math.pi*r
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")


#algortimo
if __name__ == "__main__":
    try:
        r = float(input("Informe o valor do Raio: ").replace(",", "."))
        a = area_circulo(r)
        comp = comprimento_circunferencia(r)
     
        limpar()
        print(f"Area da circunferência {a:.2f}.")
        print(f"O valor do Comprimento da circunferência: {comp:.2f}.")
    except Exception as e:
        print(f"Não foi possível exibir os resultados. {e}.")