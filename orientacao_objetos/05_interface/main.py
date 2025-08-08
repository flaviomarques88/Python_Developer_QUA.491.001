import classes as c

def main():
    # Instacia Objeto da Classes Conta
    cc = c.ContaCorrente(
    titular="",
    cpf="",
    agencia="001-1",
    conta="2025-1",
    saldo=0.0
    )

    cc.consultar_dados()
      #TODO Continuem com a Construção do Programa

if __name__ == "__main__":
    main()