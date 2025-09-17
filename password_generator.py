import random
import string
print("--Welcome to password generator--")

letters=''.join(random.choices(string.ascii_letters,k=6))


print("Here is your password generator: ",letters)
while True:
 print("1.Change")
 print("2.Exit ")
 choice = input("choose options : ")
 if (choice == "1"):
    letter=''.join(random.choices(string.ascii_letters,k=6))
    print("New password ", letter)
 elif(choice=="2"):
    print("Exiting...")
    break
 else:
    print("Not possible")