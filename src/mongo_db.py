"""Database Loader Script"""

from pymongo import MongoClient


class MongoDB(object):  # pylint: disable=too-few-public-methods
    """Class MongoDB"""

    def __init__(self, db_name):
        self._conn = MongoClient("localhost", 27017)
        self._db = self._conn[db_name]
        print "Connection established with database: %s" % db_name

    # Returns the collection with the name parameter
    def collection(self, name=""):
        return self._db[name]
