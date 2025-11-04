number = int (input("A number : "))
length = int (input("length : "))
multip = []
for i in range(1 , length + 1):
    multip.append(number * i)
print (multip)
