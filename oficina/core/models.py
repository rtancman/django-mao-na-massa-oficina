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
        return self.nome