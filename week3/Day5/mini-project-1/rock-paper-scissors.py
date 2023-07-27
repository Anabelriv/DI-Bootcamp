# Instructions
# Create a new directory for the game. Inside it, create 2 files:
# rock-paper-scissors.py – this will contain functions to show the main menu, handle user’s input, and show the game summary before exiting.

from game import Game

def get_user_menu_choice():
    while True:
        try:
            print("\nMenu:")
            print("1. Play the game")
            print("2. View Results")
            print("3. Exit")
            choice = int(input("Enter your choice: "))
            if choice in [1, 2, 3]:
                return choice
            else: 
                print("Invalid choice! Please enter a valid choice.")
        except ValueError:
            print("Invalid choice! Please enter a valid choice.")

def print_results(results):
    print("/n RESULTS:")
    print(f"Total games played: {results['draw']+ results ['win'] + results['loss']}")
    print(f"Number of draws: {results['draw']}")
    print(f"Number of wins: {results['win']}")
    print(f"Number of losses: {results['loss']}")

def main():
    # results = {
    #     'draw':0,
    #     'win': 0,
    #     'loss':0
    # }
    
    while True:
        choice = get_user_menu_choice()

        if choice == 1:
            game = Game()
            results = game.play()
        elif choice == 2:
            print_results(results)
        else:
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
