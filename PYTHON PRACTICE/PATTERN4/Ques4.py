def add_movie_details(add_detail):
    l1 = add_detail.split(",")
    l2 = [i.strip()for i in l1]
    
    if len(l2)!=4:
        return movies,directors
    
    movies.append(l2)
    return movies,directors

def find_by_director(director):
    result = []
    
    for movie in movies:
        if director.lower() == movie[2].lower():
            result.append(movie)
    return result

def main():

    global movies, directors

    movies = []
    directors = set()

    n = int(input("Enter no. of movies: "))

    for i in range(n):

        add_detail = input("Enter movie details: ")

        movies, directors = add_movie_details(add_detail)

    print("Movie Collection:")
    print(movies)

    print("Directors:")
    print(directors)

    director = input("Enter director name to search: ")

    result = find_by_director(director)

    print("Movies by director:")
    print(result)


if __name__ == "__main__":
    main()