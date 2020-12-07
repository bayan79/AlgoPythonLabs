"""
ООП в Python

Предметная область: мальчик Борис в подвале магазина спорт товаров
ходит и пытается угадать, какой мяч из кучи мячей для какой игры нужен
в зависимости от цвета и размера. Но мальчик не тупой, если 
один раз ответил не правильно то записывает в свою книжечку 
правильный ответ, и в следующий раз, встретив похожий мяч, 
назовет его. Если угадал, то не записывает и забывает (не тупой, но и не умный)

Класс Ball уже реализован, но его необходимо доработать до GameBall

Класс Boy нужно реализовать чтобы можно было создать Борю, 
делать отдельный класс для Бори не универсально, а взрослые 
умеют запоминать вещи в уме, поэтому расширять класс до Person 
тоже не нужно для задачи

Класс Book реализуем для разделения мальчика и книги, потому что
я не знаю какие там дальше задания, и Боря мне может быть еще понадобиться,
а делать из него портянку с кучей разнородных фичей не канон.
"""
import random
import json

from lab2 import Ball, fuzzy_compare_int, fuzzy_compare_string


class GameBall(Ball):
    def __init__(self, size: int, color:str, game:str):
        super(GameBall, self).__init__(size, color)
        self.game = game

    def __repr__(self):
        return f"GameBall({self.size}, \"{self.color}\", \"{self.game}\")"

    def fuzzy_compare(self, ball):
        game_result = fuzzy_compare_string(self.game, ball.game)
        return  super(GameBall, self).fuzzy_compare(ball) * game_result

    def json_string(self):
        fields = ['size', 'color', 'game']
        json_dict = {field: getattr(self, field) for field in fields}
        return json.dumps(json_dict)

    @staticmethod
    def from_json_string(json_string: str):
        return GameBall(**json.loads(json_string))

    @staticmethod
    def random_ball():
        colors = ['green', 'red', 'blue', 'orange', 'white', 'yellow']
        games = ['baseball', 'soccer', 'tennis', 'ping-pong', 'polo']
        return GameBall(random.randint(1,20), random.choice(colors), random.choice(games))

class Book:
    def __init__(self):
        self.__data = []

    def read(self):
        return self.__data

    def write(self, string: str):
        self.__data.append(string)

class Boy:
    ACCURACY = 0.7
    def __init__(self, name: str):
        self.book = Book()
        self.name = name

    def take_new_ball(self):
        return GameBall.random_ball()

    def detect_ball(self, ball):
        if self.find_ball_in_book(ball):
            return True
        self.write_ball(ball)
        return False

    def find_ball_in_book(self, ball):
        for string in self.book.read():
            ball_book = GameBall.from_json_string(string)
            if ball.fuzzy_compare(ball_book) > self.ACCURACY:
                return ball_book
        return None

    def write_ball(self, ball):
        self.book.write(ball.json_string())


if __name__ == "__main__":
    boris = Boy('Boris')

    # Посмотрим как много мячей сможет записать Боря
    # после бессонной ночи и проверки 1234 мячей
    for _ in range(1234):
        ball = boris.take_new_ball()
        boris.detect_ball(ball)

    print("Balls in Boris's book: ", len(boris.book.read()))
        