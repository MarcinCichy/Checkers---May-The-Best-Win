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
        # list_black_pawns=[blp]
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
    
    # dla wszystkich pół, które nie sa uzywane w rozgrywce przypisuje status UNUSED
    for field in list_of_all_fields:                                    # dla pola znajdującego sie na liscie wszystkich pól
        if field[0].field_name not in active_fields_names:              # jezeli pole nie jest na liscie pol aktywnych to
            field[0].field_status = "UNUSED"                           # przypisz parametr obiektu STATUS jako UNUSED
    z = 0
    for i in range(0, 24):                                      # w przeciwnym przypadku dla pierwszych 24 pól
        if list_of_all_fields[i][0].field_status == "Free":     # zmień status pola z Free
            list_of_all_fields[i][0].field_status = "Occupied"  # na Occupied, bo tam ustawione będą pionki
        if list_of_all_fields[i][0].field_name in active_fields_names:
            list_of_all_fields[i][1] = pawns()[z]
            z += 1
          
    z = 0
    for j in range(40, 64):
        if list_of_all_fields[j][0].field_status == "Free":  # zmień status pola z Free
            list_of_all_fields[j][0].field_status = "Occupied"  # na Occupied, bo tam ustawione będą pionki
        if list_of_all_fields[j][0].field_name in active_fields_names:
            list_of_all_fields[j][1] = pawns()[z+12]
            z += 1

    return list_of_all_fields


def user_move():
    pawn_name_choose = input("Podaj nazwę pionka: ")
    field_name_choose = input("Podaj nazwę pola: ")
    while pawn_name_choose.upper() not in white_pawn_names and pawn_name_choose.upper() not in black_pawn_names:
        pawn_name_choose = input("Podaj poprawną nazwę pionka: ")
    while field_name_choose.upper() not in active_fields_names:
        field_name_choose = input("Podaj poprawną nazwę pola: ")
    # print(f'The Chosen pawn = {pawn_name_choose.upper()}, the chosen field = {field_name_choose.upper()}')
    return field_name_choose.upper(), pawn_name_choose.upper()
    

def check_which_pawn(move_func):
    which_field = move_func[0]                  # nazwa pola (tylko nazwa)
    which_pawn = move_func[1]                   # nazwa pionka (tylko nazwa)
    print('*'*40)
    ch = chessboard()                           # zamienic na zewnetrzna tabele
    for fields in ch:
        if which_pawn == fields[1].pawn_name:
            which_pawn_colour = ch[ch.index(fields)][1].pawn_colour
            break
    for fields in ch:
        if which_field == fields[0].field_name:
            field_index = ch.index(fields)
            print(f'Choosen field: {which_field}')
            # print(f'Field reads from list: {fields[0].field_name}')
            print(f'Choosen field ({fields[0].field_name}) has status: {fields[0].field_status}')
            print(f'Choosen pawn ({which_pawn}) has colour: {which_pawn_colour}')
            print(f"Field's index is: {field_index}")
            print(f'Into field with index: {field_index} is pawn: {ch[field_index][1].pawn_name}')
            print(f'Which has colour: {ch[field_index][1].pawn_colour}')
            if ch[field_index][1].pawn_colour != which_pawn_colour and ch[field_index][1].pawn_colour != "no_colour":
                print("Checking next field")
            elif ch[field_index][1].pawn_colour == which_pawn_colour and ch[field_index][1].pawn_colour != "no_colour":
                print(f"You can't move on field {fields[0].field_name}")
            elif ch[field_index][0].field_status == "Occupied":
                print("Field is occupied. You can't move there")
            else:
                print(f'You can move on field {fields[0].field_name}')
                # to zrobic procedure, która zmienia zawartosci poszczególnych pol w tablicy temp_chessboard
                
            

check_which_pawn(user_move())