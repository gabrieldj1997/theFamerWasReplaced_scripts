import drone
#tamanho maximo do campo para preenche-lo completamente com drones
set_world_size(5)

def recolher():
	while True:
		for i in range(300):
			if get_entity_type() == Entities.Treasure:
				use_item(Items.Weird_Substance, 5*32)
		if get_entity_type() == Entities.Treasure:
			harvest()
			plant(Entities.Bush)
			use_item(Items.Weird_Substance, 5*32)
def aguardar():
	if get_pos_x() == 4 and get_pos_y() == 4:
		plant(Entities.Bush)
		use_item(Items.Weird_Substance, 5*32)
	while measure() == None:
		continue
	recolher()

for y in range(get_world_size()):
	for x in range(get_world_size()):
		def m():
			drone.mover(x,y)
			aguardar()
		if x == 4 and y == 4:
			m()
		else:
			spawn_drone(m)