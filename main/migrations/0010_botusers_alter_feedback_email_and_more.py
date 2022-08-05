# Generated by Django 4.0.4 on 2022-08-05 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_feedback_datetime_create'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Имя пользователя')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия')),
                ('userid', models.IntegerField(unique=True, verbose_name='user_id')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Адресаты рассылки',
            },
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.CharField(blank=True, max_length=80, null=True, unique=True, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user_last_change',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.botusers'),
        ),
    ]