from aiogram.fsm.state import StatesGroup, State


class SignUp(StatesGroup):
    idora = State()
    name = State()
    phone = State()
    address = State()
    position = State()
    email = State()
    salary = State()

