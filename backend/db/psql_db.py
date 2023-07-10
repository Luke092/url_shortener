import psycopg
from psycopg.rows import dict_row

import config


class PsqlDb(object):

    def __init__(self):
        self._configs = config.Config().configs
        self._connection = None

    def connect(self):
        if self._connection is not None:
            self.disconnect()

        self._connection = psycopg.connect(
            self._configs["connectionString"],
            row_factory=dict_row
        )

    def execute_query(self, sql, args):
        if self._connection is None:
            self.connect()

        try:
            cur = self._connection.cursor()
            cur.execute(sql, args)

            return cur.fetchall()

        except (Exception, psycopg.DatabaseError) as error:
            return None

    def commit(self):
        if self._connection is None:
            return
        self._connection.commit()

    def rollback(self):
        if self._connection is None:
            return
        self._connection.rollback()

    def disconnect(self):
        self._connection.close()
        self._connection = None
