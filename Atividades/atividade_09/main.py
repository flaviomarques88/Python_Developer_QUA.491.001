#atividade
#declaração de variveis
import os

usuarios =[]
lista = {

}

#função para cadastrar usuarios
while True:
    print("🐍 MENU DE OPÇÕES")
    print("1  Cadastro um Novo Usuários")
    print("2 - Listar Todos os Usuários")
    print("3 - Alterar um Usuário")
    print("4 - Sorteia o Usuário")
    print("5 - Excluir um Usuário")
    print("6 - Sair do Programa")
    opcao = input("INFORME A OPÇÃO DESEJADA:")
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
           try:
                nome = input("Informe o Nome Completo: ").title().strip()
                data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA):").strip()
                email = input("Digite o E-mail: ").strip
                cpf = input("Digite o CPF: ").strip()
                telefone = input("Digite o Telefone: ")
                genero = input("Informe o Gênero (M/F): ").strip().upper()
                if genero not in ["M", "F"]:
                    print("Gênero inválido. Use 'M' para Masculino ou 'F' para Feminino.")
     
           finally:
                    continue
                
        case "2":
            try:
                lista = usuarios
                if lista:
                    print("Lista - Usuários Cadastrados: ")
                for i, in enumerate(lista, start=1):
                      for i, usuarios in enumerate(lista, start=1):
                        print(f"{i}. {usuarios}")
                else:
                    print("A lista está vazia.")
            except Exception as e:
                print(f"Não Foi Possível Exibir a Lista: {e}")
            finally:
                continue
        case "3":
            try:
                nome_usuario = input("Digite o Nome do Usuário que Deseja Alterar: ").title().strip()
                if nome_usuario in usuarios:
                    novo_nome = input("Digite o novo nome: ").title().strip()
                    indice = usuarios.index(nome_usuario)
                    usuarios[indice] = novo_nome
                    print(f"{nome_usuario} Foi Alterado Para {novo_nome}.")
                else:
                    print(f"{nome_usuario} não encontrado na lista.")
            except Exception as e:
                print(f"Erro ao alterar usuário: {e}")
            finally:
                continue
            
        case "4":
            try:
                if usuarios:
                    import random
                    sorteado = random.choice(usuarios)
                    print(f"O Usuário Sorteado é: {sorteado}")
                else:
                    print("Nenhum usuário Cadastrado para Sortear.")
            except Exception as e:
                print(f"Erro ao sortear usuário: {e}")
            finally:
                continue

        case "5":
            try:
                nome_excluir = input("Digite o Nome do Usuário que Deseja Excluir: ").title().strip()
                if nome_excluir in usuarios:
                    usuarios.remove(nome_excluir)
                    print(f"{nome_excluir} Foi Removido da Lista.")
                else:
                    print(f"{nome_excluir} não encontrado na lista.")
            except Exception as e:
                print(f"Erro ao Excluir Usuário: {e}")
            finally:
                continue

        case "6":
            try:
                print("Sair do Programa.")
            except Exception as e:
                print(f"Erro ao Sair do Programa: {e}")
            break
        
        case _:
           
            print("Opção Invalida. ")