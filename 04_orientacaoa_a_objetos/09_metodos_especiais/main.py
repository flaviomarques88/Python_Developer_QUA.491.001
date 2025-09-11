import Pessoa

def main():
    usuario = Pessoa.Pessoa(nome="Flavio", idade=30)
    
    print(usuario)
    print(f"Idade: {len(usuario)}")
   
    #Destruição de Objeto
    del(usuario)

if __name__ == "__main__":
    main()