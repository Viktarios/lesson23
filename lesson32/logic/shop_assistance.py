from lesson32.container.basket import Basket
from lesson32.entity.product import Product

class ShopAssistance:
    @staticmethod
    def calculate_total_price(basket):
        if isinstance(basket, Basket) and basket.size != 0:
            total = 0
            for i in range(basket.size):
                product = basket.get_product(i)

                if isinstance(product, Product):
                    total += product.money

            return total
        else:
            return 0
