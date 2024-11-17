# Reuben Stoutenburg
# UWYO COSC 1010
# 11/15/2024
# Lab 09
# Lab Section: 13
# Sources: Course code example classes

class Pizza:
    """Describe a pizza"""
    def __init__(self, size, sauce='red'):
        """Initialize the size, sauce, and toppings for pizza"""
        self.size = 0
        if self.size > 10:
            self.size = size
        else:
            self.size = 10
        self.sauce = sauce
        self.toppings = ['cheese']
    def get_size(self):
        return self.size
    def set_size(self,size):
        if size > 10:
            self.size = size
        else:
            self.size = 10
    def get_sauce(self):
        return self.sauce
    def add_toppings(self):
        return self.toppings
    def set_toppings(self, *newtoppings):
        for topping in newtoppings:
            self.toppings.append(topping)
    def num_toppings(self):
        """Calculate the number of toppings"""
        return len(self.toppings)

class Pizzeria:
    """Build a pizza and return its price, size, and contents"""
    price_per_topping = 0.30
    price_per_inch = 0.60
    def __init__(self):
        self.orders = 0
        self.pizzas = []
    def placeOrder(self):
        get_size = "What size of pizza do you wnat(min 10): "
        try:
            size = int(input(get_size))
            if size < 10:
                size = 10
        except ValueError:
            print("Please enter an size greater than 10")
        get_sauce = "What type of sauce would you like(leave blank if you want red): "
        sauce = input(get_sauce)
        if not sauce:
            sauce = red
        get_topping = "Enter the toppings you wnat, one at a time: "
        toppings = []
        while True:
            topping = input(get_topping.strip())
            if not topping:
                break
            toppings.append(topping)
        pizza = Pizza(size = size,sauce = sauce)
        for topping in toppings:
            pizza.set_toppings(topping)
        self.pizzas.append(pizza)
        self.orders += 1
    def getPrice(self, pizza):
        size_price = pizza.get_size() * Pizzeria.price_per_inch
        toppings_price = pizza.num_toppings() * Pizzeria.price_per_topping
        total_price = size_price + toppings_price
        return size_price, toppings_price, total_price
    def getReceipt(self):
        pizza = self.pizzas[-1]
        size_price, toppings_price, total_price = self.getPrice(pizza)
        print("Receipt\n")
        print(f"You ordered a {pizza.get_size()} inch pizza with {pizza.get_sauce()} sauce.\n")
        print(f"Toppings: {pizza.toppings}\n")
        print(f"Size Price: ${size_price}\n")
        print(f"Topping Price: ${toppings_price}\n")
        print(f"Total Price: ${total_price}")
        print("End of Receipt\n")
    def getNumberOfOrders(self):
        return self.orders
    
pizzeria = Pizzeria()

while True:
    prompt = "If you want to order a pizza type 'yes'. Type 'exit' to quit: "
    user_res = input(prompt).lower()
    if user_res == 'exit':
        break
    elif user_res in 'yes':
        pizzeria.placeOrder()
        pizzeria.getReceipt()

print(f"There were {pizzeria.getNumberOfOrders()} orders placed!")
            

        

        
        


        
    

    

    




        
