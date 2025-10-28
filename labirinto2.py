import drone
import moduloLab

multi = 1000000

def init():
	clear()
	inicial = num_items(Items.Gold)
	nescessario = inicial + (2 * multi)
	while inicial < nescessario:
		drone.centralizar()
		construir()
		pegarTesouro(inicial, nescessario)
		inicial = num_items(Items.Gold)
	return repeticoes

def construir():
	clear()
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def pegarTesouro(inicial, nescessario):
	valorTesouro = (get_world_size() * get_world_size()) * 32
	moduloLab.matriz = {}
	mapa = moduloLab.criarMapa()
	def loop(setor):
		q = 1
		while True:
			maca = measure()
			if maca in setor:
				c = calcularCaminho(mapa, (moduloLab.getPos()), measure())
				while c:
					next = c.pop(len(c)-1)
					if next != moduloLab.getPos():
						drone.mover(next[0],next[1])
						v = moduloLab.vizinhos(moduloLab.getPos())
						if mapa[moduloLab.getPos()] != v:
							mapa[moduloLab.getPos()] = v
				substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
				if q >= 300 or nescessario < inicial + (valorTesouro * q):
					harvest()
					return q
				else:
					use_item(Items.Weird_Substance, substance)
					q += 1
			else:
				while maca == measure():
					move(drone.dic[random() * len(drone.dic) // 1])
					v = moduloLab.vizinhos(moduloLab.getPos())
					if mapa[moduloLab.getPos()] != v:
						mapa[moduloLab.getPos()] = v
	setores = definirSetores()
	for i in range(1, len(setores)+1):
		def initLoop():
			loop(setores[i])
		if i != len(setores):
			spawn_drone(initLoop)
		else:
			initLoop()

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
	
def calcularCaminho(mapa, inicio, fim):
	fila = [inicio]
	visitado = set([inicio])
	anterior = {inicio: None}
	while fila:
		atual = fila.pop(0)
		if atual == fim:
			break
		for conexao in mapa[atual]:
			prox = conexao['square']
			if prox not in visitado:
				visitado.add(prox)
				anterior[prox] = atual
				fila.append(prox)
	caminho = []
	if fim in anterior:
		atual = fim
		while not atual == None:
			caminho.append(atual)
			atual = anterior[atual]
	return caminho