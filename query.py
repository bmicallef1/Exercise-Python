from movies import Movies

movies = Movies('./movies.txt')

userInput = " "
while userInput != ("q"):
    print("q: Quit")
    print("sn: Search Movie Names")
    print("sc: Search Casts")
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
    elif userInput == "sn":
        snInput = input("\tEnter a word to search: ")
        totalMovies = len(movies._movies)
        for movie in range(totalMovies):
            if (snInput in movies._movies[movie]['name'].lower()):
                print(movies._movies[movie]['name'])
        print()
    elif userInput == "sc":
        scInput = input("\tEnter a word to search: ")
        totalMovies = len(movies._movies)
        castList = []
        for movie in range(totalMovies):
            totalCast = len(movies._movies[movie]['cast'])
            for person in range(totalCast):
                if (scInput in movies._movies[movie]['cast'][person].lower()):
                    print(movies._movies[movie]['name'])
                    castList.append(movies._movies[movie]['cast'][person])
                    print(castList)
        print()
    else:
        print("Invalid Option!\n")