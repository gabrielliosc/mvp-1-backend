from model.servico import Servico
from pydantic import BaseModel
from typing import Optional, List
from model.pessoa import Pessoa

from schemas.pessoa_servico import ServicoPessoaSchema


class PessoasSchema(BaseModel):
    """ Define como uma nova pessoa a ser inserida deve ser representada
    """
    nome: str = 'Larissa Rodrigues'
    email: str = 'larissarodrigues@gmail.com'
    senha: str = 'senha253'
    sobre: Optional[str] = 'Sobre Larissa'

class PessoaBuscaSchema(BaseModel):
    """ 
        Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no email da pessoa.
    """
    email: str = "larissarodrigues@gmail.com"

class PessoaBuscaDelSchema(BaseModel):
    """ 
        Define como deve ser a estrutura que representa a busca para deletar uma pessoa da base. Que será feita apenas com base no id da pessoa.
    """
    idPessoa: int = "1"

class PessoaViewSchema(BaseModel):
    """ Define como uma pessoa será retornada: pessoa + serviços.
    """
    nome: str = 'Larissa Rodrigues'
    email: str = 'larissarodrigues@gmail.com'
    senha: str = 'senha253'
    sobre: Optional[str] = 'Sobre Larissa'
    servicos:List[ServicoPessoaSchema]

def apresenta_servicos(servicos: List[Servico]):
    """ Retorna uma representação de serviços seguindo o schema definido em
        ServicoPessoaSchema.
    """
    result = []
    for servico in servicos:
        result.append({
            "idServico": servico.idServico,
            "nome": servico.nome,
            "tipo": servico.tipo,
            "estado": servico.estado,
            "cidade": servico.cidade,
            "bairro": servico.bairro,
            "descricao": servico.descricao,
            "horario": servico.horario,
            "idPrestadora": servico.idPrestadora
        })

    return result

def apresenta_pessoa(pessoa: Pessoa, servicos: List[Servico]):
    """ Retorna uma representação da pessoa seguindo o schema definido em
        PessoaViewSchema.
    """
    return {
        "id": pessoa.idPessoa,
        "nome": pessoa.nome,
        "email": pessoa.email,
        "senha": pessoa.senha,
        "sobre": pessoa.sobre,
        "servicos": servicos
    }
