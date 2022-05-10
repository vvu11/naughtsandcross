#naughts and crosses two player game
#!! there is a keyerror which occurs when running the code, if ran again you will be able to play the game

import sys, tty
import termios
termios.tcflush(sys.stdin, termios.TCIOFLUSH)

#creates a dictionary which converts letter input into numbers to use later in the translate to coord section
number_mapping = {
    "a" : 0,
    "b" : 1,
    "c" : 2
}

#variables
memory = []
playing = True


#  all ANSI code sourced from : https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
print("\u001b[47;1mHOW TO PLAY: \n You will be asked for a coordinate. These range from a, b, c and 0, 1, 2 \n The letters correspond with the x-axis, and the numbers correspond with the y" )
print(" Simply enter the letter and the number you wish to place your piece with no spaces or commas inbetween (e.g a1) \nGOOD LUCK!\u001b[0m")


#this function tells the programme that the first input (0) will be converted to the dictionary above 
def translate_to_coord(ask):
    coord = [0,0]
    coord[0] = number_mapping[ask[0]]
    coord[1] = int(ask[1])
    return coord 

#this block asks the player to input their coordinates and is appended to the variable memory 
def place_counter(player):
    if (player) == 1:
        colour = (u"\u001b[35;1mPlayer \u001b[0m")
    else:
        colour = (u'\u001b[36;1mPlayer \u001b[0m')
    ask = input(colour + str(player) + "\u001b[0m type a coordinate: ")
    coord = translate_to_coord(ask)
    coord.append(player)
    memory.append(coord)

#creates a 3 by 3 grid consisting of 0's 
#it takes the coordinates given above, and uses if statements to determine which part of the grid is taken. 

def print_grid():
    count = 0
    game_over = ()
    for y in range(3):
        for x in range(3):
            draw_coord = False
            for coord in memory:  
                if coord[0] == x and coord[1] == y:
                    draw_coord = True
                    player = coord[2]
                    #print(counter, end='')
            if draw_coord and player == 1: 
                print(u'\u001b[1m\u001b[35;1mß \u001b[0m', end='')
            elif draw_coord and player == 2:
                print(u'\u001b[36;1m∑ \u001b[0m', end='')
            else:
                print(u'\u001b[1m- \u001b[0m', end='')
            if draw_coord:
                count +=1
            
        print('')
    if count == 9:
        print("game over!")
        return False
    else:
        return True


turn_counter = 0
while playing:
    if turn_counter % 2 == 0:
        #print("player 1")
        place_counter(1)
        playing = print_grid()
    else:
        #print("player 2")
        place_counter(2)
        playing = print_grid()
    turn_counter += 1
