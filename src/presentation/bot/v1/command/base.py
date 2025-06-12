from enum import Enum


class CommandCollection(Enum):
    def __str__(self):
        return str(self.value)
