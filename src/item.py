import random
import string
from validators.min import min
from validators.max import max


class Item:
    def __init__(self, product, quantity, subtotal):
        self.__id = self.id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)])
        self.__product = product
        self.__quantity = quantity
        self.__subtotal = subtotal
        self.__options = 0
        self.__score = 0
        self.__note = ''

    def get_id(self):
        return self.__id

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def get_subtotal(self):
        return self.__subtotal

    def get_note(self):
        return self.__note

    def is_rated(self):
        return self.__options >> 0 & 1

    def has_note(self):
        return self.__options >> 1 & 1

    def set_note(self, note):
        self.__note = note
        self.__options = ((1 << 1) | self.__options)

    @min(1)
    @max(5)
    def set_score(self, score):
        self.__score = score
        self.__options = ((1 << 0) | self.__options)

    def get_score(self):
        return self.__score
