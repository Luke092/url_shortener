from repository.UrlRepository import UrlRepository


class PsqlUrlRepository(UrlRepository):

    def __init__(self, connection):
        self._conn = connection

    def get_by_short_code(self, code):
        res = self._conn.execute_query("SELECT * FROM url.urls WHERE url_short = %s", (code,))

        if len(res) == 0:
            return None

        return res[0]

    def add(self, url):
        res = self._conn.execute_query("INSERT INTO url.urls (url) VALUES (%s) RETURNING *", (url,))

        if res is None:
            return None

        return res[0]

    def update(self, url):
        res = self._conn.execute_query(
            "UPDATE url.urls SET url = %s, url_short=%s WHERE id = %s RETURNING *",
            (url['url'], url['url_short'], url['id'])
        )

        if res is None:
            return None

        return res[0]
