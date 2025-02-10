def travel_destination(destination_options):
    destinations = { 
        "Beach": ["Cancun", "Bora Bora", "Turks & Caicos"],
        "International": ["Italy", "Tokyo", "Costa Rica"],
        "Camping": ["California", "Nevada", "Montana"],
        "City": ["New York City", "London", "Paris"]
        }

    if destination_options in destinations: 
        for line in destinations[destination_options]:
            print(line)
    else:
        print("Sorry, I don't have any destination for that type of vacation.")

def main():
    destinations = input("Do you want travel destination suggestions? yes/no").strip().lower()

    if destinations == "no":
        print("Okay, maybe next time!")
        return 
    
    while destinations == "yes":
        print("Great!")
        question = input("Do you want a Beach, International, Camping, or City destination?").strip().lower()

        travel_destination(destinations)

        destinations = input("Do you want to explore other destinations? yes/not now").strip().lower()

    if destinations == "not now":
        try:
            rate = int(input("Please rate our travel ideas 1-10"))
            final_score = rate * 10
            print(f(final_score))
        except ValueError:
            print("Invalit rating. Please enter a number between 1 and 10.")

        friend = input("Would you recommend this to a friend? (yes/no/maybe):").strip().lower()
        if friend == "yes" or friend == "maybe":
            print("Thank you, we appreciate it.")
        else:
            print("Sorry you did not like it.")

main()