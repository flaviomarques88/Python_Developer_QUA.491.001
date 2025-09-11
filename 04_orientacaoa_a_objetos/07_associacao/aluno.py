class Aluno:
    def __init__(self, nome_aluno, matricula):
        self.__nome_aluno = nome_aluno
        self.__matricula = matricula
        self.cursos_inscritos = []
        
#ALUNO
@property
def nome_aluno(self):
    return self.__nome_aluno

@nome_aluno.setter
def nome_aluno(self, nome_aluno):
    self.__nome_aluno = nome_aluno


#MATRICULA
@property
def matricula(self):
    return self.__matricula

@matricula.setter
def matricula(self, matricula):
    self.__matricula = matricula

#Métados de Ação
def inscrever_curso(self, curso):
    if curso not in self.cursos_inscritos:
        self.cursos_inscritos.append(curso)
        curso.adicionar_aluno(self) #Associa o Aluno ao Curso

def listar_cursos(self):
    lista = []
    for curso in self.cursos_inscritos:
        lista.append(curso.nome_curso)
        return lista