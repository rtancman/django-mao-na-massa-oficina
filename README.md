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

Para isto vamos precisar abrir o arquivo `core/core/settings.py` e alterar o `LANGUAGE_CODE` para 'pt-br' conforme abaixo:

```python

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

```

Agora ao acessar a URL http://127.0.0.1:8000/ o conteduto deve estar em PT-BR.


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

### Melhorando a nossa primeira página para carregar templates html

Para isto vamos precisar criar um diretório templates em nossa app `core`.

```bash
mkdir -p core/templates
```