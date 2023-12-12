from typing import Optional, List
from pydantic import BaseModel
from sqlalchemy import LargeBinary

from schemas.pessoa_servico import PessoaServicoSchema
from model.servico import Servico


class ServicoSchema(BaseModel):
    """ Define como um novo serviço a ser inserido deve ser representado
    """
    nome: str = 'Trabalho com encanamento'
    tipo: str = 'HIDRAULICA'
    estado: Optional[str] = 'RJ'
    cidade: Optional[str] = 'RIO DE JANEIRO'
    bairro: Optional[str] = 'FLAMENGO'
    descricao: str = 'Serviço de conserto de encanamento'
    horario: str = '12h/20h'
    idPrestadora: int = 1

class ServicoViewSchema(BaseModel):
    """ Define como um serviço será retornado: serviço + prestadora do serviço.
    """
    idServico: int
    nome: str
    tipo: str
    estado: str
    cidade: str
    bairro: str
    descricao: str
    horario: str
    idPrestadora: int
    pessoa: PessoaServicoSchema

class ListagemServicosSchema(BaseModel):
    """ Define como uma listagem de serviços será retornada.
    """
    servicos:List[ServicoViewSchema]

def apresenta_servico(servico: Servico, pessoa: PessoaServicoSchema):
    """ Retorna uma representação do serviço seguindo o schema definido em
        ServicoViewSchema.
    """
    result = {
            "idServico": servico.idServico,
            "nome": servico.nome,
            "tipo": servico.tipo,
            "estado": servico.estado,
            "cidade": servico.cidade,
            "bairro": servico.bairro,
            "descricao": servico.descricao,
            "horario": servico.horario,
            "foto": servico.foto,
            "idPrestadora": servico.idPrestadora,
            "prestadora": {"nome": pessoa.nome, "idPessoa": pessoa.idPessoa}
    }
    
    return result