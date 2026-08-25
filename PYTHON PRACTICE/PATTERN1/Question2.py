# Question 2 — Library Books

# Create:

# add_book_details(book_details, books)
# find_books(author, minimum_price, books)

# add_book_details()
# Input contains:
# book_name,author,price,quantity
# Requirements:
# Remove spaces.
# Store as tuple.
# Convert price and quantity to integers.
# Add to list.

# find_books()
# Find books:
# written by the specified author
# whose price is greater than or equal to the given price
# author comparison must be case-insensitive.
books = []
def add_book_details(book_details,books):
    details = book_details.split(",")
    book_name = details[0].strip()
    author = details[1].strip()
    price = int(details[2].strip())
    quantity = int(details[3].strip())
    
    book= (book_name,author,price,quantity)
    
    books.append(book)

def find_books(author,minimum_price,books):
    result=[]
    for book in books:
        if author.lower()==book[1].lower() and book[2]>=minimum_price:
            result.append(book)
    return result


def main():
    books = []

    n = int(input("Enter number of books: "))

    for i in range(n):
        details = input("Enter book details: ")
        add_book_details(details, books)

    print("Books:")

    author = input("Enter author: ")
    price = int(input("Enter minimum price: "))

    result = find_books(author, price, books)

    for book in result:
        print(book)


if __name__ == "__main__":
    main()