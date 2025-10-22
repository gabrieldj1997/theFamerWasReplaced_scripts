import drone
import plantacao
def init(number):
	drone.centralizar()
	colher(number * plantacao.multiplicador)
def colher(number):
	def row():
		while num_items(Items.Carrot) < number:
			if get_entity_type() == None:
				plantacao.plantar(Entities.Carrot)	
			if can_harvest():
				plantacao.plantar(Entities.Carrot)				
			move(North)
	for x in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(East)