# Django mão na massa: Como fazer um serviço para oficina do meu cunhado

Vamos fazer um mão na massa passando pela instalação, CRUD e customização do django admin. Para isto vamos construir uma aplicação que gerencia ordem de serviço de uma oficina.

## Inciando o projeto

### Crie o diretórito do projeto

```bash
mkdir django-mao-na-massa-oficina
cd django-mao-na-massa-oficina
```

### Crie um virtualenv com Python

```bash
python -m venv .venv
source .venv/bin/activate
```
**OBS:** recomendamos utilizar a versão mais recente até essa postagem que é a 3.11.3

### Instale as dependências

```bash
pip install Django~=4.2.1
```

### Iniciar o nosso projeto django

```bash
django-admin startproject oficina
```

Após este comando vamos ter a seguinte estrutura de pastas

```bash

tree

.
├── README.md
└── oficina
    ├── oficina
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py
```

### Rode o django

```bash

cd oficina

python manage.py runserver
```

Agora basta acessar a URL http://127.0.0.1:8000/ :rocket:.

### Configure o Django para PT-BR

Para isto vamos precisar abrir o arquivo `core/core/settings.py` e alterar:

```python
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'
```

Agora ao acessar a URL http://127.0.0.1:8000/ o conteduto deve estar em PT-BR.

### Configure a base de dados

Rodando as migrações das apps base do django para o admin:

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

Rode o django novamente.

```bash
python manage.py runserver
```

Basta acessar a URL http://127.0.0.1:8000/admin e realizar o login para conhecer o admin do django s2.

## Sistema de ordem de serviço para oficina do meu cunhado

### Crie nossa app django

```bash
python manage.py startapp core
```

Após este comando vamos ter a seguinte estrutura de pastas

```bash
tree

.
├── core
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── oficina
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-311.pyc
    │   └── settings.cpython-311.pyc
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

```

### Nossa primeira página

Vamos alterar a página principal do django para a nossa primeira página da oficina alterando o arquivo `oficina/core/views.py` com o conteúdo abaixo:

```python
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Oficina Mão na massa!")
```

Agora precisamos configurar as urls da nossa oficina. Para isto crie o arquivo `oficina/core/urls.py` e coloque o conteúdo abaixo:

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

Tendo o nosso arquivo de rotas criados, vamos adicionar essas URLs ao nosso site da Oficina alterando o arquivo `oficina/oficina/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("core.urls")),
    path('admin/', admin.site.urls),
]
```

Rode o django novamente para aplicar as modificações:

```bash
python manage.py runserver
```

### Adicione templates

Para isto vamos precisar criar um diretório templates em nossa app `core`.

```bash
mkdir -p core/templates
```

Agora crie 3 arquivos:

1. core/templates/index.html

```html
<!DOCTYPE html>
<html>
    <head>
        <title>{% block title %}{% endblock %}</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" />
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body class="container">
        <header>
            <nav class="navbar navbar-expand-lg bg-body-tertiary">
                <div class="container-fluid">
                    <a class="navbar-brand" href="/">Oficina Mão na massa!</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div class="navbar-nav">
                        <a class="nav-link" aria-current="page" href="/">Home</a>
                        <a class="nav-link" href="/login">Login</a>
                    </div>
                    </div>
                </div>
            </nav>
        </header>
        {% block content %}
        {% endblock %}
        <footer>
            <div class="row mb-3">
                <p class="text-center">Sistema para gerenciar oficina de veículos.</p>
            </div>
        </footer>
    </body>
</html>
```

2. core/templates/home.html

```html
{% extends 'core/index.html' %}
{% block content %}
<div class="px-4 py-5 my-5 text-center">
    <h1 class="display-5 fw-bold text-body-emphasis">Oficina Mão na massa!</h1>
    <div class="col-lg-6 mx-auto">
      <p class="lead mb-4">Sistema para gerenciamento de ordens de serviço.</p>
      <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
        <a href="/login" class="btn btn-primary btn-lg px-4 gap-3">Faça o seu login</a>
      </div>
    </div>
  </div>
{% endblock content %}
```

3. core/templates/login.html

```html
{% extends 'core/index.html' %}
{% block content %}
<main>
    <form>
        <h1 class="h3 mb-3 fw-normal">Faça seu login</h1>
        <div class="mb-3">
            <label>Login</label>
            <input type="email" class="form-control" placeholder="name@example.com">
        </div>
        <div class="mb-3">
            <label>Senha</label>
            <input type="password" class="form-control" placeholder="digite a sua senha...">
        </div>
        <button class="w-100 btn btn-lg btn-primary" type="submit">Enviar</button>
    </form>
</main>
{% endblock content %}
```


Adicione a nossa app `core` na lista de apps instaladas no `oficina/oficina/settings.py`.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]
```

Para concluir essa etapa vamos carregar as novas templates:

1. Modifique o `oficina/core/views.py`

```python
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'core/home.html', {})


def login(request):
    return render(request, 'core/login.html', {})
```

2. Adicione a nova url de login no `oficina/core/urls.py`:

```python
path("login", views.login, name="index"),
```

Rode o django novamente para aplicar as modificações:

```bash
python manage.py runserver
```


### Crie Modelos

Vamos criar os modelos que vão compor o nosso sistema atual, são eles:

- Usuário
- Carro
- Ordem de serviço

**OBS:** Vamos utilizar o usuário do django.

### Crie o modelo Carro

Nosso carro terá os seguintes atributos:

- nome
- placa
- montadora
- data de criação
- usuario

Altere o arquivo oficina/core/models.py

```python
from django.conf import settings
from django.db import models
from django.utils import timezone


class Carro(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    placa = models.CharField(max_length=200)
    montadora = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nome} - {self.usuario.username}"
```

Criando a tabela para o nosso modelo Carro:

```bash
python manage.py makemigrations core
python manage.py migrate core
```

Adicionando o nosso modelo para ser acessado via admin do django:

Modifique o arquivo `oficina/core/admin.py`.

```python
from django.contrib import admin
from .models import Carro


admin.site.register(Carro)
```

Rode o django novamente para aplicar as modificações:

```bash
python manage.py runserver
```

Vamos ver o admin do django com o nosso novo modelo acessando http://127.0.0.1:8000/admin


### Crie o modelo Ordem de Serviço

Nosso modelo "Ordem Serviço" terá os seguintes atributos:

- carro
- descrição do serviço
- valor total
- data de criação

Altere o arquivo oficina/core/models.py

```python
from django.conf import settings
from django.db import models
from django.utils import timezone


class OrdemServico(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    valor = models.CharField(max_length=200)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"OS: {self.carro.id} - {self.carro.nome} - {self.carro.usuario.username}"
```

Criando a tabela para o nosso modelo OrdemServico:

```bash
python manage.py makemigrations core
python manage.py migrate core
```

Adicionando o nosso modelo para ser acessado via admin do django:

Modifique o arquivo `oficina/core/admin.py`.

```python
from django.contrib import admin
from .models import Carro, OrdemServico


admin.site.register(Carro)
admin.site.register(OrdemServico)
```

Rode o django novamente para aplicar as modificações:

```bash
python manage.py runserver
```

Vamos ver o admin do django com o nosso novo modelo acessando http://127.0.0.1:8000/admin

### Crie a função de login e logout

Agora vamos adicionar as funcionalidades de login e logout. 

1. Modifique o arquivo `oficina/core/views.py`:

Adicionando imports:
```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
```

Modifique função de login:
```python
def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()

    return render(request, 'core/login.html', {'form_login': form_login})
```

Adicione função de logout:
```python
def logout(request):
    auth_logout(request)
    return redirect('/')
```

2. Modifique os arquivo de templates:

Template de login `oficina/core/templates/core/login.html`
```html
{% extends 'core/index.html' %}
{% block content %}
<main>
    <form method="post">
        {% csrf_token %}
        <h1 class="h3 mb-3 fw-normal">Faça seu login</h1>
        <div class="mb-3">
            {{form_login.username.errors}}
            <label>Login</label>
            {{form_login.username}}
        </div>
        <div class="mb-3">
            {{form_login.password.errors}}
            <label>Senha</label>
            {{form_login.password}}
        </div>
        <button class="w-100 btn btn-lg btn-primary" type="submit">Enviar</button>
    </form>
</main>
{% endblock content %}
```

Template de home `oficina/core/templates/core/home.html` vamos modificar somente a mensagem na tela principal quando o usuário estiver logado:
```html
{% if user.is_authenticated %}
  <p>Olá <strong>{{ user.get_username }}.</strong></p>
{% else %}
  <a href="/entrar" class="btn btn-primary btn-lg px-4 gap-3">Faça o seu login</a>
{% endif %}
```

Template de index `oficina/core/templates/core/index.html` aqui vamos alterar somente os links da navegação  quando o usuário estiver logado:
```html
{% if user.is_authenticated %}
    <a class="nav-link" href="/sair">Sair</a>
{% else %}
    <a class="nav-link" href="/entrar">Entrar</a>
{% endif %}
```


3. Adicione as novas urls no arquivo `oficina/core/urls.py`:

```python
path("entrar", views.login, name="login"),
path("sair", views.logout, name="logout"),
```

Rode o django novamente e veja as modificações:

```bash
python manage.py runserver
```

### Crie a função para ordem de serviço

Vamos exibir para um usuário logado todas as ordens de serviço dele.

1. Modifique o arquivo `oficina/core/views.py`:

Importe o modelo OrdemServico:
```python
from .models import OrdemServico
```

Adicione função de ordem_servico:
```python
def orderm_servico(request):
    if not request.user.is_authenticated:
        return redirect('/entrar')

    ordens_servico = OrdemServico.objects.filter(carro__usuario=request.user).order_by('data_criacao')
    return render(request, 'core/ordem_servico.html', {'ordens_servico': ordens_servico})
```

2. Modifique os arquivo de templates:

Adicione a template oficina/core/templates/core/ordem_servico.html
```html
{% extends 'core/index.html' %}
{% block content %}
<div class="px-4 py-5 my-5 text-center">
    <h1 class="display-5 fw-bold text-body-emphasis">Ordem de Serviço</h1>
    <div class="col-lg-6 mx-auto">
      <p class="lead mb-4">Veja as suas ordens de serviço abaixo:</p>
      {% if ordens_servico %}
        <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
          <table class="table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Carro</th>
                <th scope="col">Descrição</th>
                <th scope="col">Valor</th>
                <th scope="col">data do serviço</th>
              </tr>
            </thead>
            <tbody>
              {% for ordem_servico in ordens_servico %}
              <tr>
                <th scope="row">{{ ordem_servico.id }}</th>
                <td>{{ ordem_servico.carro.nome }}</td>
                <td>{{ ordem_servico.descricao }}</td>
                <td>{{ ordem_servico.valor }}</td>
                <td>{{ ordem_servico.data_criacao }}</td>
              </tr>
              {% endfor %}
            </tbody>
          </table>
        </div>
      {% else %}
        <div class="alert alert-warning d-flex align-items-center" role="alert">
          <div>
            Não existe nenhuma ordem de serviço para este usuário.
          </div>
        </div>
      {% endif %}
    </div>
  </div>
{% endblock content %}
```

3. Adicione a nova url no arquivo `oficina/core/urls.py`:

```python
path("ordem-servico", views.orderm_servico, name="orderm_servico"),
```

Rode o django novamente para aplicar as modificações:

```bash
python manage.py runserver
```
