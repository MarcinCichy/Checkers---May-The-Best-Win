# CHECKERS
# The Game
# May The Best Win

from os import system, name
import time
from termcolor import colored, cprint
from pyfiglet import Figlet


def clear_screen():
    """ Clear the screen in depends of operation system (Windows, Linux or iOS).
        It was copied from internet,  I will find out how it works in future (_=system is unknown for me) :)"""
    if name == "nt":
        _=system('cls')
    else:
        _=system('clear')
        

# Temporary chessboard
temp_chessboard = []


# The names of all fields, from which the names of Field objects will be taken
all_fields_names = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
                    'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
                    'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8',
                    'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8',
                    'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8',
                    'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8',
                    'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8',
                    'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8']

# Names of active fields (those on which pawns move)
active_fields_names = ['A2', 'A4', 'A6', 'A8',
                       'B1', 'B3', 'B5', 'B7',
                       'C2', 'C4', 'C6', 'C8',
                       'D1', 'D3', 'D5', 'D7',
                       'E2', 'E4', 'E6', 'E8',
                       'F1', 'F3', 'F5', 'F7',
                       'G2', 'G4', 'G6', 'G8',
                       'H1', 'H3', 'H5', 'H7']

# Names of border fields, i.e. those where the possibility of movement is limited by the edges of the board
border_fields_names = ['B1', 'D1', 'F1', 'A8', 'C8', 'E8', 'G8']


# The names of the black pawns
black_pawn_names = ['BP1', 'BP2', 'BP3', 'BP4',
                    'BP5', 'BP6', 'BP7', 'BP8',
                    'BP9', 'BP10', 'BP11', 'BP12']

# The names of the white pawns
white_pawn_names = ['WP1', 'WP2', 'WP3', 'WP4',
                    'WP5', 'WP6', 'WP7', 'WP8',
                    'WP9', 'WP10', 'WP11', 'WP12']

# Names for fields without a pawn
without_pawns_name = ['W_O_P']


"""
    shortcuts for Unicode to draw chessboard
"""

LUC = '\u250C'      # LEFT UPPER CORNER
HS = '\u2500'       # HORIZONTAL STRAIGHT
HUHC = '\u252C'     # HORIZONTAL UPPER HALF CROSS
RUC = '\u2510'      # RIGHT UPPER CORNER
VS = '\u2502'       # VERTICAL STRAIGHT
VRHC = '\u251C'     # VERTICAL RIGHT HALF CROSS
DCR = '\u253C'      # DOUBLE CROSS
VLHC = '\u2524'     # VERTICAL LEFT HALF CROSS
LDC = '\u2514'      # LEFT DOWN CORNER
HDHC = '\u2534'     # HORIZONTAL DOWNER HALF CROSS
RDC = '\u2518'      # RIGHT DOWN CORNER
WF = '\u2588'       # WHITE FIELD


class Pawn:
    def __init__(self, pawn_name, pawn_colour=None, pawn_place=None):
        self.pawn_name = pawn_name
        self.pawn_colour = pawn_colour                # Black or White.
        self.pawn_place = pawn_place                  # The place where pawn is on the board.
    

class Field:
    def __init__(self, field_name, field_status="Free"):
        self.field_name = field_name
        self.field_status = field_status            # It may be empty or it may be occupied by a pawn


# A function that creates Pawn class objects for black and white pawns and for "no pawns"
def pawns():
    list_of_all_pawns = []
    black_pawns = {name: Pawn(pawn_name=name) for name in black_pawn_names}
    for blp in black_pawns:
        black_pawns[blp].pawn_colour = "black"
        list_of_all_pawns.append(black_pawns[blp])
    white_pawns = {name: Pawn(pawn_name=name) for name in white_pawn_names}
    for whp in white_pawns:
        white_pawns[whp].pawn_colour = "white"
        list_of_all_pawns.append(white_pawns[whp])
    without_pawns = Pawn(pawn_name="W_O_P", pawn_colour="no_colour")
    list_of_all_pawns.append(without_pawns)
    return list_of_all_pawns
  
    
# A function that creates a game board with the names of all the fields
def chessboard():
    list_of_all_fields = []
    fields = {name: Field(field_name=name) for name in all_fields_names}
    for f in fields:
        temp_list = []
        temp_list.append(fields[f])
        temp_list.append((pawns()[-1]))
        list_of_all_fields.append(temp_list)
    
    # For all fields that are not used in the game (white fields) it assigns the status "UNUSED"
    for field in list_of_all_fields:                                    # For a field that is on the list of all fields
        if field[0].field_name not in active_fields_names:              # if the field is not on the list of active fields, then
            field[0].field_status = "UNUSED"                           # assign a parameter of the STATUS object as "UNUSED"
    z = 0
    for i in range(0, 24):                                      # otherwise, for the first 24 fields
        if list_of_all_fields[i][0].field_status == "Free":     # change the field status from "Free"
            list_of_all_fields[i][0].field_status = "Occupied"  # on "Occupied", because there will be pawns
        if list_of_all_fields[i][0].field_name in active_fields_names:
            list_of_all_fields[i][1] = pawns()[z]
            z += 1
          
    z = 0
    for j in range(40, 64):                                     # For last 24 fields
        if list_of_all_fields[j][0].field_status == "Free":     # change the field status from "Free"
            list_of_all_fields[j][0].field_status = "Occupied"  # on "Occupied", because there will be pawns
        if list_of_all_fields[j][0].field_name in active_fields_names:
            list_of_all_fields[j][1] = pawns()[z+12]
            z += 1

    return list_of_all_fields


def take_user_move(who_turn):
    print(f"Now it's turn: {who_turn}s")
    pawn_name_choose = input("Enter the name of the pawn: ")
    # ask for pawn until chosen pawn is on white or black pawn lists and the colour of pawn is equal who_turn
    if who_turn == "white":
        while pawn_name_choose.upper() not in white_pawn_names:
            pawn_name_choose = input("Enter the correct name of the pawn: ")
    elif who_turn == "black":
        while pawn_name_choose.upper() not in black_pawn_names:
            pawn_name_choose = input("Enter the correct name of the pawn: ")
    field_name_choose = input("Enter a field name: ")
    
    # ask for field until chosen field is on active field name list and the move is no longer than 1 field
    while field_name_choose.upper() not in active_fields_names:
        field_name_choose = input("Please enter a valid field name: ")
    return field_name_choose.upper(), pawn_name_choose.upper()
    

def is_move_correct(move_func, temp_chessb):
    which_field = move_func[0]                  # field name (name only, not object)
    which_pawn = move_func[1]                   # pawn name (name only, not object)
    for field in temp_chessb:
        if which_pawn == field[1].pawn_name:
            which_pawn_field_index = temp_chessb.index(field)
            break
            
    for field in temp_chessb:
        if which_field == field[0].field_name:
            chosen_field_index = temp_chessb.index(field)
            distance = which_pawn_field_index - chosen_field_index
            # check distance, is it not too long
            if (abs(distance) != 7) and (abs(distance) != 14) and (abs(distance) != 9) and (abs(distance) != 18):
                return "You can't move there. Wrong distance."
                # check if pawn moves back, that move is prohibited
            elif ((which_pawn in white_pawn_names) and distance < 0) or ((which_pawn in black_pawn_names) and distance > 0):
                return f"You can't move back your pawn."
            elif (abs(which_pawn_field_index-chosen_field_index) == 14) or (abs(which_pawn_field_index-chosen_field_index) == 18):
                info_capture = capture_pawn(temp_chessb, which_pawn_field_index, chosen_field_index)
                return info_capture
            # check that the selected field is free. If yes...
            elif temp_chessb[chosen_field_index][0].field_status == "Free":
                move_pawn(temp_chessb, which_pawn_field_index, chosen_field_index)
                # return f'You can move on field: {fields[0].field_name}.'
                return temp_chessb[chosen_field_index][1].pawn_colour
            # check that the selected field is free. If no...
            elif temp_chessb[chosen_field_index][0].field_status == "Occupied":
                return "Field is occupied. You can't move there."
                
    
def move_pawn(temp_chessb, which_pawn_field_index, chosen_field_index):
    temp_chessb[chosen_field_index][1] = temp_chessb[which_pawn_field_index][1]  # copying a Pawn class object from the field where it is to the indicated field
    temp_chessb[chosen_field_index][0].field_status = "Occupied"                 # change the status of a field selected after moving a pawn there
    temp_chessb[which_pawn_field_index][1] = pawns()[-1]                         # setting the value of the Pawn class object to the value W_O_P in the current field
    temp_chessb[which_pawn_field_index][0].field_status = "Free"                 # and setting the status of the released field to Free
    if temp_chessb[which_pawn_field_index][1].pawn_colour == "white":
        return "white"
    else:
        return "black"


def capture_pawn(temp_chessb, which_pawn_field_index, chosen_field_index):
    if which_pawn_field_index - chosen_field_index == -14:
        middle_field_index = (which_pawn_field_index + 7)
    elif which_pawn_field_index - chosen_field_index == 14:
        middle_field_index = (which_pawn_field_index - 7)
    elif which_pawn_field_index - chosen_field_index == -18:
        middle_field_index = (which_pawn_field_index + 9)
    elif which_pawn_field_index - chosen_field_index == 18:
        middle_field_index = (which_pawn_field_index - 9)
    else:
        return "err0"
    
    if temp_chessb[middle_field_index][0].field_status == "Free":
        return "You can't move there. You can't jump over free field."
    elif temp_chessb[middle_field_index][1].pawn_colour == temp_chessb[which_pawn_field_index][1].pawn_colour:
        return "You can't move there. You can't jump over your own pawn."
    else:
        if temp_chessb[middle_field_index][1].pawn_colour == "white":
            white_pawn_names.remove(temp_chessb[middle_field_index][1].pawn_name)
        elif temp_chessb[middle_field_index][1].pawn_colour == "black":
            black_pawn_names.remove(temp_chessb[middle_field_index][1].pawn_name)
        # two lines below delete captured pawn from chessboard
        temp_chessb[middle_field_index][1] = pawns()[-1]
        temp_chessb[middle_field_index][0].field_status = "Free"
        move_pawn(temp_chessb, which_pawn_field_index, chosen_field_index)
        return "You captured enemy pawn!"
    

def show_info(info):
    if info == "white" or info == "black":
        print('')
    else:
        print(info)
        
        
def whose_turn(info):
    if info == "white":
        return "black"
    else:
        return "white"
    
    
def shows_game_board(temp_chessb):
    """ Shows chessboard. Uses Unicode signs to draw chessboard.
        Uses prepared earlier shortcuts for every needed signs. """
    
    # clear_screen()
    cols = all_fields_names[0:8]
    rows = all_fields_names[::8]

    # rows = 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'
    # cols = 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'
 
    # chessboard header
    print(LUC, end="")
    for i in range(0, 29, 4):
        print(HS * 5 + HUHC, end="")    # the top line of the chessboard header
    print(HS * 5 + RUC)
    print(VS,'   ',VS, end='')          # first free field
    for x in range(8):
        print(' ', cols[x][1],'', VS, end="")          # shows digits from 1 to 8 into first row
    print('\n', end="")     # next line start draw from new line, but don't make one empty line
    print(VRHC, end="")
    for i in range(0, 29, 4):
        print(HS * 5 + DCR, end="")    # the middle line of the chessboard
    print(HS * 5 + VLHC)
    
    # chessboard body
    for y in range(8):
        print(VS, '', rows[y][0], '', VS, end="")       # shows letters from A to H at the left side of chessboard
        for z in range(y*8, y*8+8):
            if temp_chessb[z][1].pawn_name in white_pawn_names:
                colored_pawn = colored(temp_chessb[z][1].pawn_name, "yellow")
            elif temp_chessb[z][1].pawn_name in black_pawn_names:
                colored_pawn = colored(temp_chessb[z][1].pawn_name, "blue")
            if temp_chessb[z][1].pawn_name != "W_O_P":      #
                if len(temp_chessb[z][1].pawn_name) == 3:   # for names of pawn which are 3 chars length
                    print('', colored_pawn, VS, end="")
                else:
                    print(colored_pawn, VS, end="")  # for names of pawn which are 4 chars length, delete space at front
            else:
                if temp_chessb[z][0].field_status != "UNUSED":
                    print('    ', VS, end="")
                else:
                    print(WF, '', WF, VS, end="")       # shows empty field for fields value W_O_P (without pawn)
        print('\n', end="")     # next line start draw from new line
        
        # draw middle line in middle of chessboard, but after last line draw bottom line
        if y != 7:
            print(VRHC, end="")
            for i in range(0, 29, 4):
                print(HS * 5 + DCR, end="")  # the middle line of the chessboard
            print(HS * 5 + VLHC)
        else:
            print(LDC, end="")
            for i in range(0, 29, 4):
                print(HS * 5 + HDHC, end="")  # the middle line of the chessboard
            print(HS * 5 + RDC)
    print('\n')


def start_game_screen():
    """ Show start screen. Use pyfigled and termcolor modules"""
    
    f = Figlet(font="standard")
    print(colored(f.renderText("           CHECKERS"), "green"))
    time.sleep(1)  # Used time module for program delay
    f = Figlet(font="doom")
    print(colored(f.renderText("May The  Best Win"), "red"))
    # print(colored("       May The Best Win", "red"))
    time.sleep(3)


def end_game_screen():
    time.sleep(2)
    clear_screen()
    start_game_screen()
    answer = input(colored("       Do You want play again [Y]es/[N]o ? ", "green"))
    if answer == "n":
        goodbye_screen()
    
    else:
        main_game()
        
    
def goodbye_screen():
    """Shows goodbye screen"""

    clear_screen()
    start_game_screen()
    f = Figlet(font ="standard")
    print(colored(f.renderText('GOODBYE'), "magenta"))
    
    
def main_game():
    temp_chessboard = chessboard()
    clear_screen()
    start_game_screen()
    print('\n')
    clear_screen()
    shows_game_board(temp_chessboard)
    turn = "white"
    while (len(black_pawn_names) > 0) or (len(white_pawn_names) > 0):
        announcement = is_move_correct(take_user_move(turn), temp_chessboard)
        clear_screen()
        shows_game_board(temp_chessboard)
        computer_move_and_capture(temp_chessboard)
        show_info(announcement)
        turn = whose_turn(announcement)
        
    end_game_screen()
    

# def computer_move_and_capture(temp_chessb):
#     """ It is a function that performs computer movements and captures the opponent's pieces.
#         This function tries to guess human movements.
#         This function is really huge. This is no K.I.S.S, but it works. I know.
#         This is K.I.W.I -> Keep It Working Idiot  ;-)"""
#
#     possible_moves = []
#     possible_captures = []
#     possible_enemy_counterattacks = []
#     for field in temp_chessb:
#         if field[1].pawn_name in black_pawn_names:              # field with pawn which is black
#             which_pawn = field[1]                               # object -> black pawn
#             which_pawn_field_index = temp_chessb.index(field)   # index of field with black pawn
#
#             """ POSSIBILITY OF PAWN MOVE
#                 section to check if computer's move is possible
#                 left movement """
#             comp_move_chosen_field_left_index = which_pawn_field_index + 7    # the field where computer could put his pawn
#             possible_partial_move = []       # empty list to store possible computer moves
#             if temp_chessb[comp_move_chosen_field_left_index][0].field_status == "Free":  # if field where comp could put his pawn is free, after move pawn to the left
#                 possible_partial_move.append(which_pawn.pawn_name)     # add the pawn which could be moved to list of possibility
#                 possible_partial_move.append(temp_chessb[comp_move_chosen_field_left_index][0].field_name)  # add this free field to that list too
#                 possible_moves.append(possible_partial_move)    # add partial move list to list with all possibility moves
#
#             """ section to check if computer's move is possible
#                 right movement """
#             comp_move_chosen_field_right_index = which_pawn_field_index + 9
#             possible_partial_move = []
#             if temp_chessb[comp_move_chosen_field_right_index][0].field_status == "Free":
#                 possible_partial_move.append(which_pawn.pawn_name)
#                 possible_partial_move.append(temp_chessb[comp_move_chosen_field_right_index][0].field_name)
#                 possible_moves.append(possible_partial_move)
#
#             """ POSSIBILITY OF PAWN CAPTURE
#                 section to check if capture pawn by computer is possible
#                 capturing a pawn to the left """
#             comp_capture_left_field_index = which_pawn_field_index + 14  # the field where comp should put his pawn after capture white pawn
#             possible_partial_captures = []  # empty list to store possible computer moves after capture
#             if temp_chessb[comp_capture_left_field_index][0].field_status == "Free" and temp_chessb[comp_move_chosen_field_left_index][1].pawn_colour == "white": # if the field where comp put his pawn after capture white pawn is free and the pawn which was jumped over by computer if white
#                 possible_partial_captures.append(which_pawn.pawn_name)      # add the pawn which could possible captures to the partial list
#                 possible_partial_captures.append(temp_chessb[comp_capture_left_field_index][0].field_name) # add the field where comp could possible put his pawn after capture enemy's pawn
#                 possible_captures.append(possible_partial_captures)     # add partial possible capture to list with all possible captures
#
#             """ section to check if capture pawn by computer is possible
#                 capturing a pawn to the right """
#             comp_capture_right_field_index = which_pawn_field_index + 18
#             possible_partial_captures = []
#             if temp_chessb[comp_capture_right_field_index][0].field_status == "Free" and temp_chessb[comp_move_chosen_field_right_index][1].pawn_colour == "white":
#                 possible_partial_captures.append(which_pawn.pawn_name)
#                 possible_partial_captures.append(temp_chessb[comp_capture_right_field_index][0].field_name)
#                 possible_captures.append(possible_partial_captures)

def computer_move_and_capture(temp_chessb):
    """ It is a function that performs computer movements and captures the opponent's pieces.
        This function tries to guess human movements.
        This function is really huge. This is no K.I.S.S, but it works. I know.
        This is K.I.W.I -> Keep It Working Idiot  ;-)"""

    possible_moves = []
    possible_captures = []
    possible_enemy_counterattacks = []
    for field in temp_chessb:
        if field[1].pawn_name in black_pawn_names:  # field with pawn which is black
            which_pawn = field[1]  # object -> black pawn
            which_pawn_field_index = temp_chessb.index(field)  # index of field with black pawn
            list_of_distances = [7, 9, 14, 18]
            """ POSSIBILITY OF PAWN MOVE
                section to check if computer's move is possible
                left movement and right movement"""
            for distance in list_of_distances:
                if distance == 7 or distance == 9:
                    comp_move_chosen_field_index = which_pawn_field_index + distance  # the field where computer could put his pawn
                    possible_partial_move = []  # empty list to store possible computer moves
                    if temp_chessb[comp_move_chosen_field_index][0].field_status == "Free":  # if field where comp could put his pawn is free, after move pawn
                        possible_partial_move.append(which_pawn.pawn_name)  # add the pawn which could be moved to list of possibility
                        possible_partial_move.append(temp_chessb[comp_move_chosen_field_index][0].field_name)  # add this free field to that list too
                        possible_moves.append(possible_partial_move)  # add partial move list to list with all possibility moves

                    """ POSSIBILITY OF PAWN CAPTURE
                        section to check if capture pawn by computer is possible
                        capturing a pawn to the left """
                elif distance == 14 or distance == 18:
                    comp_capture_field_index = which_pawn_field_index + distance  # the field where comp should put his pawn after capture white pawn
                    possible_partial_captures = []  # empty list to store possible computer moves after capture
                    enemy_position_index = comp_capture_field_index - (distance // 2)
                    # print(enemy_position_index)
                    if temp_chessb[comp_capture_field_index][0].field_status == "Free" and temp_chessb[int(enemy_position_index)][1].pawn_colour == "white":  # if the field where comp put his pawn after capture white pawn is free and the pawn which was jumped over by computer if white
                        possible_partial_captures.append(which_pawn.pawn_name)  # add the pawn which could possible captures to the partial list
                        possible_partial_captures.append(temp_chessb[comp_capture_field_index][0].field_name)  # add the field where comp could possible put his pawn after capture enemy's pawn
                        possible_captures.append(possible_partial_captures)  # add partial possible capture to list with all possible captures
        
            """ section to check if capture pawn by computer is possible
                capturing a pawn to the right """
    # """ POSSIBILITY OF ENEMY (HUMAN BEING) COUNTERATTACK """
    # for field in temp_chessb:
    #     for y in range(len(possible_moves)):
    #         possible_enemy_counterattacks_partial = []      # empty list to store possibility of human moves
    #         if field[0].field_name in possible_moves[y]:    # if field (from whole chessboard) is in list with possible computer's moves
    #             possible_comp_move_index = temp_chessb.index(field)  # set index of field where possible computer could moves its pawn
    #             possible_enemy_stay_index_left = possible_comp_move_index + 9  # set the index of field where is possibility to stay human's pawn on the left from possibility computer's  position
    #             possible_enemy_stay_index_right = possible_comp_move_index + 7  # set the index of field where is possibility to stay human's pawn on the right from possibility computer's  position
    #             if temp_chessb[possible_enemy_stay_index_left][1].pawn_colour == "white" or temp_chessb[possible_enemy_stay_index_right][1].pawn_colour == "white":  # if the pawn which is in possible field is white
    #                 possible_enemy_counterattacks_partial.append(possible_moves[y][0])  # then add to the partial list [comp's pawn name, possible field name], this is the place where enemy could attack
    #                 possible_enemy_counterattacks_partial.append(temp_chessb[possible_comp_move_index][0].field_name)
    #                 if temp_chessb[possible_comp_move_index][0].field_name not in border_fields_names:      # if field is not in the border_fields_list (where attack isn't possible)
    #                     possible_enemy_counterattacks.append(possible_enemy_counterattacks_partial)         # add that pawn's name and field's name to the last list witch contains coordinates to possible enemy's attack
    #
    #             possible_enemy_stay_index_left_after_capture = possible_comp_move_index + 18  # set the index of field where is possibility to stay human's pawn on the left from possibility computer's  position
    #             possible_enemy_stay_index_right_after_capture = possible_comp_move_index + 14  # set the index of field where is possibility to stay human's pawn on the right from possibility computer's  position
    #             if temp_chessb[possible_enemy_stay_index_left_after_capture][1].pawn_colour == "white" or temp_chessb[possible_enemy_stay_index_right_after_capture][1].pawn_colour == "white":  # if the pawn which is in possible field is white
    #                 possible_enemy_counterattacks_partial.append(possible_moves[y][0])  # then add to the partial list [comp's pawn name, possible field name], this is the place where enemy could attack
    #                 possible_enemy_counterattacks_partial.append(temp_chessb[possible_comp_move_index][0].field_name)
    #                 if temp_chessb[possible_comp_move_index][0].field_name not in border_fields_names:  # if field is not in the border_fields_list (where attack isn't possible)
    #                     possible_enemy_counterattacks.append(possible_enemy_counterattacks_partial)  # add that pawn's name and field's name to the last list witch contains coordinates to possible enemy's attack
    #if len(possible_captures) > 0 and
    
    
    print(possible_moves)
    print(possible_captures)
    print(possible_enemy_counterattacks)
    
    return "black"


main_game()
