from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from  model import Base, Servico


class Pessoa(Base):
    __tablename__ = 'pessoa'

    idPessoa = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), unique = True, nullable=False)
    senha = Column(String(8), nullable=False)
    sobre = Column(String(300))
    

    #Relacionamento entre serviços e pessoa
    servicos = relationship("Servico")

    def __init__(self, nome:str, email:str, senha:str, sobre:str):
        """
        Criação de uma pessoa

        Argumentos:
            nome: nome da pessoa.
            email: email de acesso.
            senha: senha de acesso.
            sobre: breve descrição sobre a pessoa.
        """
        self.nome = nome
        self.email = email
        self.senha = senha
        self.sobre = sobre

    def cadastro_servico(self, servico: Servico):
        """ Cadastra um novo servico à uma pessoa
        """
        self.servicos.append(servico)