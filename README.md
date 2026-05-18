# PetHelp

PetHelp é uma aplicação web comunitária feita com Django e SQLite para ajudar famílias a reencontrarem pets perdidos, divulgar animais encontrados e incentivar adoção responsável.

## Funcionalidades

- Home responsiva com hero em tela cheia, missão, vitrine de pets e identidade visual azul/branco.
- Cadastro, login, logout e controle de sessão com autenticação nativa do Django.
- Usuários comuns podem cadastrar, editar e excluir apenas as próprias publicações.
- Usuários admin/staff podem moderar qualquer publicação pelo site e pelo Django Admin.
- Cadastro completo de pet com categoria, foto, raça, idade, porte, bairro, cidade, data, características, telefone e descrição.
- Upload de imagem em `media/` com preview no formulário.
- Galeria com cards modernos, página exclusiva de detalhes e filtros por nome, bairro e categoria.
- Mensagens de sucesso/erro, validações de formulário, animações suaves e layout responsivo.

## Estrutura

```text
accounts/        cadastro, login e logout
pets/            model Pet, forms, views, rotas e admin
pethelp/         settings, urls, wsgi/asgi
templates/       templates globais, accounts e pets
static/          CSS e JavaScript
media/           uploads locais
db.sqlite3       banco SQLite local
```

## Instalação

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000/
```

## Variáveis Úteis

- `SECRET_KEY`: chave secreta do Django em produção.
- `DEBUG`: use `False` em produção.
- `ALLOWED_HOSTS`: domínios liberados, separados por vírgula.
- `CSRF_TRUSTED_ORIGINS`: origens HTTPS confiáveis, separadas por vírgula.
- `SQLITE_PATH`: caminho opcional para o arquivo SQLite.
- `MEDIA_ROOT`: caminho opcional para uploads.

## Deploy

O projeto está preparado para deploy com `gunicorn`, `whitenoise` e `collectstatic`. Em produção, prefira um provedor com disco persistente para manter `db.sqlite3` e os uploads em `media/`.

Passos gerais:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --no-input
gunicorn pethelp.wsgi:application
```

Configure `DEBUG=False`, `SECRET_KEY`, `ALLOWED_HOSTS` e `CSRF_TRUSTED_ORIGINS` no ambiente do servidor.

## Admin

Crie um superusuário:

```bash
python manage.py createsuperuser
```

Depois acesse `/admin/` para gerenciar usuários, pets, excluir publicações e moderar conteúdo.
