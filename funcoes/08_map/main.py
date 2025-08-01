# lambda

pa = lambda x: x+2
pg = lambda x: x*2

#algoritmo principal
if __name__ == "__main__":
    #lista
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # exibe a pa e pg
    print(f"Progressão Aritimética: {list(map(pa, numeros))}")
    print(f"Progressão Geométrica: {list(map(pg, numeros))}")