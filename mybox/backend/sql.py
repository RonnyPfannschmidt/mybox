"""

"""

from sqlalchemy import create_engine
from sqlalchemy import (
    MetaData, Table, Column,
    Unicode, UnicodeText, Integer,
)

meta = MetaData()

folders = Table(
    'folders', meta,
    Column('id', Integer, primary_key=True),
    Column('name', Unicode, unique=True),
)



class Backend(object):
    def __init__(self, engine):
        self.engine = engine

    @classmethod
    def create(cls, uri):
        engine = create_engine(uri)
        return cls(engine)

    def tree(self):
        return {}

    def add_folder(self, name):
        pass
