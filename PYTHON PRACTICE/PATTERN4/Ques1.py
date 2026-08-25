# Question 36 — Art Gallery
# Problem Description:

# Create a program to maintain details of artworks in an art gallery and provide a way to find all artworks created by a particular artist.

# You need to write 2 functions.

# Function 1: add_artist_details()
# Parameter:
# add_detail
# The add_detail parameter is a string containing the artwork ID, artist name, artwork type, and year, separated by commas.

# Example:
# 1,a,painting,2001

# Requirements:
# Split the input string using a comma.
# Remove unnecessary spaces from each value.
# The input should contain exactly 4 values.
# Store the details as a separate list inside the gallery list.
# Add the artist name to the artists set.
# The artist name should be taken from the second value of the input.
# Return both the gallery list and artists set.

# Each artwork should be stored in the following format:
# [artwork_id, artist_name, artwork_type, year]

# If the input does not contain exactly 4 values, return the existing gallery and artists without adding anything.

# Function 2: find_by_artist()
# Parameter:
# artist

# The function should search for all artworks created by the given artist.

# Requirements:
# Search through the gallery list.
# Artist name comparison should be case-insensitive.
# Return a list containing all artwork records belonging to that artist.
# If no artwork is found for the given artist, return an empty list.

def add_artist_details(add_detail):

    l1 = add_detail.split(',')

    l2 = [i.strip() for i in l1]

    if len(l2) != 4:
        return gallery, artists

    gallery.append(l2)

    artists.add(l2[1])

    return gallery, artists


def find_by_artist(artist):

    result = []

    for i in gallery:

        if i[1].lower() == artist.lower():
            result.append(i)

    return result

def main():
    global gallery, artists

    gallery = []           
    artists = set()

    n = int(input("Enter no. of artworks: "))

    for i in range(n):

        add_detail = input("Enter artwork details: ")

        gallery, artists = add_artist_details(add_detail)

    print("Gallery:")
    print(gallery)

    print("Artists:")
    print(artists)

    artist = input("Enter artist name to search: ")

    result = find_by_artist(artist)

    print("Artworks by artist:")
    print(result)


if __name__ == "__main__":
    main()