# Generated by Django 4.0.4 on 2022-05-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_blockimage_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='tag',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Тег'),
        ),
    ]
