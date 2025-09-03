import flet as ft


def main(page: ft.Page):
    page.title = "Meu Primeiro app Flet"
    page.scroll = "adaptive"

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Column({
                    ft.Text("Ola, Mundo Flet Python!!!",
                        size=30,
                        weight="bold"
                        ),
                        ft.Text("😎😎🐍👌", size=30)  
                })
                    
            ),
            expand=True,
        ),
        ft.Image(
        src="\foto-imagem.jpg",
        fit=ft.ImageFit.CONTAIN,
        erro_content=ft.Text("Não Foi Possivel Carregar a Imagem."),
    
        )

    )


ft.app(main)