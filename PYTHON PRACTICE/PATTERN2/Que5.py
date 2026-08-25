# Hotel Bookings
# Problem Description
# A hotel records the number of bookings handled by different employees. The program should store the total number of bookings handled by each employee and identify the employee with the highest number of bookings.

# Function 1
# Function Name: record_bookings

# Parameters:
# employee_name, bookings, bookingboard
# Requirements:
# Convert the employee name to uppercase before storing it.
# If bookings <= 0, do not add the bookings to the dictionary.
# If the employee already exists in the dictionary, add the new bookings to the employee's existing bookings.
# If the employee does not exist, create a new entry.
# Return the updated dictionary.


# Function 2
# Function Name: find_top_employee

# Parameter:
# bookingboard

# Requirements:
# Return the employee who has handled the highest number of bookings.
# If the dictionary is empty, return:
# ("", 0)
# If two or more employees have the same maximum number of bookings, the first inserted employee wins.

bookingboard={}
def record_bookings(employee_name,bookings,bookingboard):
    employee_name = employee_name.upper()
    if bookings<=0:
        return bookingboard
    if employee_name in bookingboard:
        bookingboard[employee_name]+=bookings
    else:
        bookingboard[employee_name]=bookings
    return bookingboard
    
    
def find_top_employee(bookingboard):
    if not bookingboard:
        return("",0)
    top_employee = max(bookingboard,key=bookingboard.get)
    return top_employee,bookingboard[top_employee]


def main():

    bookingboard = {}

    n = int(input("Enter number of employees: "))

    print("Enter employee bookings:")

    for i in range(n):

        name = input("Enter employee name: ")

        bookings = int(
            input(f"Enter {name}'s bookings: ")
        )

        bookingboard = record_bookings(
            name,
            bookings,
            bookingboard
        )

    print("\nBooking Summary:")

    for name, bookings in bookingboard.items():
        print(f"{name}:{bookings}")

    name, bookings = find_top_employee(bookingboard)

    print("\nTop Employee")
    print(f"{name}:{bookings}")


if __name__ == "__main__":
    main()