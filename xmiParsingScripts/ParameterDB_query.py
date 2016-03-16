import sqlite3
import os

from ParameterDB_constructor import parameter_db_name

__all__ = ["get_table_names"]

class connection_cache(object):

    def __init__(self):
        self._connection_dict = {}

    def connect(self, file_name):
        if file_name in self._connection_dict:
            return self._connection_dict[file_name]

        conn = sqlite3.connect(file_name)
        self._connection_dict[file_name] = conn
        return conn

_global_connection_cache = connection_cache()


def get_table_names(db_name):
    cursor = _global_connection_cache.connect(db_name).cursor()
    query = "SELECT name FROM sqlite_master WHERE type='table'"
    cursor.execute(query)
    results = cursor.fetchall()
    return results

