# Question 5 — Course Management
# Problem Description
# An educational platform stores information about different courses. Each course has a course name, category, duration, and fee.
# The program should allow the user to add course details and then find courses based on their category and maximum fee.
# Functional Requirements

# 1. Add Course Details
# Function Name: add_course_details
# Parameters:
# course_name
# category
# duration
# fee
# courses

# The function should:
# Create a tuple containing the course name, category, duration, and fee.
# Add the tuple to the courses list.
# Return the updated list.

# 2. Find Courses
# Function Name: find_courses
# Parameters:
# category
# maximum_fee
# courses

# The function should:
# Find courses belonging to the specified category.
# Category comparison should be case-insensitive.
# Find courses whose fee is less than or equal to the given maximum fee.
# Return a list containing all matching course tuples.
# If no course matches the given conditions, return an empty list.

courses=[]
def add_course_details(course_name,category,duration,fee,courses):
    course =(course_name,category,duration,fee)
    courses.append(course)
    return courses


def find_courses(category,maximum_fee,courses):
    result = []
    for course in courses:
        if category.lower() == course[1].lower() and course[3] <= maximum_fee:
            result.append(course)
    return result

def main():
    courses = []

    n = int(input("Enter number of courses: "))

    for i in range(n):
        course_name = input("Enter course name: ")
        category = input("Enter category: ")
        duration = int(input("Enter duration: "))
        fee = int(input("Enter fee: "))

        add_course_details(course_name, category, duration, fee, courses)

    category = input("Enter category: ")
    maximum_fee = int(input("Enter maximum fee: "))

    result = find_courses(category, maximum_fee, courses)

    print("Courses:")

    for course in result:
        print(course)


if __name__ == "__main__":
    main()