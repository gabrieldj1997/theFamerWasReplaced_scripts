import drone
fertilizar = False
multiplicador = 1000000000
def plantar(type):
	if arar(type) and get_ground_type() == Grounds.Grassland:
		till()
	if num_items(Items.Water) > 0 and get_water() < 0.5:
		use_item(Items.Water)
	if can_harvest():
		harvest()
	plant(type)
	if num_items(Items.Fertilizer) > 0 and fertilizar:
		use_item(Items.Fertilizer)
def arar(type):
	dic=[Entities.Bush, Entities.Grass, Entities.Tree]
	if type in dic:
		return False
	return True