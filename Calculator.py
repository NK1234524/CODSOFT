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
      more = input("Do you want to add more numbers? (yes/no): ")
      if more.lower() != "yes":
       break
  elif choice=="2":
    print("Welcome to subtraction")
    while True:
      num1 = int(input("Enter the number 1 : "))
      num2 = int(input("Enter the number 2 : "))
      sub = num1-num2
      if sub<0 :
       print("negative integer : ",num1-num2)
      else:
        print("positive integer : ",sub)
      more = input("Do you want to subtract more numbers? (yes/no): ")
      if more.lower() != "yes":
        break
  elif choice=="3":
    print("Welcome to multiplication")
    while True:
      num1 = int(input("Enter the number"))
      num2 = int(input("Enter the number"))
      print(num1*num2)
      more = input("Do you want to multiply more numbers? (yes/no): ")
      if more.lower() != "yes":
       break
  elif choice=="4":
    print("Welcome to division")
    while True:
      num1 = int(input("Enter the number"))
      num2 = int(input("Enter the number"))
      print(num1/num2)
      more = input("Do you want to divide more numbers? (yes/no): ")
      if more.lower() != "yes":
        break
      if num2==0:
        print("Infinity")
      break