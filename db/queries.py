# USERS
# QUESTIONS
# RESULTS


CREATE_USERS_TABLE = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER NOT NULL UNIQUE,
        username TEXT
    )
'''     # CREATE_USERS_TABLE -- создаем переменную с тройными кавычками, потому что запрос будет длинным, на несколько строк
# CREATE TABLE IF NOT EXISTS users -- создать таблицу users, если ее еще не создавали (IF NOT EXISTS -- если не существует)
# id - имя колонки; INTEGER - тип данных (целое число); PRIMARY KEY -- главный ключ, уникальный номер каждой строки
# AUTOINCREMENT -- SQLite сам будет ставить id, не надо писать вручную
# telegram_id -- id человека в Телеграме. приходит от message.from_user.id; NOT NULL -- поле не может быть пустым, без него строку не сохранить
# UNIQUE -- в таблице не может быть двух одинаковых telegram_id. Один человек = одна строка
# username TEXT -- useraname человека в текстовом порядке, также тут нет NOT NULL значит поле может быть пустым, если у человек нет username
# ЭТА ТАБЛИЦА -- СПИСОК ВСЕХ, КТО ХОТЬ РАЗ НАЖАЛ /start


CREATE_QUESTIONS_TABLE = '''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT NOT NULL,
        correct_answer TEXT NOT NULL
    )
'''


CREATE_RESULTS_TABLE = '''
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        question_id INTEGER NOT NULL,
        is_correct BOOLEAN NOT NULL DEFAULT 0,

        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
    )
'''
# user_id -- это id человека в таблице users, а question_id -- это id вопроса из таблицы questions
# BOOLEAN -- в SQLite это на самом деле 0 или 1; DEFAULT 0 -- если не указать по умолчанию будет 0, то есть "неправильно"
# FOREIGN KEY -- внешний ключ, связывает одну таблицу с другой
# FOREIGN KEY (user_id) REFERENCES userd(id) ON DELETE CASCADE -- гарантирует, что результат нельзя записать для несуществующего пользователя.
# REFERENCES -- отсылается на колонку id из таблицы users или questions
# Если пользователя удалят из users, все его ответы в results удалятся автоматически (ON DELETE CASCADE)



# CRUD -- CREATE-READ-UPDATE-DELETE -- это 4 базовые операции с базой


#1 Read (ключевое слово - SELECT):

GET_USER_BY_TG_ID = 'SELECT * FROM users WHERE telegram_id = ?'    # находит  и возвращает данные пользователя

#2 Create (ключевое слово - INSERT):

INSERT_USER = 'INSERT OR IGNORE INTO users (telegram_id, username) VALUES (?, ?)'   # добавляет нового пользователя в таблицу

# -- Домашка --

#3 Update (ключевое слово - UPDATE): 

UPDATE_USER_USERNAME = 'UPDATE users SET username = ? WHERE telegram_id = ?'   # меняет данные существуещего пользователя, например его ник

#4 Delete (ключевое слово DELETE):

DELETE_USER = 'DELETE FROM users WHERE telegram_id = ?'    # удаляет запись пользователя из базы



# --QUESTIONS--

GET_ALL_QUESTIONS = 'SELECT * FROM questions'

CREATE_QUESTION = 'INSERT INTO questions (question_text, correct_answer) VALUES (?, ?)'

GET_QUESTION_BY_ID = 'SELECT FROM * questions WHERE id = ?'

UPDATE_QUESTION = 'UPDATE questions SET question_text = ?'

DELETE_QUESTION = 'DELETE FROM questions WHERE id = ?'

INSERT_QUESTION = 'INSERT INTO questions (question_text, correct_answer) VALUES (?, ?)'



# -- RESULTS --

INSERT_RESULT = 'INSERT INTO results (user_id, question_id, is_correct) VALUES (?, ?, ?)'

GET_ALL_RESULTS = 'SELECT * FROM results'

UPDATE_RESULT = 'UPDATE results SET is_correct = ? WHERE user_id = ? AND question_id = ?'

DELETE_RESULTS = 'DELETE FROM results WHERE user_id = ? AND question_id = ?'

GET_SCORE_BY_USER_ID = 'SELECT COUNT(*) as total, SUM(is_correct) as correct FROM results WHERE user_id = ?'

