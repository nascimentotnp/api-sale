# api-fakesto# API Fakestore

## Descrição

A API Fakestore é um sistema de gerenciamento de produtos desenvolvido em Python utilizando o Flask como framework web. O sistema segue uma arquitetura de microserviços e adota princípios de Clean Architecture. A aplicação inclui funcionalidades para registro de usuários, gerenciamento de produtos e integração com um banco de dados PostgreSQL.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework web para desenvolvimento da API.
- **Flask-RESTx**: Para criação de APIs RESTful.
- **SQLAlchemy**: ORM para interação com o banco de dados.
- **PostgreSQL**: Sistema de gerenciamento de banco de dados.
- **Docker**: Para containerização da aplicação.
- **Swagger**: Para documentação da API.
- **JWT**: Para autenticação de usuários.


## Funcionalidades

- **Cadastro de Usuários**: Permite o registro de novos usuários com validação de dados e criptografia de senhas.
- **Gerenciamento de Produtos**: CRUD (Create, Read, Update, Delete) para produtos, incluindo categorias e imagens.
- **Autenticação**: Utiliza Flask-Login para gerenciamento de sessões e JWT para autenticação de APIs.
- **Documentação da API**: Integrada com Swagger para fácil visualização e testes das rotas.

## Configuração do Ambiente

1. **Clone o repositório:**

   git clone https://github.com/seu-usuario/api-fakestore.git
   cd api-fakestore
   
2. **Configure o ambiente virtual:
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows

3. **Instale as dependências:
   pip install -r requirements.txt
4. Configure as variáveis de ambiente:

    Crie um arquivo .env na raiz do projeto com as seguintes variáveis:

    DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
   JWT_SECRET_KEY=chave_secreta
   # True for development, False for production
    DEBUG=False
    
    # Flask ENV
    FLASK_APP=run.py
    FLASK_DEBUG=0
    
    HEALTH_CHECK=health
    PATH_BASE=/sale
    PORT=8080
    # No Slash at the end
    ASSETS_ROOT=/static/assets
    
    # API_FAKE
    URL_SALE_API="https://fakestoreapi.com"
    
    # Database credentials
    DB_ENGINE=postgresql
    DB_HOST=localhost
    DB_USER=postgres
    DB_PASS=root
    DB_NAME=sale
    DB_PORT=5432
    #JWT
    JWT_ACCESS_TOKEN_EXPIRES=3600
    JWT_REFRESH_TOKEN_EXPIRES=30

    UPLOAD_FOLDER='app/static/uploads'
5. Execute a aplicação:
   flask run no terminal ou execute o docker-compose com o cmomando docker-compose up --build   




