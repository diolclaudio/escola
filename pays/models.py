from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Pagar(models.Model):
    nome = models.CharField('Nome do aluno', max_length=20)
    classe = models.CharField('Classe e Turma', max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=5)
    mes = models.CharField('mês', choices=[('Janeiro', 'Janeiro'), ('Fevereiro', 'Fevereiro'),
                                           ('Março', 'Março'), ('Abril', 'Abril'), ('Maio', 'Maio'), ('Junho', 'Junho'), ('Julho', 'Julho'), ('Agosto', 'Agosto'), ('Setembro', 'Setembro'), ('Outubro', 'Outubro'), ('Novembro', 'Novembro'), ('Desembro', 'Desembro')], max_length=20)
    email = models.EmailField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete = models.DO_NOTHING)
    def __str__(self):
        return self.nome

class Inscricoes(models.Model):
    nome = models.CharField('Nome completo', max_length=20)
    curso = models.CharField(max_length=23, choices=[('Curso de informática', 'Curso de informática'), ('Curso de medicina geral', 'Curso de medicina geral'), ('Curso de electrónica', 'Curso de electrónica'), ('Curso de artes', 'Curso de artes')])
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    numero = models.DecimalField('Número de celular', max_digits=9, decimal_places=0)
    email = models.EmailField(max_length=50)
    def __str__(self):
        return self.nome

class Comentario(models.Model):
    opiniao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.opiniao