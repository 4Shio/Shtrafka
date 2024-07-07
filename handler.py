from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from base import *
from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton
from datetime import *
from aiogram.fsm.state import StatesGroup, State
from func import *
import re
now = datetime.now()

router = Router()

def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row],one_time_keyboard = True)

remove_key = ReplyKeyboardRemove()

def make_str(text_str):
    return   ' '.join(str(i) for i in text_str )

def make_more_str(text_str):
      return '\n'.join('  '.join(str(i) for i in v) for v in text_str)



with session as session:
    
    class GetQuery(StatesGroup):
          mark = State()
          color = State()
          number = State()
          address = State()
    

    @router.message(Command("start"))
    async def start(message:Message):
                if session.query(Workers).filter_by(telegram_id = message.from_user.id).count() ==0:
                    await message.answer (text="Как я погляжу вы новенький \n Приветсвую - это тестовый бот для штрафстоянки",reply_markup=make_row_keyboard(["Добавить автомобиль","просмотр вех автомобилей"]))
                    name = Workers(name = message.from_user.full_name,telegram_id = message.from_user.id)
                    session.add(name)
                    session.commit()
                    session.close()

                else:     
                    await message.answer(text='Приветсвую - это тестовый бот для штрафстоянки',reply_markup=make_row_keyboard(["Добавить автомобиль","просмотр вех автомобилей"]))

    @router.message(F.text == "Добавить автомобиль")
    async def add_avto(message:types.Message,state:FSMContext):
        await message.answer(text='Напишите марку')
          
        await state.set_state(GetQuery.mark)

        @router.message(GetQuery.mark)
        async def get_mark(message_mark:types.Message,state:FSMContext):
                await state.update_data(mark =message_mark.text)
                await state.set_state(GetQuery.color)
                await message_mark.answer(text="Теперь напиши цвет")

        @router.message(GetQuery.color)
        async def get_color(message_color:types.Message,state:FSMContext):
              await state.update_data(color = message_color.text)
              await state.set_state(GetQuery.address)
              await message_color.answer(text='Введите адресс')
        
        @router.message(GetQuery.address)
        async def get_addres(message_addres:types.Message,state:FSMContext):
            await state.update_data(addres = message_addres.text)
            await state.set_state(GetQuery.number)
            await message_addres.answer(text='Введите гос номер')


        @router.message(GetQuery.number)
        async def get_number(message_number:types.Message,state:FSMContext):
            await state.update_data(number = message_number.text)
            data = await state.get_data()
            
            
            now = datetime.now()
            car =  cars_to_get(mark = data['mark'],
                        color = data['color'],
                        gos_number = data['number'],
                        address = data['addres'],
                        time = now,
                        
                        )
            session.add(car)
            session.commit()
            session.rollback()
    @router.message(F.text == "просмотр вех автомобилей")
    async def view_all(message_view_all:types.Message):
         
         await message_view_all.answer(text= make_more_str(session.query(cars_to_get.mark,cars_to_get.color, cars_to_get.gos_number,cars_to_get.address,cars_to_get.time).all()))
         session.rollback()