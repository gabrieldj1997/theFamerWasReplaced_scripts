import plantacao
import drone
def plantar():
	bag = []
	def row():
		for y in range(get_world_size()):
			plantacao.plantar(Entities.Cactus)			
			move(North)
		return True
	for x in range(get_world_size()):
		if num_drones() >= max_drones():
			row()
			break
		if x != get_world_size() - 1:
			bag.append(spawn_drone(row))
		move(East)
	for i in bag:
		while not wait_for(i):
			continue
def trocar(cord):
	control = True
	center = measure()
	if cord == North:
		up = measure(North)
		down = measure(South)	
		if get_pos_y() != get_world_size()-1:
			if center > up:
				swap(North)
				control = False	
		if get_pos_y() != 0:
			if center < down:
				swap(South)
				control = False
	if cord == East:
		left = measure(West)
		right = measure(East)	
		if get_pos_x() != get_world_size()-1:
			if center > right:
				swap(East)
				control = False	
		if get_pos_x() != 0:
			if center < left:
				swap(West)
				control = False
	if not control:
		trocar(cord)
	return control
def organizar():
	for i in [(North, East), (East, North)]:
		drone.centralizar()
		def row():
			while True:
				control = True
				for _ in range(get_world_size()):
					c = trocar(i[1])
					if control:
						control = c
					move(i[1])
				if control:
					return True
		drone.centralizar()
		bag = []
		for x in range(get_world_size()):
			d = spawn_drone(row)
			if d != None:
				bag.append(d)
				move(i[0])
			else:
				row()
		for x in bag:
			wait_for(x)
			
def init(number):
	n = num_items(Items.Cactus)
	while num_items(Items.Cactus) < (number * plantacao.multiplicador):
		drone.centralizar()
		plantar()
		organizar()
		harvest()
	return True