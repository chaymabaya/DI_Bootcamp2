names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_names = input("enter votre nom : ")
if user_names in names :
    index = names .index(user_names)
    print("we should be printing the index" , index )
else:
    print("we should be not printing the index")