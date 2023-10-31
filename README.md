# Projeto de Gerenciamento de Lojas, Clientes e Fornecedores

Este projeto é um sistema de gerenciamento que permite simular as relações entre lojas, clientes e fornecedores. 
Ele foi projetado para atender às seguintes regras de negócio:

### Relacionamentos

#### Lojas:

Cada loja pode ter um ou mais clientes.  
Uma loja pode ter um ou vários fornecedores.  
Cada loja pode listar diversos itens em seu estoque.

#### Clientes:

Um cliente pode estar associado a uma loja.  

#### Fornecedores:

Um fornecedor pode estar associado a várias lojas.  
Um fornecedor pode fornecer diversos itens para diferentes lojas.

#### Itens:

Cada item é associado a um fornecedor.  
Itens são mantidos no estoque das lojas e podem ser comprados por clientes.

![sic_db](https://github.com/joselisboaa/Flask-SIC/assets/67613937/3454dd26-ca6a-4fb0-9a9f-d23a53522a45)


### Funcionalidades
* CRUD de Lojas
* CRUD de Clientes
* CRUD de Fornecedores
* CRUD de Itens

### Pré-requisitos e configuração para o Projeto

1. Instale o `python 3.8.x` ou `python 3.10.x` usando seu gerenciador de pacotes, caso não tenha instalado. Para isso você possivelmente vai precisar de permissão.

2. Crie um ambiente virtual (venv):

    `python3 -m venv venv`

### Instalando as dependências do Projeto

1. Ative o ambiente virtual de acordo com seu sistema operacional:

    * Em sistemas Linux-based, execute `source venv/bin/activate`.
    * No Windows usando o Prompt, execute `venv\Scripts\activate.bat`.
    * No Windows usando o PowerShell, execute `.venv\Scripts\activate.ps1`.
    * No Windows usando o Git Bash, execute `source venv\Scripts\activate`.

    Sempre que for executar o projeto verifique se o ambiente virtual está ativado, como pode ser visto abaixo:

    ![venv foto](https://github.com/joselisboaa/Flask-SIC/assets/67613937/bb42e351-4ec1-4bad-8b10-4dcc979e25dd)

2. No diretório raiz, execute `pip install -r requirements.txt` para instalar as dependências.


### Referência das bibliotecas utilizadas

[Flask](https://flask.palletsprojects.com/en/2.3.x/)  
[Flask Smorest](https://flask-smorest.readthedocs.io/en/latest/)  
[Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)   
[Psycopg](https://www.psycopg.org/)  
[Alembic](https://alembic.sqlalchemy.org/en/latest/)  
[Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/)  
[SQLAlchemy](https://www.sqlalchemy.org/)  
[Python-dotenv](https://pypi.org/project/python-dotenv/)  
[Marshmallow](https://marshmallow.readthedocs.io/en/stable/)  
