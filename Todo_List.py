todo_list=[]

while True :
  print("---Welcome to TODO List---")
  print("1.View Tasks")
  print("2.Add Task")
  print("3.Update Task")
  print("4.Delete Task")
  print("5.Exit")
  choice = input("Enter the choice here :")
  if choice =="1" :
   if not todo_list:
    print("Empty Todo List ")
   else:
    print("\n Your tasks ")
    for index,task in enumerate(todo_list,start=1):
      print(f"{index}.{task}")

  elif choice =="2":
    task = input("Add new task\n")
    todo_list.append(task)
    print("Task added successfully ")

  elif choice =="3":
    if not todo_list:
      print("Empty Todo List ")
    else:
      for index,task in enumerate(todo_list,start=1):
        print(f"{index}.{task}")
      index = int(input("Enter the task index number to update : "))-1
      if 0<=index<len(todo_list):
        new_task =input("Enter the new task here\n")
        todo_list[index]=new_task
        print("Task updated successfully")
      else:
        print("Invalid index number")
  
  elif choice == "4":
    if not todo_list:
      print("Empty Todo List")
    else:
      for index,task in enumerate(todo_list,start=1):
        print(f"{index}.{task}")
      index = int(input("Enter the task index number to delete : "))-1
      if 0<=index<len(todo_list):
        removed = todo_list.pop(index)
        print(f"Task removed deleted successfully\n")
      else:
        print("Invalid task number")

  elif choice == "5":
    print("Exiting....\n")
    break

  else:
    print("Invalid choice.please try again\n")
    print("Please choose option from choices provided from 1 to 5 only")

