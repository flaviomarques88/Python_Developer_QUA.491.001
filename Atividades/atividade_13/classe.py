import json

class Conta:
    #Construtor
    def __init__(self, titular, cpf, agencia, conta, saldo):
        # Atributos
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    #Métados
    def Consultar_dados(self):
        print(f"Titular: {self.titular}.")
        print(f"CPF: {self.cpf}.")
        print(f"Agência: {self.agencia}.")
        print(f"Conta: {self.conta}.")
        print(f"Saldo: R$ {self.saldo:.2f}.")

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo

    def imprimir_extrato(self):
            dados = {
                'Nome do Titular': self.titular,
                'CPF do Titular': self.cpf,
                'Agência': self.agencia,
                'Conta': self.conta,
                'Saldo': self.saldo
            }
            with open("conta.json", "w", encoding="utf-8") as f:
                json.dump(dados, f, ensure_ascii=False, indent=4)
                