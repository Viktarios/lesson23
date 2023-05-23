class Basket:
    def __init__(self, products=None):
        if not products:
            self.__products = []
        else:
            self.__products = products

    @property
    def size(self):
        return len(self.__products)

    def get_product(self, index):
        return self.__products[index]

    def add(self, product):
        self.__products.append(product)

    def __str__(self):
        msg = "List of product"
        for i in range(self.size):
            msg += f"\n{i+1})" + str(self.__products[i])

        return msg

