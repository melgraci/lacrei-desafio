\# API de Gerenciamento de Consultas Médicas



API REST desenvolvida como parte do desafio técnico da \*\*Lacrei Saúde\*\*, com o objetivo de disponibilizar um sistema para gerenciamento de profissionais e consultas médicas.



A aplicação permite realizar operações de cadastro, consulta, atualização e exclusão de profissionais e consultas, além de permitir a busca de consultas por profissional.



\## Tecnologias utilizadas



\* \*\*Python 3.13\*\*

\* \*\*Django 6.1\*\*

\* \*\*Django REST Framework\*\*

\* \*\*PostgreSQL 16\*\*

\* \*\*Poetry\*\*

\* \*\*Docker e Docker Compose\*\*

\* \*\*Gunicorn\*\*

\* \*\*Ruff\*\*

\* \*\*GitHub Actions\*\*

\* \*\*Token Authentication\*\*



\## Funcionalidades



\### Profissionais



A API permite:



\* Criar profissional

\* Listar profissionais

\* Consultar profissional por ID

\* Atualizar profissional

\* Excluir profissional



Dados cadastrados:



\* Nome social

\* Profissão

\* Endereço

\* Contato



\### Consultas



A API permite:



\* Criar consulta

\* Listar consultas

\* Consultar consulta por ID

\* Atualizar consulta

\* Excluir consulta

\* Buscar consultas por profissional



Dados cadastrados:



\* Data da consulta

\* Profissional relacionado



A relação entre consulta e profissional é feita por uma chave estrangeira.



\## Endpoints



A API utiliza o prefixo:



```text

/api/

```



\### Profissionais



```text

GET    /api/profissionais/

POST   /api/profissionais/

GET    /api/profissionais/{id}/

PUT    /api/profissionais/{id}/

PATCH  /api/profissionais/{id}/

DELETE /api/profissionais/{id}/

```



\### Consultas



```text

GET    /api/consultas/

POST   /api/consultas/

GET    /api/consultas/{id}/

PUT    /api/consultas/{id}/

PATCH  /api/consultas/{id}/

DELETE /api/consultas/{id}/

```



\### Busca de consultas por profissional



É possível filtrar as consultas utilizando o ID do profissional:



```text

GET /api/consultas/?profissional\_id=1

```



\## Autenticação



A API utiliza autenticação baseada em token através do Django REST Framework.



As requisições protegidas devem enviar o token no cabeçalho:



```http

Authorization: Token SEU\_TOKEN

```



Sem autenticação, os endpoints protegidos retornam:



```http

401 Unauthorized

```



A autenticação é aplicada por padrão às APIs através da configuração global do Django REST Framework.



\## Validação de dados



Os dados enviados para a API são validados através dos serializers do Django REST Framework.



São verificados, entre outros pontos:



\* Nome social obrigatório

\* Profissão obrigatória

\* Endereço obrigatório

\* Contato obrigatório

\* Data da consulta obrigatória

\* Profissional obrigatório

\* Existência do profissional relacionado



Dados inválidos são rejeitados pela API com respostas HTTP apropriadas.



\## Banco de dados



O projeto utiliza \*\*PostgreSQL 16\*\*.



As configurações do banco de dados são obtidas através de variáveis de ambiente, evitando que credenciais sejam armazenadas diretamente no código.



Exemplo:



```env

DB\_NAME=lacrei\_db

DB\_USER=lacrei\_user

DB\_PASSWORD=sua\_senha

DB\_HOST=db

DB\_PORT=5432

```



As credenciais reais utilizadas no ambiente local e de produção não devem ser versionadas.



\## Configuração do ambiente



As configurações sensíveis são armazenadas em arquivos `.env`.



Exemplo de `.env`:



```env

SECRET\_KEY=chave-de-desenvolvimento

DEBUG=True



DB\_NAME=lacrei\_db

DB\_USER=lacrei\_user

DB\_PASSWORD=lacrei\_password

DB\_HOST=db

DB\_PORT=5432



ALLOWED\_HOSTS=localhost,127.0.0.1

CORS\_ALLOWED\_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

```



O arquivo `.env` não deve ser enviado para o GitHub.



O ambiente de produção utiliza um arquivo separado:



```text

.env.prod

```



Esse arquivo também não deve ser versionado.



\## Execução local com Poetry



\### 1. Clonar o repositório



```bash

git clone https://github.com/melgraci/lacrei-desafio.git

cd lacrei-desafio

```



\### 2. Instalar as dependências



```bash

poetry install

```



\### 3. Configurar as variáveis de ambiente



Crie um arquivo `.env` na raiz do projeto.



Exemplo:



```env

SECRET\_KEY=chave-de-desenvolvimento

DEBUG=True



DB\_NAME=lacrei\_db

DB\_USER=lacrei\_user

DB\_PASSWORD=lacrei\_password

DB\_HOST=localhost

DB\_PORT=5432



ALLOWED\_HOSTS=localhost,127.0.0.1

CORS\_ALLOWED\_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

```



\### 4. Executar as migrações



```bash

poetry run python manage.py migrate

```



\### 5. Executar o servidor



```bash

poetry run python manage.py runserver

```



A API estará disponível em:



```text

http://127.0.0.1:8000/

```



\## Execução com Docker



O projeto possui configuração Docker para executar a aplicação juntamente com o PostgreSQL.



\### Ambiente de desenvolvimento



Execute:



```bash

docker compose up -d --build

```



A API ficará disponível em:



```text

http://localhost:8000/

```



Para visualizar os containers:



```bash

docker compose ps

```



Para visualizar os logs:



```bash

docker compose logs -f web

```



Para executar as migrações:



```bash

docker compose exec web poetry run python manage.py migrate

```



\## Ambiente de produção



O projeto possui um arquivo específico para o ambiente de produção:



```text

docker-compose.prod.yml

```



Para iniciar:



```bash

docker compose -f docker-compose.prod.yml up -d --build

```



Os containers utilizados são:



\* Aplicação Django executada com Gunicorn

\* PostgreSQL



A aplicação de produção utiliza o comando:



```bash

poetry run gunicorn config.wsgi:application --bind 0.0.0.0:8000

```



As variáveis de ambiente de produção são carregadas através do arquivo:



```text

.env.prod

```



Esse arquivo não é versionado.



\## Migrações em produção



Para executar as migrações no ambiente de produção:



```bash

docker compose -f docker-compose.prod.yml exec web poetry run python manage.py migrate

```



\## Testes automatizados



Os testes foram implementados utilizando o `APITestCase` do Django REST Framework.



Atualmente existem \*\*12 testes automatizados\*\*, cobrindo funcionalidades como:



\* CRUD de profissionais

\* Validação de profissional

\* CRUD de consultas

\* Associação entre consulta e profissional

\* Busca de consultas por profissional

\* Validação de data

\* Validação de profissional

\* Profissional inexistente

\* Acesso sem autenticação



Para executar os testes localmente:



```bash

poetry run python manage.py test

```



Para executar os testes dentro do container:



```bash

docker compose -f docker-compose.prod.yml exec web poetry run python manage.py test

```



\## Qualidade de código



O projeto utiliza \*\*Ruff\*\* para análise estática e padronização do código Python.



Para executar:



```bash

poetry run ruff check .

```



O projeto deve apresentar:



```text

All checks passed!

```



As migrações geradas automaticamente pelo Django são excluídas da análise do Ruff.



\## CORS



O projeto utiliza `django-cors-headers` para controle das origens permitidas.



As origens são configuradas através da variável:



```env

CORS\_ALLOWED\_ORIGINS

```



Exemplo:



```env

CORS\_ALLOWED\_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

```



Em produção, essa configuração deve ser ajustada para os domínios autorizados.



\## Logs



O projeto possui configuração de logging para requisições Django.



Os logs permitem acompanhar erros e requisições HTTP durante a execução da aplicação.



Em ambiente Docker, os logs podem ser consultados através de:



```bash

docker compose logs -f web

```



ou, no ambiente de produção:



```bash

docker compose -f docker-compose.prod.yml logs -f web

```



\## Estrutura do projeto



```text

lacrei-desafio/

│

├── api/

│   ├── migrations/

│   ├── models.py

│   ├── serializers.py

│   ├── tests.py

│   ├── urls.py

│   └── views.py

│

├── config/

│   ├── settings.py

│   ├── urls.py

│   ├── asgi.py

│   └── wsgi.py

│

├── .github/

│   └── workflows/

│       └── ci.yml

│

├── .dockerignore

├── .gitignore

├── Dockerfile

├── docker-compose.yml

├── docker-compose.prod.yml

├── manage.py

├── poetry.lock

├── pyproject.toml

└── README.md

```



\## CI/CD

CI/CD: GitHub Actions configurado para executar lint, testes e construção da imagem Docker. A configuração da pipeline está em desenvolvimento.



\## Segurança



Foram adotadas algumas medidas de segurança no projeto:



\* Autenticação por token

\* Validação dos dados de entrada

\* Uso do Django REST Framework

\* Uso do ORM do Django para acesso ao banco

\* Credenciais armazenadas em variáveis de ambiente

\* `.env` e `.env.prod` ignorados pelo Git

\* `.env` e `.env.prod` excluídos da imagem Docker através do `.dockerignore`

\* `DEBUG=False` no ambiente de produção

\* `SECRET\_KEY` segura no ambiente de produção

\* Configuração de CORS

\* Logging de requisições e erros



As configurações relacionadas a HTTPS, cookies seguros e HSTS serão habilitadas futuramente no ambiente AWS quando a aplicação estiver atrás de HTTPS.



\## Decisões técnicas



\### Django REST Framework



O Django REST Framework foi utilizado para facilitar a implementação da API REST, serializers, autenticação, validação e testes.



\### PostgreSQL



O PostgreSQL foi escolhido como banco de dados relacional da aplicação e é executado através de Docker no ambiente local.



\### Poetry



O Poetry é utilizado para gerenciamento de dependências e ambiente do projeto.



\### Docker



O Docker permite padronizar o ambiente de execução da aplicação e do banco de dados.



\### Gunicorn



O Gunicorn é utilizado para executar a aplicação Django em ambiente de produção, substituindo o servidor de desenvolvimento do Django.



\### Token Authentication



Foi utilizada autenticação por token para proteger os endpoints da API.



\## Rollback



O rollback da aplicação pode ser realizado através do controle de versões do Git.



Em caso de uma alteração problemática, uma versão anterior pode ser restaurada através de um revert:



```bash

git revert <commit>

```



Após o revert, a pipeline de CI/CD pode reconstruir e publicar a versão corrigida.



A estratégia definitiva de rollback do ambiente AWS será documentada futuramente após a configuração do ambiente de staging e produção.


\## Status do projeto



\### Implementado



\* \[x] API REST

\* \[x] Django

\* \[x] Django REST Framework

\* \[x] PostgreSQL

\* \[x] Poetry

\* \[x] Docker

\* \[x] Docker Compose

\* \[x] Gunicorn

\* \[x] CRUD de profissionais

\* \[x] CRUD de consultas

\* \[x] Busca de consultas por profissional

\* \[x] Validação de dados

\* \[x] Autenticação por token

\* \[x] CORS

\* \[x] Logging

\* \[x] Testes automatizados

\* \[x] Ruff

\* \[x] GitHub Actions

\* \[x] Build Docker na CI

\* \[x] Configuração de produção Docker

\* \[x] Variáveis de ambiente

\* \[x] Proteção de arquivos sensíveis



\## AWS



A etapa de deploy em AWS ainda está em desenvolvimento.



Atualmente, o projeto está preparado para execução em ambiente Docker e possui uma estrutura de produção com PostgreSQL, Gunicorn e variáveis de ambiente.



Estou estudando e aprofundando os conhecimentos em serviços AWS para realizar posteriormente o deploy da aplicação em ambiente de staging/produção.



\### Status



\* \[x] Aplicação containerizada com Docker

\* \[x] PostgreSQL configurado

\* \[x] Ambiente de produção com Gunicorn

\* \[x] CI com GitHub Actions

\* \[ ] Deploy em staging na AWS

\* \[ ] Deploy em produção na AWS

\* \[ ] Configuração de infraestrutura AWS

\* \[ ] Estratégia de rollback em ambiente AWS



A ausência do deploy em AWS neste momento é uma etapa de aprendizado e não impede a execução local da aplicação ou a execução da suíte de testes.








https://github.com/melgraci/lacrei-desafio



