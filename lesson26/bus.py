class Bus:
    def __init__(self, brand='no name', price=0, number=[]):
        self.__brand = brand
        self.__price = price
        self.__number = number

    def get_brand(self):
        return self.__brand

    def set_brand(self, name):
        self.__brand = name

    def get_number(self):
        return self.__number

    def set_number(self):
        return self.__number

    def __str__(self):
        return f"Bus: {self.brand}, price =${self.price}, " \
               f"number = {self.number}"


if __name__ == "__main__":
    bus = Bus()
    print(bus.)
