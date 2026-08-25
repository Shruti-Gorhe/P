# Mobile Store
# Problem Description:

# Create a program to maintain a list of mobile phones available in a mobile store and calculate the total purchase amount for a requested quantity of a mobile phone.
# You need to write 2 functions.

# Function 1: add_mobile()
# Parameters:
# details
# mobiles

# The details parameter contains the brand, model, price, and available stock, separated by commas.

# Requirements:
# Split the details string using a comma.
# Extract:
# Brand
# Model
# Price
# Available stock
# Convert price and stock from string to integer.
# Store each mobile as a separate list inside the mobiles list.

# The mobile should be stored in the following format:
# [brand, model, price, stock]

# Function 2: calculate_purchase()

# Parameters:
# input_string
# mobiles

# The input_string contains the mobile model and required quantity, separated by a comma.

# Example:
# S25 Ultra,2

# Requirements:
# Split the input string using a comma.
# Extract the mobile model and required quantity.
# Search for the mobile using its model.
# Model comparison should be case-insensitive.
# Check whether the required quantity is less than or equal to the available stock.
# If sufficient stock is available, calculate the total purchase amount using:
# price × required_quantity
# If the required quantity is greater than the available stock, return:
# Insufficient stock
# If the mobile model is not present in the list, return:
# No such mobile

mobiles = []
def add_mobile(details,mobiles):
    details = details.split(",")
    brand = details[0].strip()
    model = details[1].strip()
    price = int(details[2].strip())
    available_stock = int(details[3].strip())
    mobiles.append([brand,model,price,available_stock])

def calculate_purchase(input_string,mobiles):
    input_string = input_string.split(",")
    model = input_string[0].strip()
    required_quantity = int(input_string[1].strip())
    
    for mobile in mobiles:
        if mobile[1].lower() == model.lower():
            if required_quantity <= mobile[3]:
                total_amount = mobile[2]*required_quantity
                return total_amount
            else:
                return "Insufficient stock"
    return "No such mobile"

def main():
    mobiles = []
    while True:
        choice = input("Choose a method(add/calculate): ").lower()
        if choice == "add":
            n = int(input("Enter no. of mobiles: "))
            for i in range(n):
                details = input("Enter the details of mobile: ")

                add_mobile(details, mobiles)

        elif choice == "calculate":

            input_string = input(
                "Enter the mobile model and quantity(separated by comma): "
            )

            result = calculate_purchase(input_string, mobiles)

            print("Total amount:", result)

            break


if __name__ == "__main__":
    main()