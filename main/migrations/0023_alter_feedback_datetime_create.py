# Generated by Django 4.0.4 on 2022-08-05 21:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_feedback_datetime_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='datetime_create',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и время создания'),
        ),
    ]
