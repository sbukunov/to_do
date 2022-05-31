from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import datetime
from datetime import timedelta

def get_next_day():
    return datetime.datetime.now()+timedelta(days=1)

class Note(models.Model):
    class Status(models.IntegerChoices):
        ACTIVE = 1, "Активно"
        HOLD = 2, "Отложено"
        DONE = 3, "Выполнено"

    title = models.CharField(max_length=255, verbose_name='Тема')
    note = models.TextField(default='', verbose_name='Подробности')
    status = models.IntegerField(default=Status.ACTIVE, choices=Status.choices, verbose_name="Состояние")
    public = models.BooleanField(default=False, verbose_name='Публично')
    important = models.BooleanField(default=False, verbose_name='Важно')
    date_plan = models.DateTimeField(default=get_next_day, verbose_name='Плановая дата')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return f"Дело №{self.id}" #Т.е. можем перегрузить вывод как угодно

    class Meta:
        verbose_name = _("Дело") # Можно и так через gettext_lazzy as _
        verbose_name_plural = "Дела"
        ordering = ['date_plan', 'important']




