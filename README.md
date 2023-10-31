# Projeto de Gerenciamento de Lojas, Clientes e Fornecedores

Este projeto é um sistema de gerenciamento que permite simular as relações entre lojas, clientes e fornecedores. 
Ele foi projetado para atender às seguintes regras de negócio:

### Relacionamentos

#### Lojas:

Cada loja irá ter um cliente.  
Uma loja pode ter um ou vários fornecedores.  
Cada loja pode listar diversos itens em seu estoque.

#### Clientes:

Um cliente pode estar associado a uma loja.  
Um cliente pode fazer compras em diferentes lojas.

#### Fornecedores:

Um fornecedor pode estar associado a várias lojas.  
Um fornecedor pode fornecer diversos itens para diferentes lojas.

#### Itens:

Cada item é associado a um fornecedor.  
Itens são mantidos no estoque das lojas e podem ser comprados por clientes.

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

   ![venv foto.png](..%2F..%2FDownloads%2Fvenv%20foto.png)

2. No diretório raiz, execute `pip install -r requirements.txt` para instalar as dependências.