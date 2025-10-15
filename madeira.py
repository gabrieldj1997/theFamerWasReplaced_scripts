import plantacao

def init():
	colher()
	
def colher():
	def row():
		while True:
			if get_entity_type() == None:
				plantar(get_pos_x(),get_pos_y())
			if can_harvest():
				harvest()
				plantar(get_pos_x(),get_pos_y())				
			move(North)

	for x in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(East)

def plantar(x, y):
	if x % 2 == 0:
		if y % 2 == 0:
			plantacao.plantar(Entities.Bush)
		else:
			plantacao.plantar(Entities.Tree)
	else:
		if y % 2 == 0:
			plantacao.plantar(Entities.Tree)
		else:
			plantacao.plantar(Entities.Bush)