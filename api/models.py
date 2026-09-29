from django.db import models


# Create your models here.
class Profissional(models.Model):
    nome_social = models.CharField(max_length=150)
    profissao = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    contato = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_social

class Consulta(models.Model):
    data = models.DateTimeField()
    profissional = models.ForeignKey(
        Profissional,
        on_delete=models.CASCADE,
        related_name='consultas'
    )

    def __str__(self):
        return f"Consulta - {self.profissional.nome_social}"

