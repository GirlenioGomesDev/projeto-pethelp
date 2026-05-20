# PetHelp

PetHelp é uma aplicação web para cadastro e consulta de publicações sobre pets perdidos, encontrados e disponíveis para adoção.

O projeto foi criado como prática de desenvolvimento web com Django. A ideia é centralizar informações básicas como foto, bairro, cidade, características do animal e telefone de contato, facilitando a divulgação em uma única página em vez de deixar tudo espalhado em mensagens ou redes sociais.

A aplicação foi desenvolvida com Python, Django e SQLite, usando templates HTML, CSS próprio e autenticação nativa do Django.

## Funcionalidades

- Cadastro de usuários.
- Login e logout.
- Visualização pública das publicações.
- Cadastro de pets perdidos.
- Cadastro de pets encontrados.
- Cadastro de pets para adoção.
- Upload de imagem do pet.
- Preview da imagem antes do envio.
- Página de detalhes para cada publicação.
- Busca por nome, bairro, cidade, raça ou características.
- Filtro por categoria.
- Painel "Minhas Publicações" para o usuário logado.
- Edição de publicações pelo dono ou superusuário.
- Exclusão de publicações pelo dono ou superusuário.
- Campo de telefone com máscara e validação.
- Campo de data com texto ajustado conforme a categoria da publicação.
- Painel administrativo padrão do Django.
- Persistência dos dados em SQLite.

## Tecnologias

- Python
- Django
- SQLite
- HTML
- CSS
- JavaScript
- Pillow
- Gunicorn
- WhiteNoise

## Estrutura do Projeto

```text
projeto-pethelp/
├── accounts/                 # Cadastro, login e logout de usuários
├── animais/                  # App antigo mantido no repositório
├── media/                    # Imagens enviadas pelos usuários
├── pethelp/                  # Configurações principais do Django
├── pets/                     # App principal de publicações
├── static/                   # Arquivos CSS e JavaScript
├── staticfiles/              # Arquivos estáticos coletados
├── templates/                # Templates HTML
├── db.sqlite3                # Banco local SQLite
├── manage.py                 # Comando principal do Django
├── requirements.txt          # Dependências do projeto
├── build.sh                  # Script usado no deploy
├── render.yaml               # Configuração para deploy no Render
└── README.md
```

### Pastas principais

| Pasta | Descrição |
| --- | --- |
| `accounts/` | Telas e regras de cadastro, login e logout |
| `pets/` | Model, formulário, views e rotas das publicações atuais |
| `pethelp/` | Arquivos de configuração do projeto Django |
| `templates/` | Páginas HTML renderizadas pelo Django |
| `static/` | CSS e JavaScript da interface |
| `media/` | Uploads de imagens dos pets |
| `animais/` | Versão anterior do app, mantida como referência |

## Como Executar

As instruções abaixo consideram o uso no Windows.

### 1. Clonar o repositório

```bash
git clone https://github.com/GirlenioGomesDev/projeto-pethelp.git
cd projeto-pethelp
```

### 2. Criar o ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual

No PowerShell:

```powershell
.\venv\Scripts\activate
```

Se o PowerShell bloquear a execução do script, rode:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\activate
```

No Prompt de Comando:

```cmd
venv\Scripts\activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar as migrações

```bash
python manage.py migrate
```

### 6. Criar um superusuário

```bash
python manage.py createsuperuser
```

Esse usuário permite acessar o painel administrativo em:

```text
http://127.0.0.1:8000/admin/
```

### 7. Iniciar o servidor local

```bash
python manage.py runserver
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:8000/
```

## Requirements

O arquivo `requirements.txt` está organizado com uma dependência por linha:

```text
Django>=5.0,<7.0
Pillow>=10.0
gunicorn>=22.0
whitenoise>=6.6
```

## Prints

Imagens da aplicação serão adicionadas futuramente.

## Objetivos do Projeto

Este projeto foi desenvolvido para fins acadêmicos e também para compor portfólio.

Os principais objetivos foram:

- praticar a estrutura de um projeto Django;
- trabalhar com models, forms, views, urls e templates;
- usar SQLite como banco de dados local;
- implementar autenticação de usuários;
- controlar permissões de edição e exclusão;
- lidar com upload de imagens;
- criar uma aplicação simples com utilidade para a comunidade.

## Variáveis de Ambiente

O projeto funciona localmente sem configuração extra. Para produção, algumas variáveis podem ser configuradas:

| Variável | Uso |
| --- | --- |
| `SECRET_KEY` | Chave secreta do Django |
| `DEBUG` | Define se o modo de debug está ativo |
| `ALLOWED_HOSTS` | Domínios permitidos |
| `CSRF_TRUSTED_ORIGINS` | Origens confiáveis para formulários |
| `SQLITE_PATH` | Caminho opcional para o banco SQLite |
| `MEDIA_ROOT` | Caminho opcional para os uploads |

## Deploy

O repositório possui arquivos usados em deploy:

- `build.sh`
- `render.yaml`
- `gunicorn`
- `whitenoise`

Comandos comuns em produção:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn pethelp.wsgi:application
```

Caso o projeto seja publicado usando SQLite, é importante que o ambiente tenha armazenamento persistente. Sem isso, o banco e os arquivos enviados para `media/` podem ser perdidos em reinicializações.

## Melhorias Futuras

Algumas melhorias que podem ser feitas depois:

- paginação na galeria de pets;
- status da publicação, como ativo, resolvido ou adotado;
- página de contato;
- filtros mais completos;
- testes automatizados;
- melhoria no tratamento de imagens;
- opção para marcar uma publicação como finalizada;
- API para integração futura com aplicativo mobile.

## Autor

Desenvolvido por Girlenio Gomes.

GitHub: [@GirlenioGomesDev](https://github.com/GirlenioGomesDev)
