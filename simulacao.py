inicio = get_time()
for i in range(4,33):
	set_world_size(i)
	import labirinto
	antes = num_items(Items.Gold)
	r = labirinto.init()
	quick_print("tamanho do mundo: ", i)
	quick_print("tempo percorrido: ", (get_time() - inicio)/60, "(min)")
	quick_print("repetições: ", r)
	quick_print("valor adquirido: ", num_items(Items.Gold) - antes)
	quick_print("========================================")
	inicio = get_time()
	antes = num_items(Items.Gold)