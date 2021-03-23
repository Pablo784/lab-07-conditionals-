firstnum = input("Give me a number, any number!")
secondnum = input("Excellent, and give me another number!")
operation = input("And what operation do you want? (mul/div/mod)")

if (operation == "mul"):
  print(firstnum * secondnum)

if(operation == "div"):
  print(firstnum/secondnum)

if (operation == "mod"):
  print(firstnum % secondnum)

else:
  print("***invalid operation!***")
