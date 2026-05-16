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

## Deploy No Render

O projeto inclui `render.yaml` para criar um Web Service Python no Render.

Configuracoes principais:

- Build Command: `bash build.sh`
- Start Command: `python manage.py migrate && gunicorn pethelp.wsgi:application`
- Python: `3.12.10`
- Static files: WhiteNoise + `collectstatic`
- SQLite: `SQLITE_PATH=/var/data/db.sqlite3`
- Uploads: `MEDIA_ROOT=/var/data/media`

Para manter o SQLite e os uploads entre deploys, use um disco persistente no Render montado em `/var/data`. Sem disco persistente, o banco e as imagens podem ser perdidos quando o servico reiniciar ou redeployar.
