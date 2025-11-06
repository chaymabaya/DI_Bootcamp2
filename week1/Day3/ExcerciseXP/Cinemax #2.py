family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total = 0
for name , age in family.items() :
    if age < 3 :
        price = 0
    elif age >= 12 :
        price = 10
    else:
        price = 15
    print(f'{name} doit payes {price}')
    total += price
print (f"le prix total est : {total}")

