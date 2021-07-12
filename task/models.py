from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user_id = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Descrição', blank=False, null=False)
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)

    class Meta:
        ordering = ['-created_at', ]
        verbose_name_plural = 'Tarefas'

    def __int__(self):
        return self.id
 
