import random
import string
from src.handler import Handler


class Order(Handler):
    def __init__(self, date, total):
        self.__id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)])
        self.__date = date
        self.__total = total
        Handler.__init__(self)

    def get_id(self):
        return self.__id

    def get_date(self):
        return self.__date

    def get_total(self):
        return self.__total
