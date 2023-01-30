# -------------------------------------------------- BIBLIOTECAS-----------------------------------------------
import PySimpleGUI as sg
import pygame as pg
import numpy as np
import time
from sys import exit

# -------------------------------------------------- FUNÇÕES--------------------------------------------------




# automato GLIDER
def Glider():
    celula[11,68] = 1
    celula[10,70] = 1
    celula[11,70] = 1
    celula[12,70] = 1
    celula[12,69] = 1

# automato PULSAR
def Pulsar():
    celula[82,84] = 1
    celula[82,85] = 1
    celula[82,86] = 1
    celula[82,90] = 1
    celula[82,91] = 1
    celula[82,92] = 1
    celula[87,84] = 1
    celula[87,85] = 1
    celula[87,86] = 1
    celula[87,90] = 1
    celula[87,91] = 1
    celula[87,92] = 1
    celula[89,84] = 1
    celula[89,85] = 1
    celula[89,86] = 1
    celula[89,90] = 1
    celula[89,91] = 1
    celula[89,92] = 1
    celula[94,84] = 1
    celula[94,85] = 1
    celula[94,86] = 1
    celula[94,90] = 1
    celula[94,91] = 1
    celula[94,92] = 1
    celula[84,82] = 1
    celula[85,82] = 1
    celula[86,82] = 1
    celula[90,82] = 1
    celula[91,82] = 1
    celula[92,82] = 1
    celula[84,87] = 1
    celula[85,87] = 1
    celula[86,87] = 1
    celula[90,87] = 1
    celula[91,87] = 1
    celula[92,87] = 1
    celula[84,89] = 1
    celula[85,89] = 1
    celula[86,89] = 1
    celula[90,89] = 1
    celula[91,89] = 1
    celula[92,89] = 1
    celula[84,94] = 1
    celula[85,94] = 1
    celula[86,94] = 1
    celula[90,94] = 1
    celula[91,94] = 1
    celula[92,94] = 1

# automato GOSPER GLIDER GUN
def Gosper_Glider_Gun():
    celula[26,2] = 1
    celula[24,3] = 1
    celula[26,3] = 1
    celula[14,4] = 1
    celula[15,4] = 1
    celula[22,4] = 1
    celula[23,4] = 1
    celula[36,4] = 1
    celula[37,4] = 1
    celula[13,5] = 1
    celula[17,5] = 1
    celula[22,5] = 1
    celula[23,5] = 1
    celula[36,5] = 1
    celula[37,5] = 1
    celula[2,6] = 1
    celula[3,6] = 1
    celula[12,6] = 1
    celula[18,6] = 1
    celula[22,6] = 1
    celula[23,6] = 1
    celula[2,7] = 1
    celula[3,7] = 1
    celula[12,7] = 1
    celula[16,7] = 1
    celula[18,7] = 1
    celula[19,7] = 1
    celula[24,7] = 1
    celula[26,7] = 1
    celula[12,8] = 1
    celula[18,8] = 1
    celula[26,8] = 1
    celula[13,9] = 1
    celula[17,9] = 1
    celula[14,10] = 1
    celula[15,10] = 1

# automato REPLICATOR(Para a construção dele usamos um automato que é predecessor do REPLICATOR)
def Pre_Replicator():
    celula[40,70]=1
    celula[40,69]=1
    celula[40,68]=1
    celula[41,67]=1
    celula[42,67]=1
    celula[43,67]=1
  
# automato THE BOMBER(Para a construção dele usamos um automato que é predecessor do BOMBER)
def Bomber():
    celula[60,20] = 1
    celula[60,19] = 1
    celula[60,18] = 1
    celula[61,17] = 1
    celula[62,17] = 1
    celula[63,17] = 1
    celula[69,20] = 1
    celula[69,21] = 1
    celula[69,22] = 1




# Criando a borda para a célula não "atravessar" o mapa e chegar ao outro lado, como se estivesse dando uma volta
def criarBorda():
    if celula[x, y] == 1 and (x == 99 or x == 1 or y == 1 or y == 99):
        prox_celula[x, y] = 0


# NA REGRA B3/S23
def Regra_B3S23():

    
    # Regra 1: Uma célula morta com exatamente 3 vizinhas vivas, "revive"
        
    if celula[x, y] == 0 and numero_vizinhos == 3:
        prox_celula[x, y] = 1

    # Regra 2: Uma célula viva com menos de 2 ou mais de 3 vivas, "morre"
    elif celula[x, y] == 1 and (numero_vizinhos < 2 or numero_vizinhos > 3):
        prox_celula[x,y] = 0

# REGRA B36/S23:

def Regra_B36S23():
    
    

    # Regra 1: Uma célula morta com exatamente 3 vizinhas vivas ou 6 vizinhas vivas, "revive"
    if celula[x, y] == 0 and (numero_vizinhos == 3 or numero_vizinhos == 6):
        prox_celula[x, y] = 1

    # Regra 2: Uma célula viva com menos de 2 ou mais de 3 vivas, "morre"
    elif celula[x, y] == 1 and (numero_vizinhos < 2 or numero_vizinhos > 3):
        prox_celula[x,y] = 0

# Função que utiliza as opções escolhidas pelo usuário
def info():
 if(lista[0] == True):
    
    

    if(lista[4] == True):
        Glider()
    if(lista[5] == True):
        Pulsar()
    if(lista[6] == True):
        Gosper_Glider_Gun()
    if(lista[4] == True and lista[5] == True):
        Glider()
        Pulsar()
    if(lista[4] == True and lista[6] == True):
        Gosper_Glider_Gun()
        Glider()
    if(lista[5]==True and lista[6] == True):
        Gosper_Glider_Gun()
        Pulsar()
    if(lista[4]==True and lista[5] == True and lista[6] == True):
        Gosper_Glider_Gun
        Glider()
        Pulsar()
  

 elif(lista[1] == True):
    
        
    if(lista[4] == True):
        Pre_Replicator()
        
    if(lista[5] == True):
        Bomber()
    if(lista[4] == True and  lista[5] == True):
        Bomber()
        Pre_Replicator()

# --------------------------------------------- TELA - INTERAÇÃO USUÁRIO----------------------------------------------



def Iniciar():
    
    sg.theme('GreenTan')

    layout = [

        [sg.Text('                                            BEM VINDO AO JOGO DA VIDA!!!',text_color='Green')],
        #[sg.Text('')],
        [sg.Text('Escolha a regra do jogo:')],
        [sg.Radio('B3S23 (Nascer 3, Permanecer vivo 2 e 3)','id_regra',key = 'B3S23'),sg.Radio('B36S23 (Nascer 3 e 6, Permanecer vivo 2 e 3)','id_regra',key = 'B36S23')],
        #[sg.Text('')],
        [sg.Button('Enter')]
    ]

    return sg.Window('Jogo da vida', layout = layout ,size=(600,140), finalize= True)

def Borda():
    sg.theme('GreenTan')

    layout = [

        
        [sg.Text('Adicionar Borda? ')],
        [sg.Text('(Caso marque a opção "sim" as células não poderão ultrapassar o limite do mapa.)')],
        [sg.Radio('Sim','id_borda',key = 'S'),sg.Radio('Não','id_borda',key = 'N')],
        [sg.Button('Enter')]
    ]

    return sg.Window('Jogo da vida', layout = layout ,size=(520,140), finalize= True)

def Automatos_B3S23():
    
    sg.theme('GreenTan')

    layout = [

        [sg.Text('Escolha o tipo de autômato(é permitido marcar mais de uma opção):')],
        [sg.Text()],
        [sg.Checkbox('Glider (pequena nave espacial)', key = 'glider')],
        [sg.Checkbox('Pulsar (oscilador com período 3)', key = 'pulsar')],
        [sg.Checkbox('Gosper Glider Gun (é um padrão que produz um glider na 15a. geração, um outro na 30a., e assim por diante)', key = 'gosper')],
        [sg.Text("")],
        [sg.Button('Enter')]
    ]

    return sg.Window('Jogo da vida', layout = layout ,size=(700,220), finalize= True)

def Automatos_B36S23():

    sg.theme('GreenTan')

    layout = [

        [sg.Text('Escolha o tipo de autômato(é permitido marcar mais de uma opção):')],
        [sg.Text('')],
        [sg.Checkbox('Replicator (faz cópias dele mesmo ao longo de uma linha diagonal)', key = 'replicator')],
        [sg.Checkbox('Bomber (é uma nave espacial baseada no comportamento do Replicator)', key = 'bomber')],
        [sg.Text("")],
        [sg.Button('Enter')]

    ]

    return sg.Window('Jogo da vida', layout = layout ,size=(550,200), finalize= True)




janela_iniciar,janela_B3S23,janela_B36S23,janela_borda= Iniciar(),None,None,None

lista = []




while True:
    
    window , event , values = sg.read_all_windows()     
    
   

   
    if window == janela_iniciar and event == sg.WIN_CLOSED:
        break

   
    if window == janela_iniciar and event == 'Enter':
        regra_B3S23 = values['B3S23']
        regra_B36S23 = values['B36S23']
        

        lista.append(regra_B3S23)
        lista.append(regra_B36S23)
        
        janela_borda = Borda()
        janela_iniciar.hide()

        
    
    if window == janela_borda and event == sg.WIN_CLOSED:
        break

   
    if window == janela_borda and event == 'Enter':
        borda_ativada = values['S']
        borda_desativada = values['N']
        

        lista.append(borda_ativada)
        lista.append(borda_desativada)
        

        

        if(lista[0] == True):
            
            janela_B3S23 = Automatos_B3S23()
            janela_borda.hide()

        elif(lista[1] == True):
            
            janela_B36S23 = Automatos_B36S23()
            janela_borda.hide()
        
        

    if window == janela_B3S23 and event == sg.WIN_CLOSED:
        break

   
    if window == janela_B3S23 and event == 'Enter':
        automato_glider = values['glider']
        automato_pulsar = values['pulsar']
        automato_Gosper = values['gosper']
        

        lista.append(automato_glider)
        lista.append(automato_pulsar)
        lista.append(automato_Gosper)

        
        janela_B3S23.hide()
        break
        
      
       
        

    if window == janela_B36S23 and event == sg.WIN_CLOSED:
        break

    if window == janela_B36S23 and event == 'Enter':
        automato_replicator = values['replicator']
        automato_bomber = values['bomber']
        lista.append(automato_replicator)
        lista.append(automato_bomber)
        
        
        janela_B36S23.hide()
        break
        
       
        
        

    

        



# --------------------------------------------- TELA - AUTÔMATOS -----------------------------------------------------

pg.init()


#tamanho da tela
largura, altura = 500,500

# criação da tela
tela = pg.display.set_mode((altura, largura))

# cor do fundo 
cor_fundo = 18, 10, 143

# pintando o fundo na cor escolhida
tela.fill(cor_fundo)

# quantidades de quadrados no eixo x e no eixo y
qtd_quadrados_x, qtd_quadrados_y = 100, 100

# dimensão célula "largura"
dimensao_largura = largura / qtd_quadrados_x
# dimensão célula "altura"
dimensao_altura = altura / qtd_quadrados_y

# Estado das células. (Vivas = 1; Mortas = 0;)
celula = np.zeros((qtd_quadrados_x,qtd_quadrados_y))

info()


            


#ciclo de ejecução dos autômatos
while True:

 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    pg. event. get()

    # faz uma cópia do estado atual do jogo
    prox_celula = np.copy(celula)

    
    tela.fill(cor_fundo)
    
    # fazendo um delay para melhor visualização
    time.sleep(0.1)

    
    for y in range(0,qtd_quadrados_x):
        for x in range(0,qtd_quadrados_y):

            
            # Ativar a borda caso o usuário queira
            if(lista[2] == True):
                criarBorda()
            
            # Calcular o número de vizinhos em volta(emcima ,embaixo,esquerda, etc ....)
            # usaremos o "módulo"(%, o resto) pois queremos que a célula consiga "dar a volta" no mapa
            numero_vizinhos = celula[(x - 1) % qtd_quadrados_x, (y - 1) % qtd_quadrados_y ] + \
                              celula[(x)    %  qtd_quadrados_x, (y - 1) % qtd_quadrados_y ] + \
                              celula[(x + 1) % qtd_quadrados_x, (y - 1) % qtd_quadrados_y ] + \
                              celula[(x - 1)  % qtd_quadrados_x, (y)    %  qtd_quadrados_y ] + \
                              celula[(x + 1)  % qtd_quadrados_x, (y)    %  qtd_quadrados_y ] + \
                              celula[(x - 1)  % qtd_quadrados_x, (y + 1) % qtd_quadrados_y ] + \
                              celula[(x)     % qtd_quadrados_x, (y + 1) %  qtd_quadrados_y ] + \
                              celula[(x + 1) % qtd_quadrados_x, (y + 1) % qtd_quadrados_y ] 
            
            
            
            #Regras
            if(lista[0] == True):
                Regra_B3S23()

            elif(lista[1] == True):
                Regra_B36S23()
                
                
        
            
            # definindo os lados do polígono(criando o quadradinho)
            
            poligono = [((x)   * dimensao_largura,  (y) * dimensao_altura),
                    ((x+1) * dimensao_largura,  (y) * dimensao_altura),
                    ((x+1) * dimensao_largura, (y+1) * dimensao_altura),
                    ((x)   * dimensao_largura, (y+1) * dimensao_altura)]
            
            # pintando a celula de acordo com o seu estado
            if prox_celula[x, y] == 0:
                pg.draw.polygon(tela,(128,128,128), poligono, 1)
            else:
                pg.draw.polygon(tela,(255,255,255), poligono, 0)
    
   

    # Atualizando o estado do jogo
    
    celula = np.copy(prox_celula)
    
    # função que atualiza sempre a cena em cada interação do loop
    pg.display.flip()