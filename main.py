#Algoritmo genético by Wilton
#simulação jogo pacman


from random import randint

movimentos = ['←','↑','→','↓','↖','↗','↘','↙']
posicaoRelativa = [[-1,0],[0,1],[1,0],[0,-1],[-1,1],[1,1],[1,-1],[-1,-1]]

#definição do ambiente e quantidade de movimentos (genes)
QTDMOVIMENTOS = 39
TAMTABULEIRO = 40

solucaoEncontrada = False
individuo = []
posFruta = [30,-38] #considerando uma matriz 5x5

def fitness(indv):
	global  posFruta, posicaoRelativa, movimentos, solucaoEncontrada
	
	count = 0
	#calcula a posição final do individuo
	posFinalIndividuo=[0,0]
	distancia = (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5	
	for mov in indv:
		#verifica colisão
		if (posFinalIndividuo[0] + posicaoRelativa[movimentos.index(mov)][0] >= 0) and (posFinalIndividuo[1] + posicaoRelativa[movimentos.index(mov)][1] <= 0) and (posFinalIndividuo[0] + posicaoRelativa[movimentos.index(mov)][0] <= TAMTABULEIRO-1) and (posFinalIndividuo[1] + posicaoRelativa[movimentos.index(mov)][1] >= 1-TAMTABULEIRO): 
			
			
			posFinalIndividuo[0] += posicaoRelativa[movimentos.index(mov)][0] #atualizando x
			posFinalIndividuo[1] += posicaoRelativa[movimentos.index(mov)][1] #atualizando y
			
			if(distancia > (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5):
		
				distancia = (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5	
				count+=1	
			if(distancia == 0):
				print('SOLUÇÃO ENCONTRADA!')
				solucaoEncontrada = True
				break
		
		
	return count	

def getMelhorMovimento(indv, pos):
	global  posFruta, posicaoRelativa, movimentos, QTDMOVIMENTOS
	melhorMovimento = 0
	posFinalIndividuo=[0,0]
	distancia = (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5	 
	for m in movimentos:
		indv = indv[0:pos-1]+[m]+indv[pos:QTDMOVIMENTOS-1]
		for mov in indv:
			#verifica colisão
			if (posFinalIndividuo[0] + posicaoRelativa[movimentos.index(mov)][0] >= 0) and (posFinalIndividuo[1] + posicaoRelativa[movimentos.index(mov)][1] <= 0) and (posFinalIndividuo[0] + posicaoRelativa[movimentos.index(mov)][0] <= TAMTABULEIRO-1) and (posFinalIndividuo[1] + posicaoRelativa[movimentos.index(mov)][1] >= 1-TAMTABULEIRO): 
			
			
				posFinalIndividuo[0] += posicaoRelativa[movimentos.index(mov)][0] #atualizando x
				posFinalIndividuo[1] += posicaoRelativa[movimentos.index(mov)][1] #atualizando y
			
			
		if(distancia > (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5):
			melhorMovimento = movimentos.index(mov)
			distancia = (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5	
		
	return melhorMovimento	
			

def getPosPrimeiroSuspeito(indv):
	global  posFruta, posicaoRelativa, movimentos
	pos = 0
	posFinalIndividuo=[0,0]
	distancia = (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5	
	for mov in indv:
		posFinalIndividuo[0] += posicaoRelativa[movimentos.index(mov)][0] #atualizando x
		posFinalIndividuo[1] += posicaoRelativa[movimentos.index(mov)][1] #atualizando y
		
		if(distancia < (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5):
			break
		else:
			distancia = (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5	
			pos+=1	

	if pos  == QTDMOVIMENTOS:
		return randint(0,pos-1);
	return pos

def gerarNovoIndividuo():	
	global individuo, posFruta, posicaoRelativa, movimentos, QTDMOVIMENTOS
	novoIndividuo = individuo[0:]
	#fazer 1 mutação no primeiro individuo
	pos = getPosPrimeiroSuspeito(individuo)
	novoIndividuo[pos] = movimentos[getMelhorMovimento(individuo, pos)]
	
	
	#fazer crossover	
	individuoFilho1 = novoIndividuo[0:]
	
	#fazer 1 mutação no primeiro individuo
	
	novoIndividuo[getPosPrimeiroSuspeito(individuo)] = movimentos[randint(0,7)]
	
	individuoFilho2 = novoIndividuo[0:]
	
	
	
	if fitness(individuoFilho1) > fitness(individuoFilho2):
		individuo = individuoFilho1[0:]
	else:
		individuo = individuoFilho2[0:]
		
	
		
	
	
	
	

def main():
	global individuo, solucaoEncontrada, movimentos, QTDMOVIMENTOS
	
	#gerar primeiro indivíduo aleatório
	for i in range(QTDMOVIMENTOS):
		individuo.append(str(movimentos[randint(0,7)]))
	
	# buscar solução
	geracao = 0	
	while(not solucaoEncontrada):
		print('ger.: '+str(geracao)+' Individuo: '+str(individuo) + ' fitness: '+str(fitness(individuo)))	
		gerarNovoIndividuo()
		geracao+=1
	
	#exibir solução
	print('\n___________________________________________\n')
	print('ger.: '+str(geracao)+' Individuo: '+str(individuo) + ' fitness: '+str(fitness(individuo)))

if __name__ == '__main__':
	main()