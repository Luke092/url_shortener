from db.psql_db import PsqlDb
from repository.PsqlUrlRepository import PsqlUrlRepository


class UoW(object):

    def __init__(self):
        self._db = None

    def __enter__(self):
        self._db = PsqlDb()
        self._db.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._db.disconnect()
        self._db = None

    def get_url_repository(self):
        return PsqlUrlRepository(self._db)

    def commit(self):
        self._db.commit()

    def rollback(self):
        self._db.rollback()
