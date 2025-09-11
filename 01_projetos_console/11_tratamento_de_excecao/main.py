#Declaração de variais
try:
    n = int(input("Informe um número inteiro: "))
    print(f"Número Informado: {n}.")
except Exception as e:
    print(f"Não foi possivel exibir o numero. {e}.")
finally:
    print("programa encerrado com sucesso!")