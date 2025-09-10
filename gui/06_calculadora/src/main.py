import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora App"
    page.bgcolor = ft.Colors.BLACK
    expression = ""

    # Resultado exibido na tela
    result = ft.Text(
        value="0",
        color=ft.Colors.WHITE,
        size=15,
        text_align=ft.TextAlign.RIGHT,
        expand=True,
    )

    # === Botão base com evento de clique ===
    class CalcButton(ft.ElevatedButton):
        def __init__(self, text, expand=1):
            super().__init__(
                text=text,
                expand=expand,
                on_click=self.button_clicked,
            )
            self.data = text

        def button_clicked(self, e):
            nonlocal expression
            value = e.control.data

            if value == "AC":
                expression = ""
            elif value == "=":
                try:
                    expression = str(eval(expression))
                except:
                    expression = "Erro"
            elif value == "+/-":
                if expression.startswith("-"):
                    expression = expression[1:]
                else:
                    expression = "-" + expression
            else:
                expression += value

            result.value = expression if expression else "0"
            page.update()

    # === Tipos de Botões com Cores ===
    class DigitButton(CalcButton):
        def __init__(self, text, expand=1):
            super().__init__(text, expand)
            self.bgcolor = ft.Colors.WHITE24
            self.color = ft.Colors.WHITE

    class ActionButton(CalcButton):
        def __init__(self, text):
            super().__init__(text)
            self.bgcolor = ft.Colors.ORANGE
            self.color = ft.Colors.WHITE

    class ExtraActionButton(CalcButton):
        def __init__(self, text):
            super().__init__(text)
            self.bgcolor = ft.Colors.BLUE_GREY_100
            self.color = ft.Colors.BLACK

    # === Layout da calculadora ===
    layout = ft.Container(
        width=350,
        bgcolor=ft.Colors.BLACK,
        border_radius=ft.border_radius.all(20),
        padding=20,
        content=ft.Column(
            controls=[
                ft.Container(
                    content=result,
                    alignment=ft.alignment.center_right,
                    padding=ft.padding.only(right=10, bottom=20),
                    height=80,
                ),
                ft.Row(
                    controls=[
                        ExtraActionButton("AC"),
                        ExtraActionButton("+/-"),
                        ExtraActionButton("%"),
                        ActionButton("/"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton("7"),
                        DigitButton("8"),
                        DigitButton("9"),
                        ActionButton("*"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton("4"),
                        DigitButton("5"),
                        DigitButton("6"),
                        ActionButton("-"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton("1"),
                        DigitButton("2"),
                        DigitButton("3"),
                        ActionButton("+"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton("0", expand=2),
                        DigitButton("."),
                        ActionButton("="),
                    ]
                ),
            ]
        )
    )

    page.add(layout)

ft.app(main)