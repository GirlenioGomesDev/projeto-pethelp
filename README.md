<div align="center">

# PetHelp

### Plataforma comunitária para pets perdidos, encontrados e adoção responsável

O **PetHelp** é uma aplicação web desenvolvida com **Python, Django e SQLite**, criada para aproximar pessoas que perderam seus animais, divulgar pets encontrados e apoiar adoções responsáveis.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5%2B-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Markup-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Modern%20UI-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-N%C3%A3o%20utilizado-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![License](https://img.shields.io/badge/License-N%C3%A3o%20definida-lightgrey?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-2EA44F?style=for-the-badge)

</div>

---

## Sobre o Projeto

Quem já perdeu um pet sabe que os primeiros minutos parecem longos demais. A família procura nas ruas, compartilha fotos em grupos, pergunta aos vizinhos e tenta organizar informações que, muitas vezes, ficam espalhadas.

O **PetHelp** nasceu dessa necessidade: transformar a busca por animais perdidos em um processo mais claro, acessível e colaborativo. A plataforma permite que qualquer visitante consulte publicações, filtre por bairro ou categoria e encontre rapidamente dados importantes, como foto, características e telefone de contato.

Além de ajudar em reencontros, o sistema também abre espaço para pets encontrados e animais disponíveis para adoção responsável. A proposta é simples, mas poderosa: usar tecnologia para fortalecer redes locais de cuidado, aproximar pessoas e dar mais chances a animais que precisam de ajuda.

Este projeto foi desenvolvido com foco em organização, usabilidade e propósito social. Ele une backend em Django, banco SQLite, autenticação de usuários, upload de imagens e uma interface responsiva com identidade visual acolhedora.

---

## Demonstração do Sistema

> Espaço reservado para imagens do projeto. Adicione os arquivos em uma pasta como `docs/screenshots/` e atualize os caminhos abaixo.

| Home | Galeria de Pets | Detalhes do Pet |
| --- | --- | --- |
| `docs/screenshots/home.png` | `docs/screenshots/galeria.png` | `docs/screenshots/detalhe.png` |

| Login/Cadastro | Formulário de Pet | Área Minhas Publicações |
| --- | --- | --- |
| `docs/screenshots/login.png` | `docs/screenshots/formulario.png` | `docs/screenshots/minhas-publicacoes.png` |

Exemplo para inserir uma imagem real:

```md
![Home do PetHelp](docs/screenshots/home.png)
```

---

## Funcionalidades

- **Cadastro de usuários** com nome, e-mail e senha.
- **Login, logout e controle de sessão** usando autenticação nativa do Django.
- **Publicação de pets perdidos** com foto, bairro, data do desaparecimento, características e telefone.
- **Publicação de pets encontrados** para facilitar o reconhecimento por famílias e tutores.
- **Sistema de adoção** para divulgar pets que precisam de um novo lar.
- **Upload de imagens** com armazenamento em `media/` e preview no formulário.
- **Galeria de pets** em cards modernos, com visual de vitrine.
- **Página “Ver Mais”** com todas as informações do pet e imagem em destaque.
- **Filtros de busca** por nome, bairro e categoria.
- **Área “Minhas Publicações”** para usuários autenticados.
- **Edição e exclusão de posts** pelo dono da publicação.
- **Controle de permissões**: apenas o autor ou um admin/staff pode editar ou excluir.
- **Painel administrativo do Django** para gerenciar usuários, pets e moderação.
- **Mensagens de sucesso e erro** para melhorar a experiência do usuário.
- **Layout responsivo** para desktop, tablet e celular.
- **Design humanizado** com paleta azul clara, branco, tons suaves e elementos visuais relacionados a pets.

---

## Tecnologias Utilizadas

| Tecnologia | Uso no projeto |
| --- | --- |
| **Python** | Linguagem principal da aplicação |
| **Django** | Framework backend, rotas, views, templates, autenticação e admin |
| **SQLite** | Banco de dados principal do projeto |
| **HTML5** | Estrutura das páginas |
| **CSS3** | Interface responsiva, animações, cards e identidade visual |
| **JavaScript** | Preview de imagem e pequenos comportamentos da interface |
| **Pillow** | Suporte ao upload e manipulação de imagens no Django |
| **WhiteNoise** | Entrega de arquivos estáticos em produção |
| **Gunicorn** | Servidor WSGI para deploy |
| **Bootstrap** | Não está sendo usado atualmente; o layout foi criado com CSS próprio |

---

## Estrutura do Projeto

```text
PetHelp/
├── accounts/              # Cadastro, login, logout e formulários de usuário
├── animais/               # App legado preservado no repositório
├── media/                 # Uploads enviados pelos usuários
├── pethelp/               # Configurações principais do projeto Django
├── pets/                  # App principal: model Pet, views, forms, urls e admin
├── static/                # Arquivos CSS e JavaScript
├── staticfiles/           # Arquivos estáticos coletados para produção
├── templates/             # Templates HTML globais e por app
├── db.sqlite3             # Banco SQLite local
├── manage.py              # Utilitário de gerenciamento do Django
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
```

### Pastas principais

| Pasta/arquivo | Descrição |
| --- | --- |
| `pethelp/` | Contém `settings.py`, `urls.py`, `wsgi.py` e `asgi.py` |
| `accounts/` | Responsável por cadastro de usuário, login e logout |
| `pets/` | App principal do sistema, com cadastro, galeria, detalhes e permissões |
| `animais/` | Estrutura anterior do projeto, mantida como legado |
| `templates/` | Páginas HTML usadas pelo Django |
| `static/` | CSS e JavaScript da interface |
| `media/` | Fotos enviadas no cadastro dos pets |
| `db.sqlite3` | Banco de dados SQLite usado em ambiente local |

---

## Como Rodar o Projeto no Windows

### 1. Clone o repositório

```bash
git clone https://github.com/GirlenioGomesDev/projeto-pethelp.git
cd projeto-pethelp
```

### 2. Crie o ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

```bash
.\venv\Scripts\activate
```

Se estiver usando PowerShell e aparecer bloqueio de execução de scripts, rode:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute as migrations

```bash
python manage.py migrate
```

### 6. Crie um usuário administrador

```bash
python manage.py createsuperuser
```

### 7. Inicie o servidor local

```bash
python manage.py runserver
```

Abra no navegador:

```text
http://127.0.0.1:8000/
```

Painel administrativo:

```text
http://127.0.0.1:8000/admin/
```

---

## Fluxo de Uso

1. O visitante acessa a home e navega pelas categorias.
2. Ele pode visualizar pets perdidos, encontrados e disponíveis para adoção.
3. Para cadastrar um pet, é necessário criar uma conta ou fazer login.
4. Após o login, o usuário publica um pet com foto e informações de contato.
5. O autor pode editar ou excluir a própria publicação.
6. Admins podem moderar todos os registros pelo site ou pelo Django Admin.

---

## Variáveis de Ambiente

O projeto funciona localmente sem criar um arquivo `.env`, mas em produção é recomendado configurar:

| Variável | Descrição |
| --- | --- |
| `SECRET_KEY` | Chave secreta do Django |
| `DEBUG` | Use `False` em produção |
| `ALLOWED_HOSTS` | Domínios autorizados, separados por vírgula |
| `CSRF_TRUSTED_ORIGINS` | Origens HTTPS confiáveis |
| `SQLITE_PATH` | Caminho opcional para o banco SQLite |
| `MEDIA_ROOT` | Caminho opcional para uploads |

---

## Deploy

O projeto está preparado para deploy com:

- `gunicorn`
- `whitenoise`
- `collectstatic`
- SQLite

Comandos comuns em produção:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --no-input
gunicorn pethelp.wsgi:application
```

> Importante: se usar SQLite em produção, escolha uma hospedagem com disco persistente para não perder o banco `db.sqlite3` nem os arquivos enviados em `media/`.

---

## Administração

O Django Admin permite:

- Gerenciar usuários.
- Gerenciar pets cadastrados.
- Excluir publicações.
- Moderar conteúdo.
- Acompanhar registros pelo painel administrativo.

Para acessar:

```text
/admin/
```

---

## Status do Projeto

O PetHelp está em desenvolvimento, com as principais funcionalidades já implementadas:

- Autenticação
- Cadastro de pets
- Galeria
- Filtros
- Upload de imagem
- Permissões
- Painel administrativo
- Layout responsivo

Melhorias futuras possíveis:

- Paginação na galeria.
- Sistema de status para marcar pets como resolvidos.
- Notificações por e-mail.
- Geolocalização por mapa.
- Página pública de contato.
- Testes automatizados.

---

## Propósito

Mais do que um CRUD, o PetHelp é um projeto sobre cuidado comunitário. A tecnologia aqui funciona como ponte: entre quem procura, quem encontrou, quem pode adotar e quem deseja ajudar.

Cada publicação pode representar um reencontro, uma adoção responsável ou uma nova chance para um animal que precisa de segurança.

---

## Autor

Desenvolvido por **Girlenio Gomes**.

GitHub: [@GirlenioGomesDev](https://github.com/GirlenioGomesDev)

---

## Licença

Este projeto ainda não possui uma licença formal definida. Antes de reutilizar em produção ou distribuir, recomenda-se adicionar um arquivo `LICENSE` ao repositório.
