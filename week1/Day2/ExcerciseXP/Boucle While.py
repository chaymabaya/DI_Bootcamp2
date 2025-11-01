while True :
    name = input(" Enter your name : ")
    if name.isalpha() and len(name) >= 3:
      print ("thank you")
      break
    else:
      print ("give the correct name ")
      break