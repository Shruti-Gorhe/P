# Question 33 — Grocery Store
# Problem Description:
# Create a program to maintain a list of grocery items and calculate the total cost of a requested quantity of an item.
# You need to write 2 functions.
# Function 1: add_item()
# Parameters:
# details
# items

# The details parameter contains the item name, price, and available quantity, separated by commas.
# Example:
# Rice,50,20

# Requirements:
# Split the details string using a comma.
# Extract:
# Item name
# Price per unit
# Available quantity
# Convert the price and quantity from string to integer.
# Store the item details as a separate list inside the items list.

# The item should be stored in the following format:
# [item_name, price, quantity]

# Function 2: calculate_total()
# Parameters:
# input_string
# items

# The input_string contains the item name and required quantity separated by a comma.

# Example:
# Rice,3

# Requirements:
# Split the input string using a comma.
# Extract the item name and required quantity.
# Search for the item in the items list.
# Check whether the required quantity is available.
# If the required quantity is available, calculate the total cost using:
# price × required_quantity
# Return the calculated total.

def add_item(details, items):
    details = details.split(",")

    item_name = details[0].strip()
    price = int(details[1].strip())
    quantity = int(details[2].strip())
    
    items.append([item_name, price, quantity])


def calculate_total(input_string, items):
    input_string = input_string.split(",")

    item_name = input_string[0].strip()
    required_quantity = int(input_string[1].strip())

    for item in items:
        if item[0].lower() == item_name.lower():
            
            if item[2] >= required_quantity:
                total = item[1] * required_quantity
                return total
            else:
                return "Insufficient quantity"
    
    return "Item is not in the inventory"

def main():
    items = []

    while True:
        choice = input("Choose a method(add/calculate): ").lower()

        if choice == "add":
            n = int(input("Enter no. of items: "))

            for i in range(n):
                details = input("Enter the details of item: ")
                add_item(details, items)

        elif choice == "calculate":
            input_string = input(
                "Enter the item and quantity(separated by comma): "
            )

            result = calculate_total(input_string, items)

            print("Total amount:", result)
            break


if __name__ == "__main__":
    main()