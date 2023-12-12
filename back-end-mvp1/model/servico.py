from typing import Optional
from sqlalchemy import Column, String, Integer, LargeBinary, ForeignKey

from  model import Base


class Servico(Base):
    __tablename__ = 'servico'

    idServico = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    tipo = Column(String(50), nullable=False)
    estado = Column(String(50))
    cidade = Column(String(50))
    bairro = Column(String(50))
    descricao = Column(String(300), nullable=False)
    horario = Column(String(30), nullable=False)
    foto = Column(LargeBinary)
    avaliacao = Column(Integer)


    # Definição do relacionamento entre o serviço e uma pessoa.
    # Aqui está sendo definido a coluna 'idPrestadora' que vai guardar
    # a referencia à Pessoa, a chave estrangeira que relaciona
    # uma Pessoa ao um serviço.
    idPrestadora = Column(Integer, ForeignKey("pessoa.idPessoa"), nullable=False)
    
    def __init__(self, nome:str, tipo:str, estado:str, cidade:str, bairro:str, descricao:str, horario:str):
        """
        Cria um serviço

        Argumentos:
            nome: nome do serviço oferecido.
            tipo: tipo do serviço oferecido (ex: HIDRAULICA, ELETRICA, CONSTRUCAO).
            estado, cidade e bairro: onde o serviço é oferecido.
            descricao: breve descrição do serviço prestado.
            horario: intervalo de hora de disponibilidade para o serviço (12h/20h).
            foto: imagem do serviço ofertado. Funcionalidade em desenvolvimento
            avaliacao: média da avaliação dada por usuários ao serviço. Funcionalidade em desenvolvimento
        """
        self.nome = nome
        self.tipo = tipo
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.descricao = descricao
        self.horario = horario
        #self.foto = foto
        self.idServico
        self.idPrestadora
        
    def serialize(self):
        """
        Retorna o objeto em formato de dicionário
        """
        return {
            "idServico": self.idServico,
            "nome": self.nome,
            "tipo": self.tipo,
            "estado": self.estado,
            "cidade": self.cidade,
            "bairro": self.bairro,
            "descricao": self.descricao,
            "horario": self.horario,
            "idPrestadora": self.idPrestadora
        }
    
    def atualiza_servico(self, nome: Optional[str], tipo:Optional[str], estado: Optional[str], cidade: Optional[str], bairro: Optional[str], descricao: Optional[str], horario: Optional[str]):
        """
        Atualiza um serviço existente no banco de dados

        Os paramêtros são opicionais por ser um objeto existente e por isso poder ser atualizados somente alguns atributos
        """
        if nome: self.nome = nome
        if tipo: self.tipo = tipo
        if estado: self.estado = estado
        if cidade: self.cidade = cidade
        if bairro: self.bairro = bairro
        if descricao: self.descricao = descricao
        if horario: self.horario = horario


