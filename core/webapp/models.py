from django.db import models


class List(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок", default="No Title")
    description = models.CharField(max_length=100, null=False, blank=False, verbose_name="Описание", default="No description")
    detailed_description = models.TextField(max_length=2500, null=False, blank=False, verbose_name="Подробное описание", default="Not detail description")
    status = models.CharField(max_length=100, null=False, blank=False, default="New", verbose_name="Статус")
    date = models.DateField(default="", verbose_name="Дата")

    def __str__(self):
        return f"{self.description} {self.status}"
