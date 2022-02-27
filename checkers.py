# CHECKERS
# The Game
# May The Best Win

from game_board import *
from datas import *
import copy
from funct_adds import *
from computer_movement import *
from movement_functions import *


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
def pawns(org_blk_paw_nm, org_whi_paw_nm):
    list_of_all_pawns = []
    black_pawns = {name: Pawn(pawn_name=name) for name in org_blk_paw_nm}
    for blp in black_pawns:
        black_pawns[blp].pawn_colour = "black"
        list_of_all_pawns.append(black_pawns[blp])
    white_pawns = {name: Pawn(pawn_name=name) for name in org_whi_paw_nm}
    for whp in white_pawns:
        white_pawns[whp].pawn_colour = "white"
        list_of_all_pawns.append(white_pawns[whp])
    without_pawns = Pawn(pawn_name="W_O_P", pawn_colour="no_colour")
    list_of_all_pawns.append(without_pawns)
    return list_of_all_pawns
  
    
# A function that creates a game board with the names of all the fields
def chessboard(list_of_pawns):
    list_of_all_fields = []
    fields = {name: Field(field_name=name) for name in all_fields_names}
    for f in fields:
        temp_list = []
        temp_list.append(fields[f])
        temp_list.append((list_of_pawns[-1]))
        list_of_all_fields.append(temp_list)
    
    # For all fields that are not used in the game (white fields) it assigns the status "UNUSED"
    for field in list_of_all_fields:                           # For a field that is on the list of all fields
        if field[0].field_name not in active_fields_names:     # if the field is not on the list of active fields, then
            field[0].field_status = "UNUSED"                   # assign a parameter of the STATUS object as "UNUSED"
    z = 0
    for i in range(0, 24):                                      # otherwise, for the first 24 fields
        if list_of_all_fields[i][0].field_status == "Free":     # change the field status from "Free"
            list_of_all_fields[i][0].field_status = "Occupied"  # on "Occupied", because there will be pawns
        if list_of_all_fields[i][0].field_name in active_fields_names:
            list_of_all_fields[i][1] = list_of_pawns[z]
            z += 1
    y = 12
    for j in range(40, 64):                                     # For last 24 fields
        if list_of_all_fields[j][0].field_status == "Free":     # change the field status from "Free"
            list_of_all_fields[j][0].field_status = "Occupied"  # on "Occupied", because there will be pawns
        if list_of_all_fields[j][0].field_name in active_fields_names:
            list_of_all_fields[j][1] = list_of_pawns[y]
            y += 1

    return list_of_all_fields
  
        
def main_game():
    black_pawn_names = copy.deepcopy(org_black_pawn_names)
    white_pawn_names = copy.deepcopy(org_white_pawn_names)
    list_of_pawns_on_chessboard = pawns(black_pawn_names, white_pawn_names)
    temp_chessboard = copy.deepcopy(chessboard(list_of_pawns_on_chessboard))
    clear_screen()
    start_game_screen()
    player = choose_players()
    time.sleep(2)
    print('\n')
    clear_screen()
    shows_game_board(temp_chessboard, white_pawn_names, black_pawn_names, all_fields_names)
    turn = "white"
   
    while (len(black_pawn_names) > 0) and (len(white_pawn_names) > 0):
        if player == "human":
            move_function = take_user_move(turn, org_white_pawn_names, org_black_pawn_names, active_fields_names)
        elif player == "computer" and turn == "white":
            move_function = take_user_move(turn, org_white_pawn_names, org_black_pawn_names, active_fields_names)
        elif player == "computer" and turn == "black":
            enemy_counterattacks = enemy_counterattack(temp_chessboard, (computer_move(temp_chessboard, org_black_pawn_names, list_of_distances)), list_of_distances, border_fields_names)
            rev_move_function = computer_final_decision_about_move(enemy_counterattacks, (computer_capture(temp_chessboard, org_black_pawn_names, list_of_distances)), computer_move(temp_chessboard, org_black_pawn_names, list_of_distances))
            move_function = rev_move_function[::-1]
            time.sleep(1)

        announcement = move_if_move_is_correct(move_function, temp_chessboard, list_of_pawns_on_chessboard, black_pawn_names, white_pawn_names, org_black_pawn_names, org_white_pawn_names)
        if announcement != "end":
            clear_screen()
            shows_game_board(temp_chessboard, white_pawn_names, black_pawn_names, all_fields_names)
            show_info(announcement)
            turn = whose_turn(announcement)
        else:
            break
            
    answer = end_game_screen(black_pawn_names, white_pawn_names)
    if answer == "n":
        goodbye_screen()
    else:
        main_game()

main_game()

# The lines below are deprecated, but I like them ;)
# def computer_move_and_capture(temp_chessb):
#     """ It is a function that performs computer movements and captures the opponent's pieces.
#         This function tries to guess human movements.
#         This function is really huge. This is no K.I.S.S, but it works. I know.
#         This is K.I.W.I -> Keep It Working Idiot  ;-)"""
#