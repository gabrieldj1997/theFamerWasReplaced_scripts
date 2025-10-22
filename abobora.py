import drone
import plantacao
multiplicador = 1000000000
def init(number):
	drone.centralizar()
	while num_items(Items.Pumpkin) < (number * multiplicador):
		start()
def start():
	bagDrones = []
	def verificar():
		for y in range(get_world_size()):
			while not can_harvest() or get_entity_type() == Entities.Dead_Pumpkin:
				if get_entity_type() == Entities.Dead_Pumpkin:
					plantacao.plantar(Entities.Pumpkin)
				continue
			move(North)
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