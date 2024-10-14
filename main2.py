import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker,declarative_base

BANCO = create_engine("sqlite:///banco.db")

Session = sessionmaker(bind=BANCO)

session = Session()
Base = declarative_base()

class Aluno(Base):
    __tablename__= "alunos"

    #Definindo campos da tabela.
    id = Column("ra",Integer,primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    nome = Column("sobrenome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    #Definindo atributos da classe.
    def __init__(self,nome: str, email: str, senha: str,ra: str,sobrenome: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ra = ra
        self.email = email
        self.senha = senha


#Criando tabela no banco de dados.
Base.metadata.create_all(bind=BANCO)

os.system("clear")
print("Solicitando dados para  o usuário. ")
inserir_ra = input("Digite seu R.A.: ")
inserir_nome = input("Digite seu nome: ")
inserir_sobrenome = input("Digite seu sobrenome: ")
inserir_email= input("Digite seu email: ")
inserir_senha = input("Digite seu senha: ")


aluno= Aluno(nome=inserir_nome,sobrenome=inserir_sobrenome,ra=inserir_ra, email=inserir_email, senha=inserir_senha)
session.add(aluno)
session.commit()

# Read - Select - Consulta
print("\nExibindo dados de todos os clientes.")
lista_alunos = session.query(Aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.ra} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha} ")

# U - Update - UPDATE - Atualizar 
print("\nAtualizando dados do usuario.")
email_aluno = input("Digite o email do aluno que será atualizado: ")

if aluno:
    aluno.nome = input("Digite seu nome: ")
    aluno.email = input("Digite seu email: ")
    aluno.senha = input("Digite sua senha: ")

    session.commit()
else:
    print("Aluno não encontrado!")

#R - Read = SELECT - Consulta
print("\nExibindo dados de todos os clientes.")
lista_alunos = session.query(aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.ra} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha} ")
