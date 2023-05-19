from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Carro(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    placa = models.CharField(max_length=200)
    montadora = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nome} - {self.usuario.username}"

class OrdemServico(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    descricao = models.TextField()
    valor = models.CharField(max_length=200)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"OS: {self.carro.id} - {self.carro.nome} - {self.carro.usuario.username}"