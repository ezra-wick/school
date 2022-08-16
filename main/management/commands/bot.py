from django.core.management.base import BaseCommand
from aiogram import executor
from .commands import dp

#В этом файле происходит запуск бота в решиме пулинг


def run_bot():# Функция запуска диспетчера
    import logging
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

class Command(BaseCommand): # Менеджмент команда код в hendle запскается после запуска команды
    help = "FeedBack_telegram_bot"

    def handle(self, *args, **options):
        run_bot()



