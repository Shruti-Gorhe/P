# Music Library
# Problem Description:

# Create a program to maintain details of songs in a music library and find all songs belonging to a particular singer.

# You need to write 2 functions.

# Function 1: add_song_details()

# Parameter:

# add_detail

# The input string contains:

# song_id,singer,genre,year

# Example:

# 101,Arijit Singh,Romantic,2023

# Requirements:

# Split the input string using a comma.
# Remove unnecessary spaces from each value.
# The input must contain exactly 4 values.
# Store the song details as a separate list inside the library list.
# Add the singer's name to the singers set.
# Return the library list and singers set.
# If the input does not contain exactly 4 values, do not add the record.

# Each song should be stored as:

# [song_id, singer, genre, year]
# Function 2: find_by_singer()

# Parameter:

# singer

# Requirements:

# Search the library list.
# Singer comparison should be case-insensitive.
# Return a list containing all songs belonging to that singer.
# If no song is found, return an empty list.

def add_song_details(add_detail):
    l1 = add_detail.split(",")
    l2 = [i.strip() for i in l1]
    
    if len(l2) !=4:
        return library,singers

    library.append(l2)
    
    return library,singers

def find_by_singer(singer):
    result = []
    for song in library:
        if song[1].lower == singer.lower():
            result.append(song)
    return result

def main():

    global library, singers

    library = []
    singers = set()

    n = int(input("Enter no. of songs: "))

    for i in range(n):

        add_detail = input("Enter song details: ")

        library, singers = add_song_details(add_detail)

    print("Music Library:")
    print(library)

    print("Singers:")
    print(singers)

    singer = input("Enter singer name to search: ")

    result = find_by_singer(singer)

    print("Songs by singer:")
    print(result)


if __name__ == "__main__":
    main()