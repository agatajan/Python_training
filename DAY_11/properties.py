class Product():
    margin_factor = 0.2

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if (price < 0.0):
            raise ValueError("Price should be greater than 0!")
        self.__price = price

    @price.deleter
    def price(self):
        self.__price = None

    @property
    def margin(self):
        return self.margin_factor*self.__price



product = Product("HP printer", 1000)
product.price = 1200
print(product.price)
print(product.margin)

# product.margin = 12323
