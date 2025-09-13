while True:
  print("-----WELCOME TO CALCULATOR----")
  print("1.ADDITION \n")
  print("2.SUBTRACTION \n")
  print("3.MULTIPLICATION \n")
  print("4.DIVISION \n")
  print("5.EXIT \n")

  choice = input("Enter the choice : \n")

  if choice=="1":
    print("Welcome to addition")
    while True:
      num1 = int(input("Enter the number"))
      num2 = int(input("Enter the number"))
      print(num1+num2)
      break
  elif choice=="2":
    print("Welcome to subtraction")
    while True:
      num1 = int(input("Enter the number"))
      num2 = int(input("Enter the number"))
      print(num1-num2)
      if num1<num2:
        print("Negative integer: ",num1-num2)
      break
  elif choice=="3":
    print("Welcome to multiplication")
    while True:
      num1 = int(input("Enter the number"))
      num2 = int(input("Enter the number"))
      print(num1*num2)
      break
  elif choice=="4":
    print("Welcome to division")
    while True:
      num1 = int(input("Enter the number"))
      num2 = int(input("Enter the number"))
      print(num1/num2)
      if num2==0:
        print("Infinity")
      break
  elif choice=="5" :
    print("Exit")
    break
  else:
    print("Invalid choice")
      