# entrada de dados 
nome = input("Informe seu nome: ")
idade = int (input("Informe sua Idade: "))
altura = float(input("Informe sua altura em metros: ").replace(",", "."))

#saida de dados 
print(f"Seja bem vindo ao curso de Python, {nome}!")
print(f"Idade do usuario: (idade).")
print(f"Altura do usuario: (altura).")

#verifica tipo de dados
print(f"{nome}: {type(nome)}.")
print(f"{idade}: {type(idade)}.")
print(f"{altura}: {type(altura)}")