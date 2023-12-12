from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Pessoa, Servico
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="API Serviços de Mulheres para Mulheres", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
pessoa_tag = Tag(name="Pessoa", description="Adição, visualização e remoção de pessoa à base")
servico_tag = Tag(name="Serviços", description="Adição, visualização, edição de serviços à uma pessoa cadastrada na base")


@app.get('/')
def home():
    return redirect('/openapi/swagger')


@app.post('/pessoa', tags=[pessoa_tag],
          responses={"200": PessoaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_pessoa(form: PessoasSchema):
    """Adiciona uma nova Pessoa à base de dados

    Retorna uma representação da pessoa e serviços associados.
    """
    pessoa = Pessoa(
        nome = form.nome,
        email = form.email,
        senha = form.senha,
        sobre = form.sobre or None)
    
    logger.debug(f"Adicionando a pessoa: '{pessoa.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando pessoa
        session.add(pessoa)
        # efetivando o comando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionando a pessoa: '{pessoa.nome}'")
        return apresenta_pessoa(pessoa, []), 200

    except IntegrityError as e:
        # como a duplicidade de email é a provável razão do IntegrityError
        error_msg = "Email existente na base"
        logger.warning(f"Erro na pessoa '{pessoa.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar nova pessoa"
        logger.warning(f"Erro ao adicionar pessoa '{pessoa.nome}', {e}")
        return {"mesage": error_msg}, 400


@app.get('/pessoa', tags=[pessoa_tag],
         responses={"200": PessoaViewSchema, "404": ErrorSchema})
def get_pessoa(query: PessoaBuscaSchema):
    """Faz a busca por uma Pessoa a partir do email da pessoa

    Retorna uma representação da pessoa e dos serviços relacionados
    """
    pessoa_email = query.email
    logger.debug(f"Coletando dados sobre o usuário #{pessoa_email}")

    # criando conexão com a base
    session = Session()

    # fazendo a busca
    pessoa = session.query(Pessoa).filter(Pessoa.email == pessoa_email).first()

    if not pessoa:
        # se a pessoa não for encontrada
        error_msg = "Pessoa não encontrada na base :/"
        logger.warning(f"Erro ao buscar pessoa '{pessoa_email}', {error_msg}")

        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Pessoa Encontrada: '{pessoa.nome}'")
        # Busca na base os serviços da pessoa em questão
        servicos = session.query(Servico).filter(Servico.idPrestadora == pessoa.idPessoa).all()
        
        #Criação da listagem de serviços da pessoa em questão
        result = []
        for servico in servicos:
            result.append(servico.serialize())

        return apresenta_pessoa(pessoa, result), 200


@app.delete('/pessoa', tags=[pessoa_tag],
            responses={"200": PessoaViewSchema, "404": ErrorSchema})
def del_pessoa(query: PessoaBuscaDelSchema):
    """Deleta uma Pessoa a partir do email de uma pessoa informada

    Retorna uma mensagem de confirmação da remoção.
    """
    idPessoa = query.idPessoa

    logger.debug(f"Deletando dados sobre pessoa de id #{idPessoa}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção da pessoa e de seus serviços
    session.query(Servico).filter(Servico.idPrestadora == idPessoa).delete()
    pessoa = session.query(Pessoa).filter(Pessoa.idPessoa == idPessoa).delete()  

    session.commit()

    if pessoa:
        logger.debug(f"Deletado pessoa #{idPessoa}")
        return {"mesage": "Pessoa e seus serviços removidos", "id": idPessoa}
    else:
        # se a pessoa não foi encontrada
        error_msg = "Pessoa não encontrada na base"
        logger.warning(f"Erro ao deletar pessoa de id {idPessoa}', {error_msg}")
        return {"mesage": error_msg}, 404

@app.post('/servico', tags=[servico_tag],
          responses={"200": ServicoViewSchema, "404": ErrorSchema})
def add_servico(form: ServicoSchema):
    """Adiciona um novo serviço à uma pessoa cadastrada na base identificada pelo id

    Retorna uma representação da pessoa e serviços associados.
    """
    pessoa_id  = form.idPrestadora
    logger.debug(f"Adicionando serviço à pessoa #{pessoa_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca pela pessoa
    pessoa = session.query(Pessoa).filter(Pessoa.idPessoa == pessoa_id).first()
    
    if not pessoa:
        #Pessoa não encontrada
        error_msg = "Pessoa não encontrada na base"
        logger.warning(f"Erro ao adicionar serviço a pessoa'{pessoa_id}', {error_msg}")
        return {"mesage": error_msg}, 404

    # adicionando o serviço à pessoa
    
    servico = Servico(nome=form.nome,tipo=form.tipo, estado=form.estado, cidade=form.cidade, bairro=form.bairro, descricao=form.descricao, horario=form.horario)
    
    pessoa.cadastro_servico(servico)
    
    session.commit()

    logger.debug(f"Adicionado serviço a pessoa #{pessoa_id}")

    # retorna a representação de serviço
    return apresenta_servico(servico, pessoa), 200

@app.get('/servicos', tags=[servico_tag],
         responses={"200": ListagemServicosSchema, "404": ErrorSchema})
def get_servicos():
    
    logger.debug(f"Coletando dados de serviços cadastrados")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    servicos = session.query(Servico)

    if not servicos:
        # se não foi encontrado serviços
        error_msg = "Nem um serviço encontrado"
        logger.warning(f"Erro ao buscar serviços, {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Serviços encontrados:")
        # retorna a representação de serviços e informação da prestadora do serviço
        result = []
        for servico in servicos:
            pessoa = session.query(Pessoa).filter(Pessoa.idPessoa == servico.idPrestadora).first()
            result.append(apresenta_servico(servico, pessoa))

        return {'Servicos': result}, 200
    
@app.put('/servico', tags=[servico_tag],
          responses={"200": ServicoViewSchema, "404": ErrorSchema})
def update_servico(form: ServicoBuscaSchema):
    """Edita um  serviço na base identificado pelo id

    Retorna uma representação do serviço
    """

    logger.debug(f"Editando o serviço de id #{form.idServico}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca pelo serviço e pessoa
    servico = session.query(Servico).filter(Servico.idServico == form.idServico).first()
    pessoa = session.query(Pessoa).filter(Pessoa.idPessoa == form.idPrestadora).first()
    
    if not servico:
        #Serviço não encontrada
        error_msg = "Serviço não encontrado na base"
        logger.warning(f"Erro ao editar serviço de id'{form.idServico}', {error_msg}")
        return {"mesage": error_msg}, 404

    # Atualizando o serviço

    servico.atualiza_servico(nome=form.nome,tipo=form.tipo, estado=form.estado, cidade=form.cidade, bairro=form.bairro, descricao=form.descricao, horario=form.horario)
    
    session.commit()

    logger.debug(f"Atualizando o serviço de id #{form.idServico}")
    
    # retorna a representação de serviço
    return apresenta_servico(servico, pessoa), 200