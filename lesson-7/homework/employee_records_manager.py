class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = float(salary)  # Ensures numeric sorting

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

    def to_line(self):
        return f"{self.employee_id}|{self.name}|{self.position}|{self.salary}"

    @staticmethod
    def from_line(line):
        try:
            parts = line.strip().split("|")
            if len(parts) != 4:
                raise ValueError("Invalid line format.")
            return Employee(parts[0], parts[1], parts[2], parts[3])
        except Exception as e:
            raise ValueError(f"Failed to parse employee: {e}")

class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename
        try:
            open(self.filename, "a").close()
        except Exception as e:
            raise Exception(f"Error initializing file: {e}")

    def load_employees(self):
        try:
            with open(self.filename, "r") as file:
                return [Employee.from_line(line) for line in file if line.strip()]
        except FileNotFoundError:
            return []
        except Exception as e:
            raise Exception(f"Error loading employees: {e}")

    def save_employees(self, employees):
        try:
            with open(self.filename, "w") as file:
                for emp in employees:
                    file.write(emp.to_line() + "\n")
        except Exception as e:
            raise Exception(f"Error saving employees: {e}")

    def add_employee(self):
        try:
            employee_id = input("Enter Employee ID: ").strip()
            if self.find_employee(employee_id):
                print("Employee ID already exists. Please use a unique ID.")
                return
            name = input("Enter Name: ").strip()
            position = input("Enter Position: ").strip()
            salary = input("Enter Salary: ").strip()
            if not salary.replace('.', '', 1).isdigit():
                raise ValueError("Salary must be a number.")
            new_emp = Employee(employee_id, name, position, salary)
            with open(self.filename, "a") as file:
                file.write(new_emp.to_line() + "\n")
            print("Employee added successfully!")
        except Exception as e:
            print(f"Failed to add employee: {e}")

    def view_all_employees(self):
        try:
            employees = self.load_employees()
            if not employees:
                print("No records found.")
                return
            choice = input("Sort by (1) Name or (2) Salary or (3) No sort: ").strip()
            if choice == '1':
                employees.sort(key=lambda e: e.name)
            elif choice == '2':
                employees.sort(key=lambda e: e.salary)
            print("Employee Records:")
            for emp in employees:
                print(emp)
        except Exception as e:
            print(f"Error viewing employees: {e}")

    def find_employee(self, employee_id):
        try:
            employees = self.load_employees()
            for emp in employees:
                if emp.employee_id == employee_id:
                    return emp
            return None
        except Exception as e:
            print(f"Error searching for employee: {e}")
            return None

    def search_employee(self):
        try:
            employee_id = input("Enter Employee ID to search: ").strip()
            emp = self.find_employee(employee_id)
            if emp:
                print("Employee Found:")
                print(emp)
            else:
                print("Employee not found.")
        except Exception as e:
            print(f"Error: {e}")

    def update_employee(self):
        try:
            employee_id = input("Enter Employee ID to update: ").strip()
            employees = self.load_employees()
            found = False
            for i, emp in enumerate(employees):
                if emp.employee_id == employee_id:
                    found = True
                    print(f"Current info: {emp}")
                    name = input("Enter new name (leave blank to keep current): ").strip()
                    position = input("Enter new position: ").strip()
                    salary = input("Enter new salary: ").strip()
                    if name:
                        emp.name = name
                    if position:
                        emp.position = position
                    if salary:
                        if not salary.replace('.', '', 1).isdigit():
                            raise ValueError("Salary must be numeric.")
                        emp.salary = float(salary)
                    employees[i] = emp
                    break
            if found:
                self.save_employees(employees)
                print("Employee updated successfully.")
            else:
                print("Employee not found.")
        except Exception as e:
            print(f"Error updating employee: {e}")

    def delete_employee(self):
        try:
            employee_id = input("Enter Employee ID to delete: ").strip()
            employees = self.load_employees()
            new_employees = [emp for emp in employees if emp.employee_id != employee_id]
            if len(employees) == len(new_employees):
                print("Employee ID not found.")
                return
            self.save_employees(new_employees)
            print("Employee deleted successfully.")
        except Exception as e:
            print(f"Error deleting employee: {e}")

    def run(self):
        while True:
            print("\n--- Employee Records Manager ---")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.view_all_employees()
            elif choice == '3':
                self.search_employee()
            elif choice == '4':
                self.update_employee()
            elif choice == '5':
                self.delete_employee()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")
if __name__ == "__main__":
    manager = EmployeeManager()
    manager.run()
