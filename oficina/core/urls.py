from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entrar", views.login, name="login"),
    path("sair", views.logout, name="logout"),
    path("ordem-servico", views.orderm_servico, name="orderm_servico"),
]