import random
import string
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("X-O")

l = string.ascii_lowercase
xo = 'xo'
letters = result = ''.join([char for char in l if char not in xo])

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

def check_winner(table, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(table[i][j] == player for j in range(3)) or all(table[j][i] == player for j in range(3)):
            return True
    if all(table[i][i] == player for i in range(3)) or all(table[i][2 - i] == player for i in range(3)):
        return True
    return False

# def show_dialog():
#     font = pygame.font.Font(None, 36)
#     dialog_text = "Again? (yes/no):"
#     input_text = ""
#     input_rect = pygame.Rect(200, 150, 300, 36)
#     color_inactive = pygame.Color('lightskyblue3')
#     color_active = pygame.Color('dodgerblue2')
#     color = color_inactive
#     active = False

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if input_rect.collidepoint(event.pos):
#                     active = not active
#                 else:
#                     active = False
#                 color = color_active if active else color_inactive
#             if event.type == pygame.KEYDOWN:
#                 if active:
#                     if event.key == pygame.K_RETURN:
#                         return input_text.lower()
#                     elif event.key == pygame.K_BACKSPACE:
#                         input_text = input_text[:-1]
#                     else:
#                         input_text += event.unicode

#         screen.fill((30, 30, 30))
#         txt_surface = font.render(input_text, True, color)
#         width = max(200, txt_surface.get_width()+10)
#         input_rect.w = width
#         screen.blit(txt_surface, (input_rect.x+5, input_rect.y+5))
#         pygame.draw.rect(screen, color, input_rect, 2)

#         pygame.display.flip()


def game():
    is_game_on = True
    while is_game_on:  # Outer loop for replay option
        table = [['' for _ in range(3)] for _ in range(3)]
        current_player = 'X'
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row = y // 66
                    col = x // 66
                    if accurate((row, col), table):
                        table[row][col] = current_player
                        screen.fill((30, 30, 30))  # Clear the screen

                        draw(table)
                        if check_winner(table, current_player):
                            print(f'Player {current_player} wins!')
                            running = False
                        elif all(all(cell != '' for cell in row) for row in table):
                            print('It\'s a draw!')
                            running = False
                        else:
                            current_player = 'O' if current_player == 'X' else 'X'

            initial()
            pygame.display.update()


        # pygame.quit()

        # screen.fill((30,30,30))        
        # pygame.display.update()
        pygame.display.flip()

        # Ask for replay option
        print('00000000000000')
        # replay = show_dialog()
        print("wanna play again?")
        replay = input()
        print("111111111111111")
        if replay == 'no':
            is_game_on = False
        elif replay.lower() == 'yes':
            # Clear the table and start a new game
            table = [['' for _ in range(3)] for _ in range(3)]
            current_player = 'X'
            running = True

game()
pygame.quit
