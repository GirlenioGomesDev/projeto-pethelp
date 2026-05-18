<div align="center">

# PetHelp

### Tecnologia para aproximar famílias, comunidades e pets que precisam de ajuda.

O **PetHelp** é uma aplicação web construída com **Python, Django e SQLite** para centralizar publicações de pets perdidos, animais encontrados e adoções responsáveis em uma experiência simples, acolhedora e funcional.

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5%2B-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-Ready-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-2EA44F?style=for-the-badge)
![Deploy](https://img.shields.io/badge/Deploy-Ready-blue?style=for-the-badge&logo=render&logoColor=white)

<br>

```text
🐾 PetHelp
Um espaço digital para reencontros, cuidado comunitário e adoção responsável.
```

</div>

---

## Introdução

Perder um pet não é apenas perder um animal de estimação. Para muitas famílias, é perder uma parte da rotina, da casa e da memória afetiva construída todos os dias. A busca costuma acontecer de forma espalhada: mensagens em grupos, cartazes improvisados, postagens soltas em redes sociais e informações difíceis de acompanhar.

O **PetHelp** nasce para organizar essa ajuda.

A proposta é oferecer um ambiente onde pessoas possam publicar pets perdidos, divulgar animais encontrados e dar visibilidade a pets disponíveis para adoção. Em vez de depender apenas de mensagens perdidas no meio de conversas, a comunidade passa a ter um ponto central para consultar fotos, bairros, características e telefones de contato.

Este projeto une tecnologia e propósito social. A aplicação foi pensada para ser acessível, direta e humana, porque em situações de busca ou adoção, cada detalhe importa: uma foto clara, uma descrição bem feita, um bairro informado corretamente e um contato disponível podem fazer diferença real.

---

## Demonstração Visual

> Espaço preparado para screenshots, gifs e previews do sistema.  
> Sugestão: crie uma pasta `docs/screenshots/` e adicione as imagens reais da aplicação.

### Preview das Telas

| Home | Galeria de Pets | Detalhes do Pet |
| --- | --- | --- |
| ![Home](docs/screenshots/home.png) | ![Galeria](docs/screenshots/galeria.png) | ![Detalhes](docs/screenshots/detalhe.png) |

| Login | Cadastro de Pet | Minhas Publicações |
| --- | --- | --- |
| ![Login](docs/screenshots/login.png) | ![Cadastro de Pet](docs/screenshots/cadastro-pet.png) | ![Minhas Publicações](docs/screenshots/minhas-publicacoes.png) |

### GIF de Navegação

```md
![Demonstração do PetHelp](docs/screenshots/demo.gif)
```

---

## Funcionalidades

### Usuários

- Cadastro de usuários com nome, e-mail e senha.
- Login e logout com controle de sessão.
- Autenticação usando recursos nativos do Django.
- Acesso público para visitantes visualizarem publicações.
- Acesso restrito para usuários logados cadastrarem e gerenciarem pets.

### Publicações

- Cadastro de pets perdidos.
- Cadastro de animais encontrados.
- Divulgação de pets para adoção responsável.
- Upload de imagens dos pets.
- Preview da imagem antes do envio.
- Página individual com detalhes completos de cada publicação.
- Busca por nome.
- Busca por bairro.
- Filtro por categoria.
- Área **Minhas Publicações** para o usuário acompanhar seus registros.
- Edição de publicações próprias.
- Exclusão de publicações próprias.

### Administração

- Painel administrativo nativo do Django.
- Gerenciamento de usuários.
- Gerenciamento de pets cadastrados.
- Moderação de publicações.
- Permissão para administradores editarem ou excluírem qualquer publicação.

### Segurança

- Controle de permissões por usuário.
- Apenas o dono da publicação pode editar ou excluir seu próprio conteúdo.
- Administradores e staff possuem acesso ampliado para moderação.
- Proteção CSRF nos formulários.
- Senhas armazenadas com hash pelo sistema de autenticação do Django.
- Separação entre visitantes, usuários autenticados e administradores.

### Interface

- Layout responsivo para desktop, tablet e celular.
- Interface moderna com identidade visual clara e acolhedora.
- Paleta baseada em azul claro, branco e tons suaves.
- Cards de pets no estilo vitrine.
- Mensagens de sucesso e erro.
- Animações leves e interações com hover.
- Organização visual pensada para uso simples por qualquer pessoa.

---

## Diferenciais do Sistema

- **Propósito social real:** o sistema não é apenas um CRUD; ele resolve um problema emocional e comunitário.
- **Foco em comunidade:** facilita a colaboração entre vizinhos, tutores, protetores e adotantes.
- **Acessibilidade de uso:** visitantes conseguem visualizar publicações sem criar conta.
- **Fluxo simples:** cadastro, busca e contato foram pensados para serem rápidos.
- **Interface acolhedora:** o design evita aparência fria ou genérica.
- **Organização das informações:** centraliza dados essenciais como foto, bairro, cidade, características e telefone.
- **Base preparada para evoluir:** a estrutura permite adicionar mapa, notificações, paginação e status de resolução.

---

## Stack Tecnológica

| Tecnologia | Finalidade |
| --- | --- |
| **Python** | Linguagem principal do backend |
| **Django** | Framework web usado para rotas, views, templates, autenticação e admin |
| **SQLite** | Banco de dados principal em ambiente local |
| **HTML5** | Estrutura semântica das páginas |
| **CSS3** | Layout, responsividade, animações e identidade visual |
| **Bootstrap** | Referência/compatibilidade visual; o layout atual usa CSS próprio |
| **Pillow** | Suporte ao processamento e upload de imagens |
| **Render** | Estrutura preparada para deploy com `render.yaml` |

---

## Estrutura de Pastas

```text
projeto-pethelp/
├── accounts/                 # Autenticação, cadastro de usuários e rotas de conta
├── animais/                  # App legado preservado no repositório
├── media/                    # Uploads de imagens enviados pelos usuários
├── pethelp/                  # Configurações principais do projeto Django
│   ├── settings.py           # Configurações do projeto
│   ├── urls.py               # Rotas globais
│   ├── asgi.py               # Entrada ASGI
│   └── wsgi.py               # Entrada WSGI
├── pets/                     # App principal de publicações de pets
│   ├── admin.py              # Configuração do Django Admin
│   ├── forms.py              # Formulários do sistema
│   ├── models.py             # Model Pet
│   ├── urls.py               # Rotas do app pets
│   └── views.py              # Views e regras de negócio
├── static/                   # CSS e JavaScript
│   ├── css/
│   └── js/
├── staticfiles/              # Arquivos estáticos coletados para produção
├── templates/                # Templates HTML do projeto
│   ├── accounts/
│   ├── animais/
│   ├── pets/
│   └── base.html
├── db.sqlite3                # Banco de dados SQLite local
├── manage.py                 # CLI de gerenciamento do Django
├── requirements.txt          # Dependências Python
├── build.sh                  # Script de build/deploy
├── render.yaml               # Configuração para deploy no Render
└── README.md                 # Documentação do projeto
```

### Principais diretórios

| Caminho | Descrição |
| --- | --- |
| `pethelp/` | Núcleo de configuração do projeto Django |
| `accounts/` | Cadastro, login, logout e formulários de usuário |
| `pets/` | App principal responsável pelas publicações atuais |
| `animais/` | App anterior mantido como referência/legado |
| `templates/` | Páginas HTML renderizadas pelo Django |
| `static/` | Arquivos CSS e JavaScript da interface |
| `media/` | Fotos de pets enviadas pelos usuários |
| `db.sqlite3` | Banco de dados local usado pelo SQLite |
| `manage.py` | Comando central para migrations, servidor, admin e manutenção |

---

## Instalação e Execução

As instruções abaixo foram pensadas para **Windows**.

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

Se estiver usando PowerShell e houver bloqueio de execução de scripts, use:

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

### 6. Inicie o servidor

```bash
python manage.py runserver
```

Acesse no navegador:

```text
http://127.0.0.1:8000/
```

---

## Criando um Administrador

Para acessar o painel administrativo do Django, crie um superusuário:

```bash
python manage.py createsuperuser
```

Depois acesse:

```text
http://127.0.0.1:8000/admin/
```

---

## Fluxo Principal da Aplicação

```text
Visitante
   └── Visualiza publicações
   └── Filtra por nome, bairro ou categoria

Usuário autenticado
   └── Cadastra pet
   └── Edita publicações próprias
   └── Exclui publicações próprias
   └── Acessa "Minhas Publicações"

Administrador
   └── Gerencia usuários
   └── Modera publicações
   └── Edita ou exclui qualquer post
```

---

## Variáveis de Ambiente

O projeto roda localmente sem configuração extra, mas em produção é recomendado definir:

| Variável | Finalidade |
| --- | --- |
| `SECRET_KEY` | Chave secreta do Django |
| `DEBUG` | Deve ser `False` em produção |
| `ALLOWED_HOSTS` | Lista de domínios permitidos |
| `CSRF_TRUSTED_ORIGINS` | Origens confiáveis para CSRF |
| `SQLITE_PATH` | Caminho opcional do banco SQLite |
| `MEDIA_ROOT` | Caminho opcional para arquivos de upload |

---

## Deploy

O projeto contém arquivos para facilitar deploy:

- `build.sh`
- `render.yaml`
- `gunicorn`
- `whitenoise`

Comandos comuns em ambiente de produção:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --no-input
gunicorn pethelp.wsgi:application
```

> Observação: ao usar SQLite em produção, o servidor precisa ter disco persistente. Sem isso, o banco `db.sqlite3` e os arquivos em `media/` podem ser perdidos em reinicializações ou novos deploys.

---

## Qualidade e Organização

O projeto foi estruturado com separação clara entre:

- models;
- forms;
- views;
- urls;
- templates;
- static files;
- uploads;
- autenticação;
- regras de permissão.

Essa organização facilita manutenção, evolução do código e leitura por outros desenvolvedores.

---

## Roadmap

Melhorias futuras que podem elevar ainda mais o projeto:

- Paginação da galeria.
- Status da publicação: ativo, resolvido ou adotado.
- Integração com mapa por bairro/cidade.
- Notificações por e-mail.
- Página de contato.
- Testes automatizados.
- API REST para integração com aplicativo mobile.
- Dashboard administrativo com métricas.

---

## Licença

Este projeto está documentado como **MIT License**.

Recomendação: manter um arquivo `LICENSE` na raiz do repositório com o texto completo da licença MIT.

---

## Autor

Desenvolvido por **Girlenio Gomes**.

GitHub: [@GirlenioGomesDev](https://github.com/GirlenioGomesDev)

---

<div align="center">

**PetHelp**  
Um projeto feito para mostrar que tecnologia também pode cuidar.

</div>
