# Movie Collection

# add_movie_details(movie_details, movies)
# Input:
# movie_name,genre,duration,rating
# Convert duration and rating to integers.

# find_movies(genre, minimum_rating, movies)
# Return movies:
# matching genre
# rating >= minimum rating
# genre comparison case-insensitive.

movies = []
def add_movie_details(movie_details,movies):
    details = movie_details.split(",")
    movie_name = details[0].strip()
    genre = details[1].strip()
    duration = int(details[2].strip())
    rating = int(details[3].strip())
    
    movie =(movie_name,genre,duration,rating)
    movies.append(movie)

def find_movies(genre,minimum_rating,movies):
    result =[]
    for movie in movies:
        if genre.lower() == movie[1].lower() and movie[3]>= minimum_rating:
            result.append(movie)
    return result

def main():
    movies = []
    n = int(input("Enter number of movies: "))

    for i in range(n):
        details = input("Enter movie details: ")
        add_movie_details(details, movies)

    genre = input("Enter genre: ")
    rating = int(input("Enter minimum rating: "))

    print("Movies:")

    result = find_movies(genre, rating, movies)

    for movie in result:
        print(movie)


if __name__ == "__main__":
    main()