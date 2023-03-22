from django.db import models


class Parrot(models.Model):
    name = models.CharField(max_length=63, verbose_name='Имя')
    breed = models.CharField(max_length=63, verbose_name='Порода')
    description = models.TextField(max_length=800,
                                   verbose_name='Описание',
                                   null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, verbose_name='аватарка')
    image = models.ImageField(null=True, blank=True, verbose_name='фотки')
