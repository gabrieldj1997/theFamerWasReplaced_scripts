dic = [North,East,South,West]
def movesPermitidos(xy):
	moves = []
	if xy[0] % 2 == 0:
		if xy[1] != 0:
			moves.append(South)
	else:
		if xy[1] != get_world_size() - 1:
			moves.append(North)
	if xy[1] % 2 == 0:
		if xy[0] != get_world_size() - 1:
			moves.append(East)
	else:
		if xy[0] != 0:
			moves.append(West)
	return moves
def centralizar():
	while get_pos_x() != 0:
		if get_pos_x() > get_world_size() // 2:
			move(East)
		else:
			move(West)
	while get_pos_y() != 0:
		if get_pos_y() > get_world_size() // 2:
			move(North)
		else:
			move(South)
def possivel():
	if not can_move(North) and not can_move(South):
		if not can_move(East) and not can_move(West):
			return False
	return True
def mover(x, y):
	while get_pos_x() != x:
		dx = get_pos_x() - x
		if dx < 0:
			if abs(dx) <= get_world_size() // 2:
				move(East)
			else:
				move(West)
		else:
			if abs(dx) <= get_world_size() // 2:
				move(West)
			else:
				move(East)
	while get_pos_y() != y:
		dy = get_pos_y() - y
		if dy < 0:
			if abs(dy) <= get_world_size() // 2:
				move(North)
			else:
				move(South)
		else:
			if abs(dy) <= get_world_size() // 2:
				move(South)
			else:
				move(North)