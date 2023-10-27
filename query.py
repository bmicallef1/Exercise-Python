from movies import Movies

movies = Movies('./movies.txt')

userInput = " "
while userInput != ("q"):
    print("q: Quit")
    print("list: Print all the Movie Names")
    
    userInput = input("\nEnter option: ")
    userInput = userInput.lower()

    if userInput == "q":
        break
    elif userInput == "list":
        print("\nList of all Movie Names: ")
        totalMovies = len(movies._movies)
        for movie in range(totalMovies):
            print("#", movie, ": ", movies._movies[movie]['name'])
        print()
    else:
        print("Invalid Option!\n")