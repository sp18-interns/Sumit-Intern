available_pizzas = ['SP18']
pizza_base = ['Wheat', 'Maida']
is_veg = ['Veg', 'nonveg']
available_toppings = ['mushroom', 'onions', 'capsicum', 'extra cheese']
pizza_prices = {'pune': 5, 'delhi': 7, 'bhopali': 6}
topping_prices = {'mushroom':1, 'onions': 2, 'sev':3, 'tamatar':4}
pizza_size = ['small', 'medium', 'large']

print("Enter the pizza ")
order_pizza = True
while order_pizza:    
    print("Please choose a pizza: ")
    print()
    for pizzas in available_pizzas:
        print(pizzas)
        print()
    while True:
        pizza = input("which pizza would you like to order?")
        if pizza in available_pizzas:
            print(f"You have ordered a {pizza}.")
            sub_total.append(pizza_prices[pizza])
            break
        if pizza not in available_pizzas:
            print(f"I am sorry, we currently do not have {pizza}.")