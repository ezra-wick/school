# Generated by Django 4.0.4 on 2022-08-05 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_feedback_user_last_change_delete_botusers_and_more'),
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
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=16, null=True, unique=True, verbose_name='Телефон')),
                ('name', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Имя')),
                ('email', models.CharField(blank=True, max_length=80, null=True, unique=True, verbose_name='email')),
                ('text', models.CharField(blank=True, max_length=500, null=True, verbose_name='Сообщение')),
                ('datetime_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('complete', models.BooleanField(default=False, verbose_name='Отметка о выполнении')),
                ('datetime_complete', models.DateTimeField(blank=True, default=None, verbose_name='Дата и время отработки заявки')),
                ('user_last_change', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.botusers')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
