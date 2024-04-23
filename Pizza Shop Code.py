# PIZZA SHOP

class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_menu(self):
        return f"{self.name} : ${self.price}"

class OrderItem:
    def __init__ (self, pizza, quantity):
        self.pizza = pizza
        self.quantity = quantity

    def get_cost(self):
        return self.pizza.get.price() * self.quantity
    
class Order:
    def __init__(self):
        self.items = []
    
    def add_item(self, order_item):
        self.items.append(order_item)
    
    def get_total_cost(self):
        total_cost = 0
        for item in self.items:
            total_cost += item.get_cost()
        return total_cost

class LoyaltyProgram:
    def __init__(self):
        self.discounts = []

    def check_loyalty(self):
        while True:
            loyalty_check = input("Are you a loyalty card member?: ")
            if loyalty_check.lower() == "yes":
                print("Please enter your username")
                self.discounts.append(Discount(5))
            elif loyalty_check.lower() == "no":
                break
            else:
                print("Please input either 'Yes' or 'No'\n")

class Discount:
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, cost):
        return cost - (cost * (self.percentage / 100))
    
        


# Pizza Menu with Names and Prices
p1 = Pizza("Pepperoni", 21.00)
p2 = Pizza("Chicken Supreme", 23.50)
p3 = Pizza("BBQ Meatlovers", 25.50)
p4 = Pizza("Veg Supreme", 22.50)
p5 = Pizza("Hawaiian", 19.00)
p6 = Pizza("Margherita", 18.50)

PizzaMenu = {
    "Pepperoni" : 21.00,
    "Chicken Supreme" : 23.50,
    "BBQ Meatlovers" : 25.50,
    "Veg Supreme" : 22.50,
    "Hawaiian" : 19.00,
    "Margherita" : 18.50
}

# List of Pizza Objects
pizzas = [p1, p2, p3, p4, p5, p6]
pizzaid= [1, 2, 3, 4, 5, 6]

# Print Menu
print("\nPapaPizza Menu:\n")
for pizza in pizzas:
    print(f"{pizza.display_menu()}")


# Take Orders From The Menu
order = []
pizza_total_cost = 0

while True:
    pizza_choice = input("Enter the name of the pizza you would like (or 'done' to finish): ")

    if pizza_choice.lower() == "done":
        break

    if pizza_choice in PizzaMenu:
        pizza_quantity = int(input("Quantity of this pizza: "))
        pizza_price = PizzaMenu[pizza_choice]
        cost = pizza_quantity * pizza_price
        pizza_total_cost += cost
    
    # Keep track of pizzas ordered 

        order_item = {"pizza": pizza_choice, "quantity": pizza_quantity, "price": pizza_quantity, "cost": cost}
        order.append(order_item)

    # Display Current Cost

        print(f"Total Cost: ${pizza_total_cost}")

    else:
        print(f"Sorry, '{pizza_choice} is not on the menu. Please try again.")

if order: 
    print("\nYour Order is:")
    for item in order:
        print(f"{item['quantity']}x {item['pizza']}: ${item['cost']:.2f}")
    print(f"\nTotal: ${pizza_total_cost:.2f}")
else:
    print("\nYou did not order any pizzas")

# Delivery Fee

delivery_total_cost = 0
discount = 0
discounted_cost = 0
 
while True:
    deliver = input("Would you like delivery or pickup? (delivery is $8): ")
    if deliver.lower() == "yes":
        delivery_total_cost = pizza_total_cost + 8
        print(f"Delivery cost has been added to your total it is now: ${delivery_total_cost}")
        break
    elif deliver.lower() == "no":
        break
    else:
        print("Please input either 'Yes' or 'No'\n")

# Discount and Loyalty Member Check
discounts = ["None"]
while True:
    if pizza_total_cost > 100:
        discounts.remove("None")
        print("As your order exceeds $100, you are eligible for a 5% discount! (this means a loyalty card login is not required)\n")
        discounts.append("5%")
        discount = delivery_total_cost * 0.05
        discounted_cost = delivery_total_cost - discount
        break
    else:
        loyalty = LoyaltyProgram()
        loyalty.check_loyalty()
        break

# Provide Full Costs Information

print("Your Costs Include:")
print(f"Price of Menu Items: ${pizza_total_cost}")
print("Price of Delivery: $8")
print(f"Discounts: - {','.join(discounts)} (${discount})")
print(f"Goods and Services Tax (GST): + 10% (${discounted_cost * 0.10})\n")

totalbill = discounted_cost + delivery_total_cost * 0.10

print(f"Your total cost is: ${totalbill}")




