class Invoice():
    def __init__(self, number, descrition, quantity, price):
        self.__number = number
        self.__descrition = descrition
        self.__quantity = quantity
        self.__price = price

    def display_details(self):
        print("part number=", self.__number)
        print("part description=", self.__descrition)
        print("quantity of item=", self.__quantity)
        print("price per item=", self.__price)

    def get_number(self):
        print(self.__number)

    def get_description(self):
        print(self.__descrition)

    def get_quantity(self):
        print(self.__quantity)

    def get_price(self):
        print(self.__price)

    def set_number(self, new_number):
        (self.__number) = new_number

    def set_description(self, new_description):
        (self.__descrition) = new_description

    def set_quantity(self, new_quantity):
        (self.__quantity) = new_quantity

    def set_price(self, new_price):
        (self.__price) = new_price

    def get_invoice(self):
        if self.__quantity < 0:
            self.__quantity = 0

        elif self.__price < 0:
            self.__price = 0
        print("amount=", self.__quantity*self.__price)


Invoice = Invoice(1, "pen", 5, -10)
Invoice.display_details()
Invoice.get_invoice()
