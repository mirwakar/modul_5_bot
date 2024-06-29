import os
from asyncio import run
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, BotCommand
from dotenv import load_dotenv
from status import SignUp
from functions import register_name, register_phone, register_address, register_position, register_finish, register_email, Idora, stop_process
from functions import start, helps, vacancy, start_menu, stop, info

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

db = Dispatcher()


async def main(db) -> None:
    bot = Bot(token=TOKEN)
    await bot.set_my_commands(
        [
            BotCommand(command="/start", description="Botni ishga tushurish 🚀"),
            BotCommand(command="/info", description="Shaxsiy ma'lumotlarni olish ℹ️"),
            BotCommand(command="/vacancy", description="Ishga elon berish 📄"),
            BotCommand(command="/help", description="Yordam ❓"),
            BotCommand(command="/stop", description="Ishni to'xtatish 🛑")
        ]
    )
    db.message.register(info, Command(commands=["info"]))
    db.startup.register(start)
    db.message.register(vacancy, Command(commands=["vacancy"]))
    db.message.register(stop_process, Command(commands=["stop"]))
    db.message.register(start_menu, Command(commands=["start"]))
    db.message.register(helps, Command(commands=["help"]))

    db.message.register(Idora, SignUp.idora)
    db.message.register(register_name, SignUp.name)
    db.message.register(register_phone, SignUp.phone)
    db.message.register(register_address, SignUp.address)
    db.message.register(register_position, SignUp.position)
    db.message.register(register_email, SignUp.email)
    db.message.register(register_finish, SignUp.salary)

    db.shutdown.register(stop)
    await db.start_polling(bot)


if __name__ == '__main__':
    run(main(db))
