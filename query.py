from movies import Movies

movies = Movies('./movies.txt')

userInput = " "
while userInput != ("q"):
    print("q: Quit")
    
    userInput = input("\nEnter option: ")
    userInput = userInput.lower()

    if userInput == "q":
        break
    else:
        print("Invalid Option!\n")