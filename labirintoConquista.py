import drone
set_world_size(5)

def verificar():
	while measure() == None:
		continue
	qtd = 1
	while True:
		if qtd >= 300:
			if measure() == (get_pos_x(),get_pos_y()):
				harvest()
			else:
				return			
		tesouro = measure()
		if tesouro == (get_pos_x(),get_pos_y()):
			use_item(Items.Weird_Substance, 5*5)
		while tesouro == measure():
			continue
		qtd += 1
for i in range(5*5):
	def m():
		x, y = (i % 5, i // 5)
		drone.mover(x,y)
		verificar()
	if i != 24:
		spawn_drone(m)
	else:
		m()