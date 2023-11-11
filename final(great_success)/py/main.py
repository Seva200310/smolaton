import sqlite3

# Создаем подключение к базе данных (файл my_database.db будет создан)
connection = sqlite3.connect('my_database.db')

connection.close()

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    username TEXT NOT NULL,
    score INTEGER,
    color TEXT NOT NULL,
    team TEXT 
)
''')
connection.commit()
connection.close()

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Zones (
    article_name TEXT NOT NULL,
    article_link TEXT NOT NULL,
    article_price TEXT NOT NULL,
    article_owner TEXT NOT NULL,
    article_time TIME DEFAULT NULL, -- Remove the trailing comma here
    article_time_prev TIME DEFAULT NULL,
    border_with TEXT NOT NULL
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
