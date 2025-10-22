import drone
import plantacao

def criarTerreno():
	bag = []
	drone.centralizar()
	def row():
		for _ in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
			harvest()
			if get_pos_y() != get_world_size() - 1:
				move(North)
		return True
	for _ in range(get_world_size()):
		while num_drones() >= max_drones():
			continue
		bag.append(spawn_drone(row))
		move(East)
	for i in bag:
		while not wait_for(i):
			continue

def nextSquare(maca, prioridade):
	bag = []
	atual = (get_pos_x(), get_pos_y())
	difX = atual[0] - maca[0]
	difY = atual[1] - maca[1]

	if difX < 0 and difX != 0:
		bag.append(East)
	if difX > 0 and difX != 0:
		bag.append(West)
	if difY < 0 and difY != 0:
		bag.append(North)
	if difY > 0 and difY != 0:
		bag.append(South)

	movesPermitidos = drone.movesPermitidos(atual)

	if prioridade in bag and prioridade in movesPermitidos and can_move(prioridade):
		return prioridade
	
	for i in bag:
		if i in movesPermitidos and can_move(i):
			return i
	
	return movesPermitidos[random() * len(movesPermitidos) // 1]


def init():
	
	caminho = []
	clear()
	plantacao.ararTerra()
	drone.centralizar()
	change_hat(Hats.Dinosaur_Hat)
	dir = East
	n_macas = 1
	n_total = (get_world_size() * get_world_size()) - 1
	passos = 0
	while True:
		maca = measure()
		xy = (get_pos_x(), get_pos_y())
		if not drone.possivel():
			change_hat(Hats.Brown_Hat)
			quick_print("passos init:")
			quick_print(passos)
			return True
		if n_macas == n_total:
			change_hat(Hats.Brown_Hat)
			quick_print("passos init:")
			quick_print(passos)
			return True
		while xy != maca:
			dir = nextSquare(maca, dir)
			move(dir)
			passos = passos + 1
			xy = (get_pos_x(), get_pos_y())
		n_macas = n_macas + 1
	quick_print("passos init:")
	quick_print(passos)

def init2():
	clear()
	change_hat(Hats.Dinosaur_Hat)
	passos = 0
	loop = True
	while loop:
		if not drone.possivel():
			change_hat(Hats.Brown_Hat)
			loop = False
		for i in range(get_world_size()-1):
			move(East)
		move(North)
		for i in range(get_world_size()):
			for x in range(get_world_size()-2):
				if i % 2 == 0:
					move(North)
				else:
					move(South)
				passos = passos + 1
			if i != get_world_size()-1:
				move(West)
			else:
				move(South)
			passos = passos + 1
		continue
	quick_print("passos init2:")
	quick_print(passos)


