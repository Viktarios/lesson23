from lesson32.entity.milk import Milk
from lesson32.entity.bread import Bread
from lesson32.entity.orange import Orange
from  lesson32.entity.product import Product
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
        if (isinstance(index,int)
            and index>=0 and index < self.size):
                return self.__products[index]

    def add(self, product):
        if isinstance(product,Product):
            self.__products.append(product)

    def __str__(self):
        msg = "List of product"
        for i in range(self.size):
            msg += f"\n{i+1})" + str(self.__products[i])

        return msg

