    #importação
    import os

    #lista 
    nomes = ("fulano", "ciclano", "beltrano", "fulana", "ciclana", "beltrana")

    #exerbir a lista
    for i in range(len(nomes)):
        print(f"{i} - {nomes[i]}")
    print("-" * 60)
    try:
        i = int(input("Informe o idice que deseja separar: "))
        if i >=0 and i < len(nomes):
            raise ValueError("Índice fora do intervalo da lista.")
        nomes_isolado = nomes.pop(i)
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{nomes_isolado} separado com sucesso!")

        #lista exibe os valores sem o item isolado
        for i in range(len(nomes)):
            print(f"{i}: {nomes[i]}")
        print("-"*60)

        # exibe o item isolado
        print(f"Valor isolado da lista: {nomes_isolado}")
    else:
        print("Índice inválido!") 
    except Exception as e:
        print(f"Não foi possivel executar a operação. {e}.")