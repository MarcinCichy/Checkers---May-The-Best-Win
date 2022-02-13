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
# PONIZEJ DO WYWALENIA
border_fields_names = ['A2', 'A4', 'A6', 'A8',
                       'B1', 'D1', 'F1', 'H1',
                       'H3', 'H5', 'H7',
                       'C8', 'E8', 'G8']


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
        
    def pawn_move(self):
        pass


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


def take_user_move():
    pawn_name_choose = input("Enter the name of the pawn: ")
    field_name_choose = input("Enter a field name: ")
    # ask for pawn until chosen pawn is on white or black pawn lists
    while pawn_name_choose.upper() not in white_pawn_names and pawn_name_choose.upper() not in black_pawn_names:
        pawn_name_choose = input("Enter the correct name of the pawn: ")
    # ask for field until chosen field is on active field name list and the move is no longer than 1 field
    while field_name_choose.upper() not in active_fields_names:
        field_name_choose = input("Please enter a valid field name: ")
    return field_name_choose.upper(), pawn_name_choose.upper()
    

def is_move_correct(move_func, temp_chessb):
    which_field = move_func[0]                  # field name (name only, not object)
    which_pawn = move_func[1]                   # pawn name (name only, not object)
    for fields in temp_chessb:
        if which_pawn == fields[1].pawn_name:
            which_pawn_field_index = temp_chessb.index(fields)
            break

    for fields in temp_chessb:
        if which_field == fields[0].field_name:
            chosen_field_index = temp_chessb.index(fields)
            # check distance, is it not too long
            distance = abs(which_pawn_field_index - chosen_field_index)
            if (distance != 7) and (distance != 14) and (distance != 9) and (distance != 18):
                return "You can't move there. Wrong distance."
            elif (abs(which_pawn_field_index-chosen_field_index) == 14) or (abs(which_pawn_field_index-chosen_field_index) == 18):
                info_capture = capture_pawn(temp_chessb, which_pawn_field_index, chosen_field_index)
                return info_capture
            # check that the selected field is free. If yes...
            elif temp_chessb[chosen_field_index][0].field_status == "Free":
                move_pawn(temp_chessb, which_pawn_field_index, chosen_field_index)
                return f'You can move on field: {fields[0].field_name}.'
            # check that the selected field is free. If no...
            elif temp_chessb[chosen_field_index][0].field_status == "Occupied":
                return "Field is occupied. You can't move there."
                
    
def move_pawn(temp_chessb, which_pawn_field_index, chosen_field_index):
    temp_chessb[chosen_field_index][1] = temp_chessb[which_pawn_field_index][1]  # skopiowanie obiektu klasy Pawn z pola gdzie sie znajduje na pole wskazane
    temp_chessb[chosen_field_index][0].field_status = "Occupied"                 # zmiana statusu pola wybranego po przeniesieniu tam pionka
    temp_chessb[which_pawn_field_index][1] = pawns()[-1]                         # ustawienie wartości obiektu klasy Pawn na wartośc W_O_P w dotychczasowym polu
    temp_chessb[which_pawn_field_index][0].field_status = "Free"                 # oraz ustawienie statusu zwolnionego pola na Free


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
        temp_chessb[middle_field_index][1] = pawns()[-1]
        temp_chessb[middle_field_index][0].field_status = "Free"
        move_pawn(temp_chessb, which_pawn_field_index, chosen_field_index)
        return "You captured enemy pawn!"
    
        
def main_game():
    clear_screen()
    start_game_screen()
    print('\n')
    temp_chessboard = chessboard()
    clear_screen()
    shows_game_board(temp_chessboard)
    while (len(black_pawn_names) > 0) or (len(white_pawn_names) > 0):
        info = is_move_correct(take_user_move(), temp_chessboard)
        clear_screen()
        shows_game_board(temp_chessboard)
        print(info)
        # for x in range(64):
        #     if temp_chessboard[x][0].field_status != "UNUSED":
        #         print(temp_chessboard[x][0].field_name, end=", ")
        #         print(temp_chessboard[x][0].field_status, end=", ")
        #         print(temp_chessboard[x][1].pawn_name)
    end_game_screen()


def shows_game_board(temp_chessb):
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
            if temp_chessb[z][1].pawn_name != "W_O_P":      #
                if len(temp_chessb[z][1].pawn_name) == 3:   # for names of pawn which are 3 chars length
                    print('', temp_chessb[z][1].pawn_name, VS, end="")
                else:
                    print(temp_chessb[z][1].pawn_name, VS, end="")  # for names of pawn which are 4 chars length, delete space at front
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
    print(colored(f.renderText("CHECKERS"), "green"))
    time.sleep(1)  # Used time module for program delay
    f = Figlet(font="digital")
    print(colored(f.renderText("       May The Best Win"), "red"))
    time.sleep(2)


def end_game_screen():
    time.sleep(2)
    clear_screen()
    start_screen()
    answer = input(colored("       Do You want play again [Y]es/[N]o ? ", "green"))
    if answer == "n":
        goodbye_screen()
    
    else:
        main_game()
        
    
def goodbye_screen():
    """Shows goodbye screen"""

    clear_screen()
    start_screen()
    f = Figlet(font ="standard")
    print(colored(f.renderText('GOODBYE'), "magenta"))
    
    
main_game()
