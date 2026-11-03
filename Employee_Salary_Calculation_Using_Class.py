
# Employee Salary Calculation

class Employee:

    def __init__(self, emp_id, name, basic_pay):
        self.emp_id = emp_id
        self.name = name
        self.basic_pay = basic_pay

    # Method to calculate gross salary
    def calculate_salary(self):
        hra = self.basic_pay * 0.20
        da = self.basic_pay * 0.10
        gross = self.basic_pay + hra + da

        print("\n===== EMPLOYEE SALARY DETAILS =====")
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Basic Pay:", self.basic_pay)
        print("HRA (20%):", hra)
        print("DA (10%):", da)
        print("Gross Salary:", gross)


# Get employee details
emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
basic_pay = float(input("Enter Basic Pay: "))

# Create object
emp = Employee(emp_id, name, basic_pay)

# Display salary details
emp.calculate_salary()
