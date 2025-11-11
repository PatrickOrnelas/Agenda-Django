# Agenda-Django
Projeto de agenda em Django com lista, busca, paginação, detalhe e criação de contatos. Linguagem e layout em português.

**Visão Geral**
- Aplicação web construída com `Django 5.x` para gerenciar contatos e categorias.
- Listagem paginada, busca por nome/sobrenome/telefone/e-mail e página de detalhes.
- Formulário para criação de contatos.
- Integração com Django Admin.

**Recursos**
- Contatos com: `first_name`, `last_name`, `phone`, `email`, `description`, `created_date`, `show`, `picture` (opcional), `category`, `owner`.
- Paginação de 10 itens por página.
- Busca por múltiplos campos (`q` via GET).
- Detalhe do contato e link direto a partir da lista.
- Admin personalizado com filtros, busca e edição de visibilidade.
- Imagens de contato (quando configuradas) são salvas em `pictures/%Y/%m/` dentro de `MEDIA_ROOT`.

**Estrutura do Projeto**
- `project/` configurações Django, URLs e entrypoints (ASGI/WSGI).
- `contact/` app principal: modelos, views, forms, templates e admin.
- `base_templates/` HTML base, cabeçalho e paginação.
- `base_static/` CSS global.

**Requisitos**
- Python 3.11+ (recomendado).
- Dependências principais: `Django` e `Pillow` (para `ImageField`).

**Instalação e Configuração**
- Crie e ative um ambiente virtual:
  - Windows PowerShell: `python -m venv .venv && .\.venv\Scripts\Activate.ps1`
  - CMD: `python -m venv .venv && .\.venv\Scripts\activate.bat`
- Instale as dependências:
  - `pip install "Django>=5.2" pillow`
- Crie o arquivo `project/local_settings.py` (é ignorado pelo Git):
  - Exemplo mínimo:
    - `from pathlib import Path`
    - `BASE_DIR = Path(__file__).resolve().parent.parent`
    - `MEDIA_ROOT = BASE_DIR / 'media'`
    - `ALLOWED_HOSTS = ['localhost', '127.0.0.1']`
    - Opcional: `DEBUG = True` e um `SECRET_KEY` próprio para desenvolvimento.
- Aplique as migrações:
  - `python manage.py migrate`
- (Opcional) Crie um superusuário para o admin:
  - `python manage.py createsuperuser`
- (Opcional) Coleta de estáticos para produção:
  - `python manage.py collectstatic`

**Executar o Servidor**
- `python manage.py runserver`
- Acesse `http://localhost:8000/`.

**Rotas Principais**
- `/` — Lista paginada de contatos.
- `/search/?q=<termo>` — Busca por nome, sobrenome, telefone ou e-mail.
- `/contact/<id>/detail/` — Página de detalhes do contato.
- `/contact/create/` — Formulário de criação de contato.
- `/admin/` — Django Admin.

**Dados de Exemplo**
- Sem geração automática. Crie contatos manualmente via `/contact/create/` ou pelo `/admin/`.

**Desenvolvimento**
- Templates: `base_templates/` (inclui `global/base.html`, cabeçalho `_header.html` e `pagination.html`).
- CSS: `base_static/global/css/style.css`.
- Idioma e fuso configurados: `LANGUAGE_CODE = 'pt-br'`, `TIME_ZONE = 'America/Sao_Paulo'`.

**Observações e Limitações**
- Upload de imagem: a view de criação atualmente instancia o formulário como `ContactsForm(request.POST)`.
  - Para aceitar arquivo de imagem, ajuste para `ContactsForm(request.POST, request.FILES)` e mantenha `enctype="multipart/form-data"` no template.
- `MEDIA_ROOT` precisa ser definido (ex.: via `project/local_settings.py`) para que uploads sejam armazenados e servidos corretamente.
- Em produção, configure servidor de estáticos e mídia. As regras de `urlpatterns` com `static()` funcionam apenas com `DEBUG=True`.

**Licença**
- Este projeto está licenciado sob a Licença MIT. Consulte `LICENSE`.
