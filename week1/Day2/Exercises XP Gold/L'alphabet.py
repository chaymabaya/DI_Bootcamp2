alphabet = "abcdefghijklmnopqrstuvwxyz"
for lettre in alphabet:
    print(lettre)
    voyelles = "aeiouy"
    if lettre in voyelles:
       print ("la lettre " , lettre , "est une voyelle")
    else:
       print ("la lettre ", lettre ,"est une consonne")