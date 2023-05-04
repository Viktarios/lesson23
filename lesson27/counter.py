class Counter:
    def __init__(self, count=0):
        if count >= 0:
            self.__count = count
        else:
            self.__count = 0

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        if count >= 0:
            self.__count = count

    @count.deleter
    def count(self):
        del self.__count

    def increment(self):
        self.__count += 1

    def decrement(self):
        if self.__count != 0:
            self.__count -= 1

    def reset(self):
        self.__count = 0

    def __str__(self):
        return "Counter:" + str(self.__count)
