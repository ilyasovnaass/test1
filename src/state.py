from aiogram.fsm.state import State, StatesGroup


class Quiz(StatesGroup):
    waiting_answer = State()


class AddQuestion(StatesGroup):
    question = State()
    correct_answer = State()


class DeleteQuestion(StatesGroup):
    waiting_id = State()
    