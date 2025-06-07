def Cape():

    print("Cape Slang pretty sure everyone in cape town should ace this give it a try and see how much you know")

    guesses = 7
    print(f"You have {guesses} try to use them wisely as 1 will beremoved if you wrong ")

    points = 0
    
    Question1 = input("A friendly greeting, like Hey! or What's up ?: ")
    Answer = "Awe"

    if Question1.lower() == "awe":
        points = points+5
        return (f"Yes the answer is {Answer} Heyy look at you... I knew youd get the answer Lets go.....\nyou still have {guesses} lives left and have scored {points} points")
        
        
    else:
        return (f"Oops your answer {Question1} is not quiet right would you like to try again...\n coz its your first try we wont be deducting any lives ")

   
if __name__ == "__main__":
    print(Cape())
    

