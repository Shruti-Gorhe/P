# Question 31 — Bakery Billing
# Create:
# add_item(name, category, price, quantity)
# calculate_bill(item_input)
# add_item()

# Parameters are strings.

# Convert:
# price → int
# quantity → int

# Store:
# [name, category, price, quantity]
# calculate_bill()

# Input:
# item_name,required_quantity

# Requirements:
# Search item case-insensitively.
# If item doesn't exist → "No such item".
# If required quantity > available quantity → "Insufficient quantity".
# Otherwise return:
# price × required_quantity

def add_item(details,items):
    name,category,price,quantity = details.split(",")
    price = int(price)
    quantity = int(quantity)
    items.append([name,category,price,quantity])


def calculate_bill(item_input,items):
    item_name,required_quantity = item_input.split(",")
    required_quantity = int(required_quantity)
    for item in items:
        if item[0].lower() == item_name.lower():
            if required_quantity > item[3]:
                return "Insufficient quantity"
            else:
                return item[2] * required_quantity
    return "No such item"


def main():

    items = []

    n = int(input("Enter number of bakery items: "))

    for i in range(n):

        details = input("Enter item details: ")

        add_item(details, items)

    print("\nBakery Items:")

    for item in items:
        print(item)

    order = input("\nEnter item and quantity: ")

    result = calculate_bill(order, items)

    print("Total Bill:", result)


if __name__ == "__main__":
    main()