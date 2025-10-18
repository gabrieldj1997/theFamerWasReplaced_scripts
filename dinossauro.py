import drone

dic = {
	"anti": {East: [East, South, West, North], South: [South, West, North, East], West: [West, North, East, South], North: [North, East, South, West]},
	"horario": {West: [West, South, East, North], North: [North, West, South, East], East: [East, North, West, South], South: [South, East, North, West]}
}

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
	if difY < 0:
		bag.append(North)
	if difX > 0:
		bag.append(West)
	if difY > 0:
		bag.append(South)
	if difX < 0:
		bag.append(East)
	movesPermitidos = drone.movesPermitidos(atual)
	if prioridade in bag and prioridade in movesPermitidos and can_move(prioridade):
		return prioridade
	
	for i in bag:
		if i in movesPermitidos and can_move(i):
			return i
	sentido = sentido_rotacao(atual, maca)
	for i in dic[sentido][prioridade]:
		if i in movesPermitidos and can_move(i):
			return i
	

def init():
	caminho = []
	clear()
	change_hat(Hats.Dinosaur_Hat)
	dir = East
	n_macas = 1
	n_total = (get_world_size() * get_world_size()) - 1
	while True:
		maca = measure()
		xy = (get_pos_x(), get_pos_y())
		if not drone.possivel():
			change_hat(Hats.Brown_Hat)
			return False
		if n_macas == n_total:
			change_hat(Hats.Brown_Hat)
			return True
		while xy != maca:
			dir = nextSquare(maca, dir)
			move(dir)
			xy = (get_pos_x(), get_pos_y())
		n_macas = n_macas + 1

def sentido_diagonal_acima(xy1, xy2):
	y_diagonal = xy1[1] - (-xy1[0] + xy2[0] + xy2[1])
	if y_diagonal > 0:
		return "acima"
	return "baixo"

def sentido_diagonal_baixo(xy1, xy2):
	y_diagonal = xy1[1] - (xy1[0] - xy2[0] + xy2[1])
	if y_diagonal > 0:
		return "acima"
	return "baixo"

def sentido_rotacao(xyDrone, xyMaca):
	if xyDrone[0] - xyMaca[0] < 0:
		sx = '<'
	else:
		sx = '>'
	if xyDrone[0] - xyMaca[0] == 0:
		sx = '='
	if xyDrone[1] - xyMaca[1] < 0:
		sy = '<'
	else:
		sy = '>'
	if xyDrone[1] - xyMaca[1] == 0:
		sy = '='
	dir = (xyMaca[0] % 2, xyMaca[1] % 2)
	if dir == (1,0) or dir == (0,1):
		dir2 = sentido_diagonal_baixo(xyDrone,xyMaca)
	if dir == (1,1) or dir == (0,0):
		dir2 = sentido_diagonal_acima(xyDrone,xyMaca)
	mapa = {
	(1, 0): {  
	('<','>', 'acima'): 'horario',
	('=','>', 'acima'): 'horario',
	('>','>', 'acima'): 'horario',
	('>','>', 'baixo'): 'anti',
	('>','=', 'baixo'): 'anti',
	('>','<', 'baixo'): 'anti',
	('>','<', 'baixo'): 'anti',
	('<','<', 'baixo'): 'horario',
	('<','<', 'cima'): 'anti'
	},
	(0, 0): {
	('<','>', 'baixo'): 'horario',
	('<','>', 'acima'): 'anti',
	('>','>', 'acima'): 'horario',
	('>','=', 'acima'): 'horario',
	('>','<', 'acima'): 'horario',
	('>','<', 'baixo'): 'anti',
	('=','<', 'baixo'): 'anti',
	('<','<', 'baixo'): 'anti'
	},
	(1, 1): {
	('<','>', 'baixo'): 'anti',
	('<','>', 'acima'): 'horario',
	('=','>', 'acima'): 'horario',
	('>','>', 'acima'): 'horario',
	('>','<', 'acima'): 'anti',
	('>','<', 'baixo'): 'horario',
	('<','<', 'baixo'): 'anti',
	('<','=', 'baixo'): 'anti'
	},
	(0, 1): {
	('<','>', 'acima'): 'horario',
	('>','>', 'acima'): 'anti',
	('>','>', 'baixo'): 'horario',
	('>','<', 'baixo'): 'anti',
	('=','<', 'baixo'): 'anti',
	('<','<', 'baixo'): 'anti',
	('<','<', 'acima'): 'horario',
	('<','=', 'acima'): 'horario'
	}
	}
	return mapa[dir][(sx, sy, dir2)]

init()