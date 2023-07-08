from use_cases.get_url_by_id import get_url_by_id
from use_cases.add_url import add_url


class UrlController(object):
    def add(self):
        pass

    def get_by_code(self, identifier):
        return get_url_by_id(identifier)
