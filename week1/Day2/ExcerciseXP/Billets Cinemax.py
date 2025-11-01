age_input = input ("what is your age ? ")
age = int(age_input)
if age < 3:
        price = 0
        print("Billet gratuit pour cet enfant.")
elif age <= 12:
        price = 10
        print("Billet à 10 $.")
else:
        price = 15
        print("Billet à 15 $.")
total = 0
total += price
print ("Prix total à payer" ,total)
