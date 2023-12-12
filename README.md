# API MVP 1

## Sobre O Projeto

<p>Bem vindo(a)! Esse é um projeto de back-end desenvolvido para um MVP de uma aplicação fullstack, a parte de front-end do projeto pode ser encontrada aqui.
Muitas mulheres se sentem inseguras morando sozinha principalmente pela situação de estar sozinha e precisar solicitar um serviço para a casa e um homem desconhecido entrar na casa.
Com essa problemática em mente, o objetivo do projeto é desenvolver um site de divulgação de serviços realizados por mulheres para a utilização do banco de dados de Pessoas e Serviços foi desenvolvida esta API.</p>
<p>A API é divida da seguinte forma e possui sua documentação de utilização no swagger:</p>

![image](https://github.com/gabrielliosc/mvp1-back-end/assets/33656144/38680b47-6080-4758-a2fa-be66aa62319f)

---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
