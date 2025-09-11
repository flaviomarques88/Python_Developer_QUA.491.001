import modulo as mo
if __name__ == "__main__":

    while True:
        print("1 - Calcular Equação do 1º Grau.")
        print("2 - Calcular Equação do 2º Grau.")
        print("3 - Sair do Programa.")
        opcao = input("Informe a Opção Desejada: ").strip()
        mo.limpar_tela()
        match opcao:
            case"1":
                try:
                    a = float(input("Informe o valor de A: ").replace(",", "."))
                    b = float(input("Informe o valor de B: ").replace(",", "."))
                    mo.limpar_tela()
                    x = mo.primeiro_grau(a, b)
                    print(f"O Valor de x é {x}.")
                except Exception as e:
                    print(f"Erro. (e).")
                finally:
                    continue
            case"2":
                try:
                    a = float(input("Informe o Valor de A: ").replace(",","."))
                    b = float(input("Informe o Valor de B: ").replace(",","."))
                    c = float(input("Informe o Valor de C: ").replace(",","."))
                    mo.limpar_tela()
                    x = mo.segundo_grau(a, b, c)
                    for result in x:
                        print(f"{result}.")
                    
                except Exception  as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case"3":
                print("Programa Encerrado.")
                break
            case _:
                print("Opção Inválido.")
                continue