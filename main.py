#Algoritmo genético by Wilton
#simulação jogo pacman


from random import randint

movimentos = ['←','↑','→','↓','↖','↗','↘','↙']
posicaoRelativa = [[-1,0],[0,-1],[1,0],[0,1],[-1,-1],[1,-1],[1,1],[-1,1]]

#definição do ambiente e quantidade de movimentos (genes)
QTDMOVIMENTOS = 0 #valor definido na função main baseado no calculo da distância de manhattan
TAMTABULEIRO = [5,5] #definição da matriz do jogo.

solucaoEncontrada = False
QTDMOVIMENTOSSOLUCAO = 0
individuo = []

'''
	orientações do tabuleiro 5X5 

	Y
	--------------------------------
 X |(0,0) (1,0) (2,0)  (3,0)  (4,0) |
   |(0,1) (1,1) (2,1)  (3,1)  (4,1) |
   |(0,2) (1,2) (2,2)  (3,2)  (4,2)	|
   |(0,3) (1,3) (2,3)  (3,3)  (4,3)	|
   |(0,4) (1,4) (2,4)  (3,4)  (4,4)	|
    ---------------------------------	

'''
#posições dos elementos do jogo (pacman, fruta)
posInicialIndividuo= [2,4] #posição do pacman
posFruta = [3,3]  #posição da fruta



def verificaConfiguracao():
	#função para verificar se as posições dos elementos e o tamanho do tabuleiro são válidas
	if(posInicialIndividuo[0]>=0 and posInicialIndividuo[1]>=0 and posFruta[0] >= 0 and posFruta[1] >=0 and TAMTABULEIRO[0] > posInicialIndividuo[0] and TAMTABULEIRO[1] > posInicialIndividuo[1] and TAMTABULEIRO[0] > posFruta[0] and TAMTABULEIRO[1] > posFruta[1]):
		return True
	else: return False

def verificaSolucao():

	global  individuo, posFruta, posicaoRelativa, movimentos, solucaoEncontrada, posInicialIndividuo, QTDMOVIMENTOSSOLUCAO
	
	count = 0
	#calcula a posição final do individuo
	posFinalIndividuo=posInicialIndividuo[0:]
	distancia = (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5	
	QTDMOVIMENTOSSOLUCAO = 0
	for mov in individuo:
		QTDMOVIMENTOSSOLUCAO+=1
		#verifica colisão nas bordas do tabuleiro		
		if (posFinalIndividuo[0] + posicaoRelativa[movimentos.index(mov)][0] >= 0) and (posFinalIndividuo[1] + posicaoRelativa[movimentos.index(mov)][1] >= 0) and (posFinalIndividuo[0] + posicaoRelativa[movimentos.index(mov)][0] < TAMTABULEIRO[0]) and (posFinalIndividuo[1] + posicaoRelativa[movimentos.index(mov)][1] < TAMTABULEIRO[1]): 
			
			
			posFinalIndividuo[0] += posicaoRelativa[movimentos.index(mov)][0] #atualizando x
			posFinalIndividuo[1] += posicaoRelativa[movimentos.index(mov)][1] #atualizando y
			
			if(distancia > (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5):
		
				distancia = (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5	
				count+=1	
			if(distancia == 0 and (count == QTDMOVIMENTOSSOLUCAO)):
				print('SOLUÇÃO ENCONTRADA!')
				solucaoEncontrada = True
				break
			

def fitness(indv):
	#O fitness é a quantidade de movimentos que "contribui" para chegar no objetivo (fruta)

	global  posFruta, posicaoRelativa, movimentos, solucaoEncontrada, posInicialIndividuo
	
	count = 0
	#calcula a posição final do individuo
	posFinalIndividuo=posInicialIndividuo[0:]
	distancia = (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5	
	
	for mov in indv:	
		#verifica colisão nas bordas do tabuleiro		
		if (posFinalIndividuo[0] + posicaoRelativa[movimentos.index(mov)][0] >= 0) and (posFinalIndividuo[1] + posicaoRelativa[movimentos.index(mov)][1] >= 0) and (posFinalIndividuo[0] + posicaoRelativa[movimentos.index(mov)][0] < TAMTABULEIRO[0]) and (posFinalIndividuo[1] + posicaoRelativa[movimentos.index(mov)][1] < TAMTABULEIRO[1]): 
			
			
			posFinalIndividuo[0] += posicaoRelativa[movimentos.index(mov)][0] #atualizando x
			posFinalIndividuo[1] += posicaoRelativa[movimentos.index(mov)][1] #atualizando y
			
			if(distancia > (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5):
		
				distancia = (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5	
				count+=1	
			
		
		
	return count	


def getMelhorMovimento(indv, pos):
	global  posFruta, posicaoRelativa, movimentos, QTDMOVIMENTOS, posInicialIndividuo
	melhorMovimento = 0
	posFinalIndividuo=posInicialIndividuo[0:]
	distancia = (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5	 
	for m in movimentos:
		indv = indv[0:pos-1]+[m]+indv[pos:QTDMOVIMENTOS-1]
		for mov in indv:
			#verifica colisão nas bordas do tabuleiro		
			if (posFinalIndividuo[0] + posicaoRelativa[movimentos.index(mov)][0] >= 0) and (posFinalIndividuo[1] + posicaoRelativa[movimentos.index(mov)][1] >= 0) and (posFinalIndividuo[0] + posicaoRelativa[movimentos.index(mov)][0] < TAMTABULEIRO[0]) and (posFinalIndividuo[1] + posicaoRelativa[movimentos.index(mov)][1] < TAMTABULEIRO[1]): 
			
				posFinalIndividuo[0] += posicaoRelativa[movimentos.index(mov)][0] #atualizando x
				posFinalIndividuo[1] += posicaoRelativa[movimentos.index(mov)][1] #atualizando y
			
			
		if(distancia > (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5):
			melhorMovimento = movimentos.index(mov)
			distancia = (((posFruta[0]-posFinalIndividuo[0])**2) + ((posFruta[1]-posFinalIndividuo[1])**2))** 0.5	
		
	return melhorMovimento	
			

def getPosPrimeiroSuspeito(indv):
	global  posFruta, posicaoRelativa, movimentos, posInicialIndividuo
	pos = 0
	posFinalIndividuo=posInicialIndividuo[0:]
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
	#fazer 1 mutação 
	pos = getPosPrimeiroSuspeito(individuo)
	novoIndividuo[pos] = movimentos[getMelhorMovimento(individuo, pos)]
	
	
	#Gerar filho 1
	individuoFilho1 = novoIndividuo[0:]	
	#fazer 1 mutação 	
	novoIndividuo[randint(getPosPrimeiroSuspeito(individuo), QTDMOVIMENTOS-1)] = movimentos[randint(0,7)]
	
	#gerar filho 2
	individuoFilho2 = novoIndividuo[0:]
	
	#fazer mutação no filho 2 caso tenham mesmo fitness
	if fitness(individuoFilho1) == fitness(individuoFilho2):
		individuoFilho2[randint(0,QTDMOVIMENTOS-1)] = movimentos[randint(0,7)]
	
	#retorna o novo individuo com o melhor fitness
	if fitness(individuoFilho1) > fitness(individuoFilho2):
		individuo = individuoFilho1[0:]
	else:
		individuo = individuoFilho2[0:]
		
	
		
	
	
	
	

def main():
	global individuo, solucaoEncontrada, movimentos, QTDMOVIMENTOS, QTDMOVIMENTOSSOLUCAO
	
	if(verificaConfiguracao()):

		#definição da quantidade de movimentos mínimos
		QTDMOVIMENTOS = abs(posFruta[0] - posInicialIndividuo[0]) + abs(posFruta[1] - posInicialIndividuo[1]) 
		QTDMOVIMENTOSSOLUCAO = QTDMOVIMENTOS
		#gerar primeiro indivíduo aleatório
		for i in range(QTDMOVIMENTOS):
			individuo.append(str(movimentos[randint(0,7)]))
		
		# buscar solução
		geracao = 0	
		while(not solucaoEncontrada):
			print('ger.: '+str(geracao)+' Indv.: '+str(individuo) + ' fit: '+str(fitness(individuo))+' stp: '+str(QTDMOVIMENTOSSOLUCAO))	
			gerarNovoIndividuo()
			verificaSolucao()
			geracao+=1
		
		#exibir solução
		print('\n___________________________________________\n')
		print('ger.: '+str(geracao)+' Indv.: '+str(individuo[0:QTDMOVIMENTOSSOLUCAO]) + ' fit: '+str(fitness(individuo))+' stp: '+str(QTDMOVIMENTOSSOLUCAO))
	else:
		print('posições dos objetos inválidas!')
if __name__ == '__main__':
	main()
