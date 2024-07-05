import sys


class Cable:

    def __set_length(self, length):
        if not isinstance(length, int) or length < 0 or length > sys.maxsize:
            raise ValueError

        self.length = length

    def __init__(self, length):
        self.__set_length(length)
