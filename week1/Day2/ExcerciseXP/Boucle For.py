numbers = range (1 , 21 )
print ("tous les nombres de 1 à 20 :")
for number in numbers:
    print(number)
print ("tous les nombres de 1 à 20 dont l'indice est pair :")
for index , value in enumerate(numbers):
    if index % 2 == 0 :
        print (value)