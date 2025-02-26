def travel_destination(destination_options): 
    destinations = { 
        'beach': ['Hawaii', 'Bahamas', 'Maldives'], 
        'mountain': ['Swiss Alps', 'Rocky Mountains', 'Himalayas'], 
        'city': ['New York', 'Paris', 'Tokyo']
    } 
    
    if destination_options in destinations:
        print(f"Here are some {destination_options} destinations:")
        for place in destinations[destination_options]:
            print(place)
    else:
        print(f"Sorry, we do not have any destinations for '{destination_options}' type of vacation.")

def main():
    destination = input("Do you want travel ideas? (yes/no): ").strip().lower()
    
    if destination == "no":
        print("Okay, maybe next time!")
        return     # Exit the program if the user says no.

    while destination == "yes":
        print("Great!")
        question = input("Do you want beach, mountain, or city destinations? (beach/mountain/city): ").strip().lower()
        travel_destination(question)

        destination = input("Do you want to explore other destinations? (yes/not now): ").strip().lower()
        if destination == "not now":
            try:
                rate = int(input("Please rate our travel ideas (1-10): "))
                final_score = rate * 10
                print(f"{final_score}% satisfaction rate")
            except ValueError:
                print("Invalid rating. Please enter a number between 1 and 10.")

            friend = input("Would you recommend this to a friend? (yes/no/maybe): ").strip().lower()
            if friend == "yes" or friend == "maybe":
                print("Thank you, we appreciate it.")
            else:
                print("Sorry you did not like it.")
            break  # Exit the loop when done.

if __name__ == "__main__":
    main()
