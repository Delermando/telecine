from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nome
