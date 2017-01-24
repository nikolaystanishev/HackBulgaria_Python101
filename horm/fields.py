import abc


class Fields(metaclass=abc.ABCMeta):
    def get_value(self, value):
        return value


class PKColumn(Fields):
    def __init__(self, value=1):
        if self.validate(value):
            self.value = value
        else:
            raise ValueError

    def get_type(self):
        return 'INTEGER PRIMARY KEY AUTOINCREMENT'

    def validate(self, value):
        return type(value) == int


class IntegerColumn(Fields):
    def __init__(self, value):
        if self.validate(value):
            self.value = value
        else:
            raise ValueError

    def get_type(self):
        return 'INTEGER'

    def validate(self, value):
        return type(value) == int


class TextColumn(Fields):
    def __init__(self, max_length=0, value=''):
        if self.validate_length(max_length):
            self.max_length = max_length
            if self.validate_text(value):
                self.value = value
            else:
                raise ValueError
        else:
            raise ValueError

    def get_type(self):
        return 'TEXT'

    def validate_text(self, value):
        return type(value) == str

    def validate_length(self, value):
        return type(value) == int
