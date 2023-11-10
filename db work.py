from datetime import datetime, time


class DbWork:


    def __init__(self, article_name, article_link, article_price, article_owner, article_time, article_time_prev):
        self.article_name = article_name
        self.article_link = article_link
        self.article_price = article_price
        self.article_owner = article_owner
        self.article_time = article_time
        self.article_time_prev = article_time_prev


    def enemy_is_captured(self):
        ans = False
        if self.article_time_prev is None or self.article_time < self.article_time_prev:
            ans = True
            self.article_time_prev = self.article_time
        

    def colour_paint(self):
        self.enemy_is_captured()


