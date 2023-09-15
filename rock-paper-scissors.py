import random
import pygame

pygame.init()

# Constants for colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors Game")

# Load images for the choices
rock_image = pygame.image.load("rock.png")
paper_image = pygame.image.load("paper.png")
scissors_image = pygame.image.load("scissors.png")

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

# Game loop

def display_choice(choice, x, y):
    screen.blit(choice, (x, y))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)

        # Display choices
        display_choice(rock_image, 100, 200)
        display_choice(paper_image, 300, 200)
        display_choice(scissors_image, 500, 200)

        # ... (rest of your code, including user input, result display, and play again logic) ...

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

def play_game():
    while True:
        user_choice = None

        # Game loop for user choice
        while user_choice not in ["rock", "paper", "scissors"]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return  # Exit the game if the user closes the window

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 100 <= mouse_x <= 200:
                        user_choice = "rock"
                    elif 300 <= mouse_x <= 400:
                        user_choice = "paper"
                    elif 500 <= mouse_x <= 600:
                        user_choice = "scissors"

        
        computer_choice = get_computer_choice()

        # Clear the screen
        screen.fill(WHITE)

        # Display choices
        display_choice(rock_image, 100, 200)
        display_choice(paper_image, 300, 200)
        display_choice(scissors_image, 500, 200)

        print(f"You chose {user_choice}")
        print(f"Computer chose {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no)").lower()
        if play_again != 'yes':
            print ("Thanks for playing! :)")
            break

if __name__ == "__main__":
    play_game()








