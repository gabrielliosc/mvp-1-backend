from pydantic import BaseModel
from typing import Optional, List


class PessoaServicoSchema(BaseModel):

    """ Define como uma pessoa deve ser retornada nos serviços
    """
    idPessoa: int
    nome: str

class ServicoPessoaSchema(BaseModel):
    """ Define como um serviço deve ser retornada na pessoa
    """
    idServico: int = 1
    nome: str = 'Trabalho com encanamento'
    tipo: str = 'HIDRAULICA'
    estado: Optional[str] = 'RJ'
    cidade: Optional[str] = 'RIO DE JANEIRO'
    bairro: Optional[str] = 'FLAMENGO'
    descricao: str = 'Serviço de conserto de encanamento'
    horario: str = '12h/20h'
    idPrestadora: int = 1