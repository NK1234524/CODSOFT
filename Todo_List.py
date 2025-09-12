Todo_list = []
while True:
    print("--Todo List--")
    print("Choose from the options provided velow")
    print("1.Vew List")
    print("2.Add a task")
    print("3.Update a task")
    print("4.Delete a task")
    print("5.Exit")
    choice = input("Enter the option\n")
    if choice=="1":
      if not Todo_list:
         print("Empty todo list")
      else:
        print("Here is your Todo List")
        for index,task in enumerate(Todo_list,start=1):
           print(f"{index}.{task}")
      
    elif choice=="2":
      print("Add a task")
      task = input("Enter a task\n")
      Todo_list.append(task)
      print("Task added successfully")
    elif choice=="3":
      print("Update a task in the todo List")
      if not Todo_list:
         print("Empty Todo List")
      else:
         for index,task in enumerate(Todo_list,start=1 ):
            if 0<=index<len(Todo_list):
             index = int(input("Enter the index value here"))-1
             newtask = input("Enter the updated task at %d",index)
             Todo_list[index]=newtask
             print("Task Updated")
            else:
               print("Wrong index number")
    elif choice=="4":
       print("Delete the task in the todo List")
       if not Todo_list:
          print("Empty Todo List")
       else:
          for index,task in enumerate(Todo_list,start=1):
             if 0<=index<len(Todo_list):
                index=int(input("Enter the index value here"))-1
                removed = Todo_list.pop(index)
                print("Task deleted")
             else :
                print("Wrong index number")
    elif choice=="5":
       print("EXITING...")
       break
    else:
       print("Wrong choice...")

                              
            
               
            
