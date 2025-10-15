import drone
import plantacao
			
def colher():
	def row():
		while True:
			harvest()
			plantacao.plantar(Entities.Sunflower)
			move(North)
	for i in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(East)
def init():
	drone.centralizar()
	colher()
		