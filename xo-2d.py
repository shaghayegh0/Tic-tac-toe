import random
import string

import pygame
pygame.init()

screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("X-O")

l = string.ascii_lowercase 
xo = 'xo'
letters = result = ''.join([char for char in l if char not in xo])
table = []

def initial():
    for row in range(3):
        for col in range(3):
            pygame.draw.rect(screen, (255, 255, 255), (col * 66, row * 66, 64, 64), 2)

def draw(table):
    for row in range(3):
        for col in range(3):
            cell = table[row][col]
            if cell == 'X':
                pygame.draw.line(screen, (255, 0, 0), (col * 66, row * 66), (col * 66 + 64, row * 66 + 64), 2)
                pygame.draw.line(screen, (255, 0, 0), (col * 66, row * 66 + 64), (col * 66 + 64, row * 66), 2)
            elif cell == 'O':
                pygame.draw.circle(screen, (0, 0, 255), (col * 66 + 32, row * 66 + 32), 30, 2)

def accurate(user_input, table):
    row, col = user_input
    if 0 <= row < 3 and 0 <= col < 3 and table[row][col] == '':
        return True
    else:
        return False


def turn(t):
    valid_move = False
    while not valid_move:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // 66
                col = x // 66
                if accurate((row, col), table):
                    valid_move = True
        pygame.display.update()

    table[row][col] = t
    draw(table)


def game():
    # Initialize the game board (table) as a 3x3 grid filled with empty strings
    table = [['' for _ in range(3)] for _ in range(3)]

    running = True  # Flag to control the game loop

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Set the running flag to False to exit the game loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // 66
                col = x // 66
                if accurate((row, col), table):
                    table[row][col] = 'X'  # Assuming 'X' is the current player
                    draw(table)

        initial()  # Draw the initial game board
        pygame.display.update()

    pygame.quit()  # Clean up Pygame resources when the game loop exits

game()









    

    
