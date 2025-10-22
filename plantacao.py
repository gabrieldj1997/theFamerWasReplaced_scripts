import drone
fertilizar = False
multiplicador = 1000000000
def plantar(type):
	if get_ground_type() == Grounds.Grassland:
		till()
	if num_items(Items.Water) > max_drones() and get_water() < 0.7:
		use_item(Items.Water)
	if can_harvest():
		harvest()
	plant(type)
	if num_items(Items.Fertilizer) > max_drones() and fertilizar:
		use_item(Items.Fertilizer)
def plantarMundo(type):
	def col():
		for _ in range(get_world_size()):
			plantar(type)
			if get_pos_y() != get_world_size():
				move(North)
	for _ in range(get_world_size()):
		if not spawn_drone(col):
			col()
		move(East)