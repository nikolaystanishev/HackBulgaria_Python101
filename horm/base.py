from .fields import Fields


class BaseMeta(type):
    def __new__(cls, name, bases, clsdict):

        fields = {}
        tablename = ''

        for attr, value in clsdict.items():
            if isinstance(value, Fields):
                fields[attr] = value
            if attr == '__tablename__':
                tablename = value
        for attr, _ in fields.items():
            clsdict.pop(attr)

        clsdict['_fields'] = fields
        clsdict['__tablename__'] = tablename

        clsobj = super().__new__(cls, name, bases, clsdict)

        if not hasattr(cls, 'registry'):
            cls.registry = set()

        cls.registry.add(clsobj)

        return clsobj
