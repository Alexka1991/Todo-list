# -*- coding: utf-8 -*
from django.db import models


class Todo(models.Model):
    title = models.CharField(verbose_name=u'Задача', max_length=256)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)