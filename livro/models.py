from django.db import models

class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, blank = True)
    data_publicacao = models.DateField()

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome
    