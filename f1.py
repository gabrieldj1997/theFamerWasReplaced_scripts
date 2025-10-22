import abobora
while True:
	t = get_time()
	abobora.test()
	n = num_items(Items.Pumpkin)
	harvest()
	quick_print("itens adquiridos:")
	ad = num_items(Items.Pumpkin) - n
	quick_print(ad)
	quick_print("tempo:")
	tt = get_time()-t
	quick_print(tt)
	quick_print("itens adquiridos/s:")
	quick_print(ad//tt)
	quick_print("============================")
