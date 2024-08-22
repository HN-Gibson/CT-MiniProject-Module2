class UserInputEmpty(Exception):
    pass

class CommandNotFound(Exception):
    pass

def add_task(new_task):
    status="Incomplete"
    to_do_list.append(new_task + ": " + status)
    return print(f"{new_task} added!")

def view_tasks(list):
    return print ("Your To-Do List:",*list,sep="\n")

def complete_task(selected_task):
    for task in to_do_list:
        if selected_task in task:
            selected_task=task.replace("Incomplete","Complete")
            index=to_do_list.index(task)
            to_do_list[index]=selected_task
            return print(selected_task + "! Way to go!")
        else:
            return print("Task not in list.")

def delete_task(selected_task):
    for task in to_do_list:
        if selected_task in task:
            index=to_do_list.index(selected_task)
            to_do_list.pop(index)
            return print (f"{selected_task} removed from the list!")
        else:
            return print("Task not in list.")


menu=("""
      Welcome to the To-Do List App!

        Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit
      
      """)
to_do_list = []
print(menu)

while True:
    try:    
        feature_request=input("Which menu option would you like to perform?\nPlease enter menu option as it appears above: ").lower            
        if feature_request() == "quit":
            break

        elif feature_request() == "add a task":
            new_task=input("What task would you like to add: ")
            add_task(new_task)

        elif feature_request() == "view tasks":
            view_tasks(to_do_list)

        elif feature_request() == "mark a task as complete":
            task_to_complete=input("What task did you complete? ")
            complete_task(task_to_complete)

        elif feature_request() == "delete a task":
            task_to_remove=input("What task would you like to remove? ")
            delete_task(task_to_remove)

        elif feature_request() == "":
            raise UserInputEmpty        
        else:
            raise CommandNotFound
    except UserInputEmpty:
        print("Input was empty. Please enter a command.")
        print(menu)
    except CommandNotFound:
        print("Input doesn't match available commands.\nPlease enter command from menu.")
        print(menu)
    else:
        print("Please make another command.")                   
    finally:
        print("Thank You for using my program!")

print("Your To-Do List:",*to_do_list,sep="\n")