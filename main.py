'''Синхронный код'''

# import time

# def task(name, seconds):
#     print(f'Упала задача {name} начал работу!')
#     time.sleep(seconds)
#     print(f'Задача {name} готово!')

# task('1', 4)
# task('2', 3)
# task('3', 2)


'''Асинхронный код'''

# import asyncio


# # Event Loop - менеджер


# async def task(name, seconds):
#     await asyncio.sleep(seconds)
#     print(f'Задача {name}  готово!')

# async def main():
#     await asyncio.gather(     # gather -- позволяет запустить несколько асинхронных задач одновременно 
#         task('1', 4),
#         task('2', 2),
#         task('3', 1),
#     )

# asyncio.run(main())



import asyncio      # asyncio -- встроенная библиотека python, которая позволяет выполнять асинхронные операции
import logging  # Логи - это информация о работе программы, которая помогает разработчику понять, что происходит внутри программы
from aiogram import Bot, Dispatcher     # Мы импортируем два основных класса из библиотеки aiogram
from src.handlers import router     # импортируем роутер из файла handlers.py, который находится внутри папки src
from aiogram.fsm.storage.memory import MemoryStorage    # MemoryStorage -- это хранилище данных в оперативной памяти


# FSM(FiniteStateMachine) -- конечный автомат состояний. Он позволяет боту запоминать, на каком этапе диалога находится пользователь


BOT_TOKEN = '8676423397:AAHVTJFVWoAYIrDPgbIcW-pEGti5lBn8i3M'


bot = Bot(token=BOT_TOKEN)  # Мы создаем экземпляр класса Bot(), сохраняем созданный объект в переменную и через нее мы можем управлять ботом
dp = Dispatcher(storage=MemoryStorage())    # Через диспетчер мы создаем функции, которыми обладает бот, и управляем 


async def main():   # main -- это общепринятое название главной функции программы
    dp.include_router(router)   # Подключаем наш роутер к диспетчеру
    await dp.start_polling(bot)     # отправляет запросы на тг-сервер, также это команда для запуска бота

# Polling -- способ получения обновлений от тг, при котором бот регулярно запрашивает новые события


if __name__ == '__main__':      # это защита от случайного запуска и бот запускается лишь в папке main
    logging.basicConfig(level=logging.INFO)     # у логирования есть уровни ( INFO, DEBUG, WARNING, ERROR, CRITICAL )
    asyncio.run(main())     # Запускает асинхронную функцию main()
    