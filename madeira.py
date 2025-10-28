import drone
import plantacao
def init(number):
	drone.centralizar()
	colher(number * plantacao.multiplicador)
	return True
def colher(number):
	def row():
		n = num_items(Items.Wood)
		while num_items(Items.Wood) < number:
			if can_harvest() or get_entity_type() == None:
				plantar(get_pos_x(),get_pos_y())				
			move(North)
	for x in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(East)
def plantar(x, y):
	if x % 2 == 0 and y % 2 == 0 or x % 2 == 1 and y % 2 == 1:
		plantacao.plantar(Entities.Tree)
	else:
		plantacao.plantar(Entities.Bush)
init(20)