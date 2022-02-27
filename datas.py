""" DATAS """

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
org_black_pawn_names = ['BP1', 'BP2', 'BP3', 'BP4',
                        'BP5', 'BP6', 'BP7', 'BP8',
                        'BP9', 'BP10', 'BP11', 'BP12']

# The names of the white pawns
org_white_pawn_names = ['WP1', 'WP2', 'WP3', 'WP4',
                        'WP5', 'WP6', 'WP7', 'WP8',
                        'WP9', 'WP10', 'WP11', 'WP12']

# Names for fields without a pawn
without_pawns_name = ['W_O_P']


list_of_distances = [7, 9, 14, 18]