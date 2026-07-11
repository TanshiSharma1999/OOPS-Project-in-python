class Employee:

    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_details(self):
        print("\n------ Employee Details ------")
        print(f"Employee ID : {self.emp_id}")
        print(f"Name        : {self.name}")
        print(f"Department  : {self.department}")
        print(f"Salary      : ₹{self.salary:.2f}")

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    def annual_salary(self):
        return self.salary * 12

    def is_high_earner(self):
        return self.salary > 100000

    def change_department(self, new_department):
        self.department = new_department


# ---------------- MAIN PROGRAM ----------------

employees = []

num = int(input("How many employees? "))

for i in range(num):
    print(f"\nEnter details for Employee {i + 1}")

    emp_id = int(input("Employee ID: "))
    name = input("Name: ")
    department = input("Department: ")
    salary = float(input("Salary: "))

    emp = Employee(emp_id, name, department, salary)
    employees.append(emp)


# ---------------- DISPLAY DETAILS ----------------

for emp in employees:

    emp.display_details()

    percent = float(input("\nIncrease salary by (%): "))
    emp.increase_salary(percent)

    print("\nUpdated Employee Details")
    emp.display_details()

    print(f"Annual Salary : ₹{emp.annual_salary():.2f}")

    if emp.is_high_earner():
        print("High Earner : Yes")
    else:
        print("High Earner : No")

    choice = input("Change department? (yes/no): ").lower()

    if choice == "yes":
        new_department = input("Enter new department: ")
        emp.change_department(new_department)

        print("\nDepartment Updated")
        emp.display_details()

    print("-" * 40)