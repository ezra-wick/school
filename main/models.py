from django.db import models
from django.utils.dateformat import *
import re

# Create your models here.
class Block(models.Model):

    position = models.IntegerField(
        verbose_name='Позиция',
        null=True,
        blank=True
        )

    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Раздел",
        )

    text = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name="Текст",
        )
    
    tag = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name="Тег",
        )

    class Meta:
        ordering = ('position', )
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'

    def __str__(self):
        return self.title



class BlockImage(models.Model):
    block = models.ForeignKey(
        Block,
        on_delete=models.SET_NULL,
        related_name='block_image',
        verbose_name='Блок',
        null=True,
        blank=True
    )

    image = models.ImageField(upload_to='images/', null=True, blank=True)

    tag = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Тег",
        )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.block.title


class FeedBack(models.Model):
    phone = models.CharField(max_length=16, verbose_name="Телефон", null=True, blank=True, unique=True)
    name = models.CharField(max_length=50, verbose_name="Имя", null=True, blank=True, unique=True)
    email = models.CharField(max_length=80, verbose_name="Имя", null=True, blank=True, unique=True)
    text = models.CharField(max_length=500, verbose_name="Сообщение", null=True, blank=True)
    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    complete = models.BooleanField(default=False, verbose_name="Отметка о выполнении")

    def save_phone(self, phone):
        phone = re.sub(r'\+?[78](\d{3})(\d{3})(\d\d)(\d\d)', r'+7\1\2\3\4', phone)
        if phone[0] == '9' and len(phone) == 10:
            phone = '+7' + phone

        self.phone = re.sub(r'\+?[78](\d{3})(\d{3})(\d\d)(\d\d)', r'+7\1\2\3\4', phone)
        self.username = re.sub(r'\+?[78](\d{3})(\d{3})(\d\d)(\d\d)', r'+7\1\2\3\4', phone)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.name + " Дата и время создания: %s"  % (format(self.datetime_create, "d.m.Y H:i"))
