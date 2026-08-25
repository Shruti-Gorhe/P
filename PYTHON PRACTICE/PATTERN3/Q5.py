# Question 35 — Electronics Store
# Problem Description:
# Create a program to maintain a list of electronic products available in a store and calculate the total purchase amount for a requested quantity of a product.
# You need to write 2 functions.
# Function 1: add_product()
# Parameters:
# details
# products

# The details parameter contains the product name, category, price, and available stock, separated by commas.

# Example:
# Laptop,Computer,75000,5

# Requirements:
# Split the details string using a comma.
# Extract:
# Product name
# Category
# Price
# Available stock
# Convert price and stock from string to integer.
# Store each product as a separate list inside the products list.

# The product should be stored in the following format:

# [product_name, category, price, stock]
# Function 2: calculate_purchase()

# Parameters:
# input_string
# products

# The input_string contains the product name and required quantity, separated by a comma.

# Example:
# Laptop,2

# Requirements:
# Split the input string using a comma.
# Extract the product name and required quantity.
# Search for the product in the products list.
# Product name comparison should be case-insensitive.
# Check whether the required quantity is less than or equal to the available stock.
# If sufficient stock is available, calculate the total purchase amount using:
# price × required_quantity
# If the product is not present in the list, return:
# "No such product"
# If the required quantity is greater than the available stock, return:
# "Insufficient stock"


def add_product(details,products):
    details = details.split(",")
    product_name = details[0].strip()
    category =details[1].strip()
    price = int(details[2].strip())
    available_stock = int(details[3].strip())
    products.append([product_name,category,price,available_stock])
    
def calculate_purchase(input_string,products):
    input_string = input_string.split(",")
    product_name = input_string[0].strip()
    required_quantity = int(input_string[1].strip())
    
    for product in products:
        if product[0].lower() == product_name.lower():
            if required_quantity > product[3]:
                return "Insufficient stock"
            else:
                return product[2] * required_quantity
    return "No such product"
                


def main():

    products = []

    while True:

        choice = input("Choose a method(add/calculate): ").lower()

        if choice == "add":

            n = int(input("Enter no. of products: "))

            for i in range(n):

                details = input("Enter the details of product: ")

                add_product(details, products)

        elif choice == "calculate":

            input_string = input(
                "Enter the product name and quantity(separated by comma): "
            )
            
            result = calculate_purchase(input_string, products)

            print("Total amount:", result)

            break

if __name__ == "__main__":
    main()