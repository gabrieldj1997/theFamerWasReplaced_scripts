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
	x = get_pos_x()
	y = get_pos_y()
	for i in range(x):
		move(West)
	for i in range(y):
		move(South)
def possivel():
	if not can_move(North) and not can_move(South):
		if not can_move(East) and not can_move(West):
			return False
	return True

def mover(x, y):
	while get_pos_x() != x or get_pos_y() != y: 
		difX = abs(get_pos_x() - x)
		difY = abs(get_pos_y() - y)

		for i in range(difX):
			if not possivel():
				return False
			if(get_pos_x() < x):
				if not move(East):
					move(dic[random()*len(dic)//1])
			else:
				if not move(West):
					move(dic[random()*len(dic)//1])
		for i in range(difY):
			if not possivel():
				return False
			if(get_pos_y() < y):
				if not move(North):
					move(dic[random()*len(dic)//1])
			else:
				if not move(South):
					move(dic[random()*len(dic)//1])
