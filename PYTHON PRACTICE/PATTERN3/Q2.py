# Question — Book Inventory and Billing
# Problem Description:

# Create a program to maintain a list of books available in a bookstore and calculate the total amount for a requested quantity of a book.

# You need to write 2 functions.

# Function 1: add_book_details()

# Parameters:

# book_name
# rate_per_copy
# quantity

# All three parameters are given as strings.

# Requirements:

# Add the book details to a single list.
# Each book's details should be stored as a separate list.
# Convert rate_per_copy and quantity from string to integer before adding them to the list.
# The details should be stored in the following format:
# [book_name, rate_per_copy, quantity]

# Function 2: calculate_total_amount()

# Parameter:
# input_string
# The input is a string containing the book name and required quantity separated by a comma.

# Example:
# Harry potter,3
# Requirements:
# Split the input string using a comma.
# Extract the book name and required quantity.
# Search for the book in the list.
# Check whether the required quantity is:
# Less than the available quantity
# Equal to the available quantity
# More than the available quantity
# If the required quantity is less than or equal to the available quantity:
# Calculate the total amount using:
# rate_per_copy × required_quantity
# Return the calculated total amount.
# If the book is not present in the list, return:
# Book is not in the inventory



books = []
def add_book_details(book_name, rate_per_copy, quantity):
    rate_per_copy = int(rate_per_copy)
    quantity = int(quantity)

    book = [book_name, rate_per_copy, quantity]
    books.append(book)

    return books


def calculate_total_amount(input_string):
    data = input_string.split(',')

    book_name = data[0].strip()
    req_quantity = int(data[1].strip())

    for book in books:
        if book[0].lower() == book_name.lower():

            if req_quantity <= book[2]:
                total_amount = book[1] * req_quantity
                return total_amount

            else:
                return "Required quantity is not available"

    return "Book is not in the inventory"


def main():

    while True:

        choice = input("Choose a method(add/calculate): ").lower()

        if choice == "add":

            n = int(input("Enter no. of books: "))

            for i in range(n):
                details = input("Enter the details of book: ")

                data = details.split(',')

                book_name = data[0].strip()
                rate = data[1].strip()
                quantity = data[2].strip()

                add_book_details(book_name, rate, quantity)

        elif choice == "calculate":

            input_string = input(
                "Enter the book and quantity(separated by comma): "
            )

            result = calculate_total_amount(input_string)

            if isinstance(result, int):
                print("Total amount:", result)
            else:
                print(result)

            break


if __name__ == "__main__":
    main()