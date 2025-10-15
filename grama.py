
def init():
	colher()

def colher():
	def row():
		while True:
			harvest()
			move(North)
	for i in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(East)
