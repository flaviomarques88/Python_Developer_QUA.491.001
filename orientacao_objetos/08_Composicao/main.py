import classes as c

def main():
    proprietario = c.Pessoa(nome="", cpf="", email="", telefone="", endereco="")

    carro = c.Veiculo(modelo="", fabricante="", cor="", placa="", ano="", proprietario="" )

    #INPUT
    print("🐍 DADOS DO PROPRIETÁRIO:")
    proprietario.nome = input("Informe o Nome: ").strip().title()
    proprietario.cpf = input("Informe o CPF: ").strip()
    proprietario.email = input("Informe o E-Mail: ").strip().lower()
    proprietario.telefone = input("Informe o Telefone: ").strip()
    proprietario.endereco = input("Informe o Endereço: ").strip().title()

    print("🐍 DADOS DO VEICULO:")
    carro.modelo = input("Informe o Modelo: ").strip().title()
    carro.fabricante = input("Informe o Fabricante: ").strip().title()
    carro.cor = input("Informe a Cor do Carro: ").strip()
    carro.placa = input("Informe a Placa do Carro: ").strip().upper()
    carro.ano = input("Informe o Ano do Carro: ").strip()

    carro.proprietario = proprietario

    print("\nExibindo os Dados do Veiculo:\n")
    print(f"Modelo: {carro.modelo}")
    print(f"Fabricante: {carro.fabricante}")
    print(f"Cor do Veiculo: {carro.cor}")
    print(f"Placa do Veiculo: {carro.placa}")
    print(f"Ano do Veiculo: {carro.ano}")
    print(f"Dados do Proprietario do Veiculo: {carro.proprietario}") # CORRIGIR ESTÁ LINHA

if __name__ == "__main__":
    main()