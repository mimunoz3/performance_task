destination_list = ["beach,", "international,", "camping", "or city"] # List of vacation typers
name = input("What is your name? ") # Asks for User's name.
print(f"Welcome {name}!")  # Welcomes the User.

vacation = input("Do you want travel destination suggestions? yes/no")    # Asks the User if they'd like destination suggestions
vacation = vacation.lower() # Makes "destination" input lowercase, which allows for all inputs to be recognized no matter the capitilization.

if vacation == "no":
    print("Okay, maybe next time!")
while vacation == "yes":
    print("Great, Let's Play")
    question = input("Do you want beach, international, camping, or city destinations? ") # Gives the User 3 joke options to choose from
    question = question.lower() # Makes "question" input lowercase, which allows for all inputs to be recognized no matter the capitilization.
   
    if question == "beach": # vacation type #1.
        input("Cancun, Bora Bora, or Turks & Caicos. Do any of these interest you?")
        vacation = input("Do you want other destination suggestions?")  # Asks the User if they'd like another suggestion
        
    elif question == "international": # vacation type #2.
        print("Italy, Tokyo, Costa Rica")
        vacation = input("Do you want other destination suggestions?")  # Asks the User if they'd like another suggestion

    elif question == "camping": # vacation type #4
        print("California, Nevada, Montana")
        vacation = input("Do you want other destination suggestions?")  # Asks the User if they'd like another suggestion

    elif question == "city": # vacation type #5
        print("New York City California, Miami")
        vacation = input("Do you want other destination suggestions?")  # Asks the User if they'd like another suggestion


    def scoring_process(scoring): # Function for scoring process.
        final_score = [] # Purpose: Empty List for the User's score of the game, which allows the scoring process to have a result.

        for score in scoring:
            if vacation == "finished":
               score = int(scoring * 10) 
               final_score = score
               
        return final_score
    
    scoring = input("Please rate our travel suggestions 1-10! ") # Asks for User's rating.
    result = scoring_process(scoring)
    print((result), " percent satisfaction rate") # Prints out function result.


    if int(result) > 70:
        friend = input("Glad to hear you enjoyed! Would you recommend this game to a friend? ") # Asks User if they would recommend this game.
    else:
        unfortunate = input("Sad to hear that you didn't enjoy it.")
    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ") # If YES or MAYBE, then this will display.
    else:
        print("That's okay. ") # If OTHER ANSWER, then this will display.
