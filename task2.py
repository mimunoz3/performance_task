
destination_list = ["beach,", "international,", "camping"] # List of joke options.
name = input("What is your name? ") # Asks for User's name.
print(f"Welcome {name}!")  # Welcomes the User.

destination = input("Do you want travel suggestions? ")    # Asks the User if they'd like to hear a joke.
destination = destination.lower() # Makes "joke" input lowercase, which allows for all inputs to be recognized no matter the capitilization.

if destination == "no":
    print("Okay suit yourself!")
while destination == "yes":
    print("Great, Let's Play")
    question = input("Do you want beach, international, or camping destinations?") # Gives the User 3 vacation types to choose from
    question = question.lower() # Makes "question" input lowercase, which allows for all inputs to be recognized no matter the capitilization.
    
    if question == "beach": #  Option #1.
        print("Cancun, Bora Bora, or Turks & Caicos.")
        interest1 = input("Do you want other destination suggestions?")
        more1 = input("Do you want beach, international, or camping destinations?")

    elif question == "international": #  Option #2.
        print("Italy, Tokyo, Costa Rica")
        interest1 = input("Do you want other destination suggestions?")
        more1 = input("Do you want beach, international, or camping destinations?")

    elif question == "camping": #  Option #3.
        print("California, Nevada, Montana")
        interest1 = input("Do you want other destination suggestions?")
        more1 = input("Do you want beach, international, or camping destinations?")
       
    def scoring_process(scoring): # Function for scoring process.
        final_score = [] # Purpose: Empty List for the User's score of the game, which allows the scoring process to have a result.

    #     for score in scoring:
    #         if joke == "finished":
    #            score = int(scoring * 10) 
    #            final_score = score
               
    #     return final_score
    
    # scoring = input("Please rate our game 1-10! ") # Asks for User's rating.
    # result = scoring_process(scoring)
    # print((result), " percent satisfaction rate") # Prints out function result.


    # if int(result) > 70:
    #     friend = input("Glad to hear you enjoyed the game! Would you recommend this game to a friend? ") # Asks User if they would recommend this game.
    # else:
    #     unfortunate = input("Sad to hear that you didn't enjoy the game.")
    # if friend == "yes" or friend == "maybe":
    #     print("Thanks, we appreciate it. ") # If YES or MAYBE, then this will display.
    # else:
    #     print("That's okay. ") # If OTHER ANSWER, then this will display.

