# Generated by Django 3.0.8 on 2022-06-16 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_block_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'ordering': ('position',), 'verbose_name': 'Блок', 'verbose_name_plural': 'Блоки'},
        ),
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.CharField(blank=True, max_length=80, null=True, unique=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='block',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='blockimage',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
