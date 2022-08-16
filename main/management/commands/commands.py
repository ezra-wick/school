from main.models import BotUsers, FeedBack
from aiogram import types
import asyncio
from django.utils.dateformat import *
from django.utils import timezone

import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
load_dotenv()

bot = Bot(token=os.getenv('TOKEN')) # Создаем экземпляр бота
dp = Dispatcher(bot) # Создаём диспетчера для бота

#Поскольку aiogram асинхронный а Django работает с БД синхронно необходимо операции чтения и записи в БД производить
#из синхронной функции.


def add_users(message): #Функция добавления пользователя в БД
    set_new_user, user_add = BotUsers.objects.get_or_create(
#метод get_or_create проверяет БД на наличие записи по уникальному ключу если записи с таким ключём нет, то она создаётся.
#если запись есть, то запись модифицируется. Возвращается объект и логическая переменна в зависимости от того добавлен новый или нет
        userid=message.chat.id,
        defaults={
            "username": message.chat.username,
            "first_name": message.chat.first_name,
            "last_name": message.chat.last_name,
        }
    )
    async_list = []
    async_list.append(set_new_user)
    async_list.append(user_add)
    return async_list


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply(
        "Введите пароль для добавления в список рассылки и управления ботом в формате\n/password :<password>.\nДля получения дополнительной информации используйте команду help")

@dp.message_handler(commands=['help'])
async def send_about(message: types.Message):

    await message.reply("""\n
    Данный бот нужен для обработки обратной связи от пользователей.\n
    Для получения уведомлений и работы с зявками необходимо авторизоваться с помощью команды password.\n
    Для авторизованных пользователей бот поддерживает следующие функции:\n
    /start - Запуск чата,\n
    /help - Информация о боте,\n
    /complete - Получить список всех зарешенных зявок,\n
    /no_complete - Список зявкок которые нужно отработать,\n
    /check_complete:id - Отметить заявку как отработанную.\n""")

@dp.message_handler(commands=['password'])
async def logging_in_bot(message: types.Message):#Функция авторизации нового пользователя.
    if message.text == "/password :" + os.getenv('bot_password'):
#Если команда /password : + пароль совпали, то добвляем в список рассылки
        # set_new_user = BotUsers(username=message.chat.username,
        #                        first_name=message.chat.first_name,
        #                        last_name=message.chat.last_name,
        #                        userid=message.chat.id)
#Поскольку из асинхронной функции нельзя вызвать синхронный код, то для него создаём отдельный event_loop который в
#работает асинхронно в асинхронной функции и обрабаотывает синхронный код
        loop = asyncio.get_event_loop()
        async_list_task = loop.run_in_executor(None, add_users, message)#Вызываем в этом эвент лупе нашу функцию чтения БД
        async_list = await async_list_task
        if async_list[1]:# Если get_or_create вернул что объект только создан, то
            await message.reply("Вы добавлены в список рассылки")
        else:
             await message.reply("Вы уже были добавлены!")
    else:
        await message.reply("Пароль не верный!")

def get_in_db(message, complete):
    #print(message)
    #print(complete)
    FB = FeedBack.objects.filter(complete=complete)#Получаем QuerySet по полю complete
    my_list = [BotUsers.objects.filter(userid=message.chat.id).exists()]#Проверяем авторизован ли пользователь.
    #Если пользователь с определённым чатID есть в таблице рассылки, то считается авторизованным в боте
    #print(my_list)
    for item in FB: # Готовим Строку табличного вида с записями.
        my_list.append(str(item.id) + " " + str(item.name) + " " + str(item.phone) +" " + str(format(item.datetime_create, "d.m.Y H:i")))
    return my_list

@dp.message_handler(commands=['no_complete', "complete"])
async def get_no_complete(message: types.Message): #Функция запроса всех отработанных или неотработанных заявок
        loop = asyncio.get_event_loop() # event_loop для запуска синхронной функции внутри асинхронной.
        if message.text=="/no_complete": #Если команда прислать все незавершенные заявки
            async_list_task = loop.run_in_executor(None, get_in_db, message, False) #Вызываем функцию get_in_db с двумя аргументами
            async_list = await async_list_task
        elif message.text=="/complete":
            async_list_task = loop.run_in_executor(None, get_in_db, message, True)
            async_list = await async_list_task
        if async_list[0]:#Если пользователь авторизован, то первый элемент списка True
            table = "id    Имя    Телефон      Дата и Время\n"# Делаем шапку таблицы
            for item in async_list[1:]:
                table+=item + "\n"
            await message.reply(table)
        else:
             await message.reply("Вы не авторизованы!")

def chect_FB(message, id):
    FB = FeedBack.objects.filter(id=id)
    UserComplete = BotUsers.objects.get(userid=message.chat.id)
    print(UserComplete)
    my_list = [BotUsers.objects.filter(userid=message.chat.id).exists()]
    print(my_list)
    #FB.complete = True
    #FB.user_last_change = UserComplete
    print(FB)
    my_list.append(FB.update(complete = True, user_last_change = UserComplete.id, datetime_complete=timezone.now()))
    return my_list

@dp.message_handler()
async def get_no_complete(message: types.Message):
        loop = asyncio.get_event_loop()
        if message.text[0:16] == "/check_complete:":
            try:
                id = int(message.text[16:])
                async_list_task = loop.run_in_executor(None, chect_FB, message, id)
                async_list = await async_list_task
                if async_list[0]:
                    if async_list[1]==True:
                        await message.reply("Заявка отработана!")
                    else: await message.reply("Ошибка выполнения, обратитесь к администратору!")
                else:
                    await message.reply("Вы не авторизованы!")
            except ValueError: await message.reply("id должно быть целым числом")


async def send_message(userid, text_message):

    await bot.send_message(chat_id=userid, text=text_message)

