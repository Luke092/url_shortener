from use_cases.add_url import add_url
from use_cases.get_url_by_id import get_url_by_id


class UrlController(object):
    def add(self, url):
        url = add_url(url)

        if url is None:
            return {
                "status": 400
            }

        return {
            "status": 200,
            "body": url
        }

    def get_by_code(self, identifier):
        url = get_url_by_id(identifier)

        if url is None:
            return {
                "status": 404
            }

        return {
            "status": 200,
            "body": url
        }
