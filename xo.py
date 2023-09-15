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
   
    # Loop to print each row
    global table
    for i in range (5):
        if i % 2 == 0:
            print(" " , end="")
            
            # Print table
            for j in range(3):
                k = random.choice(letters)
                table += [k]
                if j != 2:
                    print( k, end="  |  ")
                else:
                    print( k, end="")
            
            print("")
        else:
            print(3*'-' , " " , 3*'-' , " " , 3*'-' )


def draw(table):
   i = 0
   while i < len(table):
        if i > 0 :
            print(3*'-' , " " , 3*'-' , " " , 3*'-' )
        print(" ", end="")
        for j in range(3):
            if j != 2:
                print( table[i], end="  |  ")
            else:
                print( table[i], end="")
            i += 1
        print("")

def accurate(user_input , table):
    
    while (user_input not in table) or (user_input == 'x') or (user_input == 'o'):
        print("pick a letter in XO table to turn it into x")
        #user input
        user_input = input()
        
    return user_input
def turn(t):
    global user_input
    if t == 'x':
        print("player1, it's your turn :)" , '\n' , "pick a letter in X-O table to turn it into x")
    else:
        print("player2, it's your turn :)" , '\n' , "pick a letter in X-O table to turn it into o")
    #if input is ok
    user_input = input()
    user_input = accurate(user_input , table)
    #changing table
    for i in range(len(table)):
            if table[i] == user_input:
                table[i] = t
    #showing table again
    draw(table)



def game():
    global table
    table = []
    #randomize the xo table
    initial()
    while not check('x') and not check('o') and not game_draw(table):    
        turn('x')
        #check if player1 wins
        if check('x'):
            print("player1 won!!!")
            play_again = input("playing again? (yes/no)").lower()
            if play_again == 'no':
                print ("thanks for playing! :)")
                break
            elif play_again == 'yes':
                game()
        else:
            turn('o')
        #check if player2 wins
        if check('o'):

            print("player2 won!!!")
            play_again = input("playing again? (yes/no)").lower()
            if play_again == 'no':
                print ("thanks for playing! :)")
                break
            elif play_again == 'yes':
                game()
        if game_draw(table):

            print("It's a draw!!!")
            play_again = input("playing again? (yes/no)").lower()
            if play_again == 'no':
                print ("thanks for playing! :)")
                break
            elif play_again == 'yes':
                game()



def check(xo):
    #check for 3 rows
    for i in range(3):
        if table[i]==table[i+3]==table[i+6]==xo:
            return True
    for i in range(0,9,3):
        if table[i]==table[i+1]==table[i+2]==xo:
            return True
    if table[0]==table[4]==table[8]==xo:
        return True
    if table[2]==table[4]==table[6]==xo:
        return True
    return False

def game_draw(table):
    for i in table:
        if i not in ['x' , 'o']:
            return False
    return True



game()





    

    
