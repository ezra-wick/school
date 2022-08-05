# Generated by Django 4.0.4 on 2022-08-05 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_botusers_feedback_complete_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='datetime_complete',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='user_last_change',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.botusers'),
        ),
    ]