dicDir = {North:South, East:West, South:North, West:East}
matriz = {}

def vizinhos(xy):
	vizinhos = []
	if can_move(North):
		vizinhos.append({"square":(xy[0], xy[1]+1), "dir": North})
	if can_move(East):
		vizinhos.append({"square":(xy[0]+1, xy[1]), "dir": East})
	if can_move(South):
		vizinhos.append({"square":(xy[0], xy[1]-1), "dir": South})
	if can_move(West):
		vizinhos.append({"square":(xy[0]-1, xy[1]), "dir": West})
	return vizinhos

def getPos():
	return (get_pos_x(), get_pos_y())

def d(dir):
	bagDrones = []
	matriz = {}
	while True:
		v = vizinhos(getPos())
		matriz[getPos()] = v
		if len(v) == 1:
			return (True, matriz, bagDrones)
		if len(v) == 2:
			for vizinho in v:
				if vizinho["dir"] != dicDir[dir]:
					viz = vizinho["dir"]
			move(viz)
			dir = viz
		if len(v) > 2:
			qtdDrone = -1
			for vizinho in v:
				if not vizinho["square"] in matriz and vizinho["dir"] != dicDir[dir]:
					qtdDrone += 1
			for vizinho in v:
				def droneMove():
					move(vizinho["dir"])
					r = d(vizinho["dir"])
					return r
				if vizinho["dir"] != dicDir[dir]:
					if qtdDrone > 0:
						while num_drones() >= max_drones():
							continue
						bagDrones.append(spawn_drone(droneMove))
						qtdDrone -= 1
					else:
						viz = vizinho["dir"]
			move(viz)
			dir = viz
			
def criarMapa():
	bagDrones = []
	matriz[getPos()] = vizinhos(getPos())
	for vizinho in matriz[getPos()]:
		def droneMove():
			move(vizinho["dir"])
			r = d(vizinho["dir"])
			return r
		bagDrones.append(spawn_drone(droneMove))
	for i in bagDrones:
		result = wait_for(i)
		m = result[1]
		for square in m:
			if not square in matriz:
				matriz[square] = m[square]
	aguardar(bagDrones)
	return matriz
def aguardar(bag):
	for i in bag:
		result = wait_for(i)
		if result[2]:
			aguardar(result[2])
		m = result[1]
		for square in m:
			if not square in matriz:
				matriz[square] = m[square]	

