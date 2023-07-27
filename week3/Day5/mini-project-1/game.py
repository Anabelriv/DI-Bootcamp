# ## game.py

# - Game class

#   - class attribute
#     lst_choice = ["rock", "paper", "scissors"]

#   - **init** method
#     - attribute
  
#     result = {
#         draw : 0,
#         win : 0
#         loss : 0
#     }
    

#   @staticmethod
#   - get_user_item()
#     - while
#     - input method and check if the answer is in the list
#     - try/except and check for the possible errors
#     - return the choice

#   @staticmethod
#   - get_computer_item()
#     - use random choice to get a choice for the computer

#   - get_game_result(self, user_item, computer_item)
#     - conditions (compare)
#     - update the dictionary

#   - play(self):
#     - user = get_user_item()
#     - computer = get_computer_item()
#     - get_game_result(user, computer)
#     - print the output sentence
#     - return the results

# ## rock-paper-scissors.py

#     import the Game class

#     - get_user_menu_choice()
#         - show the user menu,

#     - print_results(results)
#         - print the results

#     - main()
#         - get_user_menu_choice() --> continue asking until the user
#         entered a valid choice
#         - create a game object and call the play() method

import random 

class Game:
    lst_choice = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.result = {
            'draw': 0,
            'win': 0, 
            'loss':0
        }

    @staticmethod
    def get_user_item():
        while True:
            try:
                user_choice = input ("Enter your choice (rock, paper, scissors): ").lower()
                if user_choice in Game.lst_choice:
                    return user_choice
                else:
                    raise Exception ("Invalid choice! Please enter a valid choice.")
            except Exception:
                print("Error Exciting the game.")

    @staticmethod
    def get_computer_item():
        return random.choice(Game.lst_choice)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            self.result['draw'] += 1
            return "It's a draw!"
        elif (user_item == 'rock' and computer_item == 'scissors') or \
            (user_item == 'paper' and computer_item == 'rock') or \
            (user_item == 'scissors' and computer_item == 'paper'):
            self.result['win'] += 1
            return "Congratulations! You win!"
        else:
                self.result['loss'] += 1
                return "Sorry! You lose."

    def play(self):
        user = self.get_user_item()
        computer = self.get_computer_item()
        result = self.get_game_result(user, computer)
        print(f"Your choice: {user}, Computer's choise: {computer}")
        print(result)
        return self.result    
        



# options = ("rock", "paper", "scissors")

# playing = True

# while playing:

#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input("Enter a choice(rock, paper, scissors): ")
#     print(f"Player: {player}")
#     print(f"Player: {computer}")

#     if player == computer:
#         print("It's a tie")
#     elif player == "rock" and computer =="scissors":
#         print("You win!")
#     elif player == "paper" and computer =="rock":
#         print("You win!")
#     elif player == "scissors" and computer =="paper":
#         print("You win!")
#     else:
#         print("You lose!")

#     play_again = input("Play again? (y/n): ").lower()
#     if not play_again == "y":
#         playing = False

# print("Thanks for playing!")


