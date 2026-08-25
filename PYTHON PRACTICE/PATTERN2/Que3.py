# Question 18 — Student Marks
# Problem Description
# A school records marks obtained by different students. The program should store the total marks of each student and identify the student with the highest marks.
# Function 1
# Function Name: record_marks

# Parameters:
# student_name, marks, markboard
# Requirements:
# Convert the student name to uppercase before storing it.
# If marks <= 0, do not add the marks to the dictionary.
# If the student already exists in the dictionary, add the new marks to the student's existing marks.
# If the student does not exist, create a new entry.
# Return the updated dictionary.

# Function 2
# Function Name: find_top_student

# Parameter:
# markboard

# Requirements:
# Return the student who has the highest total marks.
# If the dictionary is empty, return:
# ("", 0)
# If two or more students have the same maximum marks, the first inserted student wins.

markboard = {}
def record_marks(student_name,marks,markboard):
    student_name = student_name.lower()
    if marks <=0:
        return markboard
    if student_name in markboard:
        markboard[student_name]+=marks
    else:
        markboard[student_name]=marks
    return markboard

def find_top_student(markboard):
    if not markboard:
        return("",0)
    top_student = max(markboard, key = markboard.get)
    return top_student,markboard[top_student]

def main():

    markboard = {}

    n = int(input("Enter number of students: "))

    print("Enter student marks:")

    for i in range(n):

        name = input("Enter student name: ")

        marks = int(
            input(f"Enter {name}'s marks: ")
        )

        markboard = record_marks(
            name,
            marks,
            markboard
        )

    print("\nMarks Summary:")

    for name, marks in markboard.items():
        print(f"{name}:{marks}")

    name, marks = find_top_student(markboard)

    print("\nTop Student")
    print(f"{name}:{marks}")


if __name__ == "__main__":
    main()