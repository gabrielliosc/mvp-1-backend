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



# from pydantic import BaseModel
# from typing import Optional, List
# from model.produto import Produto

# from schemas import ComentarioSchema


# class ProdutoSchema(BaseModel):
#     """ Define como um novo produto a ser inserido deve ser representado
#     """
#     nome: str = "Banana Prata"
#     quantidade: Optional[int] = 12
#     valor: float = 12.50


# class ProdutoBuscaSchema(BaseModel):
#     """ Define como deve ser a estrutura que representa a busca. Que será
#         feita apenas com base no nome do produto.
#     """
#     nome: str = "Teste"


# class ListagemProdutosSchema(BaseModel):
#     """ Define como uma listagem de produtos será retornada.
#     """
#     produtos:List[ProdutoSchema]


# def apresenta_produtos(produtos: List[Produto]):
#     """ Retorna uma representação do produto seguindo o schema definido em
#         ProdutoViewSchema.
#     """
#     result = []
#     for produto in produtos:
#         result.append({
#             "nome": produto.nome,
#             "quantidade": produto.quantidade,
#             "valor": produto.valor,
#         })

#     return {"produtos": result}


# class ProdutoViewSchema(BaseModel):
#     """ Define como um produto será retornado: produto + comentários.
#     """
#     id: int = 1
#     nome: str = "Banana Prata"
#     quantidade: Optional[int] = 12
#     valor: float = 12.50
#     total_cometarios: int = 1
#     comentarios:List[ComentarioSchema]


# class ProdutoDelSchema(BaseModel):
#     """ Define como deve ser a estrutura do dado retornado após uma requisição
#         de remoção.
#     """
#     mesage: str
#     nome: str

# def apresenta_produto(produto: Produto):
#     """ Retorna uma representação do produto seguindo o schema definido em
#         ProdutoViewSchema.
#     """
#     return {
#         "id": produto.id,
#         "nome": produto.nome,
#         "quantidade": produto.quantidade,
#         "valor": produto.valor,
#         "total_cometarios": len(produto.comentarios),
#         "comentarios": [{"texto": c.texto} for c in produto.comentarios]
#     }