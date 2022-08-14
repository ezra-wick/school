from main.models import BotUsers, FeedBack
from aiogram import types
import asyncio
from django.utils.dateformat import *
from django.utils import timezone

import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


def add_users(message):
    set_new_user, user_add = BotUsers.objects.get_or_create(
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
async def logging_in_bot(message: types.Message):
    if message.text == "/password :" + os.getenv('bot_password'):
        # set_new_user = BotUsers(username=message.chat.username,
        #                        first_name=message.chat.first_name,
        #                        last_name=message.chat.last_name,
        #                        userid=message.chat.id)
        loop = asyncio.get_event_loop()

        async_list_task = loop.run_in_executor(None, add_users, message)
        async_list = await async_list_task
        if async_list[1]:
            await message.reply("Вы добавлены в список рассылки")
        else:
             await message.reply("Вы уже были добавлены!")
    else:
        await message.reply("Пароль не верный!")

def get_in_db(message, complete):
    #print(message)
    #print(complete)
    FB = FeedBack.objects.filter(complete=complete)
    my_list = [BotUsers.objects.filter(userid=message.chat.id).exists()]
    #print(my_list)
    for item in FB:
        my_list.append(str(item.id) + " " + str(item.name) + " " + str(item.phone) +" " + str(format(item.datetime_create, "d.m.Y H:i")))
    return my_list

@dp.message_handler(commands=['no_complete', "complete"])
async def get_no_complete(message: types.Message):
        loop = asyncio.get_event_loop()
        if message.text=="/no_complete":
            async_list_task = loop.run_in_executor(None, get_in_db, message, False)
            async_list = await async_list_task
        elif message.text=="/complete":
            async_list_task = loop.run_in_executor(None, get_in_db, message, True)
            async_list = await async_list_task
        if async_list[0]:
            table = "id    Имя    Телефон      Дата и Время\n"
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

