import drone

def plantar(type):
	if arar(type) and get_ground_type() == Grounds.Grassland:
		till()
	if num_items(Items.Water) > max_drones():
		use_item(Items.Water)
	if can_harvest():
		harvest()
	plant(type)
	if num_items(Items.Fertilizer) > max_drones():
		use_item(Items.Fertilizer)

def arar(type):
	dic=[Entities.Bush, Entities.Grass, Entities.Tree]
	if type in dic:
		return False
	return True 

def costPlantacao(type):
	cost = get_cost(type)
	can = True
	for item in cost:
		print(item)
		print(num_items(item))
		print(cost[item])
		if num_items(item) < cost[item]:
			can = False
	return can

def companhia(type):
	drone.centralizar()
	while True:
		plantar(type)
		type, cord = get_companion()
		drone.mover(cord[0],cord[1])
		