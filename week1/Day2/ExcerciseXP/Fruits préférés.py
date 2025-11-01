fruits = input("Entrez vos fruits préférés  : ")
liste_fruits = fruits.split()
fruit = input("Entrez le nom d'un fruit : ")
if fruit in liste_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
