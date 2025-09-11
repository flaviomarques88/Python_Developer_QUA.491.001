import curso
import aluno

def main():
    # Instancia as Classes
    curso1 = curso.curso(nome_curso="Python")
    curso2 = curso.curso(nome_curso="Java")
    aluno1 = aluno.aluno(nome_aluno="Fulano", matricula="2025-1")
    aluno2 = aluno.aluno(nome_aluno="Cicrano", matricula="2025-2")
    aluno3 = aluno.aluno(nome_aluno="Beltrano", matricula="2025-3")
    aluno4 = aluno.aluno(nome_aluno="Flavio", matricula="2025-4")
    aluno5 = aluno.aluno(nome_aluno="Maria", matricula="2025-5")
    aluno6 = aluno.aluno(nome_aluno="José", matricula="2025-6")

    #Inscrevendo Alunos no Curso 2
    aluno1.inscrever_curso(curso1)
    aluno2.inscrever_curso(curso1)
    aluno3.inscrever_curso(curso1)
    aluno4.inscrever_curso(curso1)

    #Inscrevendo Alunos no Curso 2
    aluno5.inscrever_curso(curso2)
    aluno6.inscrever_curso(curso2)

    # Lista de Alunos do Curso 1
    print(f"Curso: {curso1.nome_curso}")
    print("Lista de Alunos:")
    for aluno in curso1.listar_alunos():
        print(aluno)

if __name__ == "__main__":
    main()