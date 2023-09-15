import random




def get_user_choice():
    print("Enter your choice: Rock, Paper, or Scissors")
    return input().lower()

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    
    else:
        return "Computer wins!"

def play_game():
    while True:
        user_choice = get_user_choice()
        while user_choice not in ["rock", "paper", "scissors"]:
            print( "Didn't get it, could you write your choice again?")
            user_choice = get_user_choice()

        computer_choice = get_computer_choice()
        
        print(f"You chose {user_choice}")
        print(f"Computer chose {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no)").lower()
        if play_again != 'yes':
            print ("thanks for playing! :)")
            break
        

if __name__ == "__main__":
    play_game()

