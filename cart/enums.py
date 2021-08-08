from enum import IntEnum


class Status(IntEnum):
    opened = 10
    pending = 20
    accepted = 30
    packed = 40
    shipped = 50
    completed = 60
    canceled = 70

    @staticmethod
    def get_choices():
        return ((x.value, x.name) for x in Status)
