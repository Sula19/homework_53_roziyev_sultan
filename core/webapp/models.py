from django.db import models


class List(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    description = models.CharField(max_length=100, null=False, blank=False, verbose_name="Описание")
    detailed_description = models.TextField(max_length=2500, null=False, blank=False, verbose_name="Подробное описание")
    status = models.CharField(max_length=100, null=False, blank=False, verbose_name="Статус")
    date = models.DateField(default="", verbose_name="Дата")

    def __str__(self):
        return f"{self.description} {self.status}"
