import pyautogui as ai
from time import sleep
from math import *

sleep(3)
ai.click(168, 885)
sleep(5)

ai.click(145, 83)
sleep(3)
ai.typewrite("Tic Tac Toe")
ai.press("enter")
ai.moveTo(509, 298, duration=0.25)
sleep(2)
ai.scroll(-3)
sleep(5)
board_location = ai.locateOnScreen("/Users/joelsmith/Desktop/Tic_Tac_Toe_Board_2.png")
if board_location is None:
   print("Image not found!")
else:
    print(board_location)

board_centre = [board_location[0] + (ceil(board_location[2] / 2)), board_location[1] + (ceil(board_location[3] / 2))]
ai.moveTo(board_centre[0], board_centre[1], duration=1)

ai.moveTo(board_centre)

input("Are you ready!: ")
sleep(3)

board_array = {1: "", 2: "", 3: "",
               4: "", 5: "", 6: "",
               7: "", 8: "", 9: ""}

def print_board_array(board_array):
    print(board_array[1] + " " + board_array[2] + " " + board_array[3])
    print(board_array[4] + " " + board_array[5] + " " + board_array[6])
    print(board_array[7] + " " + board_array[8] + " " + board_array[9])
    print("\n")
print_board_array(board_array)

def space_is_free(position):
    if board_array[position] == "":
        return True
    else:
        return False

def checkDraw():
    for key in board_array.keys():
        if board_array[key] == "":
            return False
    return True

best_move = 0

def insert_letter(letter, position):

    if space_is_free(position):
        board_array[position] = letter
        print_board_array(board_array)


        if(checkDraw()):
            print("Draw!")
            exit()

        if checkForWin():
            if letter == "X":
                print("Bot Wins!")
                exit()

            else:
                print("Player wins!")
                exit()
        return
    else:
        print("Can't insert there!")
        position = int(input("Enter New Position: "))
        insert_letter(letter, position)


def checkForWin():
    if (board_array[1] == board_array[2] and board_array[1] == board_array[3] and board_array[1] != ""):
        return True
    elif (board_array[4] == board_array[5] and board_array[4] == board_array[6] and board_array[4] != ""):
        return True
    elif (board_array[7] == board_array[8] and board_array[7] == board_array[9] and board_array[7] != ""):
        return True
    elif (board_array[1] == board_array[4] and board_array[1] == board_array[7] and board_array[1] != ""):
        return True
    elif (board_array[2] == board_array[5] and board_array[2] == board_array[8] and board_array[2] != ""):
        return True
    elif (board_array[3] == board_array[6] and board_array[3] == board_array[9] and board_array[3] != ""):
        return True
    elif (board_array[1] == board_array[5] and board_array[1] == board_array[9] and board_array[1] != ""):
        return True
    elif (board_array[7] == board_array[5] and board_array[7] == board_array[3] and board_array[7] != ""):
        return True
    else:
        return False

def check_which_mark_won(mark):
    if board_array[1] == board_array[2] and board_array[1] == board_array[3] and board_array[1] == mark:
        return True
    elif (board_array[4] == board_array[5] and board_array[4] == board_array[6] and board_array[4] == mark):
        return True
    elif (board_array[7] == board_array[8] and board_array[7] == board_array[9] and board_array[7] == mark):
        return True
    elif (board_array[1] == board_array[4] and board_array[1] == board_array[7] and board_array[1] == mark):
        return True
    elif (board_array[2] == board_array[5] and board_array[2] == board_array[8] and board_array[2] == mark):
        return True
    elif (board_array[3] == board_array[6] and board_array[3] == board_array[9] and board_array[3] == mark):
        return True
    elif (board_array[1] == board_array[5] and board_array[1] == board_array[9] and board_array[1] == mark):
        return True
    elif (board_array[7] == board_array[5] and board_array[7] == board_array[3] and board_array[7] == mark):
        return True
    else:
        return False




player = "O"
bot = "X"

def playerMove():
    has_player_moved = False
    position = 0
    while has_player_moved is False:
        if ai.pixel(435, 421)[0] == 242 and board_array[1] == "":
            position = 1
            has_player_moved = True
        elif ai.pixel(507, 351)[0] == 242 and board_array[2] == "":
            position = 2
            has_player_moved = True
        elif ai.pixel(576, 351)[0] == 242 and board_array[3] == "":
            position = 3
            has_player_moved = True
        elif ai.pixel(435, 421)[0] == 242 and board_array[4] == "":
            position = 4
            has_player_moved = True
        elif ai.pixel(507, 421)[0] == 242 and board_array[5] == "":
            position = 5
            has_player_moved = True
        elif ai.pixel(576, 421)[0] == 242 and board_array[6] == "":
            position = 6
            has_player_moved = True
        elif ai.pixel(435, 491)[0] == 242 and board_array[7] == "":
            position = 7
            has_player_moved = True
        elif ai.pixel(507, 491)[0] == 242 and board_array[8] == "":
            position = 8
            has_player_moved = True
        elif ai.pixel(576, 491)[0] == 242 and board_array[9] == "":
            position = 9
            has_player_moved = True

    insert_letter(player, position)

    return

def compMove():
    best_score = -800
    best_move = 0
    for key in board_array.keys():
       if board_array[key] == "":
           board_array[key] = bot
           score = minimax(board_array, 0, False)
           board_array[key] = ""
           if score > best_score:
               best_score = score
               best_move = key
    if best_move == 1:
        ai.moveTo(board_centre, duration=0.25)
        ai.moveRel(-78, -78, duration=0.25)
        ai.click(ai.position())
    if best_move == 2:
        ai.moveTo(board_centre, duration=0.25)
        ai.moveRel(0, -78, duration=0.25)
        ai.click(ai.position())
    if best_move == 3:
        ai.moveTo(board_centre, duration=0.25)
        ai.moveRel(78, -78, duration=0.25)
        ai.click(ai.position())
    if best_move == 4:
        ai.moveTo(board_centre, duration=0.25)
        ai.moveRel(-78, 0, duration=0.25)
        ai.click(ai.position())
    if best_move == 5:
        ai.moveTo(board_centre, duration=0.25)
        ai.moveRel(0, 0, duration=0.25)
        ai.click(ai.position())
    if best_move == 6:
        ai.moveTo(board_centre, duration=0.25)
        ai.moveRel(78, 0, duration=0.25)
        ai.click(ai.position())
    if best_move == 7:
        ai.moveTo(board_centre, duration=0.25)
        ai.moveRel(-78, 78, duration=0.25)
        ai.click(ai.position())
    if best_move == 8:
        ai.moveTo(board_centre, duration=0.25)
        ai.moveRel(0, 78, duration=0.25)
        ai.click(ai.position())
    if best_move == 9:
        ai.moveTo(board_centre, duration=0.25)
        ai.moveRel(78, 78, duration=0.25)
        ai.click(ai.position())
        return
    insert_letter(bot, best_move)
    return


def minimax(board_array, depth, isMaximizing):
    if (check_which_mark_won(bot)):
        return 1
    elif (check_which_mark_won(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        best_score = -800
        for key in board_array.keys():
            if (board_array[key] == ""):
                board_array[key] = bot
                score = minimax(board_array, depth + 1, False)
                board_array[key] = ""
                if (score > best_score):
                    best_score = score
        return best_score

    else:
        best_score = 800
        for key in board_array.keys():
            if (board_array[key] == ""):
                board_array[key] = player
                score = minimax(board_array, depth + 1, True)
                board_array[key] = ""
                if (score < best_score):
                    best_score = score
        return best_score


while not checkForWin():
    compMove()
    playerMove()
