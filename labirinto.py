import drone
import moduloLab

multi = 1000000

def init():
	clear()
	inicial = num_items(Items.Gold)
	nescessario = inicial + (2 * multi)
	repeticoes = 0
	while inicial < nescessario:
		drone.centralizar()
		construir()
		repeticoes += pegarTesouro(inicial, nescessario)
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
	q = 1
	while True:
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