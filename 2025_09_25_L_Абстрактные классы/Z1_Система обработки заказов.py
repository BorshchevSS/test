class Order:
    def __init__(self, order_id):
        self.__order_id = order_id
        self.__products = []
        self.__delivery_address = None
        self.__status = "Created"
        self.__payment_info = None
        self.__total_cost = 0

    def add_product(self, product, price):
        self.__products.append((product, price))
        self.__update_total_cost()

    def remove_product(self, product):
        self.__products = [(p, price) for p, price in self.__products
                           if p != product]
        self.__update_total_cost()

    def __update_total_cost(self):
        self.__total_cost = sum(price for p, price in self.__products)

order = Order(1234)
order.add_product("Pr 1", 100)
order.add_product("Pr 2", 200)
print(order._Order__total_cost)