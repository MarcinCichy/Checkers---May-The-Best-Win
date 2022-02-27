def take_user_move(who_turn, org_whi_pa_nms, org_blk_pa_nms, acti_fiel_nms):
	print(f"Now it's turn: {who_turn}")
	pawn_name_choose = input("Enter the name of the pawn: ")
	if pawn_name_choose == "end":
		return "end"
	else:
		# ask for pawn until chosen pawn is on white or black pawn lists and the colour of pawn is equal who_turn
		if who_turn == "white":
			while pawn_name_choose.upper() not in org_whi_pa_nms:
				pawn_name_choose = input("Enter the correct name of the pawn: ")
		elif who_turn == "black":
			while pawn_name_choose.upper() not in org_blk_pa_nms:
				pawn_name_choose = input("Enter the correct name of the pawn: ")
		field_name_choose = input("Enter a field name: ")
		
		# ask for field until chosen field is on active field name list
		while field_name_choose.upper() not in acti_fiel_nms:
			field_name_choose = input("Please enter a valid field name: ")
		return field_name_choose.upper(), pawn_name_choose.upper()


def move_if_move_is_correct(move_func, temp_chessb, list_of_pawns, bla_paw_nm, whi_paw_nm, org_bla_paw_nm, org_whi_paw_nm):
	# print(move_func[0])
	if move_func == "end":
		return "end"
	else:
		which_field = move_func[0]  # field name (name only, not object)
		which_pawn = move_func[1]  # pawn name (name only, not object)
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
				elif ((which_pawn in org_whi_paw_nm) and distance < 0) or (
						(which_pawn in org_bla_paw_nm) and distance > 0):
					return f"You can't move back your pawn."
				elif (abs(which_pawn_field_index - chosen_field_index) == 14) or (
						abs(which_pawn_field_index - chosen_field_index) == 18):
					info_capture = capture_pawn(temp_chessb, which_pawn_field_index, chosen_field_index, list_of_pawns,
												whi_paw_nm, bla_paw_nm)
					return info_capture
				# check that the selected field is free. If yes...
				elif temp_chessb[chosen_field_index][0].field_status == "Free":
					info_move = move_pawn(temp_chessb, which_pawn_field_index, chosen_field_index, list_of_pawns)
					return info_move
				# check that the selected field is free. If no...
				elif temp_chessb[chosen_field_index][0].field_status == "Occupied":
					return "Field is occupied. You can't move there."


def move_pawn(temp_chessb, which_pawn_field_index, chosen_field_index, list_of_pawns):
	temp_chessb[chosen_field_index][1] = temp_chessb[which_pawn_field_index][
		1]  # copying a Pawn class object from the field where it is to the indicated field
	temp_chessb[chosen_field_index][
		0].field_status = "Occupied"  # change the status of a field selected after moving a pawn there
	temp_chessb[which_pawn_field_index][1] = list_of_pawns[
		-1]  # setting the value of the Pawn class object to the value W_O_P in the current field
	temp_chessb[which_pawn_field_index][0].field_status = "Free"  # and setting the status of the released field to Free
	return temp_chessb[chosen_field_index][1].pawn_colour


def capture_pawn(temp_chessb, which_pawn_field_index, chosen_field_index, list_of_pawns, whi_paw_nm, bla_paw_nm):
	middle_field_index = None
	if which_pawn_field_index - chosen_field_index == -14:
		middle_field_index = (which_pawn_field_index + 7)
	elif which_pawn_field_index - chosen_field_index == 14:
		middle_field_index = (which_pawn_field_index - 7)
	elif which_pawn_field_index - chosen_field_index == -18:
		middle_field_index = (which_pawn_field_index + 9)
	elif which_pawn_field_index - chosen_field_index == 18:
		middle_field_index = (which_pawn_field_index - 9)
	
	if temp_chessb[middle_field_index][0].field_status == "Free":
		return "You can't move there. You can't jump over free field."
	elif temp_chessb[middle_field_index][1].pawn_colour == temp_chessb[which_pawn_field_index][1].pawn_colour:
		return "You can't move there. You can't jump over your own pawn."
	else:
		if temp_chessb[middle_field_index][1].pawn_colour == "white":
			whi_paw_nm.remove(temp_chessb[middle_field_index][1].pawn_name)
		elif temp_chessb[middle_field_index][1].pawn_colour == "black":
			bla_paw_nm.remove(temp_chessb[middle_field_index][1].pawn_name)
		# three lines below delete captured pawn from chessboard and move the pawn
		temp_chessb[middle_field_index][1] = list_of_pawns[-1]
		temp_chessb[middle_field_index][0].field_status = "Free"
		info_move = move_pawn(temp_chessb, which_pawn_field_index, chosen_field_index, list_of_pawns)
		return info_move