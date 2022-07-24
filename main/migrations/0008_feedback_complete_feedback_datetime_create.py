# Generated by Django 4.0.4 on 2022-07-19 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_feedback_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='complete',
            field=models.BooleanField(default=False, verbose_name='Отметка о выполнении'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='datetime_create',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время создания'),
        ),
    ]
