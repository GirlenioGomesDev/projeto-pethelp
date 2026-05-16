# PetHelp

Aplicacao web comunitaria feita com Django e SQLite para ajudar pessoas a encontrar pets perdidos, divulgar animais encontrados e facilitar adocoes responsaveis.

## Tecnologias

- Python
- Django
- SQLite
- Templates Django
- HTML, CSS e JavaScript
- Upload de imagens com Django
- Autenticacao nativa do Django

## Funcionalidades

- Pagina inicial moderna com hero, estatisticas animadas e pets recentes.
- Cadastro, login e logout de usuarios.
- Publicacoes por categoria: pets perdidos, patinhas encontradas e adocao.
- Upload de foto do pet.
- Pesquisa por nome, tipo, bairro, caracteristicas e descricao.
- Filtros por categoria e status.
- Pagina de detalhes.
- Minhas Publicacoes para usuarios logados.
- Editar, apagar e marcar publicacao como resolvida.
- Permissoes por dono da publicacao ou admin.
- Interface responsiva com cards, badges e animacoes suaves.

## Como Rodar

```bash
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abra no navegador:

```text
http://127.0.0.1:8000/
```

## Banco De Dados

O projeto usa SQLite. O arquivo `db.sqlite3` fica fora do Git por ser dado local de desenvolvimento. Para recriar o banco, rode:

```bash
python manage.py migrate
```

## Uploads

As imagens enviadas pelos usuarios ficam em `media/`, que tambem fica fora do Git. A pasta e mantida no repositorio com `media/.gitkeep`.

## Deploy No PythonAnywhere Com SQLite

O PythonAnywhere e a opcao recomendada para hospedar este projeto no plano free mantendo SQLite.

No console Bash do PythonAnywhere:

```bash
git clone https://github.com/GirlenioGomesDev/projeto-pethelp.git
cd projeto-pethelp
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --no-input
```

No painel Web do PythonAnywhere, crie um app Django e configure:

- Source code: `/home/seuusuario/projeto-pethelp`
- Working directory: `/home/seuusuario/projeto-pethelp`
- Static URL: `/static/`
- Static directory: `/home/seuusuario/projeto-pethelp/staticfiles`
- Media URL: `/media/`
- Media directory: `/home/seuusuario/projeto-pethelp/media`

No arquivo WSGI do PythonAnywhere, aponte para:

```python
from pethelp.wsgi import application
```

Se quiser fixar as variaveis no WSGI, use:

```python
import os

os.environ['DEBUG'] = 'False'
os.environ['ALLOWED_HOSTS'] = 'seuusuario.pythonanywhere.com'
os.environ['CSRF_TRUSTED_ORIGINS'] = 'https://seuusuario.pythonanywhere.com'
```

## Deploy No Render

O projeto inclui `render.yaml` para criar um Web Service Python no plano free do Render, ligado a um Postgres free.

Configuracoes principais:

- Build Command: `bash build.sh`
- Pre-Deploy Command: `python manage.py migrate`
- Start Command: `gunicorn pethelp.wsgi:application`
- Python: `3.12.10`
- Static files: WhiteNoise + `collectstatic`
- Banco: `DATABASE_URL` vindo do Postgres `pethelp-db`

No plano free, o Render nao permite disco persistente em Web Services. Por isso, o banco usa Postgres free em vez de SQLite. Uploads em `media/` continuam em disco local temporario e podem ser perdidos quando o servico reiniciar, redeployar ou sair do ar por inatividade. Para uploads permanentes no free, use um storage externo, como Cloudinary ou S3 compativel.
