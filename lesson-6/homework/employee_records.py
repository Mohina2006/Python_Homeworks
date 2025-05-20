import os

def display_menu():
    print("\nEmployee Records Manager")
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")

def add_employee():
    print("\nAdd New Employee")
    emp_id = input("Enter Employee ID: ")
    
    # Check if employee ID already exists
    with open("employees.txt", "r") as file:
        for line in file:
            if line.startswith(emp_id + ","):
                print("Employee ID already exists!")
                return
    
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")
    
    with open("employees.txt", "a") as file:
        file.write(f"{emp_id},{name},{position},{salary}\n")
    print("Employee record added successfully!")

def view_employees():
    print("\nAll Employee Records")
    print("ID\tName\t\tPosition\t\tSalary")
    print("-" * 60)
    
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                emp_id, name, position, salary = line.strip().split(",")
                print(f"{emp_id}\t{name}\t{position}\t\t{salary}")
    except FileNotFoundError:
        print("No employee records found. The file is empty or doesn't exist.")

def search_employee():
    emp_id = input("Enter employee ID to search: ")
    found = False
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    emp_id, name, position, salary = line.strip().split(",")
                    print("Employee found")
                    print(f"ID: {emp_id}")
                    print(f"Name: {name}")
                    print(f"Position: {position}")
                    print(f"Salary: {salary}")
                    found = True
                    break
    except FileNotFoundError:
        pass
    if not found:
        print("Employee not found")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    found = False
    employees = []
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    found = True
                    emp_id, name, position, salary = line.strip().split(",")
                    print("\nCurrent Employee Information:")
                    print(f"1. Name: {name}")
                    print(f"2. Position: {position}")
                    print(f"3. Salary: {salary}")
                    choice = input("\nWhat would you like to update? (1-3, or 'cancel'): ")
                    if choice.lower() == 'cancel':
                        return
                    if choice == '1':
                        name = input("Enter new name:")
                    elif choice == '2':
                        position = input("Enter new position")
                    elif choice == '3':
                        salary = input("Enter new salary")
                    else:
                        print("Invalid choice. No changes made. ")
                    employees.append(f"{emp_id},{name},{position},{salary}\n")
                else:
                    employees.append(line)
    except FileNotFoundError:
        print("No employee records found.")
        return
    if found:
        with open("employees.txt", "w") as file:
            file.writelines(employees)
        print("Employee record updated successfully!")
    else:
        print("Employee not found.")

def delete_employee():
    emp_id = input("\nEnter Employee ID to delete: ")
    found = False
    employees = []
    
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    found = True
                    # Don't add this line back (effectively deleting it)
                    emp_id, name, position, salary = line.strip().split(",")
                else:
                    employees.append(line)
    except FileNotFoundError:
        print("No employee records found.")
        return
    
    if found:
        with open("employees.txt", "w") as file:
            file.writelines(employees)
        print("Employee record deleted successfully!")
    else:
        print("Employee not found.")
def main():
    # Create the file if it doesn't exist
    if not os.path.exists("employees.txt"):
        open("employees.txt", "w").close()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()