guesses = 7
points = 0

def Cape():

    print("Cape Slang pretty sure everyone in cape town should ace this give it a try and see how much you know")


    print(f"You have {guesses} lives try to use them wisely as 1 will be removed if you wrong ")

    
    
    def FirstQuestion():

        Question1 = input("A friendly greeting, like Hey! or What's up ?: ")
        Answer = "AWE"

        if Question1.lower() == Answer.lower():
            points +5
            return (f"Yes the answer is {Answer} Heyy look at you... I knew you would get the answer Lets go.....\nyou still have {guesses} lives left and have scored {points} points")
        
        
        else:
            print(f"Oops your answer {Question1} is not quiet right would you like to try again...\n coz its your first try we wont be deducting any lives ")
            return input("A friendly greeting, like Hey! or What's up ?: ")
        
        
    print(FirstQuestion())

    def SecondQuestion():

        Question2 = input("A gattering where people get together and put some meat on the coals: ")
        Answer = "BRAAI"

        if  Question2.lower() == Answer.lower():
            points +5
            return (f"Look at you doing your thing 2 in a row your answer {Answer} is correct \nyou just scored another {points} points and have {guesses} lives left")
        
        else:
            guesses 
            return (f"Eishhhh not quiet right your answer {Question2} is not what we looking for...you can try again \nyour lives are {guesses} we have deducted 1")
            
        

    print(SecondQuestion())

    def ThirdQuestion():


        Question3 = input("Greasy or junk food commonly eaten on a night out")
        Answer = "VUIL DITE"

        if Question3.lower() == Answer.lower().strip():
            points +5
            return (f"Your answer{Question3} is right how bout we enjoy a nice {Answer} together \nyou scored yourself {points} points and a have {guesses} lives")

        else:
            guesses -1
            return (f"I guess someone wont be getting some extra points \n{points} points left and {guesses}  have deducted 1")           
        
    print(ThirdQuestion())


if __name__ == "__main__":
    Cape()
    

