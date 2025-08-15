from deep_translator import GoogleTranslator
import os 

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    tradutor = GoogleTranslator(source="auto", target="pt")

    while True:
        try:
            print("1 - TRADUZIR TEXTO.")
            print("2 - SAIR DO PROGRAMA.")
            opcao = input("Informe a Opção Desejada.").strip()
            limpar()
            match opcao:
                case"1":
                    texto_original = input("Digite o Texo a Traduzido: ")
                    texto_traduzido = tradutor.translate(texto_original)
                    print(f"Texto Traduzido:\n{texto_traduzido}")
                case"2":
                    print("Programa Encerrado.")
                    break
                case _:
                    print("Opção Inválida.")
                    continue
        except Exception as e:
            print(f"Não foi possivel traduzir. {e}.")
            continue
            
if __name__ == "__main__":
    main()