#importa modulo
from modulo import limpar_tela, velocidade_media, aceleracao_media

#algoritimo principal
if __name__ == "__main__":
    v = 0

    while True:
        print("1 - Calcular Velocidade Média.")
        print("2 - Calcular Aceleração Média.")
        print("3 - Sair do Programa.")
        opcao = input("Informe a opção deseja: ").strip()
        limpar_tela()
        match opcao:
            case "1":
                try:
                    vi = float(input("Informe a velocidade Inicial: ").replace(",","."))
                except Exception as e:
                    vf = float(input("Informe a velocidade Final: ").replace(",","."))
                    v = velocidade_media
                    print(f"Erro. (e).")
                finally:
                    continue
            case "2":
                try:
                    t = float(input("Informe o Tempo: ").replace(",","."))
                    limpar_tela()
                    if v is not 0:
                        a = aceleracao_media(v, t)
                        print(f"Aceleração media: {a}.")
                    else:
                        print("Sem Informações da velocidade media.")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "3":
                print("Programa Encerrado.")
                break
            case _:
                print("Opção Inválido.")
                continue