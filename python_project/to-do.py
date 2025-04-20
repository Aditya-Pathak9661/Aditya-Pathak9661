'''
this is a to-do list , which help us in daily life
'''

def task():
    tasks = []
    print("...Welcome to the Task Management App...")

    total_task =int(input("enter your task number: "))
    for i in range(1, total_task+1):
        task_name = input(f"enter your task{i} = ")
        tasks.append(task_name)
    print(f"today's tasks are \n {tasks}")

    while True:
        operation = int(input("enter 1-add \n2-update \n3-delete \n4-view \n5-exit/stop \n : "))

        if operation == 1:
            add = input("enter task you want to add= ")
            tasks.append(add)
            print(f"task {add} has been succesfully added...")
        
        elif operation == 2:
            update_val = input("enter the task name you want to update = ")
            if update_val in tasks:
                up = input("enter new task =")
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"tasks update{up}")
        elif operation == 3:
            del_val = input("which task you want to delete: ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"tasks delete{del_val}")
        elif operation == 4:
            print(f"total task = {tasks}")
        elif operation == 5:
            print("closing the program ...")
            break
        else:
            print(f"invalid {operation} input ")

task()