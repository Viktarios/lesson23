

class Animal:
    def __init__(self, name="no name"):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return f"Animal with name {self.__name}"
