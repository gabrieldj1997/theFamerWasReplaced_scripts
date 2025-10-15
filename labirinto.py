dic = {North:South, South:North, East:West, West:East}

def init():
		construir()
		resolve()

def construir():
	clear()
	bag = []
	def row():
		for y in range(get_world_size()):
			plant(Entities.Bush)
			move(North)
		return True
	for x in range(get_world_size()):
		while num_drones() >= max_drones():
			continue
		bag.append(spawn_drone(row))
		move(East)
	for i in bag:
		while not wait_for(i):
			continue
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def vizinhos(xy):
	moves = []
	if can_move(East):
		nextId = getId((xy[0]+1,xy[1]))
		moves.append({"id": nextId, "next": East})
	if can_move(West):
		nextId = getId((xy[0]-1,xy[1]))
		moves.append({"id": nextId, "next": West})
	if can_move(North):
		nextId = getId((xy[0],xy[1]+1))
		moves.append({"id": nextId, "next": North})
	if can_move(South):
		nextId = getId((xy[0],xy[1]-1))
		moves.append({"id": nextId, "next": South})
	return moves

def resolve():
	inicio = (get_pos_x(), get_pos_y())
	final = measure()
	bfs(inicio, final)

def getId(xy):
	return xy[1] * get_world_size() + xy[0]

def bfs(inicio, final):
	visitados = []
	bag = []
	def drone():
		control = False
		while not control:
			atual = (get_pos_x(), get_pos_y())
			if atual == final:
				harvest()
				clear()
				init()
			v = vizinhos(atual)
			if not getId(atual) in visitados:
				visitados.append(getId(atual))
				if len(visitados) > 10:
					visitados.pop(0)
			n = len(v)
			for i in range(n):
				if n == 1:
					control = True
				if n == 2 and v[i]["id"] not in visitados:
					move(v[i]["next"])
				if n >= 3:
					if v[i]["id"] not in visitados:
						move(v[i]["next"])
						bag.append(spawn_drone(drone))
						move(dic[v[i]["next"]])
						control = True
		return [True, bag]

	atual = (get_pos_x(), get_pos_y())
	if atual == final:
		harvest()
		clear()
		return True
	visitados.append(getId(atual))
	for vizinho in vizinhos(atual):
		while num_drones() >= max_drones():
			continue
		move(vizinho["next"])
		bag.append(spawn_drone(drone))
		move(dic[vizinho["next"]])