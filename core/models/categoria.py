from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="descrição", help_text="Prateleira do livro")

    def __str__(self):
        return f"({self.id}) {self.descricao}"
