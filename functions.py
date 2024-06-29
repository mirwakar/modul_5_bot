import os
from asyncio import run
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, BotCommand, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ContentType
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
from pprint import pprint
from status import SignUp


async def info(message: Message, bot: Bot, state: FSMContext):
    bot = message.bot
    profile = await bot.get_chat(chat_id=message.from_user.id)
    user = message.from_user
    data = f"""sizning ismingiz: {user.first_name},\n id raqamingiz: {user.id} \n"""
    if user.last_name:
        data += f"sizning familiyangiz: {user.last_name}\n"
    if user.username:
        data += f"sizning familiyangiz: @{user.username}\n"
    if profile.bio:
        data += f"sizning bioingiz: {profile.bio}\n"
    pprint(data)
    await message.answer(text=data)


async def helps(message: Message, bot: Bot, state: FSMContext):
    await message.answer(
        text="""
/start -> botni ishga tushurish🚀
/help -> Comandalarni ko'rishℹ️
/vacancy -> E'lon berish📄
/stop -> Jarayonni to'xtatish❌

Agar savollaringiz bo'lsa, <a href="https://t.me/mirshakar03">@mirshakar03</a> bilan aloqaga chiqing.
        """,
        parse_mode="HTML"
    )


async def vacancy(message: Message, state: FSMContext):
    await message.answer("Idorani kiriting:")
    await state.set_state(SignUp.idora)


async def Idora(message: Message, state: FSMContext):
    await state.update_data(idora=message.text)
    await message.answer("Ismingizni kiriting:")
    await state.set_state(SignUp.name)


async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Telefon raqamingizni kiriting: ")
    await state.set_state(SignUp.phone)


async def register_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Manzilingizni kiriting: ")
    await state.set_state(SignUp.address)


async def register_address(message: Message, state: FSMContext):
    await state.update_data(address=message.text)
    await message.answer("Lavozimingizni kiriting: ")
    await state.set_state(SignUp.position)


async def register_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Emailingizni kiriting: ")
    await state.set_state(SignUp.salary)


async def register_position(message: Message, state: FSMContext):
    await state.update_data(position=message.text)
    await message.answer("Ish haqini kiriting: ")
    await state.set_state(SignUp.email)


async def register_finish(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(salary=message.text)
    data = await state.get_data()
    user = message.from_user
    txt = f'''
Ma'lumotlaringiz:
🇺🇿Telegram: @{user.username if user.username else "username mavjud emas"}
🏢Idora:{data.get("idora")}
🧍‍♂️Ism: {data.get("name")}
☎️Telefon: {data.get("phone")}
🌎Manzil: {data.get("address")}
🪙Maosh: {data.get("email")}
👨‍💻Lavozim: {data.get("position")}
📬Email: {data.get("salary")}
        '''
    await message.answer(text=txt)
    await message.answer(f"@{user.first_name} tez orada malumotingiz kanalga chiqadi")

    await state.clear()
   # await message.answer("Tez orada malumotlaringiz kanalga chiqariladi:")
   # await bot.send_message(chat_id=6225636357, text=txt)


async def stop_process(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Jarayon to'xtatildi.")


async def start_menu(message: Message, bot: Message, state: FSMContext):
    await message.answer(f"Assalommu aleykum {message.from_user.first_name} /help yordamida kerakli menyuni tanlang")


async def start(bot: Bot):
    await bot.send_message(chat_id=6225636357, text="Bot ishg atushdi ✅")


async def stop(bot: Bot):
    await bot.send_message(chat_id=6225636357, text="Bot toxtadi ⚠️")
