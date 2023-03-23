import calendar

# define a function to display calendar for a given month and year
def display_calendar(year, month):
    print(calendar.month(year, month))

# define a function to add a task to the planner
def add_task(planner):
    task = input("Enter task: ")
    date = input("Enter date (YYYY-MM-DD): ")
    if date in planner:
        planner[date].append(task)
    else:
        planner[date] = [task]

# define a function to view tasks for a specific date
def view_tasks(planner):
    date = input("Enter date (YYYY-MM-DD): ")
    if date in planner:
        print("Tasks for", date)
        for task in planner[date]:
            print("- ", task)
    else:
        print("No tasks for", date)

# initialize an empty planner dictionary
planner = {}

# main loop for the planner
while True:
    print("Personal Planner")
    print("1. View Calendar")
    print("2. Add Task")
    print("3. View Tasks")
    print("4. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        year = int(input("Enter year: "))
        month = int(input("Enter month: "))
        display_calendar(year, month)
    elif choice == "2":
        add_task(planner)
    elif choice == "3":
        view_tasks(planner)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
