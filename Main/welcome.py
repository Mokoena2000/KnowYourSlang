print("Welcome to Know Your Slang!")
print("A game where you will be given a sentence and tell us what its slang word is")
print("Show us how well do you know south african slang put yourself to the test and show of your knowledge to friends and family")
print("Challenge yourself to learn more local slang and see just how much you Xav ")
print("Making day to day communicasion in SA easier with most common used word to make communication lekker \nHave fun and remember HULLE WIETIE WAT ONS WIETIE")

print(" ")
print(" ")

name = input("Before we start its best practise to ask a persons name: ")

play = input(f"Hello {name} Would you like to joing the fun: (Yes/No)")

def Start():


    if play.lower() == "yes":
        return (f"Awesome {name} lets start the fun choose where you would like to visit")
        
    elif play.lower() == "no":
        return (f"Ooops its all good {name} lets play next time")

    else:
        return "Please choose yes or no"
        
                              

if __name__ == "__main__":
    print(Start())






    
