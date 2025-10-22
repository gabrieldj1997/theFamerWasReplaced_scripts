import drone
import plantacao
def init(number):
	clear()
	drone.centralizar()
	colher(number * plantacao.multiplicador)
	return True

def colher(number):
	def row():
		while num_items(Items.Hay) < number:
			harvest()
			move(North)
	for i in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(East)
