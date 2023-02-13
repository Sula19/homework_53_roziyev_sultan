from django.db import models


class List(models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=100, null=False, blank=False, default="New", verbose_name="Статус")
    date = models.CharField(max_length=50, default="", verbose_name="Дата")

    def __str__(self):
        return f"{self.description} {self.status}"
