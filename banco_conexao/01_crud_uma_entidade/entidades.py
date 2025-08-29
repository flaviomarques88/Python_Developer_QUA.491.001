from sqlalchemy import Column, Integer, String, Date

def criar_tb_pessoa(engine, Base):
    try:
        class Pessoa(Base):
            __tablename__ = "pessoa"

            id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
            nome = Column(String, nullable=False)
            email = Column(String, nullable=False, unique=True)
            data_nascimento = Column(Date, nullable=False)

        Base.metadata.create_all(engine)  # Comando Para Criar a Tabela no Banco

        return Pessoa
    except Exception as e:
        print(f"Erro ao Conectar ao Banco de Dados. {e}")