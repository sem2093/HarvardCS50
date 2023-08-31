def main():
    print("Welcome to My To-Do List App!")
    tasks = []
    
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter a new task: ")
            tasks.append(task)
            function_1()
        elif choice == '2':
            print("\n--- Your Tasks ---")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        elif choice == '3':
            function_n()
            break
        else:
            function_2()

def function_1():
    print("Task added successfully!")
    return 
def function_2():
    print("Please Type '1','2',or'3'")
    return
def function_n():
    print("Goodbye!")
    return
if __name__ == "__main__":
    main()

