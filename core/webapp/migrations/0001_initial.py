# Generated by Django 4.1.6 on 2023-02-23 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='No Title', max_length=50, verbose_name='Заголовок')),
                ('description', models.CharField(default='No description', max_length=100, verbose_name='Описание')),
                ('detailed_description', models.TextField(default='Not detail description', max_length=2500, verbose_name='Подробное описание')),
                ('status', models.CharField(default='New', max_length=100, verbose_name='Статус')),
                ('date', models.DateField(default='', verbose_name='Дата')),
            ],
        ),
    ]
