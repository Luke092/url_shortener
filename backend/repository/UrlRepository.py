import abc


class UrlRepository(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_by_short_code(self, code):
        raise NotImplementedError()

    @abc.abstractmethod
    def add(self, url):
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, url):
        raise NotImplementedError()
