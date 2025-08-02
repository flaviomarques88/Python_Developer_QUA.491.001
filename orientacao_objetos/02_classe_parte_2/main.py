# classe
class Pessoa:
    #construtor
    def __init__(self, nome, idade, telefone, cpf, email):
        #atributos da classe
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cpf = cpf
        self.email = email

#métado de ação
def apresentar(self):
    return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos,  meu telefone é {self.telefone}, meu CPF é {self.cpf} e meu e-mail é {self.email}."
    # algoritmo principal
if __name__ == "__main__":
    usuario = Pessoa(
        nome="",
        idade=0,
        telefone="",
        cpf="",
        email=""
    )
   

    try:
        #input
        usuario.nome = input("Informe seu Nome: ").strip().title()
        usuario.idade = int(input("Informe sua Idade: "))
        usuario.telefone = input("Informe seu Telefone: ").strip()
        usuario.cpf = input("Informe seu CPF: ").strip()
        usuario.email = input("Informe seu E-mail: ").strip().lower()

        #chama o métado
        print(usuario.apresentar())
    except Exception as e:
        print(f"Erro. {e}.")