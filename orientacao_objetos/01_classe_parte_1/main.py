# classe
class Pessoa:
    #atributos
    nome = "Flavio"
    idade = 30
    telefone = "(61) 99668-2501"
    cpf = "088.099.055-11"
    email = "flavio@gmail.com"

    # métado
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, meu telefone é {self.telefone}, meu CPF é {self.cpf} e meu e-mail é {self.email} ")
    
# progrma principal
if __name__ == "__main__":
    # instanciar classe
    usuario = Pessoa()

    # objeto se apresenta
    usuario.apresentar()