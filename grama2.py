import drone
import plantacao
listX = [2, 6, 10, 14, 18, 22, 26, 30]
drone.centralizar()
def colher():
	def poli():
		if get_entity_type() == None:
			till()
		type, xy = get_companion()
		if not xy[0] in listX:
			drone.mover(xy[0],xy[1])
			plantacao.plantar(type)
	while True:
		for _ in range(get_world_size()):
			harvest()
			while num_drones() >= max_drones():
				continue
			spawn_drone(poli)
			move(North)
for i in listX:
	drone.mover(i, 0)
	if i != listX[len(listX) - 1]:
		spawn_drone(colher)
	else:
		colher()
