""" Functions responsible for moving pawns through the computer """

import time
import random as r


def computer_move(temp_chessb, org_blk_pa_nms, li_of_dist):
	""" POSSIBILITY OF COMPUTER'S PAWN MOVE
		function to check if computer's move is possible """
	possible_moves = []
	for field in temp_chessb:
		if field[1].pawn_name in org_blk_pa_nms:  # field with pawn which is black
			which_pawn = field[1]  # object -> black pawn
			which_pawn_field_index = temp_chessb.index(field)  # index of field with black pawn
			
			for distance in li_of_dist:
				if distance == 7 or distance == 9:
					comp_move_chosen_field_index = which_pawn_field_index + distance  # the field where computer could put his pawn
					possible_partial_move = []  # empty list to store possible computer moves
					if comp_move_chosen_field_index > 63:
						continue
					else:
						if temp_chessb[comp_move_chosen_field_index][
							0].field_status == "Free":  # if field where comp could put his pawn is free, after move pawn
							possible_partial_move.append(
								which_pawn.pawn_name)  # add the pawn which could be moved to list of possibility
							possible_partial_move.append(temp_chessb[comp_move_chosen_field_index][
															 0].field_name)  # add this free field to that list too
							possible_moves.append(
								possible_partial_move)  # add partial move list to list with all possibility moves
	return possible_moves


def computer_capture(temp_chessb, org_blk_pa_nms, li_of_dist):
	""" POSSIBILITY OF HUMAN'S PAWN CAPTURE BY COMPUTER
		function to check if capture pawn by computer is possible """
	
	possible_captures = []
	for field in temp_chessb:
		if field[1].pawn_name in org_blk_pa_nms:  # field with pawn which is black
			which_pawn = field[1]  # object -> black pawn
			which_pawn_field_index = temp_chessb.index(field)  # index of field with black pawn
			
			for distance in li_of_dist:
				if distance == 14 or distance == 18:
					if which_pawn_field_index >= 48:
						pass
					else:
						comp_capture_field_index = which_pawn_field_index + distance  # the field where comp should put his pawn after capture white pawn
						possible_partial_captures = []  # empty list to store possible computer moves after capture
						if comp_capture_field_index > 63:
							continue
						else:
							enemy_position_index = comp_capture_field_index - (distance // 2)
							# print(enemy_position_index)
							
							if temp_chessb[comp_capture_field_index][0].field_status == "Free" and \
									temp_chessb[int(enemy_position_index)][
										1].pawn_colour == "white":  # if the field where comp put his pawn after capture white pawn is free and the pawn which was jumped over by computer if white
								possible_partial_captures.append(
									which_pawn.pawn_name)  # add the pawn which could possible captures to the partial list
								possible_partial_captures.append(temp_chessb[comp_capture_field_index][
																	 0].field_name)  # add the field where comp could possible put his pawn after capture enemy's pawn
								possible_captures.append(
									possible_partial_captures)  # add partial possible capture to list with all possible captures
	return possible_captures


def enemy_counterattack(temp_chessb, possible_moves, li_of_dist, brd_fie_nms):
	""" POSSIBILITY OF ENEMY (HUMAN BEING) COUNTERATTACK """
	possible_enemy_counterattacks = []
	for f in temp_chessb:
		for y in range(len(possible_moves)):
			if f[0].field_name in possible_moves[
				y]:  # if field (from whole chessboard) is in list with possible computer's moves
				# index field where computer movement is allowed
				possible_comp_move_index = temp_chessb.index(
					f)  # set index of field where possible computer could moves its pawn
				# for all possible distances (7,9, 14 i 18)
				for distance in  li_of_dist:
					if distance < 10:  # only for moves, without captures
						# possible_enemy_counterattacks_partial = []  # empty list to store possibility of human moves
						possible_enemy_stay_index = possible_comp_move_index + distance  # set the index of field where it is possibility to stay human's pawn -> this is index of possible move plus distance
						if possible_enemy_stay_index > 63:
							continue
						else:
							if temp_chessb[possible_enemy_stay_index][
								1].pawn_colour == "white":  # if the pawn which is in possible field is white
								possible_enemy_counterattacks_partial = possible_moves[
									y]  # then add to the partial list [comp's pawn name, possible field name], this is the place where enemy could attack
								if temp_chessb[possible_comp_move_index][
									0].field_name not in brd_fie_nms and possible_enemy_counterattacks_partial not in possible_enemy_counterattacks:  # if field is not in the border_fields_list (where attack isn't possible)
									possible_enemy_counterattacks.append(
										possible_enemy_counterattacks_partial)  # add that pawn's name and field's name to the last list witch contains coordinates to possible enemy's attack
					else:
						pass
	return possible_enemy_counterattacks


def computer_final_decision_about_move(poss_enemy_counterattack, poss_captures, poss_mov):
	computer_possible_moves = []
	for items in poss_mov:
		if items not in poss_enemy_counterattack:
			computer_possible_moves.append(items)
		else:
			computer_possible_moves = poss_enemy_counterattack
	
	time.sleep(1)  # Imagine that computer thinks ;)
	if len(poss_captures) > 0:
		which_move = poss_captures[r.randrange(len(poss_captures))]
		return which_move
	elif len(computer_possible_moves) > 0:
		which_move = computer_possible_moves[r.randrange(len(computer_possible_moves))]
		return which_move