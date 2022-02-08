# CHECKERS

import os


def clear_screen():
    """ Clear the screen in depends of operation system (Windows, Linux or iOS).
        It was copied from internet,  I will find out how it works in future (_=system is unknown for me) :)"""
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')


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

  
class Pawn:
    def __init__(self, pawn_name, pawn_colour=None, pawn_place=None, pawn_status=1):
        self.pawn_name = pawn_name
        self.pawn_colour = pawn_colour                # Black or White.
        self.pawn_place = pawn_place                  # The place where pawn is on the board.
        self.pawn_status = pawn_status                # It is on board=1 or not=0. At start all pawns are on the board.
        
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
    without_pawns = Pawn(pawn_name="W_O_P", pawn_colour="no_colour", pawn_status=0)
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


def user_move():
    pawn_name_choose = input("Podaj nazwę pionka: ")
    field_name_choose = input("Podaj nazwę pola: ")
    # ask for pawn until chosen pawn is on white or black pawn lists
    while pawn_name_choose.upper() not in white_pawn_names and pawn_name_choose.upper() not in black_pawn_names:
        pawn_name_choose = input("Podaj poprawną nazwę pionka: ")
    # ask for field until chosen field is on active field name list and the move is no longer than 1 field
    while field_name_choose.upper() not in active_fields_names or is_move_correct([field_name_choose.upper(), "W_O_P"], temp_chessboard) == "wrong":
    # while field_name_choose.upper() not in active_fields_names:
        field_name_choose = input("Podaj poprawną nazwę pola: ")
    return field_name_choose.upper(), pawn_name_choose.upper()
    

def is_move_correct(move_func, temp_chessb):
    which_field = move_func[0]                  # field name (name only, not object)
    which_pawn = move_func[1]                   # pawn name (name only, not object)
    print('*'*40)
    for fields in temp_chessb:
        if which_pawn == fields[1].pawn_name:
            which_pawn_colour = temp_chessb[temp_chessb.index(fields)][1].pawn_colour
            which_pawn_field_index = temp_chessb.index(fields)
            break

    for fields in temp_chessb:
        if which_field == fields[0].field_name:
            chosen_field_index = temp_chessb.index(fields)
            # check distance, is it not too long
            if (which_pawn_field_index - chosen_field_index < 7) and (which_pawn_field_index - chosen_field_index > 18):
            # if (which_pawn_field_index-chosen_field_index !=7) and (which_pawn_field_index-chosen_field_index !=9):
                print("Distance is too long")
                return "wrong"
            if temp_chessb[chosen_field_index][0].field_status == "Free":
                # move pawn with "move_pawn()" function
                # remove print below
                print(f'You can move on field {fields[0].field_name}')
                move_pawn(temp_chessb, which_pawn_field_index, chosen_field_index)
            elif temp_chessb[chosen_field_index][1].pawn_colour == which_pawn_colour:
                # remove print below and return error
                # print(f'kolor pionka na wybranym polu: {temp_chessb[chosen_field_index][1].pawn_colour}')
                # print(f'kolor wybranego pionka: {which_pawn_colour}')
                print("Field is occupied by your pawn. You can't move there")
            elif temp_chessb[chosen_field_index][1].pawn_colour != which_pawn_colour:
                # uwaga tutaj dorobic fukcje, ktora kasuje pionek z listy po jego przekroczeniu
                print("Checking next field")
                print(f'kolor pionka na wybranym polu: {temp_chessb[chosen_field_index][1].pawn_colour}')
                print(f'kolor wybranego pionka: {which_pawn_colour}')
                print(chosen_field_index)
                print(which_pawn_field_index-chosen_field_index)
                if (which_pawn_field_index-chosen_field_index == abs(7)):
                    chosen_field_index += 7
                    print(chosen_field_index)
                elif (which_pawn_field_index - chosen_field_index == abs(9)):
                    chosen_field_index += 9
                    print(chosen_field_index)

            """
            bardzo wazne informacja ponizej jest:
            Sprawdz czy nie podano zakresu większego niż jedno pole -> gotowe
            Sprawdz czy wybrane pole jest wolne, jezeli tak to przesun tam pionek -> gotowe.
            Jezeli nie, to sprawdz jakiego koloru jest tam pionek -> gotowe
            jezeli twojego koloru, to nie mozesz tam isc -> gotowe
            jezeli przeciwnego, to sprawdz co jest w nastepnym polu za tym pionkiem
            jezeli jest wolne, to przenies tam pinkek i wykasuj pionek, który przeskoczyles.
            jezeli jest zajete, to nie mozesz tam isc
            """
                
                
            # print(f'Chosen field: {which_field}')
            # print(f'Chosen field ({fields[0].field_name}) has status: {fields[0].field_status}')
            # print(f'Chosen pawn ({which_pawn}) has colour: {which_pawn_colour}')
            # print(f'Chosen pawn occupied field with index: {which_pawn_field_index}')
            # print(f"Field's index is: {chosen_field_index}")
            # print(f'Into field with index: {chosen_field_index} is pawn: {temp_chessb[chosen_field_index][1].pawn_name}')
            # print(f'Which has colour: {temp_chessb[chosen_field_index][1].pawn_colour}')
    
def move_pawn(temp_chessb, which_pawn_field_index, chosen_field_index):
    # what I need:
    # which_pawn_field_index, chosen_field_index
    print('*' * 40)
    # do przesunięcia pionka
    # [0] - obiekt klasy Field
    # [1] - obiekt klasy Pawn
    # chosen_field - wybrane pole
    # which_pawn_field - pole, na którym jest wybrany pionek
    temp_chessb[chosen_field_index][1] = temp_chessb[which_pawn_field_index][1]  # skopiowanie obiektu klasy Pawn z pola gdzie sie znajduje na pole wskazane
    temp_chessb[chosen_field_index][0].field_status = "Occupied"                 # zmiana statusu pola wybranego po przeniesieniu tam pionka
    temp_chessb[which_pawn_field_index][1] = pawns()[-1]                         # ustawienie wartości obiektu klasy Pawn na wartośc W_O_P w dotychczasowym polu
    temp_chessb[which_pawn_field_index][0].field_status = "Free"                 # oraz ustawienie statusu zwolnionego pola na Free


def main_game():
    temp_chessboard = chessboard()
    # zrobic warunek, który ogranicza czas gry do wyzerowania listy pinkow czarnych lub bialych
    while True:
        # for x in range(64):
        #     if temp_chessboard[x][0].field_status != "UNUSED":
        #         print(temp_chessboard[x][0].field_name, end=", ")
        #         print(temp_chessboard[x][0].field_status, end=", ")
        #         print(temp_chessboard[x][1].pawn_name)
        # print('*'*40)
        is_move_correct(user_move(), temp_chessboard)
        for x in range(64):
            if temp_chessboard[x][0].field_status != "UNUSED":
                print(temp_chessboard[x][0].field_name, end=", ")
                print(temp_chessboard[x][0].field_status, end=", ")
                print(temp_chessboard[x][1].pawn_name)
            

main_game()
