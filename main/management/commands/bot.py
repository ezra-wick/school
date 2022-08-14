from django.core.management.base import BaseCommand
from aiogram import executor
from .commands import dp


def run_bot():
    import logging
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

class Command(BaseCommand):
    help = "FeedBack_telegram_bot"

    def handle(self, *args, **options):
        run_bot()



