""" FUNCTION TO SHOW GAMEBOARD """


from termcolor import colored


"""
    shortcuts for Unicode signs to draw chessboard
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


def shows_game_board(temp_chessb, wh_paw_nam, bla_paw_nam, all_fi_nm):
	"""
	Shows chessboard. Uses Unicode signs to draw chessboard.
		Uses prepared earlier shortcuts for every needed signs.
	"""
	
	# clear_screen()
	cols = all_fi_nm[0:8]  # all_fields_names
	rows = all_fi_nm[::8]  # all_fields_names
	
	# cols = 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'
	# rows = 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'

	# chessboard header
	print(LUC, end="")
	for i in range(0, 29, 4):
		print(HS * 5 + HUHC, end="")  # the top line of the chessboard header
	print(HS * 5 + RUC)
	print(VS, '   ', VS, end='')  # first free field
	for x in range(8):
		print(' ', cols[x][1], '', VS, end="")  # shows digits from 1 to 8 into first row
	print('\n', end="")  # next line start draw from new line, but don't make one empty line
	print(VRHC, end="")
	for i in range(0, 29, 4):
		print(HS * 5 + DCR, end="")  # the middle line of the chessboard
	print(HS * 5 + VLHC)
	
	# chessboard body
	for y in range(8):
		print(VS, '', rows[y][0], '', VS, end="")  # shows letters from A to H at the left side of chessboard
		for z in range(y * 8, y * 8 + 8):
			colored_pawn = None
			if temp_chessb[z][1].pawn_name in wh_paw_nam:
				colored_pawn = colored(temp_chessb[z][1].pawn_name, "yellow")
			elif temp_chessb[z][1].pawn_name in bla_paw_nam:
				colored_pawn = colored(temp_chessb[z][1].pawn_name, "blue")
			if temp_chessb[z][1].pawn_name != "W_O_P":  #
				if len(temp_chessb[z][1].pawn_name) == 3:  # for names of pawn which are 3 chars length
					print('', colored_pawn, VS, end="")
				else:
					print(colored_pawn, VS, end="")  # for names of pawn which are 4 chars length, delete space at front
			else:
				if temp_chessb[z][0].field_status != "UNUSED":
					print('    ', VS, end="")
				else:
					print(WF, '', WF, VS, end="")  # shows empty field for fields value W_O_P (without pawn)
		print('\n', end="")  # next line start draw from new line
		
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