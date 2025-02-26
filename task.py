
def travel_destination(destination_options): 
    destinations = { 
        'beach': ['Hawaii', 'Bahamas', 'Maldives'], 
        'mountain': ['Swiss Alps', 'Rocky Mountains', 'Himalayas'], 
        'city': ['New York', 'Paris', 'Tokyo'] } 
    
    # print = input("Do you Beach, mountain, or city suggestions?")
    if destination_options in destinations: print(f"Here are some {destination_options} destinations:")
    for place in destinations[destination_options]:
        print(place)
    else: print(f"Sorry, we do not have any destinations for '{destination_options}' type of vacation.")
    def main():
         destination_options = input("Enter the type of vacation (beach, mountain, city): ").strip().lower() 
         travel_destination(destination_options) 
         if __name__ == "__main__":
             main()
destination = input("Do you want travel ideas?")
if destination == "no":
        print("Okay, maybe next time!")
        
while destination == "yes":
        print("Great!")
        question = input("Do you want beach, mountain, or city destinations?").strip().lower()

        travel_destination(question)
        
        destination = input("Do you want to explore other destinations? yes/not now").strip().lower()
        
if destination == "not now":
        try:
            rate = int(input("Please rate our travel ideas 1-10"))
            final_score = rate * 10
            print(f"{final_score} percent satisfaction rate")
        except ValueError:
            print("Invalid rating. Please enter a number between 1 and 10.")

        friend = input("Would you recommend this to a friend? (yes/no/maybe):").strip().lower()
        if friend == "yes" or friend == "maybe":
            print("Thank you, we appreciate it.")
        else:
            print("Sorry you did not like it.")