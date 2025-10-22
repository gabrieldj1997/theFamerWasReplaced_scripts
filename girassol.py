import drone
import plantacao
def init(number):
	drone.centralizar()
	colher(number * plantacao.multiplicador)
def colher(number):
	def row():
		while num_items(Items.Power) < number:
			harvest()
			plantacao.plantar(Entities.Sunflower)
			move(North)
	for i in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(East)
		