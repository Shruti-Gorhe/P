# Question 16 — Sales Monitor
# Problem Description

# A company records sales made by employees during different sessions of the day.

# Function 1
# record_sales(employee_name, sales, salesboard)

# Requirements:
# Convert employee name to uppercase.
# If sales <= 0, do not add it.
# If employee already exists, add sales to existing sales.
# Otherwise create a new entry.
# Return updated dictionary.

# Function 2
# find_top_performer(salesboard)
# Requirements:
# Return employee with highest sales.
# Empty dictionary → ("", 0).
# If tie, first inserted employee wins.

def record_sales(employee_name, sales, salesboard):
    employee_name = employee_name.upper()
    if sales<=0:
        return salesboard
    if employee_name in salesboard:
        salesboard[employee_name]+= sales
    else:
        salesboard[employee_name]=sales
    return salesboard


def find_top_performer(salesboard):
    if not salesboard:
        return("",0)
    else:
        top_employee = max(salesboard, key = salesboard.get)
        return top_employee, salesboard[top_employee]

def main():

    salesboard = {}

    num_employees_morning = int(
        input("Enter the number of employees for the morning session: ")
    )

    print("Enter sales for the morning session:")

    for i in range(num_employees_morning):

        employee_name = input("Enter employee name: ")

        sales = int(
            input(f"Enter {employee_name}'s sales: ")
        )

        salesboard = record_sales(
            employee_name,
            sales,
            salesboard
        )

    print("\nMorning Session Sales:")

    for employee, sales in salesboard.items():
        print(f"{employee}:{sales}")

    num_employees_afternoon = int(
        input("\nEnter the number of employees for the afternoon session: ")
    )

    print("Enter sales for the afternoon session:")

    for i in range(num_employees_afternoon):

        employee_name = input("Enter employee name: ")

        sales = int(
            input(f"Enter {employee_name}'s sales: ")
        )

        salesboard = record_sales(
            employee_name,
            sales,
            salesboard
        )

    print("\nAfternoon Session Sales:")

    for employee, sales in salesboard.items():
        print(f"{employee}:{sales}")

    top_employee, top_sales = find_top_performer(salesboard)

    print("\nTop Performer")
    print(f"{top_employee}:{top_sales}")


if __name__ == "__main__":
    main()