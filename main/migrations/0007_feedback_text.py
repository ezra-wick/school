# Generated by Django 4.0.4 on 2022-06-22 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_block_id_alter_blockimage_id_alter_feedback_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='text',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Сообщение'),
        ),
    ]
