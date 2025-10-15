import plantacao

def init():
	colher()
	
def colher():
	def row():
		while True:
			while not can_harvest():
				continue
			if can_harvest():
				harvest()
				plantacao.plantar(Entities.Carrot)				
			move(North)
	
	for x in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(East)