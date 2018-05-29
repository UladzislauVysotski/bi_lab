class CoffeeShop(object):
    visitors_count = 0

    def __init__(self, visitor_name, discount):
        self.visitor_name = visitor_name
        self.discount = discount
        # self.sum_bill = 0
        self.coffee_dict = {}
        CoffeeShop.visitors_count += 1

    @staticmethod
    def get_visitors_count():
        return CoffeeShop.visitors_count

    @staticmethod
    def print_visitors_count():
        print("Count of visitors: %d" % CoffeeShop.visitors_count)

    @property
    def get_visitor_coffee_count(self):
        return len(self.coffee_dict)

    @property
    def get_visitor_coffee_list(self):
        return self.coffee_dict

    def print_visitor_coffee_list(self):
        for coffee, price in self.coffee_dict.items():
            print(coffee, price)

    def add_coffee(self, coffee_name, coffee_price):
        self.coffee_dict[coffee_name] = coffee_price

    @property
    def get_bill_without_discount(self):
        sum_bill = 0
        for coffee, price in self.coffee_dict.items():
            sum_bill += price
        return sum_bill

    @property
    def get_bill_with_discount(self):
        return self.get_bill_without_discount * (1 - self.discount / 100)

    def del_coffee(self, coffee_name):
        self.coffee_dict.pop(coffee_name)

    def print_full_info(self):
        print()
        print("Name: ", self.visitor_name)
        print("Discount: ", self.discount, "%")
        print("Sum without discount: ", self.get_bill_without_discount)
        print("Sum with discount: ", self.get_bill_with_discount)
        print("Coffee count: ", self.get_visitor_coffee_count)
        print("Coffee:")
        self.print_visitor_coffee_list()
        print()


visitor1 = CoffeeShop("Melice", 10)
visitor1.add_coffee("Latte", 25)
visitor1.add_coffee("Americano", 20)
visitor1.add_coffee("Mocco", 15)
visitor1.del_coffee("Mocco")

visitor1.print_full_info()

CoffeeShop.print_visitors_count()

visitor2 = CoffeeShop("Adison", 0)
visitor2.add_coffee("Latte", 25)
visitor2.del_coffee("Latte")

visitor2.print_full_info()

CoffeeShop.print_visitors_count()
