# Question 38 — Student Records
# Problem Description:

# Create a program to maintain student records and find all students belonging to a particular department.

# You need to write 2 functions.

# Function 1: add_student_details()

# Parameter:

# add_detail

# The input string contains:

# student_id,student_name,department,year

# Example:

# 101,Riya,Computer Science,2026

# Requirements:

# Split the input string using a comma.
# Remove unnecessary spaces from each value.
# The input must contain exactly 4 values.
# Store each student's details as a separate list inside the students list.
# Add the department to the departments set.
# Return the students list and departments set.
# If the input does not contain exactly 4 values, do not add the record.

# Each student should be stored as:

# [student_id, student_name, department, year]


# Function 2: find_by_department()

# Parameter:

# department

# Requirements:

# Search through the students list.
# Department comparison should be case-insensitive.
# Return all student records belonging to the given department.
# If no student is found, return an empty list.



def add_student_details(add_detail):
    l1 = add_detail.split(",")
    l2 = [i.strip()for i in l1]
    
    if len(l2)!=4:
        return students,departments
    
    students.append(l2)
    return students,departments


def find_by_department(department):
    result = []
    
    for student in students:
        if department.lower() == student[3].lower():
            result.append(student)
    return result

def main():

    global students, departments

    students = []
    departments = set()

    n = int(input("Enter no. of students: "))

    for i in range(n):

        add_detail = input("Enter student details: ")

        students, departments = add_student_details(add_detail)

    print("Student Records:")
    print(students)

    print("Departments:")
    print(departments)

    department = input("Enter department to search: ")

    result = find_by_department(department)

    print("Students in department:")
    print(result)


if __name__ == "__main__":
    main()

    
    
    
    