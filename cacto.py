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
			
def trocar():
	control = True
	center = measure()
	right = measure(East)
	up = measure(North)
	down = measure(South)
	left = measure(West)
							
	if get_pos_y() != get_world_size()-1:
		if center > up:
			swap(North)
			control = False
									
	if get_pos_x() != get_world_size()-1:
		if center > right:
			swap(East)
			control = False
					
	if get_pos_y() != 0:
		if center < down:
			swap(South)
			control = False
									
	if get_pos_x() != 0:
		if center < left:
			swap(West)
			control = False

	if not control:
		trocar()
	return control
		
def organizar():
	def row():
		n = 0
		while True:
			control = True
			for i in range(get_world_size()):
				c = trocar()
				if control:
					control = c
				move(North)
			
			if control:
				if n > 0:
					control = False
				return [True, control]
			n = n + 1

	while True:
		control = True
		drone.centralizar()
		bag = []
		for i in range(2):
			for x in range(get_world_size()):
				while num_drones() >= ((get_world_size() + 1) // 2) + 1:
					continue
				if x % 2 == i:
					bag.append(spawn_drone(row))
				move(East)
			for i in bag:
				while not wait_for(i)[0]:
					continue
				if control:
					control = wait_for(i)[1]
			if control:
				return True

		

def init():
	while True:
		plantar()
		organizar()
		harvest()