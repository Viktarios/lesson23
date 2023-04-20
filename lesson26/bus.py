class Bus:
    def __init__(self, brand='no name', price=0, number=0):
        self.brand = brand
        self.price = price
        self.number = number

    # def __del__(self):
    #     print(f"destructor for {self.brand}")

    def __str__(self):
        return f"Bus: {self.brand}, price =${self.price}, " \
               f"number = {self.number}"


if __name__ == "__main__":
    bus1 = Bus("Scania")
    bus2 = Bus("MAZ")
    bus3 = Bus("Volvo")
    bus4 = Bus("PAZ")
    bus5 = Bus("Mercedes Benz")

