import pygame

corBranca = (255,255,255)
corVermelha = (255,0,0)
corVerde = (0,255,0)

movimentos = ['←','↑','→','↓','↖','↗','↘','↙']
posicaoRelativa = [[-1,0],[0,-1],[1,0],[0,1],[-1,-1],[1,-1],[1,1],[-1,1]]

def simular(tamTabuleiro, posIndividuo, posFruta, sequenciaPassos):

    global movimentos, posicaoRelativa

    try:
        pygame.init()
    except:
        print('o modulo pygame não foi inicializado corretamente')

    largura = 450
    altura = 450 

    tam_bloco_x = largura // tamTabuleiro[0]
    tam_bloco_y = altura // tamTabuleiro[1]
   
    fundo = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('pacman simulação')

    #definições do pacman
    tamanho = (tam_bloco_x + tam_bloco_y)//2
    pos_x = posIndividuo[0] * tam_bloco_x
    pos_y = posIndividuo[1] * tam_bloco_y

    sair = True
   
    relogio = pygame.time.Clock()
    while sair:
               
        for mov in sequenciaPassos:             
          
            #atualizar x
            pos_x += posicaoRelativa[movimentos.index(mov)][0] * tamanho
            pos_y += posicaoRelativa[movimentos.index(mov)][1] * tamanho
            pygame.draw.rect(fundo, corVerde,[pos_x,pos_y,tamanho,tamanho])
            pygame.draw.rect(fundo, corVermelha,[posFruta[0] * tam_bloco_x,posFruta[1] * tam_bloco_y,tamanho,tamanho])
        
    
            pygame.display.update()
            
            fundo.fill(corBranca)
           
            relogio.tick(5)
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:                    
                    finalizar()

            

        #redefinir posição inicial
        pos_x = posIndividuo[0] * tam_bloco_x
        pos_y = posIndividuo[1] * tam_bloco_y    

def finalizar():
    pygame.quit()


