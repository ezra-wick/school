# Generated by Django 4.0.4 on 2022-07-19 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_feedback_complete_feedback_datetime_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='datetime_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания'),
        ),
    ]