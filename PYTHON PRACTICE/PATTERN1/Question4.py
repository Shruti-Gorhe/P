# Question 4 — Employee Records
# Problem Description

# An organization stores information about its employees. Each employee has a name, department, years of experience, and salary.

# The program should allow the user to add employee details and then find employees based on their department and minimum years of experience.

# Functional Requirements
# 1. Add Employee Details
# Function Name: add_employee_details
# Parameters:
# name
# department
# experience
# salary

# The function should:
# Create a tuple containing the employee name, department, experience, and salary.
# Add the tuple to the employees list.
# Return the updated list.
# For example:

# Input:

# Name = Rahul
# Department = IT
# Experience = 4
# Salary = 60000

# Stored tuple:
# ("Rahul", "IT", 4, 60000)

# 2. Find Employees
# Function Name: find_employees
# Parameters:
# department
# minimum_experience
# employees

# The function should:
# Find employees belonging to the specified department.
# Department comparison should be case-insensitive.
# Find employees whose experience is greater than or equal to the given minimum experience.
# Return a list containing all matching employee tuples.
# If no employee matches the given conditions, return an empty list.

employees = []
def add_employee_details(name,department,experience,salary,employees):
    employee = (name,department,experience,salary)
    employees.append(employee)
    return employees


def find_employees(department,minimum_experience,employees):
    result = []
    for employee in employees:
        if department.lower() == employee[1].lower() and employee[2] >=minimum_experience:
            result.append(employee)
    return result


def main():
    employees = []

    n = int(input("Enter number of employees: "))

    for i in range(n):
        name = input("Enter employee name: ")
        department = input("Enter department: ")
        experience = int(input("Enter experience: "))
        salary = int(input("Enter salary: "))

        add_employee_details(name, department, experience, salary,employees)

    department = input("Enter department: ")
    minimum_experience = int(input("Enter minimum experience: "))

    print("Employees:")

    result = find_employees(department, minimum_experience, employees)

    for employee in result:
        print(employee)

if __name__ == "__main__":
    main()
    
    
