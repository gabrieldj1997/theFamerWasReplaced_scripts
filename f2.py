def definirSetores():
	setores = {}
	tamanho_setor = 8
	tamanho_matriz = get_world_size() 
	num_setores_por_dimensao = tamanho_matriz // tamanho_setor
	cont = 1
	for y_bloco in range(num_setores_por_dimensao):
		for x_bloco in range(num_setores_por_dimensao):
			xy1 = (x_bloco * tamanho_setor, y_bloco * tamanho_setor)
			xy2 = (xy1[0] + tamanho_setor - 1, xy1[1] + tamanho_setor - 1)
			coordenadas_xy = []
			for y in range(xy1[1], xy2[1] + 1):
				for x in range(xy1[0], xy2[0] + 1):
					coordenadas_xy.append((x, y))
			setores[cont] = coordenadas_xy
			cont += 1
	return setores
	
		
quick_print(definirSetores())

#(a,b) => b * n_world + a = id
#(7,5) => 5 * 8 + 7 = 47

#id => 
#47 => x = 47 % 8, y = 47 // 8