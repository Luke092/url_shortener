from use_cases.add_url import add_url
from use_cases.get_url_by_id import get_url_by_id


class UrlController(object):
    def add(self, url):
        return add_url(url)

    def get_by_code(self, identifier):
        return get_url_by_id(identifier)
