from src.handler_interface import HandlerI


class Handler(HandlerI):
    def __init__(self):
        self._items = {}

    def add(self, key, item):
        self._items[key] = item

    def get_all(self):
        return list(self._items.values())

    def get_by_id(self, id):
        return self._items.get(id)
