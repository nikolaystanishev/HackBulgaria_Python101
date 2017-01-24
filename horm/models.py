import sqlite3
from .base import BaseMeta
import queries


class BaseModel(metaclass=BaseMeta):
    db = sqlite3.connect('BaseModel.db')
    db.row_factory = sqlite3.Row
    c = db.cursor()

    @classmethod
    def create_all_tables(cls):
        for cl in cls.registry:
            if cl._fields:
                query = queries.create_table(cl.__tablename__, cl._fields)
                BaseModel.c.execute(query)
                BaseModel.db.commit()

    @classmethod
    def create_obj(cls, **kwargs):
        fields = []
        values = []
        for f, v in kwargs.items():
            fields.append(f)
            values.append(v)
        query = queries.insert_in_table(cls.__tablename__, fields)
        BaseModel.c.execute(query, tuple(values))
        BaseModel.db.commit()

    @classmethod
    def filter(cls, **kwargs):
        fields = []
        values = []
        for f, v in kwargs.items():
            fields.append(f)
            values.append(v)
        query = queries.select_from_table(cls.__tablename__, fields)
        result = BaseModel.c.execute(query, tuple(values))
        return dict(result.fetchone())
