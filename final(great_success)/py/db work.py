from datetime import datetime, time
import random
import sqlite3
import colorsys



class DbWork:
    def __init__(self, article_name, article_link, article_price, article_owner, article_time, article_time_prev, username = None, score = 0, team = None):
        self.article_name = article_name
        self.article_link = article_link
        self.article_price = article_price
        self.article_owner = article_owner
        self.article_time = article_time
        self.article_time_prev = article_time_prev
        self.color = random.choice(DbWork.generate_colors(100))
        self.username = username
        self.score = score
        self.team = team

    @staticmethod
    def generate_colors(num_colors):
        # Начальное значение оттенка (от 0 до 1)
        hue_start = 0.0

        # Шаг изменения оттенка для каждого цвета
        hue_step = 1.0 / num_colors

        # Генерация цветов
        colors = []
        for i in range(num_colors):
            # Получаем RGB значения из HSV
            rgb = colorsys.hsv_to_rgb(hue_start, 0.8, 0.8)  # Насыщенность и значение оставляем постоянными
            # Масштабируем значения от 0-1 до 0-255 и преобразуем в целые числа
            colors.append(tuple(int(val * 255) for val in rgb))

            # Увеличиваем оттенок для следующего цвета
            hue_start += hue_step

        return colors

    def enemy_is_captured(self, new_owner, new_score):
        self.color = None
        ans = False
        if self.article_time_prev is None or self.article_time < self.article_time_prev:
            ans = True
            self.article_time_prev = self.article_time
            self.article_owner = new_owner
            self.score = new_score
        return ans, self.color


    def colour_column(self):
        # Создаем подключение к базе данных
        connection = sqlite3.connect('my_database.db')
        # Создаем объект курсора
        cursor = connection.cursor()
        # Выполняем SQL-запрос для считывания данных из таблицы Users
        cursor.execute('SELECT color FROM Users')
        # Извлекаем все строки результата
        rows = cursor.fetchall()
        self.color = rows


        # Закрываем соединение с базой данных
        connection.close()

    # def colour_change(self):





