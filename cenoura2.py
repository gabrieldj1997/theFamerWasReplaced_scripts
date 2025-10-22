import drone
import plantacao
listX = [2,5,8,11,14,17,20,23,26,29]
drone.centralizar()
def colher():
	def poli():
		if get_entity_type() == None:
			till()
		type, xy = get_companion()
		
		drone.mover(xy[0],xy[1])
		plantacao.plantar(type)
	while True:
		for _ in range(get_world_size()):
			plantacao.plantar(Entities.Carrot)
			while not spawn_drone(poli):
				continue
			move(North)
for i in listX:
	drone.mover(i, 0)
	if i != listX[len(listX) - 1]:
		spawn_drone(colher)
	else:
		colher()