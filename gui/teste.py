import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de Combustível"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Combustível: Gasolina ou Diesel
    combustivel_tipo = ft.Dropdown(
        label="Tipo de Combustível",
        options=[
            ft.dropdown.Option("Gasolina"),
            ft.dropdown.Option("Diesel")
        ],
        width=300
    )

    # Preço por litro
    preco_input = ft.TextField(label="Preço por litro (R$)", width=300, keyboard_type="number")

    # Quantidade de litros
    litros_input = ft.TextField(label="Quantidade de litros", width=300, keyboard_type="number")

    # Resultado
    resultado_texto = ft.Text(value="", size=20, color=ft.colors.GREEN_800)

    # Função de cálculo
    def calcular_total(e):
        try:
            preco = float(preco_input.value)
            litros = float(litros_input.value)
            tipo = combustivel_tipo.value

            total = preco * litros

            resultado_texto.value = f"Total a pagar com {tipo}: R$ {total:.2f}"
            page.update()
        except:
            resultado_texto.value = "Erro: verifique os dados inseridos."
            resultado_texto.color = ft.colors.RED
            page.update()

    # Botão de calcular
    calcular_btn = ft.ElevatedButton(text="Calcular", on_click=calcular_total)

    # Adicionar tudo na página
    page.add(
        ft.Text("Calculadora de Gasolina e Diesel", size=24, weight="bold"),
        combustivel_tipo,
        preco_input,
        litros_input,
        calcular_btn,
        resultado_texto
    )

# Rodar o app
ft.app(target=main)
