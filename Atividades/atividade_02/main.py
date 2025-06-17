while True:
    try:
        #entrada de dados
        nome = input("Informe o seu nome: ").title().strip()
        peso = float(input("Informe seu peso KG: " )).replace(',', '.')
        altura = float(input("Informe Sua altura em Metro: ").replace(',', '.'))
        imc = peso / altura **2

        print(f"O valar do IMC de {nome} é {imc:.2f}")

        if imc < 18.5:
            print(f"{nome} está abaixo do peso.")
        elif imc < 25:
            print(f"{nome} está no peso ideal.")
        elif imc < 30:
            print(f"{nome} está acima do peso.")
        elif imc < 40:
            print(f"{nome} está obeso.")
        else:
            while True:
              prossegrir = input("Deseja Refazer? (S/N): ").strip().upper()
              if prossegrir ==  "S" or prossegrir  == "N":
                break
              else:
                  print("Opção Invalida.")
                  continue
              
        match prossegrir:
            case "S":
                continue 
            case "N":
                break                      
    
    except Exception as e:
        print(f"Não foi calcular o IMC: {e}.")
        continue