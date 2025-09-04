import flet as ft
from dataclasses import dataclass

# classe Pessoa
@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    salario: float
    email: str

def main(page: ft.Page):
    #função do evento
    def mostrar_dados(e):
        saida_titulo.value="Dados do Usuário:\n"
        nome.value = f"Nome: {usuario.nome.value}"
        nome.value = f"Idade: {usuario.idade.value}"
        nome.value = f"Peso: {usuario.peso.value}KG"
        nome.value = f"Salário: {usuario.salario.value:.2f}"
        nome.value = f"E-Mail: {usuario.email.value}"

        page.update()

    # instancia a class
    usuario = Pessoa(nome="", idade=0, peso=0.0, salario=0.0, email="")

    # As propriedades da pagina
    page.title = "Dados do Usuário"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    #Seta os valores informado pelo usuario
    usuario.nome = ft.TextField(label="Nome")
    usuario.idade = ft.TextField(label="Idade", suffix_text="Anos")
    usuario.peso = ft.TextField(label="Peso", suffix_text="KG")
    usuario.salario = ft.TextField(label="Salário", prefix_text="R$ ")
    usuario.email = ft.TextField(label="E-Mail", on_submit=mostrar_dados)

    #variaveis de saida
    saida_titulo = ft.Text(weight="bold")
    nome = ft.Text()
    idade = ft.Text()
    peso = ft.Text()
    salario = ft.Text()
    email = ft.Text()

    
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Dados do Usuário", size=30, weight="bold"),
                alignment=ft.alignment.center,
            ),
            
            expand=True,
        ),
    
        usuario.nome,
        usuario.idade,
        usuario.peso,
        usuario.salario,
        usuario.email,
        ft.ElevatedButton("Enviar", on_click=mostrar_dados),
        saida_titulo,
        nome,
        idade,
        peso,
        salario,
        email
    
    )

ft.app(main)