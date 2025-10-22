import drone
import plantacao
def test():
	drone.centralizar()
	start()
	return True
def init(number):
	drone.centralizar()
	n = num_items(Items.Pumpkin)
	num_abobora = num_items(Items.Pumpkin)
	while num_items(Items.Pumpkin) < num_abobora + (number * plantacao.multiplicador):
		start()
	return True
def start():
	bagDrones = []
	def verificar():
		while True:
			control = True
			for y in range(get_world_size()):
				if not can_harvest() or get_entity_type() == Entities.Dead_Pumpkin:
					if get_entity_type() == Entities.Dead_Pumpkin:
						plantacao.plantar(Entities.Pumpkin)
					control = False
				move(North)
			if control:
				return True
	def plantar():
		for y in range(get_world_size()):
			plantacao.plantar(Entities.Pumpkin)		
			move(North)
		verificar()
		return True
	for x in range(get_world_size()):
		if x != get_world_size() - 1:
			while num_drones() >= max_drones():
				continue
			bagDrones.append(spawn_drone(plantar))
			move(East)
		else:
			plantar()
	for drone in bagDrones:
		while not wait_for(drone):
			continue
	return True