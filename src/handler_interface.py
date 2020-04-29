import abc


class HandlerI(abc.ABC):
    @abc.abstractmethod
    def add(self, key, item):
        pass

    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def get_by_id(self, id):
        pass
