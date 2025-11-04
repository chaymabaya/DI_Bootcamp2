active = True
toppings = []
while active:
    topping  = input(" entrer  les ingrédients pour votre pizza : ")
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"Adding {topping} to your pizza.")
        toppings.append(topping)
base_price = 10
topping_adds = 20
total_price = base_price + topping_adds * len(toppings)
print(toppings)
print("prix total " , total_price)